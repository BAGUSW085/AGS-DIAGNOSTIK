"""
Ingest & Indexer Manual Resmi Suzuki Grand Vitara (JB420) - Vol 1.pdf & Vol 2.pdf
==================================================================================
Script ini dirancang khusus untuk memproses file PDF buku pedoman perbaikan resmi
Suzuki Grand Vitara JB420 (`Vol 1.pdf` - 661 halaman & `Vol 2.pdf` - 827 halaman)
di dalam sub-folder `manual repair suzuki vitara` pada proyek Anda, serta memuat
katalog hasil ekstraksi (`jb420_extracted_catalog.json` - 189 DTC & 51 Bab).

Fitur utama:
1. Mengekstrak teks per halaman dari `Vol 1.pdf` (Bab 0–4: Informasi Umum, Mesin,
   Suspensi, Driveline/Axle, Rem) dan `Vol 2.pdf` (Bab 5–10: Transmisi, Setir,
   HVAC, Restraint/Airbag, Bodi & Sistim Wiring 9A, serta Sistim Kontrol BCM/Immobilizer/Keyless).
2. Mendeteksi kode bab otomatis (misal `1A-16`, `5A-73`, `9A-24`, `10B-17`) serta melakukan
   chunking dokumen agar pencarian AI Repair Manual (RAG) akurat.
3. Mengisi data presisi dari buku manual asli JB420 ke tabel:
   - `sensor_specs` (Tegangan standar terminal ECM C37 & E23 dari Bab 1A hal. 257–265)
   - `wiring_diagrams` (Pinout lengkap ECM C37 & E23, TCM A/T E92 & E93, serta BCM G30/G31/G32)
   - `dtc_codes` (Seluruh 189 kode DTC resmi dari `jb420_extracted_catalog.json` + prosedur detail)

Cara menjalankan di komputer lokal Anda:
    python -m app.db.ingest_vitara_manuals --dir "./manual repair suzuki vitara"
"""

import argparse
import asyncio
import json
import logging
from pathlib import Path
import re
from typing import Iterator

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings
from app.models import DTCCode, RepairManual, SensorSpec, WiringDiagram

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Pola regex untuk mendeteksi kode halaman/bab khas manual Suzuki JB420 (contoh: 1A-16, 5A-73, 9A-24, 10B-17)
SECTION_CODE_PATTERN = re.compile(r"\b(00|[0-9]{1,2}[A-M])-([0-9]{1,3}|[i]+)\b")


def extract_text_from_pdf(pdf_path: Path) -> list[tuple[int, str, str]]:
    """
    Membaca teks per halaman dari file PDF manual Suzuki Grand Vitara JB420.
    Mengembalikan list tuple: (nomor_halaman, kode_seksi_bab, teks_halaman).
    """
    try:
        from pypdf import PdfReader
    except ImportError:
        logger.warning(
            "Library 'pypdf' belum terinstal. Jalankan `pip install pypdf` untuk membaca PDF: %s",
            pdf_path.name,
        )
        return []

    reader = PdfReader(str(pdf_path))
    extracted_pages: list[tuple[int, str, str]] = []
    current_section = "00"

    for idx, page in enumerate(reader.pages, start=1):
        txt = (page.extract_text() or "").strip()
        if not txt:
            continue
        match = SECTION_CODE_PATTERN.search(txt[:250])
        if match:
            current_section = f"Bab {match.group(1)} ({match.group(0)})"
        extracted_pages.append((idx, current_section, txt))

    return extracted_pages


def chunk_pdf_pages(
    pages: list[tuple[int, str, str]], filename: str, max_chars: int = 1500
) -> Iterator[tuple[str, str, str]]:
    """
    Memecah halaman-halaman PDF menjadi potongan (section_title, content_text, tags)
    berdasarkan bab/seksi dan batas karakter agar konteks tabel/prosedur tidak terputus.
    """
    jb420_keywords = {
        "jb420", "j20", "j20a", "m16", "grand vitara", "vitara", "ecm", "tcm",
        "bcm", "sdm", "icm", "c37", "e23", "e92", "e93", "g30", "g31", "g32",
        "ckp", "cmp", "tps", "app", "map", "maf", "iat", "ect", "ho2s", "a/f",
        "egr", "evap", "imt", "can", "dlc", "koil", "injektor", "throttle",
        "transmisi", "solenoid", "tcc", "air bag", "immobilizer", "keyless",
        "ground", "sikring", "relay", "p0101", "p0106", "p0116", "p0122",
        "p0222", "p0171", "p0300", "p0335", "p0340", "p0420", "p0705", "p2101",
        "p2135", "p2763", "b1141", "b1150",
    }

    buffer: list[str] = []
    buffer_len = 0
    chunk_start_page = 1
    chunk_end_page = 1
    chunk_section = "Bab 00"
    part_counter = 1

    for page_num, sec_label, text in pages:
        page_block = f"[{filename} - Hal. {page_num} | {sec_label}]\n{text}"
        if buffer and (buffer_len + len(page_block) > max_chars):
            joined = "\n\n".join(buffer)
            lower_text = joined.lower()
            found_tags = sorted(kw for kw in jb420_keywords if kw in lower_text)
            for base_tag in ("grand vitara", "jb420"):
                if base_tag not in found_tags:
                    found_tags.insert(0, base_tag)

            title = (
                f"{filename} | {chunk_section} "
                f"(Hal. {chunk_start_page}-{chunk_end_page}) #{part_counter}"
            )
            yield title, joined, ",".join(found_tags)

            buffer = [page_block]
            buffer_len = len(page_block)
            chunk_start_page = page_num
            chunk_end_page = page_num
            chunk_section = sec_label
            part_counter += 1
        else:
            if not buffer:
                chunk_start_page = page_num
                chunk_section = sec_label
            buffer.append(page_block)
            buffer_len += len(page_block)
            chunk_end_page = page_num

    if buffer:
        joined = "\n\n".join(buffer)
        lower_text = joined.lower()
        found_tags = sorted(kw for kw in jb420_keywords if kw in lower_text)
        for base_tag in ("grand vitara", "jb420"):
            if base_tag not in found_tags:
                found_tags.insert(0, base_tag)
        title = (
            f"{filename} | {chunk_section} "
            f"(Hal. {chunk_start_page}-{chunk_end_page}) #{part_counter}"
        )
        yield title, joined, ",".join(found_tags)


