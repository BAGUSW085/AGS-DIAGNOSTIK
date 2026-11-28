"""
Smart Diagnostic Engine & Self-Learning Loop Service
====================================================
Pilar 1 - Project Bengkel Masa Depan (FastAPI + Async SQLAlchemy 2.0)

Fitur Utama:
1. Hybrid Diagnostic Scoring Algorithm (0 - 100%):
   - Text Similarity (TF-IDF Cosine + Jaccard Token Overlap + Normalisasi Sinonim Bengkel Indonesia)
   - Exact & Family OBD-II DTC Match Boost
   - Vehicle Brand/Model Affinity Bonus (Spesifik karakter mobil)
   - Empirical Prior dari tabel `SymptomCheckpointLink` + Bukti Historis Terverifikasi (`FaultHistory`)
2. Self-Learning Feedback Loop:
   - Saat PKB (`WorkOrder`) selesai dikerjakan, temuan aktual mekanik disimpan ke `FaultHistory`
   - Bobot `base_weight` pada `SymptomCheckpointLink` diperbarui secara adaptif menggunakan
     Exponential Moving Average (EMA) agar rekomendasi semakin akurat seiring bertambahnya kasus.
"""

from collections import defaultdict
from dataclasses import dataclass, field
import json
import math
from pathlib import Path
import re
from typing import Any, Sequence

from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# Catatan: Sesuaikan path import di bawah dengan struktur modul ORM proyek Anda
from app.models import (
    DTCCode,
    FaultCategory,
    FaultCheckpoint,
    FaultHistory,
    HistoricalCase,
    RepairManual,
    SensorSpec,
    SymptomCheckpointLink,
    Vehicle,
    WiringDiagram,
    WorkOrder,
)
from app.services.modern_dtc_catalog import (
    build_low_confidence_safe_advice,
    evaluate_adaptive_live_data,
    is_text_compatible_with_fuel,
    lookup_modern_dtc,
    strip_unverified_jb420_pins_from_text,
)
from app.services.vehicle_applicability import (
    VehicleApplicabilityInfo,
    resolve_vehicle_applicability,
)

# ---------------------------------------------------------------------------
# 1. KAMUS NORMALISASI ISTILAH BENGKEL INDONESIA & STOPWORDS
# ---------------------------------------------------------------------------

INDONESIAN_STOPWORDS: set[str] = {
    "yang", "dan", "di", "ke", "dari", "saat", "ketika", "kalau", "bila",
    "pada", "untuk", "dengan", "atau", "ada", "tidak", "agak", "sangat",
    "sekali", "mobil", "mesin", "tiba", "terus", "habis", "setelah", "baru",
}

# Pemetaan kata gaul/istilah lapangan mekanik ke token kanonik agar pencocokan akurat
AUTOMOTIVE_SYNONYM_MAP: dict[str, str] = {
    "brebet": "mbrebet",
    "berebet": "mbrebet",
    "ndut": "mbrebet",
    "ndutan": "mbrebet",
    "nyendat": "mbrebet",
    "tersendat": "mbrebet",
    "pincang": "pincang",
    "getar": "getar",
    "goyang": "getar",
    "langsam": "idle",
    "stasioner": "idle",
    "ngempos": "ngempos",
    "lelet": "berat",
    "boyo": "berat",
    "kempos": "ngempos",
    "panas": "overheat",
    "mendidih": "overheat",
    "temperatur": "overheat",
    "mogok": "mogok",
    "mati": "mati",
    "susah": "sulit",
    "berat": "berat",
}


def preprocess_symptom_tokens(text: str) -> list[str]:
    """Membersihkan teks keluhan, menormalisasi sinonim bengkel, dan menghapus stopwords."""
    if not text:
        return []
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", text.lower())
    raw_tokens = cleaned.split()
    normalized: list[str] = []
    for tok in raw_tokens:
        if len(tok) <= 1 or tok in INDONESIAN_STOPWORDS:
            continue
        canonical = AUTOMOTIVE_SYNONYM_MAP.get(tok, tok)
        normalized.append(canonical)
    return normalized


def parse_dtc_codes(raw_dtc: str | list[str] | None) -> set[str]:
    """Mengubah input kode DTC (string dipisah koma atau list) menjadi himpunan kode standar."""
    if not raw_dtc:
        return set()
    if isinstance(raw_dtc, str):
        items = re.split(r"[,;\s]+", raw_dtc.strip().upper())
    else:
        items = [str(code).strip().upper() for code in raw_dtc]
    return {item for item in items if re.match(r"^[PCBU][0-9A-F]{4}$", item)}


_DTC_SCANNER_SUFFIX_RE = re.compile(r"^([PCBU][0-9A-F]{4})-?[0-9A-F]{2}$")
_NO_DTC_TOKENS = {"-", "TIDAK", "ADA", "NONE", "NIL", "KOSONG"}


def split_dtc_codes(raw: str | None) -> list[str]:
    """
    Memecah teks DTC (dipisah koma/spasi/titik koma) menjadi daftar kode unik berurutan.
    Format scanner seperti 'P0037-00' atau 'P003700' dinormalkan ke kode standar 'P0037'.
    """
    codes: list[str] = []
    for tok in re.split(r"[,;\s]+", (raw or "").strip().upper()):
        if not tok or tok in _NO_DTC_TOKENS:
            continue
        match = _DTC_SCANNER_SUFFIX_RE.match(tok)
        if match:
            tok = match.group(1)
        if tok not in codes:
            codes.append(tok)
    return codes


# ---------------------------------------------------------------------------
# 2. SCHEMAS REQUEST & RESPONSE (PYDANTIC V2)
# ---------------------------------------------------------------------------


class DiagnosticRequest(BaseModel):
    brand: str = Field(..., examples=["Toyota"], description="Merk kendaraan")
    model: str = Field(..., examples=["Avanza 1.5 G"], description="Model kendaraan")
    symptom_text: str = Field(
        ...,
        min_length=5,
        examples=["Mesin brebet pincang waktu digas di tanjakan dan check engine kedip"],
        description="Keluhan pelanggan atau gejala yang dirasakan mekanik",
    )
    dtc_codes: list[str] = Field(
        default_factory=list,
        examples=[["P0300", "P0302"]],
        description="Daftar kode DTC OBD-II dari scanner (opsional)",
    )
    top_k: int = Field(default=5, ge=1, le=15, description="Jumlah rekomendasi titik cek teratas")


class CheckpointRecommendation(BaseModel):
    rank: int
    checkpoint_id: int
    checkpoint_code: str
    checkpoint_name: str
    category_name: str
    probability_percent: float = Field(..., description="Skor probabilitas (0.0 - 100.0%)")
    confidence_label: str = Field(..., description="HIGH / MEDIUM / LOW")
    inspection_steps: str
    estimated_check_minutes: int
    matched_historical_cases: int
    matched_dtc_codes: list[str]
    matched_keywords: list[str]
    sample_resolution_note: str | None = None


class DiagnosticResponse(BaseModel):
    brand: str
    model: str
    normalized_tokens: list[str]
    input_dtc_codes: list[str]
    total_historical_cases_scanned: int
    recommendations: list[CheckpointRecommendation]


class SelfLearningFeedbackRequest(BaseModel):
    work_order_id: int | None = None
    vehicle_id: int
    resolved_checkpoint_id: int = Field(..., description="Titik cek yang terbukti menyelesaikan masalah")
    symptom_text: str
    dtc_codes: list[str] = Field(default_factory=list)
    resolution_notes: str = Field(..., description="Catatan tindakan perbaikan mekanik")


# ---------------------------------------------------------------------------
# 3. ALGORITMA SMART DIAGNOSTIC ENGINE
# ---------------------------------------------------------------------------


@dataclass
class _CheckpointAggregator:
    checkpoint: FaultCheckpoint
    category_name: str
    history_score_sum: float = 0.0
    prior_rule_max_score: float = 0.0
    matched_cases_count: int = 0
    matched_dtcs: set[str] = field(default_factory=set)
    matched_keywords: set[str] = field(default_factory=set)
    best_case_similarity: float = 0.0
    best_resolution_note: str | None = None


class SmartDiagnosticEngine:
    """
    Mesin inferensi diagnosa kerusakan mobil berbasis Hybrid Case-Based Reasoning (CBR)
    dan Prior Pakar (`SymptomCheckpointLink`).
    """

    # Bobot komponen komposit (Total = 1.00)
    WEIGHT_SYMPTOM_SIMILARITY = 0.45
    WEIGHT_DTC_MATCH = 0.30
    WEIGHT_VEHICLE_AFFINITY = 0.15
    WEIGHT_PRIOR_RULE = 0.10

    # Faktor peluruhan (learning rate) untuk pembaruan mandiri (EMA)
    EMA_ALPHA = 0.15

    @classmethod
    def _compute_tfidf_cosine_and_overlap(
        cls,
        query_tokens: list[str],
        doc_tokens: list[str],
        idf_map: dict[str, float],
    ) -> tuple[float, set[str]]:
        """Menghitung kombinasi TF-IDF Cosine Similarity & Jaccard Overlap beserta token yang cocok."""
        if not query_tokens or not doc_tokens:
            return 0.0, set()

        q_set = set(query_tokens)
        d_set = set(doc_tokens)
        common_tokens = q_set.intersection(d_set)
        if not common_tokens:
            return 0.0, set()

        # Vector TF-IDF
        vocab = q_set.union(d_set)
        dot_product = 0.0
        q_norm_sq = 0.0
        d_norm_sq = 0.0

        for term in vocab:
            idf = idf_map.get(term, 1.0)
            q_tf = query_tokens.count(term) / len(query_tokens)
            d_tf = doc_tokens.count(term) / len(doc_tokens)
            q_val = q_tf * idf
            d_val = d_tf * idf

            dot_product += q_val * d_val
            q_norm_sq += q_val * q_val
            d_norm_sq += d_val * d_val

        denom = math.sqrt(q_norm_sq) * math.sqrt(d_norm_sq)
        cosine_sim = (dot_product / denom) if denom > 0 else 0.0
        jaccard_sim = len(common_tokens) / len(vocab)

        # Kombinasi 70% TF-IDF Cosine + 30% Jaccard
        combined_sim = (0.70 * cosine_sim) + (0.30 * jaccard_sim)
        return min(combined_sim, 1.0), common_tokens

    @classmethod
    def _compute_dtc_similarity(
        cls, query_dtcs: set[str], target_dtcs: set[str]
    ) -> tuple[float, set[str]]:
        """
        Menghitung kecocokan kode DTC OBD-II:
        - Exact Match (misal P0302 == P0302): skor 1.0
        - Subsystem Family Match (3 karakter awal sama, misal P0302 vs P0300): skor 0.65
        """
        if not query_dtcs or not target_dtcs:
            return 0.0, set()

        exact_matches = query_dtcs.intersection(target_dtcs)
        if exact_matches:
            return 1.0, exact_matches

        # Cek kecocokan keluarga sistem (contoh P03xx = Ignition/Misfire)
        q_prefixes = {code[:3] for code in query_dtcs}
        t_prefixes = {code[:3] for code in target_dtcs}
        family_matches = q_prefixes.intersection(t_prefixes)
        if family_matches:
            matched_labels = {f"{prefix}xx (Family)" for prefix in family_matches}
            return 0.65, matched_labels

        return 0.0, set()

    @classmethod
    def _compute_vehicle_affinity(
        cls, req_brand: str, req_model: str, hist_brand: str, hist_model: str
    ) -> float:
        """Memberikan bonus afinitas jika merk dan model kendaraan sama."""
        b1, b2 = req_brand.strip().lower(), (hist_brand or "").strip().lower()
        m1, m2 = req_model.strip().lower(), (hist_model or "").strip().lower()

        if b1 and b1 == b2:
            if m1 and (m1 in m2 or m2 in m1):
                return 1.0  # Merk & Model cocok
            return 0.5  # Merk sama, model berbeda
        return 0.0

    @classmethod
    async def diagnose(
        cls, session: AsyncSession, payload: DiagnosticRequest
    ) -> DiagnosticResponse:
        """
        Menjalankan evaluasi kasus historis & rule pakar untuk menghasilkan ranking
        titik pemeriksaan (`FaultCheckpoint`) dengan persentase probabilitas (0 - 100%).
        """
        query_tokens = preprocess_symptom_tokens(payload.symptom_text)
        query_dtcs = parse_dtc_codes(payload.dtc_codes)

        # 1. Ambil seluruh Checkpoint beserta Kategori
        cp_stmt = select(FaultCheckpoint, FaultCategory.name).join(
            FaultCategory, FaultCheckpoint.category_id == FaultCategory.id
        )
        cp_rows = (await session.execute(cp_stmt)).all()
        if not cp_rows:
            return DiagnosticResponse(
                brand=payload.brand,
                model=payload.model,
                normalized_tokens=query_tokens,
                input_dtc_codes=sorted(query_dtcs),
                total_historical_cases_scanned=0,
                recommendations=[],
            )

        aggregators: dict[int, _CheckpointAggregator] = {
            cp.id: _CheckpointAggregator(checkpoint=cp, category_name=cat_name)
            for cp, cat_name in cp_rows
        }

        # 2. Ambil seluruh FaultHistory yang sudah terverifikasi dan SymptomCheckpointLink
        hist_stmt = select(FaultHistory).where(FaultHistory.is_verified.is_(True))
        histories: Sequence[FaultHistory] = (await session.execute(hist_stmt)).scalars().all()

        link_stmt = select(SymptomCheckpointLink)
        links: Sequence[SymptomCheckpointLink] = (await session.execute(link_stmt)).scalars().all()

        # 3. Bangun kamus IDF (Inverse Document Frequency) dari korpus riwayat + links
        doc_freq: dict[str, int] = defaultdict(int)
        total_docs = len(histories) + len(links) + 1
        history_tokens_cache: list[tuple[FaultHistory, list[str], set[str]]] = []

        for h in histories:
            h_tokens = preprocess_symptom_tokens(h.symptom_text)
            h_dtcs = parse_dtc_codes(h.dtc_codes)
            history_tokens_cache.append((h, h_tokens, h_dtcs))
            for tok in set(h_tokens):
                doc_freq[tok] += 1

        link_tokens_cache: list[tuple[SymptomCheckpointLink, list[str], set[str]]] = []
        for lnk in links:
            l_tokens = preprocess_symptom_tokens(lnk.symptom_keyword)
            l_dtcs = parse_dtc_codes(lnk.dtc_code)
            link_tokens_cache.append((lnk, l_tokens, l_dtcs))
            for tok in set(l_tokens):
                doc_freq[tok] += 1

        idf_map: dict[str, float] = {
            term: math.log((total_docs + 1) / (df + 1)) + 1.0
            for term, df in doc_freq.items()
        }

        # 4. Evaluasi kesamaan terhadap setiap kasus di `FaultHistory`
        for h, h_tokens, h_dtcs in history_tokens_cache:
            agg = aggregators.get(h.resolved_checkpoint_id)
            if not agg:
                continue

            text_sim, matched_kw = cls._compute_tfidf_cosine_and_overlap(
                query_tokens, h_tokens, idf_map
            )
            dtc_sim, matched_dtc = cls._compute_dtc_similarity(query_dtcs, h_dtcs)
            veh_sim = cls._compute_vehicle_affinity(
                payload.brand, payload.model, h.brand, h.model
            )

            # Abaikan riwayat yang sama sekali tidak memiliki irisan gejala maupun DTC
            if text_sim < 0.08 and dtc_sim == 0.0:
                continue

            # Jika user tidak memasukkan DTC, distribusikan bobot DTC ke kemiripan gejala teks
            if query_dtcs:
                case_score = (
                    (cls.WEIGHT_SYMPTOM_SIMILARITY * text_sim)
                    + (cls.WEIGHT_DTC_MATCH * dtc_sim)
                    + (cls.WEIGHT_VEHICLE_AFFINITY * veh_sim)
                ) / (cls.WEIGHT_SYMPTOM_SIMILARITY + cls.WEIGHT_DTC_MATCH + cls.WEIGHT_VEHICLE_AFFINITY)
            else:
                case_score = (
                    (0.78 * text_sim) + (0.22 * veh_sim)
                )

            agg.history_score_sum += case_score
            agg.matched_cases_count += 1
            agg.matched_dtcs.update(matched_dtc)
            agg.matched_keywords.update(matched_kw)

            if case_score > agg.best_case_similarity:
                agg.best_case_similarity = case_score
                agg.best_resolution_note = h.resolution_notes

        # 5. Evaluasi terhadap aturan pakar `SymptomCheckpointLink` (Prior Knowledge)
        for lnk, l_tokens, l_dtcs in link_tokens_cache:
            agg = aggregators.get(lnk.checkpoint_id)
            if not agg:
                continue

            text_sim, matched_kw = cls._compute_tfidf_cosine_and_overlap(
                query_tokens, l_tokens, idf_map
            )
            dtc_sim, matched_dtc = cls._compute_dtc_similarity(query_dtcs, l_dtcs)

            if text_sim == 0.0 and dtc_sim == 0.0:
                continue

            raw_rule_match = max(text_sim, dtc_sim) if query_dtcs else text_sim
            weighted_rule = raw_rule_match * float(lnk.base_weight or 0.5)

            if weighted_rule > agg.prior_rule_max_score:
                agg.prior_rule_max_score = weighted_rule
            agg.matched_dtcs.update(matched_dtc)
            agg.matched_keywords.update(matched_kw)

        # 6. Hitung skor gabungan & normalisasi ke probabilitas (0 - 100%)
        scored_items: list[tuple[_CheckpointAggregator, float]] = []
        for agg in aggregators.values():
            if agg.matched_cases_count == 0 and agg.prior_rule_max_score == 0.0:
                continue

            # Rata-rata skor historis + boost logaritmik berdasarkan frekuensi kasus nyata
            avg_hist_score = (
                agg.history_score_sum / agg.matched_cases_count
                if agg.matched_cases_count > 0
                else 0.0
            )
            frequency_boost = min(0.25, 0.08 * math.log1p(agg.matched_cases_count))

            composite_raw = (
                (0.65 * max(avg_hist_score, agg.best_case_similarity))
                + (0.35 * agg.prior_rule_max_score)
                + frequency_boost
            )
            scored_items.append((agg, composite_raw))

        # Urutkan dari skor tertinggi
        scored_items.sort(key=lambda item: item[1], reverse=True)
        top_items = scored_items[: payload.top_k]

        # Normalisasi distribusi probabilitas menggunakan fungsi kalibrasi terukur
        total_raw = sum(score for _, score in top_items) or 1.0
        recommendations: list[CheckpointRecommendation] = []

        for idx, (agg, raw_score) in enumerate(top_items, start=1):
            # Kombinasi proporsi relatif dan tingkat kecocokan absolut agar persentase intuitif
            relative_share = raw_score / total_raw
            calibrated_prob = min(98.5, max(5.0, ((0.55 * min(raw_score, 1.0)) + (0.45 * relative_share)) * 100.0))
            prob_rounded = round(calibrated_prob, 1)

            if prob_rounded >= 70.0:
                conf_label = "HIGH"
            elif prob_rounded >= 40.0:
                conf_label = "MEDIUM"
            else:
                conf_label = "LOW"

            recommendations.append(
                CheckpointRecommendation(
                    rank=idx,
                    checkpoint_id=agg.checkpoint.id,
                    checkpoint_code=agg.checkpoint.code,
                    checkpoint_name=agg.checkpoint.name,
                    category_name=agg.category_name,
                    probability_percent=prob_rounded,
                    confidence_label=conf_label,
                    inspection_steps=agg.checkpoint.inspection_steps,
                    estimated_check_minutes=agg.checkpoint.estimated_check_minutes,
                    matched_historical_cases=agg.matched_cases_count,
                    matched_dtc_codes=sorted(agg.matched_dtcs),
                    matched_keywords=sorted(agg.matched_keywords),
                    sample_resolution_note=agg.best_resolution_note,
                )
            )

        return DiagnosticResponse(
            brand=payload.brand,
            model=payload.model,
            normalized_tokens=query_tokens,
            input_dtc_codes=sorted(query_dtcs),
            total_historical_cases_scanned=len(histories),
            recommendations=recommendations,
        )

    @classmethod
    async def record_resolution_and_learn(
        cls, session: AsyncSession, feedback: SelfLearningFeedbackRequest
    ) -> FaultHistory:
        """
        Loop Self-Learning:
        1. Menyimpan kasus yang baru diselesaikan ke tabel `FaultHistory` (is_verified=True).
        2. Memperbarui bobot `SymptomCheckpointLink` dengan Exponential Moving Average (EMA)
           atau membuat link baru jika pola gejala belum terpetakan.
        """
        veh_stmt = select(Vehicle).where(Vehicle.id == feedback.vehicle_id)
        vehicle = (await session.execute(veh_stmt)).scalar_one_or_none()
        brand = vehicle.brand if vehicle else "Unknown"
        model = vehicle.model if vehicle else "Unknown"

        clean_dtcs = sorted(parse_dtc_codes(feedback.dtc_codes))
        dtc_str = ",".join(clean_dtcs)
        tokens = preprocess_symptom_tokens(feedback.symptom_text)
        canonical_symptom_kw = " ".join(dict.fromkeys(tokens[:8]))  # Maks 8 kata kunci unik

        # 1. Tambahkan ke riwayat terverifikasi
        new_history = FaultHistory(
            vehicle_id=feedback.vehicle_id,
            brand=brand,
            model=model,
            symptom_text=feedback.symptom_text.strip(),
            dtc_codes=dtc_str,
            resolved_checkpoint_id=feedback.resolved_checkpoint_id,
            resolution_notes=feedback.resolution_notes.strip(),
            is_verified=True,
        )
        session.add(new_history)

        # 2. Update bobot prior pada `SymptomCheckpointLink`
        primary_dtc = clean_dtcs[0] if clean_dtcs else ""
        link_stmt = select(SymptomCheckpointLink).where(
            SymptomCheckpointLink.checkpoint_id == feedback.resolved_checkpoint_id
        )
        existing_links = (await session.execute(link_stmt)).scalars().all()

        matched_link: SymptomCheckpointLink | None = None
        for lnk in existing_links:
            lnk_tokens = set(preprocess_symptom_tokens(lnk.symptom_keyword))
            overlap = len(lnk_tokens.intersection(tokens))
            if (primary_dtc and lnk.dtc_code == primary_dtc) or overlap >= 2:
                matched_link = lnk
                break

        if matched_link:
            # Perkuat bobot menggunakan EMA menuju 0.98
            old_weight = float(matched_link.base_weight or 0.70)
            new_weight = min(0.98, (1.0 - cls.EMA_ALPHA) * old_weight + (cls.EMA_ALPHA * 1.0))
            matched_link.base_weight = round(new_weight, 4)

            # Perkaya kata kunci gejala baru yang belum ada di link tersebut
            merged_tokens = list(
                dict.fromkeys(preprocess_symptom_tokens(matched_link.symptom_keyword) + tokens)
            )[:12]
            matched_link.symptom_keyword = " ".join(merged_tokens)
            if primary_dtc and not matched_link.dtc_code:
                matched_link.dtc_code = primary_dtc
        else:
            # Buat pemetaan gejala-checkpoint baru secara otomatis
            new_link = SymptomCheckpointLink(
                checkpoint_id=feedback.resolved_checkpoint_id,
                symptom_keyword=canonical_symptom_kw or feedback.symptom_text.lower(),
                dtc_code=primary_dtc,
                base_weight=0.75,
            )
            session.add(new_link)

        # Jika terhubung ke WorkOrder, pastikan status catatan sinkron
        if feedback.work_order_id:
            wo_stmt = select(WorkOrder).where(WorkOrder.id == feedback.work_order_id)
            wo = (await session.execute(wo_stmt)).scalar_one_or_none()
            if wo and not wo.initial_dtc_codes and dtc_str:
                wo.initial_dtc_codes = dtc_str

        await session.flush()
        return new_history


# ===========================================================================
# 4. WEIGHED CASE SEARCH ENGINE (EXCEL FORMULA SPECIFICATION)
# ===========================================================================

class WeightedCaseSearchRequest(BaseModel):
    brand: str = Field(default="", description="Merk kendaraan (opsional)")
    model: str = Field(default="", description="Model kendaraan (opsional)")
    year: int | None = Field(default=None, ge=1980, le=2030, description="Tahun kendaraan untuk penentuan generasi & wiring")
    engine_code: str = Field(default="", description="Kode/varian mesin opsional (misal: K14B, K15B, 1NR-VE)")
    odometer_km: int | None = Field(default=None, ge=0, description="Data kilometer tempuh kendaraan (kelipatan 100 km)")
    complaint: str = Field(default="", description="Keluhan pelanggan (misal: Mesin brebet saat idle)")
    symptom: str = Field(default="", description="Gejala teknis (misal: RPM naik turun tidak stabil)")
    dtc: str = Field(default="", description="Kode DTC OBD-II (misal: P0171, P0131)")
    stft: float | None = Field(default=None, description="Short Term Fuel Trim (%)")
    ltft: float | None = Field(default=None, description="Long Term Fuel Trim (%)")
    rpm: float | None = Field(default=None, description="RPM Idle")
    o2: float | None = Field(default=None, description="Tegangan Sensor O2 (V), contoh: 0.45")
    map_kpa: float | None = Field(default=None, description="Tekanan Manifold MAP (kPa)")
    maf_gps: float | None = Field(default=None, description="Aliran Udara MAF (g/s)")
    ect_c: float | None = Field(default=None, description="Suhu Air Pendingin ECT (°C)")
    # Live Data Khusus Diesel Common-Rail
    rail_pressure_mpa: float | None = Field(default=None, description="Tekanan Fuel Rail Common-Rail (MPa)")
    boost_kpa: float | None = Field(default=None, description="Tekanan Boost Turbo Absolut (kPa)")
    inj_feedback_mm3: float | None = Field(default=None, description="Koreksi Injektor Diesel (mm³/st)")
    egr_pct: float | None = Field(default=None, description="Posisi Bukaan Katup EGR (%)")
    # Live Data Khusus Hybrid / EV
    hv_soc_pct: float | None = Field(default=None, description="State of Charge Baterai HV (%)")
    hv_cell_delta_mv: float | None = Field(default=None, description="Selisih Tegangan Sel Baterai HV (mV)")
    hv_insulation_mohm: float | None = Field(default=None, description="Tahanan Isolasi Sistem HV (MOhm)")
    hv_temp_c: float | None = Field(default=None, description="Suhu Baterai / Inverter HV (°C)")
    system_filter: str | None = Field(default=None, description="Filter sistem: Udara, Bahan Bakar, Pendingin, dll.")


