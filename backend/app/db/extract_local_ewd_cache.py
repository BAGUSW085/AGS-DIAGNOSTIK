"""
Extractor & Indexer EWD Lokal Ringan (Toyota GSIC .svgz + connect/*.xml + PDF Avanza & Suzuki)
==============================================================================================
Mengekstrak HANYA file EWD ringan (<120 MB total) dari arsip RAR lokal bengkel ke
`backend/local_ewd_cache/` (diabaikan oleh .gitignore demi keamanan HKI & ukuran repo)
sehingga Viewer Wiring AGOS berjalan instan (<50 ms) tanpa perlu flashdisk tertancap.

Penggunaan:
    python -m app.db.extract_local_ewd_cache --archive-dir "D:\\Repair Manual TOYOTA ZIP FILE"
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

CATEGORY_LABELS = {
    "ENG": "Mesin & Kontrol Injeksi (ENG)",
    "TM": "Transmisi Otomatis / Manual (TM)",
    "DL": "Penggerak 4WD & Gardan (DL)",
    "BRA": "Rem, ABS, TRC & VSC (BRA)",
    "CS": "Jaringan CAN Bus & DLC3 (CS)",
    "SEC": "Immobiliser & Keamanan (SEC)",
    "SRS": "Airbag & Seat Belt (SRS)",
    "HVAC": "Sistem AC & Blower (HVAC)",
    "BE": "Kelistrikan Bodi & Lampu (BE)",
    "BO": "Pintu, Power Window & Spion (BO)",
    "PS": "Sumber Daya & Sekring (PS)",
    "ST": "Power Steering / EPS (ST)",
    "AV": "Audio & Navigasi (AV)",
    "SUS": "Suspensi & Chasis (SUS)",
    "OTHER": "Sistem Kelistrikan Lainnya",
}

TOYOTA_SVGZ_MODELS = [
    {
        "model_id": "toyota_fortuner_2005",
        "brand": "Toyota",
        "label": "Toyota Fortuner / Innova Gen 1 (2005–2011 — 1KD/2KD/2TR/1GR)",
        "archive": "FORTUNER.rar",
        "pack_id": "toyota_fortuner_gen1_2005_2015",
    },
    {
        "model_id": "toyota_fortuner_2012",
        "brand": "Toyota",
        "label": "Toyota Fortuner Facelift (2012–2015 — 2KD-FTV VNT / 1KD / 2TR)",
        "archive": "FORTUNER 2012.rar",
        "pack_id": "toyota_fortuner_gen1_2005_2015",
    },
    {
        "model_id": "toyota_hilux_2012",
        "brand": "Toyota",
        "label": "Toyota Hilux (2012–2015 — 1KD/2KD/2TR)",
        "archive": "HILUX 2012.rar",
        "pack_id": "toyota_hilux_hiace_2005_2015",
    },
    {
        "model_id": "toyota_yaris_gen1",
        "brand": "Toyota",
        "label": "Toyota Yaris Gen 1 (1NZ-FE / 2NZ-FE)",
        "archive": "RM_YARIS.rar",
        "pack_id": "toyota_yaris_vios_1nzfe_2003_2016",
    },
    {
        "model_id": "toyota_vios_gen2",
        "brand": "Toyota",
        "label": "Toyota Vios / Limo (1NZ-FE / 2NZ-FE)",
        "archive": "RM_TOYOTA_VIOS.rar",
        "pack_id": "toyota_yaris_vios_1nzfe_2003_2016",
    },
    {
        "model_id": "toyota_camry_acv40",
        "brand": "Toyota",
        "label": "Toyota Camry (2AZ-FE / 2GR-FE / Hybrid)",
        "archive": "CAMRY.rar",
        "pack_id": "toyota_corolla_camry_alphard_2004_2015",
    },
]


def find_7z_binary() -> str:
    candidates = [
        shutil.which("7z"),
        r"C:\Program Files\7-Zip\7z.exe",
        r"C:\Program Files (x86)\7-Zip\7z.exe",
        r"C:\Program Files (x86)\BlueStacks X\7z.exe",
    ]
    for c in candidates:
        if c and Path(c).exists():
            return str(c)
    raise FileNotFoundError(
        "7z.exe tidak ditemukan. Install 7-Zip atau pastikan 7z.exe ada di PATH."
    )


def extract_patterns(seven_z: str, archive_path: Path, out_dir: Path, patterns: list[str]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [seven_z, "x", "-y", "-r", str(archive_path), f"-o{out_dir}", *patterns]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if res.returncode not in (0, 1):
        raise RuntimeError(f"7z gagal pada {archive_path.name}: {res.stderr[-300:]}")


def parse_title_xml_map(model_dir: Path) -> dict[str, dict]:
    """Scan title.xml files under model_dir and map fig_stem -> {name, sc, term}."""
    info_map: dict[str, dict] = {}
    for txml in model_dir.rglob("title.xml"):
        if "system" not in str(txml).replace("\\", "/").lower():
            continue
        try:
            root = ET.parse(txml).getroot()
        except Exception:
            continue
        for sys_el in root.findall(".//System"):
            sc = (sys_el.attrib.get("sc") or "OTHER").strip().upper()
            name_el = sys_el.find("name")
            fig_el = sys_el.find("fig")
            term_el = sys_el.find("term")
            if fig_el is None or not (fig_el.text or "").strip():
                continue
            fig_code = fig_el.text.strip()
            sys_name = (name_el.text or fig_code).strip() if name_el is not None else fig_code
            term_from = term_el.attrib.get("from", "") if term_el is not None else ""
            # Keep first or richest entry per fig_code
            if fig_code not in info_map:
                info_map[fig_code] = {
                    "name": sys_name,
                    "sc": sc,
                    "category_label": CATEGORY_LABELS.get(sc, CATEGORY_LABELS["OTHER"]),
                    "term_from": term_from,
                }
            elif sys_name not in info_map[fig_code]["name"]:
                info_map[fig_code]["name"] += f" / {sys_name}"
    return info_map


def build_svgz_model_index(model_cfg: dict, model_dir: Path, cache_root: Path) -> dict:
    title_map = parse_title_xml_map(model_dir)
    # Find all system/fig/*.svgz
    fig_files = {}
    for svgz in model_dir.rglob("*.svgz"):
        norm = str(svgz).replace("\\", "/").lower()
        if "/system/fig/" in norm:
            fig_files[svgz.stem] = svgz

    conn_files = {}
    for cxml in model_dir.rglob("*.xml"):
        norm = str(cxml).replace("\\", "/").lower()
        if "/system/connect/" in norm:
            conn_files[cxml.stem] = cxml

    systems = []
    for code in sorted(fig_files.keys()):
        meta = title_map.get(code, {})
        svgz_rel = str(fig_files[code].relative_to(cache_root)).replace("\\", "/")
        conn_rel = (
            str(conn_files[code].relative_to(cache_root)).replace("\\", "/")
            if code in conn_files
            else None
        )
        sc = meta.get("sc", "OTHER")
        systems.append(
            {
                "code": code,
                "name": meta.get("name", code),
                "sc": sc,
                "category_label": meta.get(
                    "category_label", CATEGORY_LABELS.get(sc, CATEGORY_LABELS["OTHER"])
                ),
                "term_from": meta.get("term_from", ""),
                "svgz_path": svgz_rel,
                "connect_xml_path": conn_rel,
                "has_xray_graph": conn_rel is not None,
            }
        )

    return {
        "model_id": model_cfg["model_id"],
        "brand": model_cfg["brand"],
        "label": model_cfg["label"],
        "format": "toyota_svgz",
        "pack_id": model_cfg["pack_id"],
        "system_count": len(systems),
        "systems": systems,
    }


def index_avanza_pdfs(seven_z: str, archive_dir: Path, cache_root: Path) -> dict | None:
    avanza_rar = archive_dir / "RM AVANZA.rar"
    if not avanza_rar.exists():
        return None
    avanza_dir = cache_root / "toyota" / "toyota_avanza_pdf"
    extract_patterns(
        seven_z,
        avanza_rar,
        avanza_dir,
        ["*.pdf"],
    )
    docs = []
    for pdf in sorted(avanza_dir.rglob("*.pdf")):
        rel = str(pdf.relative_to(cache_root)).replace("\\", "/")
        norm = rel.lower()
        if "/system/" in norm:
            cat = "Wiring Sistem (Avanza)"
        elif "/routing/" in norm:
            cat = "Routing & Lokasi Kabel"
        elif "/relay/" in norm:
            cat = "Lokasi Relay & Fuse Box"
        else:
            cat = "Daftar Soket & Konektor"
        doc_id = f"avanza__{pdf.stem.lower()}"
        docs.append(
            {
                "doc_id": doc_id,
                "title": pdf.stem.replace("-", " ").replace("_", " "),
                "category": cat,
                "rel_path": rel,
                "size_kb": round(pdf.stat().st_size / 1024, 1),
            }
        )
    return {
        "model_id": "toyota_avanza_pdf",
        "brand": "Toyota",
        "label": "Toyota Avanza / Xenia Gen 1 (K3-VE / 3SZ-VE — EWD PDF Asli)",
        "format": "pdf_collection",
        "pack_id": "toyota_avanza_xenia_2004_2015",
        "doc_count": len(docs),
        "docs": docs,
    }


def index_suzuki_pdfs(workspace_root: Path) -> list[dict]:
    suzuki_dir = workspace_root / "manual repair suzuki vitara"
    models = []
    gv1 = suzuki_dir / "manual repair suzuki grand vitara 2012.pdf"
    gv2 = suzuki_dir / "grand vitara 2.pdf"
    if gv1.exists() or gv2.exists():
        docs = []
        if gv1.exists():
            docs.append(
                {
                    "doc_id": "suzuki_gv_vol1",
                    "title": "Grand Vitara JB420 Vol.1 — Mesin, CKP (Hal. 173), MAP (Hal. 126), Sistem Kontrol",
                    "category": "Manual PDF Vektor Asli (Bahasa Indonesia)",
                    "abs_rel_workspace": str(gv1.relative_to(workspace_root)).replace("\\", "/"),
                    "quick_pages": [
                        {"label": "DTC P0335 CKP & Starter (Hal. 173)", "page": 173},
                        {"label": "Prosedur Ukur CKP (Hal. 174)", "page": 174},
                        {"label": "Diagnosa Mesin Umum (Hal. 61)", "page": 61},
                        {"label": "Tabel Fail-Safe ECM (Hal. 91)", "page": 91},
                        {"label": "DTC P0106 MAP Sensor (Hal. 126)", "page": 126},
                    ],
                }
            )
        if gv2.exists():
            docs.append(
                {
                    "doc_id": "suzuki_gv_vol2",
                    "title": "Grand Vitara JB420 Vol.2 — Transmisi A/T, AC, SRS Airbag, Body BCM",
                    "category": "Manual PDF Vektor Asli (Bahasa Indonesia)",
                    "abs_rel_workspace": str(gv2.relative_to(workspace_root)).replace("\\", "/"),
                    "quick_pages": [
                        {"label": "DTC P1777 CAN TCM–ECM (Hal. 97)", "page": 97},
                        {"label": "Sistem AC (Hal. 301)", "page": 301},
                        {"label": "Wiring SRS Airbag (Hal. 379)", "page": 379},
                        {"label": "Kontrol Kelistrikan Bodi BCM (Hal. 739)", "page": 739},
                    ],
                }
            )
        models.append(
            {
                "model_id": "suzuki_grand_vitara_jb420",
                "brand": "Suzuki",
                "label": "Suzuki Grand Vitara JB420 / J20A (PDF Vektor + Alur Interaktif)",
                "format": "pdf_collection",
                "pack_id": "suzuki_grand_vitara_jb420",
                "doc_count": len(docs),
                "docs": docs,
            }
        )

    ertiga = suzuki_dir / "MANUAL REPAIR SUZUKI ERTIGA GEN 1 2012 SAMPEI 2017.pdf"
    if ertiga.exists():
        models.append(
            {
                "model_id": "suzuki_ertiga_k14b",
                "brand": "Suzuki",
                "label": "Suzuki Ertiga Gen 1 K14B 2012–2017 (PDF Vektor + Alur Interaktif)",
                "format": "pdf_collection",
                "pack_id": "suzuki_ertiga_gen1_2012_2017",
                "doc_count": 1,
                "docs": [
                    {
                        "doc_id": "suzuki_ertiga_full",
                        "title": "Suzuki Ertiga Gen 1 K14B Full Service Manual (1.620 Halaman)",
                        "category": "Manual PDF Vektor Asli",
                        "abs_rel_workspace": str(ertiga.relative_to(workspace_root)).replace("\\", "/"),
                        "quick_pages": [
                            {"label": "DTC P0122/P0123 TPS (Hal. 105)", "page": 105},
                            {"label": "DTC P0222/P0223 APP/TPS (Hal. 118)", "page": 118},
                            {"label": "Circuit Diagram K14B (Hal. 131)", "page": 131},
                            {"label": "Circuit Diagram K14B (Hal. 144)", "page": 144},
                            {"label": "Sinyal CAN Communication (Hal. 170)", "page": 170},
                        ],
                    }
                ],
            }
        )
    return models


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract lightweight local EWD cache for AGOS")
    parser.add_argument(
        "--archive-dir",
        default=r"D:\Repair Manual TOYOTA ZIP FILE",
        help="Folder sumber arsip RAR/ZIP manual Toyota",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Lewati ekstraksi ulang RAR jika folder model sudah ada dan berisi file",
    )
    args = parser.parse_args()

    backend_dir = Path(__file__).resolve().parents[2]
    workspace_root = backend_dir.parent
    cache_root = backend_dir / "local_ewd_cache"
    cache_root.mkdir(parents=True, exist_ok=True)
    archive_dir = Path(args.archive_dir)

    seven_z = find_7z_binary()
    print(f"Menggunakan 7z: {seven_z}")
    print(f"Target cache lokal: {cache_root}")

    models_index = []

    # 1. Ekstrak 6 Model Toyota SVGZ + connect/*.xml (ringan!)
    for cfg in TOYOTA_SVGZ_MODELS:
        rar_path = archive_dir / cfg["archive"]
        model_dir = cache_root / "toyota" / cfg["model_id"]
        if args.skip_existing and model_dir.exists() and any(model_dir.rglob("*.svgz")):
            print(f"-> [CACHE] Memuat ulang indeks {cfg['model_id']}...")
        else:
            if not rar_path.exists():
                print(f"[SKIP] Arsip tidak ditemukan: {rar_path}")
                continue
            print(f"-> Mengekstrak EWD ringan dari {cfg['archive']}...")
            extract_patterns(
                seven_z,
                rar_path,
                model_dir,
                [
                    "*system\\fig\\*.svgz",
                    "*system\\connect\\*.xml",
                    "*system\\title.xml",
                ],
            )
        m_idx = build_svgz_model_index(cfg, model_dir, cache_root)
        models_index.append(m_idx)
        print(f"   OK: {m_idx['system_count']} sistem EWD (.svgz + connect XML)")

    # 2. Ekstrak Avanza EWD PDFs
    print("-> Mengekstrak EWD PDF dari RM AVANZA.rar...")
    avanza_idx = index_avanza_pdfs(seven_z, archive_dir, cache_root)
    if avanza_idx:
        models_index.append(avanza_idx)
        print(f"   OK: {avanza_idx['doc_count']} dokumen PDF EWD Avanza")

    # 3. Indeks Suzuki PDFs (tanpa duplikasi file!)
    suzuki_models = index_suzuki_pdfs(workspace_root)
    models_index.extend(suzuki_models)
    print(f"-> Terindeks {len(suzuki_models)} model Suzuki PDF lokal (zero duplication)")

    # Hitung total ukuran cache
    total_bytes = sum(f.stat().st_size for f in cache_root.rglob("*") if f.is_file())
    index_payload = {
        "version": "1.0",
        "cache_size_mb": round(total_bytes / (1024 * 1024), 2),
        "models": models_index,
    }
    index_file = cache_root / "ewd_index.json"
    index_file.write_text(json.dumps(index_payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSELESAI! Indeks ditulis ke: {index_file}")
    print(f"Total ukuran cache lokal EWD: {index_payload['cache_size_mb']} MB")


if __name__ == "__main__":
    main()
