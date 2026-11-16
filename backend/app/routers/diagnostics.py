"""
Smart Fault Diagnostics router — CRUD + diagnostic engine endpoint.
"""

import json
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.models.diagnostic import (
    FaultCategory, FaultHistory, FaultCheckpoint, SymptomCheckpointLink,
)
from app.schemas.diagnostic import (
    FaultCategoryCreate, FaultCategoryResponse,
    FaultHistoryCreate, FaultHistoryResponse, FaultHistoryUpdate,
    FaultCheckpointCreate, FaultCheckpointResponse,
    SymptomCheckpointLinkCreate, SymptomCheckpointLinkResponse,
)
from app.utils.deps import get_current_user

router = APIRouter(prefix="/diagnostics", tags=["Diagnostics"])


# ── Fault Categories ─────────────────────────────────────────────────────────

@router.get("/categories", response_model=list[FaultCategoryResponse])
async def list_fault_categories(
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List all fault categories."""
    result = await db.execute(select(FaultCategory).order_by(FaultCategory.name))
    return result.scalars().all()


@router.post("/categories", response_model=FaultCategoryResponse, status_code=201)
async def create_fault_category(
    data: FaultCategoryCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Create a new fault category."""
    cat = FaultCategory(**data.model_dump())
    db.add(cat)
    await db.flush()
    await db.refresh(cat)
    return cat


# ── Fault Checkpoints ────────────────────────────────────────────────────────

@router.get("/checkpoints", response_model=list[FaultCheckpointResponse])
async def list_checkpoints(
    category_id: int | None = Query(None),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List diagnostic checkpoints, optionally filtered by category."""
    stmt = select(FaultCheckpoint).order_by(FaultCheckpoint.order_priority)
    if category_id:
        stmt = stmt.where(FaultCheckpoint.category_id == category_id)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/checkpoints", response_model=FaultCheckpointResponse, status_code=201)
async def create_checkpoint(
    data: FaultCheckpointCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Create a new diagnostic checkpoint."""
    cp = FaultCheckpoint(**data.model_dump())
    db.add(cp)
    await db.flush()
    await db.refresh(cp)
    return cp


# ── Fault History CRUD ───────────────────────────────────────────────────────

@router.get("/history", response_model=list[FaultHistoryResponse])
async def list_fault_history(
    vehicle_id: int | None = Query(None),
    category_id: int | None = Query(None),
    limit: int = Query(50, le=200),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List fault history records with optional filters."""
    stmt = select(FaultHistory).order_by(FaultHistory.created_at.desc()).limit(limit)
    if vehicle_id:
        stmt = stmt.where(FaultHistory.vehicle_id == vehicle_id)
    if category_id:
        stmt = stmt.where(FaultHistory.category_id == category_id)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.post("/history", response_model=FaultHistoryResponse, status_code=201)
async def create_fault_history(
    data: FaultHistoryCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Record a new fault history entry."""
    fh = FaultHistory(**data.model_dump())
    db.add(fh)
    await db.flush()
    await db.refresh(fh)
    return fh


@router.put("/history/{history_id}", response_model=FaultHistoryResponse)
async def update_fault_history(
    history_id: int,
    data: FaultHistoryUpdate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Update a fault history entry."""
    result = await db.execute(select(FaultHistory).where(FaultHistory.id == history_id))
    fh = result.scalar_one_or_none()
    if not fh:
        raise HTTPException(status_code=404, detail="Riwayat kerusakan tidak ditemukan")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(fh, field, value)
    await db.flush()
    await db.refresh(fh)
    return fh


# ── Symptom-Checkpoint Links ────────────────────────────────────────────────

@router.post("/links", response_model=SymptomCheckpointLinkResponse, status_code=201)
async def create_symptom_link(
    data: SymptomCheckpointLinkCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Link a checkpoint to a fault history record."""
    link = SymptomCheckpointLink(**data.model_dump())
    db.add(link)
    await db.flush()
    await db.refresh(link)
    return link


# ══════════════════════════════════════════════════════════════════════════════
# 🧠 SMART DIAGNOSTIC ENGINE — The core intelligence endpoint
# ══════════════════════════════════════════════════════════════════════════════

@router.post("/diagnose")
async def diagnose_fault(
    symptoms: str = Query(..., description="Gejala kerusakan yang dilaporkan"),
    category_id: int = Query(..., description="Kategori kerusakan"),
    brand: str | None = Query(None, description="Merk kendaraan (opsional)"),
    model: str | None = Query(None, description="Model kendaraan (opsional)"),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """
    🧠 SMART FAULT DIAGNOSTIC ENGINE

    Analisa gejala kerusakan baru berdasarkan riwayat historis:
    1. Cari riwayat kerusakan dengan gejala mirip di kategori yang sama
    2. Hitung frekuensi setiap checkpoint yang menjadi penyebab (was_cause=True)
    3. Urutkan checkpoint berdasarkan probabilitas tertinggi
    4. Return ranking rekomendasi pengecekan (0-100%)
    """
    # Ambil semua riwayat kerusakan di kategori ini
    stmt = select(FaultHistory).where(FaultHistory.category_id == category_id)
    result = await db.execute(stmt)
    histories = result.scalars().all()

    if not histories:
        # Fallback: kembalikan semua checkpoint di kategori ini dengan prioritas default
        cp_result = await db.execute(
            select(FaultCheckpoint)
            .where(FaultCheckpoint.category_id == category_id)
            .order_by(FaultCheckpoint.order_priority)
        )
        checkpoints = cp_result.scalars().all()
        return {
            "status": "no_history",
            "message": "Belum ada riwayat kerusakan di kategori ini. Menggunakan urutan pengecekan default.",
            "input_symptoms": symptoms,
            "recommendations": [
                {
                    "checkpoint_id": cp.id,
                    "checkpoint_name": cp.name,
                    "description": cp.description,
                    "probability_percent": 0.0,
                    "based_on_cases": 0,
                    "default_priority": cp.order_priority,
                }
                for cp in checkpoints
            ],
        }

    # Hitung kemiripan gejala dengan text matching sederhana
    # (di versi lanjut bisa pakai embeddings / cosine similarity)
    symptom_keywords = set(symptoms.lower().split())

    scored_histories = []
    for hist in histories:
        hist_keywords = set(hist.reported_symptoms.lower().split())
        # Jaccard similarity
        intersection = symptom_keywords & hist_keywords
        union = symptom_keywords | hist_keywords
        similarity = len(intersection) / len(union) if union else 0.0
        if similarity > 0.05:  # Minimal threshold
            scored_histories.append((hist, similarity))

    # Jika tidak ada yang mirip, fallback ke semua history di kategori
    if not scored_histories:
        scored_histories = [(hist, 1.0 / len(histories)) for hist in histories]

    # Hitung frekuensi checkpoint yang was_cause=True pada riwayat mirip
    checkpoint_scores: dict[int, dict] = {}
    total_weight = sum(sim for _, sim in scored_histories)

    for hist, similarity in scored_histories:
        # Ambil links untuk setiap history
        links_result = await db.execute(
            select(SymptomCheckpointLink).where(
                SymptomCheckpointLink.fault_history_id == hist.id
            )
        )
        links = links_result.scalars().all()

        for link in links:
            if link.checkpoint_id not in checkpoint_scores:
                checkpoint_scores[link.checkpoint_id] = {
                    "weighted_cause_count": 0.0,
                    "weighted_total_count": 0.0,
                    "cause_count": 0,
                    "total_count": 0,
                }

            checkpoint_scores[link.checkpoint_id]["weighted_total_count"] += similarity
            checkpoint_scores[link.checkpoint_id]["total_count"] += 1

            if link.was_cause:
                checkpoint_scores[link.checkpoint_id]["weighted_cause_count"] += similarity
                checkpoint_scores[link.checkpoint_id]["cause_count"] += 1

    # Ambil detail checkpoint dan hitung probabilitas
    recommendations = []
    for cp_id, scores in checkpoint_scores.items():
        cp_result = await db.execute(
            select(FaultCheckpoint).where(FaultCheckpoint.id == cp_id)
        )
        cp = cp_result.scalar_one_or_none()
        if cp:
            probability = (
                (scores["weighted_cause_count"] / total_weight * 100)
                if total_weight > 0
                else 0.0
            )
            recommendations.append({
                "checkpoint_id": cp.id,
                "checkpoint_name": cp.name,
                "description": cp.description,
                "probability_percent": round(min(probability, 100.0), 1),
                "based_on_cases": scores["cause_count"],
                "total_appearances": scores["total_count"],
            })

    # Urutkan berdasarkan probabilitas tertinggi
    recommendations.sort(key=lambda x: x["probability_percent"], reverse=True)

    # Tambahkan checkpoint yang belum muncul di riwayat (dengan 0%)
    all_cp_result = await db.execute(
        select(FaultCheckpoint)
        .where(FaultCheckpoint.category_id == category_id)
        .order_by(FaultCheckpoint.order_priority)
    )
    all_checkpoints = all_cp_result.scalars().all()
    existing_cp_ids = {r["checkpoint_id"] for r in recommendations}

    for cp in all_checkpoints:
        if cp.id not in existing_cp_ids:
            recommendations.append({
                "checkpoint_id": cp.id,
                "checkpoint_name": cp.name,
                "description": cp.description,
                "probability_percent": 0.0,
                "based_on_cases": 0,
                "total_appearances": 0,
            })

    return {
        "status": "analyzed",
        "message": f"Analisis berdasarkan {len(scored_histories)} riwayat kerusakan mirip",
        "input_symptoms": symptoms,
        "matched_histories": len(scored_histories),
        "total_histories_in_category": len(histories),
        "recommendations": recommendations,
    }
