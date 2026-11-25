"""
AI Repair Manual, OBD-II DTC, Sensor Spec & Wiring Assistant Service (Pilar 2)
==============================================================================
Project Bengkel Masa Depan (FastAPI + Async SQLAlchemy 2.0)

Fitur Utama:
1. Hybrid RAG Search (`RepairManual`): Pencarian buku manual perbaikan berdasarkan merk,
   model, kata kunci gejala, atau tag teknis dengan peringkat relevansi.
2. Lookup & Analisis Kode DTC OBD-II (`DTCCode`): Penjelasan kode (misal P0300, P0335),
   tingkat keparahan (severity), penyebab umum, dan korelasi otomatis ke spesifikasi sensor terkait.
3. Database Spesifikasi Sensor (`SensorSpec`): Standar voltase idle/WOT, tahanan (Ohm),
   dan konfigurasi pin (TPS, MAP, O2, CKP/CMP).
4. Wiring Diagram & Pinout ECU Viewer (`WiringDiagram`): Detail konektor ECU, warna kabel,
   jalur power +12V / 5V reference, dan lokasi titik massa (ground) bodi/mesin.
5. Unified AI Assistant Endpoint (`/api/v1/manuals/ask-assistant`): Menggabungkan konteks
   Manual + DTC + Sensor Spec + Wiring Pinout menjadi jawaban terstruktur siap pakai bagi mekanik.
"""

import base64
import io
import json
import re
from pathlib import Path
from typing import Any, Sequence

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user, get_db
from app.models import DTCCode, RepairManual, SensorSpec, User, WiringDiagram
from app.services.admin_guard import require_workshop_pin
from app.services.modern_dtc_catalog import lookup_modern_dtc
from app.services.vehicle_applicability import (
    VEHICLE_GENERATION_CATALOG,
    CustomManualPackSummary,
    VehicleApplicabilityInfo,
    build_engine_directory,
    delete_custom_manual_pack,
    get_custom_manual_pack_by_id,
    list_all_manual_pack_summaries,
    load_custom_manual_packs,
    resolve_vehicle_applicability,
    save_custom_manual_pack,
)

# ---------------------------------------------------------------------------
# 1. PYDANTIC V2 SCHEMAS
# ---------------------------------------------------------------------------


class DTCCodeOut(BaseModel):
    code: str
    system: str
    description_id: str
    possible_causes: list[str]
    recommended_fix: str | None = None
    severity_level: str


class SensorSpecOut(BaseModel):
    id: int
    brand: str
    model: str
    sensor_name: str
    pin_configuration: str
    voltage_idle: str
    voltage_wot: str
    resistance_ohm: str
    testing_notes: str


class WiringPinoutItem(BaseModel):
    pin_code: str
    wire_color: str
    function: str


class WiringDiagramOut(BaseModel):
    id: int
    brand: str
    model: str
    year_range: str
    system_name: str
    ecu_connector_code: str
    pinouts: list[WiringPinoutItem]
    ground_locations: str
    diagram_image_url: str | None = None


class RepairManualChunkOut(BaseModel):
    id: int
    brand: str
    model: str
    section_title: str
    content_text: str
    tags: list[str]
    relevance_score: float


class RAGAssistantQuery(BaseModel):
    query: str = Field(
        ...,
        min_length=2,
        examples=["Cara cek sensor CKP Suzuki Grand Vitara J20A kode P0335 dan warna kabel pinout ECU"],
        description="Pertanyaan teknis mekanik (bisa memuat merk, model, gejala, sensor, atau kode DTC)",
    )
    brand: str | None = Field(default=None, examples=["Suzuki"])
    model: str | None = Field(default=None, examples=["Grand Vitara"])
    dtc_code: str | None = Field(default=None, examples=["P0335"])
    pack_id: str | None = Field(
        default=None,
        examples=["suzuki_ertiga_gen1_2012_2017"],
        description="ID Buku Manual aktif yang dipilih mekanik (mis. suzuki_jb420_builtin, suzuki_ertiga_gen1_2012_2017, universal)",
    )
    engine_code: str | None = Field(
        default=None,
        examples=["1TR-FE"],
        description="Opsional kode mesin spesifik pada manual multi-mesin (mis. 1TR-FE, 2KD-FTV, K3-VE)",
    )

    def __init__(self, **data):
        if "question" in data and "query" not in data:
            data["query"] = data["question"]
        super().__init__(**data)


class RAGAssistantResponse(BaseModel):
    query: str
    detected_dtc_codes: list[str]
    synthesized_guidance: str
    matched_dtc_details: list[DTCCodeOut]
    matched_sensor_specs: list[SensorSpecOut]
    matched_wiring_diagrams: list[WiringDiagramOut]
    matched_manual_sections: list[RepairManualChunkOut]


# ---------------------------------------------------------------------------
# 2. SERVICE LAYER: RAG & TECHNICAL DATA RETRIEVAL
# ---------------------------------------------------------------------------


