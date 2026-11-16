"""
Database Seeder - Project Bengkel Masa Depan
============================================
Script async (SQLAlchemy 2.0) untuk mengisi data awal (seed data) mencakup:
1. User & Role Bengkel (Admin, Service Advisor, Mekanik, Kasir)
2. Customer & Kendaraan Populer Indonesia (Avanza, Xpander, Innova Reborn, Brio, Vitara)
3. Kategori Kerusakan, Titik Cek Mekanik (FaultCheckpoint), Link Gejala-Checkpoint, & Riwayat Diagnosa
4. Data OBD-II DTC Codes, Sensor Specs (TPS, MAP, O2, CKP), Repair Manual, & Wiring Diagram
5. Stok Sparepart Gudang Awal & Contoh Work Order (PKB)

Cara menjalankan:
    python -m app.db.seed_data
"""

import asyncio
from datetime import datetime, timezone
from decimal import Decimal
import logging
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# Catatan: Sesuaikan path import di bawah ini dengan struktur modul backend Anda
from app.core.config import settings
from app.core.security import get_password_hash
from app.models import (
    Base,
    Customer,
    DTCCode,
    FaultCategory,
    FaultCheckpoint,
    FaultHistory,
    RepairManual,
    SensorSpec,
    Sparepart,
    StockMovement,
    SymptomCheckpointLink,
    Transaction,
    TransactionItem,
    User,
    Vehicle,
    WiringDiagram,
    WorkOrder,
    WorkOrderItem,
)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


async def is_already_seeded(session: AsyncSession) -> bool:
    """Cek apakah database sudah memiliki data awal agar seeder bersifat idempotent."""
    result = await session.execute(select(User.id).limit(1))
    return result.scalar_one_or_none() is not None


async def seed_users(session: AsyncSession) -> dict[str, User]:
    """1. Seed User untuk setiap role utama di bengkel."""
    users_data = [
        {
            "key": "admin",
            "username": "admin_bengkel",
            "full_name": "Budi Santoso (Owner)",
            "email": "admin@bengkelmasadepan.id",
            "role": "admin",
            "password_hash": get_password_hash("Admin123!"),
            "is_active": True,
        },
        {
            "key": "sa",
            "username": "sa_hendri",
            "full_name": "Hendri Pratama (Service Advisor)",
            "email": "hendri.sa@bengkelmasadepan.id",
            "role": "service_advisor",
            "password_hash": get_password_hash("Advisor123!"),
            "is_active": True,
        },
        {
            "key": "mekanik",
            "username": "mekanik_agus",
            "full_name": "Agus Setiawan (Master Technician)",
            "email": "agus.mekanik@bengkelmasadepan.id",
            "role": "mekanik",
            "password_hash": get_password_hash("Mekanik123!"),
            "is_active": True,
        },
        {
            "key": "kasir",
            "username": "kasir_rina",
            "full_name": "Rina Wulandari (Kasir)",
            "email": "rina.kasir@bengkelmasadepan.id",
            "role": "kasir",
            "password_hash": get_password_hash("Kasir123!"),
            "is_active": True,
        },
    ]

    users_map: dict[str, User] = {}
    for item in users_data:
        key = item.pop("key")
        user = User(**item)
        session.add(user)
        users_map[key] = user

    await session.flush()
    logger.info("Berhasil menyiapkan %d data User.", len(users_map))
    return users_map


