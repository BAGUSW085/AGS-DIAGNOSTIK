"""
Enrichment & Quality Audit Tool for ALL 207 Suzuki Grand Vitara JB420 DTCs.
Populates every single DTC in backend/app/jb420_extracted_catalog.json with:
  1. Cleaned Indonesian text (fixes PDF OCR typos like 'EGRvalve', 'E G R v a l v e', 'atauN' -> 'ORN').
  2. Logical, real-world workshop `curated_repair_options` (component service/clean/test FIRST, then socket/harness, then supply/scanner/ECM LAST).
  3. Authentic 3-Tier OEM Measurement Standards directly from Suzuki Grand Vitara JB420 Manual
     (Bab 1A-34..36 Data Scan Tool & Bab 1A-199..207 Tegangan Terminal ECM):
       - `standard_specs`: Static Measurement (IG ON / Kunci OFF — Multimeter Ohm & Volt)
       - `idle_standards`: Engine Idle Measurement (Mesin Hidup · Panas Kerja 80–90°C)
       - `scanner_standards`: OBD-II Scan Tool Live Data & Active Test Reference
  4. Explicit `sim_circuit_key` & `atlas_module_id` so ZERO non-ignition DTCs can ever fall back to Ignition Coil!
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "backend" / "app" / "jb420_extracted_catalog.json"


def clean_pdf_text(text: str) -> str:
    if not text:
        return ""
    s = str(text)
    # Fix spaced PDF headings/tokens (e.g. "E G R  v a l v e", "E C M", "T C M", "A B S")
    s = re.sub(r"\bE\s*G\s*R\s*v\s*a\s*l\s*v\s*e\b", "Katup EGR (EGR Valve)", s, flags=re.IGNORECASE)
    s = re.sub(r"\bEGRvalve\b", "Katup EGR (EGR Valve)", s, flags=re.IGNORECASE)
    s = re.sub(r"\bE\s+C\s+M\b", "ECM", s)
    s = re.sub(r"\bT\s+C\s+M\b", "TCM", s)
    s = re.sub(r"\bB\s+C\s+M\b", "BCM", s)
    s = re.sub(r"\bS\s+D\s+M\b", "SDM", s)
    s = re.sub(r"\bG\s+anti\b", "Ganti", s)
    # Fix infamous Suzuki ID PDF auto-translation: "ORN" -> "atauN"
    s = re.sub(r"[“\"']?atauN[”\"']?", '"ORN" (Oranye)', s)
    s = re.sub(r"\bSIrkuit\b", "Sirkuit", s)
    s = re.sub(r"\bSistim\b", "Sistem", s)
    s = re.sub(r"\bsistim\b", "sistem", s)
    s = re.sub(r"\bkoslet\b", "korslet", s, flags=re.IGNORECASE)
    s = re.sub(r"\bputaran\s+putaran\b", "putaran", s, flags=re.IGNORECASE)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# -----------------------------------------------------------------------------
# COMPREHENSIVE JB420 SUBSYSTEM PROFILES (100% OFFICIAL MANUAL BAB 1A-34 & 1A-199)
# -----------------------------------------------------------------------------
PROFILES: dict[str, dict] = {
    "egr_control": {
        "sim_circuit_key": "egr_6w",
        "atlas_module_id": "gv_egr_evap_imtv",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Servis & Bersihkan EGR)",
                "title": "Bongkar & Bersihkan Katup EGR serta Saluran Gas Buang dari Kerak Karbon",
                "desc": "Semprot ruang katup, dudukan plunger, dan saluran intake EGR dengan carb/intake cleaner hingga kerak karbon rontok dan plunger bergerak lancar tanpa macet.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Katup EGR",
                "title": "Ukur Tahanan 4 Kumparan Stepper Motor EGR (20–31 Ω) & Ganti Unit Jika Rusak",
                "desc": "Ukur tahanan antara Pin 2↔1, 2↔3, 5↔4, 5↔6 pada soket 6-pin EGR (standar 20–31 Ω @ 20°C). Ganti katup EGR bila kumparan putus (OL), korslet, atau motor stepper macet.",
            },
            {
                "tag": "Opsi 3 • Soket & Jalur Kabel EGR",
                "title": "Periksa Suplai +12V (BLU/BLK) & Jalur 4 Kabel Stepper (C37-03 s/d C37-06)",
                "desc": "Pastikan tegangan 10–14V masuk ke kabel BLU/BLK (E23-01/16), bersihkan pin soket 6-pin EGR, dan perbaiki kabel YEL/BLK, YEL/RED, YEL/GRN, atau YEL yang putus/korslet.",
            },
            {
                "tag": "Opsi 4 • Uji Aktif Scanner & ECM",
                "title": "Hapus DTC, Lakukan Active Test EGR via Scanner & Evaluasi ECM (Langkah Terakhir)",
                "desc": "Buka paksa katup EGR 30–50% via Active Test saat idle (mesin harus goyang/hampir mati). Cek/ganti ECM hanya jika katup EGR dan seluruh kabel terbukti 100% normal.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Katup EGR (Pin 2 & 5 · BLU/BLK, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tahanan 4 Kumparan Stepper EGR (Pin 2↔1/3 & 5↔4/6 @ 20°C)", "normal_range": "20 – 31", "unit": "Ohm"},
            {"parameter": "Tegangan Standby ECM C37-03/04/05/06 (IG ON, Soket Terpasang)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Isolasi Kabel YEL/BLK, YEL/RED, YEL/GRN, YEL ke Massa (Kunci OFF)", "normal_range": "Tak Terhingga (OL / > 1 MΩ)", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Terminal ECM C37-03/04/05/06 Saat Idle Panas (EGR Tertutup)", "normal_range": "10.0 – 14.0 V (Stabil)", "unit": "V DC"},
            {"parameter": "Pulsa Kontrol Stepper C37-03/04/05/06 (Cranking / 2.500 RPM Beban)", "normal_range": "0 – 1 V ↑↓ 10 – 14 V (Duty Pulse)", "unit": "V Pulse"},
            {"parameter": "Putaran Mesin Idle Panas & Kestabilan (EGR Tertutup Rapat)", "normal_range": "650 ± 50 RPM (Halus, tidak pincang)", "unit": "RPM"},
            {"parameter": "Reaksi Mesin Saat EGR Dibuka Paksa di Idle (Uji Kebocoran/Macet)", "normal_range": "Idle langsung pincang / hampir mati", "unit": "Respon"},
        ],
        "scanner_standards": [
            {"parameter": "EGR VALVE OPENING (Bab 1A-35 · Idle Panas Tanpa Beban)", "normal_range": "0 % (0 step — Tertutup Rapat)", "unit": "%"},
            {"parameter": "EGR VALVE OPENING (Akselerasi / Jalan 2.000–3.500 RPM Panas)", "normal_range": "15 – 50 % (Aktif Bertahap)", "unit": "%"},
            {"parameter": "MAP Sensor saat Active Test EGR 0% → 40% di Idle", "normal_range": "Naik dari 24–38 kPa → > 45 kPa", "unit": "kPa"},
            {"parameter": "COOLANT TEMP (Syarat Kerja EGR Aktif)", "normal_range": "80 – 100 °C", "unit": "°C"},
        ],
    },

    "evap_purge": {
        "sim_circuit_key": "evap_2w",
        "atlas_module_id": "gv_egr_evap_imtv",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Katup & Selang EVAP)",
                "title": "Bersihkan Katup Solenoid EVAP Purge & Cek Selang Vakum Kanister",
                "desc": "Lepas katup EVAP (C16), pastikan katup menutup rapat saat OFF (tidak bocor saat ditiup) dan selang vakum kanister bebas retak/tersumbat arang karbon.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Solenoid EVAP",
                "title": "Ukur Tahanan Kumparan Katup EVAP (30–34 Ω @ 20°C) & Ganti Jika Putus",
                "desc": "Ukur tahanan antara Pin 1 dan Pin 2 soket 2-pin EVAP Purge Valve. Ganti unit katup bila tahanan OL/korslet atau katup gagal klik saat diberi +12V sesaat.",
            },
            {
                "tag": "Opsi 3 • Soket & Kabel C37-13",
                "title": "Periksa Suplai +12V (BLU/BLK) & Kabel Kontrol ECM C37-13 (GRN/BLK)",
                "desc": "Verifikasi tegangan +12V di Pin 1 soket EVAP saat IG ON dan kontinuitas kabel GRN/BLK ke ECM C37-13 (< 2 Ω, tidak korslet massa).",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Main Relay ke Soket EVAP (Pin 1 · BLU/BLK, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tahanan Kumparan Katup EVAP Purge (Pin 1↔2 @ 20°C)", "normal_range": "30 – 34", "unit": "Ohm"},
            {"parameter": "Tegangan ECM C37-13 (GRN/BLK · IG ON Mesin Mati)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Terminal ECM C37-13 Saat Idle Panas (Purge OFF)", "normal_range": "10.0 – 14.0 V", "unit": "V DC"},
            {"parameter": "Sinyal Duty Pulse C37-13 Saat Active Test 52% (Bab 1A-200)", "normal_range": "0 – 0.6 V ↑↓ 10 – 14 V (PWM)", "unit": "V Pulse"},
            {"parameter": "Kerapatan Katup EVAP Saat Idle (Tanpa Aktivasi)", "normal_range": "Tertutup rapat (0 kebocoran vakum)", "unit": "Kondisi"},
        ],
        "scanner_standards": [
            {"parameter": "CANIST PRG DUTY (Bab 1A-35 · Idle Panas Tanpa Beban)", "normal_range": "0 %", "unit": "%"},
            {"parameter": "CANIST PRG DUTY (Jalan Stabil / Misc Test Scanner)", "normal_range": "10 – 60 % (Aktif Saat Cruise)", "unit": "%"},
            {"parameter": "SHORT FT B1 (Reaksi Saat Purge Diaktifkan 50%)", "normal_range": "Turun sesaat (–5% s/d –15%)", "unit": "%"},
        ],
    },

    "imt_valve": {
        "sim_circuit_key": "imt_2w",
        "atlas_module_id": "gv_egr_evap_imtv",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Servis Katup & Vakum IMT)",
                "title": "Periksa Selang Vakum Intake Tuning, Diafragma Aktuator & Bersihkan Katup IMT",
                "desc": "Pastikan selang vakum tangki vakum & diafragma IMT tidak sobek/lepas serta batang penggerak katup intake bergerak lancar.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Solenoid IMT",
                "title": "Ukur Tahanan Kumparan Solenoid IMT (30–40 Ω @ 20°C) & Ganti Jika Putus",
                "desc": "Ukur tahanan 2 pin solenoid IMT; ganti unit solenoid apabila kumparan putus (OL) atau katup tidak membuka saluran vakum saat diberi +12V.",
            },
            {
                "tag": "Opsi 3 • Kabel C37-33 & Suplai +12V",
                "title": "Periksa Suplai +12V (BLU/BLK) & Jalur Kabel ECM C37-33 (GRY/RED)",
                "desc": "Cek tegangan 10–14V pada BLU/BLK (IG ON), pastikan kabel GRY/RED ke C37-33 tidak putus atau korslet ke massa/power.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Solenoid IMT (Pin 1 · BLU/BLK, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tahanan Kumparan Solenoid IMT (Pin 1↔2 @ 20°C)", "normal_range": "30 – 40", "unit": "Ohm"},
            {"parameter": "Tegangan Terminal ECM C37-33 (GRY/RED · IG ON Mesin Mati)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Terminal ECM C37-33 Saat Idle Panas (Bab 1A-202)", "normal_range": "0.0 – 1.0 V (Aktif ON)", "unit": "V DC"},
            {"parameter": "Tegangan Terminal ECM C37-33 Saat Putaran ≥ 4.700 RPM", "normal_range": "10.0 – 14.0 V (Non-Aktif OFF)", "unit": "V DC"},
            {"parameter": "Gerakan Tuas Aktuator Vakum IMT Saat Mesin Distart → Idle", "normal_range": "Tertarik Penuh oleh Vakum", "unit": "Mekanis"},
        ],
        "scanner_standards": [
            {"parameter": "INTAKE TUNING SOL (Bab 1A-35 · Putaran Idle Panas)", "normal_range": "ON", "unit": "Status"},
            {"parameter": "INTAKE TUNING SOL (Putaran ≥ 4.700 RPM)", "normal_range": "OFF", "unit": "Status"},
            {"parameter": "MAP (Intake Manifold Absolute Pressure · Idle)", "normal_range": "24 – 38 kPa", "unit": "kPa"},
        ],
    },

    "ign_coil": {
        "sim_circuit_key": "coil_4w",
        "atlas_module_id": "gv_ign_coil",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Busi & Swap Test Koil)",
                "title": "Periksa/Ganti Busi & Lakukan Swap Test Koil COP ke Silinder Lain",
                "desc": "Cek celah busi (1.0–1.1 mm), pastikan boot karet koil tidak retak/bocor api, dan tukar koil ke silinder tetangga: bila misfire ikut pindah, ganti unit koil COP.",
            },
            {
                "tag": "Opsi 2 • Soket & Jalur Koil 3-Pin",
                "title": "Cek Sekering #39 (20A IG COIL), Ground Pin 3 (BLK/ORN) & Trigger C37-18..21",
                "desc": "Ukur +12V pada Pin 1 (BLK/WHT), kontinuitas ground Pin 3 (< 1 Ω ke blok), dan pulsa trigger 5V dari ECM C37-21/20/19/18.",
            },
            {
                "tag": "Opsi 3 • Injektor & Kompresi Mesin",
                "title": "Periksa Injektor Silinder Terkait & Ukur Tekanan Kompresi Silinder",
                "desc": "Jika pengapian sehat tetapi masih pincang, periksa pengabutan injektor (11.5–14.5 Ω) dan ukur kompresi (standar J20A: 12–14 kg/cm²).",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Koil Pin 1 (BLK/WHT · Sekering #39 20A IG COIL, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Kontinuitas Ground Koil Pin 3 (BLK/ORN ke Blok Mesin, Kunci OFF)", "normal_range": "< 1.0", "unit": "Ohm"},
            {"parameter": "Tegangan Trigger ECM C37-21/20/19/18 (IG ON Mesin Mati)", "normal_range": "0.0 – 0.6", "unit": "V DC"},
            {"parameter": "Celah Elektroda Busi J20A (IFR6J11 / K20PR-U11)", "normal_range": "1.0 – 1.1", "unit": "mm"},
        ],
        "idle_standards": [
            {"parameter": "Pulsa Trigger Koil C37-21/20/19/18 Saat Idle Panas (Bab 1A-201)", "normal_range": "0 – 0.6 V ↑↓ 3 – 5 V (Active-High Pulse)", "unit": "V Pulse"},
            {"parameter": "Tegangan Suplai Pin 1 Koil Saat Mesin Idle", "normal_range": "13.5 – 14.5", "unit": "V DC"},
            {"parameter": "Putaran Mesin Idle Tanpa Beban (J20A Panas)", "normal_range": "650 ± 50", "unit": "RPM"},
        ],
        "scanner_standards": [
            {"parameter": "IGNITION ADVANCE (Bab 1A-35 · Idle Panas Tanpa Beban)", "normal_range": "5 – 15 ° BTDC", "unit": "° BTDC"},
            {"parameter": "MISFIRE COUNTER (Silinder #1 – #4 Saat Idle)", "normal_range": "0 hitungan (Stabil)", "unit": "Count"},
            {"parameter": "SHORT FT B1 / LONG FT B1 (Idle Panas)", "normal_range": "–10% s/d +10% (Limit ±20%)", "unit": "%"},
        ],
    },

    "ckp": {
        "sim_circuit_key": "ckp_2w",
        "atlas_module_id": "gv_ckp",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Ukur & Ganti Sensor CKP)",
                "title": "Bersihkan Ujung Sensor CKP, Cek Rotor & Ukur Tahanan Induktif (1,68–2,52 kΩ)",
                "desc": "Bersihkan gram besi di ujung magnet sensor CKP, ukur tahanan antar 2 pin sensor pada kondisi dingin & panas (standar 1.680–2.520 Ω @ 20°C). Ganti sensor bila putus saat panas.",
            },
            {
                "tag": "Opsi 2 • Soket & Kabel Shield CKP",
                "title": "Perbaiki Soket 2-Pin CKP & Cek Kabel C37-51 (GRN) / C37-36 (PNK)",
                "desc": "Pastikan soket tidak terendam rembesan oli, periksa kontinuitas kabel ke C37-51 dan C37-36 (< 2 Ω) serta isolasi terhadap ground.",
            },
            {
                "tag": "Opsi 3 • Rantai Timing & ECM",
                "title": "Periksa Gigi Rotor Crankshaft (36–6) & Sinyal RPM pada Scanner Saat Cranking",
                "desc": "Pastikan pelat rotor crankshaft tidak patah/longgar dan scanner membaca 180–250 RPM saat distarter.",
            },
        ],
        "static_specs": [
            {"parameter": "Tahanan Kumparan Sensor CKP Induktif J20A (20°C)", "normal_range": "1.68 – 2.52", "unit": "kOhm"},
            {"parameter": "Tegangan Terminal ECM C37-51 (GRN) & C37-36 (PNK · IG ON)", "normal_range": "0.0 – 1.0", "unit": "V DC"},
            {"parameter": "Kontinuitas Kabel CKP ke ECM C37-51 & C37-36 (Kunci OFF)", "normal_range": "< 2.0", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Gelombang Sinusoidal C37-51 ke C37-36 Saat Idle Panas (Bab 1A-204)", "normal_range": "+4..6 V ↑↓ –4..–6 V AC (30 pulsa/putaran)", "unit": "V AC"},
            {"parameter": "Tegangan AC Multimeter CKP Saat Cranking (200 RPM)", "normal_range": "≥ 0.5 – 1.5 V AC", "unit": "V AC"},
            {"parameter": "Putaran Mesin Idle Stabil (J20A Panas)", "normal_range": "650 ± 50", "unit": "RPM"},
        ],
        "scanner_standards": [
            {"parameter": "ENGINE SPEED (Saat Mesin Di-Crank / Starter)", "normal_range": "180 – 250 RPM (Wajib terbaca!)", "unit": "RPM"},
            {"parameter": "ENGINE SPEED / DESIRED IDLE (Bab 1A-34 · Idle Panas)", "normal_range": "650 ± 50 RPM", "unit": "RPM"},
            {"parameter": "IGNITION ADVANCE (Idle Panas)", "normal_range": "5 – 15 ° BTDC", "unit": "° BTDC"},
        ],
    },

    "cmp": {
        "sim_circuit_key": "cmp_3w",
        "atlas_module_id": "gv_cmp",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Ukur & Ganti Sensor CMP)",
                "title": "Bersihkan Sensor CMP (Hall-IC) dari Lumpur Oli & Ganti Jika Pulsa Hilang",
                "desc": "Lepas sensor CMP di belakang cylinder head, bersihkan ujung magnetik dari sludge oli, dan ganti sensor bila suplai +12V & ground normal namun sinyal C37-52 diam.",
            },
            {
                "tag": "Opsi 2 • Soket 3-Pin & Kabel C37-52",
                "title": "Periksa Suplai +12V (BLU/BLK), Ground (BLK/ORN) & Sinyal C37-52 (WHT/RED)",
                "desc": "Ukur +12V pada Pin 1, kontinuitas massa Pin 3 (< 1 Ω), dan kabel sinyal WHT/RED ke ECM C37-52.",
            },
            {
                "tag": "Opsi 3 • Rantai Timing & Sinkronisasi CKP-CMP",
                "title": "Periksa Kekendoran Rantai Timing (Timing Chain) & Tanda Top Camshaft",
                "desc": "Rantai timing mulur menyebabkan fasa pulsa CMP bergeser terhadap CKP dan memicu P0340.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Main Relay Sensor CMP Pin 1 (BLU/BLK, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal ECM C37-52 (WHT/RED · IG ON Mesin Mati)", "normal_range": "0 – 1 V atau 4 – 5 V (tergantung posisi nok)", "unit": "V DC"},
            {"parameter": "Massa Sensor CMP Pin 3 (BLK/ORN ke Bodi, Kunci OFF)", "normal_range": "< 1.0", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Pulsa Sinyal CMP C37-52 ke Massa Saat Idle Panas (Bab 1A-204)", "normal_range": "0 – 0.6 V ↑↓ 4 – 5 V (6 pulsa/putaran cam)", "unit": "V Pulse"},
            {"parameter": "Tegangan Rata-rata Multimeter DC di C37-52 Saat Idle", "normal_range": "2.0 – 3.5 V DC (Berdenyut)", "unit": "V DC"},
            {"parameter": "Waktu Starter Mesin (Normal vs P0340)", "normal_range": "1 – 2 detik langsung hidup", "unit": "Detik"},
        ],
        "scanner_standards": [
            {"parameter": "ENGINE SPEED (Dihitung ECM dari Pulsa CMP — Bab 1A-37)", "normal_range": "650 ± 50 RPM (Idle Panas)", "unit": "RPM"},
            {"parameter": "FUEL SYSTEM B1 (Idle Panas)", "normal_range": "CLSD (Closed Loop)", "unit": "Status"},
            {"parameter": "IGNITION ADVANCE (Idle Panas)", "normal_range": "5 – 15 ° BTDC", "unit": "° BTDC"},
        ],
    },

    "maf_iat": {
        "sim_circuit_key": "maf_5w",
        "atlas_module_id": "gv_maf_iat",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cleaning MAF & Filter Udara)",
                "title": "Bersihkan Elemen Kawat Sensor MAF/IAT dengan MAF Cleaner & Cek Filter Udara",
                "desc": "Semprot kawat hot-wire MAF & termistor IAT memakai MAF Sensor Cleaner khusus (jangan disentuh tangan!), ganti filter udara kotor, dan cek kebocoran karet belalai intake.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Sensor MAF/IAT",
                "title": "Ukur Tegangan Sinyal MAF (C37-26) / IAT (C37-25) & Ganti Sensor Jika Meleset",
                "desc": "Bila suplai +12V dan ground normal namun output MAF di luar 0.5–1.0V (IG ON) / 1.3–1.8V (Idle), atau suhu IAT tidak sesuai suhu ruang, ganti unit MAF/IAT assy.",
            },
            {
                "tag": "Opsi 3 • Soket 5-Pin & Jalur Kabel",
                "title": "Periksa Soket 5-Pin MAF (BLU/BLK, RED, BLU, LT GRN, GRY/GRN)",
                "desc": "Pastikan suplai +12V Main Relay masuk ke Pin 1, ground C37-27 & C37-57 < 0.3V, dan soket tidak kendur/korosi.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Main Relay MAF Pin 1 (BLU/BLK, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal MAF C37-26 (RED · IG ON Mesin Mati)", "normal_range": "0.50 – 1.00", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal IAT C37-25 (LT GRN · IG ON @ 40°C)", "normal_range": "1.32 – 1.65 (3.18–3.67V @ 0°C)", "unit": "V DC"},
            {"parameter": "Ground Sensor MAF C37-27 (BLU) & IAT C37-57 (GRY/GRN)", "normal_range": "< 0.3 V (< 3 Ω)", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Sinyal MAF C37-26 Saat Idle Panas (Bab 1A-202)", "normal_range": "1.30 – 1.80", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal MAF C37-26 Saat Digas 2.500–4.000 RPM", "normal_range": "2.20 – 3.50 (Naik Responsif)", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal IAT C37-25 Saat Idle Panas (Ruang Mesin ~40–60°C)", "normal_range": "0.85 – 1.65", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "MAF (Mass Air Flow Rate · Bab 1A-34 Idle Panas)", "normal_range": "1.0 – 4.0 g/s", "unit": "g/s"},
            {"parameter": "MAF pada 2.500 RPM Tanpa Beban (Bab 1A-34)", "normal_range": "4.0 – 12.0 g/s", "unit": "g/s"},
            {"parameter": "INTAKE AIR TEMP (Bab 1A-34 · Idle Panas)", "normal_range": "Suhu ruang + (–5°C s/d +40°C)", "unit": "°C"},
            {"parameter": "CALC LOAD (Idle Tanpa Beban)", "normal_range": "0 – 10 %", "unit": "%"},
        ],
    },

    "map_baro": {
        "sim_circuit_key": "map_3w",
        "atlas_module_id": "gv_map",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Vakum & Bersihkan MAP)",
                "title": "Periksa Selang Vakum Intake, Lubang Sensor MAP & Kebocoran Gasket Manifold",
                "desc": "Pastikan lubang port vakum sensor MAP tidak mampet kerak oli/karbon serta seluruh selang vakum (PCV, booster rem, EVAP) rapat tanpa kebocoran.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Sensor MAP",
                "title": "Ukur Referensi +5V (C37-14) & Sinyal MAP (C37-55), Ganti Sensor Jika Menyimpang",
                "desc": "Bila +5V (4.5–5.5V) dan ground C37-57 (< 0.3V) normal namun output C37-55 tidak ~4.0V (IG ON) atau tidak turun ke 0.4–2.0V saat idle, ganti sensor MAP.",
            },
            {
                "tag": "Opsi 3 • Soket 3-Pin & Jalur +5V Bersama",
                "title": "Periksa Jalur +5V Bersama (GRY/RED C37-14) & Massa Sensor (GRY/GRN C37-57)",
                "desc": "Catatan JB420: Kabel GRY/RED C37-14 dipakai bersama oleh MAP, A/C Pressure & ELC Sensor; cek apakah salah satu sensor korslet menarik +5V turun.",
            },
        ],
        "static_specs": [
            {"parameter": "Tegangan Referensi +5V MAP C37-14 (GRY/RED, IG ON)", "normal_range": "4.5 – 5.5", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal MAP C37-55 (RED/WHT · IG ON @ 100 kPa)", "normal_range": "Sekitar 3.8 – 4.2", "unit": "V DC"},
            {"parameter": "Ground Sensor MAP C37-57 (GRY/GRN, IG ON)", "normal_range": "< 0.3", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Sinyal MAP C37-55 Saat Idle Panas (Bab 1A-204)", "normal_range": "0.40 – 2.00 V (Tipikal 1.1 – 1.5 V)", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal MAP Saat Gas Dihentak (Snap Throttle)", "normal_range": "Lonjak ke 3.5 – 4.2 V lalu turun cepat", "unit": "V DC"},
            {"parameter": "Ke-vakuman Intake Manifold (Vacuum Gauge Idle)", "normal_range": "18 – 22 in.Hg", "unit": "in.Hg"},
        ],
        "scanner_standards": [
            {"parameter": "MAP (Intake Manifold Absolute Pressure · Bab 1A-35 Idle)", "normal_range": "24 – 38 kPa (7.1 – 11.2 in.Hg)", "unit": "kPa"},
            {"parameter": "MAP Saat Kunci Kontak ON (Mesin Mati · Permukaan Laut)", "normal_range": "96 – 103 kPa (≈ BARO)", "unit": "kPa"},
            {"parameter": "BAROMETRIC PRES (Bab 1A-35)", "normal_range": "95 – 103 kPa (sesuai elevasi)", "unit": "kPa"},
        ],
    },

    "ect": {
        "sim_circuit_key": "ect_2w",
        "atlas_module_id": "gv_ect",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Coolant, Soket & Thermostat)",
                "title": "Periksa Level Air Radiator, Bleeding Udara Palsu & Bersihkan Soket 2-Pin ECT",
                "desc": "Pastikan radiator terisi penuh tanpa kantong udara, thermostat bekerja normal (buka ~82°C), dan pin konektor ECT bebas korosi/rembesan air.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Sensor ECT",
                "title": "Ukur Tahanan NTC Sensor ECT (20°C vs 80°C) & Ganti Sensor Jika Menyimpang",
                "desc": "Ukur tahanan sensor: 2,21–2,69 kΩ @ 20°C dan 290–354 Ω @ 80°C. Ganti sensor ECT baru (torsi 15 N·m) bila nilai meleset atau putus (terbaca –40°C).",
            },
            {
                "tag": "Opsi 3 • Jalur Kabel C37-24 & C37-57",
                "title": "Perbaiki Kabel Sinyal C37-24 (PPL/YEL) & Massa Sensor C37-57 (GRY/GRN)",
                "desc": "Pastikan kabel PPL/YEL tidak putus (membaca 5V / –40°C) atau korslet ke massa (membaca 0V / +140°C).",
            },
        ],
        "static_specs": [
            {"parameter": "Tahanan NTC Sensor ECT pada Suhu Dingin (20°C)", "normal_range": "2.21 – 2.69", "unit": "kOhm"},
            {"parameter": "Tahanan NTC Sensor ECT pada Suhu Kerja (80°C)", "normal_range": "290 – 354", "unit": "Ohm"},
            {"parameter": "Tegangan Sinyal C37-24 (PPL/YEL · IG ON Dingin 20–30°C)", "normal_range": "2.20 – 3.10 (3.3–3.8V @ 0°C)", "unit": "V DC"},
            {"parameter": "Tegangan Ground Sensor C37-57 (GRY/GRN, IG ON)", "normal_range": "< 0.3", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Sinyal ECT C37-24 Saat Idle Panas 85–95°C (Bab 1A-202)", "normal_range": "0.40 – 0.65 (0.40–0.53V @ 100°C)", "unit": "V DC"},
            {"parameter": "Aktivasi Kipas Radiator #1 (Relay Low)", "normal_range": "ON pada ≥ 97.5°C · OFF < 95°C", "unit": "°C"},
            {"parameter": "Putaran Mesin Idle Panas (Setelah Warm-Up)", "normal_range": "650 ± 50", "unit": "RPM"},
        ],
        "scanner_standards": [
            {"parameter": "COOLANT TEMP (Bab 1A-34 · Idle Setelah Pemanasan)", "normal_range": "80 – 100 °C (176 – 212 °F)", "unit": "°C"},
            {"parameter": "COOLANT TEMP vs INTAKE AIR TEMP (Start Pagi Dingin)", "normal_range": "Selisih < 3 °C (Suhu ruang ~28–32°C)", "unit": "°C"},
            {"parameter": "RADIATOR FAN RENDAH (Bab 1A-36)", "normal_range": "OFF (< 95°C) / ON (≥ 97.5°C)", "unit": "Status"},
        ],
    },

    "af_sensor1": {
        "sim_circuit_key": "af_6w",
        "atlas_module_id": "gv_af_ho2s",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Ukur Heater & Ganti A/F Sensor-1)",
                "title": "Ukur Tahanan Heater A/F Sensor-1 (2,0–3,5 Ω @ 20°C) & Ganti Unit Jika Putus",
                "desc": "Lepas soket 6-pin A/F Sensor depan (manifold knalpot), ukur tahanan pemanas (Pin 1–2). Ganti unit A/F Sensor-1 (torsi 44 N·m) bila heater putus atau elemen jenuh karbon.",
            },
            {
                "tag": "Opsi 2 • Soket 6-Pin, Main Relay & Sekering O2 HTR",
                "title": "Periksa Sekering O2 HTR, Suplai +12V (BLU/BLK) & Jalur C37-32/34/35/37/38",
                "desc": "Pastikan +12V Main Relay masuk ke Pin 1 (BLU/BLK), kabel tidak meleleh kena pipa knalpot, dan pin C37-32/31/38/37/35/34 tersambung utuh.",
            },
            {
                "tag": "Opsi 3 • Cek Kebocoran Knalpot & Tekanan BBM",
                "title": "Periksa Kebocoran Paking Exhaust Manifold & Kualitas Campuran BBM",
                "desc": "Kebocoran knalpot sebelum sensor A/F atau misfire memicu pembacaan miskin palsu & memunculkan DTC A/F.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Heater A/F Pin 1 (BLU/BLK · Main Relay, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tegangan Kontrol Heater C37-32 (PNK/BLU · IG ON Mesin Mati)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tegangan Resistor Kalibrasi C37-35 (RED/YEL · IG ON)", "normal_range": "0.15 – 4.82", "unit": "V DC"},
            {"parameter": "Tahanan Heater A/F Sensor-1 (Pada 20°C)", "normal_range": "2.0 – 3.5", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan A/F Sensor Signal (+) C37-38 (WHT · Idle Panas, Bab 1A-203)", "normal_range": "3.0 – 3.2", "unit": "V DC"},
            {"parameter": "Tegangan A/F Sensor Signal (–) C37-37 (BLK · Idle Panas, Bab 1A-202)", "normal_range": "2.6 – 2.8", "unit": "V DC"},
            {"parameter": "Pulsa PWM Heater C37-32 (PNK/BLU · Idle Panas, Bab 1A-202)", "normal_range": "0 – 1 V ↑↓ 10 – 14 V (Duty Pulse)", "unit": "V Pulse"},
        ],
        "scanner_standards": [
            {"parameter": "A/F B1 S1 CURRENT (Bab 1A-35 · Idle Panas)", "normal_range": "–0.20 s/d +0.10 mA (≈ 0 mA Stoikiometri)", "unit": "mA"},
            {"parameter": "A/F B1 S1 ACT (Status Aktivasi · Bab 1A-35)", "normal_range": "AKTIF", "unit": "Status"},
            {"parameter": "FUEL SYSTEM B1 (Idle Panas)", "normal_range": "CLSD (Closed Loop)", "unit": "Status"},
            {"parameter": "SHORT FT B1 / LONG FT B1", "normal_range": "–10% s/d +10% (Limit ±20%)", "unit": "%"},
        ],
    },

    "ho2s2": {
        "sim_circuit_key": "o2_4w",
        "atlas_module_id": "gv_af_ho2s",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Ukur Heater & Ganti HO2S-2)",
                "title": "Ukur Tahanan Heater HO2S-2 Belakang (5–15 Ω @ 20°C) & Ganti Sensor Jika Putus",
                "desc": "Cabut soket 4-pin HO2S-2 di belakang katalitik konverter, ukur tahanan kumparan pemanas. Ganti unit HO2S-2 baru (kunci 22 mm, torsi 44 N·m) bila heater putus/sinyal macet.",
            },
            {
                "tag": "Opsi 2 • Soket 4-Pin & Kabel Bawah Kolong",
                "title": "Perbaiki Kabel Sensor HO2S-2 (BLU/BLK, BLK/RED C37-47, RED C37-11, BLK/YEL)",
                "desc": "Sensor berada di kolong knalpot—sering terputus/tertarik polisi tidur atau terkena air; cek +12V BLU/BLK, kontrol heater C37-47, sinyal RED C37-11, dan massa.",
            },
            {
                "tag": "Opsi 3 • Paking Knalpot & Katalis",
                "title": "Cek Kebocoran Pipa Knalpot Sebelum HO2S-2 & Reset DTC via Scanner",
                "desc": "Kebocoran pipa knalpot membuat O2 belakang membaca oksigen tinggi terus-menerus.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai +12V Heater HO2S-2 (BLU/BLK · Main Relay, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tahanan Heater HO2S-2 Belakang (Pada 20°C)", "normal_range": "5.0 – 15.0", "unit": "Ohm"},
            {"parameter": "Tegangan Bias Sinyal C37-11 (RED · IG ON Mesin Mati, Bab 1A-200)", "normal_range": "4.0 – 5.0", "unit": "V DC"},
            {"parameter": "Tegangan Standby Heater C37-47 (BLK/RED · IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Sinyal HO2S-2 C37-11 Saat Idle Panas (Bab 1A-200)", "normal_range": "Sekitar 0.15 – 0.85 V (Stabil ~0.6–0.7V katalis sehat)", "unit": "V DC"},
            {"parameter": "Pulsa PWM Heater C37-47 Saat Idle Panas (Bab 1A-203)", "normal_range": "0 – 1 V ↑↓ 10 – 14 V (Duty Pulse)", "unit": "V Pulse"},
            {"parameter": "Massa Sensor HO2S-2 (BLK/YEL ke Bodi)", "normal_range": "< 0.3", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "O2S B1 S2 (Bab 1A-35 · 2.000 RPM ≥ 3 Menit Panas)", "normal_range": "0.10 – 0.95 V", "unit": "V"},
            {"parameter": "O2S B1 S2 ACT (Status Aktivasi · Bab 1A-35)", "normal_range": "AKTIF", "unit": "Status"},
            {"parameter": "FUEL SYSTEM B1 (Idle Panas)", "normal_range": "CLSD (Closed Loop)", "unit": "Status"},
        ],
    },

    "etc_tps_app": {
        "sim_circuit_key": "etc_6w",
        "atlas_module_id": "gv_etc_app",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Carbon Clean & Relearn)",
                "title": "Bersihkan Kerak Karbon Throttle Body & Lakukan Kalibrasi Idle Relearn",
                "desc": "Bersihkan kupu-kupu & dinding throttle body memakai throttle cleaner lembut (jangan paksa pegas kasar), pastikan katup tidak macet, lalu lakukan Idle Air Volume Learning.",
            },
            {
                "tag": "Opsi 2 • Ukur Soket 6-Pin ETC / APP & Relay THR MOT",
                "title": "Cek Sekering/Relay THR MOT (E23-17/50), Referensi +5V & Sinyal Main/Sub",
                "desc": "Ukur tahanan motor ETC (0.5–10 Ω), suplai +5V TPS (C37-53) / APP (E23-56 & E23-53), serta sinkronisasi tegangan Main vs Sub saat pedal ditekan perlahan.",
            },
            {
                "tag": "Opsi 3 • Ganti Unit Throttle Body / Pedal APP",
                "title": "Ganti Unit Electric Throttle Body Assy atau Sensor Pedal Gas (APP)",
                "desc": "Ganti unit ETC/APP jika motor aktuator putus, gear internal aus, atau grafik tegangan TPS/APP meloncat/putus saat pedal diinjak halus.",
            },
        ],
        "static_specs": [
            {"parameter": "Tahanan Motor Aktuator Throttle (Pin 1↔2 · C37-44/45 @ 20°C)", "normal_range": "0.5 – 10.0", "unit": "Ohm"},
            {"parameter": "Suplai +5V TPS (C37-53) & APP Main/Sub (E23-56 / E23-53, IG ON)", "normal_range": "4.5 – 5.5", "unit": "V DC"},
            {"parameter": "Suplai Daya Motor Throttle E23-17 (GRN · Relay THR MOT, IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "TPS Main (C37-54) / Sub (C37-40) IG ON Pedal Penuh (WOT)", "normal_range": "3.67–4.25 V (Main) · 3.88–4.45 V (Sub)", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan TPS Main C37-54 & Sub C37-40 Saat Idle (Bab 1A-203/204)", "normal_range": "0.72–1.04 V (Main) · 1.60–1.91 V (Sub)", "unit": "V DC"},
            {"parameter": "Tegangan APP Main E23-55 & Sub E23-52 Pedal Dilepas (Bab 1A-207)", "normal_range": "0.65–0.82 V (Main) · 0.30–0.44 V (Sub)", "unit": "V DC"},
            {"parameter": "Pulsa Motor ETC C37-44/45 Saat Idle Panas", "normal_range": "0 – 1 V ↑↓ 10 – 14 V (PWM Halus)", "unit": "V Pulse"},
        ],
        "scanner_standards": [
            {"parameter": "THROTTLE POSITION (Bab 1A-35 · Pedal Dilepas → Penuh)", "normal_range": "0 – 5 % (Idle) → 90 – 100 % (WOT)", "unit": "%"},
            {"parameter": "TP SENSOR 1 / 2 VOLT (Bab 1A-36 · Pedal Dilepas)", "normal_range": "0.7–1.2 V (TP1) · 1.6–2.0 V (TP2)", "unit": "V"},
            {"parameter": "APP SENSOR 1 VOLT (Bab 1A-36 · Dilepas → Penuh)", "normal_range": "0.7–0.8 V → 3.5–4.3 V", "unit": "V"},
            {"parameter": "DESIRED IDLE / ENGINE SPEED (Idle Panas)", "normal_range": "650 ± 50 RPM", "unit": "RPM"},
        ],
    },

    "cooling_fan": {
        "sim_circuit_key": "fan_4w",
        "atlas_module_id": "gv_cooling_fan",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Sekering, Relay & Motor Kipas)",
                "title": "Periksa Sekering RAD FAN, Uji Tukar Relay Kipas #1/#2/#3 & Tes Putar Motor Kipas",
                "desc": "Ukur tahanan koil Relay Kipas (60–120 Ω), pastikan motor kipas berputar kencang dan tidak macet/aus carbon brush saat diuji langsung +12V.",
            },
            {
                "tag": "Opsi 2 • Soket & Jalur Kontrol E23-46/47/48",
                "title": "Periksa Suplai +12V IG1 & Kabel Kontrol Relay ECM E23-46/47/48",
                "desc": "Ukur 10–14V di E23-46 (RED/BLK) saat kipas OFF; tegangan harus turun ke 0–2V saat Active Test kipas ON atau ECT ≥ 97.5°C.",
            },
            {
                "tag": "Opsi 3 • Cek Sensor ECT & Sistem Pendingin",
                "title": "Verifikasi Pembacaan Sensor ECT & Kuras/Bleeding Coolant Bila Overheat",
                "desc": "Pastikan sensor ECT membaca suhu aktual 80–100°C agar ECM memberi perintah kipas pada suhu tepat.",
            },
        ],
        "static_specs": [
            {"parameter": "Tahanan Koil Relay Kipas #1/#2/#3 (Pin 85↔86 @ 20°C)", "normal_range": "60 – 120", "unit": "Ohm"},
            {"parameter": "Tegangan Standby ECM E23-46/47/48 (IG ON, Kipas OFF)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Suplai Daya Utama Motor Kipas (Sekering 30A RAD FAN)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan E23-46 (Relay #1) Saat Idle Panas ≥ 97.5°C / AC ON (Bab 1A-206)", "normal_range": "0.0 – 2.0 V (Kipas Aktif)", "unit": "V DC"},
            {"parameter": "Tegangan E23-47/48 (Relay #2/#3) Saat ECT ≥ 102.5°C / AC ≥ 1600 kPa", "normal_range": "0.0 – 2.0 V (High Speed ON)", "unit": "V DC"},
            {"parameter": "Arus Kerja Motor Kipas Radiator (Normal)", "normal_range": "6 – 12 A (Putaran halus & kencang)", "unit": "A"},
        ],
        "scanner_standards": [
            {"parameter": "RADIATOR FAN RENDAH (Relay #1 · Bab 1A-36)", "normal_range": "OFF (< 95°C) → ON (≥ 97.5°C)", "unit": "Status"},
            {"parameter": "RADIATOR FAN NO.1 & NO.2 TINGGI (Relay #2/#3 · Bab 1A-36)", "normal_range": "OFF (< 100°C) → ON (≥ 102.5°C)", "unit": "Status"},
            {"parameter": "COOLANT TEMP (Idle Panas)", "normal_range": "80 – 100 °C", "unit": "°C"},
        ],
    },

    "knock": {
        "sim_circuit_key": "knock_2w",
        "atlas_module_id": "gv_knock",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Pemasangan & Torsi Sensor Knock)",
                "title": "Periksa Dudukan, Kebersihan Permukaan Blok & Torsi Baut Knock Sensor (23 N·m)",
                "desc": "Baut knock sensor kendor atau dudukan blok berkarat melemahkan sinyal piezo. Pastikan permukaan bersih & kencangkan tepat 23 N·m.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Knock Sensor",
                "title": "Ukur Tahanan Internal Knock Sensor (500–620 kΩ @ 20°C) & Ganti Jika Putus",
                "desc": "Ukur tahanan antara terminal sensor dan bodi/pin ground (standar 500–620 kΩ). Ganti knock sensor bila nilai OL/korslet atau rumah plastik retak.",
            },
            {
                "tag": "Opsi 3 • Kabel Shield C37-56 & BBM",
                "title": "Periksa Kabel Shield C37-56 (WHT) & Pastikan Oktan BBM Sesuai (RON ≥ 92)",
                "desc": "Pastikan kabel sinyal WHT tidak putus/korslet ke pelindung shield massa dan tidak ada bunyi ketukan mekanis berat dari mesin.",
            },
        ],
        "static_specs": [
            {"parameter": "Tahanan Internal Elemen Piezo Knock Sensor (@ 20°C)", "normal_range": "500 – 620", "unit": "kOhm"},
            {"parameter": "Tegangan Bias ECM C37-56 (WHT · IG ON, Bab 1A-204)", "normal_range": "2.0 – 3.0", "unit": "V DC"},
            {"parameter": "Torsi Pengencangan Baut Knock Sensor ke Blok", "normal_range": "23", "unit": "N·m"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan DC Bias C37-56 Saat Mesin Idle Panas", "normal_range": "2.0 – 3.0 V DC (Stabil)", "unit": "V DC"},
            {"parameter": "Sinyal AC Piezo C37-56 Saat Mesin Digas 4.000 RPM (Bab 1A-214)", "normal_range": "Gelombang getaran AC ~0.5–2.0 Vp-p", "unit": "V AC"},
        ],
        "scanner_standards": [
            {"parameter": "IGNITION ADVANCE (Bab 1A-35 · Idle Panas)", "normal_range": "5 – 15 ° BTDC (Tidak tertahan mundur)", "unit": "° BTDC"},
            {"parameter": "KNOCK RETARD / SPARK ADVANCE (Akselerasi 2.500–4.000 RPM)", "normal_range": "Naik halus 20 – 38 ° BTDC", "unit": "° BTDC"},
        ],
    },

    "fuel_trim_nonwiring": {
        "sim_circuit_key": "map_3w",
        "atlas_module_id": "gv_nonwiring_p0171",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Vakum & MAF)",
                "title": "Lakukan Smoke Test Kebocoran Vakum Intake/PCV & Bersihkan Sensor MAF",
                "desc": "P0171/P0172 umumnya masalah mekanis/aliran udara—periksa selang vakum, paking intake, katup PCV, belalai karet filter, dan bersihkan sensor MAF.",
            },
            {
                "tag": "Opsi 2 • Cek Tekanan BBM & Injektor",
                "title": "Ukur Tekanan Fuel Rail (3.0–3.5 bar) & Servis/Kalibrasi 4 Injektor",
                "desc": "Pastikan pompa bensin & filter BBM menghasilkan tekanan 300–350 kPa stabil dan tidak ada injektor tersumbat (P0171) atau menetes bocor (P0172).",
            },
            {
                "tag": "Opsi 3 • Cek Knalpot & A/F Sensor-1",
                "title": "Periksa Kebocoran Exhaust Manifold & Pantau Live Data A/F Sensor-1 + Fuel Trim",
                "desc": "Pastikan tidak ada bocor knalpot sebelum A/F Sensor-1, lalu reset Fuel Trim Learned Values dan uji jalan.",
            },
        ],
        "static_specs": [
            {"parameter": "Tekanan Bahan Bakar (Fuel Pressure · IG ON Priming)", "normal_range": "300 – 350 (3.0 – 3.5 bar)", "unit": "kPa"},
            {"parameter": "Tahanan Kumparan Injektor #1–#4 (@ 20°C)", "normal_range": "11.5 – 14.5", "unit": "Ohm"},
            {"parameter": "Suplai +5V Sensor MAP (C37-14) & +12V MAF (BLU/BLK)", "normal_range": "4.5–5.5 V (MAP) · 10–14 V (MAF)", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tekanan Bahan Bakar Fuel Rail Saat Mesin Idle", "normal_range": "300 – 350 kPa (Stabil)", "unit": "kPa"},
            {"parameter": "Tegangan Sinyal MAF (C37-26) & MAP (C37-55) Saat Idle Panas", "normal_range": "1.3–1.8 V (MAF) · 1.1–1.5 V (MAP)", "unit": "V DC"},
            {"parameter": "Tegangan A/F Sensor-1 C37-38 (+) / C37-37 (–) Saat Idle", "normal_range": "3.0–3.2 V (+) · 2.6–2.8 V (–)", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "SHORT FT B1 (STFT) & LONG FT B1 (LTFT · Bab 1A-35)", "normal_range": "–10% s/d +10% (Ambang DTC ±20%)", "unit": "%"},
            {"parameter": "TOTAL FUEL TRIM B1 (Bab 1A-35)", "normal_range": "–15% s/d +15% (Limit ±35%)", "unit": "%"},
            {"parameter": "MAF & MAP Saat Idle Panas", "normal_range": "1.0–4.0 g/s · 24–38 kPa", "unit": "g/s · kPa"},
            {"parameter": "A/F B1 S1 CURRENT (Bab 1A-35)", "normal_range": "–0.20 s/d +0.10 mA", "unit": "mA"},
        ],
    },

    "catalyst_nonwiring": {
        "sim_circuit_key": "o2_4w",
        "atlas_module_id": "gv_nonwiring_p0420",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Kebocoran Knalpot & Misfire)",
                "title": "Periksa Kebocoran Pipa/Gasket Knalpot, Riwayat Misfire & Fuel Trim Dahulu",
                "desc": "Jangan langsung vonis katalis! Kebocoran kecil di gasket exhaust atau misfire/BBM buruk sering memicu P0420 palsu.",
            },
            {
                "tag": "Opsi 2 • Bandingkan Grafik A/F-1 vs HO2S-2 & Tes Suhu Katalis",
                "title": "Uji Perbandingan Grafik O2 Depan vs Belakang & Ukur Suhu Inlet/Outlet Katalis",
                "desc": "Pada katalis sehat, sinyal HO2S-2 tenang (~0.6–0.7V) & suhu outlet katalis 30–60°C lebih panas daripada inlet. Cek HO2S-2 bila lambat/menyimpang.",
            },
            {
                "tag": "Opsi 3 • Pembersihan / Ganti Catalytic Converter",
                "title": "Lakukan Carbon/Catalyst Cleaning atau Ganti Unit Catalytic Converter",
                "desc": "Bila tidak ada kebocoran knalpot, sensor O2 sehat, dan grafik HO2S-2 tetap berayun cepat mengikuti A/F depan, ganti unit catalytic converter.",
            },
        ],
        "static_specs": [
            {"parameter": "Tahanan Heater HO2S-2 (Belakang · 20°C)", "normal_range": "5.0 – 15.0", "unit": "Ohm"},
            {"parameter": "Tegangan Bias C37-11 (HO2S-2 · IG ON Mesin Mati)", "normal_range": "4.0 – 5.0", "unit": "V DC"},
            {"parameter": "Kerapatan Pipa & Paking Knalpot Sebelum HO2S-2", "normal_range": "0 Kebocoran Gas Buang", "unit": "Visual"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan HO2S-2 C37-11 Saat Idle Panas (Katalis Sehat)", "normal_range": "Stabil ~0.55 – 0.80 V (Tidak cepat berayun)", "unit": "V DC"},
            {"parameter": "Suhu Outlet vs Inlet Catalytic Converter (IR Thermometer)", "normal_range": "Outlet 30 – 60 °C lebih panas dari Inlet", "unit": "°C"},
        ],
        "scanner_standards": [
            {"parameter": "O2S B1 S2 (Bab 1A-35 · 2.000 RPM ≥ 3 Menit Panas)", "normal_range": "0.10 – 0.95 V (Tenang / fluktuasi lambat)", "unit": "V"},
            {"parameter": "A/F B1 S1 CURRENT vs O2S B1 S2 ACT", "normal_range": "–0.20..+0.10 mA · Keduanya AKTIF", "unit": "mA"},
            {"parameter": "SHORT FT B1 / LONG FT B1", "normal_range": "–10% s/d +10%", "unit": "%"},
        ],
    },

    "charging_elc": {
        "sim_circuit_key": "gen_elc",
        "atlas_module_id": "gv_charging",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Aki, V-Belt & Pengisian)",
                "title": "Periksa Tegangan Aki, Ketegangan V-Belt & Terminal B+ Alternator",
                "desc": "Pastikan V-belt tidak selip, kepala aki kencang bebas sulfat, dan kabel B+ alternator tersambung kuat tanpa voltage drop (> 0.3V).",
            },
            {
                "tag": "Opsi 2 • Servis Alternator / Cek Sensor Beban Arus (ELC)",
                "title": "Servis/Ganti IC Regulator & Carbon Brush Alternator atau Sensor ELC (Kabel Aki)",
                "desc": "Untuk P0620/P0625/P0626 cek IC regulator & sikat arang alternator; untuk P1501/P1502 cek sensor arus ELC pada kabel aki & referensi +5V C37-14.",
            },
            {
                "tag": "Opsi 3 • Soket Alternator & Kabel C37-08/28/09",
                "title": "Perbaiki Jalur Kabel Kontrol Generator (C37-08/28 BRN/BLK) & ELC (C37-09 BLU)",
                "desc": "Pastikan kabel sinyal monitor/kontrol alternator dan sensor ELC ke ECM tidak putus/korslet.",
            },
        ],
        "static_specs": [
            {"parameter": "Tegangan Aki Tanpa Beban (Kunci OFF)", "normal_range": "12.4 – 12.8", "unit": "V DC"},
            {"parameter": "Tegangan Monitor Field C37-08 (BRN/BLK · IG ON, Bab 1A-199)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tegangan Sinyal ELC Sensor C37-09 (BLU · IG ON, Bab 1A-200)", "normal_range": "0.50 – 1.00", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Pengisian Aki Saat Mesin Idle Panas (Lampu OFF / ON)", "normal_range": "13.5 – 14.5", "unit": "V DC"},
            {"parameter": "Pulsa C37-08 (Field) & C37-28 (Control · Lampu ON, Bab 1A-199/202)", "normal_range": "0–1V ↑↓ 10–14V (C37-08) · 0–0.6V ↑↓ 5–7V (C37-28)", "unit": "V Pulse"},
            {"parameter": "Tegangan ELC Sensor C37-09 (2.000 RPM · Lampu + Blower HI)", "normal_range": "1.3–1.7 V (Lampu) · 1.8–2.4 V (Lampu+HI)", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "BATTERY VOLTAGE (Bab 1A-35 · IG ON / Idle)", "normal_range": "10–14 V (IG ON) · 13.5–14.5 V (Idle)", "unit": "V"},
            {"parameter": "GENERATOR CONT DUTY & FIELD DUTY (Bab 1A-35 · Idle)", "normal_range": "100% (Cont) · 10.0 – 50.0% (Field)", "unit": "%"},
            {"parameter": "BATTERY CURRENT J20A (Bab 1A-35 · 2.000 RPM)", "normal_range": "10–16 A (Tanpa Beban) · 35–45 A (Beban HI)", "unit": "A"},
        ],
    },

    "starter_relay": {
        "sim_circuit_key": "starter_rly",
        "atlas_module_id": "gv_cranking",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Aki, Sekering & Relay Starter)",
                "title": "Periksa Tegangan Aki, Sekering ST SIG / STR MOT & Uji/Ganti Relay Starter",
                "desc": "Pastikan tegangan aki ≥ 12.2V saat cranking, cek sekering starter, dan uji kumparan serta kontak daya Relay Starting Motor Control.",
            },
            {
                "tag": "Opsi 2 • Cek Switch Netral/Inhibitor & Motor Starter",
                "title": "Periksa Switch Posisi Tuas P/N (A/T) atau Kopling (M/T) & Solenoid Motor Starter",
                "desc": "Pastikan tuas P/N terbaca benar oleh TCM/ECM dan kabel terminal 50 starter tidak kendor/berkarat.",
            },
            {
                "tag": "Opsi 3 • Jalur Kabel C37-22 (BLK/YEL)",
                "title": "Perbaiki Jalur Kabel Kontrol Relay Starter C37-22 (BLK/YEL) ke Boks Relay",
                "desc": "Ukur kontinuitas kabel BLK/YEL antara ECM C37-22 dan koil relay starter; pastikan tidak putus atau korslet ke massa/power.",
            },
        ],
        "static_specs": [
            {"parameter": "Tegangan ECM C37-22 (BLK/YEL · IG ON Posisi Normal, Bab 1A-201)", "normal_range": "0.0 – 1.0", "unit": "V DC"},
            {"parameter": "Tahanan Kumparan Relay Starter (Pin 85↔86)", "normal_range": "60 – 120", "unit": "Ohm"},
            {"parameter": "Tegangan Aki Statis (Kunci OFF)", "normal_range": "≥ 12.4", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan ECM C37-22 (BLK/YEL) Saat Kunci Posisi ST (Cranking · Bab 1A-201)", "normal_range": "8.0 – 14.0 V", "unit": "V DC"},
            {"parameter": "Tegangan ECM C37-22 Saat Mesin Sudah Hidup (Idle)", "normal_range": "0.0 – 1.0 V (Relay OFF)", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "STARTER SW (Bab 1A-36 · Posisi ST Cranking)", "normal_range": "ON (Saat Starter) · OFF (Saat Idle)", "unit": "Status"},
            {"parameter": "BATTERY VOLTAGE (Saat Cranking / Idle)", "normal_range": "≥ 9.6 V (Crank) · 13.5–14.5 V (Idle)", "unit": "V"},
        ],
    },

    "fuel_level": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_fuel_pump",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Pelampung & Fuel Sender)",
                "title": "Periksa & Bersihkan Pelampung / Resistor Geser Fuel Level Sender di Tangki",
                "desc": "Ukur tahanan sender pelampung bensin pada posisi Penuh (F) dan Kosong (E); ganti pelampung/sender jika lintasan karbon aus atau macet.",
            },
            {
                "tag": "Opsi 2 • Soket Tangki & Kabel E23-24",
                "title": "Perbaiki Konektor Pompa Bensin & Jalur Kabel E23-24 (YEL/RED)",
                "desc": "Bersihkan soket di atas tangki bahan bakar dan pastikan kabel sinyal YEL/RED ke ECM E23-24 & speedometer tidak putus/korslet.",
            },
            {
                "tag": "Opsi 3 • Cek Sub-Sender & Reset DTC",
                "title": "Periksa Sub-Fuel Level Sensor (Tangki Sadel JB420) & Hapus DTC",
                "desc": "Grand Vitara JB420 memiliki Main & Sub fuel level sensor yang dirangkai seri; cek keduanya jika jarum bensin tidak akurat.",
            },
        ],
        "static_specs": [
            {"parameter": "Tegangan Sinyal Fuel Level E23-24 (YEL/RED · IG ON, Bab 1A-206)", "normal_range": "0.5 – 5.5 V (Berubah sesuai isi tangki)", "unit": "V DC"},
            {"parameter": "Tahanan Sender Pelampung Bensin (Penuh → Kosong)", "normal_range": "~10–30 Ω (Penuh) → ~250–320 Ω (Kosong)", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Sinyal E23-24 Saat Mesin Idle (Stabil tidak melompat)", "normal_range": "0.5 – 5.5 V (Stabil)", "unit": "V DC"},
            {"parameter": "Suplai Pompa Bensin E23-15 (WHT/GRN · Idle)", "normal_range": "0.0 – 2.5 V (Pompa ON)", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "FUEL TANK LEVEL (Bab 1A-35 · IG ON / Idle)", "normal_range": "0 – 100 % (Sesuai aktual isi tangki)", "unit": "%"},
            {"parameter": "FUEL PUMP (Bab 1A-35 · Mesin Hidup)", "normal_range": "ON", "unit": "Status"},
        ],
    },

    "vss_brake_ac": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_vss_brake_ac",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Komponen Sensor/Switch)",
                "title": "Periksa & Setel / Ganti Sensor atau Switch Terkait (VSS / Switch Rem / A/C Pressure)",
                "desc": "Untuk P0504 setel tinggi switch pedal rem & cek bohlam rem; untuk P0532/P0533 cek tekanan freon A/C & sensor tekanan; untuk P0500 cek sinyal kecepatan roda dari ABS/VSS.",
            },
            {
                "tag": "Opsi 2 • Soket & Jalur Kabel ke ECM",
                "title": "Perbaiki Konektor & Jalur Kabel Sinyal/Referensi +5V ke ECM",
                "desc": "Bersihkan pin konektor, pastikan suplai +12V (switch rem) atau +5V C37-14 (A/C pressure) masuk dan kabel sinyal tidak putus/korslet.",
            },
            {
                "tag": "Opsi 3 • Verifikasi Scanner & Uji Jalan",
                "title": "Verifikasi Perubahan Data Switch/Sensor via Scanner & Hapus DTC",
                "desc": "Uji tekan-lepas pedal rem (OFF↔ON), nyalakan AC (kPa naik), atau uji jalan (> 20 km/jam untuk VSS) lalu hapus DTC.",
            },
        ],
        "static_specs": [
            {"parameter": "Switch Rem E23-20 (GRN/WHT · Dilepas → Ditekan, Bab 1A-205)", "normal_range": "0–1 V (Lepas) → 10–14 V (Ditekan)", "unit": "V DC"},
            {"parameter": "Switch Rem Cruise E23-08 (YEL/GRN · Dilepas → Ditekan)", "normal_range": "10–14 V (Lepas) → 0–1 V (Ditekan)", "unit": "V DC"},
            {"parameter": "Referensi +5V A/C Pressure C37-14 (GRY/RED · IG ON)", "normal_range": "4.5 – 5.5", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Sinyal A/C Pressure C37-12 (GRY/BLK · Idle, Bab 1A-200)", "normal_range": "1.38–1.52 V (AC OFF) · 2.15–2.38 V (AC ON)", "unit": "V DC"},
            {"parameter": "Sinyal Relay Kompresor A/C E23-49 (PNK · Idle AC ON)", "normal_range": "0.0 – 1.0 V (AC ON) · 10–14 V (AC OFF)", "unit": "V DC"},
            {"parameter": "Sinyal Kecepatan VSS (Saat Kendaraan Jalan)", "normal_range": "Pulsa/CAN sebanding kecepatan roda", "unit": "km/jam"},
        ],
        "scanner_standards": [
            {"parameter": "BRAKE SWITCH (Bab 1A-35 · Dilepas / Ditekan)", "normal_range": "OFF (Dilepas) ↔ ON (Ditekan)", "unit": "Status"},
            {"parameter": "A/C PRESSURE J20A (Bab 1A-36 · 30°C)", "normal_range": "600–1000 kPa (OFF) · 1300–1480 kPa (ON)", "unit": "kPa"},
            {"parameter": "VEHICLE SPEED (Saat Idle vs Jalan)", "normal_range": "0 km/jam (Berhenti) · Sama dgn Speedometer", "unit": "km/jam"},
        ],
    },

    "ecm_power": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_ecm_power",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Aki, Sekering DOME/FI & Main Relay)",
                "title": "Periksa Tegangan Aki, Sekering DOME/FI/IGN & Uji Main Relay ECM",
                "desc": "P1510 sering disebabkan sekering DOME putus atau aki sempat dilepas/drop; cek tegangan permanen +B pada E23-02 (WHT) dan Main Relay E23-01/16 (BLU/BLK).",
            },
            {
                "tag": "Opsi 2 • Cek 5 Titik Ground ECM & Soket E23/C37",
                "title": "Bersihkan Soket ECM & Kencangkan Baut Ground ECM (C37-15/29/30/48/58)",
                "desc": "Pastikan seluruh 5 pin ground utama ECM memiliki tahanan < 1 Ω ke blok mesin (< 0.3V saat IG ON) dan bebas korosi/air.",
            },
            {
                "tag": "Opsi 3 • Reset / Evaluasi Internal ECM",
                "title": "Hapus DTC & Verifikasi Ulang; Ganti/Reprogram ECM Jika P0601/P0602/P0607 Tetap Muncul",
                "desc": "Lakukan verifikasi ulang dengan daya aki stabil; bila kode memori internal ECM muncul kembali setelah daya & ground 100% normal, ganti/reprogram ECM.",
            },
        ],
        "static_specs": [
            {"parameter": "Power Backup Memori ECM E23-02 (WHT · Sekering DOME, Kunci OFF)", "normal_range": "10.0 – 14.0 (Selalu Ada +12V)", "unit": "V DC"},
            {"parameter": "Main Power Supply ECM E23-01 & E23-16 (BLU/BLK · IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Sinyal Kunci Kontak E23-29 (BLK/WHT · IG ON)", "normal_range": "10.0 – 14.0 (0–1 V saat OFF)", "unit": "V DC"},
            {"parameter": "Ground Utama ECM C37-15/29/30/48/58 (IG ON)", "normal_range": "< 0.3 V (< 1 Ω ke blok)", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Kerja ECM E23-01 / E23-16 / E23-02 Saat Mesin Idle", "normal_range": "13.5 – 14.5 V (Stabil)", "unit": "V DC"},
            {"parameter": "Kontrol Main Relay E23-60 (BLU · IG ON / Idle, Bab 1A-207)", "normal_range": "0.0 – 2.0 V (ON) · 10–14 V (OFF)", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "BATTERY VOLTAGE (Bab 1A-35 · IG ON → Idle)", "normal_range": "12.0–12.8 V (IG ON) · 13.5–14.5 V (Idle)", "unit": "V"},
            {"parameter": "STATUS KOMUNIKASI ECM & READINESS", "normal_range": "Terhubung Normal · 0 Error Memori", "unit": "Status"},
        ],
    },

    "can_bus": {
        "sim_circuit_key": "can_2w",
        "atlas_module_id": "gv_can_bus",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Ukur Tahanan Terminasi CAN 60 Ω)",
                "title": "Lepas Aki & Ukur Tahanan Bus CAN-H ↔ CAN-L di DLC Pin 6–14 (Standar 54–66 Ω)",
                "desc": "Jika terbaca ~120 Ω berarti salah satu jalur CAN/resistor terminasi putus; jika < 10 Ω berarti CAN-H dan CAN-L korslet; jika OL berarti jalur putus total.",
            },
            {
                "tag": "Opsi 2 • Cek Soket & Daya Modul Terkait (ECM/TCM/ABS/BCM)",
                "title": "Periksa Sekering, Ground & Konektor Modul yang Gagal Merespons CAN",
                "desc": "Cabut soket modul satu per satu (ABS, TCM, BCM) sambil memantau tahanan & tegangan CAN untuk mengisolasi modul yang membebani jaringan.",
            },
            {
                "tag": "Opsi 3 • Perbaiki Kabel Twisted Pair CAN",
                "title": "Perbaiki Kabel WHT/RED (CAN-H · E23-04) & WHT/BLU (CAN-L · E23-19)",
                "desc": "Pastikan sambungan kabel CAN tetap terpilin rapat (twisted pair) agar bebas gangguan interferensi elektromagnetik, lalu hapus DTC semua modul.",
            },
        ],
        "static_specs": [
            {"parameter": "Tahanan Terminasi Bus CAN (DLC Pin 6 ↔ Pin 14 · Aki Dilepas)", "normal_range": "54 – 66 (2× 120 Ω Paralel)", "unit": "Ohm"},
            {"parameter": "Tegangan Jalur CAN-High E23-04 (WHT/RED · IG ON, Bab 1A-205)", "normal_range": "2.5 – 3.6 (Pulsa s/d 4.5 V)", "unit": "V DC"},
            {"parameter": "Tegangan Jalur CAN-Low E23-19 (WHT/BLU · IG ON, Bab 1A-205)", "normal_range": "1.5 – 2.5 (Pulsa s/d 0.5 V)", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Rata-rata CAN-H & CAN-L Saat Mesin Idle", "normal_range": "~2.6–2.9 V (CAN-H) · ~2.1–2.4 V (CAN-L) · Total ≈ 5.0 V", "unit": "V DC"},
            {"parameter": "Isolasi CAN-H / CAN-L Terhadap Ground Bodi (Kunci OFF)", "normal_range": "> 10 kΩ (Tidak korslet massa)", "unit": "Ohm"},
        ],
        "scanner_standards": [
            {"parameter": "ALL MODULE HEALTH SCAN (ECM, TCM, ABS, BCM, SDM)", "normal_range": "Semua Modul Terdeteksi & Merespons", "unit": "Status"},
            {"parameter": "BUS OFF / LOST COMMUNICATION COUNTER", "normal_range": "0 Error Aktif", "unit": "Count"},
        ],
    },

    "tcm_at": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_mod_tcm",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Oli ATF & Konektor Transmisi)",
                "title": "Periksa Level/Kualitas Oli ATF 3317, Bersihkan Soket Transmisi & Setel Switch Tuas",
                "desc": "Oli ATF kotor/kurang atau soket luar transmisi kemasukan air/oli sering memicu DTC solenoid & range switch. Cek juga setelan kabel tuas P-R-N-D-3-2-L.",
            },
            {
                "tag": "Opsi 2 • Ukur Tahanan Solenoid / Sensor Transmisi",
                "title": "Ukur Tahanan Shift Solenoid (11–15 Ω @ 20°C) / Sensor Kecepatan & Ganti Jika Rusak",
                "desc": "Ukur tahanan kumparan solenoid atau sensor suhu/kecepatan transmisi dari soket TCM E92. Ganti solenoid/valve body bila tahanan di luar spesifikasi atau macet.",
            },
            {
                "tag": "Opsi 3 • Cek Suplai Daya TCM & Jalur Harness",
                "title": "Periksa Suplai +12V TCM (E92-06), Ground (E92-01/23) & Hapus DTC TCM + ECM",
                "desc": "Pastikan tegangan kerja TCM normal dan kabel dari TCM ke bodi transmisi tidak putus/korslet, lalu tes jalan perpindahan gigi 1→2→3→4.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai Daya Utama TCM E92-06 (IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tahanan Shift Solenoid A/B / TCC (Pada 20°C)", "normal_range": "11.0 – 15.0", "unit": "Ohm"},
            {"parameter": "Ground Modul TCM E92-01 & E92-23 (Kunci OFF)", "normal_range": "< 1.0 (< 0.3 V IG ON)", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Shift Solenoid di Posisi P/N Saat Idle Panas", "normal_range": "Sesuai logika gigi (0–1 V OFF · 9–14 V ON)", "unit": "V DC"},
            {"parameter": "Level & Kondisi Oli ATF (Mesin Idle Panas 70–80°C, Posisi P)", "normal_range": "Di antara tanda HOT dipstick · Merah jernih", "unit": "Visual"},
        ],
        "scanner_standards": [
            {"parameter": "SHIFT POSITION / TR SWITCH (P-R-N-D-3-2-L)", "normal_range": "Sesuai tepat posisi fisik tuas transmisi", "unit": "Status"},
            {"parameter": "ATF TEMPERATURE (Idle Panas)", "normal_range": "60 – 90 °C", "unit": "°C"},
            {"parameter": "INPUT / OUTPUT SHAFT SPEED (Idle Posisi P)", "normal_range": "≈ Engine RPM (Input) · 0 RPM (Output)", "unit": "RPM"},
        ],
    },

    "abs_ebd": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_mod_abs",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Bersihkan Sensor Roda & Ring Encoder)",
                "title": "Bersihkan Ujung Wheel Speed Sensor & Ring Magnetik Bearing dari Serbuk Besi",
                "desc": "Serbuk besi kampas rem menempel di magnet sensor atau bearing roda oblak adalah penyebab paling umum DTC C10xx. Bersihkan & cek celah dudukan knuckle.",
            },
            {
                "tag": "Opsi 2 • Cek Kabel Roda & Ganti Wheel Speed Sensor",
                "title": "Periksa Kabel Sensor Roda (Area Belok/Suspensi) & Ganti Sensor Jika Putus",
                "desc": "Kabel sensor roda depan sering putus di dalam karena sering menekuk saat belok; ukur sinyal/kontinuitas dari soket ABS E03 dan ganti sensor jika rusak.",
            },
            {
                "tag": "Opsi 3 • Sekering ABS, Ground & Modul Hidrolik",
                "title": "Periksa Sekering ABS 40A/25A/15A, Ground E03-01 & Lakukan Uji Jalan",
                "desc": "Pastikan suplai +B (E03-13/26) & IG1 (E03-07) normal 10–14V, hapus DTC, dan jalankan mobil > 20 km/jam untuk memverifikasi lampu ABS padam.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai Daya Modul ABS E03-07 (IG1) & E03-13/26 (+B)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tahanan Ground Bodi Modul ABS E03-01 (Kunci OFF)", "normal_range": "< 1.0", "unit": "Ohm"},
            {"parameter": "Kontinuitas Kabel Sensor Roda ke Soket Modul ABS E03", "normal_range": "< 2.0 (Tidak korslet massa)", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Kerja Modul ABS Saat Mesin Idle", "normal_range": "13.5 – 14.5", "unit": "V DC"},
            {"parameter": "Status Lampu Indikator ABS & Rem di Speedometer (Setelah Start)", "normal_range": "Menyala 2 detik lalu PADAM", "unit": "Indikator"},
        ],
        "scanner_standards": [
            {"parameter": "WHEEL SPEED FL / FR / RL / RR (Berhenti → Jalan 20 km/jam)", "normal_range": "0 km/jam (Diam) · Ke-4 roda sama saat lurus (±1 km/jam)", "unit": "km/jam"},
            {"parameter": "ABS MOTOR RELAY & VALVE RELAY (Idle)", "normal_range": "OFF (Motor) · ON (Valve Standby)", "unit": "Status"},
            {"parameter": "STOP LAMP SWITCH (Dilepas / Ditekan)", "normal_range": "OFF ↔ ON", "unit": "Status"},
        ],
    },

    "srs_airbag": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_mod_srs",
        "repair_options": [
            {
                "tag": "Opsi 1 • WAJIB SOP KESELAMATAN SRS",
                "title": "Cabut Kabel Negatif Aki & Tunggu ≥ 90 Detik — Cek Soket Kuning & Clock Spring",
                "desc": "DILARANG mengukur tahanan langsung pada inflator airbag! Cabut aki ≥ 90 detik, periksa soket kuning yang kendor/pin miring, dan uji kontinuitas kabel spiral kemudi (contact coil) secara terpisah.",
            },
            {
                "tag": "Opsi 2 • Ganti Contact Coil / Sensor Crash / Pretensioner",
                "title": "Ganti Clock Spring (Contact Coil) Putus atau Sensor/Sabuk Pretensioner Rusak",
                "desc": "Bila tombol klakson/audio setir ikut mati (B1031/B1032), clock spring hampir pasti putus; ganti unit baru dan pastikan posisi tengah (center mark) tepat.",
            },
            {
                "tag": "Opsi 3 • Cek Suplai SDM G47-16 & Evaluasi Modul SDM",
                "title": "Periksa Sekering AIR BAG, Suplai G47-16 (≥ 8V) & Ground G47-20 (< 1 Ω)",
                "desc": "Bila airbag pernah mengembang (B1021) atau error internal SDM (B1013), wajib ganti modul SDM & komponen terpicu sesuai prosedur pabrik.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai Daya Modul SDM G47-16 (BLK/WHT · Sikring AIR BAG, IG ON)", "normal_range": "≥ 8.0 (Normal 10 – 14 V)", "unit": "V DC"},
            {"parameter": "Ground Utama Modul SDM G47-20 (BLK ke Bodi, Kunci OFF)", "normal_range": "< 1.0", "unit": "Ohm"},
            {"parameter": "PERINGATAN OHMMETER PADA INFLATOR AIRBAG / PRETENSIONER", "normal_range": "DILARANG UKUR OHM! (Gunakan Scanner/Resistor Dummy)", "unit": "SAFETY"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Suplai Modul SDM G47-16 Saat Mesin Idle", "normal_range": "13.5 – 14.5", "unit": "V DC"},
            {"parameter": "Lampu Indikator AIR BAG di Speedometer (Setelah IG ON)", "normal_range": "Berkedip 6 kali lalu PADAM", "unit": "Indikator"},
        ],
        "scanner_standards": [
            {"parameter": "DRIVER / PASSENGER INFLATOR RESISTANCE (Via Scanner SDM)", "normal_range": "1.8 – 3.5 Ω (Dibaca Aman oleh SDM)", "unit": "Ohm"},
            {"parameter": "SDM BATTERY VOLTAGE (Live Data SDM)", "normal_range": "11.5 – 14.5 V", "unit": "V"},
            {"parameter": "CRASH DATA / DEPLOYMENT STATUS", "normal_range": "NO CRASH / NOT DEPLOYED", "unit": "Status"},
        ],
    },

    "hvac_ac": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_mod_hvac",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Bersihkan Sensor & Cek Motor Damper)",
                "title": "Bersihkan Sensor Suhu Kabin/Ambient/Sunload dari Debu & Cek Gerak Motor Damper",
                "desc": "Debu menyumbat kisi sensor suhu kabin atau gear motor damper (air mix / mode) macet adalah penyebab utama DTC B15xx. Bersihkan & uji gerak damper.",
            },
            {
                "tag": "Opsi 2 • Ukur & Ganti Sensor / Aktuator HVAC",
                "title": "Ukur Tahanan Termistor Sensor Suhu / Potensiometer Damper & Ganti Jika Rusak",
                "desc": "Bandingkan tahanan sensor terhadap suhu aktual (tipikal ~1,7–2,5 kΩ @ 25°C); ganti sensor atau motor aktuator damper bila putus/menyimpang.",
            },
            {
                "tag": "Opsi 3 • Cek Soket Panel Auto A/C (G52) & Suplai +5V",
                "title": "Periksa Suplai +12V (G52-01/02), Referensi +5V (G52-14) & Jalur Kabel HVAC",
                "desc": "Pastikan soket modul kontrol Auto A/C (G52) terpasang rapat, tegangan +5V normal, lalu reset DTC via self-diagnosis/scanner.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai Daya Modul HVAC G52-01 (IG ON) & G52-02 (+B)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tegangan Referensi +5V Sensor/Potensiometer HVAC (G52-14)", "normal_range": "4.0 – 6.0", "unit": "V DC"},
            {"parameter": "Tahanan Termistor Sensor Suhu Kabin / Evap (@ 25°C)", "normal_range": "1.6 – 2.6", "unit": "kOhm"},
        ],
        "idle_standards": [
            {"parameter": "Suhu Hembusan Kisi Tengah AC Saat Idle (AC ON Max Cool)", "normal_range": "6 – 12 °C (Tergantung suhu luar)", "unit": "°C"},
            {"parameter": "Sinyal Potensiometer Air Mix Damper (Full Cold → Full Hot)", "normal_range": "Berubah mulus ~0.5 V → ~4.5 V", "unit": "V DC"},
        ],
        "scanner_standards": [
            {"parameter": "INSIDE / AMBIENT / EVAPORATOR TEMP (Live Data HVAC)", "normal_range": "Sesuai suhu aktual (tidak –40°C / +80°C)", "unit": "°C"},
            {"parameter": "SUNLOAD SENSOR (Teduh → Sinar Matahari Langsung)", "normal_range": "Naik responsif saat disinari senter/matahari", "unit": "W/m² / V"},
            {"parameter": "AIR MIX / MODE ACTUATOR POSITION", "normal_range": "Mengikuti setelan tombol panel AC", "unit": "% / V"},
        ],
    },

    "bcm_body": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_mod_bcm",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Sekering, Bohlam/Switch & Baterai Remote)",
                "title": "Periksa Sekering Kabin, Switch Pintu/Lampu & Baterai Remote Kunci",
                "desc": "Periksa sekering terkait di Junction Block, kontak switch pintu/kunci, dan pastikan tidak ada aksesori aftermarket yang membebani sirkuit BCM.",
            },
            {
                "tag": "Opsi 2 • Cek Soket BCM & Jalur CAN/LIN",
                "title": "Periksa Konektor Modul BCM (G51/E82), Suplai +B/+IG & Titik Ground Kabin",
                "desc": "Pastikan konektor BCM di bawah dasbor kering bebas rembesan air kaca depan dan kabel komunikasi CAN ke ECM/meter tidak putus.",
            },
            {
                "tag": "Opsi 3 • Registrasi Ulang / Evaluasi BCM",
                "title": "Hapus DTC BCM & Uji Fungsi Beban via Active Test Scanner",
                "desc": "Uji aktivasi lampu/central lock/wiper via scanner; evaluasi penggantian BCM hanya jika seluruh jalur eksternal normal.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai Daya Utama BCM (+B & IG1)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tahanan Ground Bodi Modul BCM (Kunci OFF)", "normal_range": "< 1.0", "unit": "Ohm"},
        ],
        "idle_standards": [
            {"parameter": "Tegangan Kerja BCM Saat Mesin Idle", "normal_range": "13.5 – 14.5", "unit": "V DC"},
            {"parameter": "Status Respon Lampu / Central Lock / Wiper", "normal_range": "Bekerja responsif tanpa kedip abnormal", "unit": "Fungsi"},
        ],
        "scanner_standards": [
            {"parameter": "BCM BATTERY VOLTAGE & IG1 STATUS", "normal_range": "12.0–14.5 V · IG1 ON", "unit": "V"},
            {"parameter": "DOOR / LIGHT / KEY SWITCH INPUTS", "normal_range": "Berubah ON/OFF sesuai saklar fisik", "unit": "Status"},
        ],
    },

    "icm_immo_kscm": {
        "sim_circuit_key": "dynamic",
        "atlas_module_id": "gv_mod_icm",
        "repair_options": [
            {
                "tag": "Opsi 1 • Utama (Cek Kunci Cadangan & Baterai Remote)",
                "title": "Uji Coba Kunci Cadangan Asli & Ganti Baterai Smart Key (CR2032)",
                "desc": "Coba start dengan kunci cadangan asli tanpa gantungan logam berat. Untuk Keyless (KSCM), ganti baterai CR2032 (≥ 3.0V) dan dekatkan fob ke tombol/rumah kunci.",
            },
            {
                "tag": "Opsi 2 • Cek Antena Cincin Immobilizer / Antena Keyless",
                "title": "Periksa Soket Antena Immobilizer (Rumah Kunci) & Jalur E23-13 (PNK/BLU) / E23-28 (GRY/BLU)",
                "desc": "Pastikan soket antena coil di sekitar lubang kunci kontak terpasang rapat, tegangan suplai +12V normal, dan kabel komunikasi ke ECM tidak putus.",
            },
            {
                "tag": "Opsi 3 • Registrasi Ulang Transponder / Sinkronisasi ECM–ICM",
                "title": "Lakukan Registrasi Kunci Transponder & Sinkronisasi ID ECM–ICM via Scanner",
                "desc": "Registrasikan ulang ID kunci bila memori hilang atau pasca penggantian ECM/ICM/KSCM, lalu pastikan lampu ikon kunci di speedometer padam.",
            },
        ],
        "static_specs": [
            {"parameter": "Suplai Daya Antena Immobilizer / Modul KSCM (IG ON)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Jalur Clock E23-13 (PNK/BLU) & Data E23-28 (GRY/BLU · IG ON, Bab 1A-205/206)", "normal_range": "10.0 – 14.0", "unit": "V DC"},
            {"parameter": "Tegangan Baterai Remote Smart Key (CR2032)", "normal_range": "≥ 3.0", "unit": "V DC"},
        ],
        "idle_standards": [
            {"parameter": "Status Lampu Indikator Kunci / Immobilizer (Setelah IG ON / Start)", "normal_range": "PADAM (Tidak berkedip)", "unit": "Indikator"},
            {"parameter": "Izin Injeksi & Pengapian ECM", "normal_range": "Aktif normal (Mesin hidup stabil)", "unit": "Status"},
        ],
        "scanner_standards": [
            {"parameter": "IMMOBILIZER / TRANSPONDER MATCH STATUS", "normal_range": "MATCHED / OK (Kunci Terdaftar ≥ 1)", "unit": "Status"},
            {"parameter": "ECM – ICM / KSCM COMMUNICATION", "normal_range": "NORMAL / VERIFIED", "unit": "Status"},
        ],
    },
}


def pick_profile_key(code: str, sys_cat: str, desc: str) -> str:
    c = code.upper().strip()
    sc = (sys_cat or "").lower()
    ds = (desc or "").lower()

    if c in ("P0400", "P0401", "P0402", "P0403", "P0404", "P0405", "P0406") or "egr" in ds or "daur ulang gas buang" in ds:
        return "egr_control"
    if c in ("P0443", "P0444", "P0445") or "evaporative" in ds or "purge" in ds:
        return "evap_purge"
    if c == "P0660" or "intake manifold tuning" in ds or "imt" in ds:
        return "imt_valve"
    if re.match(r"^P030[0-8]$|^P035[1-8]$", c):
        return "ign_coil"
    if re.match(r"^P033[5-9]$", c) or "crankshaft" in ds:
        return "ckp"
    if re.match(r"^P034[0-9]$", c) or "camshaft" in ds:
        return "cmp"
    if re.match(r"^P010[0-4]$|^P011[0-4]$", c) or "mass air flow" in ds or "intake air temp" in ds:
        return "maf_iat"
    if re.match(r"^P010[5-9]$|^P222[7-9]$", c) or "manifold absolute pressure" in ds or "barometric" in ds:
        return "map_baro"
    if re.match(r"^P011[5-9]$|^P012[58]$", c) or "coolant temp" in ds:
        return "ect"
    if c in ("P0030", "P0031", "P0032", "P0131", "P0132", "P0133", "P0134") or ("sensor-1" in ds and ("o2" in ds or "ho2s" in ds or "a/f" in ds)):
        return "af_sensor1"
    if c in ("P0036", "P0037", "P0038", "P0136", "P0137", "P0138", "P0140", "P0141") or ("sensor-2" in ds and ("o2" in ds or "ho2s" in ds)):
        return "ho2s2"
    if re.match(r"^P012[0-4]$|^P022[0-3]$|^P0507$|^P21[0-3][0-9]$", c) or "throttle" in ds or "pedal position" in ds:
        return "etc_tps_app"
    if re.match(r"^P048[0-5]$", c) or "kipas radiator" in ds or "cooling fan" in ds:
        return "cooling_fan"
    if c in ("P0327", "P0328") or "knock" in ds:
        return "knock"
    if c in ("P0171", "P0172", "P2195", "P2196") or "terlalu kurus" in ds:
        return "fuel_trim_nonwiring"
    if c == "P0420" or "catalyst" in ds:
        return "catalyst_nonwiring"
    if c in ("P0620", "P0625", "P0626", "P1501", "P1502") or "generator" in ds or "electric load current" in ds:
        return "charging_elc"
    if c in ("P0616", "P0617") or "relay starter" in ds:
        return "starter_relay"
    if c in ("P0462", "P0463") or "fuel level" in ds:
        return "fuel_level"
    if c in ("P0500", "P0504", "P0532", "P0533") or "vehicle speed" in ds or "switch rem" in ds or "refrigerant pressure" in ds:
        return "vss_brake_ac"
    if c in ("P0601", "P0602", "P0607", "P1510") or "memori internal" in ds or "back-up power" in ds:
        return "ecm_power"
    if c in ("P1674", "P1676", "P1678", "P1685", "U1073", "U1100") or c.startswith("U") or "komunikasi can" in ds:
        return "can_bus"
    if c == "P1603" or re.match(r"^P0[789]|^P1[78]|^P27", c) or "transmission" in sc or "tcm" in sc:
        return "tcm_at"
    if c.startswith("C10") or "antilock" in sc or "abs" in sc:
        return "abs_ebd"
    if c.startswith("B10") or "supplemental restraint" in sc or "srs" in sc or "air bag" in sc:
        return "srs_airbag"
    if c.startswith("B15") or "air conditioner" in sc or "hvac" in sc:
        return "hvac_ac"
    if c.startswith("B11") or "body electrical" in sc or "bcm" in sc:
        return "bcm_body"
    if c.startswith("P16") or c.startswith("KLS") or "immobilizer" in sc or "keyless" in sc or "icm" in sc or "kscm" in sc:
        return "icm_immo_kscm"
    return "ecm_power"


def main() -> None:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    catalog = data.get("dtc_catalog", [])
    counts: dict[str, int] = {}

    for entry in catalog:
        code = str(entry.get("code", "")).upper().strip()
        sys_cat = str(entry.get("system_category", ""))
        desc = clean_pdf_text(str(entry.get("description_id", "")))
        entry["description_id"] = desc
        entry["common_causes"] = clean_pdf_text(str(entry.get("common_causes", "")))
        entry["recommended_fix"] = clean_pdf_text(str(entry.get("recommended_fix", "")))
        entry["repair_steps"] = [clean_pdf_text(s) for s in (entry.get("repair_steps") or []) if str(s).strip()]
        entry["remedies"] = [clean_pdf_text(r) for r in (entry.get("remedies") or []) if str(r).strip()]

        for p in entry.get("wiring_pinout") or []:
            if isinstance(p, dict):
                p["signal"] = clean_pdf_text(str(p.get("signal", "")))
                p["function"] = clean_pdf_text(str(p.get("function", "")))

        pkey = pick_profile_key(code, sys_cat, desc)
        counts[pkey] = counts.get(pkey, 0) + 1
        prof = PROFILES[pkey]

        # Set explicit wiring simulator key & Pilar 3 atlas link
        entry["sim_circuit_key"] = prof["sim_circuit_key"]
        entry["atlas_module_id"] = prof["atlas_module_id"]
        if pkey == "icm_immo_kscm" and ("keyless" in sys_cat.lower() or code.startswith("KLS")):
            entry["atlas_module_id"] = "gv_mod_kscm"

        # Set curated, realistic workshop repair_options (Option 1 = component service/clean/test!)
        entry["curated_repair_options"] = prof["repair_options"]

        # Clean & upgrade 3-tier OEM standards:
        # 1. Static specs (replace truncated >=85-char PDF dumps with crisp OEM static specs!)
        existing_specs = entry.get("standard_specs") or []
        clean_existing = []
        for sp in existing_specs:
            if isinstance(sp, dict):
                param = clean_pdf_text(str(sp.get("parameter", "")))
                rng = clean_pdf_text(str(sp.get("normal_range", "")))
                unit = clean_pdf_text(str(sp.get("unit", "V")))
                if param and len(param) < 78 and not param.lower().startswith("dengan kunci kontak"):
                    clean_existing.append({"parameter": param, "normal_range": rng, "unit": unit})
        # Use crisp OEM static specs from profile as authoritative base (merging unique clean OEM measurements if useful)
        static_specs = [dict(x) for x in prof["static_specs"]]
        for cs in clean_existing:
            if len(static_specs) >= 4:
                break
            if not any(cs["parameter"][:22].lower() in x["parameter"].lower() for x in static_specs):
                static_specs.append(cs)
        entry["standard_specs"] = static_specs[:4]

        # 2. Idle measurement standards (Mesin Hidup · Idle Panas Kerja 80–90°C)
        entry["idle_standards"] = [dict(x) for x in prof["idle_standards"]]

        # 3. Scanner OBD-II Live Data & Active Test standards (Bab 1A-34..36)
        entry["scanner_standards"] = [dict(x) for x in prof["scanner_standards"]]

    CATALOG_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SUKSES] Enriched {len(catalog)} JB420 DTCs in {CATALOG_PATH.name}")
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {v:3d} | {k}")


if __name__ == "__main__":
    main()
