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
        min_length=3,
        examples=["Cara cek sensor CKP Suzuki Grand Vitara J20A kode P0335 dan warna kabel pinout ECU"],
        description="Pertanyaan teknis mekanik (bisa memuat merk, model, gejala, sensor, atau kode DTC)",
    )
    brand: str | None = Field(default=None, examples=["Suzuki"])
    model: str | None = Field(default=None, examples=["Grand Vitara"])
    dtc_code: str | None = Field(default=None, examples=["P0335"])

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

    @classmethod
    async def ask_rag_assistant(
        cls, session: AsyncSession, payload: RAGAssistantQuery
    ) -> RAGAssistantResponse:
        """
        Mengorkestrasi pengambilan konteks teknis dari Buku Manual Resmi yang ditanamkan:
        HANYA menampilkan:
        1. Penyebab & Saran Penyelesaian DTC dari Buku Manual (`jb420_extracted_catalog.json` + `DTCCode`)
        2. Spesifikasi Standar Multimeter (Volt / Ohm)
        3. Jalur Wiring, Pinout Konektor Modul Kontrol, Warna Kabel & Titik Ground
        (Tanpa menampilkan teks Daftar Isi atau narasi tidak relevan).
        """
        detected_dtcs = cls._extract_dtc_from_text(payload.query, payload.dtc_code)
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

        if not summary_parts:
            synthesized = (
                "Data spesifikasi, penyebab & solusi DTC, atau jalur wiring belum ditemukan untuk kata kunci tersebut. "
                "Masukkan kode DTC Buku Manual (contoh: P0480, C1021, P0756, B1502, B1017, B1133, P1614, KLS-11) "
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