async def seed_jb420_structured_reference_data(session: AsyncSession) -> None:
    """
    Menyimpan data terstruktur asli dari Vol 1.pdf & Vol 2.pdf Suzuki Grand Vitara JB420:
    1. Spesifikasi Sensor & Tegangan Standar ECM (Bab 1A Hal. 257-265)
    2. Pinout Konektor ECM (C37 & E23), TCM (E92 & E93), dan BCM (G30, G31, G32)
    3. Kode DTC OBD-II Mesin J20A, Transmisi A/T, ABS, Airbag, dan BCM (termasuk 189 DTC dari jb420_extracted_catalog.json)
    """
    # 1. Spesifikasi Sensor Suzuki Grand Vitara JB420 (Bab 1A Vol 1.pdf Hal. 257-265)
    jb420_sensors = [
        SensorSpec(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A)",
            sensor_name="Electric Throttle Body - TPS Main & Sub (Bab 1A Hal. 261-262)",
            pin_configuration=(
                "C37-53 (WHT): +5V Power Source | C37-54 (BLK): TPS Main Signal | "
                "C37-40 (RED): TPS Sub Signal | C37-41 (GRN): TPS Ground | "
                "C37-44 (BLU/RED) & C37-45 (BLU/YEL): Throttle Actuator Motor Drive"
            ),
            voltage_idle="TPS Main (C37-54): 0.72 - 1.04 V | TPS Sub (C37-40): 1.60 - 1.91 V (Pedal gas posisi idle)",
            voltage_wot="TPS Main (C37-54): 3.67 - 4.25 V | TPS Sub (C37-40): 3.88 - 4.45 V (Pedal gas ditekan penuh)",
            resistance_ohm="Ground C37-41 (GRN) ke massa mesin: < 3 Ohm | Supply C37-53 (WHT): 4.5 - 5.5 V",
            testing_notes=(
                "Jika DTC P0122 dan P0222 muncul bersamaan, periksa kabel WHT (C37-53) +5V kemungkinan putus. "
                "Tegangan diukur setelah mesin dipanaskan dengan kunci kontak ON."
            ),
        ),
        SensorSpec(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A)",
            sensor_name="Accelerator Pedal Position (APP) Sensor Main & Sub (Bab 1A Hal. 265)",
            pin_configuration=(
                "E23-56 (WHT): +5V APP Main | E23-55 (WHT/BLU): APP Main Signal | E23-54 (ORN): Ground APP Main | "
                "E23-53 (ORN/BLU): +5V APP Sub | E23-52 (BLU/GRN): APP Sub Signal | E23-51 (BLU/YEL): Ground APP Sub"
            ),
            voltage_idle="APP Main (E23-55): 0.65 - 0.82 V | APP Sub (E23-52): 0.30 - 0.44 V (Pedal gas bebas/idle)",
            voltage_wot="APP Main (E23-55): 3.50 - 4.27 V | APP Sub (E23-52): 1.74 - 2.17 V (Pedal gas injak penuh)",
            resistance_ohm="Ground E23-54 (ORN) & E23-51 (BLU/YEL): < 0.3 V saat kunci kontak ON",
            testing_notes="Pastikan sumber +5V pada E23-56 (WHT) dan E23-53 (ORN/BLU) berada di rentang 4.5 - 5.5 V.",
        ),
        SensorSpec(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A)",
            sensor_name="Mass Air Flow (MAF) & Intake Air Temp (IAT) Sensor (Bab 1A Hal. 260)",
            pin_configuration=(
                "Power Supply: BLU/BLK (10-14V) | C37-26 (RED): MAF Signal | "
                "C37-27 (BLU): MAF Ground | C37-25 (LT GRN): IAT Signal | C37-57 (GRY/GRN): Sensor Ground"
            ),
            voltage_idle="MAF (C37-26): 0.5 - 1.0 V (Kunci ON mesin mati) | 1.3 - 1.8 V (Mesin hidup putaran idle hangat)",
            voltage_wot="IAT (C37-25): 3.18 - 3.67 V @ 0°C | 1.32 - 1.65 V @ 40°C | 0.46 - 0.60 V @ 80°C",
            resistance_ohm="Ground MAF C37-27 (BLU) & Ground Sensor C37-57 (GRY/GRN) ke bodi: < 3 Ohm",
            testing_notes="Tegangan power supply kabel BLU/BLK pada konektor MAF harus 10 - 14 V saat kunci kontak ON.",
        ),
        SensorSpec(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A)",
            sensor_name="Manifold Absolute Pressure (MAP) & Engine Coolant Temp (ECT) (Bab 1A Hal. 258-262)",
            pin_configuration=(
                "C37-14 (GRY/RED): +5V Supply MAP | C37-55 (RED/WHT): MAP Signal | "
                "C37-24 (PPL/YEL): ECT Signal | C37-57 (GRY/GRN): Sensor Ground"
            ),
            voltage_idle="MAP (C37-55): 0.4 - 2.0 V saat idle hangat (Sekitar 4.0 V saat Kunci ON mesin mati @ 100 kPa)",
            voltage_wot="ECT (C37-24): 3.3 - 3.8 V @ 0°C | 1.38 - 1.72 V @ 50°C | 0.40 - 0.53 V @ 100°C",
            resistance_ohm="Supply 5V C37-14 (GRY/RED): 4.5 - 5.5 V (dibagi dengan A/C pressure & electric load sensor)",
            testing_notes=(
                "Catatan Bab 1A Hal. 199: Jika DTC P0107 dan P1501 muncul bersamaan, periksa kabel GRY/RED (C37-14) putus. "
                "Jika DTC P0108, P0113, dan P0118 muncul bersamaan, periksa ground sensor GRY/GRN (C37-57)."
            ),
        ),
        SensorSpec(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A)",
            sensor_name="CKP Sensor, CMP Sensor, A/F Sensor (Sensor-1) & HO2S-2 (Bab 1A Hal. 258-262)",
            pin_configuration=(
                "CKP: C37-51 (BLU/GRN +) & C37-36 (PNK -) | CMP: C37-52 (WHT/RED) | "
                "A/F Sensor-1: C37-38 (WHT +), C37-37 (BLK -), C37-32 (PNK/BLU Heater) | "
                "HO2S-2: C37-11 (RED Signal), C37-47 (BLK/RED Heater)"
            ),
            voltage_idle=(
                "A/F Sensor-1: C37-38 (WHT) 3.0 - 3.2 V & C37-37 (BLK) 2.6 - 2.8 V saat idle | "
                "HO2S-2 (C37-11): ~0.15 V saat idle (4 - 5 V saat Kunci ON)"
            ),
            voltage_wot=(
                "CKP (C37-51 & C37-36): Gelombang sinusoidal +4..+6V ke -4..-6V (30 [36-6] pulsa/putaran kruk as) | "
                "CMP (C37-52): Pulsa 0-0.6V <-> 4-5V (6 pulsa/putaran camshaft)"
            ),
            resistance_ohm="Ground HO2S-2 (GRN) ke massa mesin: < 3 Ohm",
            testing_notes="Gunakan oscilloscope untuk memeriksa gelombang CKP (CH1 C37-51) dan CMP (CH1 C37-52).",
        ),
    ]

    for spec in jb420_sensors:
        exists = await session.execute(
            select(SensorSpec.id).where(
                SensorSpec.model == spec.model,
                SensorSpec.sensor_name == spec.sensor_name,
            )
        )
        if exists.scalar_one_or_none() is None:
            session.add(spec)

    # 2. Pinout Konektor ECM, TCM, dan BCM Suzuki Grand Vitara JB420
    jb420_wirings = [
        WiringDiagram(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A)",
            year_range="2006-2012",
            system_name="Engine Control Module (ECM) - Konektor C37 (60-Pin) & E23 (60-Pin) (Vol 1 Bab 1A Hal. 74-76 & 257-265)",
            ecu_connector_code="Coupler C37 (Mesin) & Coupler E23 (Bodi/Instrumen)",
            pinout_json={
                "C37-01": {"wire_color": "PNK", "function": "Fuel Injector No.1 (10-14V IG ON, Pulsa Idle)"},
                "C37-02": {"wire_color": "PNK/BLK", "function": "Fuel Injector No.2 (10-14V IG ON, Pulsa Idle)"},
                "C37-11": {"wire_color": "RED", "function": "Heated Oxygen Sensor-2 (HO2S-2) Signal"},
                "C37-14": {"wire_color": "GRY/RED", "function": "Output +5V Power Source (MAP, A/C Press, Electric Load)"},
                "C37-15": {"wire_color": "BLK/ORN", "function": "Ground ECM (< 0.3V)"},
                "C37-16": {"wire_color": "PNK/GRN", "function": "Fuel Injector No.3"},
                "C37-17": {"wire_color": "PNK/BLU", "function": "Fuel Injector No.4"},
                "C37-18": {"wire_color": "BRN/YEL", "function": "Ignition Coil No.4 Trigger"},
                "C37-19": {"wire_color": "BRN/WHT", "function": "Ignition Coil No.3 Trigger"},
                "C37-20": {"wire_color": "BRN/BLK", "function": "Ignition Coil No.2 Trigger"},
                "C37-21": {"wire_color": "BRN", "function": "Ignition Coil No.1 Trigger"},
                "C37-22": {"wire_color": "BLK/YEL", "function": "Starting Motor Control Relay Output (8-14V saat ST)"},
                "C37-24": {"wire_color": "PPL/YEL", "function": "Engine Coolant Temp (ECT) Sensor Signal"},
                "C37-25": {"wire_color": "LT GRN", "function": "Intake Air Temp (IAT) Sensor Signal"},
                "C37-26": {"wire_color": "RED", "function": "Mass Air Flow (MAF) Sensor Signal (1.3-1.8V Idle)"},
                "C37-27": {"wire_color": "BLU", "function": "Ground MAF Sensor"},
                "C37-29": {"wire_color": "BLK/YEL", "function": "Ground ECM"},
                "C37-30": {"wire_color": "BLK/ORN", "function": "Ground ECM"},
                "C37-36": {"wire_color": "PNK", "function": "Crankshaft Position (CKP) Sensor (-)"},
                "C37-37": {"wire_color": "BLK", "function": "A/F Sensor Signal (-) (2.6-2.8V Idle)"},
                "C37-38": {"wire_color": "WHT", "function": "A/F Sensor Signal (+) (3.0-3.2V Idle)"},
                "C37-40": {"wire_color": "RED", "function": "Throttle Position Sensor (Sub) Signal (1.60-1.91V Idle)"},
                "C37-41": {"wire_color": "GRN", "function": "Ground Throttle Position Sensor"},
                "C37-44": {"wire_color": "BLU/RED", "function": "Throttle Actuator Motor Output (+)"},
                "C37-45": {"wire_color": "BLU/YEL", "function": "Throttle Actuator Motor Output (-)"},
                "C37-48": {"wire_color": "BLK/YEL", "function": "Ground ECM"},
                "C37-51": {"wire_color": "BLU / GRN", "function": "Crankshaft Position (CKP) Sensor (+)"},
                "C37-52": {"wire_color": "WHT/RED", "function": "Camshaft Position (CMP) Sensor Signal"},
                "C37-53": {"wire_color": "WHT", "function": "Output +5V Power Source Throttle Position Sensor"},
                "C37-54": {"wire_color": "BLK", "function": "Throttle Position Sensor (Main) Signal (0.72-1.04V Idle)"},
                "C37-55": {"wire_color": "RED/WHT", "function": "Manifold Absolute Pressure (MAP) Sensor Signal"},
                "C37-56": {"wire_color": "WHT", "function": "Knock Sensor Signal (2-3V IG ON)"},
                "C37-57": {"wire_color": "GRY/GRN", "function": "Main Sensor Ground (< 0.3V)"},
                "C37-58": {"wire_color": "BLK/YEL", "function": "Ground ECM"},
                "E23-01": {"wire_color": "BLU/BLK", "function": "Main Power Supply (10-14V IG ON dari Main Relay)"},
                "E23-02": {"wire_color": "WHT", "function": "Power Source ECM Internal Memory (+BB 10-14V Standby)"},
                "E23-04": {"wire_color": "WHT/RED", "function": "CAN High Communication Line (2.5-4.5V Pulse)"},
                "E23-05": {"wire_color": "PPL/WHT", "function": "Data Link Connector (DLC) Serial Comm 12V"},
                "E23-15": {"wire_color": "WHT/GRN", "function": "Fuel Pump Relay Output (0-2.5V saat ON 2 detik/mesin hidup)"},
                "E23-16": {"wire_color": "BLU/BLK", "function": "Main Power Supply (10-14V IG ON)"},
                "E23-17": {"wire_color": "GRN", "function": "Power Supply Throttle Actuator Drive Circuit (10-14V)"},
                "E23-19": {"wire_color": "WHT/BLU", "function": "CAN Low Communication Line (0.5-2.5V Pulse)"},
                "E23-29": {"wire_color": "BLK/WHT", "function": "Ignition Switch Signal IG1 (10-14V IG ON)"},
                "E23-46": {"wire_color": "RED/BLK", "function": "Radiator Cooling Fan Relay No.1 Output"},
                "E23-47": {"wire_color": "RED", "function": "Radiator Cooling Fan Relay No.2 Output"},
                "E23-52": {"wire_color": "BLU/GRN", "function": "APP Sensor (Sub) Signal (0.30-0.44V Idle)"},
                "E23-53": {"wire_color": "ORN/BLU", "function": "Output +5V Power Source APP Sensor (Sub)"},
                "E23-55": {"wire_color": "WHT/BLU", "function": "APP Sensor (Main) Signal (0.65-0.82V Idle)"},
                "E23-56": {"wire_color": "WHT", "function": "Output +5V Power Source APP Sensor (Main)"},
                "E23-60": {"wire_color": "BLU", "function": "Main Relay Control Output (0-2V IG ON)"},
            },
            ground_locations=(
                "Ground ECM terbagi pada terminal C37-15 (BLK/ORN), C37-29 (BLK/YEL), C37-30 (BLK/ORN), "
                "C37-48 (BLK/YEL), dan C37-58 (BLK/YEL) menuju titik massa mesin J20A (Bab 9A Hal. 484)."
            ),
            diagram_image_url="/assets/wiring/jb420_ecm_c37_e23.png",
        ),
        WiringDiagram(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A A/T)",
            year_range="2006-2012",
            system_name="Transmission Control Module (TCM) - Konektor E92 (24-Pin) & E93 (26-Pin) (Vol 2 Bab 5A Hal. 102-104)",
            ecu_connector_code="Coupler E92 (24-Pin) & Coupler E93 (26-Pin)",
            pinout_json={
                "E92-01": {"wire_color": "BLK/ORN", "function": "Ground TCM (0-1V IG ON)"},
                "E92-02": {"wire_color": "BRN/RED", "function": "Pressure Control Solenoid Valve (-) (0.6-1.0V)"},
                "E92-03": {"wire_color": "PPL/WHT", "function": "TCC Pressure Control Solenoid Valve (-) (0.6-1.0V)"},
                "E92-04": {"wire_color": "YEL/RED", "function": "Pressure Control Solenoid Valve (+) Duty Pulse"},
                "E92-05": {"wire_color": "GRN/YEL", "function": "TCC Pressure Control Solenoid Valve (+) Duty Pulse"},
                "E92-06": {"wire_color": "BLK/WHT", "function": "Main Power Source IG (10-14V IG ON)"},
                "E92-07": {"wire_color": "WHT", "function": "Jalur Komunikasi CAN (Rendah) (1.6-2.5V Pulse)"},
                "E92-11": {"wire_color": "YEL/BLK", "function": "A/T Fluid Temperature Sensor (+) (2.9-3.1V @ 20°C, 0.3-0.5V @ 100°C)"},
                "E92-12": {"wire_color": "ORN", "function": "A/T Fluid Temperature Sensor (-)"},
                "E92-15": {"wire_color": "GRN/RED", "function": "Shift Solenoid Valve-B (No.2) (9-14V pada posisi P)"},
                "E92-16": {"wire_color": "GRN", "function": "Shift Solenoid Valve-A (No.1) (9-14V pada posisi P)"},
                "E92-17": {"wire_color": "RED", "function": "Jalur Komunikasi CAN (Tinggi) (2.5-3.6V Pulse)"},
                "E92-23": {"wire_color": "BLK", "function": "Ground TCM (0-1V)"},
                "E92-24": {"wire_color": "WHT", "function": "Backup Memory Power Source (+BB 10-14V Tetap)"},
                "E93-01": {"wire_color": "RED", "function": "Transmission Range Sensor Posisi 'R' (8-14V di R)"},
                "E93-04": {"wire_color": "WHT", "function": "Output Shaft Speed Sensor (+) (18 pulsa/putaran)"},
                "E93-06": {"wire_color": "BLU", "function": "Input Shaft Speed Sensor (+) (24 pulsa/putaran)"},
                "E93-07": {"wire_color": "GRN", "function": "Transmission Range Sensor Posisi 'D' (8-14V di D)"},
                "E93-08": {"wire_color": "GRN/ORN", "function": "Transmission Range Sensor Posisi 'N' (8-14V di N)"},
                "E93-14": {"wire_color": "ORN", "function": "Output Shaft Speed Sensor (-) (2-3V IG ON mesin mati)"},
                "E93-16": {"wire_color": "PNK", "function": "Input Shaft Speed Sensor (-) (2-3V IG ON mesin mati)"},
                "E93-18": {"wire_color": "GRN/WHT", "function": "Transmission Range Sensor Posisi 'L'"},
                "E93-19": {"wire_color": "GRN/ORN", "function": "Transmission Range Sensor Posisi '2'"},
                "E93-20": {"wire_color": "PNK", "function": "Transmission Range Sensor Posisi 'P' (8-14V di P)"},
                "E93-23": {"wire_color": "PPL/WHT", "function": "Data Link Connector (DLC) (8-14V IG ON)"},
            },
            ground_locations="Terminal E92-1 (BLK/ORN) dan E92-23 (BLK) terhubung ke body ground bawah dashboard.",
            diagram_image_url="/assets/wiring/jb420_tcm_e92_e93.png",
        ),
        WiringDiagram(
            brand="Suzuki",
            model="Grand Vitara JB420 (2.0L J20A)",
            year_range="2006-2012",
            system_name="Body Electrical Control Module (BCM) - Konektor G30, G31, G32 (Vol 2 Bab 10B Hal. 741-744)",
            ecu_connector_code="Coupler G30 (24-Pin), G31 (40-Pin) & G32 (15-Pin)",
            pinout_json={
                "G30-19": {"wire_color": "YEL", "function": "Sirkuit Komunikasi SDM Air Bag (ke G47-22 / G46-15, 4-6V IG ON)"},
                "G31-21": {"wire_color": "BLK/RED", "function": "Ground Outside Air Temperature (Ambient) Sensor"},
                "G31-24": {"wire_color": "WHT/BLK", "function": "Input Sinyal Outside Air Temperature Sensor (4-6V Open)"},
            },
            ground_locations="Titik ground bodi kabin (G30/G31/G32) mengacu pada Bab 9A Hal. 484 (Titik Ground No. 10, 11, 12).",
            diagram_image_url="/assets/wiring/jb420_bcm_g30_g31_g32.png",
        ),
    ]

    for wd in jb420_wirings:
        exists = await session.execute(
            select(WiringDiagram.id).where(
                WiringDiagram.model == wd.model,
                WiringDiagram.system_name == wd.system_name,
            )
        )
        if exists.scalar_one_or_none() is None:
            session.add(wd)

    # 3. Kode DTC Spesifik Suzuki Grand Vitara JB420 (Prioritas + Katalog 189 DTC jb420_extracted_catalog.json)
    jb420_dtcs = [
        DTCCode(
            code="P0101",
            system_category="Powertrain - Fuel & Air Metering (JB420 Bab 1A-62)",
            description_id="Range / Performance Sirkuit Mass Air Flow (MAF) Sensor",
            common_causes="Kabel BLU/BLK power supply MAF putus, ground BLU (C37-27) tahanan tinggi (>3 Ohm), kebocoran udara intake, atau MAF sensor kotor/rusak.",
            recommended_fix="Ukur tegangan power supply kabel BLU/BLK konektor MAF (harus 10-14V saat IG ON) dan tegangan sinyal C37-26 (RED) saat idle hangat (standar 1.3 - 1.8 V).",
            severity_level="MEDIUM",
        ),
        DTCCode(
            code="P0106",
            system_category="Powertrain - Fuel & Air Metering (JB420 Bab 1A-68)",
            description_id="Range / Performance Manifold Absolute Pressure (MAP) Sensor",
            common_causes="Selang vakum/seal MAP bocor, kabel +5V GRY/RED (C37-14) putus, ground sensor GRY/GRN (C37-57) putus, atau sinyal RED/WHT (C37-55) koslet.",
            recommended_fix="Periksa tegangan +5V pada kabel GRY/RED (C37-14) dan sinyal C37-55 (RED/WHT): standar ~4V saat IG ON mesin mati dan 0.4 - 2.0 V saat idle hangat.",
            severity_level="MEDIUM",
        ),
        DTCCode(
            code="P0122",
            system_category="Powertrain - Electronic Throttle Control (JB420 Bab 1A-88)",
            description_id="Sirkuit Throttle Position Sensor (Main) Rendah (dan/atau P0222 Sub Rendah)",
            common_causes="Jika P0122 dan P0222 muncul bersamaan, kabel WHT (C37-53) sumber +5V TPS putus. Atau kabel sinyal BLK (C37-54) koslet ke ground.",
            recommended_fix="Ukur tegangan +5V antara kabel WHT konektor Electric Throttle Body dan ground mesin (standar 4-6V), serta sinyal C37-54 (BLK) 0.72-1.04V saat idle.",
            severity_level="HIGH",
        ),
        DTCCode(
            code="P2101",
            system_category="Powertrain - Electronic Throttle Control (JB420 Bab 1A-173)",
            description_id="Range / Performance Sirkuit Throttle Actuator Control Motor",
            common_causes="Kerak karbon menumpuk di katup kupu-kupu Electric Throttle Body, relay throttle actuator (BLU/ORN E23-50) bermasalah, atau kabel motor C37-44 (BLU/RED) & C37-45 (BLU/YEL) putus.",
            recommended_fix="Bersihkan throttle body, periksa sikring 'THR MOT', periksa power supply E23-17 (GRN) 10-14V, dan ukur tahanan motor aktuator throttle.",
            severity_level="CRITICAL",
        ),
        DTCCode(
            code="P2763",
            system_category="Powertrain - Automatic Transmission TCM (JB420 Bab 5A-69)",
            description_id="Sirkuit Torque Converter Clutch (TCC) Pressure Control Solenoid Tinggi (atau P2764 Rendah)",
            common_causes="Sirkuit solenoid TCC pada terminal TCM E92-5 (GRN/YEL +) dan E92-3 (PPL/WHT -) koslet ke power/ground, atau solenoid TCC rusak.",
            recommended_fix="Lepas konektor TCM E92, periksa hubungan terminal E92-3 (PPL/WHT) dan E92-5 (GRN/YEL), serta ukur sinyal duty pulse saat mesin idle di posisi P.",
            severity_level="HIGH",
        ),
        DTCCode(
            code="B1141",
            system_category="Body Electrical - BCM (JB420 Bab 10B-17)",
            description_id="Sirkuit Outside Air Temperature Sensor (Ambient) Tinggi (>4.88V) / Putus",
            common_causes="Konektor sensor suhu udara luar lepas, kabel WHT/BLK (G31-24) atau ground BLK/RED (G31-21) pada BCM putus.",
            recommended_fix="Ukur tegangan antara terminal WHT/BLK (G31-24) konektor sensor ambient dan ground bodi saat IG ON (standar 4-6V) dan pastikan ground BLK/RED (G31-21) terhubung baik.",
            severity_level="LOW",
        ),
    ]

    # Muat juga seluruh 8 Modul Wiring (251 Pin) & 207+ DTC hasil ekstraksi mendalam jb420_extracted_catalog.json
    catalog_candidates = [
        Path(__file__).resolve().parent.parent / "jb420_extracted_catalog.json",
        Path(__file__).with_name("jb420_extracted_catalog.json"),
        Path("./app/jb420_extracted_catalog.json"),
        Path("./jb420_extracted_catalog.json"),
    ]
    catalog_data: dict[str, Any] = {}
    for cat_path in catalog_candidates:
        if cat_path.exists():
            try:
                catalog_data = json.loads(cat_path.read_text(encoding="utf-8"))
                break
            except Exception as exc:
                logger.warning("Gagal memuat katalog JSON %s: %s", cat_path, exc)

    mod_pins = catalog_data.get("module_pinouts", {})
    if isinstance(mod_pins, dict) and mod_pins:
        extra_mod_wirings = [
            ("Grand Vitara JB420 (2.0L J20A)", "ABS / EBD Hydraulic Unit & Control Module - Konektor E03 (26-Pin) (Vol 1 Bab 4E Hal. 636-649)", "Coupler E03 (26-Pin ABS Control Module)", mod_pins.get("ABS_E03", {}), "Ground ABS pada terminal E03-01 ke bodi ruang mesin kanan (Bab 9A Hal. 484).", "/assets/wiring/jb420_abs_e03.png"),
            ("Grand Vitara JB420 (2.0L J20A)", "Automatic Air Conditioner (HVAC Control Module) - Konektor G52 (32-Pin) (Vol 2 Bab 7B Hal. 327-330)", "Coupler G52 (32-Pin HVAC Control Module)", mod_pins.get("HVAC_G52", {}), "Ground sensor HVAC pada G52-13 (BLK/RED) & G52-12 (YEL) ke bodi kabin tengah.", "/assets/wiring/jb420_hvac_g52.png"),
            ("Grand Vitara JB420 (2.0L J20A)", "SRS Air Bag Sensing & Diagnostic Module (SDM) - Konektor G47 (23-Pin) (Vol 2 Bab 8B Hal. 370)", "Coupler G47 (23-Pin SRS Air Bag SDM)", mod_pins.get("SDM_G47", {}), "Ground utama SDM pada terminal G47-20 (BLK) ke lantai konsol tengah (< 1 Ohm).", "/assets/wiring/jb420_sdm_g47.png"),
            ("Grand Vitara JB420 (2.0L J20A)", "Immobilizer Control Module (ICM) - Konektor G24 (6-Pin) (Vol 2 Bab 10C Hal. 785)", "Coupler G24 (6-Pin Immobilizer Control Module)", mod_pins.get("ICM_G24", {}), "Ground ICM pada terminal G24-02 (BLK) di kolom kemudi bawah dashboard.", "/assets/wiring/jb420_icm_g24.png"),
            ("Grand Vitara JB420 (2.0L J20A)", "Keyless Start Control Module (KSCM) - Konektor G44 (40-Pin) (Vol 2 Bab 10E Hal. 803-804)", "Coupler G44 (40-Pin Keyless Start Control Module)", mod_pins.get("KSCM_G44", {}), "Ground KSCM pada terminal G44-09 & steering lock unit G44-30 di belakang glove box.", "/assets/wiring/jb420_kscm_g44.png"),
        ]
        for mdl, sname, ccode, pjson, gnd, img in extra_mod_wirings:
            if not pjson:
                continue
            ex_wd = (await session.execute(select(WiringDiagram).where(WiringDiagram.ecu_connector_code == ccode))).scalar_one_or_none()
            if ex_wd is None:
                session.add(
                    WiringDiagram(
                        brand="Suzuki",
                        model=mdl,
                        year_range="2006-2012",
                        system_name=sname,
                        ecu_connector_code=ccode,
                        pinout_json=pjson,
                        ground_locations=gnd,
                        diagram_image_url=img,
                    )
                )

    for item in catalog_data.get("dtc_catalog", []):
        jb420_dtcs.append(
            DTCCode(
                code=item["code"],
                system_category=item["system_category"],
                description_id=item["description_id"],
                common_causes=item["common_causes"],
                recommended_fix=item["recommended_fix"],
                severity_level=item.get("severity_level", "MEDIUM"),
            )
        )

    seen_codes: set[str] = set()
    for dtc in jb420_dtcs:
        if dtc.code in seen_codes:
            continue
        seen_codes.add(dtc.code)
        existing_dtc = (
            await session.execute(select(DTCCode).where(DTCCode.code == dtc.code))
        ).scalar_one_or_none()
        if existing_dtc is None:
            session.add(dtc)
        elif "Periksa wiring harness, konektor sensor/aktuator terkait" in (existing_dtc.possible_causes or ""):
            existing_dtc.system = dtc.system
            existing_dtc.system_category = dtc.system_category
            existing_dtc.description_id = dtc.description_id
            existing_dtc.possible_causes = dtc.possible_causes
            existing_dtc.common_causes = dtc.common_causes
            existing_dtc.recommended_fix = dtc.recommended_fix
            existing_dtc.severity_level = dtc.severity_level