class ManualRepairAdvice(BaseModel):
    diagnosis_title: str
    system_category: str
    group_category: str
    manual_book_section: str
    cause_summary: str
    cause_items: list[dict[str, str]] = []
    repair_options: list[dict[str, str]] = []
    step_by_step_repair: list[str]
    sensor_standards: list[dict[str, str]]
    idle_standards: list[dict[str, str]] = []
    scanner_standards: list[dict[str, str]] = []
    sim_circuit_key: str | None = None
    atlas_module_id: str | None = None
    wiring_ref_id: str | None = None
    oem_wiring_image: str | None = None
    shared_with_dtcs: list[str] = []
    wiring_cross_ref_note: str | None = None
    atlas_photo_index: int = 0
    connector: dict[str, Any] | None = None
    verification_status: str = "VERIFIED_OEM"
    manual_page_ref: str | None = None
    wiring_pinout: list[dict[str, str]]
    relearn_reset_steps: list[str]
    is_pinout_verified: bool = True
    active_pack_id: str = "universal"
    safety_warning: str | None = None
    hv_safety_warning: str | None = None
    is_low_confidence_fallback: bool = False
    adaptive_live_findings: list[dict[str, str]] = []
    customer_summary: str | None = None


class WeightedCaseMatchItem(BaseModel):
    rank: int
    case_code: str
    brand: str
    model: str
    year: int | None
    engine_capacity: str | None
    engine_code: str | None = None
    odometer_km: int | None = None
    km_diff: int | None = None
    year_diff: int | None = None
    license_plate: str | None = None
    mechanic_name: str | None = None
    verification_status: str = "TERVERIFIKASI"
    complaint: str
    symptom: str
    dtc: str
    final_diagnosis: str
    repair_action: str
    system_category: str
    group_category: str
    text_score: float
    live_score: float | None
    total_score: float
    category_label: str
    inspection_findings: str
    manual_advice: ManualRepairAdvice | None = None


class SystemScoreSummary(BaseModel):
    system_name: str
    group_name: str
    parameters_checked: str
    cases_count: int
    top_score: float
    category_label: str
    top_diagnosis: str
    top_case_code: str


class WeightedCaseSearchResponse(BaseModel):
    top_headline: str
    top_case_code: str
    top_diagnosis: str
    top_score_percent: float
    top_category_label: str
    system_filter_applied: str | None
    ranked_matches: list[WeightedCaseMatchItem]
    system_summaries: list[SystemScoreSummary]
    direct_manual_advice: ManualRepairAdvice
    vehicle_applicability: VehicleApplicabilityInfo | None = None