async def seed_customers_and_vehicles(session: AsyncSession) -> dict[str, Vehicle]:
    """2. Seed data pelanggan dan kendaraan khas pasar Indonesia."""
    customers_data = [
        {
            "name": "Hendra Wijaya",
            "phone": "081234567890",
            "address": "Jl. Raya Darmo No. 45, Surabaya",
            "vehicles": [
                {
                    "key": "avanza",
                    "license_plate": "L 1234 AB",
                    "brand": "Toyota",
                    "model": "Avanza 1.5 G",
                    "year": 2019,
                    "transmission": "AT",
                    "engine_code": "2NR-VE",
                    "vin": "MHKM5EB3JKK012345",
                    "current_km": 68500,
                },
                {
                    "key": "vitara",
                    "license_plate": "L 8899 VX",
                    "brand": "Suzuki",
                    "model": "Grand Vitara 2.0",
                    "year": 2012,
                    "transmission": "AT",
                    "engine_code": "J20A",
                    "vin": "JS3TD54V0C4109876",
                    "current_km": 142000,
                },
            ],
        },
        {
            "name": "Siti Rahmawati",
            "phone": "081398765432",
            "address": "Perum Griya Asri Blok C-12, Sidoarjo",
            "vehicles": [
                {
                    "key": "xpander",
                    "license_plate": "W 4567 QR",
                    "brand": "Mitsubishi",
                    "model": "Xpander Ultimate",
                    "year": 2021,
                    "transmission": "AT",
                    "engine_code": "4A91",
                    "vin": "MMBXLNC2WMH054321",
                    "current_km": 45200,
                }
            ],
        },
        {
            "name": "Wahyu Nugroho",
            "phone": "085711223344",
            "address": "Jl. Soekarno Hatta No. 18, Malang",
            "vehicles": [
                {
                    "key": "innova",
                    "license_plate": "N 9981 KL",
                    "brand": "Toyota",
                    "model": "Kijang Innova Reborn 2.4 V Diesel",
                    "year": 2020,
                    "transmission": "AT",
                    "engine_code": "2GD-FTV",
                    "vin": "MHFJB8EM5L0099887",
                    "current_km": 89000,
                },
                {
                    "key": "brio",
                    "license_plate": "N 1123 YZ",
                    "brand": "Honda",
                    "model": "Brio Satya E",
                    "year": 2022,
                    "transmission": "CVT",
                    "engine_code": "L12B",
                    "vin": "MHRDD1850NJ203948",
                    "current_km": 28400,
                },
            ],
        },
    ]

    vehicles_map: dict[str, Vehicle] = {}
    for c_data in customers_data:
        v_list = c_data.pop("vehicles")
        customer = Customer(**c_data)
        session.add(customer)
        await session.flush()

        for v_data in v_list:
            key = v_data.pop("key")
            vehicle = Vehicle(customer_id=customer.id, **v_data)
            session.add(vehicle)
            vehicles_map[key] = vehicle

    await session.flush()
    logger.info("Berhasil menyiapkan %d Kendaraan pelanggan.", len(vehicles_map))
    return vehicles_map


