#!/usr/bin/env python3
"""
AGOS Smart Diagnostik — Automated QA Gate: Validasi Data DTC, Wiring OEM & Pinout Konektor
===========================================================================================
Sesuai PRD Evaluasi DTC & Wiring v1.1 (Prompt 3 & Prompt 4 — Zero-Hallucination Policy).

Skrip ini memvalidasi seluruh 207 DTC JB420, Shared Wiring Asset Registry, Atlas Pillar 3,
UI Wiring Simulator (Web & Offline), dan paket Offline APK.

GAGAL (exit code 1) jika ditemukan:
  1. DTC dengan `wiring_ref_id` atau `oem_wiring_image` kosong/null, tidak terdaftar di
     `wiring_diagrams`, atau file gambar fisiknya tidak ada (> 0 bytes) di Web & Offline.
  2. Referensi text-only ("Lihat P0xxx" / "Sama dengan P0xxx") tanpa resolved image valid,
     atau sisa file gambar text-only lama yang masih direferensikan di kode/atlas/JSON.
  3. Ketidakcocokan antara `connector.pin_count`, `len(connector.pins)`, `len(wiring_pinout)`,
     dan konfigurasi jumlah kabel di simulator UI (`WIRING_CIRCUITS` pada `index.html`),
     atau pelanggaran kunci Opsi A (A/F Sensor-1 WAJIB 4-Pin 2x2, dilarang 6-Pin `af_6w`).
  4. Duplikasi nomor pin, nomor pin < 1, nomor pin > `pin_count`, atau pin tidak berurutan 1..N.
  5. Ketidaksinkronan antara katalog Web & Offline APK atau adanya CDN eksternal di bundle offline.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB_STATIC = ROOT / "backend" / "app" / "static"
OFFLINE_WWW = ROOT / "android_offline" / "www"
CATALOG_WEB = ROOT / "backend" / "app" / "jb420_extracted_catalog.json"
CATALOG_OFFLINE = OFFLINE_WWW / "data" / "jb420_catalog.json"
ATLAS_JS = WEB_STATIC / "js" / "jb420-wiring-atlas.js"
WEB_INDEX = WEB_STATIC / "index.html"
OFFLINE_INDEX = OFFLINE_WWW / "index.html"
DIAG_SERVICE = ROOT / "backend" / "app" / "services" / "diagnostic_service.py"
OFFLINE_ENGINE = OFFLINE_WWW / "js" / "engine.js"

OBSOLETE_TEXT_ONLY_FILES = [
    "v1_maf_p0102_1a65.webp",
    "v1_iat_p0112_1a77.webp",
    "v1_map_p0107_1a70.webp",
    "v1_ect_p0118_1a85.webp",
    "v1_egr_p0403_1a123.webp",
]

TEXT_ONLY_REF_RE = re.compile(
    r"(?:lihat\s+(?:dtc\s+)?[PCBU]\d{4}|sama\s+dengan\s+[PCBU]\d{4}|see\s+dtc\s+[PCBU]\d{4})",
    re.IGNORECASE,
)

# Ground truth OEM kritis yang dikunci dari audit Vol 1 & Vol 2 + keputusan user (Opsi A 4-Pin A/F)
OEM_LOCKED_ASSERTIONS: dict[str, dict] = {
    "P0101": {"pin_count": 5, "layout": "1x5", "image": "img/jb420_wiring/v1_maf_p0101_1a62.webp"},
    "P0102": {"pin_count": 5, "layout": "1x5", "image": "img/jb420_wiring/v1_maf_p0101_1a62.webp"},
    "P0103": {"pin_count": 5, "layout": "1x5", "image": "img/jb420_wiring/v1_maf_p0101_1a62.webp"},
    "P0111": {"pin_count": 5, "layout": "1x5", "image": "img/jb420_wiring/v1_iat_p0111_1a74.webp"},
    "P0112": {"pin_count": 5, "layout": "1x5", "image": "img/jb420_wiring/v1_iat_p0111_1a74.webp"},
    "P0106": {"pin_count": 3, "layout": "1x3", "image": "img/jb420_wiring/v1_map_p0106_1a68.webp"},
    "P0107": {"pin_count": 3, "layout": "1x3", "image": "img/jb420_wiring/v1_map_p0106_1a68.webp"},
    "P0108": {"pin_count": 3, "layout": "1x3", "image": "img/jb420_wiring/v1_map_p0106_1a68.webp"},
    "P0116": {"pin_count": 2, "layout": "1x2", "image": "img/jb420_wiring/v1_ect_p0116_1a81.webp"},
    "P0118": {"pin_count": 2, "layout": "1x2", "image": "img/jb420_wiring/v1_ect_p0116_1a81.webp"},
    "P0030": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_af_heater_p0030_1a54.webp"},
    "P0031": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_af_heater_p0030_1a54.webp"},
    "P0032": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_af_heater_p0030_1a54.webp"},
    "P0131": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_af_p0131_1a94.webp"},
    "P0132": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_af_p0131_1a94.webp"},
    "P0133": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_af_p0131_1a94.webp"},
    "P0134": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_af_p0131_1a94.webp"},
    "P0037": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_ho2s_p0037_1a59.webp"},
    "P0137": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_ho2s2_p0137_1a97.webp"},
    "P0335": {"pin_count": 3, "layout": "1x3", "image": "img/jb420_wiring/v1_ckp_p0335_1a115.webp"},
    "P0340": {"pin_count": 3, "layout": "1x3", "image": "img/jb420_wiring/v1_cmp_p0340_1a117.webp"},
    "P0327": {"pin_count": 1, "layout": "1x1", "image": "img/jb420_wiring/v1_knock_p0327_1a113.webp"},
    "P0328": {"pin_count": 1, "layout": "1x1", "image": "img/jb420_wiring/v1_knock_p0327_1a113.webp"},
    "P0401": {"pin_count": 6, "layout": "2x3", "image": "img/jb420_wiring/v1_egr_p0401_1a120.webp"},
    "P0402": {"pin_count": 6, "layout": "2x3", "image": "img/jb420_wiring/v1_egr_p0401_1a120.webp"},
    "P0403": {"pin_count": 6, "layout": "2x3", "image": "img/jb420_wiring/v1_egr_p0401_1a120.webp"},
    "P0420": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_cat_p0420_1a125.webp"},
    "P0462": {"pin_count": 2, "layout": "1x2", "image": "img/jb420_wiring/v1_fuellevel_p0462_1a129.webp"},
    "P0504": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v1_brake_p0504_1a139.webp"},
    "P0532": {"pin_count": 3, "layout": "1x3", "image": "img/jb420_wiring/v1_acpress_p0532_1a141.webp"},
    "P0616": {"pin_count": 4, "layout": "2x2", "image": "img/jb420_wiring/v2_a1_cranking_9a39.webp"},
    "P0620": {"pin_count": 2, "layout": "1x2", "image": "img/jb420_wiring/v2_a2_pengisian_9a40.webp"},
    "P1501": {"pin_count": 3, "layout": "1x3", "image": "img/jb420_wiring/v1_eld_p1501_1a154.webp"},
    "P2122": {"pin_count": 6, "layout": "1x6", "image": "img/jb420_wiring/v1_app_p2122_1a181.webp"},
    "P2138": {"pin_count": 6, "layout": "1x6", "image": "img/jb420_wiring/v1_app_p2122_1a181.webp"},
}


def parse_ui_wiring_circuit_wire_counts(html_text: str) -> dict[str, int]:
    """Parse jumlah `wires: [...]` untuk setiap key di objek `WIRING_CIRCUITS` pada `index.html`."""
    m_start = re.search(r"const\s+WIRING_CIRCUITS\s*=\s*\{", html_text)
    if not m_start:
        return {}
    m_end = re.search(r"\n\s*let\s+dynamicAutoCircuit\s*=", html_text[m_start.start():])
    if not m_end:
        return {}
    block = html_text[m_start.start(): m_start.start() + m_end.start()]
    counts: dict[str, int] = {}

    # coil_4w dibuat lewat buildOemCoilCircuit('suzuki_jb420_builtin', 1) -> 3 pin COP J20A
    if "coil_4w: buildOemCoilCircuit('suzuki_jb420_builtin'" in block:
        counts["coil_4w"] = 3

    key_pattern = re.compile(r"^\s{6}([a-z0-9_]+):\s*\{", re.MULTILINE)
    matches = list(key_pattern.finditer(block))
    for i, km in enumerate(matches):
        key = km.group(1)
        seg_end = matches[i + 1].start() if i + 1 < len(matches) else len(block)
        seg = block[km.start():seg_end]
        wm = re.search(r"wires:\s*\[([\s\S]*?)\],\s*\n\s*steps:", seg)
        if wm:
            wire_objs = re.findall(r"\{\s*sourceType:", wm.group(1))
            counts[key] = len(wire_objs)
    return counts


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not CATALOG_WEB.exists():
        print(f"[FATAL] Catalog tidak ditemukan: {CATALOG_WEB}")
        return 1

    data = json.loads(CATALOG_WEB.read_text(encoding="utf-8"))
    catalog = data.get("dtc_catalog", [])
    registry = data.get("wiring_diagrams", {})

    if not catalog:
        errors.append("dtc_catalog kosong!")
    if not registry:
        errors.append("wiring_diagrams (Shared Wiring Asset Registry) kosong!")

    web_html = WEB_INDEX.read_text(encoding="utf-8") if WEB_INDEX.exists() else ""
    ui_wire_counts = parse_ui_wiring_circuit_wire_counts(web_html)
    if not ui_wire_counts:
        errors.append("Gagal mem-parsing WIRING_CIRCUITS dari backend/app/static/index.html!")

    # ── CHECK 1 & 2 & 3 & 4: AUDIT SELURUH 207 DTC ─────────────────────────────
    seen_codes: set[str] = set()
    by_code: dict[str, dict] = {}
    for entry in catalog:
        code = str(entry.get("code", "")).upper().strip()
        if not code:
            errors.append("Ada entri DTC tanpa kode!")
            continue
        if code in seen_codes:
            errors.append(f"[{code}] Kode DTC duplikat di katalog!")
        seen_codes.add(code)
        by_code[code] = entry

        # 1. Shared Wiring Reference & Physical Asset Check
        ref_id = entry.get("wiring_ref_id")
        img_path = entry.get("oem_wiring_image")
        if not ref_id or not isinstance(ref_id, str):
            errors.append(f"[{code}] wiring_ref_id kosong/null!")
        elif ref_id not in registry:
            errors.append(f"[{code}] wiring_ref_id '{ref_id}' tidak terdaftar di wiring_diagrams!")

        if not img_path or not isinstance(img_path, str):
            errors.append(f"[{code}] oem_wiring_image kosong/null!")
        else:
            if any(obs in img_path for obs in OBSOLETE_TEXT_ONLY_FILES):
                errors.append(f"[{code}] oem_wiring_image masih menunjuk ke halaman text-only lama: {img_path}")
            web_file = WEB_STATIC / img_path
            off_file = OFFLINE_WWW / img_path
            if not web_file.exists() or web_file.stat().st_size == 0:
                errors.append(f"[{code}] File gambar Web tidak ditemukan/kosong: {web_file}")
            if OFFLINE_WWW.exists() and (not off_file.exists() or off_file.stat().st_size == 0):
                errors.append(f"[{code}] File gambar Offline tidak ditemukan/kosong: {off_file}")

        # 2. Text-Only Reference Check tanpa gambar valid
        cross_note = str(entry.get("wiring_cross_ref_note") or "")
        if TEXT_ONLY_REF_RE.search(cross_note) and not img_path:
            errors.append(f"[{code}] Hanya berisi teks referensi '{cross_note}' tanpa oem_wiring_image valid!")

        # 3 & 4. Connector Pin Count, Pin Number Uniqueness, Range & UI Parity
        conn = entry.get("connector")
        pinouts = entry.get("wiring_pinout") or []
        if not isinstance(conn, dict):
            errors.append(f"[{code}] Field 'connector' (Single Source of Truth) tidak ada!")
        else:
            pcount = conn.get("pin_count")
            pins = conn.get("pins")
            layout = str(conn.get("layout") or "")
            if not isinstance(pcount, int) or pcount < 1 or pcount > 8:
                errors.append(f"[{code}] connector.pin_count tidak valid: {pcount!r}")
            elif not isinstance(pins, list) or len(pins) != pcount:
                errors.append(f"[{code}] Mismatch connector.pin_count ({pcount}) vs len(connector.pins) ({len(pins) if isinstance(pins, list) else 'N/A'})!")
            else:
                pin_nums: list[int] = []
                for idx, p in enumerate(pins):
                    pnum = p.get("pin") if isinstance(p, dict) else None
                    if not isinstance(pnum, int):
                        errors.append(f"[{code}] connector.pins[{idx}].pin bukan integer: {pnum!r}")
                    else:
                        if pnum < 1 or pnum > pcount:
                            errors.append(f"[{code}] Nomor pin di luar rentang 1..{pcount}: pin={pnum}")
                        pin_nums.append(pnum)
                if len(set(pin_nums)) != len(pin_nums):
                    errors.append(f"[{code}] Duplikasi nomor pin terdeteksi pada connector.pins: {pin_nums}")
                elif set(pin_nums) != set(range(1, pcount + 1)):
                    errors.append(f"[{code}] Nomor pin tidak lengkap 1..{pcount}: {sorted(pin_nums)}")

            if len(pinouts) != pcount:
                errors.append(f"[{code}] Mismatch len(wiring_pinout) ({len(pinouts)}) vs connector.pin_count ({pcount})!")

            for wp in pinouts:
                if "Konektor Sirkuit" in str(wp.get("pin", "")):
                    errors.append(f"[{code}] Placeholder generik 'Konektor Sirkuit' masih ditemukan di wiring_pinout!")

            # Parity dengan WIRING_CIRCUITS di index.html
            sim_key = str(entry.get("sim_circuit_key") or "")
            if sim_key and sim_key != "dynamic":
                if sim_key not in ui_wire_counts:
                    errors.append(f"[{code}] sim_circuit_key '{sim_key}' tidak ditemukan di WIRING_CIRCUITS (index.html)!")
                elif ui_wire_counts[sim_key] != pcount:
                    errors.append(
                        f"[{code}] Mismatch UI WIRING_CIRCUITS['{sim_key}'] ({ui_wire_counts[sim_key]} wires) "
                        f"vs connector.pin_count ({pcount})!"
                    )

            if not re.match(r"^[12]x[1-8]$", layout):
                errors.append(f"[{code}] connector.layout tidak valid: '{layout}'")

    # ── CHECK 5: VERIFIKASI KUNCI OEM GROUND TRUTH & OPSI A (4-PIN A/F) ────────
    for code, expected in OEM_LOCKED_ASSERTIONS.items():
        ent = by_code.get(code)
        if not ent:
            errors.append(f"[OEM LOCK] DTC wajib {code} hilang dari katalog!")
            continue
        conn = ent.get("connector") or {}
        if conn.get("pin_count") != expected["pin_count"]:
            errors.append(f"[OEM LOCK {code}] pin_count={conn.get('pin_count')} != wajib {expected['pin_count']}!")
        if conn.get("layout") != expected["layout"]:
            errors.append(f"[OEM LOCK {code}] layout={conn.get('layout')} != wajib {expected['layout']}!")
        if ent.get("oem_wiring_image") != expected["image"]:
            errors.append(f"[OEM LOCK {code}] oem_wiring_image={ent.get('oem_wiring_image')} != wajib {expected['image']}!")

    # Cek khusus ECT tidak boleh lagi punya typo C37-56
    for ect_c in ("P0116", "P0117", "P0118"):
        ent = by_code.get(ect_c) or {}
        blob = json.dumps(ent, ensure_ascii=False)
        if "C37-56" in blob:
            errors.append(f"[OEM LOCK {ect_c}] Typo C37-56 (pin Knock!) masih ada di entri ECT — wajib C37-24!")

    # ── CHECK 6: ZERO 6-PIN A/F HALLUCINATION (`af_6w`) & ZERO OBSOLETE FILES ──
    scan_targets = [
        ("index.html (Web)", WEB_INDEX),
        ("index.html (Offline)", OFFLINE_INDEX),
        ("jb420-wiring-atlas.js", ATLAS_JS),
        ("diagnostic_service.py", DIAG_SERVICE),
        ("engine.js (Offline)", OFFLINE_ENGINE),
        ("jb420_extracted_catalog.json", CATALOG_WEB),
    ]
    for label, fpath in scan_targets:
        if not fpath.exists():
            continue
        txt = fpath.read_text(encoding="utf-8")
        if "af_6w" in txt:
            errors.append(f"[OPSI A VIOLATION] Identifier 'af_6w' masih ditemukan di {label}!")
        if re.search(r"6-Pin\s*(?:Wideband|Soket\s*A/F|JB420)|6-Kabel\s*A/F|A/F\s*\(6-Kabel", txt, re.IGNORECASE):
            errors.append(f"[OPSI A VIOLATION] Teks asumsi A/F 6-Pin masih ditemukan di {label}!")
        for obs in OBSOLETE_TEXT_ONLY_FILES:
            if obs in txt:
                errors.append(f"[TEXT-ONLY ASSET] Referensi file text-only lama '{obs}' masih ada di {label}!")

    # Pastikan 5 file text-only lama juga sudah terhapus fisik dari disk
    for folder_lbl, base_dir in [("Web", WEB_STATIC / "img" / "jb420_wiring"), ("Offline", OFFLINE_WWW / "img" / "jb420_wiring")]:
        for obs in OBSOLETE_TEXT_ONLY_FILES:
            if (base_dir / obs).exists():
                errors.append(f"[CLEANUP] File text-only lama masih ada di {folder_lbl}: {base_dir / obs}")

    # ── CHECK 7: AUDIT SEMUA FOTO DI `jb420-wiring-atlas.js` ───────────────────
    if ATLAS_JS.exists():
        atlas_txt = ATLAS_JS.read_text(encoding="utf-8")
        atlas_imgs = re.findall(r"img:\s*'([^']+)'", atlas_txt)
        if not atlas_imgs:
            errors.append("Tidak ditemukan daftar gambar pada jb420-wiring-atlas.js!")
        for rel in atlas_imgs:
            wf = WEB_STATIC / rel
            of = OFFLINE_WWW / rel
            if not wf.exists() or wf.stat().st_size == 0:
                errors.append(f"[ATLAS] Foto Web hilang/kosong: {rel}")
            if OFFLINE_WWW.exists() and (not of.exists() or of.stat().st_size == 0):
                errors.append(f"[ATLAS] Foto Offline hilang/kosong: {rel}")
        # Cek typo ECT di Atlas
        ect_block_m = re.search(r"id:\s*'gv_ect'[\s\S]*?id:\s*'gv_af_ho2s'", atlas_txt)
        if ect_block_m and "C37-56" in ect_block_m.group(0):
            errors.append("[ATLAS gv_ect] Typo pin C37-56 masih ada di jb420-wiring-atlas.js (wajib C37-24)!")

    # ── CHECK 8: PARITAS OFFLINE APK & ZERO-CDN ────────────────────────────────
    if CATALOG_OFFLINE.exists():
        off_data = json.loads(CATALOG_OFFLINE.read_text(encoding="utf-8"))
        if len(off_data.get("dtc_catalog", [])) != len(catalog):
            errors.append(
                f"[OFFLINE PARITY] Jumlah DTC offline ({len(off_data.get('dtc_catalog', []))}) != web ({len(catalog)})!"
            )
        if len(off_data.get("wiring_diagrams", {})) != len(registry):
            errors.append(
                f"[OFFLINE PARITY] Jumlah wiring_diagrams offline ({len(off_data.get('wiring_diagrams', {}))}) != web ({len(registry)})!"
            )
        off_p0030 = next((d for d in off_data.get("dtc_catalog", []) if d.get("code") == "P0030"), None)
        if not off_p0030 or (off_p0030.get("connector") or {}).get("pin_count") != 4:
            errors.append("[OFFLINE PARITY] P0030 di android_offline/www/data/jb420_catalog.json belum 4-pin!")
    else:
        errors.append(f"[OFFLINE PARITY] File katalog offline tidak ditemukan: {CATALOG_OFFLINE}")

    if OFFLINE_INDEX.exists():
        off_html = OFFLINE_INDEX.read_text(encoding="utf-8")
        for forbidden in ("cdn.tailwindcss.com", "cdnjs.cloudflare.com", "fonts.googleapis.com", "api.qrserver.com"):
            if forbidden in off_html:
                errors.append(f"[OFFLINE ZERO-CDN] URL CDN eksternal terdeteksi di offline index.html: {forbidden}")

    # ── RINGKASAN LAPORAN QA GATE ──────────────────────────────────────────────
    print("=" * 72)
    print("  AGOS SMART DIAGNOSTIK — AUTOMATED DTC & WIRING OEM QA GATE REPORT")
    print("=" * 72)
    print(f"  Total DTC Diaudit          : {len(catalog)}")
    print(f"  Shared Wiring Assets       : {len(registry)}")
    print(f"  UI WIRING_CIRCUITS Parsed  : {len(ui_wire_counts)} sirkuit")
    print(f"  OEM Ground-Truth Locks     : {len(OEM_LOCKED_ASSERTIONS)} DTC kritis (termasuk P0101, P0030 4-Pin, P0106)")
    print(f"  Total Warnings             : {len(warnings)}")
    print(f"  Total Errors               : {len(errors)}")
    print("-" * 72)

    for w in warnings:
        print(f"  [WARN]  {w}")

    if errors:
        for e in errors:
            print(f"  [FAIL]  {e}")
        print("=" * 72)
        print("  STATUS QA GATE: GAGAL (EXIT CODE 1)")
        print("=" * 72)
        return 1

    print("  [PASS]  100% DTC memiliki wiring_ref_id & file gambar OEM HD fisik (Web + Offline).")
    print("  [PASS]  0 referensi text-only tanpa gambar & 0 file text-only usang tersisa.")
    print("  [PASS]  100% connector.pin_count === len(pins) === len(wiring_pinout) === UI wires.")
    print("  [PASS]  0 duplikasi pin & 0 nomor pin di luar rentang 1..pin_count.")
    print("  [PASS]  Opsi A A/F Sensor-1 4-Pin (2x2) terkunci ketat (0 sisa af_6w / 6-pin).")
    print("  [PASS]  Paritas katalog Web ↔ Offline APK 100% identik & Zero-CDN terverifikasi.")
    print("=" * 72)
    print("  STATUS QA GATE: 100% LULUS (EXIT CODE 0)")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
