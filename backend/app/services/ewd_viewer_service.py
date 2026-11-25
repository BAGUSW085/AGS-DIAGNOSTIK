"""
Router Multi-Merek Wiring Diagram & Alur Sinyal Interaktif (AGOS Smart Diagnostik)
==================================================================================
Mendukung:
1. Toyota GSIC `.svgz` + graf koneksi `connect/*.xml` (338+ sistem siap X-Ray & animasi aliran otomatis)
2. Alur Sinyal Berantai Langkah-demi-Langkah (Mode Junior & Mode Senior + Kartu Anti-Salah)
   untuk Toyota (1KD/2KD, 2TR-FE, CAN Bus, Immobiliser) dan Suzuki (Grand Vitara JB420 & Ertiga K14B)
3. Pembuka PDF Vektor Asli (Avanza EWD PDF & Suzuki Grand Vitara / Ertiga PDF langsung ke nomor halaman)

Arsitektur BYOD / Local-Only:
Seluruh file manual OEM dibaca dari `backend/local_ewd_cache/` (diabaikan oleh .gitignore)
atau folder lokal bengkel — tidak pernah dibundel ke repositori publik.
"""

from __future__ import annotations

import gzip
import json
import re
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(tags=["Wiring Diagram & Alur Sinyal Interaktif"])

BACKEND_DIR = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = BACKEND_DIR.parent
STATIC_DIR = BACKEND_DIR / "app" / "static"
CACHE_ROOT = BACKEND_DIR / "local_ewd_cache"
INDEX_FILE = CACHE_ROOT / "ewd_index.json"
CUSTOM_PACKS_FILE = BACKEND_DIR / "app" / "data" / "custom_manual_packs.json"