async def seed_diagnostic_knowledge_base(
    session: AsyncSession, vehicles_map: dict[str, Vehicle]
) -> dict[str, FaultCheckpoint]:
    """
    3. Seed Pilar 1: Smart Fault Diagnostic
    Mencakup FaultCategory, FaultCheckpoint, SymptomCheckpointLink (bobot prior),
    dan FaultHistory (data historis kasus riil untuk perhitungan probabilitas).
    """
    categories_data = {
        "engine": FaultCategory(
            name="Engine & Fuel System",
            description="Sistem pembakaran, injeksi bahan bakar, pengapian, dan sensor mesin.",
        ),
        "electrical": FaultCategory(
            name="Electrical & Ignition",
            description="Sistem pengisian, starter, kelistrikan bodi, ECU, dan jalur massa.",
        ),
        "cooling": FaultCategory(
            name="Cooling & A/C System",
            description="Sistem pendingin mesin, radiator, ekstra fan, dan kompresor AC.",
        ),
        "transmission": FaultCategory(
            name="Transmission & Drivetrain",
            description="Transmisi manual/AT/CVT, kopling, solenoid valve, dan gardan.",
        ),
    }
    for cat in categories_data.values():
        session.add(cat)
    await session.flush()

    checkpoints_data = [
        {
            "key": "coil_spark",
            "category_id": categories_data["engine"].id,
            "code": "CHK-ENG-001",
            "name": "Ignition Coil & Busi Silinder 1-4",
            "inspection_steps": (
                "1. Cek kebocoran arus pada selongsong karet koil.\n"
                "2. Ukur celah dan keausan elektroda busi (standar 0.8-1.1 mm).\n"
                "3. Lakukan power balance test via scanner OBD-II."
            ),
            "estimated_check_minutes": 20,
        },
        {
            "key": "throttle_isc",
            "category_id": categories_data["engine"].id,
            "code": "CHK-ENG-002",
            "name": "Throttle Body & Idle Speed Control (ISC) / ETCS",
            "inspection_steps": (
                "1. Periksa tumpukan karbon pada katup kupu-kupu throttle body.\n"
                "2. Cek bukaan TPS saat idle (standar 3-9%) dan lakukan relearn idle."
            ),
            "estimated_check_minutes": 25,
        },
        {
            "key": "fuel_pump",
            "category_id": categories_data["engine"].id,
            "code": "CHK-ENG-003",
            "name": "Fuel Pump Pressure & Filter Bensin",
            "inspection_steps": (
                "1. Pasang fuel pressure gauge pada jalur fuel rail.\n"
                "2. Pastikan tekanan berada di 40-48 PSI saat mesin hidup.\n"
                "3. Periksa penurunan tekanan (holding pressure) saat kunci kontak OFF."
            ),
            "estimated_check_minutes": 30,
        },
        {
            "key": "ckp_cmp",
            "category_id": categories_data["electrical"].id,
            "code": "CHK-ELC-001",
            "name": "Sensor CKP (Crankshaft) & CMP (Camshaft)",
            "inspection_steps": (
                "1. Ukur tahanan sensor CKP saat suhu kerja (konektor dilepas).\n"
                "2. Cek sinyal pulsa RPM saat cranking melalui live data scanner.\n"
                "3. Periksa keretakan kabel atau oli rembes pada soket CKP."
            ),
            "estimated_check_minutes": 25,
        },
        {
            "key": "cooling_fan",
            "category_id": categories_data["cooling"].id,
            "code": "CHK-COL-001",
            "name": "Motor Extra Fan Radiator, Relay Fan & Thermostat",
            "inspection_steps": (
                "1. Cek putaran motor fan saat suhu ECT menyentuh 95°C atau AC ON.\n"
                "2. Periksa tahanan relay fan dan kondisi sekring utama.\n"
                "3. Cek perbedaan suhu selang radiator atas dan bawah (indikasi thermostat macet)."
            ),
            "estimated_check_minutes": 20,
        },
        {
            "key": "scv_diesel",
            "category_id": categories_data["engine"].id,
            "code": "CHK-ENG-004",
            "name": "Suction Control Valve (SCV) & Filter Solar Commonrail",
            "inspection_steps": (
                "1. Baca target vs actual Fuel Rail Pressure pada scanner (idle ~30-35 MPa).\n"
                "2. Cek indikator water sedimenter dan kondisi kemacetan plunger SCV."
            ),
            "estimated_check_minutes": 35,
        },
    ]

    checkpoints_map: dict[str, FaultCheckpoint] = {}
    for cp_item in checkpoints_data:
        key = cp_item.pop("key")
        cp = FaultCheckpoint(**cp_item)
        session.add(cp)
        checkpoints_map[key] = cp
    await session.flush()

    # SymptomCheckpointLink: Bobot prior pakar untuk kata kunci gejala + DTC
    symptom_links = [
        SymptomCheckpointLink(
            checkpoint_id=checkpoints_map["coil_spark"].id,
            symptom_keyword="mbrebet pincang getar akselerasi",
            dtc_code="P0300",
            base_weight=0.88,
        ),
        SymptomCheckpointLink(
            checkpoint_id=checkpoints_map["throttle_isc"].id,
            symptom_keyword="rpm naik turun langsam tidak stabil mati saat ac nyala",
            dtc_code="P0505",
            base_weight=0.85,
        ),
        SymptomCheckpointLink(
            checkpoint_id=checkpoints_map["fuel_pump"].id,
            symptom_keyword="berat tarikan ngempos tenaga hilang",
            dtc_code="P0171",
            base_weight=0.72,
        ),
        SymptomCheckpointLink(
            checkpoint_id=checkpoints_map["ckp_cmp"].id,
            symptom_keyword="mogok saat panas susah starter mesin mati mendadak",
            dtc_code="P0335",
            base_weight=0.90,
        ),
        SymptomCheckpointLink(
            checkpoint_id=checkpoints_map["cooling_fan"].id,
            symptom_keyword="overheat temperatur naik ac tidak dingin saat macet",
            dtc_code="P0118",
            base_weight=0.87,
        ),
        SymptomCheckpointLink(
            checkpoint_id=checkpoints_map["scv_diesel"].id,
            symptom_keyword="diesel pincang susah hidup pagi limp mode tenaga tertahan",
            dtc_code="P0087",
            base_weight=0.89,
        ),
    ]
    session.add_all(symptom_links)

    # FaultHistory: Riwayat kasus selesai untuk melatih algoritma probabilitas empiris
    histories = [
        FaultHistory(
            vehicle_id=vehicles_map["avanza"].id,
            brand="Toyota",
            model="Avanza",
            symptom_text="Mesin mbrebet pincang saat akselerasi dan tanjakan, lampu check engine kedip",
            dtc_codes="P0300,P0302",
            resolved_checkpoint_id=checkpoints_map["coil_spark"].id,
            resolution_notes="Koil silinder no. 2 bocor arus ke dinding blok, diganti koil original & 4 busi iridium.",
            is_verified=True,
        ),
        FaultHistory(
            vehicle_id=vehicles_map["avanza"].id,
            brand="Toyota",
            model="Avanza",
            symptom_text="Mesin getar mbrebet saat pedal gas diinjak dalam, tarikan berat",
            dtc_codes="P0300",
            resolved_checkpoint_id=checkpoints_map["coil_spark"].id,
            resolution_notes="Karet selongsong koil no. 3 retak dan busi aus.",
            is_verified=True,
        ),
        FaultHistory(
            vehicle_id=vehicles_map["xpander"].id,
            brand="Mitsubishi",
            model="Xpander",
            symptom_text="RPM mesin mbrebet dan naik turun saat idle AC menyala",
            dtc_codes="P0505",
            resolved_checkpoint_id=checkpoints_map["throttle_isc"].id,
            resolution_notes="Pembersihan karbon throttle body dan reset learning nilai bukaan katup via MUT-III.",
            is_verified=True,
        ),
        FaultHistory(
            vehicle_id=vehicles_map["vitara"].id,
            brand="Suzuki",
            model="Grand Vitara",
            symptom_text="Mesin mati mendadak saat macet dan panas, tunggu dingin baru bisa starter lagi",
            dtc_codes="P0335",
            resolved_checkpoint_id=checkpoints_map["ckp_cmp"].id,
            resolution_notes="Sensor CKP J20A putus lilitan dalam saat temperatur kerja tinggi. Diganti sensor CKP baru.",
            is_verified=True,
        ),
        FaultHistory(
            vehicle_id=vehicles_map["brio"].id,
            brand="Honda",
            model="Brio",
            symptom_text="Temperatur overheat naik saat macet dan AC tiba-tiba keluar angin panas",
            dtc_codes="",
            resolved_checkpoint_id=checkpoints_map["cooling_fan"].id,
            resolution_notes="Arang (carbon brush) motor extra fan radiator habis, diganti motor fan assy.",
            is_verified=True,
        ),
        FaultHistory(
            vehicle_id=vehicles_map["innova"].id,
            brand="Toyota",
            model="Kijang Innova Reborn",
            symptom_text="Mesin diesel pincang saat pagi, tenaga tertahan limp mode di RPM 2000",
            dtc_codes="P0087",
            resolved_checkpoint_id=checkpoints_map["scv_diesel"].id,
            resolution_notes="Penggantian filter solar bawah-atas dan pembersihan/penggantian SCV.",
            is_verified=True,
        ),
    ]
    session.add_all(histories)
    await session.flush()
    logger.info("Berhasil menyiapkan Knowledge Base Diagnosa & Riwayat Kasus.")
    return checkpoints_map