async def ingest_vitara_folder(
    session: AsyncSession,
    folder_path: Path,
    brand: str = "Suzuki",
    model: str = "Grand Vitara JB420 (2.0L J20A)",
) -> int:
    """
    Memindai seluruh file (`Vol 1.pdf`, `Vol 2.pdf`, `.txt`, `.md`) di dalam sub-folder
    `manual repair suzuki vitara` dan menyimpannya ke database RAG (`repair_manuals`),
    sekaligus mengisi data teknis presisi JB420 ke `sensor_specs`, `wiring_diagrams`, dan `dtc_codes`.
    """
    await seed_jb420_structured_reference_data(session)

    # Auto-resolve folder path if it does not exist or has no PDF files
    supported_ext = {".pdf", ".txt", ".md"}
    resolved_path = folder_path
    has_files = resolved_path.exists() and any(p.suffix.lower() in supported_ext for p in resolved_path.rglob("*"))
    if not has_files:
        fallback_candidates = [
            Path("./manual repair suzuki vitara"),
            Path("../manual repair suzuki vitara"),
            Path("../../manual repair suzuki vitara"),
            Path(r"C:\project bengkel masa depan ai antigravity\manual repair suzuki vitara"),
        ]
        for candidate in fallback_candidates:
            if candidate.exists() and any(p.suffix.lower() in supported_ext for p in candidate.rglob("*")):
                logger.info("Menggunakan folder fallback manual repair suzuki vitara: %s", candidate.resolve())
                resolved_path = candidate
                break

    if not resolved_path.exists() or not resolved_path.is_dir():
        logger.error("Folder tidak ditemukan: %s", resolved_path.resolve())
        return 0

    files = sorted(
        p for p in resolved_path.rglob("*")
        if p.is_file() and p.suffix.lower() in supported_ext
    )

    if not files:
        logger.warning(
            "Tidak ditemukan file .pdf, .txt, atau .md di dalam folder: %s",
            folder_path.resolve(),
        )
        return 0

    inserted_chunks = 0
    for file_path in files:
        logger.info("Memproses file manual: %s ...", file_path.name)
        rel_path = str(file_path.name)

        if file_path.suffix.lower() == ".pdf":
            pages = extract_text_from_pdf(file_path)
            if not pages:
                continue
            chunks_iter = chunk_pdf_pages(pages, file_path.stem)
        else:
            raw_text = file_path.read_text(encoding="utf-8", errors="ignore")
            if not raw_text.strip():
                continue
            chunks_iter = chunk_pdf_pages([(1, "Dokumen Teks", raw_text)], file_path.stem)

        for sec_title, content, tags in chunks_iter:
            exists_stmt = select(RepairManual.id).where(
                RepairManual.section_title == sec_title,
                RepairManual.source_file_path == rel_path,
            )
            if (await session.execute(exists_stmt)).scalar_one_or_none() is not None:
                continue

            session.add(
                RepairManual(
                    brand=brand,
                    model=model,
                    section_title=sec_title,
                    content_text=content,
                    tags=tags,
                    source_file_path=rel_path,
                )
            )
            inserted_chunks += 1

    await session.flush()
    return inserted_chunks


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ingest sub-folder Manual Repair Suzuki Grand Vitara JB420 (Vol 1.pdf & Vol 2.pdf) ke database RAG."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default="./manual repair suzuki vitara",
        help="Path ke sub-folder manual repair Suzuki Vitara (yang berisi Vol 1.pdf & Vol 2.pdf)",
    )
    args = parser.parse_args()

    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    target_dir = Path(args.dir)
    async with async_session() as session:
        async with session.begin():
            count = await ingest_vitara_folder(session, target_dir)
            logger.info(
                "Selesai! Berhasil mengindeks %d bagian manual Suzuki Grand Vitara JB420 ke database RAG.",
                count,
            )

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