# =============================================================================
# 1. CURATED END-TO-END SIGNAL CHAINS (TOYOTA & SUZUKI — OEM VERIFIED)
# =============================================================================
CURATED_SIGNAL_CHAINS: dict[str, dict[str, Any]] = {
    "toyota_ckp_to_inj": {
        "chain_id": "toyota_ckp_to_inj",
        "brand": "Toyota",
        "label": "Toyota 1KD/2KD — CKP (C5) → ECM → EDU (+12V & INJF) → Injektor & Massa EE",
        "render_mode": "toyota_svgz",
        "model_id": "toyota_fortuner_2005",
        "sys_code": "ECS-1KD",
        "scope": "Fortuner / Innova / Hilux 1KD-FTV & 2KD-FTV (EM00M4E)",
        "stages": [
            {
                "shortLabel": "1. CKP → ECM",
                "cat": "INPUT",
                "badge": "🔵 INPUT PULSA AC",
                "title": "Sensor CKP (C5-B) mengirim sinyal putaran RPM & posisi TMA ke Engine ECU (E7)",
                "direction": "Sensor CKP (C5-B) ──▶ Engine ECU (E7-27 & E7-34)",
                "fromNodes": ["C5"],
                "toNodes": ["E7"],
                "lineIds": ["108", "109"],
                "func": "Gigi rotor kruk as memotong magnet sensor CKP sehingga menghasilkan pulsa AC (NE+ / NE-). ECM membaca pulsa ini untuk menghitung RPM dan menentukan saat tepat penyemprotan solar.",
                "prereq": "Prasyarat 1KD/2KD: Sinyal CKP ini wajib sinkron dengan Sensor CMP (C1, E6-23/31) & Immobiliser tidak terkunci agar mesin mau menyemprot.",
                "asKey": "Cranking / Idle (Soket Terpasang)",
                "asTool": "Scanner DLC3 / Osiloskop",
                "asSpec": "50–400 rpm (Start) • 700–800 (Idle)",
                "wires": [
                    {"lineId": "108", "color": "Y", "from": "C5-1 (NE+)", "to": "E7-27 (NE+)", "role": "Pulsa Positif Putaran Kruk As (DTC P0335)"},
                    {"lineId": "109", "color": "L", "from": "C5-2 (NE-)", "to": "E7-34 (NE-)", "role": "Pulsa Negatif / Referensi Sensor CKP"},
                ],
                "nextHandoff": "Lanjut Tahap 2: Cek kabel pelindung (Shield) CKP & massa utama Engine ECU menuju baut blok mesin EE.",
            },
            {
                "shortLabel": "2. Shield & Massa EE",
                "cat": "GROUND",
                "badge": "⚫ GROUND & SHIELD",
                "title": "Pelindung Noise CKP (C5-3) & Massa Utama ECM (E7-6/7) → Titik Massa EE",
                "direction": "C5-3 → Splice 14881 | E7-6/7 (E02/E01) → Splice 14821 ──▶ Massa Akhir EE",
                "fromNodes": ["C5", "E7"],
                "toNodes": ["EE", "14821", "14881"],
                "lineIds": ["105", "110", "116", "112"],
                "func": "Kabel shield (C5-3) membuang gangguan listrik agar sinyal AC CKP tidak cacat, sedangkan E01 & E02 menutup rangkaian ground utama ECM ke baut massa akhir blok mesin (EE).",
                "prereq": "",
                "asKey": "IG OFF, Soket ECM Lepas",
                "asTool": "Multimeter Mode Ohm (Ω)",
                "asSpec": "< 1 Ω ke Negatif Aki",
                "wires": [
                    {"lineId": "105", "color": "W-B", "from": "C5-3 (Shield E)", "to": "Splice 14881", "role": "Selubung Anti-Noise CKP"},
                    {"lineId": "110", "color": "W", "from": "E7-6 (E02)", "to": "Splice 14821", "role": "Massa Driver Engine ECU"},
                    {"lineId": "116", "color": "W-B", "from": "E7-7 (E01)", "to": "Splice 14821", "role": "Massa Utama Engine ECU"},
                    {"lineId": "112", "color": "W-B", "from": "Splice 14821", "to": "Titik Massa EE", "role": "Kabel Akhir ke Baut Blok Mesin (EE)"},
                ],
                "nextHandoff": "Lanjut Tahap 3: Setelah CKP + CMP + Ground beres, ECM mengirim 4 jalur perintah semprot (#1–#4) ke modul EDU (I6).",
            },
            {
                "shortLabel": "3. ECM → EDU (#1–#4)",
                "cat": "OUTPUT",
                "badge": "🟠 OUTPUT PERINTAH 5V",
                "title": "Engine ECU (E7) mengirim pulsa perintah semprot #1–#4 ke EDU (I6)",
                "direction": "Engine ECU (E7-24, 23, 22, 21) ──▶ EDU (I6-6, 3, 2, 5)",
                "fromNodes": ["E7"],
                "toNodes": ["I6"],
                "lineIds": ["58", "59", "61", "63"],
                "func": "ECM mengubah timing dari CKP menjadi 4 pulsa pemicu 5V menuju EDU sesuai urutan injeksi 1-3-4-2. EDU yang memperkuatnya menjadi tegangan tinggi untuk membuka injektor.",
                "prereq": "",
                "asKey": "IG OFF, Soket E7 & I6 Lepas",
                "asTool": "Multimeter Mode Ohm (Ω)",
                "asSpec": "Kontinuitas < 1 Ω • Isolasi ≥ 10 kΩ",
                "wires": [
                    {"lineId": "58", "color": "B-W", "from": "E7-24 (#1)", "to": "I6-6 (#10)", "role": "Perintah Injektor Silinder 1"},
                    {"lineId": "59", "color": "R", "from": "E7-23 (#2)", "to": "I6-3 (#20)", "role": "Perintah Injektor Silinder 2"},
                    {"lineId": "61", "color": "V", "from": "E7-22 (#3)", "to": "I6-2 (#30)", "role": "Perintah Injektor Silinder 3"},
                    {"lineId": "63", "color": "Y-R", "from": "E7-21 (#4)", "to": "I6-5 (#40)", "role": "Perintah Injektor Silinder 4"},
                ],
                "nextHandoff": "Lanjut Tahap 4 (KRUSIAL): Cek Suplai +12V EDU (I5-8), Massa EDU (I6-1 → EE), dan Konfirmasi Balik INJF.",
            },
            {
                "shortLabel": "4. +12V EDU, INJF & GND",
                "cat": "FEEDBACK",
                "badge": "🟣 DAYA +12V & FEEDBACK",
                "title": "Suplai +12V EDU (I5-8), Massa EDU (EE), & Balasan INJF ke ECM (E7-25)",
                "direction": "EA1-2 (+12V) ──▶ EDU I5-8 | EDU I6-7 (INJF) ──▶ ECM E7-25 | I6-1 ──▶ Massa EE",
                "fromNodes": ["I6", "I5", "EA1"],
                "toNodes": ["E7", "EE"],
                "lineIds": ["53", "57", "55"],
                "func": "Kabel Hitam I5-8 adalah sumber +12V utama dari Relay EDU (sering jadi penyebab mesin mati total). Kabel Pink INJF melapor balik ke ECM bahwa injektor sukses terbuka; jika putus memicu DTC P0200 & mesin langsung mati.",
                "prereq": "Tip Senior: Sebelum memvonis EDU mahal rusak, pastikan I5-8 (+12V) ada 11–14V saat IG ON & I6-1 → EE < 1 Ω.",
                "asKey": "IG ON (+12V I5-8) / IG OFF (GND & INJF)",
                "asTool": "DC Volt (I5-8) & Ohm (I6-1/I6-7)",
                "asSpec": "I5-8: 11–14 V • GND/INJF: < 1 Ω",
                "wires": [
                    {"lineId": "53", "color": "B", "from": "EA1-2 (Relay EDU)", "to": "I5-8 (+B EDU)", "role": "Suplai Daya +12V Utama Modul EDU"},
                    {"lineId": "57", "color": "P", "from": "I6-7 (INJF)", "to": "E7-25 (INJF)", "role": "Sinyal Konfirmasi Balik Injeksi (EDU → ECM)"},
                    {"lineId": "55", "color": "W-B", "from": "I6-1 (GND)", "to": "Titik Massa EE", "role": "Massa Arus Tinggi EDU ke Blok Mesin (EE)"},
                ],
                "nextHandoff": "Lanjut Tahap 5 (Ujung Akhir): Daya tinggi ~85–110V DC dari EDU I5 menuju 4 Injektor Solar (F4–F7).",
            },
            {
                "shortLabel": "5. Kabel Akhir Injektor",
                "cat": "POWER",
                "badge": "🔴 TEGANGAN TINGGI (~85–110V)",
                "title": "Kabel Akhir Aktuator: EDU I5 ↔ Junction J12 ↔ 4 Injektor Solar (F4–F7)",
                "direction": "EDU I5 (COM1/COM2) ──▶ J12 ──▶ Injektor F4–F7 (Pin 1) ──▶ Balik ke EDU I5 (INJ1–4)",
                "fromNodes": ["I5", "J12"],
                "toNodes": ["F4", "F5", "F6", "F7"],
                "lineIds": ["66", "80", "70", "74", "84", "86", "69", "81", "87", "75"],
                "func": "Ujung akhir rantai CKP: EDU menembakkan ~85–110V DC melalui COM1 (Silinder 1&4) dan COM2 (Silinder 2&3) via J12, lalu mengontrol bukaan solenoid tiap injektor lewat INJ1–INJ4.",
                "prereq": "BAHAYA TEGANGAN TINGGI (~85–110V): Dilarang mengukur mode Ohm (Ω) saat mesin hidup / IG ON! Cabut soket dahulu.",
                "asKey": "WAJIB IG OFF & Soket Lepas!",
                "asTool": "Multimeter Mode Ohm (Ω)",
                "asSpec": "Harness < 1 Ω • Isolasi ≥ 10 kΩ",
                "wires": [
                    {"lineId": "66", "color": "R-B", "from": "I5-5 (COM1)", "to": "J12-7 (Inj 1 & 4)", "role": "Suplai HV Bersama Silinder 1 & 4"},
                    {"lineId": "80", "color": "L-W", "from": "I5-6 (COM2)", "to": "J12-10 (Inj 2 & 3)", "role": "Suplai HV Bersama Silinder 2 & 3"},
                    {"lineId": "69", "color": "W", "from": "F4-2 (Injektor #1)", "to": "I5-4 (INJ1)", "role": "Kontrol Solenoid Silinder 1"},
                    {"lineId": "81", "color": "P", "from": "F5-2 (Injektor #2)", "to": "I5-2 (INJ2)", "role": "Kontrol Solenoid Silinder 2"},
                    {"lineId": "87", "color": "L", "from": "F6-2 (Injektor #3)", "to": "I5-1 (INJ3)", "role": "Kontrol Solenoid Silinder 3"},
                    {"lineId": "75", "color": "G", "from": "F7-2 (Injektor #4)", "to": "I5-3 (INJ4)", "role": "Kontrol Solenoid Silinder 4"},
                ],
                "nextHandoff": "Rantai Selesai: Sensor CKP → ECM → +12V/INJF EDU → Injektor F4–F7 & Massa Akhir EE.",
            },
        ],
    },
    "toyota_rail_to_scv": {
        "chain_id": "toyota_rail_to_scv",
        "brand": "Toyota",
        "label": "Toyota 1KD/2KD — Sensor Rail (F8) → ECM → Katup SCV (S8) [Tekanan Solar]",
        "render_mode": "toyota_svgz",
        "model_id": "toyota_fortuner_2005",
        "sys_code": "ECS-1KD",
        "scope": "Fortuner / Innova / Hilux 1KD-FTV & 2KD-FTV (EM00M4E)",
        "stages": [
            {
                "shortLabel": "1. +5V Sensor Rail",
                "cat": "POWER",
                "badge": "🔴 SUPLAI +5V & E2",
                "title": "Suplai Referensi +5V (VC) & Massa (E2) menuju Sensor Tekanan Rail (F8)",
                "direction": "J7-19 (VC +5V) & J9-7 (E2) ──▶ Sensor Common-Rail (F8-3 & F8-1)",
                "fromNodes": ["J7", "J9"],
                "toNodes": ["F8"],
                "lineIds": ["83", "78"],
                "func": "Memberi tegangan referensi stabil +5V DC agar elemen sensor tekanan pada pipa Common-Rail dapat bekerja akurat.",
                "prereq": "",
                "asKey": "IG ON, Soket F8 Lepas/Back-Probe",
                "asTool": "Multimeter DC Volt (V)",
                "asSpec": "4,5 – 5,5 V DC",
                "wires": [
                    {"lineId": "83", "color": "R-W", "from": "J7-19 (VC)", "to": "F8-3 (VC)", "role": "Suplai Referensi +5V DC"},
                    {"lineId": "78", "color": "BR", "from": "J9-7 (E2)", "to": "F8-1 (E2)", "role": "Massa Referensi Sensor"},
                ],
                "nextHandoff": "Lanjut Tahap 2: Sensor F8 mengirim balik sinyal tegangan tekanan solar aktual (PR) ke ECM.",
            },
            {
                "shortLabel": "2. Sinyal PR → ECM",
                "cat": "INPUT",
                "badge": "🔵 INPUT SINYAL 0–5V",
                "title": "Sensor F8 mengirim sinyal tekanan aktual Common-Rail ke ECM (E7-26)",
                "direction": "Sensor Common-Rail (F8-2) ──▶ Engine ECU (E7-26 PR)",
                "fromNodes": ["F8"],
                "toNodes": ["E7"],
                "lineIds": ["85"],
                "func": "Tegangan naik seiring naiknya tekanan solar di pipa rail. ECM memakai nilai ini untuk mengatur bukaan katup SCV.",
                "prereq": "",
                "asKey": "IG ON / Idle (Soket Terpasang)",
                "asTool": "DC Volt (Back-Probe) / Scanner",
                "asSpec": "~1,0 V (IG ON) • ~1,5 V (Idle)",
                "wires": [
                    {"lineId": "85", "color": "R-Y", "from": "F8-2 (PR)", "to": "E7-26 (PR)", "role": "Sinyal Analog Tekanan Common-Rail (DTC P0190)"},
                ],
                "nextHandoff": "Lanjut Tahap 3 (Akhir): ECM memerintahkan Katup SCV (S8) mengoreksi debit solar.",
            },
            {
                "shortLabel": "3. ECM → Katup SCV",
                "cat": "OUTPUT",
                "badge": "🟠 OUTPUT PWM AKTUATOR",
                "title": "Jalur Akhir: Engine ECU (E7-1/2) mengatur debit pompa solar via SCV (S8)",
                "direction": "Engine ECU (E7-1 PCV+ & E7-2 PCV-) ──▶ Katup SCV (S8-2 & S8-1)",
                "fromNodes": ["E7"],
                "toNodes": ["S8"],
                "lineIds": ["22", "24"],
                "func": "Pulsa PWM ECM membuka/menutup plunger katup SCV pada Supply Pump untuk menjaga tekanan Common-Rail sesuai target.",
                "prereq": "",
                "asKey": "IG OFF, Soket S8 Lepas",
                "asTool": "Multimeter Mode Ohm (Ω)",
                "asSpec": "Kumparan SCV: 1,9–2,3 Ω (20°C)",
                "wires": [
                    {"lineId": "22", "color": "G-Y", "from": "E7-1 (PCV+)", "to": "S8-2", "role": "Suplai PWM Positif SCV (DTC P0088/P0093)"},
                    {"lineId": "24", "color": "G-W", "from": "E7-2 (PCV-)", "to": "S8-1", "role": "Kontrol Duty Balik SCV"},
                ],
                "nextHandoff": "Loop Selesai: Sensor Rail F8 → ECM E7 → Katup SCV S8.",
            },
        ],
    },
    "toyota_ign_2tr": {
        "chain_id": "toyota_ign_2tr",
        "brand": "Toyota",
        "label": "Toyota 2TR-FE — Sekring 15A INJ → Koil No.1 (I1) ↔ ECM (E11) → Massa EC",
        "render_mode": "toyota_svgz",
        "model_id": "toyota_fortuner_2005",
        "sys_code": "IS-2TR",
        "scope": "Fortuner / Innova 2TR-FE Bensin (EM00M4E)",
        "stages": [
            {
                "shortLabel": "1. +12V (15A INJ)",
                "cat": "POWER",
                "badge": "🔴 SUPLAI +12V IG ON",
                "title": "Daya +12V dari Sekring 15A INJ mengalir menuju Pin 1 Koil No.1 (I1)",
                "direction": "Fuse 15A INJ (2-JB) ──▶ ID1/ID3 ──▶ Koil I1 Pin 1 (+B)",
                "fromNodes": ["2-JB"],
                "toNodes": ["I1"],
                "lineIds": ["4", "3", "2"],
                "func": "Menyuplai arus primer +12V ke koil pengapian saat kunci kontak ON/START.",
                "prereq": "Varian Tahun/Transmisi: Sebelum Jul 2007 A/T lewat soket ID3; M/T & setelah Jul 2007 lewat ID1.",
                "asKey": "IG ON, Soket I1 Lepas",
                "asTool": "Multimeter DC Volt (V)",
                "asSpec": "11 – 14 V DC ke Massa",
                "wires": [
                    {"lineId": "4", "color": "R", "from": "2D-10 (15A INJ)", "to": "ID1/ID3 Pin 5", "role": "Keluaran Sekring 15A INJ"},
                    {"lineId": "3", "color": "R", "from": "ID1/ID3 Pin 5", "to": "Splice 1237", "role": "Cabang Distribusi +B 4 Koil"},
                    {"lineId": "2", "color": "R", "from": "Splice 1237", "to": "I1-1 (+B)", "role": "Suplai +12V Masuk Koil No.1"},
                ],
                "nextHandoff": "Lanjut Tahap 2: ECM mengirim sinyal pemicu IGT1 untuk memercikkan api busi.",
            },
            {
                "shortLabel": "2. Pemicu IGT1",
                "cat": "OUTPUT",
                "badge": "🟠 OUTPUT PULSA 5V",
                "title": "Engine ECU (E11-17) memicu Igniter Koil No.1 (I1-3) via IGT1",
                "direction": "Engine ECU (E11-17) ──▶ Koil No.1 (I1-3 IGT1)",
                "fromNodes": ["E11"],
                "toNodes": ["I1"],
                "lineIds": ["1"],
                "func": "Pulsa kotak 5V menyalakan & memutus transistor igniter internal koil agar tercipta loncatan api tegangan tinggi di busi.",
                "prereq": "",
                "asKey": "Mesin Idle / Cranking (Terpasang)",
                "asTool": "DC Volt / Osiloskop",
                "asSpec": "0,8–1,2 V (Pulsa 5V)",
                "wires": [
                    {"lineId": "1", "color": "R", "from": "E11-17 (IGT1)", "to": "I1-3 (IGT1)", "role": "Sinyal Pemicu Pengapian Silinder 1 (DTC P0351)"},
                ],
                "nextHandoff": "Lanjut Tahap 3: Koil mengirim laporan balik IGF ke ECM.",
            },
            {
                "shortLabel": "3. Balasan IGF",
                "cat": "FEEDBACK",
                "badge": "🟣 UMPAN BALIK IGF",
                "title": "Koil No.1 melapor balik ke ECM via jalur gabungan IGF (J13/J14 → E11-23)",
                "direction": "Koil I1-2 (IGF) ──▶ J13/J14 ──▶ Engine ECU E11-23 (IGF1)",
                "fromNodes": ["I1"],
                "toNodes": ["J13", "J14", "E11"],
                "lineIds": ["6", "21"],
                "func": "Konfirmasi pengapian sukses. Jika jalur #21 (J13 → E11-23) putus, ECM memutus injektor dan muncul P0351–P0354 bersamaan.",
                "prereq": "",
                "asKey": "IG ON / Idle (Terpasang)",
                "asTool": "Multimeter DC Volt (V)",
                "asSpec": "4,5–5,0 V (IG ON) • ~3 V (Idle)",
                "wires": [
                    {"lineId": "6", "color": "G-R", "from": "I1-2 (IGF)", "to": "J13/J14", "role": "Umpan Balik dari Koil No.1"},
                    {"lineId": "21", "color": "G-R", "from": "J13/J14", "to": "E11-23 (IGF1)", "role": "Jalur Gabungan IGF ke ECM"},
                ],
                "nextHandoff": "Lanjut Tahap 4 (Akhir): Arus primer dibuang ke Titik Massa Mesin EC.",
            },
            {
                "shortLabel": "4. Massa Akhir EC",
                "cat": "GROUND",
                "badge": "⚫ GROUND AKHIR",
                "title": "Kabel Akhir: Pembuangan Arus Koil ke Titik Massa Kepala Silinder (EC)",
                "direction": "Koil I1-4 (GND) ──▶ Cabang Massa Bersama ──▶ Titik Massa EC",
                "fromNodes": ["I1"],
                "toNodes": ["EC"],
                "lineIds": ["7", "13", "20", "25"],
                "func": "Menutup rangkaian arus primer koil ke blok mesin.",
                "prereq": "",
                "asKey": "IG OFF, Soket I1 Lepas",
                "asTool": "Multimeter Mode Ohm (Ω)",
                "asSpec": "< 1 Ω ke Negatif Aki",
                "wires": [
                    {"lineId": "7", "color": "W-B", "from": "I1-4 (GND)", "to": "Cabang Massa Koil", "role": "Massa Koil Silinder 1"},
                    {"lineId": "25", "color": "W-B", "from": "Cabang Massa Bersama", "to": "Titik Massa EC", "role": "Kabel Akhir ke Baut Massa EC"},
                ],
                "nextHandoff": "Rantai Pengapian Selesai.",
            },
        ],
    },
    "suzuki_gv_p0335": {
        "chain_id": "suzuki_gv_p0335",
        "brand": "Suzuki",
        "label": "Suzuki Grand Vitara JB420 — DTC P0335 CKP & Starter (Hal. 1A-115)",
        "render_mode": "suzuki_schematic",
        "schematic_key": "GV_P0335",
        "pdf_doc_id": "suzuki_gv_vol1",
        "pdf_page": 173,
        "scope": "Grand Vitara JB420 / J20A (Manual Hal. 1A-115)",
        "stages": [
            {
                "shortLabel": "1. Main Relay → ECM",
                "cat": "POWER",
                "badge": "🔴 DAYA UTAMA +12V",
                "title": "Suplai +12V dari Sikring \"FI\" & Main Relay menuju ECM (E23)",
                "direction": "Box Sikring #9 (FI) → Main Relay #4 ──▶ ECM E23-1/16/29/60",
                "fromNodes": ["FUSE_BOX", "MAIN_RELAY"],
                "toNodes": ["ECM"],
                "wireIds": ["GV_W1", "GV_W2", "GV_W3"],
                "func": "Saat kunci kontak ON, ECM mengaktifkan Main Relay lewat C37-22 (BLK/WHT), lalu Main Relay menyalurkan +12V via kabel Biru-Hitam (BLU/BLK) ke ECM E23.",
                "prereq": "Kenapa Cek Ini Dulu? Jika Main Relay mati atau Sikring FI putus, ECM tidak hidup sama sekali sehingga scanner gagal konek.",
                "asKey": "IG ON, Soket Terpasang",
                "asTool": "Multimeter DC Volt (V)",
                "asSpec": "10 – 14 V DC",
                "wires": [
                    {"id": "GV_W1", "from": "Sikring FI (#10)", "to": "Main Relay (#4)", "color": "BLK/RED (Hitam-Merah)", "role": "Suplai Aki +12V Masuk Main Relay"},
                    {"id": "GV_W2", "from": "Main Relay (#4)", "to": "ECM E23-1/16/29/60", "color": "BLU/BLK (Biru-Hitam)", "role": "Daya Utama +12V Menuju ECM"},
                    {"id": "GV_W3", "from": "ECM C37-22", "to": "Kumparan Main Relay", "color": "BLK/WHT (Hitam-Putih)", "role": "Kontrol Ground Aktifasi Main Relay"},
                ],
                "nextHandoff": "Lanjut Tahap 2: Putar kunci ke START → sinyal starter masuk ke ECM untuk memicu pemantauan DTC P0335.",
            },
            {
                "shortLabel": "2. Sinyal Starter",
                "cat": "INPUT",
                "badge": "🔵 SINYAL START & RELAY",
                "title": "Kunci Kontak & Relay Starter melapor \"Cranking\" ke ECM (C37-30/58)",
                "direction": "Kunci Kontak (#5) → Relay Starter (#7) ──▶ Starter (#6) & ECM C37-30/58",
                "fromNodes": ["IGN_SW", "ST_RELAY"],
                "toNodes": ["ECM", "STARTER", "TR_SW"],
                "wireIds": ["GV_W4", "GV_W5", "GV_W6", "GV_W7", "GV_W8"],
                "func": "Di Grand Vitara, ECM mendeteksi P0335 bila sinyal starting motor masuk 2 detik tetapi sinyal CKP tidak muncul.",
                "prereq": "Varian Transmisi (Hal. 1A-115): Ground Relay Starter melewati TR Switch (#8) pada [A] A/T (BLK/RED), sedangkan [B] M/T langsung massa (BLK).",
                "asKey": "Kunci Posisi START",
                "asTool": "DC Volt / Cek Sikring ST",
                "asSpec": "10 – 14 V (Cranking)",
                "wires": [
                    {"id": "GV_W4", "from": "Sikring ST SIG (#12)", "to": "Kunci Kontak (#5)", "color": "BLK/YEL (Hitam-Kuning)", "role": "Suplai Sinyal Starter"},
                    {"id": "GV_W6", "from": "Relay Starter (#7)", "to": "ECM C37-30 & C37-58", "color": "BLK/ORN (Hitam-Oranye)", "role": "Kontrol & Deteksi Cranking di ECM"},
                    {"id": "GV_W8", "from": "Relay Starter (#7)", "to": "TR Switch (#8) / Massa", "color": "[A] BLK/RED • [B] BLK", "role": "Pengaman P/N (A/T) atau Ground (M/T)"},
                ],
                "nextHandoff": "Lanjut Tahap 3 (Inti P0335): Sensor CKP (#1) membangkitkan pulsa ke ECM C37-36 (PNK) & C37-51 (BLU).",
            },
            {
                "shortLabel": "3. CKP → ECM",
                "cat": "INPUT",
                "badge": "🔵 SINYAL CKP INDUKTIF",
                "title": "Sensor CKP (#1) mengirim pulsa putaran kruk as ke ECM C37-36 & C37-51",
                "direction": "CKP Sensor (#1) ──▶ Kabel PNK (C37-36) & BLU (C37-51)",
                "fromNodes": ["CKP_GV"],
                "toNodes": ["ECM"],
                "wireIds": ["GV_W9", "GV_W10"],
                "func": "Gigi Sensor Plate (#2) memotong magnet CKP (#1) menghasilkan pulsa AC pada 2 kabel: Pink (PNK → C37-36) dan Biru (BLU → C37-51).",
                "prereq": "Prosedur Resmi Hal. 1A-116: (1) Lepas soket CKP, IG ON → 0 V. (2) Lepas soket ECM, IG OFF → tahanan ke ground ∞. (3) Kontinuitas kabel < 5 Ω.",
                "asKey": "IG OFF, Soket CKP & ECM Lepas",
                "asTool": "Multimeter Ohm (Ω) & DC V",
                "asSpec": "< 5 Ω • Ke GND ∞ • IG ON 0V",
                "wires": [
                    {"id": "GV_W9", "from": "CKP Sensor (PNK)", "to": "ECM C37-36", "color": "PNK (Pink)", "role": "Jalur Sinyal CKP (+) — Kontinuitas < 5 Ω"},
                    {"id": "GV_W10", "from": "CKP Sensor (BLU)", "to": "ECM C37-51", "color": "BLU (Biru)", "role": "Jalur Sinyal CKP (-) — Kontinuitas < 5 Ω"},
                ],
                "nextHandoff": "Lanjut Tahap 4 (Akhir): Verifikasi Ground ECM (C37-15/29/48) sebelum memvonis Sensor CKP atau ECM.",
            },
            {
                "shortLabel": "4. Ground ECM",
                "cat": "GROUND",
                "badge": "⚫ GROUND AKHIR",
                "title": "Jalur Akhir: Ground Utama ECM (C37-15, C37-29, C37-48) ke Blok Mesin",
                "direction": "ECM C37-15 / C37-29 / C37-48 (BLK) ──▶ Massa Blok Mesin",
                "fromNodes": ["ECM"],
                "toNodes": ["GND_GV"],
                "wireIds": ["GV_W11"],
                "func": "Menutup rangkaian ground referensi ECM ke blok mesin. Jika kabel PNK/BLU (< 5 Ω), sensor plate, dan ground bagus namun tetap P0335, baru ganti CKP atau cek ECM.",
                "prereq": "",
                "asKey": "IG OFF, Soket C37 Lepas",
                "asTool": "Multimeter Mode Ohm (Ω)",
                "asSpec": "< 1 Ω ke Negatif Aki",
                "wires": [
                    {"id": "GV_W11", "from": "ECM C37-15 / 29 / 48", "to": "Massa Blok Mesin", "color": "BLK (Hitam)", "role": "Ground Utama Sistem ECM"},
                ],
                "nextHandoff": "Selesai: Seluruh alur P0335 Grand Vitara (Hal. 1A-115 s/d 1A-116) telah ditelusuri.",
            },
        ],
    },
    "suzuki_ertiga_k14b": {
        "chain_id": "suzuki_ertiga_k14b",
        "brand": "Suzuki",
        "label": "Suzuki Ertiga Gen 1 K14B — CKP/CMP → ECM → Koil, Injektor & Fuel Pump",
        "render_mode": "suzuki_schematic",
        "schematic_key": "ERTIGA_K14B",
        "pdf_doc_id": "suzuki_ertiga_full",
        "pdf_page": 131,
        "scope": "Ertiga Gen 1 K14B 2012–2017 (Pinout OEM C01/E01)",
        "stages": [
            {
                "shortLabel": "1. Main Relay & GND",
                "cat": "POWER",
                "badge": "🔴 DAYA & MASSA ECM",
                "title": "Suplai +12V Main Relay (E01-55/56) & Ground ECM (C01-50/51)",
                "direction": "Main Relay ──▶ ECM E01-55/56 | ECM C01-50/51 ──▶ Ground Mesin",
                "fromNodes": ["ER_MAIN"],
                "toNodes": ["ER_ECM", "ER_GND"],
                "wireIds": ["ER_W1", "ER_W2", "ER_W3"],
                "func": "ECM menarik E01-54 (BRN/WHT) ke 0–1V saat IG ON agar Main Relay menyala dan mengalirkan +12V ke E01-55 & E01-56 (BLK/RED).",
                "prereq": "",
                "asKey": "IG ON, Back-Probe Terpasang",
                "asTool": "Multimeter DC Volt (V)",
                "asSpec": "+B: 10–14V • GND: < 0,3V",
                "wires": [
                    {"id": "ER_W1", "from": "Main Relay", "to": "ECM E01-55 & E01-56", "color": "BLK/RED (Hitam-Merah)", "role": "Suplai Daya Utama ECM +B1 & +B2"},
                    {"id": "ER_W2", "from": "ECM E01-54", "to": "Main Relay", "color": "BRN/WHT (Cokelat-Putih)", "role": "Kontrol Main Relay (0–1V IG ON)"},
                    {"id": "ER_W3", "from": "ECM C01-50 & C01-51", "to": "Massa Mesin", "color": "BLK (Hitam)", "role": "Ground Utama ECM (< 0,3 V)"},
                ],
                "nextHandoff": "Lanjut Tahap 2: Cek sinyal CKP (C01-9 PNK) & CMP (C01-8 RED/YEL) tipe Hall-Effect.",
            },
            {
                "shortLabel": "2. CKP & CMP",
                "cat": "INPUT",
                "badge": "🔵 INPUT HALL-EFFECT",
                "title": "Sensor CKP (C01-9) & CMP (C01-8) mengirim pulsa kotak 0–5V ke ECM",
                "direction": "CKP ──▶ C01-9 (PNK) | CMP ──▶ C01-8 (RED/YEL)",
                "fromNodes": ["ER_CKP", "ER_CMP"],
                "toNodes": ["ER_ECM"],
                "wireIds": ["ER_W4", "ER_W5"],
                "func": "Ertiga K14B memakai CKP & CMP tipe Hall-Effect 3-pin (digital). Tegangan di pin C01-9 & C01-8 bergantian antara 0–1V dan 4–5V saat mesin diputar.",
                "prereq": "Tip Praktisi: Putar kruk as pelan saat IG ON — multimeter di C01-9 (PNK) harus bolak-balik 0–1V ↔ 4–5V.",
                "asKey": "IG ON, Putar Kruk As / Idle",
                "asTool": "DC Volt / Osiloskop",
                "asSpec": "0–1 V ↔ 4–5 V (Pulsa)",
                "wires": [
                    {"id": "ER_W4", "from": "Sensor CKP", "to": "ECM C01-9", "color": "PNK (Pink)", "role": "Sinyal Putaran Kruk As (Hall-Effect)"},
                    {"id": "ER_W5", "from": "Sensor CMP", "to": "ECM C01-8", "color": "RED/YEL (Merah-Kuning)", "role": "Sinyal Noken As (Sinkronisasi Silinder)"},
                ],
                "nextHandoff": "Lanjut Tahap 3: ECM menembakkan pulsa ke 4 Koil Pengapian & 4 Injektor.",
            },
            {
                "shortLabel": "3. Koil & Injektor",
                "cat": "OUTPUT",
                "badge": "🟠 OUTPUT AKTUATOR",
                "title": "ECM menggerakkan 4 Koil Pengapian & 4 Injektor Bensin",
                "direction": "ECM C01-4/17/5/6 ──▶ Koil 1–4 | C01-13/37/25/1 ──▶ Injektor 1–4",
                "fromNodes": ["ER_ECM"],
                "toNodes": ["ER_COIL", "ER_INJ"],
                "wireIds": ["ER_W6", "ER_W7"],
                "func": "Koil dipicu pulsa 0–1V (naik pulsa saat idle), sedangkan Injektor mendapat +12V standby dan ECM memutus-nyambung ground-nya.",
                "prereq": "",
                "asKey": "IG ON & Idle (Back-Probe)",
                "asTool": "DC Volt / Test Lamp LED",
                "asSpec": "Koil: 0–1V • Inj: 10–14V",
                "wires": [
                    {"id": "ER_W6", "from": "ECM C01-4 / 17 / 5 / 6", "to": "Koil Silinder 1–4", "color": "GRN/YEL, GRN/WHT, BRN, LT GRN", "role": "Pemicu 4 Koil Pengapian"},
                    {"id": "ER_W7", "from": "ECM C01-13 / 37 / 25 / 1", "to": "Injektor Silinder 1–4", "color": "BLU/YEL, BLU/WHT, BLU/RED, LT GRN/BLK", "role": "Kontrol Ground Pulsa 4 Injektor"},
                ],
                "nextHandoff": "Lanjut Tahap 4 (Akhir): ECM mengaktifkan Relay Pompa Bensin (E01-49).",
            },
            {
                "shortLabel": "4. Fuel Pump",
                "cat": "OUTPUT",
                "badge": "🟠 OUTPUT RELAY POMPA",
                "title": "Jalur Akhir: ECM E01-49 (YEL/RED) menyalakan Relay Pompa Bensin",
                "direction": "ECM E01-49 (YEL/RED) ──▶ Relay Pompa Bensin",
                "fromNodes": ["ER_ECM"],
                "toNodes": ["ER_FP"],
                "wireIds": ["ER_W8"],
                "func": "Saat IG ON, E01-49 ditarik ke 0–1V selama 2 detik (priming), lalu baru menyala lagi begitu sinyal CKP (Tahap 2) masuk saat starter.",
                "prereq": "Tip Diagnosa: Pompa nyala 2 dtk saat IG ON tapi mati saat distarter → Pompa & Relay BAGUS, cek Sensor CKP (Tahap 2)!",
                "asKey": "IG ON (2 dtk) & Mesin Hidup",
                "asTool": "Multimeter DC Volt (V)",
                "asSpec": "0–1V (ON) • 10–14V (OFF)",
                "wires": [
                    {"id": "ER_W8", "from": "ECM E01-49", "to": "Relay Pompa Bensin", "color": "YEL/RED (Kuning-Merah)", "role": "Kontrol Ground Relay Pompa Bensin"},
                ],
                "nextHandoff": "Rantai Ertiga K14B Selesai.",
            },
        ],
    },
}