async def seed_manuals_dtc_and_wiring(session: AsyncSession) -> None:
    """
    4. Seed Pilar 2: AI Repair Manual & Wiring Assistant (RAG)
    Mencakup DTCCode, SensorSpec, WiringDiagram, dan RepairManual.
    """
    dtc_list = [
        DTCCode(
            code="P0300",
            system="Powertrain - Ignition",
            description_id="Terdeteksi Misfire Acak atau Multi-Silinder (Random/Multiple Cylinder Misfire Detected)",
            possible_causes=(
                "1. Busi aus atau celah tidak sesuai\n"
                "2. Ignition coil lemah atau bocor arus\n"
                "3. Injektor kotor atau tersumbat\n"
                "4. Tekanan fuel pump lemah (< 38 PSI)\n"
                "5. Kebocoran vakum intake manifold"
            ),
            severity_level="HIGH",
        ),
        DTCCode(
            code="P0335",
            system="Powertrain - Sensor",
            description_id="Kerusakan Rangkaian Sensor Posisi Poros Engkol / Crankshaft Position Sensor (CKP) 'A'",
            possible_causes=(
                "1. Sensor CKP lemah saat suhu panas (internal open circuit)\n"
                "2. Konektor sensor CKP kendor atau terkorosi oli\n"
                "3. Kabel sinyal CKP ke ECM putus atau short ke ground\n"
                "4. Gigi reluctor roda gila kotor atau cacat"
            ),
            severity_level="CRITICAL",
        ),
        DTCCode(
            code="P0171",
            system="Powertrain - Fuel Metering",
            description_id="Campuran Bahan Bakar Terlalu Kurus / System Too Lean (Bank 1)",
            possible_causes=(
                "1. Kebocoran udara setelah sensor MAF\n"
                "2. Tekanan pompa bensin turun atau filter bensin mampet\n"
                "3. Sensor MAF kotor oleh debu/oli\n"
                "4. Sensor O2 (Upstream) membaca terlalu lambat"
            ),
            severity_level="MEDIUM",
        ),
        DTCCode(
            code="P0087",
            system="Powertrain - Commonrail Diesel",
            description_id="Tekanan Fuel Rail / Sistem Terlalu Rendah (Fuel Rail/System Pressure - Too Low)",
            possible_causes=(
                "1. Filter solar tersumbat kotoran/gel\n"
                "2. Suction Control Valve (SCV) macet atau aus\n"
                "3. Kebocoran balik (back-leak) berlebih pada injektor commonrail\n"
                "4. Supply pump tekanan tinggi lemah"
            ),
            severity_level="HIGH",
        ),
    ]
    existing_dtc_codes = set((await session.execute(select(DTCCode.code))).scalars().all())
    for d in dtc_list:
        if d.code not in existing_dtc_codes:
            session.add(d)

    sensor_specs = [
        SensorSpec(
            brand="Suzuki",
            model="Grand Vitara 2.0 (J20A)",
            sensor_name="Throttle Position Sensor (TPS)",
            pin_configuration="Pin 1: Vref (+5.0V) | Pin 2: Signal TPS | Pin 3: Sensor Ground (E2)",
            voltage_idle="0.45 - 0.65 V (Katup Tertutup Penuh)",
            voltage_wot="4.10 - 4.60 V (Pedal Gas Penuh / WOT)",
            resistance_ohm="3.5k - 5.5k Ohm (antara Pin 1 dan Pin 3)",
            testing_notes="Tegangan harus naik secara linier tanpa putus saat katup dibuka perlahan.",
        ),
        SensorSpec(
            brand="Suzuki",
            model="Grand Vitara 2.0 (J20A)",
            sensor_name="Crankshaft Position Sensor (CKP - Inductive/Hall)",
            pin_configuration="Pin 1: Power 12V (IG) | Pin 2: Signal Output (5V Square Wave) | Pin 3: Ground",
            voltage_idle="Pulsa gelombang kotak 0V - 5.0V mengikuti putaran mesin",
            voltage_wot="Frekuensi meningkat proporsional terhadap RPM",
            resistance_ohm="Tipe Hall Effect: Jangan ukur dengan Ohmmeter biasa; gunakan osiloskop/multimeter DCV.",
            testing_notes="Panaskan area sensor dengan heatgun (~80°C) jika menguji gejala mati saat mesin panas.",
        ),
        SensorSpec(
            brand="Toyota",
            model="Avanza 1.5 (2NR-VE)",
            sensor_name="Manifold Absolute Pressure (MAP) Sensor",
            pin_configuration="Pin 1: Ground (E2) | Pin 2: IAT Signal | Pin 3: VC (+5.0V) | Pin 4: PIM (MAP Signal)",
            voltage_idle="1.10 - 1.50 V (pada kevakuman idle ~30-35 kPa)",
            voltage_wot="3.80 - 4.20 V (Kunci Kontak ON Mesin Mati / Atmosferik ~101 kPa)",
            resistance_ohm="Ukur berbasis output voltase pada Pin 4 terhadap Ground E2",
            testing_notes="Jika pembacaan kPa tidak berubah saat digas, periksa selang/lubang port vakum dari sumbatan oli.",
        ),
        SensorSpec(
            brand="Universal OBD-II",
            model="Narrowband Zirconia O2 Sensor (Upstream Sensor 1)",
            sensor_name="Heated Oxygen Sensor (HO2S)",
            pin_configuration="2 Kabel Hitam: Heater (12V & Duty ECM) | 1 Biru/Hitam: Signal (+) | 1 Putih/Abu: Ground (-)",
            voltage_idle="Berfluktuasi cepat antara 0.10 V (Lean) hingga 0.90 V (Rich) pada suhu kerja > 350°C",
            voltage_wot="0.80 - 0.92 V (Saat akselerasi penuh / Open Loop Enrichment)",
            resistance_ohm="Rangkaian Heater: 4.0 - 15.0 Ohm pada suhu ruang 25°C",
            testing_notes="Jika tegangan tertahan konstan di 0.45V setelah mesin panas, sensor O2 sudah mati/tidak aktif.",
        ),
    ]
    session.add_all(sensor_specs)

    wiring_diagrams = [
        WiringDiagram(
            brand="Suzuki",
            model="Grand Vitara 2.0 (J20A)",
            year_range="2006-2014",
            system_name="ECM Power, Ground & Ignition Coil Circuit",
            ecu_connector_code="Connector C37 & E61 (32-Pin ECM)",
            pinout_json={
                "E61-Pin-01": {"wire_color": "BLK/OR (Hitam-Oranye)", "function": "Main Ground Massa Mesin (G102)"},
                "E61-Pin-04": {"wire_color": "WHT/RED (Putih-Merah)", "function": "Main Relay Power Supply (+12V)"},
                "C37-Pin-11": {"wire_color": "BRN/YEL (Coklat-Kuning)", "function": "Ignition Coil #1 Trigger Signal"},
                "C37-Pin-12": {"wire_color": "BRN/WHT (Coklat-Putih)", "function": "Ignition Coil #2 Trigger Signal"},
                "C37-Pin-19": {"wire_color": "RED/BLU (Merah-Biru)", "function": "CKP Sensor Signal Input"},
                "C37-Pin-20": {"wire_color": "GRN (Hijau)", "function": "Sensor Common Ground (E2)"},
            },
            ground_locations="Titik Massa G102 berada di belakang blok silinder kanan dekat dudukan throttle body.",
            diagram_image_url="/assets/wiring/suzuki_j20a_ecm_ignition.png",
        ),
        WiringDiagram(
            brand="Toyota",
            model="Avanza / Veloz 1.5 (2NR-VE)",
            year_range="2015-2021",
            system_name="ETCS (Electronic Throttle Control) & Injector Circuit",
            ecu_connector_code="Connector A24 & B31",
            pinout_json={
                "B31-Pin-14": {"wire_color": "BLU (Biru)", "function": "Throttle Actuator Motor (+) M+"},
                "B31-Pin-15": {"wire_color": "PNK (Merah Muda)", "function": "Throttle Actuator Motor (-) M-"},
                "B31-Pin-22": {"wire_color": "YEL (Kuning)", "function": "VTA1 Primary TPS Signal"},
                "B31-Pin-23": {"wire_color": "WHT (Putih)", "function": "VTA2 Secondary TPS Sub-Signal"},
                "A24-Pin-02": {"wire_color": "WHT/BLK (Putih-Hitam)", "function": "EC1 Engine Ground"},
            },
            ground_locations="Titik Massa utama terletak pada kepala silinder sisi intake dan dinding fender kiri.",
            diagram_image_url="/assets/wiring/toyota_2nrve_etcs.png",
        ),
    ]
    session.add_all(wiring_diagrams)

    manuals = [
        RepairManual(
            brand="Suzuki",
            model="Grand Vitara 2.0 (J20A)",
            section_title="Prosedur Pemeriksaan & Penggantian Sensor CKP & Rantai Timing J20A",
            content_text=(
                "1. Lepaskan kabel negatif baterai.\n"
                "2. Apabila muncul kode DTC P0335 dan mesin mati saat suhu kerja tinggi, periksa tegangan suplai "
                "12V pada soket 3-pin sensor CKP menggunakan multimeter.\n"
                "3. Pastikan celah udara (air gap) antara ujung sensor CKP dan rotor reluctor bebas dari serbuk besi.\n"
                "4. Torsi pengencangan baut pengikat sensor CKP: 10 N.m (1.0 kgf-m)."
            ),
            tags="suzuki,vitara,j20a,ckp,p0335,mogok,panas",
        ),
        RepairManual(
            brand="Toyota",
            model="Avanza 1.5 (2NR-VE)",
            section_title="Prosedur Reset & Relearn Idle Speed Setelah Pembersihan Throttle Body",
            content_text=(
                "1. Pastikan suhu kerja mesin sudah mencapai minimal 80°C dan seluruh beban kelistrikan (AC, lampu, audio) OFF.\n"
                "2. Matikan kunci kontak, cabut sekring EFI (15A) dan ETCS (10A) di kotak sekring ruang mesin selama 60 detik.\n"
                "3. Pasang kembali sekring, putar kunci kontak ke ON (jangan distarter) selama 15 detik agar katup kalibrasi.\n"
                "4. Hidupkan mesin tanpa menginjak pedal gas dan biarkan idle selama 5-7 menit hingga RPM stabil di 700 ± 50 RPM."
            ),
            tags="toyota,avanza,2nr-ve,throttle,idle,rpm,reset",
        ),
    ]
    session.add_all(manuals)
    await session.flush()
    logger.info("Berhasil menyiapkan data DTC, Spesifikasi Sensor, Wiring Diagram, & Manual RAG.")


