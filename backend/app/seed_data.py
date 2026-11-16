"""
Database seeder — populates the database with realistic Indonesian automotive workshop data.
Run with: python -m app.seed_data
"""

import asyncio
import json
from app.database import engine, async_session_factory, Base
from app.models import (
    User, Customer, Vehicle,
    FaultCategory, FaultCheckpoint, FaultHistory, SymptomCheckpointLink,
    DTCCode, SensorSpec, RepairManual, WiringDiagram,
    Sparepart,
)
from app.utils.security import hash_password


async def seed():
    """Seed the database with sample data."""
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_factory() as db:
        # ══════════════════════════════════════════════════════════════════
        # USERS
        # ══════════════════════════════════════════════════════════════════
        users = [
            User(username="admin", full_name="Admin Bengkel", hashed_password=hash_password("admin123"), role="admin"),
            User(username="budi_mekanik", full_name="Budi Santoso", hashed_password=hash_password("budi123"), role="mekanik"),
            User(username="agus_mekanik", full_name="Agus Prasetyo", hashed_password=hash_password("agus123"), role="mekanik"),
            User(username="sari_kasir", full_name="Sari Wulandari", hashed_password=hash_password("sari123"), role="kasir"),
            User(username="rina_sa", full_name="Rina Handayani", hashed_password=hash_password("rina123"), role="service_advisor"),
        ]
        db.add_all(users)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # CUSTOMERS & VEHICLES
        # ══════════════════════════════════════════════════════════════════
        customers = [
            Customer(name="Pak Hendra Wijaya", phone="081234567890", email="hendra@email.com", address="Jl. Sudirman No. 45, Jakarta Selatan"),
            Customer(name="Bu Dewi Lestari", phone="085678901234", address="Jl. Gatot Subroto No. 12, Bandung"),
            Customer(name="Mas Eko Prasetyo", phone="087890123456", address="Jl. Ahmad Yani No. 88, Surabaya"),
            Customer(name="Pak Rudi Hartono", phone="081122334455", email="rudi.h@gmail.com", address="Jl. Diponegoro No. 33, Semarang"),
            Customer(name="Bu Siti Aminah", phone="089912345678", address="Jl. Pahlawan No. 7, Malang"),
        ]
        db.add_all(customers)
        await db.flush()

        vehicles = [
            Vehicle(customer_id=customers[0].id, plate_number="B 1234 XYZ", brand="Toyota", model="Avanza 1.3 G", year=2019, engine_code="1NR-VE", transmission="manual", fuel_type="bensin"),
            Vehicle(customer_id=customers[0].id, plate_number="B 5678 ABC", brand="Toyota", model="Innova 2.0 V", year=2021, engine_code="1TR-FE", transmission="automatic", fuel_type="bensin"),
            Vehicle(customer_id=customers[1].id, plate_number="D 9012 DEF", brand="Honda", model="Jazz GK5 RS", year=2018, engine_code="L15B", transmission="cvt", fuel_type="bensin"),
            Vehicle(customer_id=customers[2].id, plate_number="L 3456 GHI", brand="Mitsubishi", model="Xpander 1.5 Ultimate", year=2022, engine_code="4A91", transmission="automatic", fuel_type="bensin"),
            Vehicle(customer_id=customers[3].id, plate_number="H 7890 JKL", brand="Suzuki", model="Ertiga GL", year=2020, engine_code="K15B", transmission="manual", fuel_type="bensin"),
            Vehicle(customer_id=customers[3].id, plate_number="H 1122 MNO", brand="Suzuki", model="Vitara 1.6", year=2017, engine_code="M16A", transmission="automatic", fuel_type="bensin"),
            Vehicle(customer_id=customers[4].id, plate_number="N 3344 PQR", brand="Daihatsu", model="Xenia 1.3 R", year=2020, engine_code="1NR-VE", transmission="manual", fuel_type="bensin"),
            Vehicle(customer_id=customers[4].id, plate_number="N 5566 STU", brand="Toyota", model="Fortuner 2.4 VRZ", year=2023, engine_code="2GD-FTV", transmission="automatic", fuel_type="diesel"),
        ]
        db.add_all(vehicles)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # FAULT CATEGORIES & CHECKPOINTS
        # ══════════════════════════════════════════════════════════════════
        categories = [
            FaultCategory(name="Engine - Mesin Bensin", description="Masalah mesin pembakaran bensin (fuel injection, ignition, sensor)"),
            FaultCategory(name="Engine - Mesin Diesel", description="Masalah mesin diesel (common rail, turbo, glow plug)"),
            FaultCategory(name="Kelistrikan Body", description="Masalah kelistrikan bodi (lampu, power window, central lock, wiper)"),
            FaultCategory(name="AC - Pendingin", description="Masalah sistem pendingin kabin (kompresor, freon, blower, evaporator)"),
            FaultCategory(name="Transmisi", description="Masalah transmisi manual dan otomatis (kopling, matic, CVT)"),
            FaultCategory(name="Rem", description="Masalah sistem pengereman (disc brake, drum, ABS, master rem)"),
            FaultCategory(name="Suspensi & Kaki-kaki", description="Masalah suspensi, steering, ball joint, tie rod, bearing roda"),
            FaultCategory(name="Pendingin Mesin", description="Masalah sistem pendingin mesin (radiator, thermostat, water pump, kipas)"),
        ]
        db.add_all(categories)
        await db.flush()

        # Checkpoints untuk Mesin Bensin
        engine_checkpoints = [
            FaultCheckpoint(category_id=categories[0].id, name="Cek Busi", description="Periksa kondisi busi (keausan elektroda, warna, gap). Normal gap: 0.8-1.1mm", order_priority=1),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Koil Pengapian", description="Ukur tahanan primer/sekunder koil. Periksa spark dengan tester", order_priority=2),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Injector", description="Periksa semprotan injector (spray pattern). Ukur tahanan: 11-16 Ohm", order_priority=3),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Fuel Pump & Tekanan BBM", description="Ukur tekanan fuel rail: 3.0-3.5 bar (bensin). Dengar suara pompa bensin", order_priority=4),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Sensor TPS", description="Ukur voltase TPS: idle 0.5V, full throttle 4.5V. Cek perlahan dari idle ke full", order_priority=5),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Sensor MAP/MAF", description="Ukur voltase MAP: idle ~1.0V, akselerasi naik. MAF: idle 1.0-1.5V", order_priority=6),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Sensor O2 (Lambda)", description="Sensor O2 upstream: berfluktuasi 0.1-0.9V saat warm. Downstream: stabil ~0.45V", order_priority=7),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Sensor CKP/CMP", description="Periksa sinyal sensor crankshaft dan camshaft. Gap sensor: 0.5-1.5mm", order_priority=8),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Kompresi Silinder", description="Kompresi normal: 11-14 kg/cm² (bensin). Selisih antar silinder max 1 kg/cm²", order_priority=9),
            FaultCheckpoint(category_id=categories[0].id, name="Cek Timing Chain/Belt", description="Periksa keausan timing chain/belt. Cek tanda timing pada gear cam dan crank", order_priority=10),
        ]

        # Checkpoints untuk AC
        ac_checkpoints = [
            FaultCheckpoint(category_id=categories[3].id, name="Cek Tekanan Freon", description="Low side: 25-35 psi (idle), High side: 200-250 psi. Gunakan manifold gauge", order_priority=1),
            FaultCheckpoint(category_id=categories[3].id, name="Cek Kompresor AC", description="Periksa kopling magnet, suara kompresor, dan kebocoran oli. Ukur ampere", order_priority=2),
            FaultCheckpoint(category_id=categories[3].id, name="Cek Blower & Resistor", description="Tes blower di semua speed. Ukur tahanan resistor blower setiap step", order_priority=3),
            FaultCheckpoint(category_id=categories[3].id, name="Cek Evaporator", description="Periksa suhu evaporator (normal: 2-5°C). Cek bau apek dan kebocoran", order_priority=4),
            FaultCheckpoint(category_id=categories[3].id, name="Cek Kondensor & Kipas", description="Periksa kondensor (bersih/kotor), kipas kondensor berputar saat AC on", order_priority=5),
            FaultCheckpoint(category_id=categories[3].id, name="Cek Expansion Valve", description="Periksa pembukaan/penutupan expansion valve. Suhu pipa masuk vs keluar", order_priority=6),
        ]

        # Checkpoints untuk Kelistrikan
        elec_checkpoints = [
            FaultCheckpoint(category_id=categories[2].id, name="Cek Aki/Baterai", description="Ukur voltase aki: 12.4-12.7V (off), 13.8-14.4V (mesin hidup). Load test", order_priority=1),
            FaultCheckpoint(category_id=categories[2].id, name="Cek Alternator/Charging", description="Ukur output alternator: 13.8-14.4V. Cek diode dan regulator", order_priority=2),
            FaultCheckpoint(category_id=categories[2].id, name="Cek Fuse & Relay", description="Periksa semua fuse terkait. Tes relay dengan multimeter (koil: 50-120 Ohm)", order_priority=3),
            FaultCheckpoint(category_id=categories[2].id, name="Cek Grounding/Massa", description="Ukur tahanan ground point: harus < 0.5 Ohm. Bersihkan karat pada ground", order_priority=4),
            FaultCheckpoint(category_id=categories[2].id, name="Cek Wiring/Kabel", description="Periksa kabel putus, lecet, atau terbakar. Ukur continuity kabel", order_priority=5),
        ]

        # Checkpoints untuk Rem
        brake_checkpoints = [
            FaultCheckpoint(category_id=categories[5].id, name="Cek Kampas Rem", description="Periksa ketebalan kampas rem: minimum 2mm. Cek keausan merata/tidak", order_priority=1),
            FaultCheckpoint(category_id=categories[5].id, name="Cek Disc/Piringan Rem", description="Ukur ketebalan piringan rem, periksa alur/goresan. Runout: max 0.05mm", order_priority=2),
            FaultCheckpoint(category_id=categories[5].id, name="Cek Minyak Rem", description="Periksa level minyak rem (DOT3/DOT4). Cek warna: keruh = perlu ganti", order_priority=3),
            FaultCheckpoint(category_id=categories[5].id, name="Cek Master Rem", description="Periksa kebocoran master cylinder. Tes pedal: tidak boleh turun pelan", order_priority=4),
            FaultCheckpoint(category_id=categories[5].id, name="Cek Kaliper Rem", description="Periksa piston kaliper macet/seret. Cek seal dust dan kebocoran", order_priority=5),
        ]

        all_checkpoints = engine_checkpoints + ac_checkpoints + elec_checkpoints + brake_checkpoints
        db.add_all(all_checkpoints)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # FAULT HISTORIES (data riwayat realistis untuk training diagnostic)
        # ══════════════════════════════════════════════════════════════════
        fault_histories = [
            # --- Avanza: Mesin Brebet ---
            FaultHistory(
                vehicle_id=vehicles[0].id, category_id=categories[0].id,
                reported_symptoms="Mesin brebet saat akselerasi, terasa ngempos di RPM rendah, kadang mati sendiri di lampu merah",
                diagnosed_cause="Busi aus dan kotor karbon, gap membesar",
                solution="Ganti busi 4 pcs (NGK BKR6EYA-11). Bersihkan throttle body",
                mechanic_id=users[1].id, mileage_km=85000, repair_cost=350000, resolved=True,
            ),
            # --- Jazz: Mesin pincang ---
            FaultHistory(
                vehicle_id=vehicles[2].id, category_id=categories[0].id,
                reported_symptoms="Mesin pincang, getaran kuat saat idle, suara mesin kasar tidak rata, check engine nyala",
                diagnosed_cause="Koil pengapian silinder 3 lemah/mati",
                solution="Ganti ignition coil silinder 3. Reset ECU",
                mechanic_id=users[1].id, mileage_km=92000, repair_cost=850000, resolved=True,
            ),
            # --- Xpander: Mesin ngelitik ---
            FaultHistory(
                vehicle_id=vehicles[3].id, category_id=categories[0].id,
                reported_symptoms="Mesin ngelitik saat menanjak, tenaga berkurang, brebet di RPM tinggi",
                diagnosed_cause="Sensor knock rusak + karbon tebal di ruang bakar",
                solution="Ganti knock sensor. Decarbonize ruang bakar. Tune up lengkap",
                mechanic_id=users[2].id, mileage_km=45000, repair_cost=1200000, resolved=True,
            ),
            # --- Avanza: AC tidak dingin ---
            FaultHistory(
                vehicle_id=vehicles[0].id, category_id=categories[3].id,
                reported_symptoms="AC tidak dingin, angin keluar tapi hangat, kadang bau apek dari dashboard",
                diagnosed_cause="Freon habis karena kebocoran di evaporator",
                solution="Ganti evaporator AC. Isi freon R134a 500gr. Ganti dryer filter",
                mechanic_id=users[2].id, mileage_km=88000, repair_cost=3500000, resolved=True,
            ),
            # --- Ertiga: AC kurang dingin ---
            FaultHistory(
                vehicle_id=vehicles[4].id, category_id=categories[3].id,
                reported_symptoms="AC kurang dingin, blower normal tapi udara tidak sejuk, kompresor hidup-mati terus",
                diagnosed_cause="Freon kurang (tekanan low side rendah) + kondensor kotor",
                solution="Cuci kondensor. Tambah freon R134a 200gr. Normal kembali",
                mechanic_id=users[1].id, mileage_km=62000, repair_cost=250000, resolved=True,
            ),
            # --- Innova: Lampu depan mati sebelah ---
            FaultHistory(
                vehicle_id=vehicles[1].id, category_id=categories[2].id,
                reported_symptoms="Lampu depan kiri mati, sudah ganti bohlam tapi tetap mati, fuse utuh",
                diagnosed_cause="Relay headlamp rusak + soket bohlam terbakar/korosi",
                solution="Ganti relay headlamp. Ganti soket bohlam H4. Bersihkan ground point",
                mechanic_id=users[1].id, mileage_km=110000, repair_cost=200000, resolved=True,
            ),
            # --- Xenia: Power window macet ---
            FaultHistory(
                vehicle_id=vehicles[6].id, category_id=categories[2].id,
                reported_symptoms="Power window pintu depan kanan tidak bisa naik turun, tidak ada suara motor sama sekali",
                diagnosed_cause="Switch power window rusak (tidak ada arus ke motor)",
                solution="Ganti switch power window depan kanan",
                mechanic_id=users[2].id, mileage_km=75000, repair_cost=350000, resolved=True,
            ),
            # --- Jazz: Rem bunyi ---
            FaultHistory(
                vehicle_id=vehicles[2].id, category_id=categories[5].id,
                reported_symptoms="Rem depan bunyi berdecit saat pengereman, terasa getar di pedal rem",
                diagnosed_cause="Kampas rem depan habis + disc brake sudah tipis dan beralur",
                solution="Ganti kampas rem depan dan disc brake depan sepasang",
                mechanic_id=users[1].id, mileage_km=95000, repair_cost=1800000, resolved=True,
            ),
            # --- Avanza: Mesin overheat ---
            FaultHistory(
                vehicle_id=vehicles[0].id, category_id=categories[7].id,
                reported_symptoms="Temperatur mesin naik tinggi sampai merah, air radiator cepat habis, ada uap dari kap mesin",
                diagnosed_cause="Thermostat macet tertutup + kebocoran upper hose radiator",
                solution="Ganti thermostat + upper hose radiator. Kuras coolant dan isi baru",
                mechanic_id=users[2].id, mileage_km=90000, repair_cost=650000, resolved=True,
            ),
            # --- Fortuner: Mesin diesel ngebul putih ---
            FaultHistory(
                vehicle_id=vehicles[7].id, category_id=categories[1].id,
                reported_symptoms="Asap putih tebal saat start pagi, mesin diesel kasar idle, tenaga kurang saat dingin",
                diagnosed_cause="Glow plug mati 2 buah (silinder 1 dan 3)",
                solution="Ganti glow plug 4 pcs. Cek timer glow plug relay - OK",
                mechanic_id=users[1].id, mileage_km=35000, repair_cost=1600000, resolved=True,
            ),
        ]
        db.add_all(fault_histories)
        await db.flush()

        # Symptom-Checkpoint Links (yang mana checkpoint yang ditemukan sbg penyebab)
        symptom_links = [
            # Avanza brebet -> busi adalah penyebab
            SymptomCheckpointLink(fault_history_id=fault_histories[0].id, checkpoint_id=engine_checkpoints[0].id, was_cause=True, notes="Busi no 2 dan 4 gap membesar 1.5mm, hitam karbon"),
            SymptomCheckpointLink(fault_history_id=fault_histories[0].id, checkpoint_id=engine_checkpoints[1].id, was_cause=False, notes="Koil normal"),
            SymptomCheckpointLink(fault_history_id=fault_histories[0].id, checkpoint_id=engine_checkpoints[4].id, was_cause=False, notes="TPS normal 0.5V idle"),

            # Jazz pincang -> koil penyebab
            SymptomCheckpointLink(fault_history_id=fault_histories[1].id, checkpoint_id=engine_checkpoints[0].id, was_cause=False, notes="Busi masih bagus"),
            SymptomCheckpointLink(fault_history_id=fault_histories[1].id, checkpoint_id=engine_checkpoints[1].id, was_cause=True, notes="Koil silinder 3 mati total, tidak ada spark"),
            SymptomCheckpointLink(fault_history_id=fault_histories[1].id, checkpoint_id=engine_checkpoints[2].id, was_cause=False, notes="Injector spray normal"),

            # Xpander ngelitik -> sensor knock
            SymptomCheckpointLink(fault_history_id=fault_histories[2].id, checkpoint_id=engine_checkpoints[0].id, was_cause=False, notes="Busi normal"),
            SymptomCheckpointLink(fault_history_id=fault_histories[2].id, checkpoint_id=engine_checkpoints[7].id, was_cause=False, notes="CKP/CMP signal OK"),
            SymptomCheckpointLink(fault_history_id=fault_histories[2].id, checkpoint_id=engine_checkpoints[8].id, was_cause=False, notes="Kompresi rata 12.5 kg/cm²"),

            # Avanza AC -> evaporator bocor
            SymptomCheckpointLink(fault_history_id=fault_histories[3].id, checkpoint_id=ac_checkpoints[0].id, was_cause=False, notes="Tekanan 0/0 psi - freon kosong"),
            SymptomCheckpointLink(fault_history_id=fault_histories[3].id, checkpoint_id=ac_checkpoints[1].id, was_cause=False, notes="Kompresor OK setelah diisi freon"),
            SymptomCheckpointLink(fault_history_id=fault_histories[3].id, checkpoint_id=ac_checkpoints[3].id, was_cause=True, notes="Kebocoran di evaporator ditemukan dengan detektor UV"),

            # Ertiga AC kurang dingin -> freon kurang + kondensor kotor
            SymptomCheckpointLink(fault_history_id=fault_histories[4].id, checkpoint_id=ac_checkpoints[0].id, was_cause=True, notes="Low side: 15 psi (harusnya 25-35)"),
            SymptomCheckpointLink(fault_history_id=fault_histories[4].id, checkpoint_id=ac_checkpoints[4].id, was_cause=True, notes="Kondensor sangat kotor debu dan lumpur"),

            # Innova lampu mati -> relay + soket
            SymptomCheckpointLink(fault_history_id=fault_histories[5].id, checkpoint_id=elec_checkpoints[2].id, was_cause=True, notes="Relay headlamp LH tidak bunyi klik, koil putus"),
            SymptomCheckpointLink(fault_history_id=fault_histories[5].id, checkpoint_id=elec_checkpoints[4].id, was_cause=True, notes="Soket bohlam terbakar, pin korosi"),
            SymptomCheckpointLink(fault_history_id=fault_histories[5].id, checkpoint_id=elec_checkpoints[3].id, was_cause=False, notes="Ground point OK"),

            # Jazz rem bunyi -> kampas + disc
            SymptomCheckpointLink(fault_history_id=fault_histories[7].id, checkpoint_id=brake_checkpoints[0].id, was_cause=True, notes="Kampas rem depan tersisa 1mm, indikator sudah bunyi"),
            SymptomCheckpointLink(fault_history_id=fault_histories[7].id, checkpoint_id=brake_checkpoints[1].id, was_cause=True, notes="Disc brake beralur dalam, ketebalan dibawah limit"),
        ]
        db.add_all(symptom_links)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # DTC CODES
        # ══════════════════════════════════════════════════════════════════
        dtc_codes = [
            DTCCode(
                code="P0300", description_en="Random/Multiple Cylinder Misfire Detected",
                description_id="Misfire acak/multiple silinder terdeteksi",
                possible_causes=json.dumps(["Busi aus/rusak", "Koil pengapian lemah", "Injector tersumbat", "Kompresi rendah", "Timing off", "Kebocoran vakum"]),
                diagnostic_steps=json.dumps(["Scan live data - cek misfire counter per silinder", "Cek busi semua silinder", "Tes koil pengapian satu per satu", "Cek injector spray pattern", "Tes kompresi silinder", "Cek kebocoran intake manifold"]),
                severity="high", system_category="powertrain",
            ),
            DTCCode(
                code="P0171", description_en="System Too Lean (Bank 1)",
                description_id="Campuran bahan bakar terlalu kurus (Bank 1)",
                possible_causes=json.dumps(["Kebocoran intake manifold", "Sensor MAF kotor", "Fuel pump lemah", "Injector tersumbat", "Sensor O2 rusak", "Filter udara sangat kotor"]),
                diagnostic_steps=json.dumps(["Cek kebocoran vakum intake manifold", "Bersihkan/cek sensor MAF", "Ukur tekanan fuel rail", "Cek live data LTFT (Long Term Fuel Trim)", "Cek sensor O2 upstream", "Periksa filter udara"]),
                sensor_specs=json.dumps({"LTFT_normal": "-10% s/d +10%", "fuel_pressure": "3.0-3.5 bar"}),
                severity="medium", system_category="powertrain",
            ),
            DTCCode(
                code="P0420", description_en="Catalyst System Efficiency Below Threshold (Bank 1)",
                description_id="Efisiensi sistem katalis dibawah ambang batas (Bank 1)",
                possible_causes=json.dumps(["Catalytic converter rusak/aus", "Sensor O2 downstream rusak", "Kebocoran exhaust manifold", "Bahan bakar berkualitas buruk"]),
                diagnostic_steps=json.dumps(["Bandingkan sinyal O2 upstream vs downstream", "Upstream harus fluktuasi, downstream stabil ~0.45V", "Cek kebocoran exhaust", "Tes backpressure exhaust"]),
                severity="medium", system_category="powertrain",
            ),
            DTCCode(
                code="P0335", description_en="Crankshaft Position Sensor A Circuit Malfunction",
                description_id="Kerusakan rangkaian sensor posisi crankshaft A",
                possible_causes=json.dumps(["Sensor CKP rusak", "Kabel/konektor CKP putus", "Gap sensor terlalu lebar", "Reluctor ring rusak/retak", "ECU bermasalah"]),
                diagnostic_steps=json.dumps(["Ukur tahanan sensor CKP: 500-1200 Ohm", "Cek gap sensor: 0.5-1.5mm", "Periksa kabel dan konektor", "Cek sinyal CKP dengan osiloskop", "Periksa reluctor ring di flywheel"]),
                sensor_specs=json.dumps({"resistance": "500-1200 Ohm", "gap": "0.5-1.5mm"}),
                severity="critical", system_category="powertrain",
            ),
            DTCCode(
                code="P0340", description_en="Camshaft Position Sensor A Circuit Malfunction",
                description_id="Kerusakan rangkaian sensor posisi camshaft A",
                possible_causes=json.dumps(["Sensor CMP rusak", "Kabel putus/korosi", "Timing chain kendur", "Gear camshaft aus"]),
                diagnostic_steps=json.dumps(["Ukur tahanan sensor CMP", "Cek sinyal dengan osiloskop", "Periksa timing chain tension", "Cek timing mark"]),
                severity="critical", system_category="powertrain",
            ),
            DTCCode(
                code="P0113", description_en="Intake Air Temperature Sensor 1 Circuit High",
                description_id="Rangkaian sensor suhu udara masuk 1 tinggi",
                possible_causes=json.dumps(["Sensor IAT rusak/putus", "Kabel konektor lepas", "Short circuit ke ground"]),
                diagnostic_steps=json.dumps(["Cek konektor sensor IAT", "Ukur tahanan sensor: ~2.5 kOhm pada 20°C", "Cek voltase di konektor: 0.5-4.5V"]),
                sensor_specs=json.dumps({"resistance_20C": "2.0-3.0 kOhm", "voltage_range": "0.5-4.5V"}),
                severity="low", system_category="powertrain",
            ),
            DTCCode(
                code="C1201", description_en="Engine Control System Malfunction (Toyota)",
                description_id="Kerusakan sistem kontrol mesin (Toyota) - sering muncul bersamaan DTC mesin",
                possible_causes=json.dumps(["DTC mesin aktif (P-code)", "Masalah throttle body", "Sensor pedal akselerator rusak"]),
                diagnostic_steps=json.dumps(["Cek DTC mesin lainnya terlebih dahulu", "Selesaikan DTC powertrain, C1201 biasanya hilang otomatis", "Cek throttle body dan sensor pedal jika tidak ada P-code"]),
                severity="medium", system_category="chassis", brand="Toyota",
            ),
            DTCCode(
                code="B1421", description_en="Driver Side Airbag Circuit Resistance High",
                description_id="Tahanan rangkaian airbag sisi pengemudi tinggi",
                possible_causes=json.dumps(["Konektor kabel spiral (clock spring) kendur", "Clock spring rusak", "Modul airbag bermasalah"]),
                diagnostic_steps=json.dumps(["PERINGATAN: Lepas terminal aki, tunggu 3 menit sebelum kerja airbag", "Cek konektor di bawah setir", "Ukur tahanan clock spring: 2-3 Ohm", "Periksa konektor modul airbag"]),
                severity="high", system_category="body",
            ),
        ]
        db.add_all(dtc_codes)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # SENSOR SPECS
        # ══════════════════════════════════════════════════════════════════
        sensor_specs = [
            SensorSpec(brand="Toyota", model="Avanza 1.3 (1NR-VE)", sensor_name="TPS (Throttle Position Sensor)", normal_value_range="0.5V - 4.5V", unit="V", location="Di throttle body", notes="Idle: ~0.5V, Full: ~4.5V. Kenaikan harus linier"),
            SensorSpec(brand="Toyota", model="Avanza 1.3 (1NR-VE)", sensor_name="MAP (Manifold Absolute Pressure)", normal_value_range="1.0V - 4.5V", unit="V", location="Di intake manifold", notes="Idle: ~1.0V, akselerasi: naik. Konci ON mesin off: ~4.5V"),
            SensorSpec(brand="Toyota", model="Avanza 1.3 (1NR-VE)", sensor_name="ECT (Engine Coolant Temp)", normal_value_range="0.3V - 3.5V", unit="V", location="Di housing thermostat", notes="Dingin: ~3.0V (2.0-3.0 kOhm). Panas 80°C: ~0.5V (200-300 Ohm)"),
            SensorSpec(brand="Toyota", model="Avanza 1.3 (1NR-VE)", sensor_name="O2 Sensor Upstream", normal_value_range="0.1V - 0.9V", unit="V", location="Di exhaust manifold", notes="Harus berfluktuasi antara 0.1-0.9V saat warm up. Frekuensi: 1-3 Hz"),
            SensorSpec(brand="Toyota", model="Avanza 1.3 (1NR-VE)", sensor_name="CKP (Crankshaft Position)", normal_value_range="500 - 1200", unit="Ω", location="Di dekat flywheel/crankshaft pulley", notes="Gap: 0.5-1.5mm. Sinyal AC pulse"),
            SensorSpec(brand="Honda", model="Jazz GK5 (L15B)", sensor_name="TPS", normal_value_range="0.5V - 4.5V", unit="V", location="Throttle body elektronik", notes="Dual TPS: TPS1 naik, TPS2 turun saat buka throttle"),
            SensorSpec(brand="Honda", model="Jazz GK5 (L15B)", sensor_name="MAP Sensor", normal_value_range="1.0V - 4.8V", unit="V", location="Di intake manifold", notes="Idle: ~1.0V. WOT: ~4.0V. Kunci ON mesin off: atmosfer ~4.8V"),
            SensorSpec(brand="Honda", model="Jazz GK5 (L15B)", sensor_name="Injector Resistance", normal_value_range="11.0 - 16.0", unit="Ω", location="Di fuel rail", notes="Ukur tahanan koil injector di suhu ruangan"),
            SensorSpec(brand="Suzuki", model="Ertiga (K15B)", sensor_name="TPS", normal_value_range="0.5V - 4.5V", unit="V", location="Throttle body", notes="Idle: ~0.5V, Full throttle: ~4.5V"),
            SensorSpec(brand="Suzuki", model="Ertiga (K15B)", sensor_name="IAT (Intake Air Temp)", normal_value_range="0.5V - 4.5V", unit="V", location="Di air filter housing / intake", notes="Suhu 20°C: ~2.5V (2.0-3.0 kOhm). Suhu 80°C: ~0.7V"),
            SensorSpec(brand="Mitsubishi", model="Xpander (4A91)", sensor_name="Knock Sensor", normal_value_range="2.5V ± 0.5V", unit="V", location="Di blok silinder", notes="Voltase DC bias ~2.5V. Sinyal AC saat knocking terdeteksi"),
        ]
        db.add_all(sensor_specs)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # SPAREPARTS
        # ══════════════════════════════════════════════════════════════════
        spareparts = [
            Sparepart(part_number="BKR6EYA-11", name="Busi NGK BKR6EYA-11", brand="NGK", category="engine", buy_price=35000, sell_price=55000, stock_quantity=40, min_stock=10, location="Rak A1", supplier="PT Sumber Jaya", unit="pcs"),
            Sparepart(part_number="DEN-IK20TT", name="Busi Iridium Denso IK20TT", brand="Denso", category="engine", buy_price=85000, sell_price=125000, stock_quantity=20, min_stock=8, location="Rak A1", supplier="PT Sumber Jaya", unit="pcs"),
            Sparepart(part_number="OFL-TOY-001", name="Oil Filter Toyota Avanza/Rush", brand="Sakura", category="filter", buy_price=25000, sell_price=45000, stock_quantity=30, min_stock=10, location="Rak B1", supplier="PT Filter Indo", unit="pcs"),
            Sparepart(part_number="AIF-TOY-001", name="Air Filter Toyota Avanza 1.3", brand="Sakura", category="filter", buy_price=35000, sell_price=65000, stock_quantity=15, min_stock=5, location="Rak B2", supplier="PT Filter Indo", unit="pcs"),
            Sparepart(part_number="BPD-TOY-AVZ", name="Brake Pad Depan Toyota Avanza", brand="Akebono", category="brake", buy_price=180000, sell_price=285000, stock_quantity=8, min_stock=4, location="Rak C1", supplier="PT Brake System", unit="set"),
            Sparepart(part_number="BPD-HON-JZZ", name="Brake Pad Depan Honda Jazz GK5", brand="Akebono", category="brake", buy_price=220000, sell_price=350000, stock_quantity=6, min_stock=3, location="Rak C1", supplier="PT Brake System", unit="set"),
            Sparepart(part_number="OLI-SHELL-5W30", name="Oli Shell Helix HX7 5W-30 4L", brand="Shell", category="engine", buy_price=280000, sell_price=380000, stock_quantity=25, min_stock=10, location="Rak D1", supplier="PT Shell Indonesia", unit="pcs"),
            Sparepart(part_number="OLI-TMO-10W40", name="Oli Toyota Motor Oil 10W-40 4L", brand="Toyota", category="engine", buy_price=260000, sell_price=350000, stock_quantity=20, min_stock=10, location="Rak D1", supplier="PT Toyota Parts", unit="pcs"),
            Sparepart(part_number="CLT-PRESTONE-1L", name="Coolant Prestone Ready-to-Use 1L", brand="Prestone", category="engine", buy_price=45000, sell_price=75000, stock_quantity=15, min_stock=5, location="Rak D2", supplier="PT Prestone Indo", unit="pcs"),
            Sparepart(part_number="RLY-HEAD-12V", name="Relay Headlamp 12V 4 Pin", brand="Bosch", category="electrical", buy_price=25000, sell_price=45000, stock_quantity=10, min_stock=5, location="Rak E1", supplier="PT Bosch Indo", unit="pcs"),
            Sparepart(part_number="COIL-TOY-AVZ", name="Ignition Coil Toyota Avanza 1NR-VE", brand="Denso", category="engine", buy_price=350000, sell_price=550000, stock_quantity=4, min_stock=2, location="Rak A2", supplier="PT Sumber Jaya", unit="pcs"),
            Sparepart(part_number="THRM-88C", name="Thermostat 88°C Universal", brand="Tama", category="engine", buy_price=75000, sell_price=125000, stock_quantity=6, min_stock=3, location="Rak F1", supplier="PT Cooling Parts", unit="pcs"),
            Sparepart(part_number="FREON-R134A-500", name="Freon R134a Kaleng 500gr", brand="Chemours", category="ac", buy_price=85000, sell_price=150000, stock_quantity=12, min_stock=5, location="Rak G1", supplier="PT AC Supplies", unit="pcs"),
            Sparepart(part_number="V-BELT-4PK-945", name="V-Belt 4PK945 AC Belt", brand="Bando", category="engine", buy_price=65000, sell_price=110000, stock_quantity=5, min_stock=2, location="Rak A3", supplier="PT Belt Indo", unit="pcs"),
            Sparepart(part_number="MR-DOT3-1L", name="Minyak Rem DOT 3 1 Liter", brand="Prestone", category="brake", buy_price=55000, sell_price=85000, stock_quantity=8, min_stock=3, location="Rak C2", supplier="PT Prestone Indo", unit="pcs"),
        ]
        db.add_all(spareparts)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # REPAIR MANUALS (sample entries for RAG)
        # ══════════════════════════════════════════════════════════════════
        manuals = [
            RepairManual(
                brand="Toyota", model="Avanza", year_from=2012, year_to=2021,
                category="engine", title="Prosedur Tune Up Mesin 1NR-VE",
                content="""PROSEDUR TUNE UP MESIN 1NR-VE (Toyota Avanza 1.3)

1. PEMERIKSAAN BUSI
   - Jenis busi standar: NGK BKR6EYA-11 atau Denso K20HR-U11
   - Gap busi: 1.0 - 1.1 mm
   - Torsi pemasangan: 18 N·m
   - Interval penggantian: 20.000 km (busi standar) / 100.000 km (iridium)

2. PEMERIKSAAN OLI MESIN
   - Spesifikasi: API SN 5W-30 atau 10W-40
   - Kapasitas: 3.4 liter (dengan filter)
   - Interval ganti: 10.000 km atau 6 bulan

3. FILTER UDARA
   - Part number: 17801-BZ050
   - Interval ganti: 40.000 km
   - Cek setiap 20.000 km, bersihkan dengan udara bertekanan

4. THROTTLE BODY
   - Bersihkan dengan carb cleaner setiap 40.000 km
   - Setelah dibersihkan, lakukan prosedur relearn idle:
     a. Nyalakan mesin, biarkan idle 10 menit
     b. Matikan AC dan semua beban kelistrikan
     c. Jika idle masih tidak stabil, reset ECU dengan lepas terminal aki 15 menit

5. TIMING CHAIN
   - Timing chain tidak perlu diganti berkala
   - Cek bunyi rantai berlebihan setiap 100.000 km
   - Ganti jika ada tanda elongation/kendur""",
            ),
            RepairManual(
                brand="Toyota", model="Avanza", year_from=2012, year_to=2021,
                category="electrical", title="Sistem Kelistrikan ECU & Sensor 1NR-VE",
                content="""PINOUT ECU MESIN 1NR-VE (Toyota Avanza)
Konektor ECU: 2 konektor (E11 dan E12)

KONEKTOR E11:
- Pin 1: +B1 (Power 12V dari relay EFI) - Kabel: PUTIH-MERAH
- Pin 2: +B2 (Power 12V backup) - Kabel: PUTIH-MERAH
- Pin 3: IGSW (Ignition switch signal) - Kabel: HITAM-KUNING
- Pin 5: STA (Starter signal) - Kabel: HITAM-MERAH
- Pin 10: E1 (Ground ECU #1) - Kabel: COKLAT
- Pin 11: E2 (Ground ECU #2) - Kabel: COKLAT
- Pin 15: IGT1 (Ignition timing coil #1) - Kabel: KUNING
- Pin 16: IGT2 (Ignition timing coil #2) - Kabel: BIRU
- Pin 17: IGT3 (Ignition timing coil #3) - Kabel: HIJAU
- Pin 18: IGT4 (Ignition timing coil #4) - Kabel: UNGU
- Pin 20: INJ1 (Injector #1) - Kabel: KUNING-HITAM
- Pin 21: INJ2 (Injector #2) - Kabel: BIRU-HITAM
- Pin 22: INJ3 (Injector #3) - Kabel: HIJAU-HITAM
- Pin 23: INJ4 (Injector #4) - Kabel: UNGU-HITAM

KONEKTOR E12:
- Pin 1: VTA1 (TPS signal 1) - Kabel: KUNING-HIJAU
- Pin 2: VTA2 (TPS signal 2) - Kabel: KUNING-BIRU
- Pin 3: VC (Sensor 5V reference) - Kabel: MERAH
- Pin 4: VPA (Pedal Position Sensor) - Kabel: BIRU-MERAH
- Pin 5: EPA (Pedal Position Ground) - Kabel: COKLAT-PUTIH
- Pin 8: THW (Coolant Temp Sensor) - Kabel: HIJAU-KUNING
- Pin 10: OX1 (O2 Sensor Upstream +) - Kabel: PUTIH
- Pin 12: OX2 (O2 Sensor Downstream +) - Kabel: ABU-ABU
- Pin 15: NE+ (CKP Sensor +) - Kabel: PUTIH-BIRU
- Pin 16: NE- (CKP Sensor -) - Kabel: PUTIH-HITAM
- Pin 18: G2+ (CMP Sensor +) - Kabel: ABU-ABU-BIRU
- Pin 20: KNK (Knock Sensor) - Kabel: BIRU-PUTIH

GROUND POINTS:
- E1 (Engine ground): Baut di blok silinder kiri atas
- E2 (Body ground): Baut di inner fender kiri
- E3 (ECU ground): Baut di bracket ECU""",
            ),
        ]
        db.add_all(manuals)
        await db.flush()

        # ══════════════════════════════════════════════════════════════════
        # WIRING DIAGRAMS
        # ══════════════════════════════════════════════════════════════════
        wiring_diagrams = [
            WiringDiagram(
                brand="Toyota", model="Avanza", year_from=2012, year_to=2021,
                system_name="ECU Main (1NR-VE)",
                ecu_pinout=json.dumps([
                    {"pin": "E11-1", "signal": "+B1", "wire_color": "Putih-Merah", "description": "Power 12V dari relay EFI"},
                    {"pin": "E11-10", "signal": "E1", "wire_color": "Coklat", "description": "Ground ECU utama"},
                    {"pin": "E11-15", "signal": "IGT1", "wire_color": "Kuning", "description": "Ignition coil silinder 1"},
                    {"pin": "E11-16", "signal": "IGT2", "wire_color": "Biru", "description": "Ignition coil silinder 2"},
                    {"pin": "E11-20", "signal": "INJ1", "wire_color": "Kuning-Hitam", "description": "Injector silinder 1"},
                    {"pin": "E12-1", "signal": "VTA1", "wire_color": "Kuning-Hijau", "description": "TPS signal 1"},
                    {"pin": "E12-3", "signal": "VC", "wire_color": "Merah", "description": "5V reference untuk sensor"},
                    {"pin": "E12-8", "signal": "THW", "wire_color": "Hijau-Kuning", "description": "Coolant temperature sensor"},
                    {"pin": "E12-15", "signal": "NE+", "wire_color": "Putih-Biru", "description": "Crankshaft position sensor +"},
                    {"pin": "E12-20", "signal": "KNK", "wire_color": "Biru-Putih", "description": "Knock sensor signal"},
                ]),
                ground_points=json.dumps([
                    {"name": "E1 - Engine Ground", "location": "Baut di blok silinder kiri atas", "wire_color": "Coklat"},
                    {"name": "E2 - Body Ground", "location": "Baut di inner fender kiri", "wire_color": "Coklat"},
                    {"name": "E3 - ECU Ground", "location": "Baut di bracket ECU", "wire_color": "Hitam"},
                ]),
                power_sources=json.dumps([
                    {"name": "+B Main", "source": "Fuse EFI 15A → Relay EFI → ECU pin E11-1", "voltage": "12V"},
                    {"name": "VC (5V Ref)", "source": "Internal ECU → pin E12-3", "voltage": "5V"},
                ]),
                notes="Konektor ECU 2 bagian: E11 (power, ignition, injector) dan E12 (sensor signals)",
            ),
        ]
        db.add_all(wiring_diagrams)
        await db.flush()

        await db.commit()

    print("✅ Database seeded successfully!")
    print(f"   👤 {len(users)} users (admin/admin123, budi_mekanik/budi123, sari_kasir/sari123)")
    print(f"   👥 {len(customers)} customers")
    print(f"   🚗 {len(vehicles)} vehicles")
    print(f"   📂 {len(categories)} fault categories")
    print(f"   ✅ {len(all_checkpoints)} diagnostic checkpoints")
    print(f"   📋 {len(fault_histories)} fault history records")
    print(f"   🔗 {len(symptom_links)} symptom-checkpoint links")
    print(f"   🔧 {len(dtc_codes)} DTC codes")
    print(f"   📊 {len(sensor_specs)} sensor specifications")
    print(f"   📦 {len(spareparts)} spareparts")
    print(f"   📖 {len(manuals)} repair manual entries")
    print(f"   ⚡ {len(wiring_diagrams)} wiring diagrams")


if __name__ == "__main__":
    asyncio.run(seed())