# =============================================================================
# 2. HELPERS: LOAD INDEX, DECOMPRESS SVGZ & PARSE CONNECT XML ON-THE-FLY
# =============================================================================
def _load_index() -> dict[str, Any]:
    if not INDEX_FILE.exists():
        return {"version": "1.0", "cache_size_mb": 0, "models": [], "cache_ready": False}
    data = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    data["cache_ready"] = True
    return data


def _safe_resolve_under(base: Path, rel: str) -> Path:
    resolved = (base / rel).resolve()
    base_res = base.resolve()
    try:
        resolved.relative_to(base_res)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="Path tidak diizinkan.") from exc
    if not resolved.exists() or not resolved.is_file():
        raise HTTPException(status_code=404, detail=f"Berkas tidak ditemukan: {rel}")
    return resolved


@lru_cache(maxsize=48)
def _decompress_and_clean_svgz(abs_svgz_path: str) -> tuple[str, list[float]]:
    raw = gzip.decompress(Path(abs_svgz_path).read_bytes()).decode("utf-8", errors="replace")
    entities = dict(re.findall(r'<!ENTITY\s+(\w+)\s+"([^"]*)">', raw))
    idx = raw.find("<svg")
    if idx != -1:
        raw = raw[idx:]
    for k, v in entities.items():
        raw = raw.replace(f"&{k};", v)

    # Sanitasi glyph Adobe Svg Symbol PUA &#xF057; -> Unicode Ohm Ω
    raw = raw.replace("&#xF057;", "Ω").replace("&#61527;", "Ω").replace("\uf057", "Ω")
    raw = re.sub(r"<!--[\s\S]*?-->", "", raw)
    raw = re.sub(r"<script[^>]*/>", "", raw)
    raw = re.sub(r"<defs>[\s\S]*?</defs>", "", raw)
    raw = re.sub(r'\s+onload="[^"]*"', "", raw)
    raw = re.sub(r'\s+a:[a-zA-Z0-9_-]+="[^"]*"', "", raw)
    raw = re.sub(r'\s+xmlns:(a|ewd)="[^"]*"', "", raw)
    raw = re.sub(r"\s+ewd:([a-zA-Z0-9_-]+)=", r" data-ewd-\1=", raw)
    raw = re.sub(r'\s+xlink:href=""', "", raw)
    raw = re.sub(r"adobe-font-script:japanese;", "", raw)
    # Fix unitless CSS font-size so modern HTML5 browsers render exact OEM typography
    raw = re.sub(r"font-size:\s*(\d+(?:\.\d+)?)(?=\s*[;\"])", r"font-size:\1px", raw)
    raw = re.sub(r"(\d+\.\d)\d+", r"\1", raw)
    raw = raw.replace("<text ", '<text pointer-events="none" ')
    raw = re.sub(r"\s+", " ", raw).strip()

    vb_match = re.search(r'viewBox="([^"]+)"', raw)
    base_vb = [0.0, 0.0, 502.1, 710.0]
    if vb_match:
        nums = [float(x) for x in vb_match.group(1).split()[:4]]
        if len(nums) == 4:
            base_vb = nums
    return raw, base_vb