class WeightedDiagnosticEngine:
    """
    Engine pencarian kasus diagnosa berbobot sesuai rumus baku spreadsheet bengkel:
    - Text Scoring: Merk (0.10) + Model (0.15) + Keluhan (0.20) + Gejala (0.20) + DTC (0.20)
    - Live Data Scoring: STFT (0.20, tol 5), LTFT (0.15, tol 5), RPM (0.10, tol 300),
      O2 (0.15, tol 0.15), MAP (0.15, tol 10), MAF (0.10, tol 2), ECT (0.15, tol 10)
    - Total Score = (1 - 0.15) * TextScore + 0.15 * LiveScore
    - Ambang Kategori: Sangat mirip (>=80%), Mirip (>=60%), Cukup mirip (>=40%), Kurang mirip (<40%)
    - Integrasi Solusi Manual Repair Book langsung pada hasil diagnosa.
    """

    SYSTEM_DEFINITIONS = [
        {"name": "Udara", "group": "Pembakaran", "params": "MAF, MAP, TPS, IAT"},
        {"name": "Bahan Bakar", "group": "Pembakaran", "params": "STFT, LTFT, O2/AFR, tekanan BBM, injector pulse"},
        {"name": "Pengapian", "group": "Pembakaran", "params": "Misfire counter, spark advance, busi, koil"},
        {"name": "Mekanis", "group": "Pembakaran", "params": "Kompresi silinder, vakum idle, timing chain/belt"},
        {"name": "Pendingin", "group": "Pendukung", "params": "ECT sensor, kerja kipas, thermostat, radiator"},
        {"name": "Pelumasan", "group": "Pendukung", "params": "Tekanan oli, level oli, switch tekanan oli"},
        {"name": "Kelistrikan", "group": "Pendukung", "params": "Tegangan aki, charging alternator, massa bodi"},
        {"name": "Emisi", "group": "Pendukung", "params": "O2 sensor downstream, catalytic converter, EVAP purge"},
    ]

    _DTC_SUBSYSTEM_FAMILIES: list[set[str]] = [
        {"P0030", "P0031", "P0032", "P0036", "P0037", "P0038", "P0130", "P0131", "P0132", "P0133", "P0134", "P0135", "P0136", "P0137", "P0138", "P0140", "P0141", "P2195", "P2196"},
        {"P0100", "P0101", "P0102", "P0103", "P0104"},
        {"P0105", "P0106", "P0107", "P0108", "P2227", "P2228", "P2229"},
        {"P0110", "P0111", "P0112", "P0113", "P0114"},
        {"P0115", "P0116", "P0117", "P0118", "P0119", "P0125", "P0128"},
        {"P0120", "P0121", "P0122", "P0123", "P0220", "P0222", "P0223", "P2101", "P2102", "P2103", "P2111", "P2119", "P2135", "P0506", "P0507"},
        {"P2122", "P2123", "P2127", "P2128", "P2138"},
        {"P0171", "P0174"},
        {"P0172", "P0175"},
        {"P0200", "P0201", "P0202", "P0203", "P0204", "P0205", "P0206"},
        {"P0300", "P0301", "P0302", "P0303", "P0304", "P0305", "P0306"},
        {"P0325", "P0327", "P0328"},
        {"P0335", "P0336", "P0340", "P0341"},
        {"P0350", "P0351", "P0352", "P0353", "P0354"},
        {"P0400", "P0401", "P0402", "P0403", "P0404"},
        {"P0420", "P0430"},
        {"P0440", "P0441", "P0442", "P0443", "P0446", "P0455", "P0456"},
        {"P0480", "P0481", "P0482", "P0483", "P0484", "P0485"},
    ]

    STANDARD_OBD_FALLBACK: dict[str, dict[str, str]] = {
        "P0481": {
            "system": "Engine / Powertrain (ECM) — Cooling Fan Control",
            "description_id": "Sirkuit Kontrol Kipas Radiator 2 (High Speed / Sub Fan)",
            "possible_causes": "Relay Kipas Radiator No. 2 putus/macet, sekering kipas putus, motor kipas No. 2 rusak, atau kabel kontrol E23-47 (RED) ke ECM putus/hubung singkat.",
            "severity_level": "HIGH",
        },
        "P0482": {
            "system": "Engine / Powertrain (ECM) — Cooling Fan Control",
            "description_id": "Sirkuit Kontrol Kipas Radiator 3",
            "possible_causes": "Relay atau kabel kontrol kipas pendingin 3 putus/konslet.",
            "severity_level": "HIGH",
        },
        "P0105": {
            "system": "Engine / Powertrain (ECM) — MAP / Barometric Pressure",
            "description_id": "Malfungsi Sirkuit Sensor Tekanan Udara Intake (MAP Sensor)",
            "possible_causes": "Selang vakum sensor MAP bocor/lepas, suplai +5V atau ground sensor MAP putus, atau sensor MAP rusak.",
            "severity_level": "HIGH",
        },
        "P0106": {
            "system": "Engine / Powertrain (ECM) — MAP / Barometric Pressure",
            "description_id": "Rentang / Kinerja Sirkuit Sensor MAP Tidak Sesuai Spesifikasi",
            "possible_causes": "Lubang vakum MAP tersumbat jelaga, kebocoran vakum intake, atau sensor MAP meleset.",
            "severity_level": "MEDIUM",
        },
        "P0136": {
            "system": "Engine / Powertrain (ECM) — HO2S-2 (Bank 1 Sensor 2)",
            "description_id": "Malfungsi Sirkuit Sensor Oksigen Belakang (HO2S-2 / Bank 1 Sensor 2)",
            "possible_causes": "Sensor HO2S-2 belakang rusak, kabel sinyal/heater terbakar knalpot, atau kebocoran gas buang sebelum sensor belakang.",
            "severity_level": "MEDIUM",
        },
        "P0137": {
            "system": "Engine / Powertrain (ECM) — HO2S-2 (Bank 1 Sensor 2)",
            "description_id": "Tegangan Sirkuit Sensor Oksigen Belakang Terlalu Rendah (HO2S-2 Low)",
            "possible_causes": "Kabel sinyal HO2S-2 hubung singkat ke massa, kebocoran knalpot, atau sensor HO2S-2 mati.",
            "severity_level": "MEDIUM",
        },
        "P0138": {
            "system": "Engine / Powertrain (ECM) — HO2S-2 (Bank 1 Sensor 2)",
            "description_id": "Tegangan Sirkuit Sensor Oksigen Belakang Terlalu Tinggi (HO2S-2 High)",
            "possible_causes": "Kabel sinyal HO2S-2 hubung singkat ke +B/heater, massa sensor putus, atau sensor HO2S-2 rusak.",
            "severity_level": "MEDIUM",
        },
        "P0141": {
            "system": "Engine / Powertrain (ECM) — HO2S-2 Heater",
            "description_id": "Malfungsi Sirkuit Pemanas (Heater) Sensor Oksigen Belakang (HO2S-2)",
            "possible_causes": "Elemen pemanas HO2S-2 putus (OL), suplai +12V Main Relay hilang, atau kabel kontrol heater ECM putus.",
            "severity_level": "MEDIUM",
        },
        "P0128": {
            "system": "Engine / Powertrain (ECM) — Cooling System",
            "description_id": "Suhu Kerja Coolant di Bawah Temperatur Regulasi Thermostat",
            "possible_causes": "Thermostat macet terbuka (stuck open) atau sensor ECT (C37-24) membaca terlalu dingin.",
            "severity_level": "MEDIUM",
        },
        "P0201": {"system": "Engine / Powertrain (ECM) — Fuel Injector", "description_id": "Sirkuit Injektor Silinder 1 Putus / Bermasalah", "possible_causes": "Koil injektor No.1 putus (normal 11.5-14.5 Ohm), soket injektor kendor, atau jalur pulsa ground ECM putus.", "severity_level": "HIGH"},
        "P0202": {"system": "Engine / Powertrain (ECM) — Fuel Injector", "description_id": "Sirkuit Injektor Silinder 2 Putus / Bermasalah", "possible_causes": "Koil injektor No.2 putus (normal 11.5-14.5 Ohm), soket injektor kendor, atau jalur pulsa ground ECM putus.", "severity_level": "HIGH"},
        "P0203": {"system": "Engine / Powertrain (ECM) — Fuel Injector", "description_id": "Sirkuit Injektor Silinder 3 Putus / Bermasalah", "possible_causes": "Koil injektor No.3 putus (normal 11.5-14.5 Ohm), soket injektor kendor, atau jalur pulsa ground ECM putus.", "severity_level": "HIGH"},
        "P0204": {"system": "Engine / Powertrain (ECM) — Fuel Injector", "description_id": "Sirkuit Injektor Silinder 4 Putus / Bermasalah", "possible_causes": "Koil injektor No.4 putus (normal 11.5-14.5 Ohm), soket injektor kendor, atau jalur pulsa ground ECM putus.", "severity_level": "HIGH"},
        "P0230": {"system": "Engine / Powertrain (ECM) — Fuel Pump", "description_id": "Sirkuit Primer Relay Pompa Bensin (Fuel Pump Primary Circuit)", "possible_causes": "Relay Fuel Pump rusak, sekering pompa bensin putus, atau jalur kontrol E23-15 (WHT/GRN) dari ECM putus.", "severity_level": "CRITICAL"},
        "P0351": {"system": "Engine / Powertrain (ECM) — Ignition System", "description_id": "Sirkuit Primer/Sekunder Ignition Coil 'A' (Silinder 1)", "possible_causes": "Ignition coil No.1 mati, soket 3/4-pin koil kendor, atau kabel trigger IGT1 dari ECM putus.", "severity_level": "HIGH"},
        "P0352": {"system": "Engine / Powertrain (ECM) — Ignition System", "description_id": "Sirkuit Primer/Sekunder Ignition Coil 'B' (Silinder 2)", "possible_causes": "Ignition coil No.2 mati, soket koil kendor, atau kabel trigger IGT2 dari ECM putus.", "severity_level": "HIGH"},
        "P0353": {"system": "Engine / Powertrain (ECM) — Ignition System", "description_id": "Sirkuit Primer/Sekunder Ignition Coil 'C' (Silinder 3)", "possible_causes": "Ignition coil No.3 mati, soket koil kendor, atau kabel trigger IGT3 dari ECM putus.", "severity_level": "HIGH"},
        "P0354": {"system": "Engine / Powertrain (ECM) — Ignition System", "description_id": "Sirkuit Primer/Sekunder Ignition Coil 'D' (Silinder 4)", "possible_causes": "Ignition coil No.4 mati, soket koil kendor, atau kabel trigger IGT4 dari ECM putus.", "severity_level": "HIGH"},
        "P0560": {"system": "Engine / Powertrain (ECM) — Charging / Power", "description_id": "Tegangan Sistem Kelistrikan Tidak Normal (System Voltage Malfunction)", "possible_causes": "Aki soak, alternator overcharge/undercharge, atau kabel suplai utama E23-01 / backup E23-02 korosi.", "severity_level": "MEDIUM"},
        "P0562": {"system": "Engine / Powertrain (ECM) — Charging / Power", "description_id": "Tegangan Sistem Kelistrikan Terlalu Rendah (< 10.5V)", "possible_causes": "Alternator tidak mengisi, aki lemah, atau terminal massa mesin kendur.", "severity_level": "HIGH"},
        "P0563": {"system": "Engine / Powertrain (ECM) — Charging / Power", "description_id": "Tegangan Sistem Kelistrikan Terlalu Tinggi (> 16.0V)", "possible_causes": "IC Regulator alternator rusak (overcharging).", "severity_level": "HIGH"},
    }

    @classmethod
    def _are_same_dtc_subsystem(cls, c1: str, c2: str) -> bool:
        if c1 == c2:
            return True
        for fam in cls._DTC_SUBSYSTEM_FAMILIES:
            if c1 in fam and c2 in fam:
                return True
        return False

    _JB420_CATALOG_CACHE: dict[str, dict[str, Any]] | None = None

    @classmethod
    def _get_jb420_dtc_catalog_map(cls) -> dict[str, dict[str, Any]]:
        if cls._JB420_CATALOG_CACHE is not None:
            return cls._JB420_CATALOG_CACHE
        candidates = [
            Path(__file__).resolve().parent.parent / "jb420_extracted_catalog.json",
            Path("./app/jb420_extracted_catalog.json"),
            Path("./jb420_extracted_catalog.json"),
        ]
        mapping: dict[str, dict[str, Any]] = {}
        for p in candidates:
            if p.exists():
                try:
                    raw = json.loads(p.read_text(encoding="utf-8"))
                    for item in raw.get("dtc_catalog", []):
                        code_u = str(item.get("code", "")).strip().upper()
                        if code_u:
                            mapping[code_u] = item
                    break
                except Exception:
                    pass
        cls._JB420_CATALOG_CACHE = mapping
        return mapping

    @classmethod
    def _extract_all_request_dtcs(cls, req: WeightedCaseSearchRequest) -> list[str]:
        codes = split_dtc_codes(req.dtc)
        combined = f"{req.dtc or ''} {req.complaint or ''} {req.symptom or ''}".upper()
        for raw_match in re.findall(r"\b([PCBU][0-9A-F]{4})(?:-?[0-9A-F]{2})?\b", combined):
            if raw_match not in codes:
                codes.append(raw_match)
        for kls_match in re.findall(r"\bKLS-(\d{1,2})\b", combined):
            k_code = f"KLS-{kls_match}"
            if k_code not in codes:
                codes.append(k_code)
        for no_match in re.findall(r"\bDTC\s*NO\.?\s*(\d{1,2})\b", combined):
            k_code = f"KLS-{no_match}"
            if k_code not in codes:
                codes.append(k_code)
        return codes

    @classmethod
    def _calculate_text_similarity(
        cls,
        req: WeightedCaseSearchRequest,
        case: HistoricalCase,
    ) -> float:
        """
        Menghitung skor kemiripan kasus berbobot PRD v2.2.0 (REQ-14):
        S_total = (0.10*S_merek + 0.15*S_model + 0.10*S_tahun + 0.15*S_km
                   + 0.25*S_keluhan + 0.25*S_dtc) / sum(active_weights)
        Dengan redistribusi bobot otomatis bila variabel (mis. DTC/KM/Tahun) kosong.
        """
        weighted_sum = 0.0
        active_weight = 0.0

        def _norm_eng(val: str | None) -> str:
            return re.sub(r"[^a-z0-9]", "", (val or "").lower())

        req_eng = _norm_eng(req.engine_code)
        case_eng = _norm_eng(getattr(case, "engine_code", None))

        # Kelompok platform lintas-merek (Toyota-Daihatsu, Suzuki-Mazda, Mitsubishi-Nissan)
        shared_platform_pairs = [
            ({"toyota", "daihatsu"}, {"avanza", "xenia", "rush", "terios", "agya", "ayla", "calya", "sigra", "raize", "rocky"}),
            ({"suzuki", "mazda"}, {"ertiga", "vx-1", "vx1"}),
            ({"mitsubishi", "nissan"}, {"xpander", "livina"}),
        ]

        # 1. Merek (Bobot 0.10): persis = 1.0 | satu platform/kode mesin lintas merek = 0.8 | beda = 0.0
        if req.brand.strip():
            b_req = req.brand.strip().lower()
            b_case = (case.brand or "").strip().lower()
            m_req_low = (req.model or "").strip().lower()
            m_case_low = (case.model or "").strip().lower()
            sim_brand = 0.0
            if b_req == b_case or b_req in b_case or b_case in b_req:
                sim_brand = 1.0
            elif req_eng and case_eng and req_eng == case_eng:
                sim_brand = 0.8
            else:
                for brands_set, models_set in shared_platform_pairs:
                    if b_req in brands_set and b_case in brands_set:
                        if any(t in m_req_low for t in models_set) and any(t in m_case_low for t in models_set):
                            sim_brand = 0.8
                            break
            weighted_sum += 0.10 * sim_brand
            active_weight += 0.10

        # 2. Model (Bobot 0.15): persis = 1.0 | sebagian token cocok = 0.7 | beda = 0.0
        if req.model.strip():
            m_req_str = req.model.strip().lower()
            m_case_str = (case.model or "").strip().lower()
            m_req_toks = set(re.findall(r"[a-z0-9]+", m_req_str))
            m_case_toks = set(re.findall(r"[a-z0-9]+", m_case_str))
            sim_model = 0.0
            if m_req_str == m_case_str:
                sim_model = 1.0
            elif m_req_toks and m_case_toks:
                overlap = m_req_toks.intersection(m_case_toks)
                if overlap:
                    sim_model = 1.0 if m_req_toks == m_case_toks else 0.7
            weighted_sum += 0.15 * sim_model
            active_weight += 0.15

        # 3. Kedekatan Tahun (Bobot 0.10): max(0, 1 - |T_input - T_kasus| / 10)
        if req.year is not None and case.year is not None:
            sim_year = max(0.0, 1.0 - (abs(int(req.year) - int(case.year)) / 10.0))
            weighted_sum += 0.10 * sim_year
            active_weight += 0.10

        # 4. Kedekatan Kilometer (Bobot 0.15): max(0, 1 - |KM_input - KM_kasus| / 50000)
        case_km = getattr(case, "odometer_km", None)
        if req.odometer_km is not None and case_km is not None:
            sim_km = max(0.0, 1.0 - (abs(int(req.odometer_km) - int(case_km)) / 50000.0))
            weighted_sum += 0.15 * sim_km
            active_weight += 0.15

        # 5. Keluhan & Gejala (Bobot 0.25): Jaccard Similarity pasca normalisasi sinonim bengkel
        req_text = f"{req.complaint or ''} {req.symptom or ''}".strip()
        if req_text:
            c_req = set(preprocess_symptom_tokens(req_text))
            c_case = set(preprocess_symptom_tokens(f"{case.complaint or ''} {case.symptom or ''}"))
            sim_complaint = 0.0
            if c_req and c_case:
                union_cnt = len(c_req.union(c_case))
                sim_complaint = (len(c_req.intersection(c_case)) / union_cnt) if union_cnt > 0 else 0.0
            weighted_sum += 0.25 * sim_complaint
            active_weight += 0.25

        # 6. Kode DTC (Bobot 0.25): persis = 1.0 | satu keluarga subsistem = 0.6 | beda = 0.0
        # Jika input DTC kosong -> bobot 0.25 otomatis diredistribusikan ke variabel aktif lain!
        req_codes = set(cls._extract_all_request_dtcs(req))
        case_codes = set(split_dtc_codes(case.dtc))
        sim_dtc: float | None = None
        if req_codes:
            if not case_codes:
                sim_dtc = 0.0
            else:
                matched = 0.0
                for code in req_codes:
                    if code in case_codes:
                        matched += 1.0
                    elif any(cls._are_same_dtc_subsystem(code, other) for other in case_codes):
                        matched += 0.60
                sim_dtc = min(matched / max(len(req_codes), len(case_codes)), 1.0)
            weighted_sum += 0.25 * sim_dtc
            active_weight += 0.25

        if active_weight <= 0.0:
            return 0.0

        normalized_score = min(max(weighted_sum / active_weight, 0.0), 1.0)
        # Penalti moderat bila pengguna memasukkan DTC spesifik tapi kasus historis tidak cocok subsistem
        if req_codes and sim_dtc == 0.0:
            normalized_score *= 0.45
        return normalized_score

    @classmethod
    def _build_customer_summary(
        cls,
        advice: ManualRepairAdvice,
        app_info: VehicleApplicabilityInfo,
        req_codes: list[str],
    ) -> str:
        """Menghasilkan ringkasan bahasa awam yang mudah dipahami pemilik mobil (REQ-07)."""
        veh_name = f"{app_info.brand} {app_info.model}".strip() or "kendaraan Anda"
        sys_cat = (advice.system_category or "mesin").lower()
        code_txt = f" (kode komputer {', '.join(req_codes[:2])})" if req_codes else ""
        first_action = ""
        if advice.repair_options:
            first_action = str(advice.repair_options[0].get("title", "")).strip()

        if "pengapian" in sys_cat or any(c.startswith(("P030", "P035")) for c in req_codes):
            core = (
                f"Sistem pengapian (busi atau koil pemantik api) pada {veh_name} terdeteksi tidak membakar bensin secara sempurna{code_txt}, "
                "sehingga mesin terasa bergetar/pincang dan tenaga berkurang."
            )
        elif "udara" in sys_cat or any(c in {"P0171", "P0101", "P0105", "P0107", "P0507"} for c in req_codes):
            core = (
                f"Aliran udara yang masuk ke mesin {veh_name} tidak seimbang{code_txt}—umumnya karena selang udara/vakum bocor, "
                "kotoran pada saluran throttle, atau sensor pembaca udara kotor sehingga mesin terasa brebet dan boros BBM."
            )
        elif "pendingin" in sys_cat or any(c.startswith(("P011", "P0128", "P048")) for c in req_codes):
            core = (
                f"Sistem pendingin mesin {veh_name} (sensor suhu air atau kipas radiator) terdeteksi bermasalah{code_txt}. "
                "Segera ditangani agar suhu mesin tetap aman dan terhindar dari overheat."
            )
        elif "bahan bakar" in sys_cat or "emisi" in sys_cat or any(c.startswith(("P013", "P014", "P003", "P0172", "P0087")) for c in req_codes):
            core = (
                f"Pengaturan campuran bahan bakar atau sensor gas buang pada {veh_name} perlu diperiksa{code_txt}. "
                "Perbaikan akan mengembalikan tarikan mesin agar halus kembali sekaligus menghemat konsumsi bahan bakar."
            )
        elif app_info.resolved_fuel_type in {"EV", "Hybrid"}:
            core = (
                f"Sistem kelistrikan tegangan tinggi (Hybrid/EV) pada {veh_name} mencatat peringatan keamanan{code_txt}. "
                "Pemeriksaan wajib dilakukan teknisi bersertifikat menggunakan alat isolasi khusus."
            )
        else:
            core = (
                f"Komputer mesin {veh_name} mendeteksi gangguan pada bagian {advice.system_category or 'mesin'}{code_txt} "
                f"({advice.diagnosis_title})."
            )

        rec = (
            f" Langkah yang disarankan bengkel: {first_action}, lalu lakukan uji jalan untuk memastikan lampu indikator tidak menyala kembali."
            if first_action
            else " Mekanik akan melakukan pengukuran komponen terkait terlebih dahulu sebelum penggantian suku cadang."
        )
        return core + rec

    @classmethod
    def _calculate_live_similarity(
        cls,
        req: WeightedCaseSearchRequest,
        case: HistoricalCase,
    ) -> float | None:
        """Menghitung skor live data dengan toleransi per parameter."""
        weights_config = [
            ("stft", req.stft, case.stft, 0.20, 5.0),
            ("ltft", req.ltft, case.ltft, 0.15, 5.0),
            ("rpm", req.rpm, case.rpm, 0.10, 300.0),
            ("map_kpa", req.map_kpa, case.map_kpa, 0.15, 10.0),
            ("maf_gps", req.maf_gps, case.maf_gps, 0.10, 2.0),
            ("ect_c", req.ect_c, case.ect_c, 0.15, 10.0),
        ]

        active_weights = 0.0
        weighted_score_sum = 0.0

        for param_name, req_val, case_val, weight, tol in weights_config:
            if req_val is not None and case_val is not None:
                diff = abs(float(req_val) - float(case_val))
                sim_param = max(0.0, 1.0 - (diff / tol))
                weighted_score_sum += weight * sim_param
                active_weights += weight

        # O2 voltage check jika diisi angka
        if req.o2 is not None and case.o2_voltage:
            try:
                # Parse rata-rata rentang O2 misal "0,15–0,85 V"
                clean_o2 = case.o2_voltage.replace("V", "").replace(",", ".").replace("–", "-")
                parts = [float(p.strip()) for p in clean_o2.split("-") if p.strip()]
                if parts:
                    case_o2_avg = sum(parts) / len(parts)
                    diff_o2 = abs(float(req.o2) - case_o2_avg)
                    sim_o2 = max(0.0, 1.0 - (diff_o2 / 0.15))
                    weighted_score_sum += 0.15 * sim_o2
                    active_weights += 0.15
            except Exception:
                pass

        if active_weights <= 0:
            return None

        return min(weighted_score_sum / active_weights, 1.0)

    @classmethod
    def _determine_category(cls, score: float) -> str:
        if score >= 0.80:
            return "Sangat mirip"
        elif score >= 0.60:
            return "Mirip"
        elif score >= 0.40:
            return "Cukup mirip"
        return "Kurang mirip"

    @classmethod
    def get_repair_manual_guidance(cls, diagnosis: str, dtc: str | None = None) -> ManualRepairAdvice:
        """
        Menghasilkan panduan perbaikan resmi manual repair book yang terstruktur dan aplikatif
        berdasarkan diagnosis kerusakan mobil yang terdeteksi.
        """
        diag_clean = (diagnosis or "").lower()
        dtc_clean = (dtc or "").upper()
        dtc_codes = set(split_dtc_codes(dtc_clean))

        if (
            "vakum" in diag_clean
            or "selang intake" in diag_clean
            or re.search(r"\bmap\b|manifold\s*absolute|tekanan\s*manifold", diag_clean)
            or bool(dtc_codes & {"P0171", "P0105", "P0106", "P0107", "P0108", "P0109"})
        ):
            is_map_dtc = bool(dtc_codes & {"P0105", "P0106", "P0107", "P0108", "P0109"})
            return ManualRepairAdvice(
                diagnosis_title=(
                    "Gangguan Sirkuit Sensor Tekanan Udara Intake (MAP Sensor)"
                    if is_map_dtc
                    else "Kebocoran Udara / Vakum pada Saluran Intake (Lean Mixture)"
                ),
                system_category="Udara",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Resmi Suzuki Grand Vitara JB420 Bab 1A-68 (MAP / Air Metering) & Bab 1D (Intake Manifold)",
                cause_summary=(
                    "Sensor MAP gagal membaca tekanan vakum intake manifold akibat suplai +5V (C37-14) atau sinyal (C37-55) terputus, selang vakum pecah, atau sensor MAP rusak."
                    if is_map_dtc
                    else "Udara liar (unmetered air) bocor masuk ke intake manifold setelah sensor MAF, menyebabkan campuran bensin terlalu kurus (Lean - P0171) dan mesin brebet saat idle."
                ),
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Selang Vakum & Gasket Intake Manifold Bocor", "desc": "Selang vakum booster rem, selang PCV, atau paking intake manifold getas/retak sehingga menghisap udara luar."},
                    {"badge": "Penyebab #2", "title": "Sensor Tekanan Intake (MAP) / MAF Kotor atau Rusak", "desc": "Lubang vakum sensor MAP tersumbat jelaga oli atau kawat sensor MAF kotor sehingga bacaan beban mesin meleset."},
                    {"badge": "Penyebab #3", "title": "Tekanan Pompa Bensin Lemah / Soket 3-Pin MAP Kendor", "desc": "Suplai tekanan fuel rail turun (< 3.0 bar) atau kabel referensi +5V / massa sensor putus."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Vakum & MAP)", "title": "Periksa Selang Vakum & Sensor MAP 3-Pin", "desc": "Ganti selang vakum/PCV retak dan uji tegangan +5V (C37-14), sinyal output (C37-55), serta ground (C37-57) pada soket MAP."},
                    {"tag": "Opsi 2 • Sensor Udara", "title": "Bersihkan Sensor MAF & Cek Belalai Karet Intake", "desc": "Semprot elemen sensor MAF dengan MAF cleaner khusus dan pastikan karet belalai udara tidak sobek."},
                    {"tag": "Opsi 3 • Sistem BBM", "title": "Servis Injektor & Periksa Tekanan Fuel Pump / Filter Bensin", "desc": "Ukur tekanan fuel rail (standar 3.0–3.5 bar), ganti filter bensin, atau servis injektor yang tersumbat."},
                ],
                sensor_standards=[
                    {"parameter": "Tekanan Manifold MAP (Idle)", "normal_range": "30 - 42 kPa (~1.1 - 1.5 V)", "unit": "kPa"},
                    {"parameter": "Tegangan Referensi +5V MAP (C37-14)", "normal_range": "4.8 - 5.2 V (IG ON)", "unit": "V"},
                    {"parameter": "Short Term Fuel Trim (STFT)", "normal_range": "-10% s/d +10%", "unit": "%"},
                    {"parameter": "Long Term Fuel Trim (LTFT)", "normal_range": "-10% s/d +10%", "unit": "%"},
                ],
                wiring_pinout=[
                    {"pin": "C37-14 (Pin 1)", "signal": "GRY/RED — Sensor +5V Reference", "function": "Tegangan referensi 4.8–5.2 V dari regulator ECM (Bab 1A-15)"},
                    {"pin": "C37-55 (Pin 2)", "signal": "RED/WHT — MAP Sensor Signal Output", "function": "Sinyal tekanan manifold ke ECM (~3.9V KOEO | ~1.2V Idle)"},
                    {"pin": "C37-57 (Pin 3)", "signal": "GRY/GRN — Sensor Ground", "function": "Massa sensor referensi ECM (< 0.3 V / < 0.5 Ohm)"},
                ],
                step_by_step_repair=[
                    "1. Lakukan smoke test atau semprotkan sedikit intake cleaner di sepanjang selang vakum dan sambungan intake saat idle. Bila RPM naik, titik bocor terkonfirmasi.",
                    "2. Periksa selang vakum brake booster, selang PCV, dan selang pernapasan kanister EVAP dari keretakan atau kerapuhan.",
                    "3. Lepas klem selang menggunakan tang khusus, ganti selang vakum retak dengan selang berstandar SAE J30R7 (tahan panas/minyak).",
                    "4. Pastikan klem terpasang kuat pada posisi dudukannya tanpa meremas selang hingga robek.",
                ],
                relearn_reset_steps=[
                    "1. Sambungkan OBD-II scanner, lakukan 'Clear DTC P0171'.",
                    "2. Lakukan 'Reset Fuel Trim Learned Values' via scanner (atau lepas terminal minus aki selama 15 menit).",
                    "3. Hidupkan mesin tanpa beban kelistrikan (AC, lampu, audio OFF) hingga suhu air radiator mencapai 85-90°C.",
                    "4. Pantau live data: pastikan STFT dan LTFT kembali normal ke rentang -5% s/d +5%.",
                ],
            )
        elif "pcv" in diag_clean:
            return ManualRepairAdvice(
                diagnosis_title="Kebocoran / Kerusakan Katup PCV (Positive Crankcase Ventilation)",
                system_category="Udara",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Servis Bab 1B (Emission Control System - PCV Valve)",
                cause_summary="Katup ventilasi karter (PCV Valve) macet terbuka atau selang PCV pecah akibat uap oli panas, memicu kebocoran vakum dan mesin pincang saat idle.",
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Katup PCV Macet Terbuka (Tertahan Kerak Oli)", "desc": "Pegas katup satu arah PCV terganjal endapan lumpur oli sehingga udara terhisap terus-menerus ke intake."},
                    {"badge": "Penyebab #2", "title": "Selang Karet & Grommet PCV Getas / Pecah", "desc": "Karet selang penghubung tutup klep (valve cover) ke intake manifold mengeras dan sobek."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Ganti Part)", "title": "Ganti Katup PCV Baru & Selang Karet PCV", "desc": "Pasang katup PCV satu arah baru (torsi 12 N·m) beserta selang karet tahan panas/oli."},
                    {"tag": "Opsi 2 • Servis Bersih", "title": "Bersihkan Katup PCV, Saluran Breather & Reset ECU", "desc": "Semprot bersih kerak oli pada katup PCV dan lubang breather tutup klep bila pegas katup masih normal."},
                ],
                sensor_standards=[
                    {"parameter": "Vakum Intake saat Idle", "normal_range": "18 - 22 inHg (60 - 74 kPa vakum)", "unit": "inHg"},
                    {"parameter": "STFT Idle", "normal_range": "-10% s/d +10%", "unit": "%"},
                ],
                wiring_pinout=[
                    {"pin": "Bodi Mesin", "signal": "Ground Massa", "function": "Ground katup dan manifold bodi mesin"},
                ],
                step_by_step_repair=[
                    "1. Lepas katup PCV dari tutup klep (valve cover). Kocok katup: harus terdengar bunyi peluru klik-klik bebas di dalamnya. Jika macet, katup rusak/berkerak oli.",
                    "2. Tiup katup dari arah manifold: udara TIDAK BOLEH tembus (katup satu arah). Tiup dari arah klep: udara harus lolos.",
                    "3. Ganti katup PCV dan selang karet PCV jika mengeras atau retak.",
                    "4. Pasang katup PCV baru dengan torsi 12 N·m.",
                ],
                relearn_reset_steps=[
                    "1. Hapus memori adaptasi fuel trim ECU.",
                    "2. Nyalakan mesin dan amati kestabilan idle pada 750 ± 50 RPM.",
                ],
            )
        elif re.search(r"\bo2\b|oksigen|oxygen|lambda|a/f\s*sensor", diag_clean) or dtc_codes & {
            "P0030", "P0031", "P0032", "P0036", "P0037", "P0038",
            "P0130", "P0131", "P0132", "P0133", "P0134", "P0135", "P0136", "P0137", "P0138", "P0140", "P0141",
        }:
            is_rear_ho2s2 = bool(dtc_codes & {"P0036", "P0037", "P0038", "P0136", "P0137", "P0138", "P0140", "P0141"}) or "sensor 2" in diag_clean or "belakang" in diag_clean or "ho2s-2" in diag_clean
            return ManualRepairAdvice(
                diagnosis_title=(
                    "Gangguan Sensor Oksigen Belakang / HO2S-2 (Bank 1 Sensor 2 — 4-Pin C15)"
                    if is_rear_ho2s2
                    else "Gangguan A/F Sensor Depan / Bank 1 Sensor 1 (4-Pin JB420)"
                ),
                system_category="Bahan Bakar",
                group_category="Pembakaran",
                manual_book_section="Suzuki Grand Vitara JB420 Manual Vol 1 Bab 1A-54 / 1A-94 & Vol 2 Bab 9A-43 (A/F & HO2S 4-Pin)",
                cause_summary=(
                    "Elemen pemanas (heater) atau sel sensor HO2S-2 belakang (4-pin C15) putus/korslet, atau soket kabel terbakar panas knalpot."
                    if is_rear_ho2s2
                    else "Elemen pemanas (heater) atau sel sensor A/F Sensor-1 depan (4-pin 2x2: 2 Heater + 2 Sinyal A/F) mengalami putus/korslet, suplai HO2S Heater Relay hilang, atau sensor jenuh karbon."
                ),
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Elemen Heater Putus / Sensor Jenuh Karbon", "desc": "Kumparan pemanas internal sensor putus (OL) atau ujung elemen keramik tertutup jelaga tebal."},
                    {"badge": "Penyebab #2", "title": "Soket 4-Pin Kendor / Kabel Meleleh Terkena Knalpot", "desc": "Isolasi kabel sensor terkelupas atau hubung singkat karena menempel pada pipa exhaust manifold panas."},
                    {"badge": "Penyebab #3", "title": "Suplai +12V HO2S Heater Relay (#10 20A O2 HTR) Drop / Kebocoran Knalpot", "desc": "Suplai daya heater (+12V kabel PNK dari HO2S Heater Relay) terputus atau paking exhaust manifold bocor."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Ganti Sensor)", "title": f"Ganti {'HO2S-2 (Belakang, 4-Pin C15)' if is_rear_ho2s2 else 'A/F Sensor-1 (Depan, 4-Pin)'} Baru", "desc": "Ganti unit sensor yang putus heater/lemah menggunakan kunci soket 22 mm (torsi 44 N·m)."},
                    {"tag": "Opsi 2 • Kelistrikan & Soket", "title": "Perbaiki Kabel Harness, Soket 4-Pin & Cek HO2S Heater Relay (#10 20A)", "desc": "Pastikan suplai +12V heater dari HO2S Heater Relay (PNK) masuk normal dan kontrol PWM ECM (C37-32/47) tidak putus."},
                    {"tag": "Opsi 3 • BBM & Knalpot", "title": "Cek Kerapatan Paking Knalpot & Kualitas BBM", "desc": "Pastikan tidak ada kebocoran gas buang sebelum sensor dan gunakan BBM sesuai oktan mesin."},
                ],
                sensor_standards=(
                    [
                        {"parameter": "Voltase Sinyal HO2S-2 (C37-11 RED)", "normal_range": "0.10 - 0.90 V (Idle Hangat)", "unit": "V"},
                        {"parameter": "Suplai Heater +12V HO2S Heater Relay (PNK)", "normal_range": "10.0 - 14.0 V (IG ON)", "unit": "V"},
                        {"parameter": "Tahanan Pemanas HO2S-2 (20°C)", "normal_range": "5.0 - 7.0 Ohm", "unit": "Ohm"},
                    ]
                    if is_rear_ho2s2
                    else [
                        {"parameter": "Tahanan Heater A/F Sensor-1 (Pin 1–2 pada 20°C)", "normal_range": "2.3 - 4.3 Ohm (Soket 4-Pin)", "unit": "Ohm"},
                        {"parameter": "Suplai Heater +12V HO2S Heater Relay (Pin 1 PNK)", "normal_range": "10.0 - 14.0 V (IG ON)", "unit": "V"},
                        {"parameter": "A/F Signal (+) C37-38 WHT & (−) C37-37 BLK", "normal_range": "3.0-3.2 V (+) | 2.6-2.8 V (−)", "unit": "V"},
                    ]
                ),
                wiring_pinout=(
                    [
                        {"pin": "C37-57 (Pin 1)", "signal": "GRN — GND", "function": "Massa Sinyal HO2S-2 Belakang (< 0.3 V / < 1 Ω ke massa)"},
                        {"pin": "C37-11 (Pin 2)", "signal": "RED — O2 SIG", "function": "Sinyal Oksigen Hilir HO2S-2 (4.0–5.0 V bias IG ON · 0.10–0.90 V Idle Panas)"},
                        {"pin": "C37-47 (Pin 3)", "signal": "BLK/RED — HTR-", "function": "Kontrol Heater HO2S-2 PWM Low-Side dari ECM (10–14 V IG ON · Pulsa Idle)"},
                        {"pin": "O2 HTR RLY (Pin 4)", "signal": "PNK — HTR+", "function": "Suplai +12V Heater HO2S-2 dari HO2S Heater Relay (10–14 V IG ON)"},
                    ]
                    if is_rear_ho2s2
                    else [
                        {"pin": "O2 HTR RLY (Pin 1)", "signal": "PNK — HO2S HTR+", "function": "Suplai +12V Heater A/F dari HO2S Heater Relay / Sekring #10 20A O2 HTR (10–14 V IG ON)"},
                        {"pin": "C37-32 (Pin 2)", "signal": "PNK/BLU — HO2S HTR-", "function": "Kontrol Heater A/F Sensor-1 Low-Side PWM dari ECM (10–14 V IG ON · Pulsa saat Idle)"},
                        {"pin": "C37-38 (Pin 3)", "signal": "WHT — A/F (+)", "function": "Sinyal Utama A/F Sensor-1 (+) ke ECM (3.0–3.2 V saat Idle Panas)"},
                        {"pin": "C37-37 (Pin 4)", "signal": "BLK — A/F (-)", "function": "Sinyal Referensi A/F Sensor-1 (−) ke ECM (2.6–2.8 V saat Idle Panas)"},
                    ]
                ),
                step_by_step_repair=[
                    "1. Periksa kabel dan soket 4-pin sensor O2/A-F di exhaust manifold dari leleh/terbakar akibat panas knalpot.",
                    "2. Gunakan multimeter untuk mengukur tahanan heater pada 2 pin heater soket 4-pin sensor (A/F S1: 2.3–4.3 Ω · HO2S-2: 5–7 Ω). Bila putus/OL, sensor wajib ganti.",
                    "3. Periksa tegangan +12V pada kabel PNK dari HO2S Heater Relay (#10 20A O2 HTR) saat IG ON dan sinyal kontrol PWM ECM (C37-32/47).",
                    "4. Lepas sensor menggunakan kunci soket berbelah 22 mm, oleskan anti-seize tipis pada ulir sensor baru (jangan kena ujung sensor!), kencangkan torsi 44 N·m.",
                ],
                relearn_reset_steps=[
                    "1. Reset DTC P0131 dan reset fuel trim via scanner.",
                    "2. Jalankan kendaraan pada kecepatan konstan 60-80 km/jam selama 10 menit untuk melengkapi OBD-II O2 Monitor readiness.",
                ],
            )
        elif re.search(r"\bect\b", diag_clean) or "suhu" in diag_clean:
            return ManualRepairAdvice(
                diagnosis_title="Penyimpangan Nilai Sensor Suhu Pendingin (Engine Coolant Temperature - ECT)",
                system_category="Pendingin",
                group_category="Pendukung",
                manual_book_section="Buku Pedoman Resmi Suzuki Vitara JB420 Bab 1A-108 (ECT Sensor Inspection)",
                cause_summary="Termistor NTC pada sensor ECT mengalami penyimpangan nilai tahanan atau konektornya berkarat, membuat ECU salah mengatur semprotan bensin dingin dan putaran kipas radiator.",
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Sensor ECT Rusak / Nilai Tahanan NTC Menyimpang", "desc": "Sensor membaca suhu mesin tidak akurat sehingga suplai bensin starter pagi kurang atau kipas salah bekerja."},
                    {"badge": "Penyebab #2", "title": "Pin Soket 2-Pin ECT Berkarat / Kabel C37-24 Longgar", "desc": "Rembesan coolant atau korosi pada pin konektor memicu resistansi kontak tinggi."},
                    {"badge": "Penyebab #3", "title": "Thermostat Macet atau Ada Udara Terjebak di Radiator", "desc": "Thermostat macet terbuka/tertutup atau level air coolant kurang sehingga pembacaan suhu kacau."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Ganti Sensor)", "title": "Ganti Sensor Suhu ECT Baru & Bleeding Air Radiator", "desc": "Ganti sensor ECT di rumah thermostat (kunci 19 mm, torsi 15 N·m) dan buang udara palsu di sistem pendingin."},
                    {"tag": "Opsi 2 • Soket & Kabel", "title": "Bersihkan Soket 2-Pin ECT & Perbaiki Jalur Kabel C37-24", "desc": "Semprot contact cleaner pada terminal soket ECT dan rapatkan penjepit pin konektor."},
                    {"tag": "Opsi 3 • Sistem Pendingin", "title": "Ganti Thermostat & Kuras Air Radiator Coolant", "desc": "Ganti thermostat jika macet serta isi ulang coolant sesuai standar kapasitas pabrik."},
                ],
                sensor_standards=[
                    {"parameter": "Tahanan ECT pada 20°C (Mesin Dingin)", "normal_range": "2.21 - 2.69 kOhm (tegangan ~3.0V)", "unit": "kOhm"},
                    {"parameter": "Tahanan ECT pada 80°C (Suhu Kerja)", "normal_range": "290 - 354 Ohm (tegangan ~0.5V)", "unit": "Ohm"},
                ],
                wiring_pinout=[
                    {"pin": "C37-24", "signal": "THW / ECT Signal (PPL/YEL)", "function": "Input tegangan sinyal suhu pendingin ke ECM"},
                    {"pin": "C37-57", "signal": "E2 / Ground Sensor (GRY/GRN)", "function": "Massa sensor ECM"},
                ],
                step_by_step_repair=[
                    "1. Dinginkan mesin semalaman, sambungkan scanner sebelum start pagi, bandingkan data ECT dengan IAT (keduanya harus selisih < 3°C).",
                    "2. Buka kran kuras radiator dan tampung 1-2 liter coolant bersih.",
                    "3. Lepas sensor ECT di rumah thermostat menggunakan kunci ring 19 mm.",
                    "4. Bersihkan ulir, lapisi ulir sensor ECT baru dengan liquid gasket / Teflon tape, kencangkan torsi 15 N·m.",
                    "5. Tuangkan kembali coolant dan lakukan bleeding udara terjebak di radiator.",
                ],
                relearn_reset_steps=[
                    "1. Nyalakan mesin sampai mencapai suhu kerja 85-90°C.",
                    "2. Pastikan kipas radiator otomatis berputar saat ECT mencapai 96-98°C dan mati pada 92°C.",
                ],
            )
        elif "maf" in diag_clean or "P0101" in dtc_codes:
            return ManualRepairAdvice(
                diagnosis_title="Sensor Aliran Udara MAF Kotor / Terkontaminasi Jelaga",
                system_category="Udara",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Servis Bab 1A-62 (Mass Air Flow Sensor Inspection)",
                cause_summary="Kawat pemanas (hot-wire) sensor MAF tertutup debu dan uap oli dari filter udara kotor, menyebabkan pembacaan debit udara meleset (P0101) dan tarikan mesin kehilangan tenaga.",
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Elemen Kawat Sensor MAF Tertutup Debu / Uap Oli", "desc": "Kotoran menempel pada kawat platinum MAF sehingga pembacaan debit udara (g/s) tidak responsif."},
                    {"badge": "Penyebab #2", "title": "Elemen Filter Udara Kotor atau Seal Boks Bocor", "desc": "Saringan udara yang tersumbat debu meloloskan partikel halus langsung ke sensor MAF."},
                    {"badge": "Penyebab #3", "title": "Sensor MAF Rusak Permanen atau Soket 5-Pin Longgar", "desc": "Sirkuit internal sensor MAF mati atau tegangan suplai +12V pada pin E23-31 terputus."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Cleaning)", "title": "Bersihkan Sensor MAF dengan MAF Sensor Cleaner", "desc": "Semprot elemen kawat sensor MAF menggunakan cairan khusus MAF cleaner dan keringkan sempurna."},
                    {"tag": "Opsi 2 • Ganti Komponen", "title": "Ganti Unit Sensor MAF Baru & Elemen Filter Udara", "desc": "Ganti sensor MAF assy bila nilai g/s tetap tidak normal setelah dibersihkan, serta ganti filter udara."},
                    {"tag": "Opsi 3 • Soket & Intake", "title": "Perbaiki Konektor 5-Pin MAF & Rapatkan Belalai Intake", "desc": "Kencangkan pin terminal soket MAF dan pastikan tidak ada kebocoran pada karet belalai udara."},
                ],
                sensor_standards=[
                    {"parameter": "Tegangan MAF (Kunci Kontak ON Mesin Mati)", "normal_range": "0.90 - 1.20 V (0 g/s)", "unit": "V"},
                    {"parameter": "Tegangan MAF (Idle Mesin Hangat 750 RPM)", "normal_range": "1.30 - 1.80 V (2.0 - 3.5 g/s)", "unit": "V"},
                    {"parameter": "Tegangan MAF (Akselerasi Penuh WOT)", "normal_range": "3.50 - 4.50 V (>50 g/s)", "unit": "V"},
                ],
                wiring_pinout=[
                    {"pin": "IG-MAIN (Pin 1)", "signal": "MAF +12V Power (BLU/BLK)", "function": "Suplai daya +10–14V Main Relay ke elemen Hot-Wire MAF"},
                    {"pin": "C37-26 (Pin 2)", "signal": "MAF Signal Output (RED)", "function": "Sinyal debit aliran udara (0.5–1.0V KOEO | 1.3–1.8V idle) ke ECM"},
                    {"pin": "C37-27 (Pin 3)", "signal": "MAF Ground (BLU)", "function": "Massa khusus sensor MAF (< 0.3 V / < 3 Ohm ke bodi)"},
                    {"pin": "C37-25 (Pin 4)", "signal": "IAT Signal (LT GRN)", "function": "Sinyal sensor suhu udara masuk (IAT: 1.32–1.65V @ 40°C)"},
                    {"pin": "C37-57 (Pin 5)", "signal": "IAT Sensor Ground (GRY/GRN)", "function": "Massa referensi sensor IAT ke ECM (< 0.3 V)"},
                ],
                step_by_step_repair=[
                    "1. Matikan kunci kontak, lepas konektor terminal sensor MAF di boks filter udara.",
                    "2. Buka 2 sekrup pengikat sensor MAF menggunakan obeng kembang presisi.",
                    "3. Semprotkan cairan khusus MAF Sensor Cleaner ke kawat tipis dan termistor sensor dari jarak 10 cm (JANGAN SENTUH DENGAN JARI ATAU KUAS!).",
                    "4. Biarkan mengering sempurna selama 10 menit, lalu pasang kembali sensor beserta seal karetnya.",
                ],
                relearn_reset_steps=[
                    "1. Reset DTC P0101 melalui OBD scanner.",
                    "2. Hidupkan mesin dan tes akselerasi mendadak: pastikan nilai MAF g/s melonjak responsif.",
                ],
            )
        elif (
            "throttle" in diag_clean
            or "trotel" in diag_clean
            or re.search(r"\btps\b", diag_clean)
            or bool(dtc_codes & {"P0120", "P0121", "P0122", "P0123", "P0124", "P0220", "P0221", "P0222", "P0223", "P0507", "P2100", "P2101", "P2119", "P2135"})
        ):
            return ManualRepairAdvice(
                diagnosis_title="Endapan Karbon pada Throttle Body / Malfungsi Idle Air Control",
                system_category="Udara",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Suzuki Vitara JB420 Bab 1A-88 & Bab 1A-173 (Electric Throttle Body Service)",
                cause_summary="Tumpukan kerak karbon mengganjal katup kupu-kupu Electronic Throttle Body (ETC), membuat katup tidak menutup rapat sehingga RPM idle mengayun tinggi (P0507) atau brebet saat AC menyala.",
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Kerak Karbon Menumpuk di Dinding & Katup Throttle Body", "desc": "Endapan jelaga uap oli menghalangi katup kupu-kupu menutup presisi pada posisi bukaan idle."},
                    {"badge": "Penyebab #2", "title": "Kalibrasi Sudut Throttle (Idle Air Volume Learning) Berubah", "desc": "ECU kehilangan titik referensi bukaan 0% pasca pembersihan throttle atau pelepasan aki."},
                    {"badge": "Penyebab #3", "title": "Gasket Throttle Body Bocor atau Motor ETC / Sensor TPS Aus", "desc": "Paking throttle body rembes udara luar atau gigi reduksi motor ETC/TPS mengalami keausan."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Carbon Clean)", "title": "Bersihkan Throttle Body & Lakukan Kalibrasi Idle Relearn", "desc": "Bersihkan kerak karbon pada katup throttle dengan cleaner khusus, lalu jalankan prosedur Idle Air Volume Learning."},
                    {"tag": "Opsi 2 • Paking & Seal", "title": "Ganti Gasket Throttle Body Baru & Rapatkan Baut", "desc": "Ganti paking/seal throttle body yang sudah kempes dan kencangkan 4 baut pengikat dengan torsi 10 N·m."},
                    {"tag": "Opsi 3 • Ganti Unit ETC", "title": "Ganti Unit Electronic Throttle Body Assy / Perbaiki Soket 6-Pin", "desc": "Ganti unit Throttle Body Assy bila motor aktuator atau sensor TPS internal rusak."},
                ],
                sensor_standards=[
                    {"parameter": "Tegangan TPS Main (C37-54 saat Idle)", "normal_range": "0.72 - 1.04 V", "unit": "V"},
                    {"parameter": "Tegangan TPS Sub (C37-40 saat Idle)", "normal_range": "1.60 - 1.91 V", "unit": "V"},
                    {"parameter": "Target RPM Idle Normal (AC OFF)", "normal_range": "750 ± 50 RPM", "unit": "RPM"},
                    {"parameter": "Target RPM Idle (AC ON)", "normal_range": "850 ± 50 RPM", "unit": "RPM"},
                ],
                wiring_pinout=[
                    {"pin": "C37-44 (Pin 1)", "signal": "Throttle Actuator Motor + (BLU/RED)", "function": "Penggerak motor aktuator katup gas (0 – 1 V / PWM)"},
                    {"pin": "C37-45 (Pin 2)", "signal": "Throttle Actuator Motor - (BLU/YEL)", "function": "Penggerak motor aktuator katup gas (0 – 1 V / PWM)"},
                    {"pin": "C37-53 (Pin 3)", "signal": "TPS +5V Power Source (WHT)", "function": "Suplai referensi 4.5 – 5.5 V untuk TPS Main & Sub"},
                    {"pin": "C37-54 (Pin 4)", "signal": "TPS Main Signal (BLK)", "function": "Sinyal utama bukaan katup gas (0.72–1.04V idle | 3.67–4.25V WOT)"},
                    {"pin": "C37-40 (Pin 5)", "signal": "TPS Sub Signal (RED)", "function": "Sinyal pembanding TPS Sub (1.60–1.91V idle | 3.88–4.45V WOT)"},
                    {"pin": "C37-41 (Pin 6)", "signal": "TPS Sensor Ground (GRN)", "function": "Massa referensi sensor posisi throttle (< 0.3 V / < 3 Ohm)"},
                ],
                step_by_step_repair=[
                    "1. Lepas selang belalai intake duct dari moncong throttle body.",
                    "2. Semprotkan Electronic Throttle Body Cleaner ke kain lap microfiber halus.",
                    "3. Bersihkan deposit jelaga hitam di sekeliling dinding silinder dan katup throttle (buka katup perlahan dengan dorongan jari yang lembut).",
                    "4. Jika melepas seluruh unit throttle body, ganti gasket orisinil baru dan kencangkan 4 baut pengikat dengan torsi 10 N·m.",
                ],
                relearn_reset_steps=[
                    "1. Lakukan prosedur 'Throttle Valve Closed Position Learning': Kunci kontak ON 10 detik, lalu OFF 10 detik.",
                    "2. Lakukan 'Idle Air Volume Learning': Hidupkan mesin, matikan seluruh beban (AC/lampu), biarkan idle selama 15 menit hingga RPM stabil di 750 RPM.",
                ],
            )
        elif "injektor" in diag_clean or "P0172" in dtc_codes:
            return ManualRepairAdvice(
                diagnosis_title="Injektor Bocor Menetes / Campuran Bahan Bakar Terlalu Kaya (Rich Mixture)",
                system_category="Bahan Bakar",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Servis Bab 1G (Fuel Delivery Pipe & Injector Overhaul)",
                cause_summary="Salah satu nosel injektor tidak menutup sempurna (menetes) atau tekanan BBM berlebih, menyebabkan bensin terlalu pekat (Rich - P0172), busi basah hitam, dan mesin pincang.",
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Injektor Bocor Menetes atau Pengabutan Tidak Rata", "desc": "Jarum nosel injektor terganjal kotoran sehingga bensin menetes terus ke ruang bakar dan membuat busi basah."},
                    {"badge": "Penyebab #2", "title": "Regulator Tekanan Bensin (FPR) / Katup EVAP Purge Bocor", "desc": "Tekanan fuel rail melebihi standar (> 3.8 bar) atau uap bensin kanister EVAP tersedot liar ke intake."},
                    {"badge": "Penyebab #3", "title": "Sirkuit Koil Injektor / Sensor MAP & O2 Membaca Meleset", "desc": "Soket injektor bermasalah atau sensor pembacaan udara/oksigen memberi sinyal palsu ke ECM."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Injektor)", "title": "Ultrasonic Cleaning / Ganti Fuel Injector & Seal O-Ring", "desc": "Bersihkan dan kalibrasi injektor di alat ukur, atau ganti unit injektor yang terbukti bocor menetes."},
                    {"tag": "Opsi 2 • Regulator & EVAP", "title": "Perbaiki Fuel Pressure Regulator / Ganti Katup EVAP Purge", "desc": "Normalkan tekanan fuel rail ke 3.0–3.5 bar dan pastikan katup solenoid EVAP menutup rapat."},
                    {"tag": "Opsi 3 • Busi & BBM", "title": "Bersihkan / Ganti Busi yang Basah Karbon & Kuras Filter BBM", "desc": "Bersihkan keempat busi yang menghitam akibat campuran kaya serta ganti filter bensin."},
                ],
                sensor_standards=[
                    {"parameter": "Tekanan Fuel Rail (Mesin Idle)", "normal_range": "300 - 350 kPa (3.0 - 3.5 bar)", "unit": "kPa"},
                    {"parameter": "Tahanan Koil Injektor (20°C)", "normal_range": "11.5 - 14.5 Ohm", "unit": "Ohm"},
                    {"parameter": "Uji Kebocoran Injektor (Tekanan 3.5 bar)", "normal_range": "Maksimal 1 tetes per 2 menit", "unit": "tetes"},
                ],
                wiring_pinout=[
                    {"pin": "C37-29 s/d 32", "signal": "INJ1 - INJ4 (Ground Pulse)", "function": "Sinyal penyemprotan bahan bakar dari ECM"},
                    {"pin": "Relay EFI", "signal": "+12V Constant Power", "function": "Daya positif injektor saat kunci kontak ON"},
                ],
                step_by_step_repair=[
                    "1. Lepas sambungan pipa fuel delivery dan cabut keempat injektor.",
                    "2. Uji injektor di mesin kalibrasi injector tester untuk melihat pola semprotan (spray pattern) dan uji kebocoran (leak test).",
                    "3. Ganti injektor yang menetes atau lakukan ultrasonic cleaning jika hanya tersumbat ringan.",
                    "4. Wajib pasang O-ring atas dan seal bawah baru dengan melumasi sedikit oli mesin bersih sebelum dipasang kembali.",
                ],
                relearn_reset_steps=[
                    "1. Hapus DTC P0172 dan reset adaptive fuel trim.",
                    "2. Cek apakah LTFT kembali ke rentang -5% s/d +5% pada putaran stasioner.",
                ],
            )
        elif (
            "busi" in diag_clean
            or "koil" in diag_clean
            or "coil" in diag_clean
            or "misfire" in diag_clean
            or "pengapian" in diag_clean
            or bool(dtc_codes & {"P0300", "P0301", "P0302", "P0303", "P0304", "P0351", "P0352", "P0353", "P0354"})
        ):
            cyl_map = {"P0301": "Silinder 1", "P0302": "Silinder 2", "P0303": "Silinder 3", "P0304": "Silinder 4", "P0351": "Silinder 1", "P0352": "Silinder 2", "P0353": "Silinder 3", "P0354": "Silinder 4"}
            matched_cyls = [cyl_map[c] for c in sorted(dtc_codes) if c in cyl_map]
            cyl_label = f" pada {', '.join(matched_cyls)}" if matched_cyls else " pada Silinder Mesin (Random / Multi-Cylinder)"
            return ManualRepairAdvice(
                diagnosis_title=f"Gagal Pengapian / Engine Misfire{cyl_label} (Sistem Ignition Coil, Busi, & Injeksi)",
                system_category="Pengapian",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Resmi Suzuki Grand Vitara JB420 Vol 1.pdf Bab 1A-111 (Hal. 169-170) & Bab 1H (Ignition System)",
                cause_summary=(
                    f"Terjadi kegagalan pembakaran (misfire){cyl_label} yang menyebabkan mesin pincang/brebet dan getaran kasar. "
                    "Penyebab utama di lapangan adalah lemahnya Ignition Coil atau busi aus, disusul oleh gangguan injektor, kualitas bahan bakar, atau kebocoran vakum/kompresi."
                ),
                cause_items=[
                    {
                        "badge": "Penyebab Utama #1",
                        "title": "Koil Pengapian (Ignition Coil) Bocor / Lemah & Busi Aus",
                        "desc": "Isolator karet selongsong koil retak (api bocor ke dinding silinder), kumparan koil drop saat panas, atau celah elektroda busi sudah melebar (> 1.1 mm).",
                    },
                    {
                        "badge": "Penyebab #2",
                        "title": "Injektor Kotor / Tersumbat & Tekanan Pompa Bensin Turun",
                        "desc": "Suplai pengabutan bensin ke silinder tidak mencukupi akibat nosel injektor mampet, soket injektor kendor, atau tekanan fuel pump lemah (< 3.0 bar).",
                    },
                    {
                        "badge": "Penyebab #3",
                        "title": "Kualitas Bahan Bakar Jelek / Tercampur Air atau Oktan Rendah",
                        "desc": "Bahan bakar di dalam tangki terkontaminasi air/endapan kotoran atau basi sehingga gagal terbakar sempurna di ruang bakar.",
                    },
                    {
                        "badge": "Penyebab #4",
                        "title": "Kebocoran Vakum Intake, Katup EGR Macet, atau Kompresi Bocor",
                        "desc": "Udara liar masuk melalui selang vakum/gasket intake, katup EGR gagal menutup rapat, atau kompresi mekanikal klep/ring piston lemah.",
                    },
                ],
                repair_options=[
                    {
                        "tag": "Opsi 1 • Utama (Pengapian)",
                        "title": "Ganti Ignition Coil (Koil Pengapian) & Busi Baru",
                        "desc": "Ganti unit koil pengapian yang bocor/mati beserta busi yang sudah aus (setel celah 0.8–1.1 mm, kencangkan torsi 18–22 N·m).",
                    },
                    {
                        "tag": "Opsi 2 • Sistem Injeksi",
                        "title": "Bersihkan / Servis Injektor & Periksa Tekanan Fuel Pump",
                        "desc": "Lakukan ultrasonic cleaning injektor yang mampet, rapatkan soket konektor injektor, dan pastikan tekanan fuel rail 3.0–3.5 bar.",
                    },
                    {
                        "tag": "Opsi 3 • Bahan Bakar",
                        "title": "Kuras Sirkuit Bahan Bakar & Ganti Bahan Bakar Jelek / Filter BBM",
                        "desc": "Kuras tangki bensin bila kualitas BBM buruk/tercampur air, ganti filter bensin, dan isi bahan bakar beroktan sesuai spesifikasi.",
                    },
                    {
                        "tag": "Opsi 4 • Vakum & Mekanis",
                        "title": "Perbaiki Kebocoran Vakum / EGR, Bersihkan Filter Udara & Cek Kompresi",
                        "desc": "Perbaiki selang vakum retak, bersihkan katup EGR & saringan udara, atau periksa kompresi silinder serta kabel soket ECM.",
                    },
                ],
                sensor_standards=[
                    {"parameter": "Celah Busi Standar (Spark Plug Gap)", "normal_range": "0.80 - 1.10 mm", "unit": "mm"},
                    {"parameter": "Tahanan Resistor Internal Busi", "normal_range": "4.0 - 6.5 kOhm", "unit": "kOhm"},
                    {"parameter": "Tegangan Suplai Konektor Koil (IG ON)", "normal_range": "11.5 - 14.2 V", "unit": "V"},
                    {"parameter": "Misfire Counter per Silinder (Idle/RPM Tinggi)", "normal_range": "0 count", "unit": "hit"},
                ],
                wiring_pinout=(
                    [
                        {"pin": "IG-COIL (Pin 1)", "signal": "BLK/WHT — Suplai +12V IG1 Koil (Fuse IG COIL)", "function": "Suplai daya +10–14 V IG ON dari Ignition Switch → Fuse IG COIL di J/B (Bab 1H-2 Hal. 430; BUKAN dari ECM)"},
                        (
                            {"pin": "C37-21 (Pin 2)", "signal": "BRN — Trigger ECM Koil Silinder #1", "function": "Sinyal pemicu pulsa 5V dari ECM ke igniter Koil #1 (0–0.6V IG ON, Pulsa Idle; Koil #2: C37-20, #3: C37-19, #4: C37-18)"}
                            if bool(dtc_codes & {"P0301", "P0351"}) else
                            {"pin": "C37-20 (Pin 2)", "signal": "BRN/BLK — Trigger ECM Koil Silinder #2", "function": "Sinyal pemicu pulsa 5V dari ECM ke igniter Koil #2 (0–0.6V IG ON, Pulsa Idle; Koil #1: C37-21, #3: C37-19, #4: C37-18)"}
                            if bool(dtc_codes & {"P0302", "P0352"}) else
                            {"pin": "C37-19 (Pin 2)", "signal": "BRN/WHT — Trigger ECM Koil Silinder #3", "function": "Sinyal pemicu pulsa 5V dari ECM ke igniter Koil #3 (0–0.6V IG ON, Pulsa Idle; Koil #1: C37-21, #2: C37-20, #4: C37-18)"}
                            if bool(dtc_codes & {"P0303", "P0353"}) else
                            {"pin": "C37-18 (Pin 2)", "signal": "BRN/YEL — Trigger ECM Koil Silinder #4", "function": "Sinyal pemicu pulsa 5V dari ECM ke igniter Koil #4 (0–0.6V IG ON, Pulsa Idle; Koil #1: C37-21, #2: C37-20, #3: C37-19)"}
                            if bool(dtc_codes & {"P0304", "P0354"}) else
                            {"pin": "C37-21..18 (Pin 2)", "signal": "BRN / BRN-BLK / BRN-WHT / BRN-YEL — Trigger ECM Koil #1–#4", "function": "Tiap soket 3-pin koil menerima 1 kabel trigger dari ECM: #1 C37-21 (BRN), #2 C37-20 (BRN/BLK), #3 C37-19 (BRN/WHT), #4 C37-18 (BRN/YEL)"}
                        ),
                        {"pin": "GND-ENG (Pin 3)", "signal": "BLK/ORN — Ground Massa Koil (Blok Mesin)", "function": "Massa langsung ke blok/kepala silinder mesin (< 0.3 V / < 1 Ohm; BUKAN ke ECM — Bab 1H-2)"},
                    ]
                ),
                step_by_step_repair=[
                    "1. Lepas konektor dan baut 10 mm pengikat Ignition Coil, periksa karet selongsong (boot) koil dari retakan atau jejak loncatan bunga api putih.",
                    "2. Buka keempat busi menggunakan kunci busi magnet 16 mm (atau 14 mm sesuai tipe mesin), periksa warna keramik dan ukur celah elektroda menggunakan feeler gauge (standar 0.8 - 1.1 mm).",
                    "3. Ganti koil pengapian yang lemah/bocor serta ganti busi yang elektrodanya aus, kencangkan busi baru dengan torsi 18 - 22 N·m.",
                    "4. Bila pengapian normal namun masih misfire, periksa bunyi kerja tiap injektor, ukur tekanan fuel rail (3.0 - 3.5 bar), dan pastikan bahan bakar tidak tercampur air.",
                ],
                relearn_reset_steps=[
                    "1. Hapus histori DTC Misfire (P0300 - P0304) dan reset mempelajari ulang fuel trim.",
                    "2. Hidupkan mesin, pantau Misfire Counter di scanner pada saat idle dan saat digas 2.500 - 3.000 RPM (pastikan bernilai 0).",
                ],
            )
        elif "filter udara" in diag_clean or "saringan udara" in diag_clean:
            return ManualRepairAdvice(
                diagnosis_title="Penyumbatan Elemen Filter Udara (Air Cleaner Element Restricted)",
                system_category="Udara",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Perawatan Berkala Bab 0B & Bab 1D (Air Intake System)",
                cause_summary="Elemen saringan udara dipenuhi debu tebal sehingga menghambat suplai oksigen ke ruang bakar, menyebabkan tarikan berat, brebet pada putaran tinggi, dan konsumsi BBM boros.",
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": "Elemen Kertas Filter Udara Tersumbat Debu Tebal", "desc": "Pori-pori saringan udara tertutup kotoran sehingga aliran udara masuk ke mesin terhambat."},
                    {"badge": "Penyebab #2", "title": "Boks Rumah Filter Udara & Saluran Ducting Kotor", "desc": "Endapan pasir dan debu menumpuk di dasar boks filter udara."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Ganti Baru)", "title": "Ganti Elemen Filter Udara Baru", "desc": "Pasang elemen saringan udara baru yang bersih dan pastikan seal karet pinggir duduk rapat."},
                    {"tag": "Opsi 2 • Servis Bersih", "title": "Semprot Bersih Filter Udara & Bersihkan Boks Filter", "desc": "Semprot dengan udara bertekanan dari sisi bersih ke sisi kotor dan lap bagian dalam boks filter."},
                ],
                sensor_standards=[
                    {"parameter": "Tekanan Manifold MAP (Idle)", "normal_range": "30 - 38 kPa", "unit": "kPa"},
                    {"parameter": "Debit Aliran Udara MAF (2.500 RPM)", "normal_range": "7.5 - 12.0 g/s", "unit": "g/s"},
                ],
                wiring_pinout=[
                    {"pin": "C37-25", "signal": "IAT / Intake Air Temp (GRN/ORN)", "function": "Sinyal sensor suhu udara masuk di rumah filter udara"},
                ],
                step_by_step_repair=[
                    "1. Lepas pengait tutup boks filter udara dan keluarkan elemen filter udara.",
                    "2. Bersihkan bagian dalam boks bawah filter udara dari pasir/debu menggunakan kain lembap.",
                    "3. Pasang elemen filter udara baru (pastikan karet seal pinggir duduk rata agar udara kotor tidak bocor ke throttle body).",
                ],
                relearn_reset_steps=[
                    "1. Reset nilai adaptasi ECM dan lakukan uji jalan akselerasi.",
                ],
            )
        elif "ckp" in diag_clean or "cmp" in diag_clean or bool(dtc_codes & {"P0335", "P0336", "P0337", "P0338", "P0339", "P0340", "P0341", "P0342", "P0343", "P0344"}):
            is_cmp = bool(dtc_codes & {"P0340", "P0341", "P0342", "P0343", "P0344"}) or ("cmp" in diag_clean and "ckp" not in diag_clean)
            return ManualRepairAdvice(
                diagnosis_title=(
                    "Malfungsi Sirkuit Sensor Posisi Poros Nok / Camshaft (CMP Sensor — 3-Pin C08)"
                    if is_cmp
                    else "Malfungsi Sirkuit Sensor Posisi Poros Engkol / Crankshaft (CKP Sensor — 3-Pin C20)"
                ),
                system_category="Pengapian",
                group_category="Pembakaran",
                manual_book_section="Suzuki Grand Vitara JB420 Manual Vol 1 Bab 1A-115 / 1A-117 & Vol 2 Bab 9A-92 (CKP C20 3-Pin & CMP C08 3-Pin)",
                cause_summary=(
                    "IC Hall sensor CMP (3-pin C08) melemah saat mesin panas atau suplai +12V Main Relay (BLU/BLK) / sinyal C37-52 (WHT/RED) terputus, memicu DTC P0340 dan sulit starter."
                    if is_cmp
                    else "Kumparan induktif sensor CKP (3-pin C20: Shield BLK, PNK & BLU) melemah saat panas atau ujung magnet tertutup serbuk besi, menyebabkan sinyal C37-36 (PNK) & C37-51 (BLU) hilang (P0335) dan mesin mati mendadak."
                ),
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": f"Sensor {'CMP (3-Pin C08 Hall-IC)' if is_cmp else 'CKP (3-Pin C20 Induktif)'} Melemah Saat Mesin Panas", "desc": "Kumparan atau IC Hall di dalam sensor putus kontak ketika suhu kerja mesin tinggi sehingga mesin mati mendadak."},
                    {"badge": "Penyebab #2", "title": "Ujung Magnet Sensor Tertutup Gram Besi / Oli", "desc": "Kotoran serbuk logam menempel pada kepala sensor sehingga mengganggu pembacaan gigi reluctor."},
                    {"badge": "Penyebab #3", "title": "Soket 3-Pin Kendor / Kabel Putus atau Timing Chain Melar", "desc": "Konektor sensor kemasukan rembesan oli atau posisi rantai timing (timing chain) bergeser."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Ganti Sensor)", "title": f"Ganti Sensor {'CMP' if is_cmp else 'CKP'} Baru (Orisinil)", "desc": "Ganti unit sensor yang lemah beserta O-ring baru (kencangkan baut 10 mm torsi 10 N·m)."},
                    {"tag": "Opsi 2 • Pembersihan & Soket", "title": "Bersihkan Ujung Sensor dari Gram Besi & Perbaiki Soket 3-Pin", "desc": f"Bersihkan kepala magnet sensor, semprot soket 3-pin dengan contact cleaner, dan cek jalur {'C37-52 (WHT/RED), +12V BLU/BLK & GND BLK/YEL' if is_cmp else 'Pin 1 Shield (BLK), Pin 2 C37-36 (PNK) & Pin 3 C37-51 (BLU)'}."},
                    {"tag": "Opsi 3 • Mekanis Timing", "title": "Periksa Ketepatan Timing Chain & Roda Gigi Reluctor", "desc": "Periksa tanda top timing mesin jika kode CKP/CMP tetap muncul setelah ganti sensor."},
                ],
                sensor_standards=(
                    [
                        {"parameter": "Suplai +12V Sensor CMP (Main Relay BLU/BLK)", "normal_range": "10.0 - 14.0 V (IG ON)", "unit": "V"},
                        {"parameter": "Sinyal Output CMP C37-52 (WHT/RED)", "normal_range": "Pulsa kotak 0 - 5.0 V saat Crank/Idle", "unit": "V"},
                        {"parameter": "Ground Sensor CMP (BLK/YEL ke Massa)", "normal_range": "< 0.3 V (< 1.0 Ohm)", "unit": "V"},
                    ]
                    if is_cmp
                    else [
                        {"parameter": "Tahanan Kumparan CKP C20 (Pin 2–3 pada 20°C)", "normal_range": "1.68 - 2.52 kOhm (Induktif 3-Pin)", "unit": "kOhm"},
                        {"parameter": "Sinyal AC Output CKP C37-51/36 (Saat Crank)", "normal_range": "Pulsa AC > 0.5 V AC (Simetris)", "unit": "VAC"},
                        {"parameter": "Kontinuitas Pin 1 Shield (BLK) ke Massa Blok", "normal_range": "< 1.0 Ohm (Tidak short ke Pin 2/3)", "unit": "Ohm"},
                    ]
                ),
                wiring_pinout=(
                    [
                        {"pin": "GND BLOK (Pin 1)", "signal": "BLK/YEL — GND", "function": "Massa Sensor Hall-Effect CMP ke Blok Mesin (< 1 Ω)"},
                        {"pin": "C37-52 (Pin 2)", "signal": "WHT/RED — CMP SIG", "function": "Pulsa Digital Posisi Noken As (0–0.6 V ↔ 4–5 V saat Cranking/Idle)"},
                        {"pin": "MAIN RLY (Pin 3)", "signal": "BLU/BLK — +B 12V", "function": "Suplai +12V Main Relay untuk Sensor Hall-IC CMP (10–14 V IG ON)"},
                    ]
                    if is_cmp
                    else [
                        {"pin": "GND BLOK (Pin 1)", "signal": "BLK — SHIELD", "function": "Pelindung Shield Anti-Noise Elektromagnetik ke Massa Blok #3 (< 1 Ω)"},
                        {"pin": "C37-36 (Pin 2)", "signal": "PNK — CKP (-)", "function": "Sinyal Induktif Poros Engkol CKP (−) ke ECM (Tahanan Pin 2↔3: 1.68–2.52 kΩ)"},
                        {"pin": "C37-51 (Pin 3)", "signal": "BLU — CKP (+)", "function": "Sinyal Induktif Poros Engkol CKP (+) ke ECM (> 0.5 V AC saat Cranking)"},
                    ]
                ),
                step_by_step_repair=[
                    f"1. Periksa soket {'3-pin CMP C08 (GND BLK/YEL, Sinyal WHT/RED, +12V BLU/BLK)' if is_cmp else '3-pin CKP C20 (Pin 1 Shield BLK, Pin 2 PNK, Pin 3 BLU)'} dari rembesan oli mesin atau kabel getas.",
                    "2. Lepas baut pengikat sensor (10 mm), bersihkan ujung magnet sensor dari kotoran gram besi.",
                    "3. Ganti sensor dengan part orisinil beserta O-ring baru, kencangkan baut dengan torsi 10 N·m.",
                ],
                relearn_reset_steps=[
                    "1. Hapus kode DTC P0335/P0340 via scanner.",
                    "2. Hidupkan mesin hingga suhu kerja >85°C dan pastikan tidak ada gejala mati mendadak.",
                ],
            )
        elif (
            "kipas" in diag_clean
            or "cooling fan" in diag_clean
            or "radiator fan" in diag_clean
            or bool(dtc_codes & {"P0480", "P0481", "P0482", "P0483", "P0484", "P0485"})
        ):
            is_fan2 = "P0481" in dtc_codes or "kipas radiator 2" in diag_clean
            fan_label = "No. 2 (High Speed / Sub Fan)" if is_fan2 else "No. 1 (Low Speed / Main Fan)"
            fan_pin = "E23-47" if is_fan2 else "E23-46"
            fan_wire = "RED" if is_fan2 else "RED/BLK"
            dtc_tag = ", ".join(sorted(dtc_codes)) if dtc_codes else "P0480"
            return ManualRepairAdvice(
                diagnosis_title=f"Malfungsi Sirkuit Kontrol Kipas Radiator {fan_label} ({dtc_tag})",
                system_category="Pendingin",
                group_category="Pendukung",
                manual_book_section="Buku Pedoman Resmi Suzuki Grand Vitara JB420 Vol 1.pdf Bab 1A-15 (Item 46-48) & Bab 1A-133",
                cause_summary=(
                    f"ECM mendeteksi rangkaian terbuka (putus) atau hubung singkat pada jalur kendali Relay Kipas Radiator {fan_label} "
                    f"(terminal ECM {fan_pin} kabel {fan_wire}), sehingga kipas pendingin tidak dapat diaktifkan secara normal."
                ),
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": f"Relay Kipas Radiator {fan_label} Putus / Macet", "desc": "Kumparan koil relay putus (normal 60–120 Ohm) atau kontak platina di dalam relay aus terbakar."},
                    {"badge": "Penyebab #2", "title": "Motor Kipas Radiator Lemah / Habis Sikat Karbon (Brush)", "desc": "Motor extra fan macet atau carbon brush habis sehingga tidak berputar saat diberi suplai +12V."},
                    {"badge": "Penyebab #3", "title": f"Sekering Kipas Putus / Kabel Kontrol {fan_pin} ({fan_wire}) Putus", "desc": "Sekering utama 30A/40A putus, soket kipas meleleh, atau jalur kabel dari boks relay ke ECM terputus."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Relay)", "title": f"Ganti Relay Kipas Radiator {fan_label} Baru", "desc": "Ganti relay cooling fan di Fuse & Relay Box ruang mesin dengan relay baru sesuai spesifikasi OEM."},
                    {"tag": "Opsi 2 • Motor Kipas", "title": "Ganti Motor Kipas Radiator (Extra Fan) / Servis Brush", "desc": "Ganti unit motor kipas radiator bila putaran lemah, macet, atau berbunyi kasar."},
                    {"tag": "Opsi 3 • Sekering & Kabel", "title": f"Ganti Sekering Kipas & Perbaiki Soket / Kabel {fan_pin}", "desc": f"Ganti sekering yang putus, perbaiki soket kipas yang kendor, dan sambung jalur kabel {fan_wire} ke ECM."},
                ],
                sensor_standards=[
                    {"parameter": f"Tegangan Terminal {fan_pin} (Kipas OFF / Standby IG ON)", "normal_range": "10.0 - 14.0 V", "unit": "V"},
                    {"parameter": f"Tegangan Terminal {fan_pin} (Kipas ON Aktif)", "normal_range": "0.0 - 1.5 V (Ground Switched ECM)", "unit": "V"},
                    {"parameter": "Tahanan Koil Relay Kipas Radiator (pada 20°C)", "normal_range": "60 - 120 Ohm", "unit": "Ohm"},
                    {"parameter": "Suhu ECT Aktivasi Kipas Low-Speed (Bab 1A-233)", "normal_range": "ON ≥ 97.5°C / OFF ≤ 93.0°C", "unit": "°C"},
                ],
                wiring_pinout=[
                    {"pin": "IG1-FUSE (Koil +)", "signal": "BLK/WHT — Suplai +12V IG1 ke 3 Koil Relay Kipas", "function": "Suplai +10–14 V IG ON ke kumparan Relay Kipas No.1, No.2 & No.3 (Bab 1A-15 Item 46–48)"},
                    {"pin": "E23-46 (Relay #1)", "signal": "RED/BLK — Kontrol Massa Relay Kipas No.1 (Low)", "function": "Output kendali ground ECM ke koil Relay Kipas No.1 (10–14 V OFF, <1 V ON)"},
                    {"pin": "E23-47 (Relay #2)", "signal": "RED — Kontrol Massa Relay Kipas No.2 (High)", "function": "Output kendali ground ECM ke koil Relay Kipas No.2 (High Speed / A/C)"},
                    {"pin": "E23-48 (Relay #3)", "signal": "RED/YEL — Kontrol Massa Relay Kipas No.3 (Sub)", "function": "Output kendali ground ECM ke koil Relay Kipas No.3 (Sub Fan / A/C)"},
                ],
                step_by_step_repair=[
                    "1. Buka tutup Fuse & Relay Box di ruang mesin, periksa sekering utama Cooling Fan (30A/40A) dan sekering IG koil relay dari putus atau kaki gosong.",
                    "2. Cabut Relay Kipas Radiator No. 1, ukur tahanan kumparan koil relay (terminal 85-86: normal 60 - 120 Ohm), lalu uji beri tegangan 12V untuk memastikan kontak 30-87 terhubung (< 0.5 Ohm).",
                    f"3. Kunci kontak ON (mesin mati, AC OFF): ukur tegangan pada jalur kabel {fan_wire} (terminal ECM {fan_pin}) terhadap massa bodi — harus terbaca 10 - 14 V. Jika 0 V, jalur koil relay atau kabel {fan_wire} putus.",
                    "4. Uji langsung motor kipas radiator dengan memberi suplai 12V & massa sesaat pada konektor 2-pin motor kipas: pastikan kipas berputar kencang tanpa bunyi kasar (sikat karbon motor tidak habis).",
                ],
                relearn_reset_steps=[
                    f"1. Sambungkan scan tool ke DLC (kunci kontak OFF -> ON), hapus memori DTC {dtc_tag}.",
                    "2. Gunakan fitur 'Active Test -> Cooling Fan Relay 1 ON' pada scanner, atau hidupkan mesin hingga suhu ECT mencapai ≥ 97.5°C (atau nyalakan AC) dan pastikan kipas radiator berputar otomatis tanpa memunculkan DTC kembali.",
                ],
            )
        else:
            return ManualRepairAdvice(
                diagnosis_title=f"Panduan Diagnosa & Perbaikan: {diagnosis}",
                system_category="Umum",
                group_category="Pembakaran",
                manual_book_section="Buku Pedoman Perbaikan Workshop Manual - Prosedur Servis Standar",
                cause_summary=f"Penyebab teridentifikasi pada komponen/sistem: {diagnosis}. Periksa komponen utama, soket kelistrikan, dan jalur pendukung terkait.",
                cause_items=[
                    {"badge": "Penyebab Utama #1", "title": f"Kerusakan / Keausan Komponen Utama ({diagnosis})", "desc": "Komponen sensor atau aktuator terkait telah melampaui batas usia pakai atau mengalami malfungsi internal."},
                    {"badge": "Penyebab #2", "title": "Soket Konektor Kendor / Korosi atau Kabel Putus", "desc": "Tahanan kontak tinggi pada pin konektor atau kabel bodi (wire harness) terkelupas/hubung singkat."},
                    {"badge": "Penyebab #3", "title": "Suplai Tegangan / Titik Massa Ground Tidak Stabil", "desc": "Tegangan suplai dari sekering/relay drop atau baut titik massa bodi/mesin berkarat."},
                ],
                repair_options=[
                    {"tag": "Opsi 1 • Utama (Komponen)", "title": f"Ganti / Servis Komponen Utama ({diagnosis})", "desc": "Lakukan penggantian atau kalibrasi ulang komponen utama yang teridentifikasi bermasalah."},
                    {"tag": "Opsi 2 • Soket & Kabel", "title": "Bersihkan Soket Konektor & Perbaiki Jalur Kabel Harness", "desc": "Semprot pin konektor dengan contact cleaner, kencangkan pin longgar, dan perbaiki kabel yang putus."},
                    {"tag": "Opsi 3 • Suplai & Reset", "title": "Periksa Sekering, Massa Ground & Reset Adaptasi ECU", "desc": "Pastikan suplai daya 12V/5V dan massa normal, lalu hapus memori DTC dengan scanner."},
                ],
                sensor_standards=[
                    {"parameter": "Tegangan Pengisian Aki", "normal_range": "13.8 - 14.4 V", "unit": "V"},
                    {"parameter": "Tekanan Vakum Idle", "normal_range": "60 - 75 kPa vakum", "unit": "kPa"},
                ],
                wiring_pinout=[
                    {"pin": "Terminal ECM", "signal": "Sinyal Kontrol", "function": "Sinyal kendali aktuator dan sensor"},
                ],
                step_by_step_repair=[
                    "1. Lakukan inspeksi visual menyeluruh pada sambungan mekanis, selang karet, dan kabel konektor.",
                    "2. Bersihkan komponen dari debu/karbon menggunakan cairan pembersih yang sesuai.",
                    "3. Lakukan pengujian komponen menggunakan multitester atau scanner live data.",
                    "4. Ganti part yang telah melampaui batas keausan servis.",
                ],
                relearn_reset_steps=[
                    "1. Reset DTC dan lakukan kalibrasi idle relearn sesuai buku panduan servis.",
                ],
            )

    @classmethod
    def _classify_dtc_workshop_system(cls, code: str, sys_label: str, desc: str) -> tuple[str, str]:
        """Memetakan kode DTC dari Manual Repair Book ke 8 sistem bengkel baku."""
        c = (code or "").upper()
        txt = f"{sys_label} {desc}".lower()

        if c in {"P0480", "P0481", "P0482", "P0483", "P0484", "P0485", "P0115", "P0116", "P0117", "P0118", "P0119", "P0125", "P0128", "B1561"} or any(
            k in txt for k in ("kipas radiator", "cooling fan", "coolant", "thermostat")
        ):
            return "Pendingin", "Pendukung"
        if re.match(r"^P03[0-5][0-9]$", c) or any(k in txt for k in ("misfire", "pengapian", "knock", "crankshaft", "camshaft", "ckp", "cmp", "ignition coil")):
            return "Pengapian", "Pembakaran"
        if c in {"P0087", "P0171", "P0172", "P0174", "P0175", "P0230", "P0462", "P0463", "P2195", "P2196"} or re.match(r"^P0(03[0-8]|13[0-9]|14[01]|20[0-8])$", c) or any(
            k in txt for k in ("bahan bakar", "fuel", "ho2s", "o2 sensor", "injektor", "injector")
        ):
            return "Bahan Bakar", "Pembakaran"
        if re.match(r"^P(010[0-9]|011[0-4]|012[0-4]|022[0-4]|050[5-7]|0660|210[0-9]|211[0-9]|212[0-9]|213[0-9]|222[7-9])$", c) or any(
            k in txt for k in ("mass air flow", "manifold absolute", "intake air", "throttle", "pedal position", "barometric")
        ):
            return "Udara", "Pembakaran"
        if re.match(r"^P04([0-5][0-9])$", c) or any(k in txt for k in ("catalyst", "evaporative", "purge", "daur ulang gas buang", "egr")):
            return "Emisi", "Pendukung"
        if re.match(r"^P(07|08|09|17|18|27)[0-9]{2}$", c) or "transmission" in txt or "tcm" in txt or "torque converter" in txt or "shift solenoid" in txt:
            return "Mekanis", "Pembakaran"
        if "oil" in txt or "pelumas" in txt or "oli" in txt:
            return "Pelumasan", "Pendukung"
        return "Kelistrikan", "Pendukung"

    @classmethod
    def _select_pinouts_for_manual_dtc(
        cls,
        codes: list[str],
        combined_desc: str,
        wiring_rows: Sequence[WiringDiagram],
    ) -> list[dict[str, str]]:
        """Mengambil pinout konektor ECU/TCM/BCM nyata dari tabel `wiring_diagrams` sesuai kode DTC."""
        code_set = {c.upper() for c in codes}
        txt = combined_desc.lower()

        # Kumpulkan semua pin dari tabel wiring_diagrams (prioritaskan katalog JB420 lengkap C37/E23/E92/E93/G30-G32)
        pin_map: dict[str, tuple[str, str]] = {}
        for wd in wiring_rows:
            raw_pj = wd.pinout_json or {}
            if isinstance(raw_pj, dict):
                for pin_code, detail in raw_pj.items():
                    if isinstance(detail, dict):
                        pin_map[pin_code] = (
                            str(detail.get("wire_color", "-")),
                            str(detail.get("function", "-")),
                        )

        wanted_pins: list[str] = []
        if code_set & {"P0480", "P0481", "P0482"} or "kipas" in txt or "cooling fan" in txt:
            wanted_pins = ["E23-46", "E23-47", "C37-24", "C37-57"]
        elif code_set & {"P0115", "P0116", "P0117", "P0118", "P0125", "P0128", "B1561"} or "coolant" in txt:
            wanted_pins = ["C37-24", "C37-57", "E23-46"]
        elif code_set & {"P0100", "P0101", "P0102", "P0103", "P0111", "P0112", "P0113"} or "mass air flow" in txt or "intake air temp" in txt:
            wanted_pins = ["E23-01", "C37-26", "C37-27", "C37-25", "C37-57"]
        elif code_set & {"P0106", "P0107", "P0108", "P2227", "P2228", "P2229"} or "manifold absolute" in txt or "barometric" in txt:
            wanted_pins = ["C37-14", "C37-55", "C37-57"]
        elif code_set & {"P0122", "P0123", "P0222", "P0223", "P2101", "P2102", "P2103", "P2111", "P2119", "P2135", "P0507"} or "throttle" in txt:
            wanted_pins = ["C37-53", "C37-54", "C37-40", "C37-41", "C37-44", "C37-45"]
        elif code_set & {"P2122", "P2123", "P2127", "P2128", "P2138"} or "pedal position" in txt:
            wanted_pins = ["E23-56", "E23-55", "E23-53", "E23-52", "C37-57"]
        elif code_set & {"P0030", "P0031", "P0032", "P0037", "P0038", "P0131", "P0132", "P0133", "P0134", "P0137", "P0138", "P0140", "P2195", "P2196"} or "ho2s" in txt or "o2 sensor" in txt:
            wanted_pins = ["C37-38", "C37-37", "C37-32", "C37-11", "C37-47", "C37-57"]
        elif code_set & {"P0335", "P0340", "B1556"} or "crankshaft" in txt or "camshaft" in txt:
            wanted_pins = ["C37-51", "C37-36", "C37-52", "C37-57"]
        elif code_set & {"P0327", "P0328"} or "knock" in txt:
            wanted_pins = ["C37-56", "C37-57"]
        elif code_set & {"P0087", "P0230", "P0462", "P0463"} or "fuel" in txt:
            wanted_pins = ["E23-15", "E23-01", "E23-60", "C37-15"]
        elif any(c.startswith(("P07", "P09", "P17", "P18", "P27")) for c in code_set) or "transmission" in txt or "tcm" in txt or "solenoid" in txt or "tcc" in txt:
            if "range" in txt or code_set & {"P0705", "P0707", "P1723"}:
                wanted_pins = ["E93-20", "E93-01", "E93-08", "E93-07", "E92-01"]
            elif "temperature" in txt or "fulid" in txt or "fluid" in txt or code_set & {"P0712", "P0713"}:
                wanted_pins = ["E92-11", "E92-12", "E92-06", "E92-01"]
            elif "speed" in txt or code_set & {"P0717", "P0722"}:
                wanted_pins = ["E93-06", "E93-16", "E93-04", "E93-14"]
            elif "tcc" in txt or "pressure" in txt or code_set & {"P0741", "P0742", "P0962", "P0963", "P1878", "P2763", "P2764"}:
                wanted_pins = ["E92-04", "E92-02", "E92-05", "E92-03"]
            else:
                wanted_pins = ["E92-16", "E92-15", "E92-06", "E92-01"]
        elif any(c.startswith("U") for c in code_set) or code_set & {"P1674", "P1676", "P1678", "P1685", "P1703", "P1774", "P1777", "P1778", "B1150", "B1551", "B1552", "B1553"} or "komunikasi" in txt or "can" in txt:
            wanted_pins = ["E23-04", "E23-19", "E23-05", "E23-01"]
        elif code_set & {"B1141", "B1142", "B1143", "B1562"} or "outside air" in txt or "ambient" in txt:
            wanted_pins = ["G31-24", "G31-21", "E23-01"]
        elif any(c.startswith("B10") for c in code_set) or "air bag" in txt or "sdm" in txt or "pretensioner" in txt:
            wanted_pins = ["G30-19", "E23-29", "C37-15"]
        else:
            wanted_pins = ["E23-01", "E23-29", "E23-60", "C37-57", "C37-15"]

        out: list[dict[str, str]] = []
        for idx, p_code in enumerate(wanted_pins, start=1):
            if p_code in pin_map:
                w_color, w_func = pin_map[p_code]
                out.append({
                    "pin": f"{p_code} (Pin {idx})",
                    "signal": f"{w_color} — {w_func[:42]}",
                    "function": w_func,
                })
        return out

    @classmethod
    def _clean_manual_phrase(cls, text: str) -> str:
        """Membersihkan frasa mentah hasil ekstraksi PDF Buku Manual menjadi bahasa teknis bengkel yang rapi."""
        if not text:
            return ""
        s = re.sub(r"\|\s*Pinout\s*&\s*Warna\s*Kabel:.*$", "", text, flags=re.IGNORECASE).strip()
        s = re.sub(r"^Solusi\s*Manual\s*:\s*", "", s, flags=re.IGNORECASE).strip()
        s = re.sub(r"\bE\s*G\s*R\s*v\s*a\s*l\s*v\s*e\b", "Katup EGR (EGR Valve)", s, flags=re.IGNORECASE)
        s = re.sub(r"\bEGRvalve\b", "Katup EGR (EGR Valve)", s, flags=re.IGNORECASE)
        s = re.sub(r"\bE\s+C\s+M\b", "ECM", s)
        s = re.sub(r"\bT\s+C\s+M\b", "TCM", s)
        s = re.sub(r"\bB\s+C\s+M\b", "BCM", s)
        s = re.sub(r"\bS\s+D\s+M\b", "SDM", s)
        s = re.sub(r"[“\"']?atauN[”\"']?", '"ORN" (Oranye)', s)
        s = re.sub(r"\bG\s+anti\b", "Ganti", s)
        s = re.sub(r"\bSIrkuit\b", "Sirkuit", s)
        s = re.sub(r"\bSistim\b", "Sistem", s)
        s = re.sub(r"\bsistim\b", "sistem", s)
        s = re.sub(r"\bkoslet\b", "hubung singkat (korsleting)", s, flags=re.IGNORECASE)
        s = re.sub(r"\bbattery\b", "Baterai (Aki)", s, flags=re.IGNORECASE)
        s = re.sub(r"\bcoupler\b", "soket konektor (coupler)", s, flags=re.IGNORECASE)
        s = re.sub(r"\bwire\s+harness\b", "kabel bodi (wire harness)", s, flags=re.IGNORECASE)
        s = re.sub(r"\s*Lanjut\s+ke\s+Langkah\s+\d+\.?\s*", " ", s, flags=re.IGNORECASE)
        s = re.sub(r"\s*Periksa\s+intermittent\s+lihat.*$", "", s, flags=re.IGNORECASE)
        s = re.sub(r"\s+", " ", s).strip(" .;,-|")
        return s

    @classmethod
    def _structure_manual_dtc_causes(
        cls,
        dtc_entries: list[dict[str, str]],
        cat_entry: dict[str, Any] | None,
    ) -> tuple[str, list[dict[str, str]]]:
        """Menyusun ringkasan dan daftar poin Akar Masalah Kerusakan yang rapi dan terstruktur untuk setiap kode DTC."""
        primary = dtc_entries[0]
        code = primary["code"]
        desc_id = primary["description_id"]

        raw_causes_str = ""
        if cat_entry and cat_entry.get("common_causes"):
            raw_causes_str = str(cat_entry["common_causes"])
        elif primary.get("possible_causes"):
            raw_causes_str = str(primary["possible_causes"])

        # Bersihkan bagian Pinout & Warna Kabel yang menempel di string penyebab
        raw_causes_str = re.sub(r"\|\s*Pinout\s*&\s*Warna\s*Kabel:.*$", "", raw_causes_str, flags=re.IGNORECASE).strip()

        # Pecah berdasarkan titik koma atau pipa
        raw_parts = [cls._clean_manual_phrase(p) for p in re.split(r"[;|]+", raw_causes_str) if cls._clean_manual_phrase(p)]

        # Kamus pemetaan frasa singkat ke penjelasan yang terstruktur
        phrase_enrichment: list[tuple[tuple[str, ...], str, str]] = [
            (("ignition", "pengapian", "coil", "busi"), "Sistem Pengapian (Ignition Coil & Busi)", "Koil pengapian bocor/lemah, busi aus (celah melebar), atau jalur pemicu pengapian bermasalah."),
            (("injector", "injektor"), "Injektor Bahan Bakar & Sirkuit Injeksi", "Nosel injektor tersumbat/menetes, tahanan koil injektor abnormal, atau soket injektor kendor."),
            (("fuel pressure", "tekanan bahan bakar", "fuel pump"), "Tekanan Pompa Bensin (Fuel Pressure)", "Pompa bensin lemah (< 3.0 bar), filter BBM tersumbat, atau regulator tekanan bensin bocor."),
            (("egr",), "Sistem Katup EGR (Exhaust Gas Recirculation)", "Katup EGR macet terbuka atau saluran gas buang EGR tersumbat kerak karbon."),
            (("udara masuk", "vacuum", "vakum"), "Kebocoran Vakum Udara Intake (Unmetered Air)", "Udara liar masuk melalui selang vakum retak, paking intake manifold, atau seal throttle body."),
            (("wheel speed", "sensor abs"), "Sensor Kecepatan Roda (ABS Wheel Speed Sensor)", "Ujung magnet sensor roda tertutup serbuk besi, celah rotor berubah, atau kabel sensor putus/korslet."),
            (("shift solenoid", "solenoid valve"), "Katup Solenoid Transmisi Otomatis (Shift Solenoid)", "Kumparan solenoid transmisi putus/macet, saluran oli A/T kotor, atau valve body bermasalah."),
            (("transponder", "immobilizer", "icm"), "Sistem Transponder Kunci & Modul Immobilizer (ICM)", "Chip transponder kunci kontak tidak terbaca/belum teregistrasi atau antena cincin immobilizer rusak."),
            (("inside air", "ambient", "hvac", "evaporator"), "Sensor Suhu Kabin / AC & Modul Kontrol HVAC", "Termistor sensor suhu AC putus/menyimpang atau jalur kabel ke modul kontrol AC (HVAC) kendor."),
            (("initiator", "air bag", "sdm", "pretensioner"), "Sirkuit Modul SRS Airbag / Clock Spring (Contact Coil)", "Kabel spiral kemudi (contact coil) putus/korslet, soket kuning airbag kendor, atau modul SDM bermasalah."),
        ]

        cause_items: list[dict[str, str]] = []
        seen_titles: set[str] = set()

        for part in raw_parts:
            p_low = part.lower()
            if len(part) < 3 or p_low in ("ecm", "tcm", "bcm", "perbaikan selesai"):
                continue
            matched = False
            for kw_tuple, nice_title, nice_desc in phrase_enrichment:
                if any(k in p_low for k in kw_tuple):
                    if nice_title not in seen_titles:
                        seen_titles.add(nice_title)
                        badge = "Penyebab Utama #1" if len(cause_items) == 0 else f"Penyebab #{len(cause_items) + 1}"
                        cause_items.append({"badge": badge, "title": nice_title, "desc": nice_desc})
                    matched = True
                    break
            if not matched and len(part) <= 140:
                title_clean = part[0].upper() + part[1:] if part else part
                if title_clean not in seen_titles:
                    seen_titles.add(title_clean)
                    badge = "Penyebab Utama #1" if len(cause_items) == 0 else f"Penyebab #{len(cause_items) + 1}"
                    cause_items.append({
                        "badge": badge,
                        "title": title_clean,
                        "desc": f"Terdeteksi gangguan komponen atau rangkaian kelistrikan pada bagian {title_clean.lower()} sesuai buku manual.",
                    })
            if len(cause_items) >= 4:
                break

        if not cause_items:
            cause_items = [
                {
                    "badge": "Penyebab Utama #1",
                    "title": f"Kerusakan Komponen / Sensor ({desc_id})",
                    "desc": f"Komponen utama pada sirkuit {desc_id} mengalami keausan, putus kumparan, atau nilai di luar spesifikasi standar.",
                },
                {
                    "badge": "Penyebab #2",
                    "title": "Konektor Soket Kendor / Kabel Harness Putus atau Korslet",
                    "desc": "Terjadi resistansi kontak tinggi pada pin soket atau kabel bodi terkelupas/hubung singkat ke massa/power.",
                },
                {
                    "badge": "Penyebab #3",
                    "title": "Gangguan Suplai Tegangan / Modul Kontrol (ECU/TCM/BCM)",
                    "desc": "Suplai tegangan referensi (+12V / +5V) atau jalur massa ground ke modul kontrol tidak stabil.",
                },
            ]

        clean_summary = (
            f"Kode {code} ({desc_id}) menunjukkan adanya gangguan pada {cause_items[0]['title'].lower()}, "
            "baik akibat kerusakan komponen utama maupun masalah pada soket dan jalur kabelnya."
        )
        return clean_summary, cause_items

    @classmethod
    def _structure_manual_dtc_repair_options(
        cls,
        primary: dict[str, str],
        cat_entry: dict[str, Any] | None,
        pinouts: list[dict[str, str]],
    ) -> list[dict[str, str]]:
        """Menyusun Opsi-Opsi Tindakan Perbaikan yang Terbukti (diurutkan logis: servis/bersihkan/uji komponen dulu -> soket/kabel -> suplai/scanner/ECM)."""
        if cat_entry and cat_entry.get("curated_repair_options"):
            return [dict(opt) for opt in cat_entry["curated_repair_options"]]

        code = primary["code"]
        desc_id = primary["description_id"]
        pin_str = ", ".join(p["pin"].split(" ")[0] for p in pinouts[:3]) if pinouts else "terminal modul"

        raw_remedies: list[str] = []
        if cat_entry and cat_entry.get("remedies"):
            raw_remedies = [cls._clean_manual_phrase(str(r)) for r in cat_entry["remedies"] if cls._clean_manual_phrase(str(r))]

        # Saring keluar kalimat tidak informatif seperti "Perbaikan selesai" atau "Lakukan perbaikan sesuai diagram alir"
        filtered_remedies: list[str] = []
        for r in raw_remedies:
            r_low = r.lower()
            if any(skip in r_low for skip in ("perbaikan selesai", "diagram alir", "langkah 10", "langkah 16")):
                continue
            if len(r) > 160:
                continue
            if r not in filtered_remedies:
                filtered_remedies.append(r)

        # Urutkan agar tindakan penggantian/perbaikan komponen inti berada di urutan atas, bukan "ganti ECM" atau "tambah bensin" di nomor 1
        def _remedy_priority(text: str) -> int:
            t = text.lower()
            if "tambahkan bahan bakar" in t:
                return 90
            if "ganti ecm" in t and len(t) < 40:
                return 80
            if any(k in t for k in ("coil", "busi", "sensor", "solenoid", "actuator", "relay", "injector", "injektor", "valve")):
                return 10
            if any(k in t for k in ("kabel", "sirkuit", "soket", "coupler", "harness")):
                return 20
            return 30

        filtered_remedies.sort(key=_remedy_priority)

        options: list[dict[str, str]] = []
        for idx, rem in enumerate(filtered_remedies[:3], start=1):
            tag = "Opsi 1 • Utama" if idx == 1 else f"Opsi {idx} • Alternatif"
            title = rem[0].upper() + rem[1:] if rem else rem
            options.append({
                "tag": tag,
                "title": title,
                "desc": f"Tindakan penyelesaian sesuai prosedur pemeriksaan kode {code} pada Buku Pedoman Resmi.",
            })

        # Pastikan selalu ada minimal 3 opsi yang komprehensif untuk dipilih teknisi
        default_candidates = [
            {
                "tag": "Opsi 1 • Utama (Komponen)",
                "title": f"Ganti / Servis Komponen Utama ({desc_id})",
                "desc": f"Periksa dan ganti unit sensor/aktuator pada sirkuit '{desc_id}' bila hasil ukur multimeter di luar standar.",
            },
            {
                "tag": "Opsi 2 • Soket & Kabel",
                "title": f"Perbaiki Soket Konektor & Jalur Kabel ({pin_str})",
                "desc": f"Bersihkan pin konektor dengan contact cleaner, rapatkan pin kendor, dan perbaiki kabel putus/korslet menuju {pin_str}.",
            },
            {
                "tag": "Opsi 3 • Suplai & Kalibrasi",
                "title": f"Periksa Sekering / Massa Ground & Reset Memori DTC {code}",
                "desc": "Pastikan suplai tegangan kerja (12V/5V) dan titik ground normal (< 0.3V), lalu hapus DTC via scan tool.",
            },
        ]

        for cand in default_candidates:
            if len(options) >= 3:
                break
            if not any(cand["title"].lower()[:20] in ex["title"].lower() for ex in options):
                cand_copy = dict(cand)
                cand_copy["tag"] = "Opsi 1 • Utama (Komponen)" if len(options) == 0 else f"Opsi {len(options) + 1} • {'Soket & Kabel' if len(options) == 1 else 'Suplai & Reset'}"
                options.append(cand_copy)

        return options

    @classmethod
    def _build_advice_from_manual_dtc_entries(
        cls,
        dtc_entries: list[dict[str, str]],
        wiring_rows: Sequence[WiringDiagram],
        sensor_rows: Sequence[SensorSpec],
    ) -> ManualRepairAdvice:
        """Menyusun ManualRepairAdvice langsung dari ekstraksi mendalam Buku Manual (`jb420_extracted_catalog.json` + `dtc_codes` + `wiring_diagrams`)."""
        codes = [d["code"] for d in dtc_entries]
        primary = dtc_entries[0]
        dtc_str = ", ".join(codes)
        combined_desc = " ".join(f"{d['code']} {d['system']} {d['description_id']} {d['possible_causes']}" for d in dtc_entries)
        cat_map = cls._get_jb420_dtc_catalog_map()
        cat_entry = cat_map.get(primary["code"].upper())

        # Jika tercakup oleh handler spesialis sensor utama (P0480, MAF, O2, ECT, TPS, CKP, Misfire P0300, dll.),
        # gunakan Akar Masalah & Multi-Opsi Tindakan Perbaikan spesialis yang sudah terstruktur rapi!
        specialist = cls.get_repair_manual_guidance(primary["description_id"], dtc_str)
        if specialist.system_category != "Umum":
            if primary["system"] and "Vol " in primary["system"]:
                doc_tag = f" [ID: {cat_entry['suzuki_doc_id']}]" if cat_entry and cat_entry.get("suzuki_doc_id") else ""
                specialist.manual_book_section = f"Buku Pedoman Resmi: {primary['system']}{doc_tag} — Kode DTC {dtc_str}"
            if len(dtc_entries) > 1:
                multi_desc = "; ".join(f"{d['code']} ({d['description_id']})" for d in dtc_entries)
                specialist.diagnosis_title = f"Terdeteksi Multi-DTC Manual Book: {multi_desc}"
            if cat_entry:
                if cat_entry.get("idle_standards"):
                    specialist.idle_standards = [dict(x) for x in cat_entry["idle_standards"]]
                if cat_entry.get("scanner_standards"):
                    specialist.scanner_standards = [dict(x) for x in cat_entry["scanner_standards"]]
                if cat_entry.get("sim_circuit_key"):
                    specialist.sim_circuit_key = str(cat_entry["sim_circuit_key"])
                if cat_entry.get("atlas_module_id"):
                    specialist.atlas_module_id = str(cat_entry["atlas_module_id"])
                if cat_entry.get("wiring_ref_id"):
                    specialist.wiring_ref_id = str(cat_entry["wiring_ref_id"])
                if cat_entry.get("oem_wiring_image"):
                    specialist.oem_wiring_image = str(cat_entry["oem_wiring_image"])
                if cat_entry.get("shared_with_dtcs"):
                    specialist.shared_with_dtcs = [str(x) for x in cat_entry["shared_with_dtcs"]]
                if cat_entry.get("wiring_cross_ref_note"):
                    specialist.wiring_cross_ref_note = str(cat_entry["wiring_cross_ref_note"])
                specialist.atlas_photo_index = int(cat_entry.get("atlas_photo_index") or 0)
                if cat_entry.get("manual_page_ref"):
                    specialist.manual_page_ref = str(cat_entry["manual_page_ref"])
                if cat_entry.get("verification_status"):
                    specialist.verification_status = str(cat_entry["verification_status"])
                if cat_entry.get("connector"):
                    specialist.connector = dict(cat_entry["connector"])
                if cat_entry.get("wiring_pinout"):
                    specialist.wiring_pinout = [
                        {
                            "pin": str(p.get("pin", "-")),
                            "signal": str(p.get("signal", "-")),
                            "function": str(p.get("function", "-")),
                        }
                        for p in cat_entry["wiring_pinout"]
                    ]
            return specialist

        sys_cat, grp_cat = cls._classify_dtc_workshop_system(primary["code"], primary["system"], primary["description_id"])

        # 1. Prioritaskan Pinout & Warna Kabel ASLI per-DTC hasil ekstraksi halaman Buku Manual!
        pinouts: list[dict[str, str]] = []
        if cat_entry and cat_entry.get("wiring_pinout"):
            for p_item in cat_entry["wiring_pinout"][:8]:
                pinouts.append({
                    "pin": str(p_item.get("pin", "-")),
                    "signal": str(p_item.get("signal", "-")),
                    "function": str(p_item.get("function", "-")),
                })
        if not pinouts:
            pinouts = cls._select_pinouts_for_manual_dtc(codes, combined_desc, wiring_rows)
        if not pinouts:
            pinouts = [
                {"pin": "E23-01 (Pin 1)", "signal": "BLU/BLK — Main Power Supply", "function": "Suplai tegangan utama 10-14V IG ON dari Main Relay"},
                {"pin": "C37-57 (Pin 2)", "signal": "GRY/GRN — Main Sensor Ground", "function": "Jalur massa referensi sensor/aktuator (< 0.3V)"},
            ]

        # 2. Prioritaskan Spesifikasi Tegangan/Ohm ASLI yang diekstrak dari langkah pemeriksaan Buku Manual!
        standards: list[dict[str, str]] = []
        if cat_entry and cat_entry.get("standard_specs"):
            for sp_item in cat_entry["standard_specs"][:4]:
                standards.append({
                    "parameter": str(sp_item.get("parameter", "Pemeriksaan Multimeter")),
                    "normal_range": str(sp_item.get("normal_range", "-")),
                    "unit": str(sp_item.get("unit", "V")),
                })

        desc_low = combined_desc.lower()
        if len(standards) < 2:
            matched_sp = None
            for sp in sensor_rows:
                sp_name_low = sp.sensor_name.lower()
                if (
                    ("pedal" in desc_low and "app" in sp_name_low)
                    or ("manifold" in desc_low and "map" in sp_name_low)
                    or ("intake air" in desc_low and "iat" in sp_name_low)
                    or ("coolant" in desc_low and "ect" in sp_name_low)
                    or ("throttle" in desc_low and "tps" in sp_name_low)
                ):
                    matched_sp = sp
                    break

            if matched_sp:
                standards.extend([
                    {"parameter": f"Tegangan Idle ({matched_sp.sensor_name[:35]})", "normal_range": matched_sp.voltage_idle, "unit": "V"},
                    {"parameter": "Tegangan Kerja / Beban Penuh", "normal_range": matched_sp.voltage_wot, "unit": "V"},
                    {"parameter": "Standar Tahanan & Ground", "normal_range": matched_sp.resistance_ohm, "unit": "Ohm"},
                ])
            elif any(c.startswith(("P07", "P09", "P17", "P18", "P27")) for c in codes):
                standards.extend([
                    {"parameter": "Suplai Daya Utama TCM (E92-06 IG ON)", "normal_range": "10.0 - 14.0 V", "unit": "V"},
                    {"parameter": "Tegangan Shift Solenoid A/B pada Posisi P (E92-15/16)", "normal_range": "9.0 - 14.0 V", "unit": "V"},
                    {"parameter": "Ground TCM (E92-01 & E92-23)", "normal_range": "0.0 - 0.5 V (< 1 Ohm ke bodi)", "unit": "V"},
                ])
            elif any(c.startswith("U") for c in codes) or "can" in desc_low or "komunikasi" in desc_low:
                standards.extend([
                    {"parameter": "Tegangan Jalur CAN High (E23-04 / E03-06 / E92-17)", "normal_range": "2.5 - 3.6 V (Pulsa Data)", "unit": "V"},
                    {"parameter": "Tegangan Jalur CAN Low (E23-19 / E03-12 / E92-07)", "normal_range": "1.6 - 2.5 V (Pulsa Data)", "unit": "V"},
                    {"parameter": "Tahanan Terminasi Bus CAN (Aki Dilepas)", "normal_range": "54 - 66 Ohm (2 Resistor 120Ω Paralel)", "unit": "Ohm"},
                ])
            elif any(c.startswith("C10") for c in codes):
                standards.extend([
                    {"parameter": "Suplai Tegangan Modul ABS IG1 (E03-07) & +B (E03-13/26)", "normal_range": "10.0 - 14.0 V", "unit": "V"},
                    {"parameter": "Celah Udara Wheel Speed Sensor ke Encoder", "normal_range": "Bebas celah dudukan knuckle & bebas serbuk besi", "unit": "Spec"},
                    {"parameter": "Tahanan Ground Bodi Modul ABS (E03-01)", "normal_range": "< 1.0 Ohm", "unit": "Ohm"},
                ])
            elif any(c.startswith("B15") for c in codes):
                standards.extend([
                    {"parameter": "Suplai Daya Modul HVAC (G52-01 IG ON & G52-02 +B)", "normal_range": "10.0 - 14.0 V", "unit": "V"},
                    {"parameter": "Referensi +5V Sensor Aktuator HVAC (G52-14)", "normal_range": "4.0 - 6.0 V", "unit": "V"},
                ])
            elif any(c.startswith("B10") for c in codes):
                standards.extend([
                    {"parameter": "Suplai Daya Modul SDM Air Bag (G47-16 IG ON)", "normal_range": "≥ 8.0 V (Normal 10 - 14 V)", "unit": "V"},
                    {"parameter": "Ground Utama Modul SDM (G47-20)", "normal_range": "< 1.0 Ohm ke bodi", "unit": "Ohm"},
                ])
            else:
                standards.extend([
                    {"parameter": "Tegangan Suplai Modul Kontrol (IG ON)", "normal_range": "10.0 - 14.0 V", "unit": "V"},
                    {"parameter": "Tahanan Kontinuitas Kabel Harness Ujung-ke-Ujung", "normal_range": "< 2.0 Ohm", "unit": "Ohm"},
                ])
        standards = standards[:4]

        # 3. Gunakan Langkah Pemeriksaan & Saran Penyelesaian ASLI dari tabel Perbaikan DTC Buku Manual!
        authentic_steps: list[str] = []
        if cat_entry and cat_entry.get("repair_steps"):
            authentic_steps = [str(s) for s in cat_entry["repair_steps"] if str(s).strip()]
        elif primary.get("recommended_fix"):
            authentic_steps = [line.strip() for line in primary["recommended_fix"].splitlines() if line.strip()]

        if not authentic_steps:
            pin_codes_summary = ", ".join(p["pin"].split(" ")[0] for p in pinouts[:4])
            authentic_steps = [
                f"1. Verifikasi kode {dtc_str} menggunakan scan tool OBD-II dan catat data Freeze Frame ({primary['system']}).",
                f"2. Matikan kunci kontak, periksa konektor komponen terkait serta jalur terminal modul ({pin_codes_summary}) dari pin longgar, korosi, atau kabel koslet.",
                "3. Ukur tegangan suplai (+12V / +5V), tahanan kabel harness (< 2 Ohm), dan ground bodi/mesin menggunakan multimeter sesuai spesifikasi standar.",
                f"4. Perbaiki wiring harness yang putus/koslet atau ganti komponen pada sirkuit '{primary['description_id']}' sesuai petunjuk Buku Manual.",
            ]

        title_desc = (
            primary["description_id"]
            if len(dtc_entries) == 1
            else "; ".join(f"{d['code']}: {d['description_id']}" for d in dtc_entries)
        )
        clean_cause_summary, structured_causes = cls._structure_manual_dtc_causes(dtc_entries, cat_entry)
        structured_repair_options = cls._structure_manual_dtc_repair_options(primary, cat_entry, pinouts)
        doc_tag = f" [ID: {cat_entry['suzuki_doc_id']}]" if cat_entry and cat_entry.get("suzuki_doc_id") else ""

        idle_stds = [dict(x) for x in (cat_entry.get("idle_standards") or [])] if cat_entry else []
        scanner_stds = [dict(x) for x in (cat_entry.get("scanner_standards") or [])] if cat_entry else []
        sim_key = str(cat_entry.get("sim_circuit_key")) if cat_entry and cat_entry.get("sim_circuit_key") else None
        atlas_mod = str(cat_entry.get("atlas_module_id")) if cat_entry and cat_entry.get("atlas_module_id") else None
        wiring_ref = str(cat_entry.get("wiring_ref_id")) if cat_entry and cat_entry.get("wiring_ref_id") else None
        oem_img = str(cat_entry.get("oem_wiring_image")) if cat_entry and cat_entry.get("oem_wiring_image") else None
        shared_dtcs = [str(x) for x in (cat_entry.get("shared_with_dtcs") or [])] if cat_entry else []
        cross_note = str(cat_entry.get("wiring_cross_ref_note")) if cat_entry and cat_entry.get("wiring_cross_ref_note") else None
        atlas_pidx = int(cat_entry.get("atlas_photo_index") or 0) if cat_entry else 0
        conn_obj = dict(cat_entry["connector"]) if cat_entry and cat_entry.get("connector") else None
        ver_status = str(cat_entry.get("verification_status") or "VERIFIED_OEM") if cat_entry else "UNVERIFIED"
        page_ref = str(cat_entry.get("manual_page_ref")) if cat_entry and cat_entry.get("manual_page_ref") else None

        return ManualRepairAdvice(
            diagnosis_title=f"DTC {dtc_str}: {title_desc}",
            system_category=sys_cat,
            group_category=grp_cat,
            manual_book_section=f"Buku Pedoman Resmi: {primary['system']}{doc_tag} (Kode {dtc_str})",
            cause_summary=clean_cause_summary,
            cause_items=structured_causes,
            repair_options=structured_repair_options,
            sensor_standards=standards,
            idle_standards=idle_stds,
            scanner_standards=scanner_stds,
            sim_circuit_key=sim_key,
            atlas_module_id=atlas_mod,
            wiring_ref_id=wiring_ref,
            oem_wiring_image=oem_img,
            shared_with_dtcs=shared_dtcs,
            wiring_cross_ref_note=cross_note,
            atlas_photo_index=atlas_pidx,
            connector=conn_obj,
            verification_status=ver_status,
            manual_page_ref=page_ref,
            wiring_pinout=pinouts,
            step_by_step_repair=authentic_steps,
            relearn_reset_steps=[
                f"1. Hapus memori kode DTC {dtc_str} melalui scan tool dengan kunci kontak posisi ON (mesin mati).",
                f"2. Jalankan mesin / lakukan uji jalan sesuai 'Prosedur Menentukan DTC' pada {primary['system']} dan pastikan kode tidak muncul kembali.",
            ],
        )

    @staticmethod
    def _clean_and_dedupe_pack_pins(
        raw_pins: list[dict[str, Any]],
        pack_id: str,
        year: int | None = None,
        model_hint: str = "",
    ) -> list[dict[str, str]]:
        """
        Membersihkan baris non-kabel dari ekstraksi tabel pengecekan Toyota (seperti uji tahanan '1 - 2',
        uji isolasi '... atau ... - Masa bodi/Body ground', dan string gabungan 4 koil 1 baris)
        serta men-deduplikasi konektor beda tahun/model (C75 vs E11 di Fortuner; C20 vs C23 di Yaris/Vios).
        """
        if not raw_pins:
            return []

        cleaned: list[dict[str, str]] = []
        for pw in raw_pins:
            pin_s = str(pw.get("pin", "")).strip()
            sig_s = str(pw.get("signal", "-")).strip()
            fn_s = str(pw.get("function", "-")).strip()
            if not pin_s:
                continue
            pin_body = re.sub(r"^\[[^\]]+\]\s*", "", pin_s).strip()
            # 1. Buang baris uji tahanan komponen telanjang '1 - 2' (tidak memuat kode konektor!)
            if re.match(r"^\d\s*[-–]\s*\d$", pin_body):
                continue
            # 2. Buang baris uji isolasi short-to-ground ('... atau ... - Masa bodi / Body ground')
            if re.search(r"\batau\b.*(masa\s*bodi|body\s*ground)", pin_body, re.I):
                continue
            # 3. Buang baris rusak yang menggabungkan beberapa IGT sekaligus dalam satu sel ('IGT1 (...) IGT2 (...)')
            if len(re.findall(r"\bIGT\d\b", pin_body)) >= 2:
                continue
            cleaned.append({"pin": pin_s, "signal": sig_s, "function": fn_s})

        if not cleaned:
            cleaned = [
                {"pin": str(pw.get("pin", "-")), "signal": str(pw.get("signal", "-")), "function": str(pw.get("function", "-"))}
                for pw in raw_pins
            ]

        pid = (pack_id or "").lower()
        # 4. Deduplikasi konektor beda generasi pada Fortuner (2005: E10/E11 vs 2012: C75/C76)
        if "fortuner" in pid:
            has_c75 = any(re.search(r"\bC7[0-6]-", x["pin"]) for x in cleaned)
            has_e10 = any(re.search(r"\bE1[01]-", x["pin"]) for x in cleaned)
            if has_c75 and has_e10:
                if year is not None and year <= 2008:
                    cleaned = [x for x in cleaned if not re.search(r"\bC7[0-6]-", x["pin"])]
                else:
                    cleaned = [x for x in cleaned if not re.search(r"\bE1[01]-", x["pin"])]

        # 5. Deduplikasi konektor beda model pada Yaris/Vios (Yaris: C20/A21 vs Vios: C23/A20)
        if "yaris_vios" in pid:
            has_c20 = any(re.search(r"\b(C20|A21)-", x["pin"]) for x in cleaned)
            has_c23 = any(re.search(r"\b(C23|A20)-", x["pin"]) for x in cleaned)
            if has_c20 and has_c23:
                if "vios" in (model_hint or "").lower():
                    cleaned = [x for x in cleaned if not re.search(r"\b(C20|A21)-", x["pin"])]
                else:
                    cleaned = [x for x in cleaned if not re.search(r"\b(C23|A20)-", x["pin"])]

        # 6. Deduplikasi pin duplikat persis
        out: list[dict[str, str]] = []
        seen: set[str] = set()
        for x in cleaned:
            k = x["pin"].upper()
            if k not in seen:
                seen.add(k)
                out.append(x)
        return out

    @staticmethod
    def _select_custom_pack_pins(
        custom_pack: dict[str, Any],
        engine_code: str,
        fuel_type: str,
        diag_text: str,
        dtc_codes: Sequence[str],
        year: int | None = None,
        model_hint: str = "",
    ) -> list[dict[str, str]]:
        """
        Memilih pinout ASLI dari custom_pack secara presisi berdasarkan:
        1) Isolasi ketat kode mesin & bahan bakar (ZERO kebocoran lintas mesin seperti 3ZR-FE ke 2AZ-FE atau Bensin ke Diesel!)
        2) Blokir modul non-mesin ([AUDIO], [PARK ASSIST], [STARTING], [METER], [IMMOBILISER]) untuk DTC Engine Control
        3) Pencocokan komponen terpisah ketat (CKP vs CMP, HO2S-1 vs HO2S-2, Koil spesifik silinder, MAP vs MAF, ETC vs APP)
        4) Deduplikasi konektor beda tahun/model (Fortuner C75 vs E11; Yaris C20 vs Vios C23)
        """
        all_pins = list(custom_pack.get("wiring_pinouts", []))
        if not all_pins:
            return []

        pack_id = str(custom_pack.get("pack_id", "")).lower()
        eng_clean = re.sub(r"[^a-z0-9]", "", (engine_code or "").lower())
        codes_up = [str(c).upper() for c in dtc_codes]
        text_low = (diag_text or "").lower()

        # Pengaman khusus Ertiga Gen 1: tabel pinout C01/E01 hanya untuk K14B Bensin, BUKAN D13A Diesel!
        if pack_id == "suzuki_ertiga_gen1_2012_2017" and (fuel_type == "Diesel" or "d13a" in eng_clean):
            return []

        # Pengaman khusus Ertiga K14B untuk P0101-P0104 (MAF): K14B pakai Speed-Density (MAP + IAT), BUKAN MAF!
        if pack_id == "suzuki_ertiga_gen1_2012_2017" and any(re.match(r"^P010[0-4]$", c) for c in codes_up):
            return [
                {"pin": "C01-2", "signal": "GRY/RED — Suplai +5V Sensor MAP (K14B tanpa MAF)", "function": "Mesin K14B memakai MAP+IAT (tanpa MAF); Suplai +4.5–5.5 V IG ON"},
                {"pin": "C01-29", "signal": "RED/BLK — Sinyal Sensor MAP", "function": "Sinyal vakum intake manifold (3.85–4.35 V KOEO | 1.0–1.6 V Idle)"},
                {"pin": "C01-34", "signal": "BLK/YEL — Sinyal Sensor IAT", "function": "Sinyal suhu udara masuk (2.2–2.6 V @20°C | 1.3–1.7 V @40°C)"},
                {"pin": "C01-20", "signal": "GRY/BLU — Massa Sensor MAP & IAT", "function": "Massa sensor referensi ECM (< 0.3 V)"},
            ]

        # 1. Isolasi ketat berdasarkan tag kode mesin pada pack multi-mesin
        non_engine_mod_re = re.compile(r"^\[(AUDIO|PARK\s*ASSIST|STARTING|METER|ENGINE\s*IMMOBILIS|A/T|AIR\s*BAG|SRS|ABS|VSC|CRUISE)", re.I)
        is_fan_dtc = any(re.match(r"^P048[0-5]$", c) for c in codes_up) or bool(re.search(r"\b(kipas|cooling\s*fan|radiator\s*fan)\b", text_low))

        pool = [
            pw for pw in all_pins
            if not non_engine_mod_re.search(str(pw.get("pin", "")))
            and (is_fan_dtc or not re.match(r"^\[AIR\s*CONDITIONING", str(pw.get("pin", "")), re.I))
        ]
        if not pool:
            pool = all_pins

        has_engine_tags = any(re.search(r"\[(1|2|3|4|k3|ej|d13)[a-z0-9\-]{2,}", str(pw.get("pin", "")), re.I) for pw in pool)
        if eng_clean and len(eng_clean) >= 3 and has_engine_tags:
            eng_matched = [
                pw for pw in pool
                if eng_clean in re.sub(r"[^a-z0-9]", "", str(pw.get("pin", "")).lower())
            ]
            if eng_matched:
                pool = eng_matched
            else:
                # GUARDRAIL KETAT: JANGAN diam-diam memakai pinout mesin lain (mis. 3ZR-FE untuk 2AZ-FE)!
                return []
        elif fuel_type == "Diesel":
            diesel_only = [
                pw for pw in pool
                if re.search(r"\[(1kd|2kd|1gd|2gd|d13a|4d56|4n15)", str(pw.get("pin", "")), re.I)
            ]
            if diesel_only:
                pool = diesel_only
            elif has_engine_tags:
                return []

        # 2. Tentukan pola regex pin yang TERPISAH KETAT per subsistem
        pin_patterns: list[str] = []

        if any(re.match(r"^P030[0-8]$|^P035[1-8]$", c) for c in codes_up) or re.search(r"\b(misfire|koil|coil|pengapian|ignition|busi)\b", text_low):
            if fuel_type != "Diesel":
                pin_patterns.append(r"\b(igt[1-8]|igf\d?|ig[1-4](?!d)|koil\s*pengapian|ignition\s*coil)\b")
            else:
                pin_patterns.append(r"\b(inj\d?|injektor|injector|pcr|scv|edu)\b")
        elif any(re.match(r"^P008[78]$|^P0093$|^P019[0-4]$", c) for c in codes_up) or re.search(r"\b(fuel\s*rail|common.?rail|scv|pcr)\b", text_low):
            pin_patterns.append(r"\b(pcr\d?|pr\d?|scv|vcs|rail|injektor|injector)\b")
        elif any(re.match(r"^P033[5-9]$", c) for c in codes_up) or (re.search(r"\b(ckp|crankshaft|poros\s*engkol)\b", text_low) and not re.search(r"\b(cmp|camshaft)\b", text_low)):
            pin_patterns.append(r"\b(ne[+-]?|n1[+-]?|ckp|crankshaft|poros\s*engkol)\b")
        elif any(re.match(r"^P034[0-9]$", c) for c in codes_up) or re.search(r"\b(cmp|camshaft|poros\s*nok)\b", text_low):
            pin_patterns.append(r"(?<![A-Z0-9])\b(g2[+-]?(?!-\d)|n2[+-]?|vv1[+-]?|cmp|camshaft|poros\s*nok)\b")
        elif any(re.match(r"^P001[0-7]$", c) for c in codes_up) or re.search(r"\b(ocv|vvt)\b", text_low):
            pin_patterns.append(r"\b(ocv[+-]?|vvt|oil\s*control\s*valve)\b")
        elif any(re.match(r"^P011[5-9]$|^P012[58]$", c) for c in codes_up) or re.search(r"\b(ect|coolant|suhu\s*air|water\s*temp|thermostat)\b", text_low):
            pin_patterns.append(r"\b(thw|ethw|ect|coolant|suhu\s*air|water\s*temp)\b")
        elif any(re.match(r"^P011[0-4]$", c) for c in codes_up) or re.search(r"\b(iat|intake\s*air\s*temp|suhu\s*udara)\b", text_low):
            pin_patterns.append(r"\b(tha|etha|iat|intake\s*air\s*temp)\b")
        elif any(re.match(r"^P010[0-4]$", c) for c in codes_up) or re.search(r"\b(maf|mass\s*air\s*flow)\b", text_low):
            pin_patterns.append(r"\b(vg|e2g|evg|maf|mass\s*air\s*flow)\b")
            pin_patterns.append(r"\b(vcpm|pim|e2pm|map|tekanan\s*absolut)\b")
        elif any(re.match(r"^P010[5-9]$", c) for c in codes_up) or re.search(r"\b(map|pim|vakum|manifold)\b", text_low):
            pin_patterns.append(r"\b(vcpm|pim|e2pm|map|tekanan\s*absolut|manifold)\b")
            pin_patterns.append(r"\b(vg|e2g|evg|maf)\b")
        elif any(re.match(r"^P017[12]$", c) for c in codes_up):
            # P0171/P0172: Prioritaskan MAF jika mesin pakai MAF, atau MAP jika Speed-Density (jangan digabung dengan O2 ke 1 soket!)
            has_maf = any(re.search(r"\b(vg|e2g|evg|maf)\b", f"{pw.get('pin','')} {pw.get('signal','')}", re.I) for pw in pool)
            if has_maf:
                pin_patterns.append(r"\b(vg|e2g|evg|maf|tha|etha)\b")
            else:
                pin_patterns.append(r"\b(vcpm|pim|e2pm|map|c01-2\b|c01-29\b|c01-20\b)\b")
        elif any(re.match(r"^P003[0-2]$|^P013[0-5]$", c) for c in codes_up):
            if fuel_type == "Diesel":
                return []
            pin_patterns.append(r"\b(ha1a|a1a[+-]?|ht1a|ox1a|ox1|oxh1|ho2s-1|bank\s*1\s*sensor\s*1|o2\s*depan)\b")
        elif any(re.match(r"^P003[6-8]$|^P013[6-9]$|^P014[0-1]$", c) for c in codes_up):
            if fuel_type == "Diesel":
                return []
            pin_patterns.append(r"\b(ht1b|ox1b|ox2|ho2s-2|bank\s*1\s*sensor\s*2|o2\s*belakang)\b")
        elif re.search(r"\b(o2|ho2s|oxygen|oksigen|a/f|lambda)\b", text_low):
            if fuel_type == "Diesel":
                return []
            pin_patterns.append(r"\b(ha1a|a1a[+-]?|ht1a|ox1a|ox1|oxh1|ho2s-1|o2\s*depan)\b")
        elif any(re.match(r"^P012[0-4]$|^P022[0-3]$|^P0507$|^P21[013][0-9]$", c) for c in codes_up):
            # HARUS SEBELUM pedal/APP karena deskripsi OBD-II P0121 memuat frasa "Throttle/Pedal Position Sensor"!
            if fuel_type == "Diesel":
                pin_patterns.append(r"\b(vlu|lusl|diesel\s*throttle|throttle\s*control)\b")
            else:
                pin_patterns.append(r"\b(vta\d?|vcta|eta|vth|vc\b|tps|tp\s*sensor|m\+|m-|aktuator\s*throttle|throttle)\b")
        elif any(re.match(r"^P212[2-9]$|^P2138$", c) for c in codes_up) or re.search(r"\b(pedal|app|vpa)\b", text_low):
            pin_patterns.append(r"\b(vpa\d?|epa\d?|vcpa|vcp2|app|pedal)\b")
        elif re.search(r"\b(throttle|tps|vta|etc)\b", text_low):
            if fuel_type == "Diesel":
                pin_patterns.append(r"\b(vlu|lusl|diesel\s*throttle|throttle\s*control)\b")
            else:
                pin_patterns.append(r"\b(vta\d?|vcta|eta|vth|vc\b|tps|tp\s*sensor|m\+|m-|aktuator\s*throttle|throttle)\b")
        elif is_fan_dtc:
            pin_patterns.append(r"\b(fan\d?|fanl|fanh|rfc|kipas\s*radiator|fan\s*radiator|cooling\s*fan)\b")
        elif any(re.match(r"^P020[0-8]$", c) for c in codes_up) or re.search(r"\b(injektor|injector)\b", text_low):
            pin_patterns.append(r"\b(inj\d?|#10|#20|#30|#40|injektor|injector)\b")

        matched: list[dict[str, str]] = []
        seen_p: set[str] = set()
        for pat in pin_patterns:
            rx = re.compile(pat, re.I)
            for pw in pool:
                hay = f"{pw.get('pin', '')} {pw.get('signal', '')} {pw.get('function', '')}"
                if rx.search(hay):
                    # Jangan masukkan pinout bensin (koil/busi) pada mesin Diesel
                    if fuel_type == "Diesel" and re.search(r"\b(igt|igf|koil|ignition\s*coil)\b", hay, re.I):
                        continue
                    # Jangan masukkan pin Sensor O2 (VTH E8-2) saat mencari TPS (VTH E8-20) pada Avanza!
                    if "throttle" in pat and re.search(r"oxygen|oksigen|\bo2\b|oxh|e8-2\b", hay, re.I):
                        continue
                    # Jangan masukkan pin Pedal Gas (VPA/VCPA/EPA) saat mencari Throttle Body (VTA/TPS)!
                    if "vta" in pat and re.search(r"\b(vpa\d?|vcpa|vcp2|epa\d?|pedal\s*akselerator|accelerator\s*pedal)\b", hay, re.I):
                        continue
                    # Jangan masukkan Solenoid OCV (OC1+/OCV+) ke Sensor CMP (P0340)!
                    if "g2" in pat and re.search(r"\b(ocv|oc1|oil\s*control|katup\s*kontrol\s*oli)\b", hay, re.I):
                        continue
                    # Jangan masukkan Sensor CMP (G2/N2) ke Sensor CKP (P0335)!
                    if "ne[" in pat and re.search(r"\b(g2\b|n2[+-]|camshaft|poros\s*nok)\b", hay, re.I):
                        continue
                    pk = str(pw.get("pin", "-"))
                    if pk not in seen_p:
                        seen_p.add(pk)
                        matched.append({
                            "pin": pk,
                            "signal": str(pw.get("signal", "-")),
                            "function": str(pw.get("function", "-")),
                        })
                    if len(matched) >= 10:
                        break
            if matched:
                break

        cleaned = WeightedDiagnosticEngine._clean_and_dedupe_pack_pins(
            matched, pack_id=pack_id, year=year, model_hint=model_hint
        )

        # Hanya tambahkan ground sensor (C01-20) bila format pin SUZUKI tunggal (bukan pasangan Toyota 'PinA - PinB'!)
        if len(cleaned) == 1 and " - " not in cleaned[0]["pin"] and pack_id.startswith("suzuki_"):
            for pw in pool:
                hay = f"{pw.get('pin', '')} {pw.get('signal', '')}"
                if re.search(r"\bc01-20\b", hay, re.I):
                    cleaned.append({
                        "pin": str(pw.get("pin", "-")),
                        "signal": str(pw.get("signal", "-")),
                        "function": str(pw.get("function", "-")),
                    })
                    break

        return cleaned[:6]

    @classmethod
    async def search_weighted_cases(
        cls,
        session: AsyncSession,
        req: WeightedCaseSearchRequest,
    ) -> WeightedCaseSearchResponse:
        """
        Mengeksekusi pencarian diagnosa terpadu (Hybrid Historical Cases + Embedded Manual Repair Book):
        - Membaca seluruh tabel `HistoricalCase` DAN mencocokkan langsung ke 207+ kode resmi `DTCCode`,
          pinout 8 Modul Kontrol `WiringDiagram` (251 Pin), dan `SensorSpec` dari Buku Manual yang ditanamkan!
        - Menghitung Skor Teks & Live Data serta menyusun ranking sistem akurat.
        """
        # 0. Resolusi Model, Generasi Platform, Kode Mesin, Jenis BBM & Tahun Kendaraan (Safety Guardrail)
        app_info, custom_pack = resolve_vehicle_applicability(
            req.brand, req.model, req.year, req.engine_code
        )
        vehicle_fuel = app_info.resolved_fuel_type or "Bensin"

        # Evaluasi Live Data Adaptif (Diesel Common-Rail & Hybrid/EV)
        adaptive_live_findings = evaluate_adaptive_live_data(
            fuel_type=vehicle_fuel,
            rail_pressure_mpa=req.rail_pressure_mpa,
            boost_kpa=req.boost_kpa,
            inj_feedback_mm3=req.inj_feedback_mm3,
            egr_pct=req.egr_pct,
            hv_soc_pct=req.hv_soc_pct,
            hv_cell_delta_mv=req.hv_cell_delta_mv,
            hv_insulation_mohm=req.hv_insulation_mohm,
            hv_temp_c=req.hv_temp_c,
        )

        # 1. Ambil seluruh kasus historis + referensi Buku Manual dari database
        cases = (
            await session.execute(select(HistoricalCase).order_by(HistoricalCase.case_code.asc()))
        ).scalars().all()
        wiring_rows = (await session.execute(select(WiringDiagram))).scalars().all()
        sensor_rows = (await session.execute(select(SensorSpec))).scalars().all()

        req_codes = cls._extract_all_request_dtcs(req)
        manual_dtc_entries: list[dict[str, str]] = []
        custom_dtc_map: dict[str, dict[str, Any]] = {}
        modern_dtc_entries_map: dict[str, dict[str, Any]] = {}
        if custom_pack:
            for cd in custom_pack.get("dtc_catalog", []):
                c_key = str(cd.get("code", "")).strip().upper()
                if c_key:
                    custom_dtc_map[c_key] = cd

        if req_codes:
            db_dtcs = (
                await session.execute(select(DTCCode).where(DTCCode.code.in_(req_codes)))
            ).scalars().all()
            db_dtc_map = {row.code.upper(): row for row in db_dtcs}
            for code in req_codes:
                modern_hit = lookup_modern_dtc(code, vehicle_fuel)
                # Prioritaskan katalog modern untuk Diesel/EV/Hybrid atau kode yang belum ada di katalog JB420
                use_modern = (
                    modern_hit is not None
                    and code not in custom_dtc_map
                    and (vehicle_fuel in {"Diesel", "EV", "Hybrid"} or code not in db_dtc_map)
                )
                if code in custom_dtc_map:
                    cd = custom_dtc_map[code]
                    cd_desc = str(cd.get("description_id", f"DTC {code}"))
                    cd_causes_raw = cd.get("common_causes", "")
                    causes_val = "; ".join(str(x) for x in cd_causes_raw) if isinstance(cd_causes_raw, list) else str(cd_causes_raw)
                    # Guardrail BBM: cegah DTC khusus Bensin (mis. P0300 K14B Koil/Busi) masuk ke kendaraan Diesel (D13A)!
                    is_k14b_on_diesel = (
                        vehicle_fuel == "Diesel"
                        and ("k14b" in cd_desc.lower() or not is_text_compatible_with_fuel(f"{cd_desc} {causes_val}", vehicle_fuel))
                        and "d13a" not in cd_desc.lower()
                        and "diesel" not in cd_desc.lower()
                    )
                    if not is_k14b_on_diesel:
                        steps_val = cd.get("repair_steps", [])
                        manual_dtc_entries.append({
                            "code": code,
                            "system": str(custom_pack.get("title", "Buku Manual Kustom")),
                            "description_id": cd_desc,
                            "possible_causes": str(causes_val or cd_desc),
                            "recommended_fix": "\n".join(str(s) for s in steps_val) if isinstance(steps_val, list) else str(cd.get("recommended_fix", "")),
                            "severity_level": str(cd.get("severity_level", "HIGH")),
                        })
                        continue
                if use_modern and modern_hit:
                    modern_dtc_entries_map[code] = modern_hit
                    manual_dtc_entries.append({
                        "code": code,
                        "system": f"Katalog Universal {vehicle_fuel} / Modern OBD-II ({modern_hit['system_category']})",
                        "description_id": str(modern_hit["title_id"]),
                        "possible_causes": str(modern_hit["root_causes"]),
                        "recommended_fix": "\n".join(modern_hit.get("repair_steps", [])),
                        "severity_level": str(modern_hit.get("severity", "HIGH")),
                    })
                elif code in db_dtc_map:
                    r = db_dtc_map[code]
                    if is_text_compatible_with_fuel(f"{r.description_id} {r.possible_causes}", vehicle_fuel):
                        manual_dtc_entries.append({
                            "code": r.code,
                            "system": r.system,
                            "description_id": r.description_id,
                            "possible_causes": r.possible_causes,
                            "recommended_fix": r.recommended_fix or "",
                            "severity_level": r.severity_level,
                        })
                elif code in cls.STANDARD_OBD_FALLBACK:
                    fb = cls.STANDARD_OBD_FALLBACK[code]
                    if is_text_compatible_with_fuel(f"{fb['description_id']} {fb['possible_causes']}", vehicle_fuel):
                        manual_dtc_entries.append({
                            "code": code,
                            "system": fb["system"],
                            "description_id": fb["description_id"],
                            "possible_causes": fb["possible_causes"],
                            "recommended_fix": "",
                            "severity_level": fb["severity_level"],
                        })
        else:
            # Jika mekanik tidak mengetik kode DTC tapi menulis komponen spesifik
            raw_text_low = f"{req.complaint or ''} {req.symptom or ''}".lower()
            if vehicle_fuel == "Diesel":
                diesel_kw_hints = [
                    (("turbo", "underboost", "intercooler", "vnt", "wastegate"), "P0299"),
                    (("rail", "scv", "suction control", "filter solar", "masuk angin", "backleak"), "P0087"),
                    (("egr", "jelaga", "asap hitam"), "P0401"),
                    (("dpf", "partikulat"), "P2002"),
                    (("glow plug", "busi pemanas"), "P0380"),
                    (("edu", "driver injektor"), "P062D"),
                ]
                for phrases, target_dtc in diesel_kw_hints:
                    if any(p in raw_text_low for p in phrases):
                        mh = lookup_modern_dtc(target_dtc, "Diesel")
                        if mh:
                            modern_dtc_entries_map[target_dtc] = mh
                            manual_dtc_entries.append({
                                "code": target_dtc,
                                "system": f"Katalog Universal Diesel Common-Rail ({mh['system_category']})",
                                "description_id": mh["title_id"],
                                "possible_causes": mh["root_causes"],
                                "recommended_fix": "\n".join(mh.get("repair_steps", [])),
                                "severity_level": mh.get("severity", "HIGH"),
                            })
                        break
            elif vehicle_fuel == "EV":
                ev_kw_hints = [
                    (("isolasi", "isolation", "nyetrum", "kompresor ac"), "P0AA6"),
                    (("baterai", "battery", "sel drop", "imbalance", "tidak bisa ready", "ready"), "P0A80"),
                    (("inverter", "overheat", "coolant inverter"), "P0A93"),
                    (("dc/dc", "dc-dc", "aki 12v tidak mengisi"), "P0A94"),
                ]
                for phrases, target_dtc in ev_kw_hints:
                    if any(p in raw_text_low for p in phrases):
                        mh = lookup_modern_dtc(target_dtc, "EV")
                        if mh:
                            modern_dtc_entries_map[target_dtc] = mh
                            manual_dtc_entries.append({
                                "code": target_dtc,
                                "system": f"Katalog Universal EV / Tegangan Tinggi ({mh['system_category']})",
                                "description_id": mh["title_id"],
                                "possible_causes": mh["root_causes"],
                                "recommended_fix": "\n".join(mh.get("repair_steps", [])),
                                "severity_level": mh.get("severity", "CRITICAL"),
                            })
                        break

            if not manual_dtc_entries and vehicle_fuel != "EV":
                keyword_dtc_hints = [
                    (("kipas radiator", "cooling fan", "extra fan", "kipas mati"), "P0480"),
                    (("wheel speed", "sensor abs", "lampu abs"), "C1021"),
                    (("pompa abs", "abs pump"), "C1061"),
                    (("air bag", "airbag", "lampu srs", "pretensioner"), "B1031"),
                    (("shift solenoid", "transmisi matic", "gigi matic"), "P0751"),
                    (("sensor suhu kabin", "inside air", "ac otomatis", "blower ac"), "B1502"),
                    (("pedal gas", "app sensor"), "P2122"),
                    (("generator", "alternator", "aki tekor", "pengisian"), "P0620"),
                    (("starter relay", "tidak bisa starter"), "P0616"),
                    (("steering lock", "keyless start"), "KLS-11"),
                    (("immobilizer", "transponder"), "P1614"),
                ]
                for phrases, target_dtc in keyword_dtc_hints:
                    if any(p in raw_text_low for p in phrases):
                        row_kw = (
                            await session.execute(select(DTCCode).where(DTCCode.code == target_dtc))
                        ).scalar_one_or_none()
                        if row_kw and is_text_compatible_with_fuel(f"{row_kw.description_id} {row_kw.possible_causes}", vehicle_fuel):
                            manual_dtc_entries.append({
                                "code": row_kw.code,
                                "system": row_kw.system,
                                "description_id": row_kw.description_id,
                                "possible_causes": row_kw.possible_causes,
                                "recommended_fix": row_kw.recommended_fix or "",
                                "severity_level": row_kw.severity_level,
                            })
                        break

        # Filter sistem jika diminta pengguna (B16 pada sheet)
        filtered_system = req.system_filter.strip() if req.system_filter and req.system_filter.strip().lower() not in {"", "semua", "all"} else None

        scored_items: list[WeightedCaseMatchItem] = []
        has_any_live_data = any(
            v is not None for v in [req.stft, req.ltft, req.rpm, req.o2, req.map_kpa, req.maf_gps, req.ect_c]
        )

        # Mapping skor per sistem: list[(score_0_to_1, diagnosis_label, case_code)]
        system_stats: dict[str, list[tuple[float, str, str]]] = {
            s["name"]: [] for s in cls.SYSTEM_DEFINITIONS
        }

        exact_historical_dtc_best = 0.0
        req_codes_set = set(req_codes)

        for case in cases:
            # Guardrail kesesuaian jenis mesin: cegah kasus bensin (sensor O2/busi/koil) masuk ke EV atau busi/koil masuk ke Diesel
            if not is_text_compatible_with_fuel(
                f"{case.final_diagnosis} {case.repair_action} {case.complaint} {case.symptom}",
                vehicle_fuel,
            ):
                continue

            t_score = cls._calculate_text_similarity(req, case)
            l_score = cls._calculate_live_similarity(req, case)

            if has_any_live_data and l_score is not None:
                tot_score = ((1.0 - 0.15) * t_score) + (0.15 * l_score)
            else:
                tot_score = t_score

            # Bonus tie-breaker +2% (maks 100%) untuk kasus TERVERIFIKASI Kepala Bengkel (REQ-14)
            ver_status = (getattr(case, "verification_status", None) or "TERVERIFIKASI").upper()
            if ver_status == "TERVERIFIKASI" and tot_score > 0.0:
                tot_score = min(tot_score + 0.02, 1.0)

            tot_score = round(min(max(tot_score, 0.0), 1.0), 4)
            cat_label = cls._determine_category(tot_score)

            case_km_val = getattr(case, "odometer_km", None)
            km_diff_val = (
                abs(int(req.odometer_km) - int(case_km_val))
                if (req.odometer_km is not None and case_km_val is not None)
                else None
            )
            year_diff_val = (
                abs(int(req.year) - int(case.year))
                if (req.year is not None and case.year is not None)
                else None
            )

            case_codes_set = set(split_dtc_codes(case.dtc))
            if req_codes_set and req_codes_set.intersection(case_codes_set):
                exact_historical_dtc_best = max(exact_historical_dtc_best, tot_score)

            c_sys = case.system_category or "Udara"
            if c_sys in system_stats:
                system_stats[c_sys].append((tot_score, case.final_diagnosis, case.case_code))

            if filtered_system and c_sys.lower() != filtered_system.lower():
                continue

            advice = cls.get_repair_manual_guidance(case.final_diagnosis, case.dtc)

            item = WeightedCaseMatchItem(
                rank=1,
                case_code=case.case_code,
                brand=case.brand,
                model=case.model,
                year=case.year,
                engine_capacity=case.engine_capacity,
                engine_code=getattr(case, "engine_code", None),
                odometer_km=case_km_val,
                km_diff=km_diff_val,
                year_diff=year_diff_val,
                license_plate=getattr(case, "license_plate", None),
                mechanic_name=getattr(case, "mechanic_name", None),
                verification_status=ver_status,
                complaint=case.complaint,
                symptom=case.symptom,
                dtc=case.dtc or "Tidak ada",
                final_diagnosis=case.final_diagnosis,
                repair_action=case.repair_action,
                system_category=case.system_category,
                group_category=case.group_category,
                text_score=round(t_score * 100, 1),
                live_score=round(l_score * 100, 1) if l_score is not None else None,
                total_score=round(tot_score * 100, 1),
                category_label=cat_label,
                inspection_findings=case.inspection_findings,
                manual_advice=advice,
            )
            scored_items.append(item)

        # 2. Suntikkan kandidat resmi langsung dari BUKU MANUAL PERBAIKAN (OEM Pack Terpilih / Katalog JB420)
        custom_pinout_verified = False
        if manual_dtc_entries:
            primary_dtc = manual_dtc_entries[0]
            p_code_up = primary_dtc["code"].upper()
            eff_eng_code = (app_info.engine_code or req.engine_code or "").strip()
            is_ertiga_diesel = (
                custom_pack is not None
                and str(custom_pack.get("pack_id", "")).lower() == "suzuki_ertiga_gen1_2012_2017"
                and (vehicle_fuel == "Diesel" or "d13a" in eff_eng_code.lower())
            )
            custom_entry_used = (
                custom_pack is not None
                and p_code_up in custom_dtc_map
                and primary_dtc.get("system") == str(custom_pack.get("title", "Buku Manual Kustom"))
            )
            if custom_entry_used:
                cd_entry = custom_dtc_map[p_code_up]
                def _clean_pdf_str(raw_s: str) -> str:
                    s = str(raw_s or "")
                    s = re.sub(r"\)\s*\(Page\s+[^)]+\)", "", s, flags=re.IGNORECASE)
                    s = s.replace("an d ", "and ").replace("O FF", "OFF").replace("di sconnect", "disconnect").replace("re lay", "relay")
                    return re.sub(r"\s{2,}", " ", s).strip()

                manual_advice = cls._build_advice_from_manual_dtc_entries(
                    manual_dtc_entries, wiring_rows, sensor_rows
                )
                pack_title = str(custom_pack.get("title", "Buku Manual Kustom"))
                manual_advice.active_pack_id = app_info.active_pack_id
                manual_advice.manual_book_section = f"{pack_title} — Kode {p_code_up}"
                if cd_entry.get("description_id"):
                    manual_advice.diagnosis_title = f"DTC {p_code_up}: {_clean_pdf_str(cd_entry['description_id'])}"

                # Bersihkan sisa nomor pin JB420 (C37/E23) yang terbawa dari template spesialis umum agar tidak bercampur dengan pinout manual aktif
                cleaned_causes: list[dict[str, str]] = []
                for ci in manual_advice.cause_items:
                    cic = dict(ci)
                    for k_fld in ("title", "desc", "detail"):
                        if k_fld in cic and isinstance(cic[k_fld], str):
                            cic[k_fld] = _clean_pdf_str(strip_unverified_jb420_pins_from_text(cic[k_fld]))
                    cleaned_causes.append(cic)
                manual_advice.cause_items = cleaned_causes

                cleaned_opts: list[dict[str, str]] = []
                for opt in manual_advice.repair_options:
                    oc = dict(opt)
                    for k_fld in ("title", "desc", "why", "verify"):
                        if k_fld in oc and isinstance(oc[k_fld], str):
                            oc[k_fld] = _clean_pdf_str(strip_unverified_jb420_pins_from_text(oc[k_fld]))
                    cleaned_opts.append(oc)
                manual_advice.repair_options = cleaned_opts
                manual_advice.step_by_step_repair = [
                    _clean_pdf_str(strip_unverified_jb420_pins_from_text(st))
                    for st in manual_advice.step_by_step_repair
                    if str(st).strip()
                ]
                page_no = cd_entry.get("page")
                if page_no and not any(f"Hal. PDF {page_no}" in st or f"Hal. {page_no}" in st for st in manual_advice.step_by_step_repair):
                    manual_advice.step_by_step_repair.append(
                        f"Referensi Resmi {custom_pack.get('brand', '')} {custom_pack.get('model', '')}: Lihat detail diagram pada Hal. PDF {page_no} ({pack_title})."
                    )

                # Pilih pinout ASLI sesuai kode mesin & bahan bakar!
                if is_ertiga_diesel:
                    # Tabel pinout C01/E01 di pack Ertiga hanya untuk bensin K14B; JANGAN pakai untuk Diesel D13A!
                    manual_advice.wiring_pinout = [{
                        "pin": "Konektor ECM Diesel D13A DDiS",
                        "signal": f"Sirkuit {p_code_up} (Varian Diesel D13A)",
                        "function": "Pinout tabel C01/E01 yang tersimpan khusus mesin bensin K14B — verifikasi pin soket ECM Diesel D13A secara fisik dengan multitester atau lihat Bab 1A Diesel Hal. PDF 220+.",
                    }]
                    custom_pinout_verified = False
                else:
                    eng_norm = re.sub(r"[^a-z0-9]", "", eff_eng_code.lower())
                    pack_id_cur = str(custom_pack.get("pack_id", "")).lower()
                    raw_dtc_pins = cls._clean_and_dedupe_pack_pins(
                        list(cd_entry.get("wiring_pinout") or []),
                        pack_id=pack_id_cur,
                        year=req.year,
                        model_hint=req.model or "",
                    )
                    if eng_norm and len(eng_norm) >= 3 and raw_dtc_pins:
                        eng_filtered_pins = [
                            pw for pw in raw_dtc_pins
                            if eng_norm in re.sub(r"[^a-z0-9]", "", str(pw.get("pin", "")).lower())
                        ]
                        if eng_filtered_pins:
                            raw_dtc_pins = eng_filtered_pins
                        elif any("[" in str(pw.get("pin", "")) for pw in raw_dtc_pins):
                            # Pin DTC ini milik varian mesin lain (mis. [3ZR-FE] saat pengguna memilih 2AZ-FE)!
                            # Cari pinout asli untuk mesin yang diminta; bila tidak ada, KOSONGKAN (jangan bocor lintas mesin!)
                            raw_dtc_pins = cls._select_custom_pack_pins(
                                custom_pack, eff_eng_code, vehicle_fuel,
                                f"{manual_advice.diagnosis_title} {req.complaint or ''}", [p_code_up],
                                year=req.year, model_hint=req.model or "",
                            )
                    if raw_dtc_pins:
                        manual_advice.wiring_pinout = [
                            {
                                "pin": str(pw.get("pin", "-")),
                                "signal": str(pw.get("signal", "-")),
                                "function": str(pw.get("function", "-")),
                            }
                            for pw in raw_dtc_pins[:6]
                        ]
                        custom_pinout_verified = True
                    else:
                        smart_pins = cls._select_custom_pack_pins(
                            custom_pack, eff_eng_code, vehicle_fuel,
                            f"{manual_advice.diagnosis_title} {req.complaint or ''}", [p_code_up],
                            year=req.year, model_hint=req.model or "",
                        )
                        if smart_pins:
                            manual_advice.wiring_pinout = smart_pins
                            custom_pinout_verified = True
                        else:
                            manual_advice.wiring_pinout = [{
                                "pin": f"Konektor {p_code_up} ({custom_pack.get('brand', '')} {custom_pack.get('model', '')})",
                                "signal": "Belum ada tabel pinout khusus kode/mesin ini",
                                "function": "Diagnosa & langkah dari buku manual resmi, namun pinout konektor spesifik kode/mesin ini wajib dicek fisik dengan multitester.",
                            }]
                            custom_pinout_verified = False

                if cd_entry.get("standard_specs"):
                    manual_advice.sensor_standards = [
                        {
                            "parameter": str(sp.get("parameter", "-")),
                            "normal_range": str(sp.get("normal_range", "-")),
                            "unit": str(sp.get("unit", "-")),
                        }
                        for sp in cd_entry["standard_specs"][:6]
                    ]
                if cd_entry.get("repair_options"):
                    manual_advice.repair_options = list(cd_entry["repair_options"])
                if cd_entry.get("cause_items"):
                    manual_advice.cause_items = list(cd_entry["cause_items"])
            elif p_code_up in modern_dtc_entries_map:
                mh = modern_dtc_entries_map[p_code_up]
                raw_causes = [c.strip() for c in str(mh["root_causes"]).split(";") if c.strip()]
                cause_items = [
                    {
                        "category": "Prioritas Utama" if i == 0 else ("Kemungkinan Tinggi" if i == 1 else "Cek Pendukung"),
                        "detail": c_txt,
                    }
                    for i, c_txt in enumerate(raw_causes[:6])
                ]
                m_sys_cat = str(mh.get("system_category", "Kelistrikan"))
                grp_map = {
                    "Bahan Bakar": "Engine & Fuel",
                    "Udara": "Engine & Induction",
                    "Pengapian": "Engine & Ignition",
                    "Mekanis": "Engine & Drivetrain",
                    "Pendingin": "Thermal & Cooling",
                    "Emisi": "Exhaust & Emission",
                    "Kelistrikan": "Electrical & Network",
                }
                pinout_placeholder = (
                    [
                        {
                            "pin": "Konektor HV / BMS (Wajib APD 1000V)",
                            "signal": "Baterai HV / Inverter / CAN Bus",
                            "function": "Cek dengan Scanner BMS & Insulation Tester 500V (Jangan tusuk kabel oranye!)",
                        }
                    ]
                    if mh.get("requires_hv_safety") or vehicle_fuel == "EV"
                    else [
                        {
                            "pin": f"Soket Komponen {p_code_up} ({app_info.resolved_generation_label})",
                            "signal": f"Sirkuit {m_sys_cat} ({vehicle_fuel})",
                            "function": "Manual pinout spesifik model ini belum diunggah — verifikasi tegangan suplai (+5V/+12V) & massa langsung pada soket fisik dengan multitester.",
                        }
                    ]
                )
                manual_advice = ManualRepairAdvice(
                    diagnosis_title=str(mh["title_id"]),
                    system_category=m_sys_cat,
                    group_category=grp_map.get(m_sys_cat, "Powertrain & Control"),
                    manual_book_section=f"Katalog Universal {vehicle_fuel} / Modern OBD-II — Kode {p_code_up}",
                    cause_summary=str(mh["root_causes"]),
                    cause_items=cause_items,
                    repair_options=list(mh.get("repair_options", [])),
                    step_by_step_repair=list(mh.get("repair_steps", [])),
                    sensor_standards=list(mh.get("standard_specs", [])),
                    wiring_pinout=pinout_placeholder,
                    relearn_reset_steps=[
                        f"1. Hapus memori DTC {p_code_up} dengan scan tool (kunci ON mesin mati).",
                        "2. Lakukan kalibrasi/learning sesuai kebutuhan sistem (SCV/Injektor learning Diesel, adaptasi VVT/throttle, atau reset BMS) lalu uji jalan.",
                    ],
                    is_pinout_verified=False,
                    hv_safety_warning=app_info.hv_safety_warning if (mh.get("requires_hv_safety") or app_info.is_high_voltage) else None,
                )
            else:
                manual_advice = cls._build_advice_from_manual_dtc_entries(
                    manual_dtc_entries, wiring_rows, sensor_rows
                )

            all_codes_str = ", ".join(d["code"] for d in manual_dtc_entries)
            m_sys, m_grp = cls._classify_dtc_workshop_system(
                primary_dtc["code"], primary_dtc["system"], primary_dtc["description_id"]
            )
            if manual_advice.system_category in system_stats:
                m_sys = manual_advice.system_category
                m_grp = manual_advice.group_category

            # Jika kode DTC diketik eksplisit & belum ada kasus historis identik yang lebih tinggi, jadikan Referensi Manual #1 (94.0%)
            if req_codes:
                manual_score = 0.94 if exact_historical_dtc_best < 0.88 else 0.88
            else:
                manual_score = 0.84

            manual_case_code = f"MANUAL-{primary_dtc['code']}"
            manual_diag_label = (
                f"{primary_dtc['description_id']} (DTC {all_codes_str})"
                if len(manual_dtc_entries) == 1
                else f"Multi-DTC Manual Resmi: " + "; ".join(f"{d['code']} {d['description_id']}" for d in manual_dtc_entries)
            )
            if manual_advice.repair_options:
                manual_repair_short = " / ".join(opt["title"] for opt in manual_advice.repair_options[:2])
            elif manual_advice.step_by_step_repair:
                manual_repair_short = manual_advice.step_by_step_repair[0].lstrip("0123456789. ")
            else:
                manual_repair_short = f"Periksa sirkuit & konektor sesuai {primary_dtc['system']}"

            if m_sys in system_stats:
                system_stats[m_sys].append((manual_score, manual_diag_label, manual_case_code))

            # Apabila pengguna eksplisit mengetik kode DTC (misal P0480), selalu tampilkan hasil Buku Manual meski filter sistem lama terpasang
            if not filtered_system or filtered_system.lower() == m_sys.lower() or bool(req_codes):
                scored_items.append(
                    WeightedCaseMatchItem(
                        rank=1,
                        case_code=manual_case_code,
                        brand=req.brand.strip().title() if req.brand.strip() else "Suzuki / OBD-II",
                        model=req.model.strip().title() if req.model.strip() else "Manual Book JB420",
                        year=req.year,
                        engine_capacity=req.engine_code.strip() or None,
                        complaint=req.complaint.strip() or f"Indikator MIL / DTC {all_codes_str}",
                        symptom=req.symptom.strip() or primary_dtc["description_id"],
                        dtc=all_codes_str,
                        final_diagnosis=manual_diag_label,
                        repair_action=manual_repair_short,
                        system_category=m_sys,
                        group_category=m_grp,
                        text_score=round(manual_score * 100, 1),
                        live_score=None,
                        total_score=round(manual_score * 100, 1),
                        category_label=cls._determine_category(manual_score),
                        inspection_findings=primary_dtc["possible_causes"],
                        manual_advice=manual_advice,
                    )
                )

        # Urutkan berdasarkan Skor Total tertinggi
        scored_items.sort(key=lambda x: x.total_score, reverse=True)
        for idx, itm in enumerate(scored_items, start=1):
            itm.rank = idx

        # Susun Ringkasan Per Sistem (Tabel J3:M12 pada Excel)
        summaries: list[SystemScoreSummary] = []
        for s_def in cls.SYSTEM_DEFINITIONS:
            s_name = s_def["name"]
            c_list = system_stats.get(s_name, [])
            c_count = len(c_list)
            if c_list:
                c_list.sort(key=lambda x: x[0], reverse=True)
                top_s, top_diag, top_code = c_list[0]
                summaries.append(
                    SystemScoreSummary(
                        system_name=s_name,
                        group_name=s_def["group"],
                        parameters_checked=s_def["params"],
                        cases_count=c_count,
                        top_score=round(top_s * 100, 1),
                        category_label=cls._determine_category(top_s),
                        top_diagnosis=top_diag,
                        top_case_code=top_code,
                    )
                )
            else:
                summaries.append(
                    SystemScoreSummary(
                        system_name=s_name,
                        group_name=s_def["group"],
                        parameters_checked=s_def["params"],
                        cases_count=0,
                        top_score=0.0,
                        category_label="Belum ada kasus di database",
                        top_diagnosis="-",
                        top_case_code="-",
                    )
                )

        # Top Match + Confidence Cutoff (< 25% tanpa kecocokan DTC -> Panduan Pemeriksaan Awal Aman, anti-salah vonis!)
        top_match = scored_items[0] if scored_items else None
        is_low_conf = (not manual_dtc_entries) and (top_match is None or top_match.total_score < 25.0)

        if is_low_conf:
            safe = build_low_confidence_safe_advice(
                fuel_type=vehicle_fuel,
                vehicle_label=app_info.resolved_generation_label,
                dtc_raw=", ".join(req_codes) or req.dtc.strip(),
                hv_safety_warning=app_info.hv_safety_warning,
            )
            top_case_code_out = "BELUM-TERPETAKAN"
            top_diag_out = safe["title"]
            top_score_out = top_match.total_score if top_match else 0.0
            top_cat_out = "PERLU PEMERIKSAAN AWAL"
            top_headline = (
                f"{top_diag_out} — Kecocokan historis rendah ({top_score_out}%), "
                f"gunakan panduan cek awal aman untuk mesin {vehicle_fuel}."
            )
            direct_advice = ManualRepairAdvice(
                diagnosis_title=safe["title"],
                system_category="Kelistrikan" if vehicle_fuel == "EV" else ("Bahan Bakar" if vehicle_fuel == "Diesel" else "Umum"),
                group_category=f"Pemeriksaan Awal ({vehicle_fuel})",
                manual_book_section=f"Mode Pemeriksaan Awal Aman — {app_info.resolved_generation_label}",
                cause_summary=safe["root_cause_summary"],
                cause_items=[
                    {"category": "Status Database", "detail": safe["root_cause_summary"]},
                    {"category": "Tindakan Disarankan", "detail": safe["proven_repair_action"]},
                ],
                repair_options=safe["repair_options"],
                step_by_step_repair=safe["repair_steps"],
                sensor_standards=safe["standard_specs"],
                wiring_pinout=[
                    {
                        "pin": "Soket Fisik Komponen Terkait",
                        "signal": f"Pengukuran Aman ({vehicle_fuel})",
                        "function": "Belum ada manual OEM model ini — verifikasi suplai daya & massa langsung dengan multitester.",
                    }
                ],
                relearn_reset_steps=[
                    "1. Setelah menemukan sumber kerusakan & memperbaiki, hapus kode DTC lalu uji jalan.",
                    "2. Klik tombol 'Simpan Kasus' agar kasus baru ini langsung masuk ke database kecerdasan bengkel.",
                ],
                is_pinout_verified=False,
                safety_warning=app_info.safety_warning_desc,
                hv_safety_warning=app_info.hv_safety_warning,
                is_low_confidence_fallback=True,
                adaptive_live_findings=adaptive_live_findings,
            )
        else:
            top_case_code_out = top_match.case_code if top_match else "-"
            top_diag_out = top_match.final_diagnosis if top_match else "-"
            top_score_out = top_match.total_score if top_match else 0.0
            top_cat_out = top_match.category_label if top_match else "Kurang mirip"
            top_headline = (
                f"{top_match.final_diagnosis} — {top_match.total_score}% ({top_match.category_label}), referensi {top_match.case_code}, sistem {top_match.system_category}"
                if top_match
                else "Tidak ada kasus yang cocok"
            )
            direct_advice = (
                top_match.manual_advice
                if top_match and top_match.manual_advice
                else cls.get_repair_manual_guidance("Umum", None)
            )
            direct_advice = direct_advice.model_copy(deep=True)
            direct_advice.adaptive_live_findings = adaptive_live_findings
            if app_info.is_high_voltage and not direct_advice.hv_safety_warning:
                direct_advice.hv_safety_warning = app_info.hv_safety_warning

        # 3. Terapkan Guardrail Keamanan Wiring jika model+tahun belum memiliki pinout asli yang terverifikasi
        direct_advice.active_pack_id = app_info.active_pack_id
        if not is_low_conf:
            eff_eng_code = (app_info.engine_code or req.engine_code or "").strip()
            has_verified_pinout = False

            if app_info.active_pack_id == "suzuki_jb420_builtin":
                has_verified_pinout = True
            elif custom_pack:
                if custom_pinout_verified:
                    has_verified_pinout = True
                else:
                    # DTC tidak ada di custom_dtc_map (mis. Innova/Fortuner/Yaris + P0300) atau diagnosa tanpa DTC (K005):
                    # Cari pinout ASLI dari custom_pack["wiring_pinouts"] sesuai kode mesin & komponen!
                    smart_pins = cls._select_custom_pack_pins(
                        custom_pack,
                        eff_eng_code,
                        vehicle_fuel,
                        f"{direct_advice.diagnosis_title} {req.complaint or ''} {req.symptom or ''}",
                        req_codes,
                        year=req.year,
                        model_hint=req.model or "",
                    )
                    if smart_pins:
                        direct_advice.wiring_pinout = smart_pins
                        has_verified_pinout = True
                        direct_advice.manual_book_section = f"{app_info.active_manual_source} (Pinout Resmi {eff_eng_code or custom_pack.get('model', '')})"
                    else:
                        has_verified_pinout = False

                # Bersihkan selalu referensi pin JB420 (C37/E23) dari teks langkah & opsi pada paket manual non-JB420!
                direct_advice.step_by_step_repair = [
                    strip_unverified_jb420_pins_from_text(st) for st in direct_advice.step_by_step_repair
                ]
                cleaned_c_opts: list[dict[str, str]] = []
                for opt in direct_advice.repair_options:
                    oc = dict(opt)
                    for k_fld in ("title", "desc", "why", "verify"):
                        if k_fld in oc and isinstance(oc[k_fld], str):
                            oc[k_fld] = strip_unverified_jb420_pins_from_text(oc[k_fld])
                    cleaned_c_opts.append(oc)
                direct_advice.repair_options = cleaned_c_opts

            if has_verified_pinout:
                direct_advice.is_pinout_verified = True
                direct_advice.safety_warning = app_info.safety_warning_desc
                if custom_pack and "Pinout Resmi" not in direct_advice.manual_book_section and str(custom_pack.get("title", "")) not in direct_advice.manual_book_section:
                    direct_advice.manual_book_section = f"{app_info.active_manual_source}"
            else:
                direct_advice.is_pinout_verified = False
                if custom_pack:
                    direct_advice.safety_warning = (
                        f"Paket manual {custom_pack.get('brand', '')} {custom_pack.get('model', '')} terpasang, "
                        f"namun tabel pinout khusus varian/kode ini ({eff_eng_code or vehicle_fuel}) belum tersedia — "
                        "diagram & pin di bawah bersifat ilustrasi umum (Ref. JB420), WAJIB ukur fisik dengan multitester."
                    )
                else:
                    direct_advice.safety_warning = app_info.safety_warning_desc
                if (req.brand.strip() or req.model.strip()) and "Katalog Universal" not in direct_advice.manual_book_section and not custom_pack:
                    direct_advice.manual_book_section = (
                        f"Mode Universal OBD-II ({app_info.resolved_generation_label}) — "
                        "File Manual Spesifik Model Ini Belum Diunggah"
                    )
                # Bersihkan kode pin E23/C37 JB420 dari teks opsi & langkah perbaikan agar tidak menyesatkan mekanik!
                cleaned_opts: list[dict[str, str]] = []
                for opt in direct_advice.repair_options:
                    oc = dict(opt)
                    for k_fld in ("title", "desc", "why", "verify"):
                        if k_fld in oc and isinstance(oc[k_fld], str):
                            oc[k_fld] = strip_unverified_jb420_pins_from_text(oc[k_fld])
                    cleaned_opts.append(oc)
                direct_advice.repair_options = cleaned_opts
                direct_advice.step_by_step_repair = [
                    strip_unverified_jb420_pins_from_text(st) for st in direct_advice.step_by_step_repair
                ]
                tagged_pinouts: list[dict[str, str]] = []
                if vehicle_fuel == "Diesel":
                    # GUARDRAIL KETAT DIESEL: jangan pernah bocorkan pinout Bensin (C37 A/F, O2, Koil Pengapian) ke mesin Diesel!
                    petrol_leak = any(
                        re.search(r"\b(c37-|e23-|a/f|ho2s|koil|coil|igt|igf)\b", f"{wp.get('pin','')} {wp.get('signal','')}", re.I)
                        for wp in direct_advice.wiring_pinout
                    )
                    if petrol_leak or not direct_advice.wiring_pinout:
                        tagged_pinouts = [{
                            "pin": f"Konektor Diesel ({eff_eng_code or app_info.resolved_generation_label})",
                            "signal": f"Sirkuit Mesin Diesel ({', '.join(req_codes) or 'Verifikasi Fisik'})",
                            "function": "Pinout Bensin (Koil/Sensor O2 Bensin) diblokir untuk keamanan mesin Diesel — cek jalur sensor/injektor Common-Rail langsung dengan multitester.",
                        }]
                    else:
                        tagged_pinouts = list(direct_advice.wiring_pinout)
                else:
                    for wp in direct_advice.wiring_pinout:
                        wp_copy = dict(wp)
                        func_str = str(wp_copy.get("function", ""))
                        pin_str = str(wp_copy.get("pin", ""))
                        if "[Contoh Ref" not in func_str and "Cek dengan Scanner" not in func_str and "Manual pinout spesifik" not in func_str and "verifikasi pin soket" not in func_str.lower():
                            if re.search(r"\b[ECGB]\d{2}-\d{1,2}\b", pin_str) or "IG-FUSE" in pin_str or "IG-COIL" in pin_str or "MAIN-RLY" in pin_str or "Terminal ECM" in pin_str:
                                wp_copy["function"] = f"[Contoh Ref. JB420 — Cek Soket Fisik] {func_str}"
                        tagged_pinouts.append(wp_copy)
                direct_advice.wiring_pinout = tagged_pinouts

        # 4. Pastikan SELALU tersedia 3 tingkatan standar pengukuran (Statis IG ON/OFF, Saat Mesin Idle, & Nilai Scanner OBD-II)
        cat_map_final = cls._get_jb420_dtc_catalog_map()
        matched_cat_final = None
        for rc in req_codes:
            if rc.upper() in cat_map_final:
                matched_cat_final = cat_map_final[rc.upper()]
                break
        if matched_cat_final:
            if not direct_advice.idle_standards and matched_cat_final.get("idle_standards"):
                direct_advice.idle_standards = [dict(x) for x in matched_cat_final["idle_standards"]]
            if not direct_advice.scanner_standards and matched_cat_final.get("scanner_standards"):
                direct_advice.scanner_standards = [dict(x) for x in matched_cat_final["scanner_standards"]]
            if not direct_advice.sim_circuit_key and matched_cat_final.get("sim_circuit_key"):
                direct_advice.sim_circuit_key = str(matched_cat_final["sim_circuit_key"])
            if not direct_advice.atlas_module_id and matched_cat_final.get("atlas_module_id"):
                direct_advice.atlas_module_id = str(matched_cat_final["atlas_module_id"])
            if app_info.active_pack_id == "suzuki_jb420_builtin":
                if not direct_advice.wiring_ref_id and matched_cat_final.get("wiring_ref_id"):
                    direct_advice.wiring_ref_id = str(matched_cat_final["wiring_ref_id"])
                if not direct_advice.oem_wiring_image and matched_cat_final.get("oem_wiring_image"):
                    direct_advice.oem_wiring_image = str(matched_cat_final["oem_wiring_image"])
                if not direct_advice.shared_with_dtcs and matched_cat_final.get("shared_with_dtcs"):
                    direct_advice.shared_with_dtcs = [str(x) for x in matched_cat_final["shared_with_dtcs"]]
                if not direct_advice.wiring_cross_ref_note and matched_cat_final.get("wiring_cross_ref_note"):
                    direct_advice.wiring_cross_ref_note = str(matched_cat_final["wiring_cross_ref_note"])
                if not direct_advice.atlas_photo_index and matched_cat_final.get("atlas_photo_index"):
                    direct_advice.atlas_photo_index = int(matched_cat_final["atlas_photo_index"])
                if not direct_advice.manual_page_ref and matched_cat_final.get("manual_page_ref"):
                    direct_advice.manual_page_ref = str(matched_cat_final["manual_page_ref"])
                if matched_cat_final.get("connector"):
                    direct_advice.connector = dict(matched_cat_final["connector"])
                if matched_cat_final.get("wiring_pinout"):
                    direct_advice.wiring_pinout = [
                        {
                            "pin": str(p.get("pin", "-")),
                            "signal": str(p.get("signal", "-")),
                            "function": str(p.get("function", "-")),
                        }
                        for p in matched_cat_final["wiring_pinout"]
                    ]
                direct_advice.verification_status = str(matched_cat_final.get("verification_status") or "VERIFIED_OEM")

        if not direct_advice.idle_standards:
            if vehicle_fuel == "EV":
                direct_advice.idle_standards = [
                    {"parameter": "Tegangan Aki 12V Aux Saat Mode READY (DC-DC Aktif)", "normal_range": "13.6 – 14.5 V", "unit": "V DC"},
                    {"parameter": "Tahanan Isolasi Sistem HV (Insulation Tester 500V)", "normal_range": "> 10 MΩ (Wajib APD 1000V)", "unit": "MΩ"},
                ]
            elif vehicle_fuel == "Diesel":
                direct_advice.idle_standards = [
                    {"parameter": "Tekanan Common-Rail Bahan Bakar Saat Idle Panas", "normal_range": "30 – 45 MPa (300 – 450 bar)", "unit": "MPa"},
                    {"parameter": "Putaran Mesin Idle Panas & Pengisian Alternator", "normal_range": "700 – 800 RPM · 13.5 – 14.5 V", "unit": "RPM / V"},
                ]
            else:
                direct_advice.idle_standards = [
                    {"parameter": "Putaran Mesin Idle Tanpa Beban (Panas Kerja 80–90°C)", "normal_range": "650 – 750 ± 50 RPM", "unit": "RPM"},
                    {"parameter": "Tegangan Pengisian Alternator Saat Idle", "normal_range": "13.5 – 14.5 V (Stabil)", "unit": "V DC"},
                    {"parameter": "Vakum Intake Manifold / Tegangan Sensor MAP Saat Idle", "normal_range": "24 – 38 kPa (~1.1 – 1.5 V)", "unit": "kPa / V"},
                ]

        if not direct_advice.scanner_standards:
            if vehicle_fuel == "EV":
                direct_advice.scanner_standards = [
                    {"parameter": "HV BATTERY CELL VOLTAGE DELTA (Live Data BMS)", "normal_range": "< 50 mV antar sel", "unit": "mV"},
                    {"parameter": "HV BATTERY SOC / SOH & SUHU PACK", "normal_range": "20 – 100% · 20 – 45 °C", "unit": "% / °C"},
                ]
            elif vehicle_fuel == "Diesel":
                direct_advice.scanner_standards = [
                    {"parameter": "FUEL RAIL PRESSURE ACTUAL vs TARGET (Idle)", "normal_range": "30 – 45 MPa (Selisih < ±3 MPa)", "unit": "MPa"},
                    {"parameter": "INJECTOR FEEDBACK / CORRECTION VOLUME", "normal_range": "–2.5 s/d +2.5 mm³/st", "unit": "mm³/st"},
                ]
            else:
                direct_advice.scanner_standards = [
                    {"parameter": "COOLANT TEMP (ECT · Bab 1A-34 Idle Panas)", "normal_range": "80 – 100 °C", "unit": "°C"},
                    {"parameter": "SHORT FT B1 (STFT) & LONG FT B1 (LTFT · Bab 1A-35)", "normal_range": "–10% s/d +10% (Ambang ±20%)", "unit": "%"},
                    {"parameter": "MAF & MAP Saat Idle Panas (Bab 1A-34/35)", "normal_range": "1.0 – 4.0 g/s · 24 – 38 kPa", "unit": "g/s · kPa"},
                ]

        if not direct_advice.customer_summary:
            direct_advice.customer_summary = cls._build_customer_summary(
                direct_advice, app_info, req_codes
            )

        return WeightedCaseSearchResponse(
            top_headline=top_headline,
            top_case_code=top_case_code_out,
            top_diagnosis=top_diag_out,
            top_score_percent=top_score_out,
            top_category_label=top_cat_out,
            system_filter_applied=filtered_system,
            ranked_matches=scored_items[:20],
            system_summaries=summaries,
            direct_manual_advice=direct_advice,
            vehicle_applicability=app_info,
        )