class ManualAndWiringService:
    """Service untuk pencarian terpadu Repair Manual, DTC, Sensor Spec, dan Wiring ECU."""

    _JB420_CATALOG_CACHE: dict[str, dict[str, Any]] | None = None

    @classmethod
    def _get_jb420_dtc_catalog_map(cls) -> dict[str, dict[str, Any]]:
        if cls._JB420_CATALOG_CACHE is not None:
            return cls._JB420_CATALOG_CACHE
        catalog_path = Path(__file__).resolve().parent.parent / "jb420_extracted_catalog.json"
        mapping: dict[str, dict[str, Any]] = {}
        if catalog_path.exists():
            try:
                data = json.loads(catalog_path.read_text(encoding="utf-8"))
                for item in data.get("dtc_catalog", []):
                    c = str(item.get("code", "")).strip().upper()
                    if c:
                        mapping[c] = item
            except Exception:
                mapping = {}
        cls._JB420_CATALOG_CACHE = mapping
        return mapping

    @staticmethod
    def _extract_tokens(text: str) -> list[str]:
        cleaned = re.sub(r"[^a-zA-Z0-9\s-]", " ", (text or "").lower())
        return [tok for tok in cleaned.split() if len(tok) >= 2]

    @staticmethod
    def _extract_dtc_from_text(text: str, explicit_dtc: str | None = None) -> list[str]:
        combined = f"{text or ''} {explicit_dtc or ''}".upper()
        found: list[str] = []
        for m in re.findall(r"\b[PCBU][0-9A-F]{4}\b", combined):
            if m not in found:
                found.append(m)
        for m_kls in re.findall(r"\bKLS[-\s]?([0-9]{2})\b", combined):
            k_code = f"KLS-{m_kls}"
            if k_code not in found:
                found.append(k_code)
        for m_num in re.findall(r"\bDTC\s*(?:NO\.?\s*)?([1-5][0-9])\b", combined):
            k_code = f"KLS-{m_num}"
            if k_code not in found:
                found.append(k_code)
        # Dukung kode DTC Toyota non-OBD (Audio/AC/Navigasi/Airbag format XX-XX, mis. 01-21, 60-10, 44-41, 01-E0)
        for m_toy in re.findall(r"\b([0-9]{2}-[0-9A-F]{2})\b", combined):
            if m_toy not in found:
                found.append(m_toy)
        return found

    @classmethod
    async def lookup_dtc_codes(
        cls, session: AsyncSession, codes: Sequence[str]
    ) -> list[DTCCodeOut]:
        if not codes:
            return []
        normalized = [c.strip().upper() for c in codes if c.strip()]
        stmt = select(DTCCode).where(DTCCode.code.in_(normalized))
        rows = (await session.execute(stmt)).scalars().all()
        row_map = {r.code.upper(): r for r in rows}

        results: list[DTCCodeOut] = []
        for c in normalized:
            row = row_map.get(c)
            if not row:
                continue
            causes = [
                line.strip()
                for line in re.split(r"[\n|]+", (row.possible_causes or ""))
                if line.strip()
            ]
            results.append(
                DTCCodeOut(
                    code=row.code,
                    system=row.system,
                    description_id=row.description_id,
                    possible_causes=causes,
                    recommended_fix=row.recommended_fix,
                    severity_level=row.severity_level,
                )
            )
        return results

    @classmethod
    async def search_sensor_specs(
        cls,
        session: AsyncSession,
        brand: str | None = None,
        model: str | None = None,
        sensor_keyword: str | None = None,
    ) -> list[SensorSpecOut]:
        stmt = select(SensorSpec)
        conditions = []
        if brand:
            conditions.append(
                or_(
                    SensorSpec.brand.ilike(f"%{brand}%"),
                    SensorSpec.brand.ilike("%Universal%"),
                )
            )
        if model:
            conditions.append(
                or_(
                    SensorSpec.model.ilike(f"%{model}%"),
                    SensorSpec.brand.ilike("%Universal%"),
                )
            )
        if sensor_keyword:
            conditions.append(
                or_(
                    SensorSpec.sensor_name.ilike(f"%{sensor_keyword}%"),
                    SensorSpec.testing_notes.ilike(f"%{sensor_keyword}%"),
                )
            )
        if conditions:
            for cond in conditions:
                stmt = stmt.where(cond)

        rows = (await session.execute(stmt)).scalars().all()
        return [
            SensorSpecOut(
                id=r.id,
                brand=r.brand,
                model=r.model,
                sensor_name=r.sensor_name,
                pin_configuration=r.pin_configuration,
                voltage_idle=r.voltage_idle,
                voltage_wot=r.voltage_wot,
                resistance_ohm=r.resistance_ohm,
                testing_notes=r.testing_notes,
            )
            for r in rows
        ]

    @classmethod
    async def search_wiring_diagrams(
        cls,
        session: AsyncSession,
        brand: str | None = None,
        model: str | None = None,
        system_keyword: str | None = None,
    ) -> list[WiringDiagramOut]:
        stmt = select(WiringDiagram)
        if brand:
            stmt = stmt.where(WiringDiagram.brand.ilike(f"%{brand}%"))
        if model:
            stmt = stmt.where(WiringDiagram.model.ilike(f"%{model}%"))
        if system_keyword:
            stmt = stmt.where(
                or_(
                    WiringDiagram.system_name.ilike(f"%{system_keyword}%"),
                    WiringDiagram.ecu_connector_code.ilike(f"%{system_keyword}%"),
                )
            )

        rows = (await session.execute(stmt)).scalars().all()
        results: list[WiringDiagramOut] = []
        for r in rows:
            pinouts_list: list[WiringPinoutItem] = []
            raw_pinout: dict[str, Any] = r.pinout_json or {}
            for pin_code, detail in raw_pinout.items():
                if isinstance(detail, dict):
                    pinouts_list.append(
                        WiringPinoutItem(
                            pin_code=pin_code,
                            wire_color=str(detail.get("wire_color", "-")),
                            function=str(detail.get("function", "-")),
                        )
                    )
            results.append(
                WiringDiagramOut(
                    id=r.id,
                    brand=r.brand,
                    model=r.model,
                    year_range=r.year_range,
                    system_name=r.system_name,
                    ecu_connector_code=r.ecu_connector_code,
                    pinouts=pinouts_list,
                    ground_locations=r.ground_locations,
                    diagram_image_url=r.diagram_image_url,
                )
            )
        return results

    @classmethod
    async def retrieve_repair_manuals(
        cls,
        session: AsyncSession,
        query_text: str,
        brand: str | None = None,
        model: str | None = None,
        top_k: int = 5,
    ) -> list[RepairManualChunkOut]:
        stmt = select(RepairManual)
        if brand:
            stmt = stmt.where(RepairManual.brand.ilike(f"%{brand}%"))
        rows = (await session.execute(stmt)).scalars().all()

        core_query_tokens = set(cls._extract_tokens(query_text))
        query_tokens = set(core_query_tokens)
        if brand:
            query_tokens.update(cls._extract_tokens(brand))
        if model:
            query_tokens.update(cls._extract_tokens(model))

        scored_manuals: list[RepairManualChunkOut] = []
        for m in rows:
            doc_text = f"{m.brand} {m.model} {m.section_title} {m.content_text} {m.tags}"
            doc_tokens = set(cls._extract_tokens(doc_text))
            tag_list = [t.strip().lower() for t in (m.tags or "").split(",") if t.strip()]

            title_tokens = set(cls._extract_tokens(m.section_title or ""))
            title_hits = len(core_query_tokens.intersection(title_tokens))
            core_overlap = len(core_query_tokens.intersection(doc_tokens))
            tag_hits = len(core_query_tokens.intersection(set(tag_list)))
            if core_query_tokens and (core_overlap + tag_hits) == 0:
                continue

            is_glossary = "singkatan" in (m.content_text or "").lower() or "bab 0a" in (m.section_title or "").lower()
            glossary_penalty = -4.0 if is_glossary else 0.0
            brand_bonus = 1.0 if (brand and brand.lower() in m.brand.lower()) else 0.0
            model_bonus = 1.0 if (model and model.lower() in m.model.lower()) else 0.0

            raw_score = (core_overlap * 2.5) + (6.0 * title_hits) + (4.0 * tag_hits) + brand_bonus + model_bonus + glossary_penalty
            if raw_score <= 0 and query_tokens:
                continue

            norm_score = round(min(100.0, (raw_score / max(len(core_query_tokens), 1)) * 35.0), 1)
            scored_manuals.append(
                RepairManualChunkOut(
                    id=m.id,
                    brand=m.brand,
                    model=m.model,
                    section_title=m.section_title,
                    content_text=m.content_text,
                    tags=tag_list,
                    relevance_score=norm_score,
                )
            )

        scored_manuals.sort(key=lambda item: item.relevance_score, reverse=True)
        return scored_manuals[:top_k]

    @staticmethod
    def _clean_custom_pdf_text(raw: str) -> str:
        s = str(raw or "")
        s = re.sub(r"\)\s*\(Page\s+[^)]+\)", "", s, flags=re.IGNORECASE)
        s = s.replace("an d ", "and ").replace("O FF", "OFF").replace("di sconnect", "disconnect").replace("re lay", "relay")
        return re.sub(r"\s{2,}", " ", s).strip()

    @classmethod
    def _ask_custom_pack_rag(
        cls,
        pack: dict[str, Any],
        payload: RAGAssistantQuery,
        detected_dtcs: list[str],
    ) -> RAGAssistantResponse:
        """
        Pencarian RAG TERISOLASI secara ketat pada Buku Manual Kustom terpilih (mis. Suzuki Ertiga Gen 1 K14B/D13A).
        Menjamin ZERO kebocoran pinout/standar dari Suzuki Grand Vitara JB420 (C37/E23).
        """
        pack_title = str(pack.get("title", f"{pack.get('brand', '')} {pack.get('model', '')}")).strip()
        q_low = (payload.query or "").lower()
        q_tokens = set(cls._extract_tokens(payload.query))
        dtc_catalog: list[dict[str, Any]] = list(pack.get("dtc_catalog", []))
        sensor_specs_raw: list[dict[str, Any]] = list(pack.get("sensor_specs", []))
        wiring_pinouts_raw: list[dict[str, Any]] = list(pack.get("wiring_pinouts", []))
        eng_filter = re.sub(r"[^a-z0-9]", "", (payload.engine_code or "").lower())
        if eng_filter and len(eng_filter) >= 3:
            eng_specs = [
                sp for sp in sensor_specs_raw
                if eng_filter in re.sub(r"[^a-z0-9]", "", str(sp.get("sensor_name", "")).lower())
            ]
            if eng_specs:
                sensor_specs_raw = eng_specs
            eng_pins = [
                pw for pw in wiring_pinouts_raw
                if eng_filter in re.sub(r"[^a-z0-9]", "", str(pw.get("pin", "")).lower())
            ]
            if eng_pins:
                wiring_pinouts_raw = eng_pins

        summary_parts: list[str] = []
        matched_dtc_out: list[DTCCodeOut] = []
        matched_specs_out: list[SensorSpecOut] = []
        matched_pins_collected: list[WiringPinoutItem] = []

        # Catatan cerdas khusus K14B bila mekanik mencari MAF
        pack_engines = [str(e).upper() for e in pack.get("engine_codes", [])]
        if re.search(r"\bmaf\b|mass air flow", q_low) and "K14B" in pack_engines:
            summary_parts.append(
                f"[CATATAN ARSITEKTUR MESIN — {pack_title}]\n"
                "• Mesin Suzuki K14B (Ertiga Gen 1) TIDAK memakai MAF Sensor.\n"
                "• K14B menggunakan sistem Speed-Density berbasis MAP Sensor (C01-29 / C01-2 / C01-20) dan IAT Sensor (C01-34 / C01-20).\n"
                "• Menampilkan spesifikasi & pinout MAP + IAT resmi K14B di bawah ini:"
            )
            q_tokens.update({"map", "iat", "intake", "manifold"})

        # 1. Cocokkan Kode DTC dari paket ini
        dtc_by_code = {str(d.get("code", "")).strip().upper(): d for d in dtc_catalog if d.get("code")}
        matched_entries: list[dict[str, Any]] = []
        for code in detected_dtcs:
            if code in dtc_by_code:
                matched_entries.append(dtc_by_code[code])

        # Jika belum ada kode DTC eksplisit, cari berdasarkan kata kunci di deskripsi/penyebab DTC
        if not matched_entries and q_tokens:
            scored_dtcs: list[tuple[int, dict[str, Any]]] = []
            for d in dtc_catalog:
                hay = f"{d.get('code', '')} {d.get('description_id', '')} {d.get('common_causes', '')}".lower()
                hits = sum(1 for tok in q_tokens if tok in hay)
                if hits > 0:
                    scored_dtcs.append((hits, d))
            scored_dtcs.sort(key=lambda x: x[0], reverse=True)
            matched_entries = [x[1] for x in scored_dtcs[:3]]

        for cd in matched_entries[:4]:
            code = str(cd.get("code", "")).upper()
            desc = cls._clean_custom_pdf_text(cd.get("description_id", f"DTC {code}"))
            causes_raw = cd.get("common_causes", "")
            if isinstance(causes_raw, list):
                causes_list = [cls._clean_custom_pdf_text(c) for c in causes_raw if str(c).strip()]
            else:
                causes_list = [cls._clean_custom_pdf_text(c) for c in re.split(r"[;\n|]+", str(causes_raw)) if c.strip()]
            steps_raw = cd.get("repair_steps", [])
            steps_clean = [cls._clean_custom_pdf_text(s) for s in steps_raw if str(s).strip()]
            sev = str(cd.get("severity_level", "HIGH"))
            page_info = f" (Hal. PDF {cd['page']})" if cd.get("page") else ""

            matched_dtc_out.append(
                DTCCodeOut(
                    code=code,
                    system=pack_title,
                    description_id=desc,
                    possible_causes=causes_list[:6],
                    recommended_fix="\n".join(steps_clean[:6]),
                    severity_level=sev,
                )
            )
            steps_block = "\n".join(f"  {s}" for s in steps_clean[:5]) if steps_clean else "  Ikuti prosedur pemeriksaan manual resmi."
            summary_parts.append(
                f"[BUKU MANUAL RESMI: {pack_title} — DTC {code} ({sev})]{page_info}\n"
                f"• Deskripsi: {desc}\n"
                f"• Penyebab / Kondisi Deteksi: {'; '.join(causes_list[:5]) or '-'}\n"
                f"• Langkah Pemeriksaan:\n{steps_block}"
            )
            if cd.get("standard_specs"):
                sp_lines = "\n".join(
                    f"• {sp.get('parameter', '-')}: {sp.get('normal_range', '-')}"
                    for sp in cd["standard_specs"][:6]
                )
                summary_parts.append(f"[SPESIFIKASI STANDAR MULTIMETER — DTC {code}]\n{sp_lines}")
            if cd.get("wiring_pinout"):
                pin_lines = "\n".join(
                    f"• {p.get('pin', '-')}: {p.get('signal', '-')} — {p.get('function', '-')}"
                    for p in cd["wiring_pinout"][:8]
                )
                summary_parts.append(f"[JALUR WIRING & PINOUT RESMI — DTC {code}]\n{pin_lines}")
                for p in cd["wiring_pinout"][:8]:
                    matched_pins_collected.append(
                        WiringPinoutItem(
                            pin_code=str(p.get("pin", "-")),
                            wire_color=str(p.get("signal", "-")),
                            function=str(p.get("function", "-")),
                        )
                    )

        # 2. Cocokkan Spesifikasi Sensor dari paket ini
        sensor_aliases = {
            "koil": ["coil", "ignition", "pengapian"],
            "coil": ["koil", "ignition", "pengapian"],
            "kipas": ["fan", "radiator", "ac"],
            "fan": ["kipas", "radiator"],
            "throttle": ["tps", "etc"],
            "tps": ["throttle", "etc"],
            "pedal": ["app"],
            "suhu": ["ect", "coolant", "iat"],
            "oksigen": ["o2", "ho2s", "oxygen"],
            "o2": ["ho2s", "oxygen", "oksigen"],
            "vvt": ["ocv", "cmp", "ckp"],
            "vakum": ["map", "manifold"],
        }
        expanded_tokens = set(q_tokens)
        for t in list(q_tokens):
            expanded_tokens.update(sensor_aliases.get(t, []))
        for d in matched_entries[:2]:
            expanded_tokens.update(cls._extract_tokens(str(d.get("description_id", ""))))

        matched_spec_dicts: list[dict[str, Any]] = []
        for idx_s, sp in enumerate(sensor_specs_raw, start=1):
            hay_s = f"{sp.get('sensor_name', '')} {sp.get('pin_configuration', '')} {sp.get('voltage_idle', '')} {sp.get('voltage_wot', '')}".lower()
            if any(tok in hay_s for tok in expanded_tokens if len(tok) >= 2):
                matched_spec_dicts.append(sp)
                matched_specs_out.append(
                    SensorSpecOut(
                        id=idx_s,
                        brand=str(pack.get("brand", "")),
                        model=str(pack.get("model", "")),
                        sensor_name=str(sp.get("sensor_name", "-")),
                        pin_configuration=str(sp.get("pin_configuration", "-")),
                        voltage_idle=str(sp.get("voltage_idle", "-")),
                        voltage_wot=str(sp.get("voltage_wot", "-")),
                        resistance_ohm=str(sp.get("resistance_ohm", "-")),
                        testing_notes=str(sp.get("testing_notes", "")),
                    )
                )
        for sp in matched_spec_dicts[:2]:
            summary_parts.append(
                f"[SPESIFIKASI SENSOR RESMI — {sp.get('sensor_name', '-')}]\n"
                f"• Konfigurasi Pinout: {sp.get('pin_configuration', '-')}\n"
                f"• Tegangan Idle / KOEO: {sp.get('voltage_idle', '-')}\n"
                f"• Tegangan Kerja / WOT: {sp.get('voltage_wot', '-')}\n"
                f"• Tahanan / Suplai: {sp.get('resistance_ohm', '-')}"
            )

        # 3. Cocokkan Pinout Wiring dari paket ini (jika belum tercakup dari DTC)
        if not matched_pins_collected and wiring_pinouts_raw and expanded_tokens:
            rel_pins = [
                p for p in wiring_pinouts_raw
                if any(
                    tok in f"{p.get('pin', '')} {p.get('signal', '')} {p.get('function', '')}".lower()
                    for tok in expanded_tokens
                    if len(tok) >= 2
                )
            ]
            if rel_pins:
                pin_lines = "\n".join(
                    f"• {p.get('pin', '-')}: {p.get('signal', '-')} — {p.get('function', '-')}"
                    for p in rel_pins[:10]
                )
                summary_parts.append(
                    f"[PINOUT KONEKTOR ECM RESMI — {pack.get('brand', '')} {pack.get('model', '')}]\n{pin_lines}"
                )
                for p in rel_pins[:10]:
                    matched_pins_collected.append(
                        WiringPinoutItem(
                            pin_code=str(p.get("pin", "-")),
                            wire_color=str(p.get("signal", "-")),
                            function=str(p.get("function", "-")),
                        )
                    )

        if not summary_parts:
            sample_codes = ", ".join(str(d.get("code", "")) for d in dtc_catalog[:8] if d.get("code"))
            synthesized = (
                f"Kata kunci '{payload.query}' belum ditemukan pada buku manual aktif: {pack_title}.\n"
                f"• Total isi manual ini: {len(dtc_catalog)} kode DTC, {len(wiring_pinouts_raw)} pinout konektor, {len(sensor_specs_raw)} spesifikasi sensor.\n"
                f"• Coba cari kode DTC yang terdaftar (misal: P0300, P0107, P0117, P0122, P0130, P0335, P0480, P2135 atau {sample_codes}) "
                f"atau nama komponen (koil, map, tps, app, ect, ckp, o2, kipas, injektor, can)."
            )
        else:
            synthesized = "\n\n".join(summary_parts)

        wd_out = []
        if matched_pins_collected:
            prefixes = sorted({p.pin_code.split("-")[0] for p in matched_pins_collected if "-" in p.pin_code})
            wd_out.append(
                WiringDiagramOut(
                    id=9001,
                    brand=str(pack.get("brand", "")),
                    model=str(pack.get("model", "")),
                    year_range=f"{pack.get('year_start', '')}-{pack.get('year_end', '')}",
                    system_name=pack_title,
                    ecu_connector_code=" / ".join(prefixes) or "ECM",
                    pinouts=matched_pins_collected,
                    ground_locations="Massa utama ECM & blok mesin sesuai manual resmi",
                )
            )

        return RAGAssistantResponse(
            query=payload.query,
            detected_dtc_codes=detected_dtcs,
            synthesized_guidance=synthesized,
            matched_dtc_details=matched_dtc_out,
            matched_sensor_specs=matched_specs_out,
            matched_wiring_diagrams=wd_out,
            matched_manual_sections=[],
        )

    @classmethod
    async def ask_rag_assistant(
        cls, session: AsyncSession, payload: RAGAssistantQuery
    ) -> RAGAssistantResponse:
        """
        Mengorkestrasi pengambilan konteks teknis dari Buku Manual Resmi yang ditanamkan:
        - Jika `payload.pack_id` menunjuk ke paket manual kustom (mis. Suzuki Ertiga Gen 1),
          pencarian diisolasi 100% pada buku manual tersebut (anti-bocor pinout JB420).
        - Jika `payload.pack_id == 'suzuki_jb420_builtin'` atau kosong, menggunakan Suzuki JB420.
        - Jika `payload.pack_id == 'universal'`, memprioritaskan Katalog Universal OBD-II & Modern.
        """
        detected_dtcs = cls._extract_dtc_from_text(payload.query, payload.dtc_code)
        req_pack_id = str(payload.pack_id or "").strip()

        # Mode Terisolasi Paket Manual Kustom (Ertiga Gen 1 atau manual baru di masa depan)
        if req_pack_id and req_pack_id not in {"suzuki_jb420_builtin", "universal"}:
            custom_pack = get_custom_manual_pack_by_id(req_pack_id)
            if custom_pack:
                return cls._ask_custom_pack_rag(custom_pack, payload, detected_dtcs)

        dtc_details = await cls.lookup_dtc_codes(session, detected_dtcs)
        cat_map = cls._get_jb420_dtc_catalog_map()

        combined_hint = payload.query.lower()
        if dtc_details:
            combined_hint += " " + " ".join(
                f"{d.code} {d.description_id} {' '.join(d.possible_causes)}".lower()
                for d in dtc_details
            )

        sensor_kw = None
        module_kw = None
        for candidate in (
            "kipas", "cooling fan", "p0480", "p0481",
            "maf", "o2", "oxygen", "ho2s", "ect", "coolant", "map",
            "ckp", "cmp", "tps", "throttle", "iat", "app", "pedal",
            "coil", "ignition", "injector", "injektor", "fuel pump", "pompa bensin",
            "evap", "purge", "egr",
            "abs", "wheel speed", "e03",
            "solenoid", "tcm", "matic", "transmisi", "e92", "e93",
            "hvac", "blower", "evaporator", "suhu kabin", "g52",
            "airbag", "air bag", "srs", "sdm", "pretensioner", "g47",
            "bcm", "door lock", "power window", "wiper", "g30", "g31", "g32",
            "immobilizer", "icm", "transponder", "g24",
            "keyless", "kscm", "steering lock", "g44",
            "can",
        ):
            if candidate in combined_hint:
                if candidate in ("kipas", "cooling fan", "p0480", "p0481"):
                    sensor_kw = "fan"
                elif candidate in ("oxygen", "ho2s"):
                    sensor_kw = "o2"
                elif candidate == "coolant":
                    sensor_kw = "ect"
                elif candidate == "throttle":
                    sensor_kw = "tps"
                elif candidate == "pedal":
                    sensor_kw = "app"
                elif candidate in ("injector", "injektor"):
                    sensor_kw = "injector"
                elif candidate in ("fuel pump", "pompa bensin"):
                    sensor_kw = "fuel_pump"
                elif candidate in ("evap", "purge"):
                    sensor_kw = "evap"
                elif candidate in ("abs", "wheel speed", "e03"):
                    module_kw = "abs"
                elif candidate in ("solenoid", "tcm", "matic", "transmisi", "e92", "e93"):
                    module_kw = "tcm"
                elif candidate in ("hvac", "blower", "evaporator", "suhu kabin", "g52"):
                    module_kw = "hvac"
                elif candidate in ("airbag", "air bag", "srs", "sdm", "pretensioner", "g47"):
                    module_kw = "sdm"
                elif candidate in ("bcm", "door lock", "power window", "wiper", "g30", "g31", "g32"):
                    module_kw = "bcm"
                elif candidate in ("immobilizer", "icm", "transponder", "g24"):
                    module_kw = "icm"
                elif candidate in ("keyless", "kscm", "steering lock", "g44"):
                    module_kw = "kscm"
                else:
                    sensor_kw = candidate
                break

        spec_search_kw = (
            sensor_kw
            if sensor_kw in ("maf", "o2", "ect", "map", "ckp", "cmp", "tps", "iat", "app")
            else None
        )
        sensor_specs = (
            await cls.search_sensor_specs(
                session, brand=payload.brand, model=payload.model, sensor_keyword=spec_search_kw
            )
            if spec_search_kw
            else []
        )
        wiring_diagrams = await cls.search_wiring_diagrams(
            session, brand=payload.brand, model=payload.model
        )

        primary_cat_entry = cat_map.get(detected_dtcs[0].upper()) if detected_dtcs else None

        # Sintesis jawaban teknis HANYA mencakup:
        # (1) Penyebab & Saran Penyelesaian DTC Buku Manual, (2) Spesifikasi Standar, dan (3) Jalur Wiring & Pinout
        summary_parts: list[str] = []

        # 1. BLOK PENYEBAB & SARAN PENYELESAIAN DTC BUKU MANUAL
        if dtc_details:
            for dtc_info in dtc_details:
                c_entry = cat_map.get(dtc_info.code.upper())
                doc_ref = (
                    f" [Dokumen ID: {c_entry['suzuki_doc_id']}]"
                    if c_entry and c_entry.get("suzuki_doc_id")
                    else ""
                )
                clean_causes = [
                    c for c in dtc_info.possible_causes
                    if not c.lower().startswith("pinout & warna kabel:")
                ]
                causes_str = "; ".join(clean_causes[:4]) if clean_causes else dtc_info.description_id

                fix_lines: list[str] = []
                if c_entry and c_entry.get("remedies"):
                    remedy_summary = "; ".join(str(r).strip() for r in c_entry["remedies"][:3] if str(r).strip())
                    if remedy_summary:
                        fix_lines.append(f"• Solusi Inti Buku Manual: {remedy_summary}")
                if c_entry and c_entry.get("repair_steps"):
                    steps_preview = "\n".join(
                        f"  {s}" for s in c_entry["repair_steps"][:4] if str(s).strip()
                    )
                    if steps_preview:
                        fix_lines.append(f"• Langkah Pemeriksaan & Perbaikan:\n{steps_preview}")
                elif dtc_info.recommended_fix:
                    steps_preview = "\n".join(
                        f"  {ln.strip()}"
                        for ln in dtc_info.recommended_fix.splitlines()[:4]
                        if ln.strip()
                    )
                    if steps_preview:
                        fix_lines.append(f"• Langkah Pemeriksaan & Perbaikan:\n{steps_preview}")

                fix_block = ("\n" + "\n".join(fix_lines)) if fix_lines else ""
                summary_parts.append(
                    f"[PENYEBAB & SARAN PENYELESAIAN DTC {dtc_info.code} — {dtc_info.severity_level}]\n"
                    f"• Deskripsi: {dtc_info.description_id}\n"
                    f"• Buku Pedoman: {dtc_info.system}{doc_ref}\n"
                    f"• Area Masalah / Penyebab: {causes_str}"
                    f"{fix_block}"
                )

        # 2. BLOK SPESIFIKASI STANDAR PEMERIKSAAN (SENSOR / AKTUATOR / MODUL)
        if sensor_specs:
            sp = sensor_specs[0]
            notes_str = f"\n• Catatan Pemeriksaan: {sp.testing_notes}" if sp.testing_notes else ""
            summary_parts.append(
                f"[SPESIFIKASI SENSOR {sp.sensor_name} ({sp.brand} {sp.model})]\n"
                f"• Konfigurasi Pinout: {sp.pin_configuration}\n"
                f"• Tegangan Idle: {sp.voltage_idle}\n"
                f"• Tegangan Kerja/WOT: {sp.voltage_wot}\n"
                f"• Standar Tahanan: {sp.resistance_ohm}"
                f"{notes_str}"
            )
        elif sensor_kw == "fan":
            summary_parts.append(
                "[SPESIFIKASI SIRKUIT KONTROL KIPAS RADIATOR (Suzuki Grand Vitara JB420 Bab 1A-133 & 1A-233)]\n"
                "• Konfigurasi Pinout: E23-46 (RED/BLK): Relay Kipas No.1 | E23-47 (RED): Relay Kipas No.2 | C37-24 (PPL/YEL): Sinyal Suhu ECT\n"
                "• Tegangan Kipas OFF (Standby IG ON): 10.0 - 14.0 V pada terminal E23-46 / E23-47\n"
                "• Tegangan Kipas ON (ECT ≥ 97.5°C / AC ON): 0.0 - 1.5 V (Ground Switched oleh ECM)\n"
                "• Standar Tahanan Koil Relay: 60 - 120 Ohm (pada 20°C)"
            )
        elif primary_cat_entry and primary_cat_entry.get("standard_specs"):
            spec_lines = "\n".join(
                f"• {sp_i.get('parameter', 'Pemeriksaan')}: {sp_i.get('normal_range', '-')}"
                for sp_i in primary_cat_entry["standard_specs"][:5]
            )
            summary_parts.append(
                f"[SPESIFIKASI STANDAR PEMERIKSAAN BUKU MANUAL — DTC {primary_cat_entry['code']}]\n"
                f"{spec_lines}"
            )
        elif module_kw or dtc_details:
            eff_mod = module_kw
            if not eff_mod and detected_dtcs:
                c0 = detected_dtcs[0]
                if c0.startswith("C10"):
                    eff_mod = "abs"
                elif c0.startswith(("P07", "P09", "P17", "P18", "P27")):
                    eff_mod = "tcm"
                elif c0.startswith("B15"):
                    eff_mod = "hvac"
                elif c0.startswith("B10"):
                    eff_mod = "sdm"
                elif c0.startswith("B11"):
                    eff_mod = "bcm"
                elif c0.startswith("P161") or c0 in {"P1610", "P1614", "P1615", "P1616", "P1618", "P1621", "P1623", "P1636", "P1638"}:
                    eff_mod = "icm"
                elif c0.startswith("KLS-"):
                    eff_mod = "kscm"
                elif c0.startswith("U"):
                    sensor_kw = "can"

            module_std_map = {
                "abs": (
                    "[SPESIFIKASI STANDAR MODUL ABS / HECU (Vol 1 Bab 4E Hal. 636-649)]\n"
                    "• Tegangan Suplai IG1 (E03-07) & +B Solenoid/Motor (E03-13, E03-26): 10.0 - 14.0 V\n"
                    "• Tahanan Ground Modul ABS (E03-01 & E03-14): < 1.0 Ohm ke bodi\n"
                    "• Celah Wheel Speed Sensor: Rapat pada knuckle tanpa serbuk besi pada rotor magnetik"
                ),
                "tcm": (
                    "[SPESIFIKASI STANDAR MODUL TRANSMISI OTOMATIS TCM (Vol 2 Bab 5A Hal. 102-104)]\n"
                    "• Suplai Daya Utama TCM IG ON (E92-06) & Backup +B (E92-22): 10.0 - 14.0 V\n"
                    "• Tegangan Shift Solenoid-A/B pada Posisi P/N (E92-16 / E92-15): 9.0 - 14.0 V\n"
                    "• Ground Utama TCM (E92-01 & E92-23): < 0.5 V (< 1.0 Ohm ke massa)"
                ),
                "hvac": (
                    "[SPESIFIKASI STANDAR MODUL KONTROL AC OTOMATIS / HVAC (Vol 2 Bab 7B Hal. 327-330)]\n"
                    "• Suplai Daya Modul HVAC IG ON (G52-01) & Memori +B (G52-02): 10.0 - 14.0 V\n"
                    "• Tegangan Referensi Sensor/Aktuator +5V (G52-14): 4.0 - 6.0 V\n"
                    "• Ground Utama & Sensor HVAC (G52-15 & G52-27): < 1.0 Ohm"
                ),
                "sdm": (
                    "[SPESIFIKASI STANDAR MODUL SRS AIR BAG / SDM (Vol 2 Bab 8B Hal. 370)]\n"
                    "• Suplai Daya Utama SDM IG ON (G47-16): ≥ 8.0 V (Normal 10.0 - 14.0 V)\n"
                    "• Tahanan Sirkuit Inflator Air Bag / Pretensioner (dengan Special Tool): 1.8 - 2.5 Ohm\n"
                    "• Ground Utama SDM (G47-20): < 1.0 Ohm (PERINGATAN: Jangan ukur inflator langsung dengan ohmmeter tanpa melepas konektor!)"
                ),
                "bcm": (
                    "[SPESIFIKASI STANDAR BODY ELECTRICAL CONTROL MODULE / BCM (Vol 2 Bab 10B Hal. 754-758)]\n"
                    "• Suplai Daya +B Utama BCM (G30-01) & IG1 (G30-21) & ACC (G30-09): 10.0 - 14.0 V\n"
                    "• Tegangan Pengisian Normal Bodi (Bebas B1133): 9.5 - 15.5 V\n"
                    "• Ground Utama BCM (G30-10 & G32-39): < 1.0 Ohm ke titik massa pilar dashboard"
                ),
                "icm": (
                    "[SPESIFIKASI STANDAR IMMOBILIZER CONTROL MODULE / ICM (Vol 2 Bab 10C Hal. 785)]\n"
                    "• Suplai Daya +B ICM (G24-01) & IG1 ON (G24-04): 10.0 - 14.0 V\n"
                    "• Komunikasi Serial ICM ↔ ECM (G24-02 & G24-03): Kontinuitas < 2.0 Ohm, bebas koslet ke +B/Ground\n"
                    "• Ground ICM (G24-07): < 1.0 Ohm"
                ),
                "kscm": (
                    "[SPESIFIKASI STANDAR KEYLESS START CONTROL MODULE / KSCM (Vol 2 Bab 10E Hal. 803-804)]\n"
                    "• Suplai Daya +B KSCM (G44-01) & IG1 ON (G44-08): 10.0 - 14.0 V\n"
                    "• Tegangan Baterai Remote Keyless (CR2032): ≥ 2.8 V\n"
                    "• Ground Utama KSCM (G44-16): < 1.0 Ohm"
                ),
            }
            if eff_mod in module_std_map:
                summary_parts.append(module_std_map[eff_mod])
            elif sensor_kw == "can":
                summary_parts.append(
                    "[SPESIFIKASI JARINGAN KOMUNIKASI CAN BUS (ECM E23 / TCM E92 / ABS E03 / BCM G32)]\n"
                    "• Tegangan CAN High (WHT/RED): 2.5 - 3.6 V (Pulsa Data Aktif)\n"
                    "• Tegangan CAN Low (RED / BLU): 1.6 - 2.5 V (Pulsa Data Aktif)\n"
                    "• Tahanan Terminasi Total Bus CAN (Aki Dilepas): 54 - 66 Ohm (2 Resistor 120Ω Paralel)"
                )

        # 3. BLOK JALUR WIRING, PINOUT KONEKTOR MODUL & WARNA KABEL BUKU MANUAL
        if primary_cat_entry and primary_cat_entry.get("wiring_pinout"):
            dtc_pins = primary_cat_entry["wiring_pinout"][:8]
            first_pin_prefix = str(dtc_pins[0].get("pin", "")).split("-")[0].strip().upper()
            matched_wd = next(
                (w for w in wiring_diagrams if first_pin_prefix and first_pin_prefix in w.ecu_connector_code.upper()),
                None,
            )
            conn_title = (
                matched_wd.ecu_connector_code
                if matched_wd
                else f"Konektor Modul {first_pin_prefix or 'JB420'}"
            )
            pin_preview = "\n".join(
                f"• {p.get('pin', '-')}: {p.get('wire_color', '-')} — {p.get('function', p.get('signal', '-'))}"
                for p in dtc_pins
            )
            ground_note = (
                f"\n• Titik Massa (Ground): {matched_wd.ground_locations}"
                if matched_wd and matched_wd.ground_locations
                else ""
            )
            summary_parts.append(
                f"[JALUR WIRING & PINOUT BUKU MANUAL — DTC {primary_cat_entry['code']} ({conn_title})]\n"
                f"{pin_preview}"
                f"{ground_note}"
            )
        elif wiring_diagrams:
            matched_wd = None
            matched_pins: list[WiringPinoutItem] = []

            module_conn_map = {
                "abs": "E03",
                "tcm": "E92",
                "hvac": "G52",
                "sdm": "G47",
                "bcm": "G30",
                "icm": "G24",
                "kscm": "G44",
            }
            if module_kw in module_conn_map:
                target_conn = module_conn_map[module_kw]
                matched_wd = next(
                    (w for w in wiring_diagrams if target_conn in w.ecu_connector_code.upper()),
                    None,
                )
                if matched_wd:
                    matched_pins = matched_wd.pinouts[:8]

            if not matched_wd and sensor_kw:
                kw_aliases = {
                    "fan": ("radiator", "cooling fan", "e23-46", "e23-47", "c37-24", "c37-57"),
                    "maf": ("maf", "intake air", "air flow", "c37-26", "c37-25", "c37-27", "c37-57"),
                    "o2": ("o2", "ho2s", "oxygen", "heater", "e23-50", "e23-49", "c37-65", "c37-38", "c37-37", "c37-57"),
                    "ect": ("ect", "coolant", "water temp", "c37-24", "c37-57"),
                    "map": ("map", "manifold", "c37-55", "c37-14", "c37-57"),
                    "ckp": ("ckp", "crank", "cmp", "cam", "c37-51", "c37-36", "c37-52"),
                    "cmp": ("cmp", "cam", "ckp", "c37-52"),
                    "tps": ("tps", "throttle", "etcs", "vta", "c37-53", "c37-54", "c37-40"),
                    "app": ("app", "e23-55", "e23-56", "e23-52", "e23-53"),
                    "injector": ("injektor", "injector", "c37-60", "c37-59", "c37-58", "c37-44"),
                    "fuel_pump": ("fuel pump", "pompa bensin", "e23-45"),
                    "evap": ("evap", "canister", "purge", "c37-31"),
                    "egr": ("egr", "c37-18", "c37-19", "c37-04", "c37-05"),
                    "can": ("can ", "komunikasi can", "e23-04", "e23-19", "e03-06", "e92-17"),
                    "coil": ("coil", "ignition", "igt", "c37-33", "c37-34", "c37-47", "c37-48"),
                    "ignition": ("coil", "ignition", "igt", "c37-33", "c37-34", "c37-47", "c37-48"),
                }.get(sensor_kw, (sensor_kw,))
                for wd in reversed(wiring_diagrams):
                    pins = [
                        p for p in wd.pinouts
                        if any(k in f"{p.pin_code} {p.function}".lower() for k in kw_aliases)
                    ]
                    if pins:
                        matched_wd = wd
                        matched_pins = pins
                        break

            if not matched_wd and (sensor_kw or module_kw or dtc_details):
                matched_wd = next(
                    (w for w in wiring_diagrams if "C37" in w.ecu_connector_code and "E23" in w.ecu_connector_code),
                    wiring_diagrams[0],
                )
                matched_pins = matched_wd.pinouts[:6]

            if matched_wd and matched_pins:
                pin_preview = "\n".join(
                    f"• {p.pin_code}: {p.wire_color} — {p.function}" for p in matched_pins[:8]
                )
                summary_parts.append(
                    f"[JALUR WIRING & PINOUT MODUL ({matched_wd.ecu_connector_code})]\n"
                    f"{pin_preview}\n"
                    f"• Titik Massa (Ground): {matched_wd.ground_locations}"
                )

        # Cek pula Katalog Universal Modern (Diesel Common-Rail, Turbo, VVT/VANOS, Hybrid/EV, CAN) & Paket Manual Kustom
        if detected_dtcs:
            extra_blocks: list[str] = []
            already_codes = {d.code.upper() for d in dtc_details}
            # 1) Cek paket manual kustom HANYA bila user tidak secara eksplisit mengunci ke JB420 atau Universal
            if req_pack_id not in {"suzuki_jb420_builtin", "universal"}:
                for pack in load_custom_manual_packs():
                    p_brand = str(pack.get("brand", "")).lower()
                    p_model = str(pack.get("model", "")).lower()
                    if payload.brand and p_brand and payload.brand.lower() not in p_brand and p_brand not in payload.brand.lower():
                        continue
                    for cd in pack.get("dtc_catalog", []):
                        cd_code = str(cd.get("code", "")).upper()
                        if cd_code in detected_dtcs:
                            extra_blocks.append(
                                f"[PAKET MANUAL KUSTOM: {pack.get('title', p_model)} — {cd_code}]\n"
                                f"• Deskripsi: {cd.get('description_id', '-')}\n"
                                f"• Penyebab: {cd.get('common_causes', '-')}\n"
                                f"• Langkah: {' | '.join(cd.get('repair_steps', []))}"
                            )
            # 2) Cek Katalog Modern (Diesel / Turbo / VVT / EV / Hybrid / CAN)
            for code in detected_dtcs:
                mh = lookup_modern_dtc(code, "Diesel" if "diesel" in payload.query.lower() or "2gd" in payload.query.lower() else "Bensin")
                if mh and (req_pack_id == "universal" or code not in already_codes or code in {"P0087", "P0299", "P0015", "P0A80", "P0AA6", "U0100"}):
                    opts_txt = " | ".join(o["title"] for o in mh.get("repair_options", [])[:3])
                    specs_txt = "; ".join(f"{s['parameter']}: {s['normal_range']}" for s in mh.get("standard_specs", [])[:3])
                    hv_note = "\n⚠️ WAJIB APD TEGANGAN TINGGI (HV 1000V)!" if mh.get("requires_hv_safety") else ""
                    extra_blocks.append(
                        f"[KATALOG UNIVERSAL MODERN — {mh['code']} ({mh['system_category']})]\n"
                        f"• Deskripsi: {mh['title_id']}\n"
                        f"• Penyebab Utama: {mh['root_causes']}\n"
                        f"• Opsi Perbaikan: {opts_txt}\n"
                        f"• Standar Ukur: {specs_txt}{hv_note}"
                    )
            if extra_blocks:
                summary_parts = extra_blocks + summary_parts

        if req_pack_id == "universal" and summary_parts:
            summary_parts.insert(
                0,
                "[MODE STANDAR UNIVERSAL OBD-II]\n"
                "• Catatan: Nilai tegangan & pinout di bawah bersifat ilustrasi referensi umum (basis arsitektur Suzuki JB420 / SAE J2012). "
                "Pilih buku manual spesifik model bila sudah tersedia, atau verifikasi fisik menggunakan multitester."
            )

        if not summary_parts:
            synthesized = (
                "Data spesifikasi, penyebab & solusi DTC, atau jalur wiring belum ditemukan untuk kata kunci tersebut. "
                "Masukkan kode DTC (contoh: P0087, P0299, P0015, P0A80, P0AA6, U0100, P0480, C1021, P0756, B1502) "
                "atau nama sensor/modul (MAF, O2, ECT, TPS, CKP, ABS, TCM, HVAC, SRS Airbag, BCM, Immobilizer, Keyless)."
            )
        else:
            synthesized = "\n\n".join(summary_parts)

        return RAGAssistantResponse(
            query=payload.query,
            detected_dtc_codes=detected_dtcs,
            synthesized_guidance=synthesized,
            matched_dtc_details=dtc_details,
            matched_sensor_specs=sensor_specs,
            matched_wiring_diagrams=wiring_diagrams,
            matched_manual_sections=[],
        )