@lru_cache(maxsize=48)
def _parse_connect_xml_edges(abs_xml_path: str) -> list[list[str]]:
    root = ET.parse(abs_xml_path).getroot()
    edges: list[list[str]] = []
    seen: set[tuple[str, str, str, str, str]] = set()
    for c1 in root.findall("connector"):
        t1, code1 = c1.attrib.get("type", ""), c1.attrib.get("code", "")
        for p1 in c1.findall("pin"):
            pin1, spec1 = p1.attrib.get("no", ""), p1.attrib.get("spec", "")
            for line in p1.findall("line"):
                lid, color = line.attrib.get("id", ""), line.attrib.get("color", "")
                for c2 in line.findall("connector"):
                    t2, code2 = c2.attrib.get("type", ""), c2.attrib.get("code", "")
                    p2 = c2.find("pin")
                    pin2 = p2.attrib.get("no", "") if p2 is not None else ""
                    spec2 = p2.attrib.get("spec", "") if p2 is not None else ""
                    key = (lid, code1, pin1, code2, pin2)
                    if key in seen:
                        continue
                    seen.add(key)
                    edges.append([lid, color, code1, t1, pin1, code2, t2, pin2, spec1 or spec2])
    return edges


# =============================================================================
# 3. API ENDPOINTS
# =============================================================================
@router.get("/wiring-viewer", include_in_schema=False)
async def serve_wiring_viewer():
    """Halaman layar penuh (landscape-friendly) Viewer Wiring Diagram & Alur Sinyal AGOS."""
    viewer_file = STATIC_DIR / "ewd_viewer.html"
    if not viewer_file.exists():
        raise HTTPException(status_code=404, detail="ewd_viewer.html belum tersedia.")
    return FileResponse(viewer_file)