async def seed_inventory_and_sample_work_order(
    session: AsyncSession,
    users_map: dict[str, User],
    vehicles_map: dict[str, Vehicle],
) -> None:
    """
    5. Seed Pilar 3: Gudang Sparepart & Contoh Work Order (PKB) + Kasir
    """
    spareparts_data = [
        {
            "key": "busi_iridium",
            "sku": "SP-TYT-90919-01275",
            "name": "Busi Iridium Dual VVT-i (NR Engine)",
            "category": "Ignition",
            "buy_price": Decimal("85000.00"),
            "sell_price": Decimal("115000.00"),
            "stock_qty": 40,
            "min_stock_alert": 8,
            "unit": "pcs",
        },
        {
            "key": "koil_avanza",
            "sku": "SP-TYT-90919-02258",
            "name": "Ignition Coil Assy Toyota Avanza/Innova Dual VVT-i",
            "category": "Ignition",
            "buy_price": Decimal("480000.00"),
            "sell_price": Decimal("625000.00"),
            "stock_qty": 10,
            "min_stock_alert": 2,
            "unit": "pcs",
        },
        {
            "key": "ckp_vitara",
            "sku": "SP-SZK-33220-63J00",
            "name": "Sensor CKP Crankshaft Suzuki Grand Vitara J20A Original",
            "category": "Sensor",
            "buy_price": Decimal("520000.00"),
            "sell_price": Decimal("685000.00"),
            "stock_qty": 5,
            "min_stock_alert": 1,
            "unit": "pcs",
        },
        {
            "key": "carb_cleaner",
            "sku": "CHM-THB-001",
            "name": "Throttle Body & Intake Cleaner Spray 500ml",
            "category": "Chemical",
            "buy_price": Decimal("38000.00"),
            "sell_price": Decimal("60000.00"),
            "stock_qty": 25,
            "min_stock_alert": 5,
            "unit": "btl",
        },
        {
            "key": "filter_solar_2gd",
            "sku": "SP-TYT-23390-0L070",
            "name": "Filter Solar Element Innova Reborn / Fortuner VRZ 2GD",
            "category": "Filter",
            "buy_price": Decimal("145000.00"),
            "sell_price": Decimal("195000.00"),
            "stock_qty": 15,
            "min_stock_alert": 4,
            "unit": "pcs",
        },
    ]

    existing_skus = set((await session.execute(select(Sparepart.sku))).scalars().all())
    spareparts_map: dict[str, Sparepart] = {}
    for sp_item in spareparts_data:
        key = sp_item.pop("key")
        if sp_item["sku"] in existing_skus:
            sp = (
                await session.execute(
                    select(Sparepart).where(Sparepart.sku == sp_item["sku"])
                )
            ).scalar_one()
        else:
            sp = Sparepart(**sp_item)
            session.add(sp)
        spareparts_map[key] = sp
    await session.flush()

    # Catat StockMovement awal (IN) jika baru dibuat
    for sp in spareparts_map.values():
        if sp.sku not in existing_skus:
            session.add(
                StockMovement(
                    sparepart_id=sp.id,
                    movement_type="INITIAL_IN",
                    qty_change=sp.stock_qty,
                    balance_after=sp.stock_qty,
                    reference_note="Saldo awal seeder gudang",
                    created_by_id=users_map["admin"].id,
                )
            )

    # Buat 1 Contoh Work Order (PKB) yang sudah COMPLETED dan terbayar di Kasir
    existing_wo = (
        await session.execute(
            select(WorkOrder).where(WorkOrder.wo_number == "PKB-202610-0001")
        )
    ).scalar_one_or_none()
    if existing_wo:
        return

    wo = WorkOrder(
        wo_number="PKB-202610-0001",
        vehicle_id=vehicles_map["avanza"].id,
        service_advisor_id=users_map["sa"].id,
        mechanic_id=users_map["mekanik"].id,
        customer_complaint="Mesin mbrebet pincang saat digas, indikator engine menyala",
        initial_dtc_codes="P0300,P0302",
        status="COMPLETED",
        estimated_total=Decimal("1235000.00"),
        created_at=datetime.now(timezone.utc),
    )
    session.add(wo)
    await session.flush()

    wo_items = [
        WorkOrderItem(
            work_order_id=wo.id,
            item_type="SPAREPART",
            sparepart_id=spareparts_map["koil_avanza"].id,
            description="Ignition Coil Assy Silinder #2",
            qty=1,
            unit_price=Decimal("625000.00"),
            subtotal=Decimal("625000.00"),
        ),
        WorkOrderItem(
            work_order_id=wo.id,
            item_type="SPAREPART",
            sparepart_id=spareparts_map["busi_iridium"].id,
            description="Busi Iridium Dual VVT-i (1 Set / 4 pcs)",
            qty=4,
            unit_price=Decimal("115000.00"),
            subtotal=Decimal("460000.00"),
        ),
        WorkOrderItem(
            work_order_id=wo.id,
            item_type="SERVICE_LABOR",
            sparepart_id=None,
            description="Jasa Diagnosa Scanner OBD-II & Penggantian Koil + Busi",
            qty=1,
            unit_price=Decimal("150000.00"),
            subtotal=Decimal("150000.00"),
        ),
    ]
    session.add_all(wo_items)

    # Hitung subtotal, PPN 11%, dan Grand Total untuk Transaksi Kasir
    dpp_subtotal = Decimal("1235000.00")
    ppn_amount = (dpp_subtotal * Decimal("0.11")).quantize(Decimal("0.01"))
    grand_total = dpp_subtotal + ppn_amount

    trx = Transaction(
        invoice_number="INV-202610-0001",
        work_order_id=wo.id,
        cashier_id=users_map["kasir"].id,
        subtotal=dpp_subtotal,
        tax_ppn_rate=Decimal("11.00"),
        tax_ppn_amount=ppn_amount,
        discount_amount=Decimal("0.00"),
        grand_total=grand_total,
        payment_method="QRIS",
        payment_status="PAID",
        paid_at=datetime.now(timezone.utc),
    )
    session.add(trx)
    await session.flush()

    for w_item in wo_items:
        session.add(
            TransactionItem(
                transaction_id=trx.id,
                description=w_item.description,
                item_type=w_item.item_type,
                qty=w_item.qty,
                unit_price=w_item.unit_price,
                subtotal=w_item.subtotal,
            )
        )

    await session.flush()
    logger.info("Berhasil menyiapkan data Gudang Sparepart, PKB, & Transaksi Kasir (PPN 11%%).")


async def run_seeder() -> None:
    """Entrypoint utama eksekusi database seeder."""
    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    
    # Pastikan seluruh 16 tabel ORM sudah dibuat terlebih dahulu
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        async with session.begin():
            from app.db.seed_historical_cases import seed_historical_cases
            await seed_historical_cases(session)

            if await is_already_seeded(session):
                logger.warning("Database sudah berisi data awal. Seeder tabel bengkel dilewati (idempotent).")
                return

            logger.info("Memulai proses seeding database Project Bengkel Masa Depan...")
            users_map = await seed_users(session)
            vehicles_map = await seed_customers_and_vehicles(session)
            await seed_diagnostic_knowledge_base(session, vehicles_map)
            await seed_manuals_dtc_and_wiring(session)
            await seed_inventory_and_sample_work_order(session, users_map, vehicles_map)

        logger.info("Proses seeding selesai dan telah di-commit dengan sukses!")

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(run_seeder())