# ---------------------------------------------------------------------------
# 3. FASTAPI ROUTER ENDPOINTS
# ---------------------------------------------------------------------------

router = APIRouter(prefix="/api/v1/manuals", tags=["AI Repair Manual & Wiring Assistant"])


@router.get(
    "/dtc/{dtc_code}",
    response_model=DTCCodeOut,
    summary="Detail Kode DTC OBD-II (P0300, P0335, dsb)",
)
async def get_dtc_detail(
    dtc_code: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> DTCCodeOut:
    results = await ManualAndWiringService.lookup_dtc_codes(db, [dtc_code])
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Kode DTC {dtc_code.upper()} belum terdaftar di database.",
        )
    return results[0]


@router.get(
    "/sensor-specs",
    response_model=list[SensorSpecOut],
    summary="Cari Standar Voltase & Tahanan Sensor (TPS, MAP, O2, CKP)",
)
async def list_sensor_specs(
    brand: str | None = Query(default=None),
    model: str | None = Query(default=None),
    sensor: str | None = Query(default=None, description="Nama sensor, misal TPS, MAP, CKP, O2"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> list[SensorSpecOut]:
    return await ManualAndWiringService.search_sensor_specs(
        db, brand=brand, model=model, sensor_keyword=sensor
    )


@router.get(
    "/wiring-diagrams",
    response_model=list[WiringDiagramOut],
    summary="Lihat Pinout ECU, Warna Kabel, & Lokasi Massa (Ground)",
)
async def list_wiring_diagrams(
    brand: str | None = Query(default=None),
    model: str | None = Query(default=None),
    system: str | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> list[WiringDiagramOut]:
    return await ManualAndWiringService.search_wiring_diagrams(
        db, brand=brand, model=model, system_keyword=system
    )


@router.post(
    "/ask-assistant",
    response_model=RAGAssistantResponse,
    summary="Tanya AI Repair Manual & Wiring Assistant (RAG Terpadu)",
)
async def ask_repair_assistant(
    payload: RAGAssistantQuery,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> RAGAssistantResponse:
    return await ManualAndWiringService.ask_rag_assistant(db, payload)


class VehicleResolveRequest(BaseModel):
    brand: str = ""
    model: str = ""
    year: int | None = None
    engine_code: str = ""


class ManualPackImportRequest(BaseModel):
    pack_id: str | None = None
    brand: str = Field(..., min_length=1)
    model: str = Field(..., min_length=1)
    generation_id: str | None = None
    generation_label: str = ""
    year_start: int = Field(default=2010, ge=1980, le=2030)
    year_end: int = Field(default=2027, ge=1980, le=2030)
    engine_codes: list[str] = []
    title: str = Field(..., min_length=2)
    dtc_catalog: list[dict[str, Any]] = []
    wiring_pinouts: list[dict[str, str]] = []
    sensor_specs: list[dict[str, str]] = []


class PdfPreviewRequest(BaseModel):
    file_name: str
    content_base64: str
    brand: str = ""
    model: str = ""
    year_start: int = 2015
    year_end: int = 2026
    max_pages: int = 25


@router.get(
    "/vehicle-matrix",
    summary="Matriks Model, Generasi, Katalog Kode Mesin (Asia/Eropa/China) & Status Manual",
)
async def get_vehicle_matrix_and_packs(
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    """Mengembalikan katalog generasi kendaraan (Asia, Eropa, China), direktori kode mesin, & paket manual terpasang."""
    packs = [p.model_dump() for p in list_all_manual_pack_summaries()]
    engines = build_engine_directory()
    region_counts: dict[str, int] = {"Asia": 0, "Eropa": 0, "China": 0}
    for e in engines:
        reg = e.get("region", "Asia")
        region_counts[reg] = region_counts.get(reg, 0) + 1
    return {
        "generations": VEHICLE_GENERATION_CATALOG,
        "installed_packs": packs,
        "engine_directory": engines,
        "region_counts": region_counts,
    }


@router.get(
    "/engine-catalog",
    summary="Pencarian Katalog Kode Mesin Mobil Asia, Eropa & China",
)
async def search_engine_catalog(
    region: str | None = Query(None, description="Filter wilayah: Asia, Eropa, China"),
    brand: str | None = Query(None, description="Filter merek mobil"),
    fuel: str | None = Query(None, description="Filter bahan bakar: Bensin, Diesel, Hybrid, EV"),
    q: str | None = Query(None, description="Cari kode mesin, alias (mis. 1TR-VE, 2GD), atau model mobil"),
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    """Mencari kode mesin lintas merek Asia, Eropa, dan China lengkap dengan normalisasi alias bengkel."""
    engines = build_engine_directory()
    if region and region.lower() != "semua":
        r_low = region.strip().lower()
        engines = [e for e in engines if e.get("region", "").lower() == r_low]
    if brand:
        b_low = brand.strip().lower()
        engines = [e for e in engines if b_low in e.get("brand", "").lower()]
    if fuel and fuel.lower() != "semua":
        f_low = fuel.strip().lower()
        engines = [e for e in engines if f_low in e.get("fuel", "").lower()]
    if q:
        q_raw = q.strip().lower()
        q_norm = re.sub(r"[^a-z0-9]", "", q_raw)

        def _match_q(entry: dict[str, Any]) -> bool:
            hay = " ".join(
                [
                    entry.get("code", ""),
                    " ".join(entry.get("aliases", [])),
                    entry.get("brand", ""),
                    " ".join(entry.get("models", [])),
                    " ".join(entry.get("generation_labels", [])),
                    entry.get("desc", ""),
                    entry.get("origin_country", ""),
                    entry.get("region", ""),
                ]
            ).lower()
            if q_raw in hay:
                return True
            if q_norm and q_norm in re.sub(r"[^a-z0-9]", "", hay):
                return True
            return False

        engines = [e for e in engines if _match_q(e)]

    return {
        "total": len(engines),
        "engines": engines,
    }


@router.post(
    "/resolve-vehicle",
    response_model=VehicleApplicabilityInfo,
    summary="Resolusi Generasi Mobil, Kode Mesin & Ketersediaan Manual OEM",
)
async def resolve_vehicle_endpoint(
    payload: VehicleResolveRequest,
    current_user: User = Depends(get_current_active_user),
) -> VehicleApplicabilityInfo:
    app_info, _ = resolve_vehicle_applicability(
        payload.brand, payload.model, payload.year, payload.engine_code
    )
    return app_info


@router.post(
    "/packs/import",
    status_code=status.HTTP_201_CREATED,
    summary="Impor Paket Buku Manual Model Baru (Dilindungi PIN Kepala Bengkel)",
)
async def import_custom_manual_pack(
    payload: ManualPackImportRequest,
    _pin_ok: str = Depends(require_workshop_pin),
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    saved = save_custom_manual_pack(payload.model_dump())
    return {
        "status": "success",
        "message": f"Paket manual '{saved['title']}' berhasil diaktifkan untuk {saved['brand']} {saved['model']} ({saved['year_start']}–{saved['year_end']}).",
        "pack": saved,
    }


def _build_curated_pack_components(
    pack: dict[str, Any],
    engine_filter: str | None = None,
) -> tuple[list[dict[str, Any]], dict[str, str] | None]:
    """
    Menyaring & mengelompokkan 200–2.500 entri sensor/pinout pada manual multi-mesin (seperti Toyota Avanza,
    Fortuner, Innova, Hilux, Yaris, Corolla/Camry) menjadi 7–10 komponen inti siap simulasi di Tab 3
    (Koil/Rail, Injektor, MAP/MAF, Throttle/TPS, Pedal APP, ECT/IAT, O2/A-F, CKP/CMP/VVT, Kipas/AC)
    agar payload ringan (~30 KB bukan 800 KB) dan tidak terjebak menampilkan 'Baterai / +B' saja.
    """
    specs_all = list(pack.get("sensor_specs", []))
    pins_all = list(pack.get("wiring_pinouts", []))
    dtcs_all = list(pack.get("dtc_catalog", []))
    eng_clean = re.sub(r"[^a-z0-9]", "", (engine_filter or "").lower())

    # Filter berdasarkan kode mesin bila dipilih (atau pakai mesin pertama yang ada di pinout bila terlalu banyak)
    if eng_clean and len(eng_clean) >= 3:
        specs_pool = [s for s in specs_all if eng_clean in re.sub(r"[^a-z0-9]", "", str(s.get("sensor_name", "")).lower())] or specs_all
        pins_pool = [p for p in pins_all if eng_clean in re.sub(r"[^a-z0-9]", "", str(p.get("pin", "")).lower())] or pins_all
    else:
        specs_pool = specs_all
        pins_pool = pins_all

    is_diesel_eng = bool(re.search(r"1kd|2kd|1gd|2gd|d13a|4d56|4n15", eng_clean))
    eng_label = (engine_filter or "").strip() or (", ".join(pack.get("engine_codes", [])[:3]) or str(pack.get("model", "")))

    categories = [
        ("coil", "Koil Pengapian (IGT/IGF)" if not is_diesel_eng else "Common-Rail & SCV Diesel",
         "coil" if not is_diesel_eng else "map",
         r"\b(igt[1-8]|igf\d?|ig[1-4]|koil|ignition\s*coil)\b" if not is_diesel_eng else r"\b(pcr\d?|pr\d?|scv|vcs|fuel\s*rail|common.?rail)\b",
         r"^P030|^P035" if not is_diesel_eng else r"^P008[78]|^P0093|^P019"),
        ("map", "Sensor MAP / Tekanan Intake", "map", r"\b(pim|vcpm|e2pm|map\s*sensor|tekanan\s*absolut|manifold\s*absolute|turbo\s*pressure)\b", r"^P010[5-9]|^P023|^P0299"),
        ("maf", "Sensor MAF & Suhu Udara IAT", "maf", r"\b(vg|e2g|maf|air\s*flow|aliran\s*udara|massa\s*udara)\b", r"^P010[0-4]|^P017[12]"),
        ("throttle", "Throttle Body (ETC / TPS)", "throttle", r"\b(vta\d?|tps|tp\s*sensor|posisi\s*throttle|aktuator\s*throttle|m\+|m-)\b", r"^P012[0-4]|^P022|^P210|^P211|^P2135"),
        ("app", "Sensor Pedal Gas (APP / VPA)", "app", r"\b(vpa\d?|epa\d?|app\s*sensor|pedal\s*akselerator|accelerator\s*pedal)\b", r"^P212|^P2138"),
        ("ect", "Sensor Suhu ECT (THW) & IAT", "ect", r"\b(thw|ect\s*sensor|suhu\s*air\s*pendingin|coolant\s*temp|tha|iat\s*sensor|suhu\s*udara\s*masuk)\b", r"^P011[0-9]|^P012[58]"),
        ("ckp", "Sensor CKP (NE), CMP (G2) & VVT", "ckp", r"\b(ne[+-]|g2[+-]|ckp|cmp|poros\s*engkol|crankshaft|camshaft|ocv|vvt)\b", r"^P033[5-9]|^P034|^P001[0-7]"),
        ("o2", "Sensor Oksigen / A-F (OX / HT)", "o2", r"\b(ox\d?|ht\d?|a1a|ha1a|ho2s|o2\s*sensor|a/f\s*sensor|oksigen|rasio\s*udara)\b", r"^P003[0-8]|^P013|^P014|^P219"),
        ("injector", "Injektor Bahan Bakar", "coil", r"\b(#10|#20|#30|#40|inj\d?|injektor|injector)\b", r"^P020[0-8]|^P062D"),
        ("fan", "Kipas Radiator & Sistem AC", "fan", r"\b(fan\d?|kipas\s*radiator|cooling\s*fan|acsw|mgc|kompresor\s*ac)\b", r"^P048[0-5]|^P053"),
    ]

    curated: list[dict[str, Any]] = []
    map_reference: dict[str, str] | None = None

    for cid, label, a_type, rx_str, dtc_rx_str in categories:
        rx = re.compile(rx_str, re.I)
        dtc_rx = re.compile(dtc_rx_str, re.I)

        m_pins: list[dict[str, str]] = []
        seen_p: set[str] = set()
        for pw in pins_pool:
            hay = f"{pw.get('pin', '')} {pw.get('signal', '')} {pw.get('function', '')}"
            if rx.search(hay):
                pk = str(pw.get("pin", "-"))
                if pk not in seen_p:
                    seen_p.add(pk)
                    m_pins.append({
                        "pin": pk,
                        "signal": str(pw.get("signal", "-")),
                        "function": str(pw.get("function", "-")),
                    })
                if len(m_pins) >= 6:
                    break

        m_specs: list[dict[str, str]] = []
        seen_s: set[str] = set()
        for sp in specs_pool:
            hay_s = f"{sp.get('sensor_name', '')} {sp.get('pin_configuration', '')} {sp.get('voltage_idle', '')}"
            if rx.search(hay_s):
                sn = str(sp.get("sensor_name", "-"))
                if sn not in seen_s:
                    seen_s.add(sn)
                    m_specs.append({
                        "sensor_name": sn,
                        "pin_configuration": str(sp.get("pin_configuration", "-")),
                        "voltage_idle": str(sp.get("voltage_idle", "-")),
                        "voltage_wot": str(sp.get("voltage_wot", "-")),
                        "resistance_ohm": str(sp.get("resistance_ohm", "-")),
                    })
                if len(m_specs) >= 4:
                    break

        if not m_pins and not m_specs:
            continue

        rel_dtcs = [
            str(d.get("code", "")).upper()
            for d in dtcs_all
            if dtc_rx.search(str(d.get("code", "")))
        ][:6]

        if cid == "map" and not map_reference:
            sp0 = m_specs[0] if m_specs else {}
            p0 = m_pins[0] if m_pins else {}
            map_reference = {
                "engine": eng_label,
                "pin_hint": sp0.get("pin_configuration") or (f"{p0.get('pin', '')} ({p0.get('signal', '')})" if p0 else ""),
                "voltage_idle": sp0.get("voltage_idle") or (p0.get("function") or "Idle ~0.9–1.5V | KOEO ~3.8–4.3V"),
                "voltage_wot": sp0.get("voltage_wot") or "-",
            }

        curated.append({
            "id": cid,
            "anatomy_type": a_type,
            "short_label": label,
            "engine_label": eng_label,
            "dtcs": ", ".join(rel_dtcs) if rel_dtcs else "Lihat Pencarian Manual",
            "pins": m_pins,
            "specs": m_specs,
        })

    return curated, map_reference


@router.get(
    "/packs/{pack_id}",
    summary="Detail Ringkas & Terkelompok Paket Buku Manual Aktif (Cepat & Multi-Mesin)",
)
async def get_manual_pack_detail(
    pack_id: str,
    engine: str | None = Query(default=None, description="Opsional filter kode mesin (mis. 1TR-FE, 2KD-FTV, K3-VE)"),
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    """Mengembalikan komponen inti terkelompok, acuan MAP, kode DTC populer & ringkasan pinout dari manual aktif."""
    pid = str(pack_id or "").strip()
    if pid == "suzuki_jb420_builtin":
        return {
            "pack_id": "suzuki_jb420_builtin",
            "brand": "Suzuki",
            "model": "Grand Vitara",
            "generation_id": "suzuki_jb420",
            "generation_label": "Grand Vitara Gen 2 (JB420)",
            "year_start": 2006,
            "year_end": 2015,
            "engine_codes": ["J20A"],
            "title": "Buku Pedoman Resmi Suzuki Grand Vitara JB420 (Vol 1 & Vol 2)",
            "is_builtin": True,
            "dtc_count": 207,
            "pinout_count": 251,
            "sensor_spec_count": 9,
            "popular_dtcs": ["P0480", "C1021", "P0756", "B1502", "B1017", "B1133", "P1614", "KLS-11"],
            "curated_components": [],
            "map_reference": None,
            "wiring_pinouts": [],
            "sensor_specs": [],
        }

    pack = get_custom_manual_pack_by_id(pid)
    if not pack:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Paket manual '{pid}' tidak ditemukan.",
        )

    dtcs = list(pack.get("dtc_catalog", []))
    dtc_codes_set = {str(d.get("code", "")).upper() for d in dtcs if d.get("code")}
    preferred_order = ["P0300", "P0171", "P0087", "P0107", "P0117", "P0122", "P0130", "P0335", "P0340", "P0480", "P2135", "P0105", "P2122"]
    popular = [c for c in preferred_order if c in dtc_codes_set][:8]
    if len(popular) < 8:
        for d in dtcs:
            c = str(d.get("code", "")).upper()
            if c and c not in popular:
                popular.append(c)
            if len(popular) >= 8:
                break

    curated_comps, map_ref = _build_curated_pack_components(pack, engine)

    return {
        "pack_id": str(pack.get("pack_id", pid)),
        "brand": str(pack.get("brand", "")),
        "brand_aliases": list(pack.get("brand_aliases", [])),
        "model": str(pack.get("model", "")),
        "generation_id": pack.get("generation_id"),
        "generation_label": str(pack.get("generation_label", pack.get("model", ""))),
        "year_start": int(pack.get("year_start", 2010)),
        "year_end": int(pack.get("year_end", 2026)),
        "engine_codes": list(pack.get("engine_codes", [])),
        "selected_engine": (engine or "").strip() or None,
        "title": str(pack.get("title", "Manual Tambahan Bengkel")),
        "is_builtin": False,
        "dtc_count": len(dtcs),
        "pinout_count": len(pack.get("wiring_pinouts", [])),
        "sensor_spec_count": len(pack.get("sensor_specs", [])),
        "popular_dtcs": popular,
        "curated_components": curated_comps,
        "map_reference": map_ref,
        "wiring_pinouts": list(pack.get("wiring_pinouts", []))[:60],
        "sensor_specs": list(pack.get("sensor_specs", []))[:25],
    }


@router.delete(
    "/packs/{pack_id}",
    summary="Hapus Paket Buku Manual Kustom (Dilindungi PIN Kepala Bengkel)",
)
async def remove_custom_manual_pack(
    pack_id: str,
    _pin_ok: str = Depends(require_workshop_pin),
    current_user: User = Depends(get_current_active_user),
) -> dict[str, str]:
    ok = delete_custom_manual_pack(pack_id)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Paket manual tidak ditemukan atau merupakan paket bawaan sistem.",
        )
    return {"status": "deleted", "pack_id": pack_id}


@router.post(
    "/packs/preview-pdf",
    summary="Pra-Ekstrak Otomatis File PDF Manual Baru Menjadi Draf Paket JSON",
)
async def preview_pdf_manual_extraction(
    payload: PdfPreviewRequest,
    current_user: User = Depends(get_current_active_user),
) -> dict[str, Any]:
    """Membaca teks PDF manual baru secara otomatis, mendeteksi kode DTC OBD-II & pola pinout sebagai draf siap review."""
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise HTTPException(status_code=500, detail=f"Library pypdf belum tersedia: {exc}")

    try:
        raw_b64 = payload.content_base64.split(",", 1)[-1]
        pdf_bytes = base64.b64decode(raw_b64)
        reader = PdfReader(io.BytesIO(pdf_bytes))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Gagal membaca file PDF: {exc}")

    total_pages = len(reader.pages)
    limit = min(total_pages, max(1, payload.max_pages))
    dtc_seen: dict[str, dict[str, Any]] = {}
    pin_seen: list[dict[str, str]] = []
    seen_pin_codes: set[str] = set()

    for page_idx in range(limit):
        txt = reader.pages[page_idx].extract_text() or ""
        if not txt.strip():
            continue
        lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
        for i, ln in enumerate(lines):
            # Deteksi kode DTC (P0xxx, P1xxx, Cxxxx, Bxxxx, Uxxxx)
            for m in re.finditer(r"\b([PCBU][0-9A-F]{4})\b", ln.upper()):
                code = m.group(1)
                if code not in dtc_seen:
                    ctx_after = " ".join(lines[i : min(i + 3, len(lines))])
                    dtc_seen[code] = {
                        "code": code,
                        "description_id": ctx_after[:180],
                        "common_causes": f"Hasil ekstraksi PDF halaman {page_idx + 1}: perlu verifikasi mekanik.",
                        "repair_steps": [f"1. Periksa komponen & sirkuit kode {code} (Hal. {page_idx + 1} PDF)."],
                        "page": page_idx + 1,
                    }
            # Deteksi pola pinout konektor umum (misal E1-12, C37-24, A12)
            for pm in re.finditer(r"\b([A-Z]\d{1,2}[-]\d{1,2})\b", ln):
                p_code = pm.group(1)
                if p_code not in seen_pin_codes and len(pin_seen) < 20:
                    seen_pin_codes.add(p_code)
                    pin_seen.append({
                        "pin": p_code,
                        "signal": ln[:60],
                        "function": f"Terdeteksi di halaman {page_idx + 1} (perlu verifikasi)",
                    })

    draft_pack = {
        "brand": payload.brand.strip() or "Model Baru",
        "model": payload.model.strip() or Path(payload.file_name).stem,
        "year_start": payload.year_start,
        "year_end": payload.year_end,
        "engine_codes": [],
        "title": f"Draf Manual {payload.brand} {payload.model} ({payload.file_name})".strip(),
        "dtc_catalog": list(dtc_seen.values())[:50],
        "wiring_pinouts": pin_seen,
        "sensor_specs": [],
    }
    return {
        "file_name": payload.file_name,
        "total_pages_in_pdf": total_pages,
        "pages_scanned": limit,
        "detected_dtc_count": len(dtc_seen),
        "detected_pinout_count": len(pin_seen),
        "draft_pack": draft_pack,
    }