@router.get("/api/v1/ewd/catalog")
async def get_ewd_catalog() -> dict[str, Any]:
    """Mengembalikan katalog seluruh model Toyota (.svgz & PDF) + Suzuki PDF + preset Alur Sinyal."""
    idx = _load_index()
    chains_summary = [
        {
            "chain_id": cid,
            "brand": c["brand"],
            "label": c["label"],
            "render_mode": c["render_mode"],
            "scope": c["scope"],
            "stage_count": len(c["stages"]),
        }
        for cid, c in CURATED_SIGNAL_CHAINS.items()
    ]
    return {
        "cache_ready": idx.get("cache_ready", False),
        "cache_size_mb": idx.get("cache_size_mb", 0),
        "models": idx.get("models", []),
        "signal_chains": chains_summary,
    }


@router.get("/api/v1/ewd/chains")
async def get_all_signal_chains() -> dict[str, Any]:
    """Mengembalikan seluruh definisi Alur Sinyal Berantai (Toyota & Suzuki)."""
    return {"chains": CURATED_SIGNAL_CHAINS}


@router.get("/api/v1/ewd/system/{model_id}/{sys_code}")
async def get_ewd_system(model_id: str, sys_code: str) -> dict[str, Any]:
    """Dekompresi & konversi .svgz + graf connect/*.xml secara on-the-fly dengan LRU cache."""
    idx = _load_index()
    model = next((m for m in idx.get("models", []) if m.get("model_id") == model_id), None)
    if not model or model.get("format") != "toyota_svgz":
        raise HTTPException(status_code=404, detail=f"Model EWD tidak ditemukan: {model_id}")

    sys_entry = next(
        (s for s in model.get("systems", []) if s.get("code", "").lower() == sys_code.lower()),
        None,
    )
    if not sys_entry:
        raise HTTPException(
            status_code=404, detail=f"Sistem '{sys_code}' tidak ditemukan pada {model_id}"
        )

    svgz_file = _safe_resolve_under(CACHE_ROOT, sys_entry["svgz_path"])
    svg_html, base_vb = _decompress_and_clean_svgz(str(svgz_file))

    edges: list[list[str]] = []
    if sys_entry.get("connect_xml_path"):
        try:
            conn_file = _safe_resolve_under(CACHE_ROOT, sys_entry["connect_xml_path"])
            edges = _parse_connect_xml_edges(str(conn_file))
        except HTTPException:
            edges = []

    return {
        "model_id": model_id,
        "model_label": model["label"],
        "pack_id": model.get("pack_id", ""),
        "sys_code": sys_entry["code"],
        "sys_name": sys_entry["name"],
        "category_label": sys_entry.get("category_label", ""),
        "term_from": sys_entry.get("term_from", ""),
        "base_vb": base_vb,
        "edge_count": len(edges),
        "edges": edges,
        "svg": svg_html,
    }


@router.get("/api/v1/ewd/pdf/{doc_id}")
async def stream_ewd_pdf(doc_id: str):
    """Streaming file PDF EWD Avanza atau Manual PDF Suzuki secara inline (mendukung #page=N)."""
    idx = _load_index()
    for m in idx.get("models", []):
        if m.get("format") != "pdf_collection":
            continue
        for doc in m.get("docs", []):
            if doc.get("doc_id") == doc_id:
                if doc.get("rel_path"):
                    pdf_path = _safe_resolve_under(CACHE_ROOT, doc["rel_path"])
                elif doc.get("abs_rel_workspace"):
                    pdf_path = _safe_resolve_under(WORKSPACE_ROOT, doc["abs_rel_workspace"])
                else:
                    raise HTTPException(status_code=404, detail="Path PDF tidak terdaftar.")
                return FileResponse(
                    pdf_path,
                    media_type="application/pdf",
                    headers={"Content-Disposition": f'inline; filename="{pdf_path.name}"'},
                )
    raise HTTPException(status_code=404, detail=f"Dokumen PDF tidak ditemukan: {doc_id}")
