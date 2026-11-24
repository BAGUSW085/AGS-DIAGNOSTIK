# Buku Pedoman Reparasi Resmi Toyota Platform IMV Kijang Innova (RM1830EH-ID & RM1871EH-ID · Mesin 1TR-FE 2.0L Bensin, 2KD-FTV 2.5L Diesel & 2TR-FE 2.7L)

- **Pack ID AGOS**: `toyota_innova_gen1_2004_2015`
- **Merek & Model**: Toyota Innova (Toyota Kijang Innova Gen 1 (1TR-FE 2.0L Bensin · 2KD-FTV 2.5L D-4D Diesel · 2TR-FE 2.7L))
- **Rentang Tahun**: 2004–2015
- **Kode Mesin Tercakup**: `1TR-FE, 2KD-FTV, 2TR-FE`
- **Total Kode DTC Terindeks**: **257 Kode DTC**
- **Total Pinout Terminal ECM/ECU**: **865 Terminal**
- **Total Spesifikasi Sensor & Data List**: **353 Parameter**

---

## 1. Ringkasan Bab & Sistem (`toc_rpr.xml`)

| Kategori Servis | Nama Sistem / Mesin | Jumlah Sub-Bab Prosedur |
| :--- | :--- | :---: |
| PENDAHULUAN | KATA PENGANTAR / PERINGATAN / BAB | 2 |
| PENDAHULUAN | TOC2 | 2 |
| PENDAHULUAN | TOC3 | 2 |
| Umum | PENDAHULUAN | 11 |
| Umum | PERSIAPAN | 207 |
| Umum | SPESIFIKASI | 116 |
| Umum | PERAWATAN | 7 |
| Mesin / Sistem Hybrid | ENGINE CONTROL 1KD-FTV | 109 |
| Mesin / Sistem Hybrid | ENGINE CONTROL 2KD-FTV | 173 |
| Mesin / Sistem Hybrid | ENGINE CONTROL 1TR-FE | 101 |
| Mesin / Sistem Hybrid | MEKANIKAL MESIN 1KD-FTV | 44 |
| Mesin / Sistem Hybrid | MEKANIKAL MESIN 2KD-FTV | 47 |
| Mesin / Sistem Hybrid | MEKANIKAL MESIN 1TR-FE | 38 |
| Mesin / Sistem Hybrid | BAHAN BAKR 1KD-FTV | 31 |
| Mesin / Sistem Hybrid | BAHAN BAKAR 2KD-FTV | 42 |
| Mesin / Sistem Hybrid | BAHAN BAKAR 1TR-FE | 29 |
| Mesin / Sistem Hybrid | KONTROL EMISI 1KD-FTV | 14 |
| Mesin / Sistem Hybrid | KONTROL EMISI 2KD-FTV | 23 |
| Mesin / Sistem Hybrid | KONTROL EMISI 1TR-FE | 16 |
| Mesin / Sistem Hybrid | INTAKE / EXHAUST 1KD-FTV | 22 |
| Mesin / Sistem Hybrid | INTAKE / EXHAUST 2KD-FTV | 34 |
| Mesin / Sistem Hybrid | INTAKE / EXHAUST 1TR-FE | 10 |
| Mesin / Sistem Hybrid | PENDINGINAN 1KD-FTV | 16 |
| Mesin / Sistem Hybrid | PENDINGINAN 2KD-FTV | 16 |
| Mesin / Sistem Hybrid | PENDINGINAN 1TR-FE | 16 |
| Mesin / Sistem Hybrid | PELUMASAN 1KD-FTV | 17 |
| Mesin / Sistem Hybrid | PELUMASAN 2KD-FTV | 17 |
| Mesin / Sistem Hybrid | PELUMASAN 1TR-FE | 13 |
| Mesin / Sistem Hybrid | STARTING 1KD-FTV | 20 |
| Mesin / Sistem Hybrid | STARTING 2KD-FTV | 20 |
| Mesin / Sistem Hybrid | STARTING 1TR-FE | 13 |
| Drivetrain | TRANSMISI/TRANSAXLE OTOMATIS A340F | 85 |
| Drivetrain | KOPLING | 25 |
| Drivetrain | TRANSMISI / TRANSAXLE MANUAL R151 | 31 |
| Drivetrain | TRANSMISI / TRANSAXLE MANUAL R151F / R156F | 28 |
| Drivetrain | TRANSMISI / TRANSAXLE MANUAL G50 / G55 | 31 |
| Drivetrain | TRANSFER VF2A / 4WD / AWD | 27 |
| Drivetrain | DRIVE SHAFT / PROPELLER SHAFT | 20 |
| Drivetrain | AXLE DAN DIFFERENSIAL | 48 |
| Suspensi | ALIGNMENT / PENANGANAN DIAGNOSIS | 1 |
| Suspensi | SUSPENSI DEPAN | 35 |
| Suspensi | SUSPENSI BELAKANG | 23 |
| Suspensi | RODA / BAN | 2 |
| Rem | SISTEM KONTROL REM / KONTROL DIMANAMIS | 56 |
| Rem | SISTEM REM (LAINNYA) | 33 |
| Rem | REM (DEPAN) | 18 |
| Rem | REM (BELAKANG) | 15 |
| Rem | REM PARKIR | 15 |
| Steering | SISTEM POWER ASSIST | 16 |
| Steering | STEERING COLUMN | 17 |
| Steering | STEERING GEAR / LINKAGE | 6 |
| Audio/Visual/Telematika | AUDIO / VIDEO | 120 |
| Audio/Visual/Telematika | PARK ASSIST / MONITORING | 13 |
| Power Source / Network | BATERAI / PENGISIAN 1KD-FTV | 10 |
| Power Source / Network | BATERAI / PENGISIAN 2KD-FTV | 10 |
| Power Source / Network | BATERAI / PENGISIAN 1TR-FE | 10 |
| Interior Kendaraan | KUNCI PINTU | 57 |
| Interior Kendaraan | ANTI PENCURIAN / KEYLESS ENTRY | 35 |
| Interior Kendaraan | PENERANGAN (INT) | 25 |
| Interior Kendaraan | METER / GAUGE / DISPLAY | 37 |
| Interior Kendaraan | KACA SPION (INT) | 3 |
| Interior Kendaraan | SUPPLEMENTAL RESTRAINT SYSTEM | 42 |
| Interior Kendaraan | TEMPAT DUDUK | 41 |
| Interior Kendaraan | SEAT BELT | 42 |
| Interior Kendaraan | HEATING / AIR CONDITIONING | 70 |
| Interior Kendaraan | POWER OUTLETS (INT) | 6 |
| Interior Kendaraan | PANEL / TRIM INTERIOR | 33 |
| Eksterior Kendaraan | JENDELA / KACA | 56 |
| Eksterior Kendaraan | PINTU / HATCH | 31 |
| Eksterior Kendaraan | KACA SPION (EXT) | 18 |
| Eksterior Kendaraan | WIPER / WASHER | 22 |
| Eksterior Kendaraan | PENERANGAN (EXT) | 49 |
| Eksterior Kendaraan | HORN | 8 |
| Eksterior Kendaraan | PANEL / TRIM EKSTERIOR | 40 |
| PENDAHULUAN | TOC4 | 2 |
| Sistem EV Mesin / Hybrid | KONTROL MESIN 1KD-FTV | 168 |
| Sistem EV Mesin / Hybrid | KONTROL MESIN 2KD-FTV | 187 |
| Sistem EV Mesin / Hybrid | KONTROL MESIN 2TR-FE | 149 |
| Sistem EV Mesin / Hybrid | MEKANIKAL MESIN 1KD-FTV | 50 |
| Sistem EV Mesin / Hybrid | MEKANIKAL MESIN 2KD-FTV | 64 |
| Sistem EV Mesin / Hybrid | MEKANIKAL MESIN 2TR-FE | 52 |
| Sistem EV Mesin / Hybrid | BAHAN BAKAR 1KD-FTV | 44 |
| Sistem EV Mesin / Hybrid | BAHAN BAKAR 2KD-FTV | 48 |
| Sistem EV Mesin / Hybrid | BAHAN BAKAR 2TR-FE | 43 |
| Sistem EV Mesin / Hybrid | KONTROL EMISI 1KD-FTV | 14 |
| Sistem EV Mesin / Hybrid | KONTROL EMISI 2KD-FTV | 26 |
| Sistem EV Mesin / Hybrid | KONTROL EMISI 2TR-FE | 16 |
| Sistem EV Mesin / Hybrid | INTAKE / EXHAUST 1KD-FTV | 26 |
| Sistem EV Mesin / Hybrid | INTAKE / EXHAUST 2KD-FTV | 35 |
| Sistem EV Mesin / Hybrid | INTAKE / EXHAUST 2TR-FE | 12 |
| Sistem EV Mesin / Hybrid | PENDINGIN 1KD-FTV | 18 |
| Sistem EV Mesin / Hybrid | PENDINGIN 2KD-FTV | 22 |
| Sistem EV Mesin / Hybrid | PENDINGIN 2TR-FE | 18 |
| Sistem EV Mesin / Hybrid | PELUMASAN 1KD-FTV | 21 |
| Sistem EV Mesin / Hybrid | PELUMASAN 2KD-FTV | 22 |
| Sistem EV Mesin / Hybrid | PELUMASAN 2TR-FE | 16 |
| Sistem EV Mesin / Hybrid | STARTING 1KD-FTV | 23 |
| Sistem EV Mesin / Hybrid | STARTING 2KD-FTV | 33 |
| Sistem EV Mesin / Hybrid | STARTING 2TR-FE | 16 |
| Drivetrain | AUTOMATIC TRANSMISSION / TRANSAXLE A340E | 102 |
| Drivetrain | AUTOMATIC TRANSMISSION / TRANSAXLE A340F | 101 |
| Drivetrain | AUTOMATIC TRANSMISSION / TRANSAXLE A343E | 96 |
| Drivetrain | AUTOMATIC TRANSMISSION / TRANSAXLE A343F | 100 |
| Drivetrain | CLUTCH | 30 |
| Drivetrain | TRANSMISSION / TRANSAXLE MANUAL R151 | 42 |
| Drivetrain | TRANSFER / 4WD / AWD / VF4B | 29 |
| Suspensi | ALIGNMENT / HANDLING DIAGNOSIS | 2 |
| Suspensi | FRONT SUSPENSION | 24 |
| Suspensi | REAR SUSPENSION | 19 |
| Suspensi | TIRE / WHEEL (BAN / RODA) | 3 |
| Rem | SISTEM KONTROL REM / KONTROL DINAMIS | 82 |
| Rem | BRAKE (DEPAN) | 12 |
| Rem | BRAKE (BELAKANG) | 9 |
| Rem | PARKING BRAKE | 12 |
| Audio/Visual/Telematik | AUDIO / VIDEO | 210 |
| Audio/Visual/Telematik | PARK ASSIST / MONITORING | 58 |
| Power Source / Network | BATERAI / PENGISIAN 2TR-FE | 12 |
| Interior Kendaraan | DOOR LOCK | 78 |
| Interior Kendaraan | THEFT DETERRENT / KEYLESS ENTRY | 87 |
| Interior Kendaraan | MIRROR (INT) | 6 |
| Interior Kendaraan | SEAT (TEMPAT DUDUK) | 58 |
| Interior Kendaraan | POWER OUTLET (INT) | 15 |
| Interior Kendaraan | TRIM / PANEL INTERIOR | 35 |
| Eksterior Kendaraan | WINDOW / GLASS | 91 |
| Eksterior Kendaraan | DOOR / HATCH | 36 |
| Eksterior Kendaraan | MIRROR (EXT) | 22 |

---

## 2. Tabel Pinout & Tegangan Standar Terminal ECM / ECU

| Terminal (Simbol & Pin) | Warna Kabel & Deskripsi | Kondisi & Standar Tegangan / Tahanan |
| :--- | :--- | :--- |
| `[1KD-FTV] G38-2 (BATT) - C23-7 (E1)` | Warna Kabel: L - BR — Baterai (untuk mengukur tegangan baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[1KD-FTV] G39-9 (IGSW) - C23-7 (E1)` | Warna Kabel: B-O - BR — Ignition switch | Ignition switch ON: 11 sampai 14 V |
| `[1KD-FTV] G39-1 (+B) - C23-7 (E1)` | Warna Kabel: B - BR — Power source ECM | Ignition switch ON: 11 sampai 14 V |
| `[1KD-FTV] G39-8 (MREL) - C23-7 (E1)` | Warna Kabel: W-G - BR — MAIN relay | Ignition switch ON: 11 sampai 14 V / 10 detik berlalu setelah ignition switch off: 0 sampai 1.5 V |
| `[1KD-FTV] C22-18 (VC) - C22-28 (E2)` | Warna Kabel: R-W - BR — Power source sensor (tegangan spesifikasi) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[1KD-FTV] C23-2 (VCS) - C23-1 (E2S)` | Warna Kabel: L-W - R-L — Power source dari fuel pressure sensor (sub) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[1KD-FTV] G39-22 (VPA) - G39-28 (EPA)` | Warna Kabel: W-L - BR-W — Accelerator pedal position sensor (untuk kontrol mesin) | Ignition switch ON, pedal akselerator dibebaskan penuh: 0.6 sampai 1.0 V / Ignition switch ON, pedal akselerator ditekan penuh: 3.0 sampai 4.6 V |
| `[1KD-FTV] G39-23 (VPA2) - G39-29 (EPA2)` | Warna Kabel: GR-G - BR-Y — Accelerator pedal position sensor (untuk deteksi malfungsi sensor) | Ignition switch ON, pedal akselerator dibebaskan penuh: 1.4 sampai 1.8 V / Ignition switch ON, pedal akselerator ditekan penuh: 3.7 sampai 5.0 V |
| `[1KD-FTV] G39-26 (VCPA) - G39-28 (EPA)` | Warna Kabel: LG-R - BR-W — Power source untuk accelerator pedal position sensor (untuk VPA) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[1KD-FTV] G39-27 (VCP2) - G39-29 (EPA2)` | Warna Kabel: BR-R - BR-Y — Power source untuk accelerator pedal position sensor (untuk VPA2) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[1KD-FTV] C23-24 (VG) - C23-32 (EVG)` | Warna Kabel: W-R - B-W — MAF meter | Idling, switch A/C OFF: 0.5 sampai 3.4 V |
| `[1KD-FTV] C22-31 (THA) - C22-28 (E2)` | Warna Kabel: Y-B - BR — IAT sensor (dibuat menyatu dalam MAF meter) | Idling, temperatur udara masuk pada 20°C (68°F): 0.5 sampai 3.4 V |
| `[1KD-FTV] C22-20 (THIA) - C22-28 (E2)` | Warna Kabel: Y-G - BR — Intake air temperature sensor | Temperatur udara atmosfir: 0.5 sampai 3.4 V |
| `[1KD-FTV] C22-19 (THW) - C22-28 (E2)` | Warna Kabel: R-L - BR — ECT sensor | Idling, temperatur cairan pendingin mesin pada 80°C (176°F): 0.2 sampai 1.0 V |
| `[1KD-FTV] G39-7 (STA) - C23-7 (E1)` | Warna Kabel: B-Y*1 - BR L-Y*2 - BR — Sinyal starter | Cranking: 6.0 V atau lebih |
| `[1KD-FTV] C22-24 (#1) - C23-7 (E1) C22-23 (#2) - C23-7 (E1) C22-22 (#3) - C23-7 (E1) C22-2` | Warna Kabel: B-W - BR R - BR V - BR Y-R - BR — Injector | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1KD-FTV] C22-27 (NE+) - C22-34 (NE-)` | Warna Kabel: Y - L — Crankshaft position sensor | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[1KD-FTV] C23-23 (G+) - C23-31 (G-)` | Warna Kabel: Y - L — Camshaft position sensor | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[1KD-FTV] G38-15 (STP) - C23-7 (E1)` | Warna Kabel: G-W - BR — Stop light switch | Ignition switch ON, pedal rem ditekan: 7.5 sampai 14 V / Ignition switch ON, pedal rem dibebaskan: 0 sampai 1.5 V |
| `[1KD-FTV] G38-14 (ST1-) - C23-7 (E1)` | Warna Kabel: R-L - BR — Stop light switch (berlawanan dengan STP) | Ignition switch ON, pedal rem ditekan: 0 sampai 1.5 V / Ignition switch ON, pedal rem dibebaskan: 7.5 sampai 14 V |
| `[1KD-FTV] G39-11 (TC) - C23-7 (E1)` | Warna Kabel: P-B - BR — Terminal TC dari DLC3 | Ignition switch ON: 11 sampai 14 V |
| `[1KD-FTV] G39-12 (W) - C23-7 (E1)` | Warna Kabel: R-B - BR — MIL | MIL menyala: 0 sampai 3 V / MIL tidak menyala: 11 sampai 14 V |
| `[1KD-FTV] G38-17 (SPD) - C23-7 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari meter kombinasi | Ignition switch ON, putar roda secara perlahan: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[1KD-FTV] C23-28 (PIM) - C22-28 (E2)` | Warna Kabel: L-B - BR — Manifold absolute pressure sensor | Berikan vakum 40 kPa (300 mmHg, 11.8 in.Hg): 0.1 sampai 0.7 V / Sama seperti tekanan atmosfir: 0.8 sampai 1.5 V / Berikan tekanan positif 170 kPa (1,275 mmHg, 50.2 in.Hg): 1.6 sampai 2.3 V |
| `[1KD-FTV] G39-10 (IREL) - C23-7 (E1)` | Warna Kabel: B-W - BR — EDU relay | Ignition switch off: 11 sampai 14 V / Idling: 0 sampai 1.5 V |
| `[1KD-FTV] G39-4 (TACH) - C23-7 (E1)` | Warna Kabel: B-W - BR — Putaran mesin | Idling: Pembangkitan pulsa (lihat bentuk gelombang 4) |
| `[1KD-FTV] C22-26 (PCR1) - C22-28 (E2)` | Warna Kabel: R-Y - BR — Sensor tekanan common rail (utama) | Idling: 1.7 sampai 2.2 V |
| `[1KD-FTV] C22-33 (PCR2) - C23-1 (E2S)` | Warna Kabel: G-R - R-L — Common rail pressure sensor (sub) | Idling: 1.2 sampai 1.6 V |
| `[1KD-FTV] G39-15 (GREL) - C23-7 (E1)` | Warna Kabel: R - BR — Relay GLOW | Cranking: 11 sampai 14 V |
| `[1KD-FTV] C22-29 (THF) - C22-28 (E2)` | Warna Kabel: G-B - BR — Fuel temperature sensor | Ignition switch ON: 0.5 sampai 3.4 V |
| `[1KD-FTV] C22-8 (ALT) - C23-7 (E1)` | Warna Kabel: G - BR — Generator duty ratio | Idling: Pembangkitan pulsa (lihat bentuk gelombang 5) |
| `[1KD-FTV] C22-2 (PCV+) - C22-1 (PCV-)` | Warna Kabel: G-W - G-Y — Suction control valve | Idling: Pembangkitan pulsa (lihat bentuk gelombang 6) |
| `[1KD-FTV] C22-25 (INJF) - C23-7 (E1)` | Warna Kabel: P - BR — EDU | Idling: Pembangkitan pulsa (lihat bentuk gelombang 7) |
| `[1KD-FTV] C22-10 (VNTO) - C23-7 (E1)` | Warna Kabel: B-O - BR — Turbo motor driver | Idling: Pembangkitan pulsa (lihat bentuk gelombang 8) |
| `[1KD-FTV] C22-17 (VNTI) - C23-7 (E1)` | Warna Kabel: R-B - BR — Turbo motor driver | Idling: Pembangkitan pulsa (lihat bentuk gelombang 9) |
| `[1KD-FTV] C22-32 (PRD) - C23-7 (E1)` | Warna Kabel: GR - BR — EDU | Ignition switch off: 4 sampai 6.5 V |
| `[1KD-FTV] C23-29 (VLU) - C22-28 (E2)` | Warna Kabel: B - BR — Throttle position sensor | Ignition switch ON, throttle valve Terbuka penuh: 3.6 sampai 4.2 V / Ignition switch ON, throttle valve Tertutup penuh: 0.4 sampai 1.0 V |
| `[1KD-FTV] C23-4 (LUSL) - C23-7 (E1)` | Warna Kabel: GR - BR — Diesel throttle motor duty signal | Panaskan mesin, akselerasi mesin: Pembangkitan pulsa (lihat bentuk gelombang 10) |
| `[1KD-FTV] C22-15 (SCV) - C22-7 (E01)` | Warna Kabel: LG - W-B — VSV untuk swirl control valve | Idling: 0 sampai 1.5 V / Putaran mesin 2600 rpm atau lebih: 11 sampai 14 V |
| `[1KD-FTV] C23-9 (EGR) - C23-7 (E1)` | Warna Kabel: L-R - BR — E-VRV (untuk E-EGR) | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 11) |
| `[1KD-FTV] C23-18 (EGRC) - C23-7 (E1)` | Warna Kabel: Y-B - BR — VSV (untuk EGR Cut) | Ignition switch ON, EGR diputuskan (pedal akselerator ditekan penuh): 0 sampai 1.5 V |
| `[1KD-FTV] G38-22 (CAN+)*1 - C23-7 (E1)` | Warna Kabel: V - BR — Line komunikasi CAN | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 12) |
| `[1KD-FTV] G38-21 (CAN-)*1 - C23-7 (E1)` | Warna Kabel: P - BR — Line komunikasi CAN | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 13) |
| `[2KD-FTV] G38-2 (BATT) - C23-7 (E1)` | Warna Kabel: L - BR — Baterai (untuk mengukur tegangan baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[2KD-FTV] G39-9 (IGSW) - C23-7 (E1)` | Warna Kabel: B-O - BR — Ignition switch | Ignition switch ON: 11 sampai 14 V |
| `[2KD-FTV] G39-1 (+B) - C23-7 (E1)` | Warna Kabel: B - BR — Power source ECM | Ignition switch ON: 11 sampai 14 V |
| `[2KD-FTV] G39-8 (MREL) - C23-7 (E1)` | Warna Kabel: W-G - BR — MAIN relay | Ignition switch ON: 11 sampai 14 V / 10 detik berlalu setelah ignition switch off: 0 sampai 1.5 V |
| `[2KD-FTV] C22-18 (VC) - C22-28 (E2)` | Warna Kabel: R-W - BR — Power source sensor (tegangan spesifikasi) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2KD-FTV] C23-2 (VCS) - C23-1 (E2S)` | Warna Kabel: L-W - R-L — Power source dari fuel pressure sensor (sub) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2KD-FTV] G39-22 (VPA) - G39-28 (EPA)` | Warna Kabel: W-L - BR-W — Accelerator pedal position sensor (untuk kontrol mesin) | Ignition switch ON, pedal akselerator dibebaskan penuh: 0.6 sampai 1.0 V / Ignition switch ON, pedal akselerator ditekan penuh: 2.9 sampai 4.2 V |
| `[2KD-FTV] G39-23 (VPA2) - G39-29 (EPA2)` | Warna Kabel: GR-G - BR-Y — Accelerator pedal position sensor (untuk deteksi malfungsi sensor) | Ignition switch ON, pedal akselerator dibebaskan penuh: 1.4 sampai 1.8 V / Ignition switch ON, pedal akselerator ditekan penuh: 3.7 sampai 5.0 V |
| `[2KD-FTV] G39-26 (VCPA) - G39-28 (EPA)` | Warna Kabel: LG-R - BR-W — Power source untuk accelerator pedal position sensor (untuk VPA) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[2KD-FTV] G39-27 (VCP2) - G39-29 (EPA2)` | Warna Kabel: BR-R - BR-Y — Power source untuk accelerator pedal position sensor (untuk VPA2) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[2KD-FTV] C23-24 (VG) - C23-32 (EVG)` | Warna Kabel: W-R - B-W — MAF meter | Idling, switch A/C OFF: 0.5 sampai 3.4 V |
| `[2KD-FTV] C22-31 (THA) - C22-28 (E2)` | Warna Kabel: Y-B - BR — IAT sensor (dibuat menyatu dalam MAF meter) | Idling, temperatur udara masuk pada 20°C (68°F): 0.5 sampai 3.4 V |
| `[2KD-FTV] C22-19 (THW) - C22-28 (E2)` | Warna Kabel: R-L - BR — ECT sensor | Idling, temperatur cairan pendingin mesin pada 80°C (176°F): 0.2 sampai 1.0 V |
| `[2KD-FTV] G39-7 (STA) - C23-7 (E1)` | Warna Kabel: L-Y - BR — Sinyal starter | Cranking: 6.0 V atau lebih |
| `[2KD-FTV] C22-24 (#1) - C23-7 (E1) C22-23 (#2) - C23-7 (E1) C22-22 (#3) - C23-7 (E1) C22-2` | Warna Kabel: B-W - BR R - BR V - BR Y-R - BR — Injector | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[2KD-FTV] C22-27 (NE+) - C22-34 (NE-)` | Warna Kabel: Y - L — Crankshaft position sensor | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[2KD-FTV] C23-23 (G+) - C23-31 (G-)` | Warna Kabel: Y - L — Camshaft position sensor | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[2KD-FTV] G38-15 (STP) - C23-7 (E1)` | Warna Kabel: G-W - BR — Stop light switch | Ignition switch ON, pedal rem ditekan: 7.5 sampai 14 V / Ignition switch ON, pedal rem dibebaskan: 0 sampai 1.5 V |
| `[2KD-FTV] G38-14 (ST1-) - C23-7 (E1)` | Warna Kabel: R-L - BR — Stop light switch (berlawanan dengan STP) | Ignition switch ON, pedal rem ditekan: 0 sampai 1.5 V / Ignition switch ON, pedal rem dibebaskan: 7.5 sampai 14 V |
| `[2KD-FTV] G39-11 (TC) - C23-7 (E1)` | Warna Kabel: P-B - BR — Terminal TC dari DLC3 | Ignition switch ON: 11 sampai 14 V |
| `[2KD-FTV] G39-12 (W) - C23-7 (E1)` | Warna Kabel: R-B - BR — MIL | MIL menyala: 0 sampai 3 V / MIL tidak menyala: 11 sampai 14 V |
| `[2KD-FTV] G38-17 (SPD) - C23-7 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari meter kombinasi | Ignition switch ON, putar roda secara perlahan: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[2KD-FTV] C23-28 (PIM) - C22-28 (E2)` | Warna Kabel: L-B - BR — Manifold absolute pressure sensor | Berikan vakum 40 kPa (300 mmHg, 11.8 in.Hg): 0.1 sampai 0.7 V / Sama seperti tekanan atmosfir: 0.8 sampai 1.5 V / Berikan tekanan positif 170 kPa (1,275 mmHg, 50.2 in.Hg): 1.6 sampai 2.3 V |
| `[2KD-FTV] G39-10 (IREL) - C23-7 (E1)` | Warna Kabel: B-W - BR — EDU relay | Ignition switch off: 11 sampai 14 V / Idling: 0 sampai 1.5 V |
| `[2KD-FTV] G39-4 (TACH) - C23-7 (E1)` | Warna Kabel: B-W - BR — Putaran mesin | Idling: Pembangkitan pulsa (lihat bentuk gelombang 4) |
| `[2KD-FTV] C22-26 (PCR1) - C22-28 (E2)` | Warna Kabel: R-Y - BR — fuel pressure sensor (utama) | Idling: 1.7 sampai 2.2 V |
| `[2KD-FTV] C22-33 (PCR2) - C23-1 (E2S)` | Warna Kabel: G-R - R-L — fuel pressure sensor (sub) | Idling: 1.2 sampai 1.6 V |
| `[2KD-FTV] G39-15 (GREL) - C23-7 (E1)` | Warna Kabel: R - BR — Relay GLOW | Cranking: 11 sampai 14 V |
| `[2KD-FTV] C22-29 (THF) - C22-28 (E2)` | Warna Kabel: G-B - BR — Fuel temperature sensor | Ignition switch ON: 0.5 sampai 3.4 V |
| `[2KD-FTV] C22-8 (ALT) - C23-7 (E1)` | Warna Kabel: G - BR — Generator duty ratio | Idling: Pembangkitan pulsa (lihat bentuk gelombang 5) |
| `[2KD-FTV] C22-2 (PCV+) - C22-1 (PCV-)` | Warna Kabel: G-W - G-Y — Suction control valve | Idling: Pembangkitan pulsa (lihat bentuk gelombang 6) |
| `[2KD-FTV] C22-25 (INJF) - C23-7 (E1)` | Warna Kabel: P - BR — EDU | Idling: Pembangkitan pulsa (lihat bentuk gelombang 7) |
| `[2KD-FTV] C22-32 (PRD) - C23-7 (E1)` | Warna Kabel: GR - BR — EDU | Ignition switch off: 4 sampai 6.5 V |
| `[2KD-FTV] C23-29 (VLU) - C22-28 (E2)` | Warna Kabel: B - BR — Throttle position sensor | Ignition switch ON, throttle valve Terbuka penuh: 3.6 sampai 4.2 V / Ignition switch ON, throttle valve Tertutup penuh: 0.4 sampai 1.0 V |
| `[2KD-FTV] C23-4 (LUSL) - C23-7 (E1)` | Warna Kabel: GR - BR — Diesel throttle motor duty signal | Panaskan mesin, akselerasi mesin: Pembangkitan pulsa (lihat bentuk gelombang 8) |
| `[2KD-FTV] C23-9 (EGR) - C23-7 (E1)` | Warna Kabel: L-R - BR — E-VRV (untuk E-EGR) | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 9) |
| `[2KD-FTV] C23-33 (EGLS) - C23-7 (E1)` | Warna Kabel: L-Y - BR — EGR valve position sensor | Ignition switch ON: 0.6 sampai 1.4 V / Idling: 1.9 sampai 2.9 V |
| `[2KD-FTV] C22-20 (THIA) - C22-28 (E2)` | Warna Kabel: Y-G - BR — Intake air temperature sensor | Temperatur udara atmosfir: 0.5 sampai 3.4 V |
| `[2KD-FTV] C22-10 (VNTO) - C23-7 (E1)` | Warna Kabel: B-O - BR — Turbo motor driver | Idling: Pembangkitan pulsa (lihat bentuk gelombang 8) |
| `[2KD-FTV] C22-17 (VNTI) - C23-7 (E1)` | Warna Kabel: R-B - BR — Turbo motor driver | Idling: Pembangkitan pulsa (lihat bentuk gelombang 9) |
| `[2KD-FTV] C22-15 (SCV) - C22-7 (E01)` | Warna Kabel: LG - W-B — VSV untuk swirl control valve | Idling: 0 sampai 1.5 V / Putaran mesin 2600 rpm atau lebih: 11 sampai 14 V |
| `[2KD-FTV] C23-18 (EGRC) - C23-7 (E1)` | Warna Kabel: Y-B - BR — VSV (untuk EGR Cut) | Ignition switch ON, EGR diputuskan (pedal akselerator ditekan penuh): 0 sampai 1.5 V |
| `[1TR-FE] G89-3 (BATT) - C75-3 (E1)` | Warna Kabel: L - BR — Baterai (untuk mengukur tegangan baterai dan untuk memori ECM) | Selalu: 11 sampai 14 V |
| `[1TR-FE] G89-7 (+BM) - C75-3 (E1)` | Warna Kabel: R-W - BR — Power source throttle actuator | Selalu: 11 sampai 14 V |
| `[1TR-FE] G89-9 (IGSW) - C75-3 (E1)` | Warna Kabel: B-O - BR — Ignition switch | Ignition switch ON: 11 sampai 14 V |
| `[1TR-FE] G89-1 (+B) - C75-3 (E1)` | Warna Kabel: B - BR — Power source ECM | Ignition switch ON: 11 sampai 14 V |
| `[1TR-FE] C75-13 (OC1+) - C75-12 (OC1-)` | Warna Kabel: P-L - Y — Camshaft timing oil control valve | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[1TR-FE] G89-8 (MREL) - C75-3 (E1)` | Warna Kabel: W-G - BR — MAIN relay | Ignition switch ON: 11 sampai 14 V |
| `[1TR-FE] C76-28 (VG) - C76-30 (E2G)` | Warna Kabel: L-W - L-R — Mass air flow meter | Idling, shift lever di posisi netral: 0.5 sampai 3.0 V |
| `[1TR-FE] C76-29 (THA) - C75-28 (E2)` | Warna Kabel: L-B - BR — Intake air temperature sensor | Idling, temperatur udara masuk 20°C (68°F): 0.5 sampai 3.4 V |
| `[1TR-FE] C75-32 (THW) - C75-28 (E2)` | Warna Kabel: B - BR — Engine coolant temperature sensor | Idling, temperatur cairan pendingin mesin 80°C (176°F): 0.2 sampai 1.0 V |
| `[1TR-FE] C75-18 (VC) - C75-28 (E2)` | Warna Kabel: LG-B - BR — Power source untuk throttle position sensor (tegangan tetap) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[1TR-FE] C75-20 (VTA1) - C75-28 (E2)` | Warna Kabel: B-R - BR — Throttle position sensor (untuk kontrol mesin) | Ignition switch ON, Throttle valve tertutup penuh: 0.5 sampai 1.1 V / Ignition switch ON, Throttle valve terbuka penuh: 3.2 sampai 4.8 V |
| `[1TR-FE] C75-19 (VTA2) - C75-28 (E2)` | Warna Kabel: LG - BR — Throttle position sensor (untuk deteksi malfungsi sensor) | Ignition switch ON, Throttle valve tertutup penuh: 2.1 sampai 3.1 V / Ignition switch ON, Throttle valve terbuka penuh: 4.6 sampai 5.0 V |
| `[1TR-FE] G89-18 (VPA) - G89-20 (EPA)` | Warna Kabel: W-L - BR-W — Accelerator pedal position sensor (untuk kontrol mesin) | Ignition switch ON, pedal akselerator dibebaskan: 0.5 sampai 1.1 V / Ignition switch ON, pedal akselerator ditekan penuh: 2.6 sampai 4.5 V |
| `[1TR-FE] G89-19 (VPA2) - G89-21 (EPA2)` | Warna Kabel: GR-G - BR-Y — Accelerator pedal position sensor (untuk deteksi malfungsi sensor) | Ignition switch ON, pedal akselerator dibebaskan: 1.2 sampai 2.0 V / Ignition switch ON, pedal akselerator ditekan penuh: 3.4 sampai 5.3 V |
| `[1TR-FE] G89-26 (VCPA) - G89-20 (EPA)` | Warna Kabel: LG-R - BR-W — Power source untuk accelerator pedal position sensor (untuk VPA) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[1TR-FE] G89-27 (VCP2) - G89-21 (EPA2)` | Warna Kabel: BR-R - BR-Y — Power source untuk accelerator pedal position sensor (untuk VPA2) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[1TR-FE] C75-21 (A1A+) - C75-28 (E2)` | Warna Kabel: B - BR — Heated oxygen sensor | Putaran mesin dipertahankan pada 2.500 rpm selama 2 menit setelah pemanasan sensor: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[1TR-FE] C75-1 (HA1A) - C76-4 (E03)` | Warna Kabel: Y - W-B — Heated oxygen sensor heater | Ignition switch ON: 11 sampai 14 V |
| `[1TR-FE] C76-6 (#10) - C75-7 (E01)` | Warna Kabel: L - W-B — Injector bahan bakar | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[1TR-FE] C76-5 (#20) - C75-7 (E01)` | Warna Kabel: G - W-B — Injector bahan bakar | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[1TR-FE] C76-2 (#30) - C75-7 (E01)` | Warna Kabel: R - W-B — Injector bahan bakar | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[1TR-FE] C76-1 (#40) - C75-7 (E01)` | Warna Kabel: W - W-B — Injector bahan bakar | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[1TR-FE] C75-29 (KNK1) - C75-30 (EKNK)` | Warna Kabel: B - W — Knock sensor | Putaran mesin dipertahankan pada 4.000 rpm setelah mesin dipanaskan: Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[1TR-FE] C75-26 (G2) - C75-34 (NE-)` | Warna Kabel: R - G — Camshaft position sensor | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 5) |
| `[1TR-FE] C75-27 (NE+) - C75-34 (NE-)` | Warna Kabel: L - G — Crankshaft position sensor | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 5) |
| `[1TR-FE] C75-17 (IGT1) - C75-3 (E1)` | Warna Kabel: R - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[1TR-FE] C75-16 (IGT2) - C75-3 (E1)` | Warna Kabel: R-L - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[1TR-FE] C75-15 (IGT3) - C75-3 (E1)` | Warna Kabel: G-B - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[1TR-FE] C75-14 (IGT4) - C75-3 (E1)` | Warna Kabel: G - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[1TR-FE] C75-23 (IGF1) - C75-3 (E1)` | Warna Kabel: G-R - BR — Ignition coil (sinyal konfirmasi ignition) | Ignition switch ON: 4.5 sampai 5.5 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[1TR-FE] C76-23 (PRG) - C75-3 (E1)` | Warna Kabel: L - BR — Purge VSV | ignition switch ON: 11 sampai 14 V / Idling, dalam purge control: Pembangkitan pulsa (Lihat bentuk gelombang 7) |
| `[1TR-FE] G88-8 (SPD) - C75-3 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari meter kombinasi | Dikendarai pada 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 8) |
| `[1TR-FE] G89-12 (STA) - C75-3 (E1)` | Warna Kabel: L-Y - BR — Sinyal starter | Cranking: 6,0 V atau lebih tinggi |
| `[1TR-FE] G88-4 (STP) - C75-3 (E1)` | Warna Kabel: G-W - BR — Stop light switch | Pedal rem ditekan: 7.5 sampai 14 V / Pedal rem dibebaskan: Di bawah 1,5 V |
| `[1TR-FE] G89-16 (ST1-) - C75-3 (E1)` | Warna Kabel: R-L - BR — Stop light switch (berlawanan dengan tegangan pada terminal STP) | Ignition switch ON, pedal rem ditekan: Di bawah 1,5 V / Ignition switch ON, pedal rem dibebaskan: 7.5 sampai 14 V |
| `[1TR-FE] C75-5 (M+) - C76-3 (ME01)` | Warna Kabel: B - W-B — Throttle actuator | Idling dengan mesin panas: Pembangkitan pulsa (Lihat bentuk gelombang 9) |
| `[1TR-FE] C75-4 (M-) - C76-3 (ME01)` | Warna Kabel: W - W-B — Throttle actuator | Idling dengan mesin panas: Pembangkitan pulsa (Lihat bentuk gelombang 10) |
| `[1TR-FE] G89-25 (FC) - C75-3 (E1)` | Warna Kabel: LG-B - BR — Fuel pump control | Ignition switch ON: 11 sampai 14 V |
| `[1TR-FE] G88-30 (W) - C75-3 (E1)` | Warna Kabel: R-B - BR — MIL | Ignition switch ON: Di bawah 3,0 V / Idling: 11 sampai 14 V |
| `[1TR-FE] G88-17 (TC) - C75-3 (E1)` | Warna Kabel: P-B - BR — Terminal TC dari DLC3 | Ignition switch ON: 11 sampai 14 V |
| `[1TR-FE] G88-1 (TACH) - C75-3 (E1)` | Warna Kabel: B-W - BR — Putaran mesin | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 11) |
| `[1TR-FE] C75-10 (ALT) - C75-3 (E1)` | Warna Kabel: G - BR — Generator | Ignition switch ON: 11 sampai 14 V |
| `[1TR-FE] G89-15 (ELS) - C75-3 (E1)` | Warna Kabel: G - BR — Beban kelistrikan | Switch taillight on: 7.5 sampai 14 V / Switch taillight off: Di bawah 1,5 V |
| `[1TR-FE] G88-14 (THWO) - C75-3 (E1)` | Warna Kabel: P - BR — Sinyal putaran mesin dikirim ke meter kombinasi | Idling dengan mesin panas: Pembangkitan pulsa |
| `[1TR-FE] C76-32 (PSW) - C75-3 (E1)` | Warna Kabel: G-Y - BR — Switch tekanan oli power steering | Pada saat steering wheel dibelokkan: Di bawah 1,5 V |
| `[TRANSMISI/A/T A340F] C24-12 (NSW) - C24-1 (E1)` | Warna Kabel: L-Y - BR — Sinyal switch PNP | Ignition switch ON Shift lever dalam P atau N: Di bawah 1 V / ignition switch ON Shift lever tidak dalam P atau N: 11 sampai 14 V |
| `[TRANSMISI/A/T A340F] G40-9 (R) - C24-1 (E1)` | Warna Kabel: R-Y - BR — Sinyal switch posisi pemindahan R | Ignition switch ON Shift lever dalam posisi R: 11 sampai 14 V / ignition switch ON Shift lever tidak dalam posisi R: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] G40-8 (D) - C24-1 (E1)` | Warna Kabel: G-Y - BR — Sinyal switch posisi pemindahan D | Ignition switch ON Shift lever di D atau 3: 11 sampai 14 V / ignition switch ON Shift lever tidak di D atau 3: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] G40-12 (3) - C24-1 (E1)` | Warna Kabel: G-O - BR — 3 sinyal switch posisi pemindahan | Ignition switch ON Shift lever di 3: 11 sampai 14 V / ignition switch ON Shift lever tidak di 3: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] G40-11 (2) - C24-1 (E1)` | Warna Kabel: L - BR — 2 sinyal switch posisi pemindahan | Ignition switch ON Shift lever di 2: 11 sampai 14 V / ignition switch ON Shift lever tidak di 2: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] G40-10 (L) - C24-1 (E1)` | Warna Kabel: G-R - BR — Sinyal switch posisi pemindahan L | Ignition switch ON Shift lever di L: 11 sampai 14 V / ignition switch ON Shift lever tidak di L: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] C24-18 (S1) - C24-1 (E1)` | Warna Kabel: GR - BR — Sinyal solenoid S1 | gear ke-1 atau ke-2: 11 sampai 14 V / gigi ke-3 atau gigi ke-4: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] C24-17 (S2) - C24-1 (E1)` | Warna Kabel: W-L - BR — Sinyal solenoid S2 | gigi ke-2 atau gigi ke-3: 11 sampai 14 V / gigi ke-1 atau gigi ke-4: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] C24-20 (SLT+) - C24-19 (SLT-)` | Warna Kabel: G-Y - L-B — Sinyal solenoid SLT | Mesin idle: Pembangkitan pulsa |
| `[TRANSMISI/A/T A340F] C24-16 (SL) - C24-1 (E1)` | Warna Kabel: G - BR — Sinyal solenoid SL | Kecepatan kendaraan 65 km/h (40 mph), lock-up (ON ke OFF): Pembangkitan pulsa (Lihat bentuk gelombang 1) / Kendaraan dikendarai di bawah kondisi lock-up: 11 sampai 14 V |
| `[TRANSMISI/A/T A340F] C24-24 (THOC) - C24-23 (E2)` | Warna Kabel: BR - B-Y — Sinyal ATF temperature sensor | Temperatur ATF: 115℃ (239℉) atau lebih tinggi: Di bawah 1,5 V |
| `[TRANSMISI/A/T A340F] C24-30 (SP2+) - C24-29 (SP2-)` | Warna Kabel: R - G — Sinyal speed sensor SP2 | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[TRANSMISI/A/T A340F] C24-3 (NC0+) - C24-2 (NC0-)` | Warna Kabel: V - P — Sinyal speed sensor NC0 | Mesin idle (Shift lever di P atau N): Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[TRANSMISI/A/T A340F] G40-15 (L4) - C24-1 (E1)` | Warna Kabel: G-W - BR — Sinyal posisi L4 | Ignition switch ON Transfer di L4: Di bawah 1 V / ignition switch ON Transfer tidak di L4: 11 sampai 14 V |
| `[TRANSMISI/A/T A340F] G41-25 (SPD1) - C24-1 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[TRANSMISI/A/T A340F] G41-14 (STP) - C24-1 (E1)` | Warna Kabel: G-W - BR — Sinyal switch lampu STP | Pedal rem diinjak: 7.5 sampai 14 V / Pedal rem dibebaskan: Di bawah 1 V |
| `[TRANSMISI/A/T A340F] C24-11 (STA) - C24-1 (E1)` | Warna Kabel: B-Y - BR — Sinyal starter | Cranking: 6 V atau lebih |
| `[TRANSMISI/A/T A340F] G40-16 (TFN) - C24-1 (E1)` | Warna Kabel: W-G - BR — Sinyal switch posisi pemindahan N | Ignition switch ON Shift lever transfer di posisi N: Di bawah 1 V / ignition switch ON Shift lever transfer tidak di posisi N: 11 sampai 14 V |
| `[TRANSMISI/A/T A340F] G41-6 (IG2) - C24-1 (E1)` | Warna Kabel: B-O - BR — Ignition switch | Ignition switch ON: 11 sampai 14 V |
| `[TRANSMISI/A/T A340F] G41-21 (CAN+) - C24-1 (E1)` | Warna Kabel: V - BR — Line komunikasi CAN | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 5) |
| `[TRANSMISI/A/T A340F] G41-20 (CAN-) - C24-1 (E1)` | Warna Kabel: P - BR — Line komunikasi CAN | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[TRANSMISI/A/T A340F] G39-1 (+B) - C23-7 (E1)` | Warna Kabel: B - BR — Power source ECM | Ignition switch ON: 11 sampai 14 V |
| `[TRANSMISI/A/T A340F] G38-22 (CAN+) - C23-7 (E1)` | Warna Kabel: V - BR — Line komunikasi CAN | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[TRANSMISI/A/T A340F] G38-21 (CAN-) - C23-7 (E1)` | Warna Kabel: P - BR — Line komunikasi CAN | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-1 (+BS) - Masa bodi` | Warna Kabel: W-R — ABS solenoid power supply | Selalu: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-2 (GND1) - Masa bodi` | Warna Kabel: W-B — Masa | Selalu: Di bawah 1 Ω |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-3 (EXI4)*1 - Masa bodi` | Warna Kabel: G-W — Input dari L4 position switch (switch indikator transfer No. 1) | Posisi shift transfer L4: Di bawah 1 Ω |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-10 (STP) - Masa bodi` | Warna Kabel: G-W — Input stop light switch | Pedal rem ditekan: 8 sampai 14 V / Pedal rem dibebaskan: Di bawah 1,5 V |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-17 (EXI)*1 - Masa bodi` | Warna Kabel: R-B — Input dari 4WD detection switch (Differential vacuum actuator assembly) | Ignition switch ON Posisi shift transfer H2: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-18 (PKB) - Masa bodi` | Warna Kabel: L-O — Input switch rem parkir | ignition switch ON Rem parkir digunakan: Di bawah 1,5 V / ignition switch ON Rem parkir dibebaskan: 10 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-22 (EXI2)*2 - Masa bodi` | Warna Kabel: V — Input power supply IG | Ignition switch ON: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-23 (+BM) - Masa bodi` | Warna Kabel: R — ABS motor relay power supply | Selalu: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-24 (GND2) - Masa bodi` | Warna Kabel: W-B — Masa | Selalu: Di bawah 1 Ω |
| `[SISTEM KONTROL REM / KONTROL DIMANAMIS] A13-25 (IG1) - Masa bodi` | Warna Kabel: B — Skid control ECU (Aktuator rem assembly) power supply | ignition switch ON: 11 sampai 14 V |
| `[AUDIO / VIDEO] G5-1 (FR+) - G5-7 (GND)` | Warna Kabel: LG - BR — Sinyal suara (kanan depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G5-2 (FL+) - G5-7 (GND)` | Warna Kabel: P - BR — Sinyal suara (Kiri depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G5-3 (ACC) - G5-7 (GND)` | Warna Kabel: GR - BR — Accessory (On) | Ignition switch off: Di bawah 1 V / Ignition switch ACC: 11 sampai 14 V |
| `[AUDIO / VIDEO] G5-4 (B) - G5-7 (GND)` | Warna Kabel: L-Y - BR — Baterai | Selalu: 11 sampai 14 V |
| `[AUDIO / VIDEO] G5-5 (FR-) - G5-7 (GND)` | Warna Kabel: L - BR — Sinyal suara (kanan depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G5-6 (FL-) - G5-7 (GND)` | Warna Kabel: V - BR — Sinyal suara (Kiri depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G5-7 (GND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G5-10 (ILL+) - G5-7 (GND)` | Warna Kabel: G - BR — Sinyal penerangan | Switch kontrol lampu off: Di bawah 1 V / Switch kontrol lampu tail atau head: 11 sampai 14 V |
| `[AUDIO / VIDEO] G4-1 (RR+) - G5-7 (GND)` | Warna Kabel: R - BR — Sinyal suara (kanan belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G4-2 (RL+) - G5-7 (GND)` | Warna Kabel: B - BR — Sinyal suara (Kiri belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G4-3 (RR-) - G5-7 (GND)` | Warna Kabel: W - BR — Sinyal suara (kanan belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G4-6 (RL-) - G5-7 (GND)` | Warna Kabel: Y - BR — Sinyal suara (Kiri belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G1-11 (AGND) - Masa bodi` | Warna Kabel: Shielded - Masa bodi — Masa berpelindung | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G1-17 (SPD) - G5-7 (GND)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari meter kombinasi | Ignition switch ON, roda penggerak diputar perlahan-lahan: Pembangkitan pulsa |
| `[AUDIO / VIDEO] G1-21 (SW1) - G5-7 (GND)*` | Warna Kabel: R - BR — Sinyal steering pad switch | Steering pad switch tidak dioperasikan: 2.8 sampai 3.6 V / Switch seek+ ditekan: 0 sampai 0.6 V / Switch seek- ditekan: 0.6 sampai 1.3 V / Switch volume+ ditekan: 1.3 sampai 2.1 V / Switch volume- ditekan: 2.1 sampai 2.8 |
| `[AUDIO / VIDEO] G1-22 (SW2) - G5-7 (GND)*` | Warna Kabel: W - BR — Sinyal switch steering pad | Steering pad switch tidak dioperasikan: 2.8 sampai 3.6 V / Switch MODE ditekan: 0 sampai 0.6 V |
| `[AUDIO / VIDEO] G1-23 (SWG) - G5-7 (GND)*` | Warna Kabel: L - BR — Masa steering pad switch | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G1-25 (ADPG) - G5-7 (GND)` | Warna Kabel: G - BR — Sinyal deteksi hubungan peralatan eksternal | Peralatan eksternal dihubungkan: 0.71 sampai 1.5 V / Peralatan eksternal tidak dihubungkan: 2.61 sampai 3.3 V |
| `[AUDIO / VIDEO] G1-26 (VAR+) - G5-7 (GND)` | Warna Kabel: B - BR — Sinyal suara (Kanan) | Memainkan peralatan eksternal (Bila stereo jack digunakan): Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G1-27 (VA-) - G5-7 (GND)` | Warna Kabel: W - BR — Masa | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G1-28 (VAL+) - G5-7 (GND)` | Warna Kabel: R - BR — Sinyal suara (Kiri) | Memainkan peralatan eksternal (Bila stereo jack digunakan): Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] RA-5 (ANT+) - G5-7 (GND)` | Warna Kabel: B - BR — Power source antena | Switch radio on dan AM atau FM on: 11 sampai 14 V |
| `[AUDIO / VIDEO] z2-1 (USV1) - z2-4 (UGD1)` | Warna Kabel: # - # — Baterai | Selalu: 4.5 sampai 5.5 V |
| `[AUDIO / VIDEO] z2-2 (US1-) - z2-4 (UGD1)` | Warna Kabel: # - # — Sinyal data | Peralatan USB atau "iPod" dihubungkan: - |
| `[AUDIO / VIDEO] z2-3 (US1+) - z2-4 (UGD1)` | Warna Kabel: # - # — Sinyal data | Peralatan USB atau "iPod" dihubungkan: - |
| `[AUDIO / VIDEO] z2-4 (UGD1) - Masa bodi` | Warna Kabel: # - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G129-1 (FR+) - G129-7 (GND)` | Warna Kabel: LG - BR — Sinyal suara (kanan depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G129-2 (FL+) - G129-7 (GND)` | Warna Kabel: P - BR — Sinyal suara (Kiri depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G129-3 (ACC) - G129-7 (GND)` | Warna Kabel: GR - BR — Aksessoris (ON) | Ignition switch off: Di bawah 1 V / Ignition switch ACC: 11 sampai 14 V |
| `[AUDIO / VIDEO] G129-4 (B) - G129-7 (GND)` | Warna Kabel: L-Y - BR — Baterai | Selalu: 11 sampai 14 V |
| `[AUDIO / VIDEO] G129-5 (FR-) - G129-7 (GND)` | Warna Kabel: L - BR — Sinyal suara (kanan depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G129-6 (FL-) - G129-7 (GND)` | Warna Kabel: V - BR — Sinyal suara (Kiri depan) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G129-7 (GND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G129-10 (ILL+) - G129-7 (GND)` | Warna Kabel: G - BR — Sinyal penerangan | Switch kontrol lampu off: Di bawah 1 V / Switch kontrol lampu tail atau head: 11 sampai 14 V |
| `[AUDIO / VIDEO] G128-1 (RR+) - G129-7 (GND)` | Warna Kabel: R - BR — Sinyal suara (kanan belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G128-2 (RL+) - G129-7 (GND)` | Warna Kabel: B - BR — Sinyal suara (Kiri belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G128-3 (RR-) - G129-7 (GND)` | Warna Kabel: W - BR — Sinyal suara (kanan belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G128-6 (RL-) - G129-7 (GND)` | Warna Kabel: Y - BR — Sinyal suara (Kiri belakang) | Memainkan sistem audio: Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G127-4 (MACC) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply microphone AMP | Ignition switch off: Di bawah 1 V / Ignition switch ACC: 4 sampai 6 V |
| `[AUDIO / VIDEO] G127-5 (MIN+) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal suara microphone | Lihat "Microphone & Voice Recognition Check" (Lihat halaman ): - |
| `[AUDIO / VIDEO] G127-6 (SNS2) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal deteksi hubungan microphone | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G127-11 (AGND) - Masa bodi` | Warna Kabel: Shielded - Masa bodi — Masa berpelindung | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G127-17 (SPD) - G129-7 (GND)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari meter kombinasi | Lihat "Vehicle Signal" (Lihat halaman ): - |
| `[AUDIO / VIDEO] G127-18 (SGND) - G129-7 (GND)` | Warna Kabel: Shielded - BR — Masa berpelindung | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G127-19 (MIN-) - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal suara microphone | Lihat "Microphone & Voice Recognition Check" (Lihat halaman ): - |
| `[AUDIO / VIDEO] G127-21 (SW1) - G129-7 (GND)` | Warna Kabel: R - BR — Sinyal steering pad switch | Steering pad switch tidak dioperasikan: 4.44 sampai 5.43 V / Switch seek+ ditekan: 0.45 sampai 0.65 V / Switch seek- ditekan: 1.19 sampai 1.49 V / Switch volume+ ditekan: 2.09 sampai 2.54 V / Switch volume- ditekan: 3.20 |
| `[AUDIO / VIDEO] G127-22 (SW2) - G129-7 (GND)` | Warna Kabel: W - BR — Sinyal switch steering pad | Steering pad switch tidak dioperasikan: 4.44 sampai 5.43 V / Switch MODE ditekan: 0.45 sampai 0.65 V / Switch On hook ditekan: 1.19 sampai 1.49 V / Switch Off hook ditekan: 2.09 sampai 2.54 V |
| `[AUDIO / VIDEO] G127-23 (SWG) - G129-7 (GND)` | Warna Kabel: L - BR — Masa steering pad switch | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G127-25 (ADPG) - G129-7 (GND)` | Warna Kabel: G - BR — Sinyal deteksi hubungan peralatan eksternal | Peralatan eksternal dihubungkan: Di bawah 1 V |
| `[AUDIO / VIDEO] G127-26 (VAR+) - G129-7 (GND)` | Warna Kabel: B - BR — Sinyal suara (Kanan) | Memainkan peralatan eksternal (Bila stereo jack digunakan): Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G127-27 (VA-) - G129-7 (GND)` | Warna Kabel: W - BR — Masa | Selalu: Di bawah 1 V |
| `[AUDIO / VIDEO] G127-28 (VAL+) - G129-7 (GND)` | Warna Kabel: R - BR — Sinyal suara (Kiri) | Memainkan peralatan eksternal (Bila stereo jack digunakan): Bentuk gelombang disingkronkan dengan output suara |
| `[AUDIO / VIDEO] G2-6 (PKB) - G129-7 (GND)` | Warna Kabel: LG - BR — Sinyal rem parkir | Lihat "Vehicle Signal" (Lihat halaman ): - |
| `[AUDIO / VIDEO] RA-5 (ANT+) - G129-7 (GND)` | Warna Kabel: B - BR — Power source antena | Switch radio on dan AM atau FM on: 11 sampai 14 V |
| `[AUDIO / VIDEO] z6-1 (USV1) - z6-4 (UGD1)` | Warna Kabel: # - # — Baterai | Selalu: 4.5 sampai 5.5 V |
| `[AUDIO / VIDEO] z6-2 (US1-) - z6-4 (UGD1)` | Warna Kabel: # - # — Sinyal data | Peralatan USB atau "iPod" dihubungkan: - |
| `[AUDIO / VIDEO] z6-3 (US1+) - z6-4 (UGD1)` | Warna Kabel: # - # — Sinyal data | Peralatan USB atau "iPod" dihubungkan: - |
| `[AUDIO / VIDEO] z6-4 (UGD1) - Body ground` | Warna Kabel: # - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[PARK ASSIST / MONITORING] G129-3 (ACC) - G129-7 (GND)` | Warna Kabel: GR - BR — Accessory (On) | Ignition switch off: Di bawah 1 V / Ignition switch ACC: 11 sampai 14 V |
| `[PARK ASSIST / MONITORING] G129-4 (B) - G129-7 (GND)` | Warna Kabel: L-Y - BR — Baterai | Selalu: 11 sampai 14 V |
| `[PARK ASSIST / MONITORING] G129-7 (GND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[PARK ASSIST / MONITORING] G2-8 (V+) - G2-16 (V-)` | Warna Kabel: W - R — Tampilan sinyal | Ignition switch ON, shift lever di R: Pembangkitan pulsa (Lihat bentuk gelombang 1) / Ignition switch ON, shift lever di R, screen mejadi hitam dengan menutup lensa camera: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[PARK ASSIST / MONITORING] G2-7 (CA+) - G2-15 (CGND)` | Warna Kabel: B - Shielded — Power source | Ignition switch ON, shift lever di R: 5.5 sampai 7.05 V |
| `[PARK ASSIST / MONITORING] G2-15 (CGND) - Masa bodi` | Warna Kabel: Shielded - Masa bodi — Shielding | Selalu: Di bawah 1 V |
| `[PARK ASSIST / MONITORING] G127-2 (REV) - G129-7 (GND)` | Warna Kabel: R-Y - BR — Sinyal Reverse | Ignition switch ON, shift lever di R: 7.5 sampai 14 V / Ignition switch ON, shift lever tidak dalam R: Di bawah 1 V |
| `[KUNCI PINTU] 2D-9 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KUNCI PINTU] 2D-18 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KUNCI PINTU] 2H-4 (ALTB) - Masa bodi` | Warna Kabel: LG - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[KUNCI PINTU] 2L-12 (BECU) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[KUNCI PINTU] 2A-4 (L1) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal input penguncian power window regulator master switch assembly (switch kontrol pintu) Sinyal input pengu | Power window regulator master switch assembly (switch kontrol pintu) terkunci Silinder kunci pintu sisi pengemudi dalam posisi lock: Di bawah 1 V / Power window regulator master switch assembly (switch kontrol pintu) off |
| `[KUNCI PINTU] 2D-4 (UL1) - Masa bodi` | Warna Kabel: L-W - Masa bodi — Sinyal input membuka penguncian power window regulator master switch assembly (switch kontrol pintu) Sinyal i | Power window regulator master switch assembly (switch kontrol pintu) tidak terkunci Silinder kunci pintu sisi pengemudi dalam posisi unlock: Di bawah 1 V / Power window regulator master switch assembly (switch kontrol pi |
| `[KUNCI PINTU] 2K-10 (ACT-) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal output penggerak UNLOCK untuk door lock motor (pintu pengemudi dan pintu belakang RH*1 atau pintu LH b | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] 2K-11 (ACT+) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal output penggerak locjk untuk door lock motor (pintu pepenumpang dan pintu belakang RH*1 atau pintu LH be | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] 2O-27 (DCTY) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal input switch lampu courtesy pintu depan assembly LH*1 atau RH*2 | Pintu samping pengemudi terbuka: Di bawah 1 V / Pintu sisi pengemudi tertutup: 11 sampai 14 V |
| `[KUNCI PINTU] 2R-27 (ACT-) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal output penggerak unlock untuk door lock motor (pintu pengemudi dan pintu LH belakang*1 atau pintu RH b | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] 2R-28 (ACT+) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal output penggerak lock untuk door lock motor, pintu LH belakang*1 atau pintu RH belakang*2) | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] G29-1 (E) - Masa bodi` | Warna Kabel: B-W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KUNCI PINTU] G29-4 (+B1) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[KUNCI PINTU] G29-14 (+B2) Masa bodi` | Warna Kabel: LG - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[KUNCI PINTU] G29-18 (IG) Masa bodi` | Warna Kabel: R-L - Masa bodi — Power supply pengapian | Ignition switch off: Di bawah 1 V / ignition switch ON: 11 sampai 14 V |
| `[KUNCI PINTU] G29-7 (CTY) - Masa bodi` | Warna Kabel: R-L - Masa bodi — Sinyal input semua switch lcourtesy pintu | One atau lebih pintu-pintu terbuka: Di bawah 1 V / Semua pintu ditutup: 11 sampai 14 V |
| `[KUNCI PINTU] G29-17 (SPD) - Masa bodi` | Warna Kabel: V-R - Masa bodi — Sinyal input kecpatan kendaraan | Pengendaraan sekitar 20 km/jam (12,4 mph): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[KUNCI PINTU] G29-14 (+B2) - Masa bodi` | Warna Kabel: LG - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[KUNCI PINTU] G29-18 (IG) - Masa bodi` | Warna Kabel: R-L - Masa bodi — Power supply pengapian | Ignition switch off: Di bawah 1 V / ignition switch ON: 11 sampai 14 V |
| `[KUNCI PINTU] G29-3 (DMLP) - Masa bodi` | Warna Kabel: P - Masa bodi — Sinyal output lampu interior | Lampu-lampu interior menyala: Di bawah 1 V / Lampu-lampu interior padam: 11 sampai 14 V |
| `[KUNCI PINTU] G29-5 (KSW) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal input switch peringatan unlock | Tidak terdapat kunci dalam ignition key cylinder: 10 kΩ atau lebih tinggi / Kunci dimasukkan ke dalam ignition key cylinder: Di bawah 1 Ω |
| `[KUNCI PINTU] G29-7 (CTY) - Masa bodi` | Warna Kabel: R-L - Masa bodi — Sinyal input semua switch courtesy pintu | Satu atau lebih pintu dibuka: Di bawah 1 V / Semua pintu tertutup: 11 sampai 14 V |
| `[KUNCI PINTU] G29-13 (SH-) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal output dari security horn | Security horn assembly off: Di bawah 1 V / Security horn assembly on: Pembangkitan pulsa |
| `[KUNCI PINTU] G29-25 (L2) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal ouput kunci pintu | Engine switch off, semua pintu ditutup dan switch transmitter tidak ditekan.: Di bawah 1 V / Engine switch off, semua pintu ditutup dan switch lock transmitter ditekan.: Pembangkitan pulsa |
| `[KUNCI PINTU] G29-26 (UL3) -Masa bodi` | Warna Kabel: L-W - Masa bodi — Sinyal ouput pembebasan kunci pintu | Engine switch off, semua pintu ditutup dan switch transmitter tidak ditekan.: Di bawah 1 V / Engine switch off, semua pintu ditutup dan switch unlock transmitter ditekan.: Pembangkitan pulsa |
| `[KUNCI PINTU] G29-28 (HAZD) - Masa bodi` | Warna Kabel: G-O - Masa bodi — Sinyal output semua lampu peringatan hazard | Switch sinyal peringatan hazard assembly off: 11 sampai 14 V / Switch sinyal peringatan hazard assembly on: Di bawah 1 V |
| `[KUNCI PINTU] 2A-6 (SIG) - Masa bodi` | Warna Kabel: B-Y - Masa bodi — Ignition switch | Ignition switch off: Di bawah 1 V / ignition switch ON: 11 sampai 14 V |
| `[KUNCI PINTU] 2K-10 (ACT-) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal output penggerak unlock pada door lock motor (pintu penumpang dan pintu RH belakang) | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] 2K-11 (ACT+) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal output penggerak lock pada door lock motor (pintu penumpang dan pintu RH belakang) | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Power window regulator master switch assembly (switch kontro |
| `[KUNCI PINTU] 2O-10 (PCTY) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal input semua switch lampu courtesy | One atau lebih pintu-pintu terbuka: Di bawah 1 V / Semua pintu ditutup: 11 sampai 14 V |
| `[KUNCI PINTU] 2O-27 (DCTY) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal input switch lampu courtesy pintu depan assembly LH | Pintu samping pengemudi terbuka: Di bawah 1 V / Pintu sisi pengemudi tertutup: 11 sampai 14 V |
| `[KUNCI PINTU] 2R-27 (ACT-) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal output penggerak UNLOCK door lock motor (pintu pengemudi dan pintu belakang RH) | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] 2R-28 (ACT+) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal output penggerak penguncian door lock motor (pintu pengemudi dan pintu belakang LH) | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Power window regulator master switch assembly (switch kontro |
| `[KUNCI PINTU] 2D-2 (RDA) - Masa bodi` | Warna Kabel: V-R - Masa bodi — Sinyal input receiver kontrol pintu | Engine switch off, semua pintu ditutup dan switch transmitter tidak ditekan.: 11 sampai 14 V / Engine switch off, semua pintu ditutup dan switch transmitter ditekan.: Pembangkitan pulsa |
| `[KUNCI PINTU] 2D-5 (PRG) - Masa bodi` | Warna Kabel: G-W - Masa bodi — Sinyal output receiver kontrol pintu | Kunci dimasukkan ke dalam ignition key cylinder → Karena kunci ditarik ke luar dari ignition key cylinder: 11 sampai 14 V → Pembangkitan pulsa → 11 sampai 14 V |
| `[KUNCI PINTU] 2D-7 (LSWD) - Masa bodi` | Warna Kabel: L-R - Masa bodi — Sinyal input switch posisi door lock | Pintu sisi pengemudi terkunci: Di bawah 1 V / Pintu sisi pengemudi terkunci: 11 sampai 14 V |
| `[KUNCI PINTU] 2E-3 (PCTY) - Masa bodi` | Warna Kabel: P - Masa bodi — Sinyal input semua switch lampu courtesy | One atau lebih pintu-pintu terbuka: Di bawah 1 V / Semua pintu ditutup: 11 sampai 14 V |
| `[KUNCI PINTU] 2N-12 (ILE) - Masa bodi*1` | Warna Kabel: P - Masa bodi — Sinyal output lampu ignition key cylinder | Lampu ignition key cylinder hidup: Di bawah 1 V / Lampu ignition key cylinder mati: 11 sampai 14 V |
| `[KUNCI PINTU] 2K-10 (ACT-) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal output penggerak unlock untuk door lock motor (pintu penumpang dan pintu RH belakang *2 atau pintu LH  | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] 2K-11 (ACT+) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal output penggerak lock untuk door lock motor (pintu penumpang dan pintu RH belakang *2 atau pintu LH bela | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Power window regulator master switch assembly (switch kontro |
| `[KUNCI PINTU] 2O-10 - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal input switch peringatan unlock | Tidak terdapat kunci dalam ignition key cylinder: 10 kΩ atau lebih tinggi / Kunci dimasukkan ke dalam ignition key cylinder: Di bawah 1 Ω |
| `[KUNCI PINTU] 2O-25 (HAZ) - Masa bodi` | Warna Kabel: G-O - Masa bodi — Sinyal output semua lampu peringatan hazard | Switch sinyal peringatan hazard assembly off: 11 sampai 14 V / Switch sinyal peringatan hazard assembly on: Di bawah 1 V |
| `[KUNCI PINTU] 2O-27 (DCTY) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal input switch lampu courtesy pintu depan assembly LH*2 atau RH*3 | Pintu samping pengemudi terbuka: Di bawah 1 V / Pintu sisi pengemudi tertutup: 11 sampai 14 V |
| `[KUNCI PINTU] 2R-27 (ACT-) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal output penggerak unlock untuk door lock motor (pintu pengemudi dan pintu LH belakang*2 atau pintu RH b | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] 2R-28 (ACT+) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal output penggerak LOCK untuk door lock motor (pintu pengemudi dan pintu LH belakang*2 atau pintu RH belak | Power window regulator master switch assembly (switch kontrol pintu) tidak ditekan dan silinder kunci pintu sisi pengemudi dalam posisi netral.: Di bawah 1 V / Sisi lock dari power window regulator master switch assembly |
| `[KUNCI PINTU] G19-1 (B) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[KUNCI PINTU] G19-21 (IG+) - Masa bodi` | Warna Kabel: B-O - Masa bodi — Sinyal input IG2 | ignition switch ON: 11 sampai 14 V / Ignition switch off: Di bawah 1 V |
| `[KUNCI PINTU] G19-22 (EP) - Masa bodi` | Warna Kabel: Y - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KUNCI PINTU] G19-10 (KSW) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal input switch peringatan unlock | Tidak terdapat kunci dalam ignition key cylinder: Di bawah 1 V / Ignition switch off, kunci dalam ignition key cylinder: 11 sampai 14 V |
| `[KUNCI PINTU] G19-16 (DCTY) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal input pintu sisi pengemudi | Pintu sisi pengemudi tertutup: Di bawah 1 V / Pintu samping pengemudi terbuka: 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-1 (E) - Masa bodi` | Warna Kabel: B-W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-4 (+B1) - G29-1 (E)` | Warna Kabel: L-Y - B-W — Power supply baterai (power supply untuk ECU) | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-14 (+B2) - G29-1 (E)` | Warna Kabel: LG - B-W — Power supply baterai (untuk pengoperasian aktuator) | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-18 (IG) - G29-1 (E)` | Warna Kabel: R-L - B-W — Power supply pengapian | Ignition switch off: Di bawah 1 V / ignition switch ON: 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-5 (KSW) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal input switch peringatan unlock | Tidak terdapat kunci dalam ignition key cylinder: 10 kΩ atau lebih tinggi / Kunci dimasukkan ke dalam ignition key cylinder: Di bawah 1 Ω |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-7 (CTY) - G29-1 (E)` | Warna Kabel: R-L - B-W — Sinyal input semua switch lampu courtesy | One atau lebih pintu-pintu terbuka: Di bawah 1 V / Semua pintu ditutup: 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-9 (DSWH) - G29-1 (E)` | Warna Kabel: G-R - B-W — Sinyal input hood lock assembly (security courtesy switch) | Kap mesin ditutup penuh: Di bawah 1 Ω / Kap mesin terbuka: 10 kΩ atau lebih tinggi |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-11 (HORN) - G29-1 (E)` | Warna Kabel: W-R - B-W — Sinyal output dari horn kemanan | Status membunyikan alarm: Di bawah 1 V / Status siaga: 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-12 (SRLY) - G29-1 (E)` | Warna Kabel: W-B - B-W — Sinyal output starter cut | Status siaga: 11 sampai 14 V / Status membunyikan alarm: Di bawah 1 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-13 (SH-) - G29-1 (E)` | Warna Kabel: B - B-W — Sinyal output dari security horn | Horn keamanan assembly berbunyi (Sistem anti pencurian dalam status membunyikan alarm): Naik turun antara di bawah 1 V dan 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-27 (IND) - G29-1 (E)` | Warna Kabel: G-R - B-W — Sinyal output lampu indikator keamanan | Lampu indikator keamanan berkedip (sistem anti pencurian bekerja): Naik turun antara di bawah 1 V dan 11 sampai 14 V |
| `[ANTI PENCURIAN / KEYLESS ENTRY] G29-28 (HAZD) - G29-1 (E)` | Warna Kabel: G-O - B-W — Sinyal output semua lampu peringatan hazard | Lampu peringatan hazard dan lampu tanda belok samping berkedip (Sistem anti pencurian dalam status membunyikan alarm): Di bawah 1 V |
| `[PENERANGAN (INT)] 2H-4 (ALTB) - Masa bodi` | Warna Kabel: LG - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2L-12 (BECU) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2D-9 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[PENERANGAN (INT)] 2D-18 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[PENERANGAN (INT)] 2D-7 (LSWD) - Masa bodi` | Warna Kabel: L-R - Masa bodi — Sinyal switch deteksi unlock pintu depan. | Pintu sisi pengemudi terkunci: Di bawah 1 V / Pintu sisi pengemudi terkunci: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2O-27 (DCTY) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal switch lampu courtesy pintu sisi pengemudi | Pintu samping pengemudi terbuka: Di bawah 1 V / Pintu sisi pengemudi tertutup: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2N-12 (ILE) - Masa bodi*` | Warna Kabel: P - Masa bodi — Sinyal lampu ignition key cylinder | Lampu ignition key cylinder hidup: Di bawah 1 V / Lampu ignition key cylinder mati: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-4 (+B1) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-14 (+B2) - Masa bodi` | Warna Kabel: LG - Masa bodi — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-18 (IG) - Masa bodi` | Warna Kabel: R-L - Masa bodi — Power supply pengapian | ignition switch ON: 11 sampai 14 V / Ignition switch off: Di bawah 1 V |
| `[PENERANGAN (INT)] G29-1 (E) - Masa bodi` | Warna Kabel: B-W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[PENERANGAN (INT)] G29-3 (DMLP) - Masa bodi` | Warna Kabel: P - Masa bodi — Sinyal lampu interior | Lampu-lampu interior menyala: Di bawah 1 V / Lampu-lampu interior padam: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-7 (CTY) - Masa bodi` | Warna Kabel: R-L - Masa bodi — Sinyal semua switch courtesy | Sisi pengemudi, sisi penumpang depan, belakang RH atau belakang LH tertutup.: 11 sampai 14 V / Sisi pengemudi, sisi penumpang depan, belakang RH atau belakang LH terbuka: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-1 (B) - Masa bodi` | Warna Kabel: R - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-9 (TR) - Masa bodi*1` | Warna Kabel: W-B - Masa bodi — Sinyal rheostat | Knob rheostat diputar penuh ke kiri: 666.9 sampai 737.1 Ω / Knob rheostat diputar penuh ke kanan: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-19 (ABOF) - Masa bodi*2` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-21 (IG+) - Masa bodi` | Warna Kabel: B-O - Masa bodi — Sinyal IG2 | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-22 (EP) - Masa bodi` | Warna Kabel: Y - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-26 (PKBI) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-38 (LP) - Masa bodi*3` | Warna Kabel: R-G - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-2 (ES) - G19-3 (L)` | Warna Kabel: BR - BR-Y — Sinyal permukaan bahan bakar | Ignition switch on, level bahan bakar F: Di bawah 1 V / Ignition switch on, level bahan bakar E: 4 sampai 7 V |
| `[METER / GAUGE / DISPLAY] G19-5 (SI) - Masa bodi` | Warna Kabel: P-L - Masa bodi — Sinyal kecepatan kendaraan (input) | Kendarai sekitar 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[METER / GAUGE / DISPLAY] G19-6 (+S) - Masa bodi` | Warna Kabel: V-R - Masa bodi — Sinyal kecepatan kendaraan (output) | Kendarai sekitar 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[METER / GAUGE / DISPLAY] G19-7 (S) - Masa bodi` | Warna Kabel: B-W - Masa bodi — Sinyal Tachometer | Mesin idle: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[METER / GAUGE / DISPLAY] G5-19 (ILL+) - Masa bodi` | Warna Kabel: G - Masa bodi — Sinyal switch kontrol lampu | Switch kontrol lampu off: Di bawah 1 V / Switch kontrol lampu TAIL atau HEAD: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-10 (KSW) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal switch peringatan unlock | Tidak terdapat kunci dalam ignition key cylinder: Di bawah 1 V / Ignition switch off, kunci dalam ignition key cylinder: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-11 (BKL) - Masa bodi` | Warna Kabel: R-Y - Bodi masa — Sinya peringatan seat beltl sisi pengemudi | Ignition switch ON, seat belt sisi pengemudi tidak dipakai: Di bawah 1 V / Ignition switch ON, seat belt sisi pengemudi dipakai: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-12 (P) - Masa bodi*1` | Warna Kabel: G-B - Masa bodi — Sinyal posisi shift transmisi otomatis (P) | Ignition switch on, lampu indikator transmisi otomatis padam: Di bawah 1 V / Ignition switch on, lampu indikator transmisi otomatis menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-13 (L) - Masa bodi (*2)` | Warna Kabel: W-G - Masa bodi — Sinyal lampu peringatan A/T P | Ignition switch ON, shift lever di P, lampu peringatan A/T P menyala: Di bawah 1 V / Ignition switch ON, shift lever di P, lampu peringatan A/T P menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-14 (FFTR) - Masa bodi*3` | Warna Kabel: W-G - Masa bodi — Sinyal lampu peringatan FUEL FILTER | Ignition switch ON, lampu peringatan FUEL FILTER hidup: Di bawah 1 V / Ignition switch ON, lampu peringatan FUEL FILTER padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-15 (CTYD) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal pintu sisi pengemudi (output) | Pintu sisi pengemudi tertutup: 11 sampai 14 V / Pintu samping pengemudi terbuka: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-16 (DCTY) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal pintu sisi pengemudi (input) | Pintu sisi pengemudi tertutup: 11 sampai 14 V / Pintu samping pengemudi terbuka: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-17 (DOOR) - Masa bodi` | Warna Kabel: R-L - Masa bodi — Sinyal pintu | Pintu-pintu ditutup (Tak terkecuali pintu sisi pengemudi): 11 sampai 14 V / Pintu-pintu dibuka (Tak terkecuali pintu sisi pengemudi): Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-18 (OILW) - Masa bodi*1, *2` | Warna Kabel: P - Masa bodi — Sinyal lampu peringatan A/T OIL TEMP | Ignition switch ON, lampu peringatan A/T OIL TEMP hidup: Di bawah 1 V / Ignition switch ON, lampu peringatan A/T OIL TEMP padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-20 (SW) - Masa bodi*4` | Warna Kabel: B-Y - Masa bodi — Sinyal lampu peringatan SRS | Ignition switch ON, lampu peringatan SRS mati: Pembangkitan pulsa (Lihat bentuk gelombang 3) / Ignition switch ON, lampu peringatan SRS hidup: Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[METER / GAUGE / DISPLAY] G19-23 (S) - Masa bodi*3` | Warna Kabel: L-R - Masa bodi — Sinyal lampu peringatan FUEL FILTER | Ignition switch ON, lampu peringatan FUEL FILTER hidup: Di bawah 1 V / Ignition switch ON, lampu peringatan FUEL FILTER padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-24 (B) - Masa bodi` | Warna Kabel: G-B - Masa bodi — Sinyal indikator tanda belok LH | Ignition switch on, lampu indikator tanda belok RH padam: Di bawah 1 V / Ignition switch on, lampu indikator tanda belok RH hidup: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-25 (B) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal indikator tanda belok RH | Ignition switch ON, lampu indikator tanda belok RH padam: Di bawah 1 V / Ignition switch ON, lampu indikator tanda belok RH hidup: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-31 (MS5) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal IG (untuk Vehicle speed sensor) | ignition switch ON: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-35 (S) - Masa bodi` | Warna Kabel: LG-B - Masa bodi — Sinyal lampu peringatan OIL PRESSURE | Ignition switch ON, Lampu peringatan OIL PRESSURE padam: 11 sampai 14 V / Ignition switch ON, lampu peringatan OIL PRESSURE menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-36 (SW) - Masa bodi` | Warna Kabel: LG - Masa bodi — Sinyal lampu peringatan BRAKE | Ignition switch ON, Lampu peringatan BRAKE padam: 11 sampai 14 V / Ignition switch ON, Lampu peringatan BRAKE menyala: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-37 (CHG-) - Masa bodi` | Warna Kabel: GR - Masa bodi — Sinyal lampu peringatan CHARGE | Ignition switch ON, lampu peringatan CHARGE padam: 11 sampai 14 V / Ignition switch ON, lampu peringatan CHARGE menyala: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-38 (LP) - Masa bodi*5` | Warna Kabel: R-G - Masa bodi — Sinyal lampu peringatan ABS | Ignition switch ON, lampu peringatan ABS OFF: 11 sampai 14 V / Ignition switch ON, lampu peringatan ABS ON: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-39 (CHK) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal MIL | Ignition switch ON, MIL padam: 11 sampai 14 V / Ignition switch ON, MIL menyala: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-40 (GLW-) - Masa bodi*3` | Warna Kabel: Y-R - Masa bodi — Sinyal lampu indikator GLOW | Ignition switch ON, lampu indikator GLOW padam: 11 sampai 14 V / Ignition switch ON, lampu indikator GLOW menyala: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-2 (2) - Masa bodi*1` | Warna Kabel: G-R - Masa bodi — Sinyal posisi shift transmisi otomatis (L) | Ignition switch ON, lampu indikator transmisi otomatis L menyala: 11 sampai 14 V / Ignition switch on, lampu indikator transmisi otomatis L padam: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-3 (3) - Masa bodi*1` | Warna Kabel: L - Masa bodi — Sinyal posisi shift transmisi otomatis (2) | Ignition switch on, lampu indikator transmisi otomatis 2 menyala: 11 sampai 14 V / Ignition switch on, lampu indikator transmisi otomatis 2 padam: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-4 (4) - Masa bodi*1` | Warna Kabel: G-O - Masa bodi — Sinyal posisi shift transmisi otomatis (3) | Ignition switch on, lampu indikator transmisi otomatis 3 menyala: 11 sampai 14 V / Ignition switch on, lampu indikator transmisi otomatis 3 padam: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-5 (D) - Masa bodi*1` | Warna Kabel: B-R - Masa bodi — Sinyal posisi shift transmisi otomatis (D) | Ignition switch on, lampu indikator transmisi otomatis D menyala: 11 sampai 14 V / Ignition switch on, lampu indikator transmisi otomatis D padam: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-6 (N) - Masa bodi*1` | Warna Kabel: R-W - Masa bodi — Sinyal posisi shift transmisi otomatis (N) | Ignition switch ON, lampu indikator transmisi otomatis N menyala: 11 sampai 14 V / Ignition switch ON, Lampu indikator N transmisi otomatis OFF: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-7 (R) - Masa bodi*1` | Warna Kabel: R-Y - Bodi masa — Sinyal posisi shift transmisi otomatis (R) | Ignition switch ON, lampu indikator transmisi otomatis R menyala: 11 sampai 14 V / Lampu indikator R transmisi otomatis OFF: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-11 (-) - Masa bodi` | Warna Kabel: R-Y - Bodi masa — Sinyal lampu indikator HI BEAM | Ignition switch ON, lampu indikator HI BEAM padam: 11 sampai 14 V / Ignition switch ON, lampu indikator HI BEAM menyala: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-15 (FOG) - Masa bodi*6` | Warna Kabel: G-B - Masa bodi — Sinyal lampu indikator kabut bagian depan | Switch kontrol lampu dalam posisi TAIL atau HEAD, lampu kabut depan padam: Di bawah 1 V / Switch kontrol lampu dalam posisi TAIL atau HEAD, switch lampu kabut menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G20-18 (DISL) - Masa bodi*3` | Warna Kabel: G-B - Masa bodi — Sinyal untuk jumlah konsumsi bahan bakar. | Mesin idle: Pembangkitan pulsa |
| `[METER / GAUGE / DISPLAY] G20-25 (SW) - Masa bodi*2` | Warna Kabel: R-B - Masa bodi — Sinyal lampu indikator 4WD | Ignition switchON, lampu indikator 4WD padam: 11 sampai 14 V / Ignition switchON, lampu indikator 4WD menyala: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G32-1 (GND1) - Masa bodi` | Warna Kabel: LG - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G32-10 (SGND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G32-12 (IG) - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal IG | ignition switch ON: 11 sampai 14 V / Ignition switch off: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G32-13 (ACC) - Masa bodi` | Warna Kabel: G-R - Masa bodi — Sinyal ACC | Ignition switch ACC atau ON: 11 sampai 14 V / Ignition switch off: Di bawah 1 V |
| `[METER / GAUGE / DISPLAY] G32-14 (+B) - Masa bodi` | Warna Kabel: R - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G32-2 (SG) - G32-3 (TH+)` | Warna Kabel: BR-Y - W-G — Sinyal temperatur udara sekitar | Ignition switch ON, temperatur udara sekitar 25°C (77°F): 1,32 V / Ignition switch ON, temperatur udara sekitar 40℃ (104℉): 0,8 V |
| `[METER / GAUGE / DISPLAY] G32-8 (PBEW) - Masa bodi*1` | Warna Kabel: G-W - Masa bodi — Sinyal lampu peringatan seat belt sisi penumpang depan | Ignition switch ON, lampu peringatan seat belt sisi penumpang depan hidup: Di bawah 1 V / Ignition switch ON, lampu peringatan seat belt sisi penumpang depan mati: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G32-11 (SW+) - Masa bodi*2` | Warna Kabel: B - Masa bodi — Sinyal switch steering pad | Ignition switch ON, steering pad switch tidak ditekan: 4 V atau lebih / Ignition switch ON, INFO switch ditekan: Di bawah 1 V / Ignition switch ON, MODE RESETswitch ditekan: 2 sampai 3 V |
| `[METER / GAUGE / DISPLAY] G21-1 (B) - Masa bodi` | Warna Kabel: R - Masa bodi — Baterai | Selalu: 11 sampai 14 V Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G21-2 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G21-4 (ACC) - Masa bodi` | Warna Kabel: V - Masa bodi — Sinyal ACC | Ignition switch ACC atau ON: 11 sampai 14 V / Ignition switch off: Di bawah 1 V |
| `[HEATING / AIR CONDITIONING] G34-10 (IG+) - G34-18 (GND)` | Warna Kabel: R-L - L — Power supply pengapian | ignition switch ON: 11 sampai 14 V / Ignition switch off: Di bawah 1 V |
| `[HEATING / AIR CONDITIONING] G34-18 (GND) - Masa bodi` | Warna Kabel: L - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G34-1 (MGC) - G34-18 (GND)` | Warna Kabel: L-W - L — Sinyal pengoperasian cooler compressor assembly | Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch off atau cooler switch on (magnet clutch off): 11 sampai 14 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch on (magnet clutch on |
| `[HEATING / AIR CONDITIONING] G34-2 (ACT) - G34-18 (GND)` | Warna Kabel: R-L - L — Sinyal yang mengizinkan magnet clutch on | Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch on: 5 sampai 6 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch off: Di bawah 1 V |
| `[HEATING / AIR CONDITIONING] G34-3 (PSW) - G34-18 (GND)` | Warna Kabel: Y-B - L — Sinyal air conditioner pressure sensor | Mesin idle Tekanan refrigerant normal: Di bawah 1 V / Mesin idle Tekanan refrigerant abnormal (di bawah 0.176 MPa [1.8 kgf/cm 2 , 25.5 psi] atau lebih tinggi dari 3.025 MPa [30.9 kgf/cm 2 , 438.6 psi]): 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G34-4 (ACON) - G34-18 (GND)` | Warna Kabel: R-G - L — Sinyal cooler switch | Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch off: 11 sampai 14 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch on: Di bawah 1 V |
| `[HEATING / AIR CONDITIONING] G34-7 (TE) - G34-8 (SG-1)` | Warna Kabel: G - P — Sinyal cooler thermistor No. 1 | ignition switch ON Temperatur evaporator 0°C (32°F): 2.0 sampai 2.4 V / ignition switch ON Temperatur evaporator 15℃ (59℉): 1.1 sampai 1.5 V |
| `[HEATING / AIR CONDITIONING] G34-8 (SG-1) - Masa bodi` | Warna Kabel: P - Masa bodi — Masa untuk cooler thermistor No. 1 | Selalu: Di bawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G34-13 (IND-) - G34-18 (GND)` | Warna Kabel: R-L - L — Sinyal indikator cooler switch | Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch off atau cooler switch on: 11 sampai 14 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch on: Di bawah 1 V |
| `[HEATING / AIR CONDITIONING] G34-14 (AC1) - G34-18 (GND)` | Warna Kabel: Y - L — Sinyal pemesan idle-up | Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch off atau cooler switch on (magnet clutch off): 11 sampai 14 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch on (magnet clutch on |
| `[HEATING / AIR CONDITIONING] G38-18 (AC1) - C23-7 (E1)` | Warna Kabel: Y - BR — Sinyal pemesan idle-up | Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch on (magnet clutch on): Di bawah 1 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch off atau cooler switch on (magnet clutch off): |
| `[HEATING / AIR CONDITIONING] G38-19 (ACT) - C23-7 (E1)` | Warna Kabel: R-L - BR — Sinyal output yang mengizinkan magnet clutch on | Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch off: Di bawah 1 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Cooler switch on: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G34-5 (B/V) - G34-6 (TEMP)` | Warna Kabel: V-R — Sinyal air conditioning volume switch | Mesin idle Blower switch diset ke 1 atau lebih tinggi Air conditioning volume switch off: 11 sampai 14 V / Mesin idle Blower switch diset ke 1 atau lebih tinggi Air conditioning volume switch on (max. volume): Di bawah 1 |
| `[JENDELA / KACA] I5-6 (B) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply pengapian | Ignition switch off: Di bawah 1 V / ignition switch ON: 11 sampai 14 V |
| `[JENDELA / KACA] I5-7 (BW) - Masa bodi` | Warna Kabel: L-B - Masa bodi — Power supply motor regulator | Selalu: 11 sampai 14 V |
| `[JENDELA / KACA] I5-1 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[JENDELA / KACA] I5-2 (GND) - Masa bodi` | Warna Kabel: L-O - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[JENDELA / KACA] H8-6 (B) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply pengapian | Ignition switch off: Di bawah 1 V / ignition switch ON: 11 sampai 14 V |
| `[JENDELA / KACA] H8-7 (BW) - Masa bodi` | Warna Kabel: L-B - Masa bodi — Power supply motor regulator | Selalu: 11 sampai 14 V |
| `[JENDELA / KACA] H8-1 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[JENDELA / KACA] H8-2 (GND) - Masa bodi` | Warna Kabel: L-O - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[JENDELA / KACA] I5-4 (U) - I5-1 (E)` | Warna Kabel: R - W-B — Output down dari front power window regulator motor assembly LH | Ignition switch ON), power window switch sisi pengemudi off → up (pengoperasian manual): Di bawah 1 V ←→ 11 sampai 14 V / Ignition switch ON, power window sisi pengemudi terbuka sepenuhnya → power window switch sisi peng |
| `[JENDELA / KACA] I5-9 (D) - I5-1 (E)` | Warna Kabel: L-R - W-B — Output down dari front power window regulator motor assembly LH | Ignition switch ON, power window switch sisi pengemudi off → down (pengoperasian manual): Di bawah 1 V → 11 sampai 14 V / Ignition switch ON, power window sisi pengemudi tertutup sepenuhnya → power window switch sisi pen |
| `[JENDELA / KACA] I5-13 (U) - I5-1 (E)` | Warna Kabel: R-L - W-B — Output up dari front power window regulator motor assembly RH | Window lock switch off Ignition switch ON, remote manual switch untuk power window sisi penumpang depan posisi off → down: Di bawah 1 V ←→ 11 sampai 14 V |
| `[JENDELA / KACA] I5-15 (D) - I5-1 (E)` | Warna Kabel: G-W - W-B — Output down dari front power window regulator motor assembly RH | Window lock switch off Ignition switch ON, remote manual switch untuk power window sisi penumpang depan posisi off → down: Di bawah 1 V ←→ 11 sampai 14 V |
| `[JENDELA / KACA] I5-12 (U) - I5-1 (E)` | Warna Kabel: R-Y - W-B — Output up dari rear power window regulator motor assembly LH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang LH off → up: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] I5-10 (D) - I5-1 (E)` | Warna Kabel: G-Y - W-B — Output down dari rear power window regulator motor assembly LH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang LH off → down: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] I5-18 (U) - I5-1 (E)` | Warna Kabel: R-B - W-B — Output up dari rear power window regulator motor assembly RH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang RH off → up: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] I5-16 (D) - I5-1 (E)` | Warna Kabel: G-B - W-B — Output down dari rear power window regulator motor assembly RH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang RH off → down: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] I5-3 (VCC) - I5-2 (GND)` | Warna Kabel: BR - L-O — Power source dari power window regulator motor sensor | Ignition switch ON), power window switch sisi pengemudi off→ up atau down: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] I5-14 (PLS) - Masa bodi` | Warna Kabel: P-G - Masa bodi — Output down atau up dari front power window regulator motor assembly LH | Ignition switch ON), power window switch sisi pengemudi off→ up atau down: Bentuk gelombang pulsa muncul |
| `[JENDELA / KACA] I5-17 (PLS2) - Masa bodi` | Warna Kabel: B - Masa bodi — Output down atau up dari front power window regulator motor assembly LH | Ignition switch ON), power window switch sisi pengemudi off→ up atau down: Bentuk gelombang pulsa muncul |
| `[JENDELA / KACA] H8-4 (U) - H8-1 (E)` | Warna Kabel: B - W-B — Output up dari front power window regulator motor assembly RH | Ignition switch ON), power window switch sisi pengemudi off → up (pengoperasian manual): Di bawah 1 V ←→ 11 sampai 14 V / Ignition switch ON, power window sisi pengemudi terbuka sepenuhnya → power window switch sisi peng |
| `[JENDELA / KACA] H8-9 (D) - H8-1 (E)` | Warna Kabel: L-R - W-B — Output down dari front power window regulator motor assembly RH | Ignition switch ON, power window switch sisi pengemudi off → down (pengoperasian manual): Di bawah 1 V → 11 sampai 14 V / Ignition switch ON, power window sisi pengemudi tertutup sepenuhnya → power window switch sisi pen |
| `[JENDELA / KACA] H8-13 (U) - H8-1 (E)` | Warna Kabel: R-L - W-B — Output down dari front power window regulator motor assembly LH | Window lock switch off Ignition switch ON, remote manual switch untuk power window sisi penumpang depan posisi off → down: Di bawah 1 V ←→ 11 sampai 14 V |
| `[JENDELA / KACA] H8-15 (D) - H8-1 (E)` | Warna Kabel: G-W - W-B — Output down dari front power window regulator motor assembly LH | Window lock switch off Ignition switch ON, remote manual switch untuk power window sisi penumpang depan posisi off → down: Di bawah 1 V ←→ 11 sampai 14 V |
| `[JENDELA / KACA] H8-12 (U) - H8-1 (E)` | Warna Kabel: R-Y - W-B — Output up dari rear power window regulator motor assembly LH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang LH off → up: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] H8-10 (D) - H8-1 (E)` | Warna Kabel: G-Y - W-B — Output down dari rear power window regulator motor assembly LH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang LH off → down: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] H8-18 (U) - H8-1 (E)` | Warna Kabel: R-B - W-B — Output up dari rear power window regulator motor assembly RH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang RH off → up: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] H8-16 (D) - H8-1 (E)` | Warna Kabel: G-B - W-B — Output down dari rear power window regulator motor assembly RH | Window lock switch off Ignition switch ON, remote manual switch dari power window belakang RH off → down: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] H8-3 (VCC) - H8-2 (GND)` | Warna Kabel: BR - L-O — Power source dari power window regulator motor sensor | Ignition switch ON), power window switch sisi pengemudi off→ up atau down: Di bawah 1 V → 11 sampai 14 V |
| `[JENDELA / KACA] H8-14 (PLS) - Masa bodi` | Warna Kabel: P-G - Masa bodi — Output down atau up dari front power window regulator motor assembly RH | Ignition switch ON), power window switch sisi pengemudi off→ up atau down: Bentuk gelombang pulsa muncul |
| `[JENDELA / KACA] H8-17 (PLS2) - Masa bodi` | Warna Kabel: B - Masa bodi — Output down atau up dari front power window regulator motor assembly RH | Ignition switch ON), power window switch sisi pengemudi off→ up atau down: Bentuk gelombang pulsa muncul |
| `[1KD-FTV] G38-2 (BATT) - C23-7 (E1)` | Warna Kabel: L - BR — Baterai (untuk mengukur voltase baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[1KD-FTV] C22-18 (VC) - C22-28 (E2)` | Warna Kabel: R-W - BR — Power source sensor (voltase spesifikasi) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[1KD-FTV] C23-2 (VCS) - C23-1 (E2S)` | Warna Kabel: L-W - P-L — Power source pada fuel pressure sensor (sub) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[1KD-FTV] G39-26 (VCPA) - G39-28 (EPA)` | Warna Kabel: LG-R - BR-W — Power source untuk sensor posisi accelerator pedal (untuk VPA) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[1KD-FTV] G39-27 (VCP2) - G39-29 (EPA2)` | Warna Kabel: BR-R - BR-Y — Power source untuk sensor posisi accelerator pedal (untuk VPA2) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[1KD-FTV] G39-7 (STA) - C23-7 (E1)` | Warna Kabel: B-Y - BR — Starter signal | Cranking: 6.0 V atau lebih |
| `[1KD-FTV] G38-17 (SPD) - C23-7 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari combination meter | Ignition switch ON, putar roda secara perlahan: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[1KD-FTV] C22-26 (PCR1) - C22-28 (E2)` | Warna Kabel: R-Y - BR — Common rail pressure sensor (main) | Idling: 1.7 sampai 2.2 V |
| `[1KD-FTV] G39-15 (GREL) - C23-7 (E1)` | Warna Kabel: R - BR — GLOW relay | Cranking: 11 sampai 14 V |
| `[1KD-FTV] C22-8 (ALT) - C23-7 (E1)` | Warna Kabel: G - BR — Alternator duty ratio | Idling: Pembangkitan pulsa (lihat bentuk gelombang 5) |
| `[1KD-FTV] G38-22 (CAN+) - C23-7 (E1)` | Warna Kabel: V - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 12) |
| `[1KD-FTV] G38-21 (CAN-) - C23-7 (E1)` | Warna Kabel: P - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 13) |
| `[2KD-FTV] G38-2 (BATT) - C23-7 (E1)` | Warna Kabel: L - BR — Baterai (untuk mengukur voltase baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[2KD-FTV] C22-18 (VC) - C22-28 (E2)` | Warna Kabel: R-W - BR — Power source sensor (voltase spesifikasi) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2KD-FTV] C23-2 (VCS) - C23-1 (E2S)` | Warna Kabel: L-W - R-L — Power source pada fuel pressure sensor (sub) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2KD-FTV] G39-26 (VCPA) - G39-28 (EPA)` | Warna Kabel: LG-R - BR-W — Power source untuk sensor posisi accelerator pedal (untuk VPA) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[2KD-FTV] G39-27 (VCP2) - G39-29 (EPA2)` | Warna Kabel: BR-R - BR-Y — Power source untuk sensor posisi accelerator pedal (untuk VPA2) | Ignition switch ON: 4.5 sampai 5.0 V |
| `[2KD-FTV] G39-7 (STA) - C23-7 (E1)` | Warna Kabel: B-Y*1 - BR L-Y*2 - BR — Starter signal | Cranking: 6.0 V atau lebih |
| `[2KD-FTV] G38-17 (SPD) - C23-7 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari combination meter | Ignition switch ON, putar roda secara perlahan: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[2KD-FTV] C22-26 (PCR1) - C22-28 (E2)` | Warna Kabel: R-Y - BR — fuel pressure sensor (main) | Idling: 1.7 sampai 2.2 V |
| `[2KD-FTV] G39-15 (GREL) - C23-7 (E1)` | Warna Kabel: R - BR — GLOW relay | Cranking: 11 sampai 14 V |
| `[2KD-FTV] C22-8 (ALT) - C23-7 (E1)` | Warna Kabel: G - BR — Alternator duty ratio | Idling: Pembangkitan pulsa (lihat bentuk gelombang 5) |
| `[2KD-FTV] G38-22 (CAN+)*1 - C23-7 (E1)` | Warna Kabel: V - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 10) |
| `[2KD-FTV] G38-21 (CAN-)*1 - C23-7 (E1)` | Warna Kabel: P - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (lihat bentuk gelombang 11) |
| `[2KD-FTV] C23-2 (VCS) - C23-1 (E2S)` | Warna Kabel: L-W - P-L — Power source pada fuel pressure sensor (sub) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2KD-FTV] C22-20 (THIA) - C22-28 (E2)` | Warna Kabel: Y-G - BR — Intake air temperature sensor (turbo) | Temperatur udara intake: 0.5 sampai 3.4 V |
| `[2KD-FTV] C22-33 (PCR2) - C23-1 (E2S)` | Warna Kabel: G-R - P-L — fuel pressure sensor (sub) | Idling: 1.2 sampai 1.6 V |
| `[2TR-FE] G89-3 (BATT) - C75-3 (E1)` | Warna Kabel: L - BR — Battery (untuk mengukur voltase baterai dan untuk ECM memory) | Selalu: 11 sampai 14 V |
| `[2TR-FE] G89-7 (+BM) - C75-3 (E1)` | Warna Kabel: R-W - BR — Power source aktuator throttle | Selalu: 11 sampai 14 V |
| `[2TR-FE] G89-9 (IGSW) - C75-3 (E1)` | Warna Kabel: B-O - BR — Ignition switch | Ignition switch ON: 11 sampai 14 V |
| `[2TR-FE] G89-1 (+B) - C75-3 (E1)` | Warna Kabel: B - BR — Power source ECM | Ignition switch ON: 11 sampai 14 V |
| `[2TR-FE] C75-13 (OC1+) - C75-12 (OC1-)` | Warna Kabel: P-L - Y — Camshaft timing oil control valve | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[2TR-FE] G89-8 (MREL) - C75-3 (E1)` | Warna Kabel: W-G - BR — MAIN relay | Ignition switch ON: 11 sampai 14 V |
| `[2TR-FE] C76-28 (VG) - C76-30 (E2G)` | Warna Kabel: L-W - L-R — Mass air flow meter | Idle, shift lever dalam posisi P atau N, A/C off: 0.5 sampai 3.0 V |
| `[2TR-FE] C76-29 (THA) - C75-28 (E2)` | Warna Kabel: L-B - BR — Intake air temperature sensor | Idle, temperatur intake air 20°C (68°F): 0.5 sampai 3.4 V |
| `[2TR-FE] C75-32 (THW) - C75-28 (E2)` | Warna Kabel: B - BR — Engine coolant temperature sensor | Idle, temperatur engine coolant 80°C (176°F): 0.2 sampai 1.0 V |
| `[2TR-FE] C75-18 (VC) - C75-28 (E2)` | Warna Kabel: LG-B - BR — Power source dari throttle position sensor (voltase tetap) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2TR-FE] C75-20 (VTA1) - C75-28 (E2)` | Warna Kabel: B-R - BR — Sensor posisi throttle (untuk kontrol mesin) | Ignition switch ON, throttle valve tertutup penuh: 0.5 sampai 1.1 V / Ignition switch ON, throttle valve terbuka penuh: 3.2 sampai 4.8 V |
| `[2TR-FE] C75-19 (VTA2) - C75-28 (E2)` | Warna Kabel: LG - BR — Throttle position sensor (untuk deteksi malfungsi sensor) | Ignition switch ON, throttle valve tertutup penuh: 2.1 sampai 3.1 V / Ignition switch ON, throttle valve terbuka penuh: 4.6 sampai 5.0 V |
| `[2TR-FE] G89-18 (VPA) - G89-20 (EPA)` | Warna Kabel: W-L - BR-W — Accelerator pedal position sensor (untuk kontrol mesin) | Ignition switch ON, accelerator pedal dibebaskan: 0.5 sampai 1.1 V / Ignition switch ON, accelerator pedal ditekan penuh: 2.6 sampai 4.5 V |
| `[2TR-FE] G89-19 (VPA2) - G89-21 (EPA2)` | Warna Kabel: GR-G - BR-Y — Accelerator pedal position sensor (untuk deteksi malfungsi sensor) | Ignition switch ON, accelerator pedal dibebaskan: 1.2 sampai 2.0 V / Ignition switch ON, accelerator pedal ditekan penuh: 3.4 sampai 5.3 V |
| `[2TR-FE] G89-26 (VCPA) - G89-20 (EPA)` | Warna Kabel: LG-R - BR-W — Power source untuk sensor posisi accelerator pedal (untuk VPA) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2TR-FE] G89-27 (VCP2) - G89-21 (EPA2)` | Warna Kabel: BR-R - BR-Y — Power source untuk sensor posisi accelerator pedal (untuk VPA2) | Ignition switch ON: 4.5 sampai 5.5 V |
| `[2TR-FE] C75-21 (A1A+) - C75-28 (E2)` | Warna Kabel: B - BR — Heated oxygen sensor | Putaran mesin dipertahankan pada 2,500 rpm selama 2 menit setelah pemanasan sensor: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[2TR-FE] C75-1 (HA1A) - C76-4 (E03)` | Warna Kabel: Y - W-B — Heater sensor heated oxygen | Ignition switch ON: 11 sampai 14 V |
| `[2TR-FE] C76-6 (#10) - C75-7 (E01)` | Warna Kabel: L - W-B — Fuel injector | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[2TR-FE] C76-5 (#20) - C75-7 (E01)` | Warna Kabel: G - W-B — Fuel injector | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[2TR-FE] C76-2 (#30) - C75-7 (E01)` | Warna Kabel: R - W-B — Fuel injector | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[2TR-FE] C76-1 (#40) - C75-7 (E01)` | Warna Kabel: W - W-B — Fuel injector | Ignition switch ON: 11 sampai 14 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[2TR-FE] C75-29 (KNK1) - C75-30 (EKNK)` | Warna Kabel: B - W — Knock sensor | Putaran mesin dipertahankan pada 4000 rpm setelah mesin dipanaskan: Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[2TR-FE] C75-26 (G2) - C75-34 (NE-)` | Warna Kabel: R - G — Camshaft position sensor | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 5) |
| `[2TR-FE] C75-27 (NE+) - C75-34 (NE-)` | Warna Kabel: L - G — Crankshaft position sensor | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 5) |
| `[2TR-FE] C75-17 (IGT1) - C75-3 (E1)` | Warna Kabel: R - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[2TR-FE] C75-16 (IGT2) - C75-3 (E1)` | Warna Kabel: R-L - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[2TR-FE] C75-15 (IGT3) - C75-3 (E1)` | Warna Kabel: G-B - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[2TR-FE] C75-14 (IGT4) - C75-3 (E1)` | Warna Kabel: G - BR — Ignition coil (sinyal ignition) | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[2TR-FE] C75-23 (IGF1) - C75-3 (E1)` | Warna Kabel: G-R - BR — Ignition coil (sinyal konfirmasi ignition) | Ignition switch ON: 4.5 sampai 5.5 V / Idling: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[2TR-FE] C76-23 (PRG) - C75-3 (E1)` | Warna Kabel: L - BR — Purge VSV | Ignition switch ON: 11 sampai 14 V / Idling, dalam purge control: Pembangkitan pulsa (Lihat bentuk gelombang 7) |
| `[2TR-FE] G88-8 (SPD) - C75-3 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari combination meter | Dikendarai pada 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 8) |
| `[2TR-FE] G89-12 (STA) - C75-3 (E1)` | Warna Kabel: B-Y - BR — Starter signal | Cranking: 6.0 V atau lebih tinggi |
| `[2TR-FE] G89-30 (NSW) - C75-3 (E1)` | Warna Kabel: L-Y - BR — Park/neutral position switch | Ignition switch ON, shift lever tidak dalam posisi P atau N: 11 sampai 14 V / Ignition switch ON, shift lever dalam posisi P atau N: Dibawah 3.0 V |
| `[2TR-FE] G88-4 (STP) - C75-3 (E1)` | Warna Kabel: G-W - BR — Stop light switch | Brake pedal ditekan: 7.5 sampai 14 V / Brake pedal dibebaskan: Dibawah 1.5 V |
| `[2TR-FE] G89-16 (ST1-) - C75-3 (E1)` | Warna Kabel: R-L - BR — Stop light switch (berlawanan dengan voltase pada STP terminal) | Ignition switch ON, brake pedal ditekan: Dibawah 1.5 V / Ignition switch ON, Brake pedal dibebaskan: 7.5 sampai 14 V |
| `[2TR-FE] C75-5 (M+) - C76-3 (ME01)` | Warna Kabel: B - W-B — Throttle actuator | Idling dengan mesin panas: Pembangkitan pulsa (Lihat bentuk gelombang 9) |
| `[2TR-FE] C75-4 (M-) - C76-3 (ME01)` | Warna Kabel: W - W-B — Throttle actuator | Idling dengan mesin panas: Pembangkitan pulsa (Lihat bentuk gelombang 10) |
| `[2TR-FE] G89-25 (FC) - C75-3 (E1)` | Warna Kabel: LG-B - BR — Kontrol pompa bahan bakar | Ignition switch ON: 11 sampai 14 V |
| `[2TR-FE] G88-30 (W) - C75-3 (E1)` | Warna Kabel: R-B - BR — MIL | Ignition switch ON: Dibawah 3.0 V / Idling: 11 sampai 14 V |
| `[2TR-FE] G88-17 (TC) - C75-3 (E1)` | Warna Kabel: P-B - BR — Terminal TC dari DLC3 | Ignition switch ON: 11 sampai 14 V |
| `[2TR-FE] G88-1 (TACH) - C75-3 (E1)` | Warna Kabel: B-W - BR — Putaran mesin | Idling: Pembangkitan pulsa (Lihat bentuk gelombang 11) |
| `[2TR-FE] C75-10 (ALT) - C75-3 (E1)` | Warna Kabel: G - BR — Generator | Ignition switch ON: 11 sampai 14 V |
| `[2TR-FE] G89-15 (ELS) - C75-3 (E1)` | Warna Kabel: G - BR — Beban kelistrikan | Taillight switch on: 7.5 sampai 14 V / Taillight switch off: Dibawah 1.5 V |
| `[2TR-FE] G88-3 (ELS3) - C75-3 (E1)` | Warna Kabel: B - BR — Beban kelistrikan | Switch lampu kabut ON: 7.5 sampai 14 V / Switch lampu kabut off: Dibawah 1.5 V |
| `[2TR-FE] G88-14 (THWO) - C75-3 (E1)` | Warna Kabel: P - BR — Sinyal putaran mesin dikirim ke combination meter | Idling dengan mesin panas: Pembangkitan pulsa |
| `[2TR-FE] G88-32 (F/PS) - C75-3 (E1)` | Warna Kabel: B - BR — Center airbag sensor assembly | Ignition switch on: Pembangkitan pulsa |
| `[2TR-FE] C76-32 (PSW) - C75-3 (E1)` | Warna Kabel: G-Y - BR — Power steering oil pressure switch | Selama steering wheel dibelokkan: Dibawah 1.5 V |
| `[A/T A340E] C24-12 (NSW) - C24-1 (E1)` | Warna Kabel: L-Y - BR — Sinyal PNP switch | Ignition switch ON Shift lever dalam posisi P atau N: Dibawah 1 V / Ignition switch ON Shift lever tidak dalam posisi P atau N: 11 sampai 14 V |
| `[A/T A340E] G40-9 (R) - C24-1 (E1)` | Warna Kabel: R-Y - BR — Sinyal switch posisi pemindahan R | Ignition switch ON Shift lever dalam posisi R: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi R: Dibawah 1 V |
| `[A/T A340E] G40-8 (D) - C24-1 (E1)` | Warna Kabel: G-Y - BR — Sinyal switch posisi pemindahan D | Ignition switch ON Shift lever dalam posisi D atau 3: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi D atau 3: Dibawah 1 V |
| `[A/T A340E] G40-12 (3) - C24-1 (E1)` | Warna Kabel: G-O - BR — Sinyal 3 shift position switch | Ignition switch ON Shift lever dalam posisi 3: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 3: Dibawah 1 V |
| `[A/T A340E] G40-11 (2) - C24-1 (E1)` | Warna Kabel: L - BR — Sinyal 2 shift position switch | Ignition switch ON Shift lever dalam posisi 2: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 2: Dibawah 1 V |
| `[A/T A340E] G40-10 (L) - C24-1 (E1)` | Warna Kabel: G-R - BR — Sinyal switch posisi pemindahan L | Ignition switch ON Shift lever dalam posisi L: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi L: Dibawah 1 V |
| `[A/T A340E] C24-18 (S1) - C24-1 (E1)` | Warna Kabel: GR - BR — Sinyal solenoid S1 | Gear 1st atau 2nd: 11 sampai 14 V / Gear 3rd atau 4th: Dibawah 1 V |
| `[A/T A340E] C24-17 (S2) - C24-1 (E1)` | Warna Kabel: W-L - BR — Sinyal solenoid S2 | Gear 2nd atau 3rd: 11 sampai 14 V / Gear 1st atau 4th: Dibawah 1 V |
| `[A/T A340E] C24-20 (SLT+) - C24-19 (SLT-)` | Warna Kabel: G-Y - L-B — Sinyal solenoid SLT | Mesin idle: Pembangkitan pulsa |
| `[A/T A340E] C24-16 (SL) - C24-1 (E1)` | Warna Kabel: G - BR — Sinyal SL solenoid | Kecepatan kendaraan 65 km/jam (40 mph), lock-up (ON ke OFF): Pembangkitan pulsa (Lihat bentuk gelombang 1) / Kendaraan dikendarai dalam kondisi lock-up: 11 sampai 14 V |
| `[A/T A340E] C24-24 (THOC) - C24-23 (E2)` | Warna Kabel: BR - B-Y — Sinyal ATF temperature sensor | Temperatur ATF: 115°C (239°F) atau lebih tinggi: Dibawah 1.5 V |
| `[A/T A340E] C24-30 (SP2+) - C24-29 (SP2-)` | Warna Kabel: R - G — Sinyal speed sensor SP2 | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T A340E] C24-3 (NC0+) - C24-2 (NC0-)` | Warna Kabel: V - P — Sinyal speed sensor NC0 | Mesin idle (posisi shift lever dalam P atau N): Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[A/T A340E] G41-25 (SPD1) - C24-1 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[A/T A340E] G41-14 (STP) - C24-1 (E1)` | Warna Kabel: G-W - BR — Sinyal STP light switch | Brake pedal diinjak: 7.5 sampai 14 V / Brake pedal dibebaskan: Dibawah 1 V |
| `[A/T A340E] C24-11 (STA) - C24-1 (E1)` | Warna Kabel: B-Y - BR — Starter signal | Cranking: 6 V atau lebih |
| `[A/T A340E] G41-6 (IG2) - C24-1 (E1)` | Warna Kabel: B-O - BR — Ignition switch | Ignition switch ON: 11 sampai 14 V |
| `[A/T A340E] G41-21 (CAN+) - C24-1 (E1)` | Warna Kabel: V - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 5) |
| `[A/T A340E] G41-20 (CAN-) - C24-1 (E1)` | Warna Kabel: P - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[A/T A340E] G39-1 (+B) - C23-7 (E1)` | Warna Kabel: B - BR — Power source ECM | Ignition switch ON: 11 sampai 14 V |
| `[A/T A340E] G38-22 (CAN+) - C23-7 (E1)` | Warna Kabel: V - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[A/T A340E] G38-21 (CAN-) - C23-7 (E1)` | Warna Kabel: P - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T A340F] C24-12 (NSW) - C24-1 (E1)` | Warna Kabel: L-Y - BR — Sinyal PNP switch | Ignition switch ON Shift lever dalam posisi P atau N: Dibawah 1 V / Ignition switch ON Shift lever tidak dalam posisi P atau N: 11 sampai 14 V |
| `[A/T A340F] G40-9 (R) - C24-1 (E1)` | Warna Kabel: R-Y - BR — Sinyal switch posisi pemindahan R | Ignition switch ON Shift lever dalam posisi R: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi R: Dibawah 1 V |
| `[A/T A340F] G40-8 (D) - C24-1 (E1)` | Warna Kabel: G-Y - BR — Sinyal switch posisi pemindahan D | Ignition switch ON Shift lever dalam posisi D atau 3: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi D atau 3: Dibawah 1 V |
| `[A/T A340F] G40-12 (3) - C24-1 (E1)` | Warna Kabel: G-O - BR — Sinyal 3 shift position switch | Ignition switch ON Shift lever dalam posisi 3: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 3: Dibawah 1 V |
| `[A/T A340F] G40-11 (2) - C24-1 (E1)` | Warna Kabel: L - BR — Sinyal 2 shift position switch | Ignition switch ON Shift lever dalam posisi 2: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 2: Dibawah 1 V |
| `[A/T A340F] G40-10 (L) - C24-1 (E1)` | Warna Kabel: G-R - BR — Sinyal switch posisi pemindahan L | Ignition switch ON Shift lever dalam posisi L: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi L: Dibawah 1 V |
| `[A/T A340F] C24-18 (S1) - C24-1 (E1)` | Warna Kabel: GR - BR — Sinyal solenoid S1 | Gear 1st atau 2nd: 11 sampai 14 V / Gear 3rd atau 4th: Dibawah 1 V |
| `[A/T A340F] C24-17 (S2) - C24-1 (E1)` | Warna Kabel: W-L - BR — Sinyal solenoid S2 | Gear 2nd atau 3rd: 11 sampai 14 V / Gear 1st atau 4th: Dibawah 1 V |
| `[A/T A340F] C24-20 (SLT+) - C24-19 (SLT-)` | Warna Kabel: G-Y - L-B — Sinyal solenoid SLT | Mesin idle: Pembangkitan pulsa |
| `[A/T A340F] C24-16 (SL) - C24-1 (E1)` | Warna Kabel: G - BR — Sinyal SL solenoid | Kecepatan kendaraan 65 km/jam (40 mph), lock-up (ON ke OFF): Pembangkitan pulsa (Lihat bentuk gelombang 1) / Kendaraan dikendarai dalam kondisi lock-up: 11 sampai 14 V |
| `[A/T A340F] C24-24 (THOC) - C24-23 (E2)` | Warna Kabel: BR - B-Y — Sinyal ATF temperature sensor | Temperatur ATF: 115°C (239°F) atau lebih tinggi: Dibawah 1.5 V |
| `[A/T A340F] C24-30 (SP2+) - C24-29 (SP2-)` | Warna Kabel: R - G — Sinyal speed sensor SP2 | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T A340F] C24-3 (NC0+) - C24-2 (NC0-)` | Warna Kabel: V - P — Sinyal speed sensor NC0 | Mesin idle (posisi shift lever dalam P atau N): Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[A/T A340F] G40-15 (L4) - C24-1 (E1)` | Warna Kabel: G-W - BR — Sinyal posisi L4 | Ignition switch ON Transfer di L4: Dibawah 1 V / Ignition switch ON Transfer tidak di L4: 11 sampai 14 V |
| `[A/T A340F] G41-25 (SPD1) - C24-1 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[A/T A340F] G41-14 (STP) - C24-1 (E1)` | Warna Kabel: G-W - BR — Sinyal STP light switch | Brake pedal diinjak: 7.5 sampai 14 V / Brake pedal dibebaskan: Dibawah 1 V |
| `[A/T A340F] C24-11 (STA) - C24-1 (E1)` | Warna Kabel: B-Y - BR — Starter signal | Cranking: 6 V atau lebih |
| `[A/T A340F] G40-16 (TFN) - C24-1 (E1)` | Warna Kabel: W-G - BR — Sinyal switch posisi pemindahan N | Ignition switch ON Transfer di N: Dibawah 1 V / Ignition switch ON Transfer tidak di N: 11 sampai 14 V |
| `[A/T A340F] G41-6 (IG2) - C24-1 (E1)` | Warna Kabel: B-O - BR — Ignition switch | Ignition switch ON: 11 sampai 14 V |
| `[A/T A340F] G41-21 (CAN+) - C24-1 (E1)` | Warna Kabel: V - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 5) |
| `[A/T A340F] G41-20 (CAN-) - C24-1 (E1)` | Warna Kabel: P - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 6) |
| `[A/T A340F] G39-1 (+B) - C23-7 (E1)` | Warna Kabel: B - BR — Power source ECM | Ignition switch ON: 11 sampai 14 V |
| `[A/T A340F] G38-22 (CAN+) - C23-7 (E1)` | Warna Kabel: V - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[A/T A340F] G38-21 (CAN-) - C23-7 (E1)` | Warna Kabel: P - BR — CAN communication line | Ignition switch ON: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T A343E] G89-30 (NSW) - C75-3 (E1)` | Warna Kabel: L-Y - BR — Sinyal PNP switch | Ignition switch ON Shift lever dalam posisi P atau N: Dibawah 1 V / Ignition switch ON Shift lever tidak dalam posisi P atau N: 11 sampai 14 V |
| `[A/T A343E] G88-11 (R) - C75-3 (E1)` | Warna Kabel: R-Y - BR — Sinyal switch posisi pemindahan R | Ignition switch ON Shift lever dalam posisi R: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi R: Dibawah 1 V |
| `[A/T A343E] G88-19 (3) - C75-3 (E1)` | Warna Kabel: G-O - BR — Sinyal 3 shift position switch | Ignition switch ON Shift lever dalam posisi 3: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 3: Dibawah 1 V |
| `[A/T A343E] G88-10 (2) - C75-3 (E1)` | Warna Kabel: L - BR — Sinyal 2 shift position switch | Ignition switch ON Shift lever dalam posisi 2: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 2: Dibawah 1 V |
| `[A/T A343E] G88-9 (L) - C75-3 (E1)` | Warna Kabel: G-R - BR — Sinyal switch posisi pemindahan L | Ignition switch ON Shift lever dalam posisi L: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi L: Dibawah 1 V |
| `[A/T A343E] C76-9 (S1) - C75-3 (E1)` | Warna Kabel: B-W - BR — Sinyal solenoid S1 | Gear 1st atau 2nd: 11 sampai 14 V / Gear 3rd atau 4th: Dibawah 1 V |
| `[A/T A343E] C76-8 (S2) - C75-3 (E1)` | Warna Kabel: B-R - BR — Sinyal solenoid S2 | Gear 2nd atau 3rd: 11 sampai 14 V / Gear 1st atau 4th: Dibawah 1 V |
| `[A/T A343E] C76-12 (SLT+) - C76-13 (SLT-)` | Warna Kabel: B-L - B-Y — Sinyal solenoid SLT | Mesin idle: Pembangkitan pulsa |
| `[A/T A343E] C76-11 (SL) - C75-3 (E1)` | Warna Kabel: L-Y - BR — Sinyal SL solenoid | Kecepatan kendaraan 65 km/jam (40 mph), lock-up (ON ke OFF): Pembangkitan pulsa (Lihat bentuk gelombang 1) / Kendaraan dikendarai dalam kondisi lock-up: 11 sampai 14 V |
| `[A/T A343E] C75-22 (THOC) - C75-28 (E2)` | Warna Kabel: W-L - BR — Sinyal ATF temperature sensor | Temperatur ATF: 115°C (239°F) atau lebih tinggi: Dibawah 1.5 V |
| `[A/T A343E] C76-35 (SP2+) - C76-27 (SP2-)` | Warna Kabel: G - R — Sinyal speed sensor SP2 | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T A343E] C76-34 (NC0+) - C76-26 (NC0-)` | Warna Kabel: V - P — Sinyal speed sensor NC0 | Mesin idle (posisi shift lever dalam P atau N): Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[A/T A343E] G88-8 (SPD) - C75-3 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[A/T A343E] G88-4 (STP) - C75-3 (E1)` | Warna Kabel: G-W - BR — Sinyal STP light switch | Ignition switch ON Brake pedal diinjak: 11 sampai 14 V / Ignition switch ON Brake pedal dibebaskan: Dibawah 1 V |
| `[A/T A343E] G89-12 (STA) - C75-3 (E1)` | Warna Kabel: B-Y - BR — Starter signal | Cranking: 6 V atau lebih |
| `[A/T A343E] G88-13 (SIL) - C75-3 (E1)` | Warna Kabel: R-Y - BR — Terminal SIL dari DLC3 | Hubungkan intelligent tester ke DLC3: Pembangkitan pulsa |
| `[A/T A343E] G88-35 (WFSE) - C75-3 (E1)` | Warna Kabel: W - BR — Terminal SIL dari DLC3 | Ignition switch ON: 11 sampai 14 V |
| `[A/T A343F] G89-30 (NSW) - C75-3 (E1)` | Warna Kabel: L-Y - BR — Sinyal PNP switch | Ignition switch ON Shift lever dalam posisi P atau N: Dibawah 1 V / Ignition switch ON Shift lever tidak dalam posisi P atau N: 11 sampai 14 V |
| `[A/T A343F] G88-11 (R) - C75-3 (E1)` | Warna Kabel: R-Y - BR — Sinyal switch posisi pemindahan R | Ignition switch ON Shift lever dalam posisi R: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi R: Dibawah 1 V |
| `[A/T A343F] G88-19 (3) - C75-3 (E1)` | Warna Kabel: G-O - BR — Sinyal 3 shift position switch | Ignition switch ON Shift lever dalam posisi 3: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 3: Dibawah 1 V |
| `[A/T A343F] G88-10 (2) - C75-3 (E1)` | Warna Kabel: L - BR — Sinyal 2 shift position switch | Ignition switch ON Shift lever dalam posisi 2: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi 2: Dibawah 1 V |
| `[A/T A343F] G88-9 (L) - C75-3 (E1)` | Warna Kabel: G-R - BR — Sinyal switch posisi pemindahan L | Ignition switch ON Shift lever dalam posisi L: 11 sampai 14 V / Ignition switch ON Shift lever tidak dalam posisi L: Dibawah 1 V |
| `[A/T A343F] C76-9 (S1) - C75-3 (E1)` | Warna Kabel: B-W - BR — Sinyal solenoid S1 | Gear 1st atau 2nd: 11 sampai 14 V / Gear 3rd atau 4th: Dibawah 1 V |
| `[A/T A343F] C76-8 (S2) - C75-3 (E1)` | Warna Kabel: B-R - BR — Sinyal solenoid S2 | Gear 2nd atau 3rd: 11 sampai 14 V / Gear 1st atau 4th: Dibawah 1 V |
| `[A/T A343F] C76-12 (SLT+) - C76-13 (SLT-)` | Warna Kabel: B-L - B-Y — Sinyal solenoid SLT | Mesin idle: Pembangkitan pulsa |
| `[A/T A343F] C76-11 (SL) - C75-3 (E1)` | Warna Kabel: L-Y - BR — Sinyal SL solenoid | Kecepatan kendaraan 65 km/jam (40 mph), lock-up (ON ke OFF): Pembangkitan pulsa (Lihat bentuk gelombang 1) / Kendaraan dikendarai dalam kondisi lock-up: 11 sampai 14 V |
| `[A/T A343F] C75-22 (THOC) - C75-28 (E2)` | Warna Kabel: W-L - BR — Sinyal ATF temperature sensor | Temperatur ATF: 115°C (239°F) atau lebih tinggi: Dibawah 1.5 V |
| `[A/T A343F] C76-35 (SP2+) - C76-27 (SP2-)` | Warna Kabel: G - R — Sinyal speed sensor SP2 | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T A343F] C76-34 (NC0+) - C76-26 (NC0-)` | Warna Kabel: V - P — Sinyal speed sensor NC0 | Mesin idle (posisi shift lever dalam P atau N): Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[A/T A343F] G89-11 (L4) - C75-3 (E1)` | Warna Kabel: G-W - BR — Sinyal posisi L4 | Ignition switch ON Transfer di L4: Dibawah 1 V / Ignition switch ON Transfer tidak di L4: 11 sampai 14 V |
| `[A/T A343F] G88-8 (SPD) - C75-3 (E1)` | Warna Kabel: V-R - BR — Sinyal kecepatan | Kecepatan kendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 4) |
| `[A/T A343F] G88-4 (STP) - C75-3 (E1)` | Warna Kabel: G-W - BR — Sinyal STP light switch | Ignition switch ON Brake pedal diinjak: 11 sampai 14 V / Ignition switch ON Brake pedal dibebaskan: Dibawah 1 V |
| `[A/T A343F] G89-12 (STA) - C75-3 (E1)` | Warna Kabel: B-Y - BR — Starter signal | Cranking: 6 V atau lebih |
| `[A/T A343F] G89-23 (TFN) - C75-3 (E1)` | Warna Kabel: W-G - BR — Sinyal switch posisi pemindahan N | Ignition switch ON Transfer di N: Dibawah 1 V / Ignition switch ON Transfer tidak di N: 11 sampai 14 V |
| `[A/T A343F] G88-13 (SIL) - C75-3 (E1)` | Warna Kabel: R-Y - BR — Terminal SIL dari DLC3 | Hubungkan intelligent tester ke DLC3: Pembangkitan pulsa |
| `[A/T A343F] G88-35 (WFSE) - C75-3 (E1)` | Warna Kabel: W - BR — Terminal SIL dari DLC3 | Ignition switch ON: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-1 (+BS) - Body ground` | Warna Kabel: W - R — ABS solenoid power supply | Selalu: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-2 (GND1) - Body ground` | Warna Kabel: W - B — Ground | Selalu: Dibawah 1 Ω |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-3 (EXI4)* - Body ground` | Warna Kabel: G - W — Input LL position switch (transfer indicator switch No. 1) | Transfer shift position LL: Dibawah 1 Ω |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-10 (STP) - Body ground` | Warna Kabel: G - W — Input stop light switch | Brake pedal ditekan: 8 sampai 14 V / Brake pedal dibebaskan: Dibawah 1.5 V |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-17 (EXI)* - Body ground` | Warna Kabel: R - B — Input center differential lock position switch (transfer indicator switch No. 3) | Ignition switch ON Transfer shift position H: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-18 (PKB) - Body ground` | Warna Kabel: L - O — Input parking brake switch | Ignition switch ON Parking brake digunakan: Dibawah 1.5 V / Ignition switch ON Parking brake dibebaskan: 10 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-22 (EXI2) - Body ground` | Warna Kabel: V — Input IG power supply | Ignition switch ON: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-23 (+BM) - Body ground` | Warna Kabel: R — ABS motor relay power supply | Selalu: 11 sampai 14 V |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-24 (GND2) - Body ground` | Warna Kabel: W - B — Ground | Selalu: Dibawah 1 Ω |
| `[SISTEM KONTROL REM / KONTROL DINAMIS] A13-25 (IG1) - Body ground` | Warna Kabel: R - L — Skid control ECU (Brake actuator assembly) power supply | Ignition switch ON: 11 sampai 14 V |
| `[AUDIO / VIDEO] G5-1 (FR+) - G5-7 (GND)` | Warna Kabel: LG - BR — Sinyal suara (Front right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G5-2 (FL+) - G5-7 (GND)` | Warna Kabel: P - BR — Sinyal suara (Front left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G5-5 (FR-) - G5-7 (GND)` | Warna Kabel: L - BR — Sinyal suara (Front right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G5-6 (FL-) - G5-7 (GND)` | Warna Kabel: V - BR — Sinyal suara (Front left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G5-7 (GND) - Body ground` | Warna Kabel: BR - Body ground — Ground | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G4-1 (RR+) - G5-7 (GND)` | Warna Kabel: R - BR — Sound signal (Rear right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G4-2 (RL+) - G5-7 (GND)` | Warna Kabel: B - BR — Sinyal suara (Rear left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G4-3 (RR-) - G5-7 (GND)` | Warna Kabel: W - BR — Sound signal (Rear right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G4-6 (RL-) - G5-7 (GND)` | Warna Kabel: Y - BR — Sinyal suara (Rear left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G1-11 (AGND) - Body ground` | Warna Kabel: Shielded - Body ground — Ground berpelindung | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G1-17 (SPD) - G5-7 (GND)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari combination meter | Ignition switch ON, drive wheels dibelokkan pelahan: Pembangkitan pulsa |
| `[AUDIO / VIDEO] G1-21 (SW1) - G5-7 (GND)` | Warna Kabel: R - BR — Sinyal switch steering pad | Steering pad switch tidak dioperasikan: 2.8 sampai 3.6 V / Switch seek+ ditekan: 0 sampai 0.6 V / Switch seek- ditekan: 0.6 sampai 1.3 V / Switch volume+ ditekan: 1.3 sampai 2.1 V / Switch volume- ditekan: 2.1 sampai 2.8 |
| `[AUDIO / VIDEO] G1-22 (SW2) - G5-7 (GND)` | Warna Kabel: W - BR — Sinyal switch steering pad | Steering pad switch tidak dioperasikan: 2.8 sampai 3.6 V / Switch MODE ditekan: 0 sampai 0.6 V |
| `[AUDIO / VIDEO] G1-23 (SWG) - G5-7 (GND)` | Warna Kabel: L - BR — Masa switch steering pad | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G1-27 (VA-) - G5-7 (GND)` | Warna Kabel: W - BR — Ground | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] z2-4 (UGD1) - Body ground` | Warna Kabel: # - Body ground — Ground | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G129-1 (FR+) - G129-7 (GND)` | Warna Kabel: LG - BR — Sinyal suara (Front Right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G129-2 (FL+) - G129-7 (GND)` | Warna Kabel: P - BR — Sinyal suara (Front Left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G129-3 (ACC) - G129-7 (GND)` | Warna Kabel: GR - BR — Accessory (ON) | Ignition switch off: Dibawah 1 V / Ignition switch ACC: 11 sampai 14 V |
| `[AUDIO / VIDEO] G129-5 (FR-) - G129-7 (GND)` | Warna Kabel: L - BR — Sinyal suara (Front Right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G129-6 (FL-) - G129-7 (GND)` | Warna Kabel: V - BR — Sinyal suara (Front Left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G129-7 (GND) - Body ground` | Warna Kabel: BR - Body ground — Ground | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G128-1 (RR+) - G129-7 (GND)` | Warna Kabel: R - BR — Sinyal suara (Rear Right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G128-2 (RL+) - G129-7 (GND)` | Warna Kabel: B - BR — Sinyal suara (Rear Left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G128-3 (RR-) - G129-7 (GND)` | Warna Kabel: W - BR — Sinyal suara (Rear Right) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G128-6 (RL-) - G129-7 (GND)` | Warna Kabel: Y - BR — Sinyal suara (Rear Left) | Memainkan sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VIDEO] G127-1 (IG) - G129-7 (GND)` | Warna Kabel: P - BR — Sinyal IG | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[AUDIO / VIDEO] G127-4 (MACC) - Body ground` | Warna Kabel: B - Body ground — Power supply AMP mikrofon | Ignition switch off: Dibawah 1 V / Ignition switch ACC: 4 sampai 6 V |
| `[AUDIO / VIDEO] G127-5 (MIN+) - Body ground` | Warna Kabel: W - Body ground — Sinyal suara microphone | Set "Memeriksa Suara Microphone & Pengenalan" (Lihat halaman ): - |
| `[AUDIO / VIDEO] G127-6 (SNS2) - Body ground` | Warna Kabel: W-B - Body ground — Sinyal deteksi hubungan microphone | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G127-11 (AGND) - Body ground` | Warna Kabel: Shielded - Body ground — Ground berpelindung | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G127-17 (SPD) - G129-7 (GND)` | Warna Kabel: V-R - BR — Sinyal kecepatan dari combination meter | Lihat "Sinyal Kendaraan" (Lihat halaman ).: - |
| `[AUDIO / VIDEO] G127-18 (SGND) - G129-7 (GND)` | Warna Kabel: Shield - BR — Ground berpelindung | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G127-19 (MIN-) - Body ground` | Warna Kabel: R - Body ground — Sinyal suara microphone | Set "Memeriksa Suara Microphone & Pengenalan" (Lihat halaman ): - |
| `[AUDIO / VIDEO] G127-21 (SW1) - G129-7 (GND)` | Warna Kabel: R - BR — Sinyal switch steering pad | Steering pad switch tidak dioperasikan: 4.44 sampai 5.43 V / Switch seek+ ditekan: 0.45 sampai 0.65 V / Switch seek- ditekan: 1.19 sampai 1.49 V / Switch volume+ ditekan: 2.09 sampai 2.54 V / Switch volume- ditekan: 3.20 |
| `[AUDIO / VIDEO] G127-23 (SWG) - G129-7 (GND)` | Warna Kabel: L - BR — Masa switch steering pad | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G127-27 (VA-) - G129-7 (GND)` | Warna Kabel: W - BR — Ground | Selalu: Dibawah 1 V |
| `[AUDIO / VIDEO] G2-6 (PKB) - G129-7 (GND)` | Warna Kabel: LG - BR — Sinyal parking brake | Lihat "Sinyal Kendaraan" (Lihat halaman ).: - |
| `[AUDIO / VIDEO] z6-4 (UGD1) - Body ground` | Warna Kabel: # - Body ground — Ground | Selalu: Dibawah 1 V |
| `[PARK ASSIST / MONITORING] T1-3 (SPD) - Body ground` | Warna Kabel: V-R - Body ground — Sinyal kecepatan kendaraan | Ignition switch ON, back sonar or clearance sonar switch ON, input sinyal kecepatan kendaraan: Pembangkitan pulsa (Merubah frekuensi sesuai untuk kecepatan kendaraan) |
| `[PARK ASSIST / MONITORING] T1-6 (SOR) - T1-22 (E2)` | Warna Kabel: P - L — Sinyal komunikasi ultrasonic sensor No. 1 | Ignition switch ON, back sonar or clearance sonar switch ON, sensor mendeteksi rintangan: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[PARK ASSIST / MONITORING] T1-10 (IG) - Body ground` | Warna Kabel: L-R - Body ground — Sirkuit IG power source | Ignition switch ON, back sonar or clearance sonar switch ON: 11 sampai 14 V / Ignition switch ON, back sonar or clearance sonar switch OFF: Dibawah 1 V |
| `[PARK ASSIST / MONITORING] T1-12 (BBZ) - Body ground` | Warna Kabel: P-G - Body ground — Sinyal clearance warning buzzer No. 1 | Ignition switch ON, back or atau clearance sonar switch ON, shift lever dalam posisi reverse dan sensor dalam status mendeteksi (membunyikan buzzer): Pembangkitan pulsa (Lihat bentuk gelombang 2) / Buzzer tidak berbunyi: |
| `[PARK ASSIST / MONITORING] T1-13 (RL) - T1-21 (E)` | Warna Kabel: R-W - W-B — Sinyal posisi reverse | Ignition switch ON, pindahkan shift lever ke R: 7 V atau lebih tinggi / Ignition switch ON, pindahkan shift lever ke posisi manapun selain R: Dibawah 1 V |
| `[PARK ASSIST / MONITORING] T1-21 (E) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[PARK ASSIST / MONITORING] T1-22 (E2) - Body ground` | Warna Kabel: L - Body ground — Ground ultrasonic sensor No. 1 | Selalu: Dibawah 1 V |
| `[PARK ASSIST / MONITORING] T1-24 (BOR) - T1-22 (E2)` | Warna Kabel: BR - L — Sirkuit ultrasonic sensor power source No. 1 | Ignition switch ON, back sonar or clearance sonar switch ON: 7.2 sampai 8.8 V / Ignition switch off: Dibawah 1 V |
| `[PARK ASSIST / MONITORING] G127-1 (IG) - G129-7 (GND)` | Warna Kabel: P - BR — Sinyal IG | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[PARK ASSIST / MONITORING] G129-7 (GND) - Body ground` | Warna Kabel: BR - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[PARK ASSIST / MONITORING] G127-2 (REV) - G129-7 (GND)` | Warna Kabel: R-Y - BR — Sinyal mundur | Ignition switch ON, shift lever di R: 7.5 sampai 14 V / Ignition switch ON, shift lever tidak di R: Dibawah 1 V |
| `[PARK ASSIST / MONITORING] G2-8 (V+) - G2-16 (V-)` | Warna Kabel: W - R — Sinyal tampilan | Ignition switch ON, shift lever di R: Pembangkitan pulsa (Lihat bentuk gelombang 1) / Ignition switch ON, shift lever di R, screen hitam keluar dengan mencakup lensa kamera: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[PARK ASSIST / MONITORING] G2-15 (CGND) - Body ground` | Warna Kabel: Shielded - Body ground — Shielding | Selalu: Dibawah 1 V |
| `[DOOR LOCK] 2D-9 (GND) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[DOOR LOCK] 2D-18 (GND) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[DOOR LOCK] 2H-4 (ALTB) - Body ground` | Warna Kabel: LG - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] 2L-12 (BECU) - Body ground` | Warna Kabel: L - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] 2A-4 (L1) - Body ground` | Warna Kabel: L - Body ground — Sinyal input lock pada power window regulator master switch assembly (door control switch) Driver side door k | Power window regulator master switch assembly (door control switch) dikunci Driver side door key cylinder dalam posisi lock: Dibawah 1 V / Power window regulator master switch assembly (door control switch) off Ignition  |
| `[DOOR LOCK] 2D-4 (UL1) - Body ground` | Warna Kabel: L-W - Body ground — Sinyal input unlock pada power window regulator master switch assembly (door control switch) Driver side do | Power window regulator master switch assembly (switch kontrol pintu) tidak terkunci Driver side door key cylinder dalam posisi unlock: Dibawah 1 V / Power window regulator master switch assembly (door control switch) off |
| `[DOOR LOCK] 2K-10 (ACT-) - Body ground` | Warna Kabel: L-Y - Body ground — Sinyal output penggerak unlock pada door lock motor (pintu penumpang, pintu belakang RH*1 atau LH*2 dan bac | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] 2K-11 (ACT+) - Body ground` | Warna Kabel: L - Body ground — Output penggerak lock pada door lock motor (pintu penumpang, pintu belakang RH*1 atau LH*2 dan back door) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] 2O-27 (DCTY) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal input front door courtesy light switch assembly LH*1 atau RH*2 | Driver side door terbuka: Dibawah 1 V / Driver side door ditutup: 11 sampai 14 V |
| `[DOOR LOCK] 2R-27 (ACT-) - Body ground` | Warna Kabel: L-Y - Body ground — Sinyal output penggerak unlock pada door lock motor (pintu pengemudi dan pintu belakang LH*1 atau RH*2) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] 2R-28 (ACT+) - Body ground` | Warna Kabel: L - Body ground — Sinyal output penggerak lock pada door lock motor (pintu pengemudi dan pintu belakang LH*1 atau RH*2) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] G29-1 (E) - Body ground` | Warna Kabel: B-W - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[DOOR LOCK] G29-4 (+B1) - Body ground` | Warna Kabel: L-Y - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] G29-14 (+B2) Body ground` | Warna Kabel: LG - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] G29-18 (IG) Body ground` | Warna Kabel: R-L - Body ground — Ignition power supply | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[DOOR LOCK] G29-7 (CTY) - Body ground` | Warna Kabel: R-L - Body ground — Sinyal input switch semua door courtesy | Satu atau lebih pintu terbuka: Dibawah 1 V / Semua pintu ditutup: 11 sampai 14 V |
| `[DOOR LOCK] G29-17 (SPD) - Body ground` | Warna Kabel: V-R - Body ground — Sinyal input kecepatan kendaraan | Pengendaraan sekitar 20 km/jam (12.4 mph): Pulse generation (Lihat bentuk gemombang 1) |
| `[DOOR LOCK] G29-14 (+B2) - Body ground` | Warna Kabel: G - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] G29-18 (IG) - Body ground` | Warna Kabel: R-L - Body ground — Ignition power supply | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[DOOR LOCK] G29-3 (DMLP) - Body ground` | Warna Kabel: P - Body ground — Sinyal output interior light | Interior light menyala: Dibawah 1 V / Interior light padam: 11 sampai 14 V |
| `[DOOR LOCK] G29-5 (KSW) - Body ground` | Warna Kabel: G-Y - Body ground — Sinyal input unlock warning switch signal | Tidak terdapat kunci dalam ignition key cylinder: 10 kΩ atau lebih tinggi / Kunci dimasukkan ke dalam ignition key cylinder: Dibawah 1 Ω |
| `[DOOR LOCK] G29-7 (CTY) - Body ground` | Warna Kabel: R-L - Body ground — Sinyal input semua door courtesy switch signal | Satu atau lebih pintu terbuka: Dibawah 1 V / Semua pintu tertutup: 11 sampai 14 V |
| `[DOOR LOCK] G29-13 (SH-) - Body ground` | Warna Kabel: B - Body ground — Sinyal output security horn | Security horn assembly mati: Dibawah 1 V / Security horn assembly menyala: Pembangkitan pulsa |
| `[DOOR LOCK] G29-25 (L2) - Body ground` | Warna Kabel: L - Body ground — Sinyal ouput kunci pintu | Ignition switch ke off, semua pintu ditutup dan transmitter switch tidak ditekan: Dibawah 1 V / Ignition switch ke off, semua pintu ditutup dan transmitter lock switch ditekan: Pembangkitan pulsa |
| `[DOOR LOCK] G29-26 (UL3) -Body ground` | Warna Kabel: L-W - Body ground — Sinyal output pada pintu unlock | Ignition switch ke off, semua pintu ditutup dan transmitter switch tidak ditekan: Dibawah 1 V / Ignition switch ke OFF, semua pintu tertutup dan transmitter unlock switch ditekan: Pembangkitan pulsa |
| `[DOOR LOCK] G29-28 (HAZD) - Body ground` | Warna Kabel: G-O - Body ground — Semua sinyal output hazard warning light | Hazard warning signal switch assembly off: 11 sampai 14 V / Hazard warning signal switch assembly on: Dibawah 1 V |
| `[DOOR LOCK] 2K-10 (ACT-) - Body ground` | Warna Kabel: L-Y - Body ground — Sinyal output penggerak unlock pada door lock motor (pintu penumpang, pintu belakang RH dan back door) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] 2K-11 (ACT+) - Body ground` | Warna Kabel: L - Body ground — Output penggerak lock pada door lock motor (pintu penumpang, pintu belakang RH dan back door) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Power window regulator master switch assembly (door control switch) a |
| `[DOOR LOCK] 2O-27 (DCTY) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal input front door courtesy light switch assembly LH | Driver side door terbuka: Dibawah 1 V / Driver side door ditutup: 11 sampai 14 V |
| `[DOOR LOCK] 2R-27 (ACT-) - Body ground` | Warna Kabel: L-Y - Body ground — Sinyal output penggerak unlock pada door lock motor (pintu pengemudi dan pintu belakang LH) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] 2R-28 (ACT+) - Body ground` | Warna Kabel: L - Body ground — Sinyal output pengerak lock pada door lock motor (pintu pengemudi dan pintu belakang LH) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Power window regulator master switch assembly (door control switch) a |
| `[DOOR LOCK] 2A-6 (SIG) - Body ground` | Warna Kabel: B-Y - Body ground — Ignition switch | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[DOOR LOCK] 2D-2 (RDA) - Body ground` | Warna Kabel: V-R - Body ground — Sinyal input dari door control receiver | Ignition switch ke off, semua pintu ditutup dan transmitter switch tidak ditekan: 11 sampai 14 V / Ignition switch ke off, semua pintu ditutup dan transmitter switch ditekan.: Pembangkitan pulsa |
| `[DOOR LOCK] 2D-5 (PRG) - Body ground` | Warna Kabel: G-W - Body ground — Sinyal output door control receiver | Kunci dimasukkan ke dalam ignition key cylinder → Seperti kunci dicabut dari ignition key cylinder: 11 sampai 14 V → Pembangkit pulsa → 11 sampai 14 V |
| `[DOOR LOCK] 2D-7 (LSWD) - Body ground` | Warna Kabel: L-R - Body ground — Sinyal input pada Door lock position switch | Driver side door dibuka pengunciannya: Dibawah 1 V / Driver side door dikunci: 11 sampai 14 V |
| `[DOOR LOCK] 2E-3 (PCTY) - Body ground` | Warna Kabel: P - Body ground — Sinyal input pada semua courtesy light switch | Satu atau lebih pintu terbuka: Dibawah 1 V / Semua pintu ditutup: 11 sampai 14 V |
| `[DOOR LOCK] 2K-10 (ACT-) - Body ground` | Warna Kabel: L-Y - Body ground — Sinyal output penggerak unlock pada door lock motor (pintu penumpang dan pintu belakang LH) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] 2K-11 (ACT+) - Body ground` | Warna Kabel: L - Body ground — Sinyal output pengerak lock pada door lock motor (pintu penumpang dan pintu belakang LH) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Power window regulator master switch assembly (door control switch) a |
| `[DOOR LOCK] 2N-12 (ILE) - Body ground` | Warna Kabel: P - Body ground — Sinyal ignition key cylinder light | Ignition key cylinder light kondisi menyala: Dibawah 1 V / Ignition key cylinder light kondisi padam: 11 sampai 14 V |
| `[DOOR LOCK] 2O-25 (HAZ) - Body ground` | Warna Kabel: G-O - Body ground — Output pada hazard warning light | Hazard warning signal switch OFF: 11 sampai 14 V / Hazard warning signal switch ON: Dibawah 1 V |
| `[DOOR LOCK] 2O-27 (DCTY) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal input front door courtesy light switch assembly RH | Driver side door terbuka: Dibawah 1 V / Driver side door ditutup: 11 sampai 14 V |
| `[DOOR LOCK] 2R-27 (ACT-) - Body ground` | Warna Kabel: L-Y - Body ground — Sinyal output penggerak unlock pada door lock motor (pintu pengemudi dan pintu belakang RH) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] 2R-28 (ACT+) - Body ground` | Warna Kabel: L - Body ground — Output penggerak lock pada motor door lock (pintu sisi pengemudi) | Power window regulator master switch assembly (door control switch) tidak ditekan dan driver side door key cylinder dalam posisi netral: Dibawah 1 V / Sisi lock dari power window regulator master switch assembly (door co |
| `[DOOR LOCK] G19-1 (B) - Body ground` | Warna Kabel: R - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] G19-21 (IG+) - Body ground` | Warna Kabel: B-O - Body ground — Sinyal input IG2 | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V |
| `[DOOR LOCK] G19-22 (EP) - Body ground` | Warna Kabel: Y - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[DOOR LOCK] G19-10 (KSW) - Body ground` | Warna Kabel: G-Y - Body ground — Sinyal input unlock warning switch | Tidak terdapat kunci dalam ignition key cylinder: Dibawah 1 V / Ignition switch OFF, kunci di dalam ignition key cylinder: 11 sampai 14 V |
| `[DOOR LOCK] G19-16 (DCTY) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal input driver side door | Driver side door ditutup: Dibawah 1 V / Driver side door terbuka: 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G28-7 (AGND) - Body ground` | Warna Kabel: - — L-O - Body ground | Ground: Selalu |
| `[THEFT DETERRENT / KEYLESS ENTRY] G28-1 (VC5) - G28-7 (AGND)` | Warna Kabel: Input — L - L-O | Transponder key amplifier power supply: Tidak terdapat kunci dalam ignition key cylinder / Transponder key amplifier power supply: Kunci dimasukkan ke dalam ignition key cylinder |
| `[THEFT DETERRENT / KEYLESS ENTRY] G28-4 (CODE) - G28-7 (AGND)` | Warna Kabel: Output — L-Y - L-O | Sinyal demodulasi dari data kode kunci: Tidak terdapat kunci dalam ignition key cylinder / Sinyal demodulasi dari data kode kunci: Kunci dimasukkan ke dalam ignition key cylinder |
| `[THEFT DETERRENT / KEYLESS ENTRY] G28-5 (TXCT) - G28-7 (AGND)` | Warna Kabel: Input — L-B - L-O | Sinyal output kode kunci: Tidak terdapat kunci dalam ignition key cylinder / Sinyal output kode kunci: Kunci dimasukkan ke dalam ignition key cylinder |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-16 (GND) - Body ground` | Warna Kabel: - — G - Body ground | Ground: Selalu |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-1 (+B) - G26-16 (GND)` | Warna Kabel: Input — L-Y - G | Baterai: Selalu |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-2 (IG) - G26-16 (GND)` | Warna Kabel: Input — B-O - G | Ignition switch: Ignition switch off / Ignition switch: Ignition switch ON |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-3 (KSW) - G26-16 (GND)` | Warna Kabel: Input — BR - G | Unlock warning switch: Tidak terdapat kunci dalam ignition key cylinder / Unlock warning switch: Kunci dimasukkan ke dalam ignition key cylinder |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-14 (VC5) - G26-16 (GND)` | Warna Kabel: Input — L - G | Transponder key amplifier power supply: Tidak terdapat kunci dalam ignition key cylinder / Transponder key amplifier power supply: Kunci dimasukkan ke dalam ignition key cylinder |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-4 (TXCT) - G26-16 (GND)` | Warna Kabel: Input — L-B - G | Sinyal output kode kunci: Tidak terdapat kunci dalam ignition key cylinder / Sinyal output kode kunci: Kunci dimasukkan ke dalam ignition key cylinder |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-15 (CODE) - G26-16 (GND)` | Warna Kabel: Output — L-Y - G | Sinyal demodulasi dari data kode kunci: Tidak terdapat kunci dalam ignition key cylinder / Sinyal demodulasi dari data kode kunci: Kunci dimasukkan ke dalam ignition key cylinder |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-7 (CTY) - G26-16 (GND)` | Warna Kabel: Input — R-B - G | Front door courtesy light switch (untu Sisi Pengemudi): Pintu pengemudi ditutup / Front door courtesy light switch (untu Sisi Pengemudi): Pintu pengemudi terbuka |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-13 (EFIO) - G26-16 (GND)` | Warna Kabel: Input — Y-G - G | Sinyal output ECM: Ignition switch off / Sinyal output ECM: Ignition switch ON |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-12 (EFII) - G26-16 (GND)` | Warna Kabel: Output — Y-B - G | Sinyal input ECM: Dalam waktu 3 detik setelah starter dioperasikan terjadi initial combustion, atau dalam waktu 3 detik setelah memutar ignition switch pertama kali ke ON setelah baterai dilepas dan dihubungkan kembali. |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-8 (IND) - G26-16 (GND)` | Warna Kabel: Output — G-R - G | Sinyal security indicator light: Immobiliser set / Sinyal security indicator light: Immobiliser unset |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-9 (D) - G26-16 (GND)` | Warna Kabel: Input/Output — B - G | Komunikasi diagnosis tester: Selalu |
| `[THEFT DETERRENT / KEYLESS ENTRY] G26-5 (AGND) - Body ground` | Warna Kabel: - — L-O - Body ground | Transponder key amplifier ground: Selalu |
| `[THEFT DETERRENT / KEYLESS ENTRY] G88-15 (IMO) - Body ground` | Warna Kabel: Y-B - Body ground — Sinyal output transponder key ECU assembly | Dalam waktu 3 detik setelah starter dioperasikan terjadi initial combustion, atau dalam waktu 3 detik setelah memutar ignition switch pertama kali ke ON setelah baterai dilepas dan dihubungkan.: Pulse generation (Lihat b |
| `[THEFT DETERRENT / KEYLESS ENTRY] G88-16 (IMI) - Body ground` | Warna Kabel: Y-G -Body ground — Sinyal input transponder key ECU assembly | Ignition switch off: Dibawah 1 V / Ignition switch ON: Pulse generation (Lihat bentuk gemombang 2) |
| `[THEFT DETERRENT / KEYLESS ENTRY] G38-29 (IMO) - Body ground` | Warna Kabel: Y-B - Body ground — Sinyal output transponder key ECU assembly | Dalam waktu 3 detik setelah starter dioperasikan terjadi initial combustion, atau dalam waktu 3 detik setelah memutar ignition switch pertama kali ke ON setelah baterai dilepas dan dihubungkan.: Pulse generation (Lihat b |
| `[THEFT DETERRENT / KEYLESS ENTRY] G38-30 (IMI) - Body ground` | Warna Kabel: Y-G -Body ground — Sinyal input transponder key ECU assembly | Ignition switch off: Dibawah 1 V / Ignition switch ON: Pulse generation (Lihat bentuk gemombang 2) |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-1 (E) - Body ground` | Warna Kabel: B-W - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-4 (+B1) - G29-1 (E)` | Warna Kabel: L-Y - B-W — Baterai power supply (power supply untuk ECU) | Selalu: 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-14 (+B2) - G29-1 (E)` | Warna Kabel: G - B-W — Baterai power supply (untuk pengoperasian actuator) | Selalu: 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-18 (IG) - G29-1 (E)` | Warna Kabel: R-L - B-W — Ignition power supply | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-5 (KSW) - Body ground` | Warna Kabel: G-Y - Body ground — Sinyal input unlock warning switch signal | Tidak terdapat kunci dalam ignition key cylinder: 10 kΩ atau lebih tinggi / Kunci dimasukkan ke dalam ignition key cylinder: Dibawah 1 Ω |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-7 (CTY) - G29-1 (E)` | Warna Kabel: R-L - B-W — Sinyal input pada semua courtesy light switch | Satu atau lebih pintu terbuka: Dibawah 1 V / Semua pintu ditutup: 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-9 (DSWH) - G29-1 (E)` | Warna Kabel: G-R - B-W — Input sinyal hood lock assembly (security courtesy switch) | Engine hood ditutup rapat: Dibawah 1 Ω / Kap mesin terbuka: 10 kΩ atau lebih tinggi |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-11 (HORN) - G29-1 (E)` | Warna Kabel: W-R - B-W — Sinyal output horn kendaraan | Status membunyikan alarm: Dibawah 1 V / Status siaga: 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-12 (SRLY) - G29-1 (E)*` | Warna Kabel: W-B - B-W — Sinyal output pemotong starter | Status siaga: 11 sampai 14 V / Status membunyikan alarm: Dibawah 1 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-13 (SH-) - G29-1 (E)` | Warna Kabel: B - B-W — Sinyal output security horn | Security horn assembly berbunyi (sistem anti pencurian dalam status membunyikan alarm): Alternator antara dibawah 1 V dan 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-27 (IND) - G29-1 (E)` | Warna Kabel: G-R - B-W — Sinyal output security indicator light assembly | Security indicator light berkedip (sistem anti pencurian dioperasikan): Alternator antara dibawah 1 V dan 11 sampai 14 V |
| `[THEFT DETERRENT / KEYLESS ENTRY] G29-28 (HAZD) - G29-1 (E)` | Warna Kabel: G-O - B-W — Semua sinyal output hazard warning light | Hazard warning light berkedip (sistem anti pencurian dalam status membunyikan alarm): Dibawah 1 V |
| `[PENERANGAN (INT)] 2H-4 (ALTB) - Body ground` | Warna Kabel: LG - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2L-12 (BECU) - Body ground` | Warna Kabel: L - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2D-9 (GND) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[PENERANGAN (INT)] 2D-18 (GND) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[PENERANGAN (INT)] 2D-7 (LSWD) - Body ground` | Warna Kabel: L-R - Body ground — Sinyal front door unlock detection switch | Pintu sisi pengemudi posisi unlock: Dibawah 1 V / Pintu sisi pengemudi lock: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2O-27 (DCTY) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal Driver side door courtesy light switch | Driver side door terbuka: Dibawah 1 V / Pintu sisi pengemudi tertutup: 11 sampai 14 V |
| `[PENERANGAN (INT)] 2N-12 (ILE) - Body ground` | Warna Kabel: P - Body ground — Sinyal ignition key cylinder light | Ignition key cylinder light kondisi menyala: Dibawah 1 V / Ignition key cylinder light kondisi padam: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-4 (+B1) - Body ground` | Warna Kabel: L-Y - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-14 (+B2) - Body ground` | Warna Kabel: LG - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-18 (IG) - Body ground` | Warna Kabel: R-L - Body ground — Ignition power supply | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V |
| `[PENERANGAN (INT)] G29-1 (E) - Body ground` | Warna Kabel: B-W - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[PENERANGAN (INT)] G29-3 (DMLP) - Body ground` | Warna Kabel: P - Body ground — Sinyal interior light | Interior light menyala: Dibawah 1 V / Interior light padam: 11 sampai 14 V |
| `[PENERANGAN (INT)] G29-7 (CTY) - Body ground` | Warna Kabel: R-L - Body ground — Sinyal semua courtesy switch | Driver side, front passenger side, rear RH, rear LH atau back door ditutup: 11 sampai 14 V / Driver side, front passenger side, rear RH, rear LH atau back door dibuka: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-1 (B) - Body ground` | Warna Kabel: R - Body ground — Baterai | Selalu: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-9 (TR) - Body ground` | Warna Kabel: W-B - Body ground — Sinyal pengapian | Rheostat knob diputar sepenuhnya ke kiri: 702 Ω / Rheostat knob diputar sepenuhnya ke kanan: Dibawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-21 (IG+) - Body ground` | Warna Kabel: B-O - Body ground — Sinyal IG2 | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-22 (EP) - Body ground` | Warna Kabel: Y - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-26 (PKBI) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G19-5 (SI) - Body ground` | Warna Kabel: P-L - Body ground — Sinyal kecepatan kendaraan (input) | Kendarai sekitar 20 km/jam (12 mph): Pulse generation (Lihat bentuk gemombang 1) |
| `[METER / GAUGE / DISPLAY] G19-6 (+S) - Body ground` | Warna Kabel: V-R - Body ground — Sinyal kecepatan kendaraan (output) | Kendarai sekitar 20 km/jam (12 mph): Pulse generation (Lihat bentuk gemombang 1) |
| `[METER / GAUGE / DISPLAY] G19-7 (S) - Body ground` | Warna Kabel: B-W - Body ground — Sinyal Tachometer | Mesin idle: Pulse generation (Lihat bentuk gemombang 2) |
| `[METER / GAUGE / DISPLAY] G19-8 (ILL+) - Body ground` | Warna Kabel: G - Body ground — Sinyal light control switch | Light control switch posisi off: Dibawah 1 V / Switch kontrol lampu TAIL atau HEAD: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-10 (KSW) - Body ground` | Warna Kabel: G-Y - Body ground — Sinyal unlock warning switch | Tidak terdapat kunci dalam ignition key cylinder: Dibawah 1 V / Ignition switch OFF, kunci di dalam ignition key cylinder: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-11 (BKL) - Body ground` | Warna Kabel: R-Y - Body ground — Sinyal driver side seat belt warning | Ignition switch ON, driver side seat belt tidak dikenakan: Dibawah 1 V / Ignition switch ON, driver side seat belt dikenakan: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-12 (P) - Body ground*1` | Warna Kabel: G-B - Body ground — Sinyal posisi shift automatic transmission (P) | Ignition switch ON, automatic transmission P indicator light padam: Dibawah 1 V / Ignition switch ON, automatic transmission P indicator light menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-13 (L) - Body ground*1, *2` | Warna Kabel: W-G - Body ground — Sinyal A/T P warning light | Ignition switch ON, shift lever pada P, A/T P warning light menyala: Dibawah 1 V / Ignition switch ON, shift lever pada P, A/T P warning light padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-14 (FFTR) - Body ground*3` | Warna Kabel: W-G - Body ground — Sinyal FUEL FILTER warning light | Ignition switch ON, FUEL FILTER warning light menyala: Dibawah 1 V / Ignition switch ON, FUEL FILTER warning light padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-15 (CTYD) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal driver side door (output) | Driver side door ditutup: 11 sampai 14 V / Driver side door terbuka: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-16 (DCTY) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal driver side door (input) | Driver side door ditutup: 11 sampai 14 V / Driver side door terbuka: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-17 (DOOR) - Body ground` | Warna Kabel: R-L - Body ground — Sinyal pintu | Pintu tertutup (Mengabaikan driver side door): 11 sampai 14 V / Pintu terbuka (Mengabaikan driver side door): Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-18 (OILW) - Body ground*1, *2` | Warna Kabel: P - Body ground — Sinyal A/T OIL TEMP warning light | Ignition switch ON, A/T OIL TEMP warning light menyala: Dibawah 1 V / Ignition switch ON, A/T OIL TEMP warning light padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-20 (SW) - Body ground` | Warna Kabel: B-Y - Body ground — Sinyal SRS warning light | Ignition switch ON, SRS warning light padam: Pulse generation (Lihat bentuk gemombang 3) / Ignition switch ON, SRS warning light menyala: Pulse generation (Lihat bentuk gemombang 4) |
| `[METER / GAUGE / DISPLAY] G19-23 (S) - Body ground*3` | Warna Kabel: L-R - Body ground — Sinyal FUEL FILTER warning light (Level warning switch) | Ignition switch ON, FUEL FILTER warning light menyala: Dibawah 1 V / Ignition switch ON, FUEL FILTER warning light padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-24 (B) - Body ground` | Warna Kabel: G-B - Body ground — Sinyal Turn signal indicator LH | Ignition switch ON, turn signal indicator LH light padam: Dibawah 1 V / Ignition switch ON, turn signal indicator LH light menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-25 (B) - Body ground` | Warna Kabel: G-Y - Body ground — Sinyal turn signal indicator RH | Ignition switch ON, turn signal indicator RH light padam: Dibawah 1 V / Ignition switch ON, turn signal indicator RH light menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-31 (MS5) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal IG (untuk Speedometer sensor) | Ignition switch ON: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G19-35 (S) - Body ground` | Warna Kabel: LG-B - Body ground — Sinyal OIL PRESSURE warning light | Ignition switch ON, OIL PRESSURE warning light padam: 11 sampai 14 V / Ignition switch ON, OIL PRESSURE warning light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-36 (SW) - Body ground` | Warna Kabel: LG - Body ground — Sinyal BRAKE warning light | Ignition switch ON, BRAKE warning light padam: 11 sampai 14 V / Ignition switch ON, BRAKE warning light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-37 (CHG-) - Body ground` | Warna Kabel: GR - Body ground — Sinyal CHARGE warning light | Ignition switch ON, CHARGE warning light padam: 11 sampai 14 V / Ignition switch ON, CHARGE warning light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-38 (LP) - Body ground` | Warna Kabel: R-G - Body ground — Sinyal ABS warning light | Ignition switch ON, ABS warning light padam: 11 sampai 14 V / Ignition switch ON, ABS warning light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-39 (CHK) - Body ground` | Warna Kabel: R-B - Body ground — Sinyal MIL | Ignition switch ON, MIL padam: 11 sampai 14 V / Ignition switch ON, MIL menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G19-40 (GLW-) - Body ground*3` | Warna Kabel: Y-R - Body ground — Sinyal GLOW indicator light | Ignition switch ON, GLOW indicator light padam: 11 sampai 14 V / Ignition switch ON, GLOW indicator light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-2 (2) - Body ground*1` | Warna Kabel: G-R - Body ground — Sinyal posisi shift automatic transmission (L) | Ignition switch ON, automatic transmission L indicator light menyala: 11 sampai 14 V / Ignition switch ON, automatic transmission L indicator light padam: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-3 (3) - Body ground*1` | Warna Kabel: L - Body ground — Sinyal posisi shift automatic transmission (2) | Ignition switch ON, automatic transmission 2 indicator light menyala: 11 sampai 14 V / Ignition switch ON, automatic transmission 2 indicator light padam: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-4 (4) - Body ground*1` | Warna Kabel: G-O - Body ground — Sinyal posisi shift automatic transmission (3) | Ignition switch ON, automatic transmission 3 indicator light menyala: 11 sampai 14 V / Ignition switch ON, automatic transmission 3 indicator light padam: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-5 (D) - Body ground*1` | Warna Kabel: B-R - Body ground — Sinyal posisi shift automatic transmission (D) | Ignition switch ON, automatic transmission D indicator light menyala: 11 sampai 14 V / Ignition switch ON, automatic transmission D indicator light padam: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-6 (N) - Body ground*1` | Warna Kabel: R-W - Body ground — Sinyal posisi shift automatic transmission (N) | Ignition switch ON, automatic transmission N indicator light menyala: 11 sampai 14 V / Ignition switch ON, automatic transmission N indicator light padam: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-7 (R) - Body ground*1` | Warna Kabel: R-Y - Body ground — Sinyal posisi shift automatic transmission (R) | Ignition switch ON, automatic transmission R indicator light menyala: 11 sampai 14 V / Ignition switch ON, automatic transmission R indicator light padam: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-11 (-) - Body ground*7` | Warna Kabel: R-Y - Body ground*9 — Sinyal high beam indicator light | Ignition switch ON, HI BEAM indicator light padam: 11 sampai 14 V / Ignition switch ON, HI BEAM indicator light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-11 (-) - Body ground*7` | Warna Kabel: B-O - Body ground*5 — Sinyal high beam indicator light | Ignition switch ON, HI BEAM indicator light padam: 11 sampai 14 V / Ignition switch ON, HI BEAM indicator light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-11 (-) - Body ground*8` | Warna Kabel: R-Y - Body ground — Sinyal high beam indicator light | Ignition switch ON, HI BEAM indicator light padam: Dibawah 1 V / Ignition switch ON, HI BEAM indicator light menyala: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G20-15 (FOG) - Body ground` | Warna Kabel: G-B - Body ground — Sinyal front fog indicator light | Light control switch TAIL atau HEAD, fog light switch padam: 11 sampai 14 V / Light control switch TAIL atau HEAD, fog light switch menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-19 (TAUB) - Body ground*4` | Warna Kabel: B-R - Body ground — Sinyal untuk jumlah dari konsumsi bahan bakar | Mesin idle: Pembangkitan pulsa |
| `[METER / GAUGE / DISPLAY] G20-20 (TAU) - Body ground*4` | Warna Kabel: L - Body ground — Sinyal untuk jumlah dari konsumsi bahan bakar | Mesin idle: Pembangkitan pulsa |
| `[METER / GAUGE / DISPLAY] G20-22 (LVWG) - Body ground*5` | Warna Kabel: B-L - Body ground — Sinyal headlight leveling indicator light | Ignition switch ON, headlight leveling indicator light padam: 11 sampai 14 V / Ignition switch ON, headlight leveling indicator light padam: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G20-25 (SW) - Body ground*6` | Warna Kabel: R-B - Body ground — Sinyal center differential lock indicator light | Ignition switch ON, center differential lock indicator light padam: 11 sampai 14 V / Ignition switch ON, center differential lock indicator light menyala: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G32-1 (GND1) - Body ground` | Warna Kabel: LG - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G32-10 (SGND) - Body ground` | Warna Kabel: BR - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[METER / GAUGE / DISPLAY] G32-12 (IG) - Body ground` | Warna Kabel: R-L - Body ground — Sinyal IG | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G32-13 (ACC) - Body ground` | Warna Kabel: G-R - Body ground — Sinyal ACC | Ignition switch ACC atau ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V |
| `[METER / GAUGE / DISPLAY] G32-14 (+B) - Body ground` | Warna Kabel: R - Body ground — Baterai | Selalu: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G32-2 (SG) - G32-3 (TH+)` | Warna Kabel: BR-Y - W-G — Sinyal air conditioning ambient temperature sensor | Ignition switch ON, temperatur sekitar 25°C (77°F): 1.35 sampai 1.75 V / Ignition switch ON, temperatur sekitar 40°C (104°F): 0.85 sampai 2.34 V |
| `[METER / GAUGE / DISPLAY] G32-8 (PBEW) - Body ground` | Warna Kabel: G-W - Body ground — Sinyal front passenger side seat belt warning light | Ignition switch ON, front passenger side seat belt warning light menyala: Dibawah 1 V / Ignition switch ON, front passenger side seat belt warning light padam: 11 sampai 14 V |
| `[METER / GAUGE / DISPLAY] G32-11 (SW+) - Body ground` | Warna Kabel: B - Body ground — Sinyal switch steering pad | Ignition switch ON, steering pad switch tidak ditekan: 4 V atau lebih / Ignition switch ON, INFO switch ditekan: Dibawah 1 V / Ignition switch ON, MODE RESET switch ditekan: 2 sampai 3 V |
| `[HEATING / AIR CONDITIONING] G94-1 (GND) - Body ground` | Warna Kabel: L - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G94-5 (+B1) - G94-1 (GND)` | Warna Kabel: L-Y - L — Power source | Selalu: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-6 (IG+) - G94-1 (GND)` | Warna Kabel: R-L - L — Power source | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-13 (MGC) - Body ground` | Warna Kabel: B - Body ground — Sinyal magnet clutch | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V / Mesin idle Switch A/C ON: Dibawah 1 V / Mesin idle Switch A/C OFF: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-14 (HR) - Body ground` | Warna Kabel: L-W - Body ground — Sinyal HTR relay | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V |
| `[HEATING / AIR CONDITIONING] G94-2 (BLW) - Body ground` | Warna Kabel: L-B - Body ground — Voltase putaran blower motor control | Ignition switch ON Blower switch ON (Level LO): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[HEATING / AIR CONDITIONING] G94-3 (AOF) - G94-1 (GND)` | Warna Kabel: Y-B - L — Voltase pengoperasian mode damper servo | Ignition switch ON Mode switch DEF: Dibawah 1 V / Ignition switch ON Mode switch FACE: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-4 (AOD) - G94-1 (GND)` | Warna Kabel: R-B - L — Voltase pengoperasian mode damper servo | Ignition switch ON Mode switch FACE: Dibawah 1 V / Ignition switch ON Mode switch DEF: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-7 (ACT) - G94-1 (GND)` | Warna Kabel: R-L - L — Magnet clutch dari sinyal permit input | Mesin idle Blower switch ON (Level LO) Switch A/C OFF: Dibawah 1 V / Mesin idle Blower switch ON (Level LO) Switch A/C ON: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-8 (TW) - G94-1 (GND)` | Warna Kabel: P - L — Siyal engine coolant temperature sensor | Ignition switch ON: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G94-9 (SPD) - Body ground` | Warna Kabel: V-W - Body ground — Sinyal kecepatan kendaraan | Pengendaraan sekitar 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[HEATING / AIR CONDITIONING] G94-17 (AMH) - G94-1 (GND)` | Warna Kabel: L - L — SInyal pengoperasian air mix damper servo | Ignition switch ON Temperature switch MAX HOT: 11 sampai 14 V / Ignition switch ON Temperature switch MAX COLD: Dibawah 1 V |
| `[HEATING / AIR CONDITIONING] G94-18 (TAMO) - G94-1 (GND)` | Warna Kabel: P - L — Sinyal ambient temperature | Ignition switch ON: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G94-19 (AMC) - G94-1 (GND)` | Warna Kabel: R-W - L — SInyal pengoperasian air mix damper servo | Ignition switch ON Temperature switch MAX HOT: Dibawah 1 V / Ignition switch ON Temperature switch MAX COLD: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-21 (AC1) - G94-1 (GND)` | Warna Kabel: Y - L — Sinyal pemesan idle-up | Mesin idle Blower switch ON (Level LO) Switch A/C OFF atau ON (magnet clutch OFF): 11 sampai 14 V / Mesin idle Blower switch ON (Level LO) Switch A/C ON (magnet clutch ON): Dibawah 1 V |
| `[HEATING / AIR CONDITIONING] G94-22 (AIR) - G94-1 (GND)` | Warna Kabel: L-W - L — Voltase pengoperasian recirculation damper servo | Ignition switch ON Switch fresh on: Dibawah 1 V / Ignition switch ON Recirculation switch ON: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G94-23 (AIF) - G94-1 (GND)` | Warna Kabel: G-Y - L — Voltase pengoperasian recirculation damper servo | Ignition switch ON Recirculation switch ON: Dibawah 1 V / Ignition switch ON Switch fresh on: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G95-1 (TE) - G95-14 (SG-4)` | Warna Kabel: G - P — Sinyal cooler thermistor No. 1 | Ignition switch ON Evaporator temperature 0°C (32°F): 2 sampai 2.4 V / Ignition switch ON Evaporator temperature 15°C (59°F): 1.4 sampai 1.8 V |
| `[HEATING / AIR CONDITIONING] G95-2 (S5-3) - G94-1 (GND)` | Warna Kabel: W-R - L — Power supply untuk solar sensor | Ignition switch ON: 4.5 sampai 5.5 V |
| `[HEATING / AIR CONDITIONING] G95-5 (PSW) - G94-1 (GND)` | Warna Kabel: Y-B - L — Sinyal air conditioner pressure sensor | Mesin idle Refrigerant pressure normal: Dibawah 1 V / Mesin idle Tekanan refrigerant kurang dari 0.196 MPa (2.0 kgf/cm 2 , 28 psi) atau lebih dari 3.14 MPa (32.0 kgf/cm 2 , 455 psi): 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G95-7 (TS) - G95-2 (S5-3)` | Warna Kabel: L-W - W-R — Sinyal solar sensor | Ignition switch ON Solar sensor ditujukan untuk electric light Vehicle indoor: 0.8 sampai 4.3 V / Ignition switch ON Menutupi solar sensor dengan kain Vehicle indoor: Dibawah 0.8 V |
| `[HEATING / AIR CONDITIONING] G95-9 (VER) - Body ground` | Warna Kabel: R - Body ground — Sinyal informasi lokasi steering wheel | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G95-11 (SG-2) - Body ground` | Warna Kabel: L-Y - Body ground — Ground untuk pulse position sensor (Mode damper servo) | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G95-13 (SG-3) - Body ground` | Warna Kabel: BR-Y - Body ground — Ground untuk cooler thermistor | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G95-14 (SG-4) - Body ground` | Warna Kabel: P - Body ground — Ground untuk cooler thermistor No. 1 | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G95-16 (AGND) - G95-21 (AUXO)` | Warna Kabel: R-L - LG-R — Sinyal input untuk pulse position sensor (recirculation damper servo) | Ignition switch ON Air inlet control recirculation untuk fresh atau vice versa: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G95-17 (PIA) - G95-21 (AUXO)` | Warna Kabel: P-B - LG-R — Sinyal input untuk pulse position sensor (recirculation damper servo) | Ignition switch ON Air inlet control recirculation untuk fresh atau vice versa: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G95-18 (TR) - G95-13 (SG-3)` | Warna Kabel: GR - BR-Y — Sinyal cooler thermistor | Ignition switch ON Temperatur kabin 25°C (77°F): 1.8 sampai 2.2 V / Ignition switch ON Temperatur kabin 40°C (104°F): 1.2 sampai 1.6 V |
| `[HEATING / AIR CONDITIONING] G95-20 (SG-1) - Body ground` | Warna Kabel: BR-Y - Body ground — Ground untuk pulse position sensor (air mix damper servo) | Selalu: Dibawah 1 V |
| `[HEATING / AIR CONDITIONING] G95-21 (AUXO) - Body ground` | Warna Kabel: LG-R - Body ground — Ground untuk pulse position sensor (recirculation damper servo) | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G95-23 (PMB) - G95-20 (SG-1)` | Warna Kabel: W-L - BR-Y — Sinyal input untuk pulse position sensor (air mix damper servo) | Ignition switch ON Temperature switch MAX HOT sampai MAX COLD: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G95-24 (PMA) - G95-20 (SG-1)` | Warna Kabel: W-R - BR-Y — Sinyal input untuk pulse position sensor (air mix damper servo) | Ignition switch ON Temperature switch MAX COLD sampai MAX HOT: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G95-25 (POB) - G95-11(SG-2 )` | Warna Kabel: LG - L-Y — Sinyal input untuk pulse position sensor (mode damper servo) | Ignition switch ON Mode control FACE untuk DEF atau vice versa: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G95-26 (POA) - G95-11 (SG-2)` | Warna Kabel: L-O - L-Y — Sinyal input untuk pulse position sensor (mode damper servo) | Ignition switch ON Mode control FACE untuk DEF atau vice versa: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G39-2 (THWO) - C23-7 (E1)` | Warna Kabel: P - BR — Sinyal output temperatur engine coolant | Mesin idle: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G38-19 (ACT) - C23-7 (E1)` | Warna Kabel: R-L - BR — Magnet clutch dari sinyal permit output | Mesin idle Blower switch ON (Level LO) Switch A/C OFF: Dibawah 1 V / Mesin idle Blower switch ON (Level LO) Switch A/C ON: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] C22-19 (THW) - C22-28 (E2)` | Warna Kabel: R-L - BR — Siyal engine coolant temperature sensor | Mesin idle Temperatur engine coolant 20°C (68°F): 0.2 sampai 1.0 V |
| `[HEATING / AIR CONDITIONING] G32-3 (TH+) - G32-2 (SG)` | Warna Kabel: W-G - BR-Y — Sinyal ambient temperature sensor | Ignition switch ON Ambient temperature 20 sampai 30°C (68 sampai 86°F): 1 sampai 1.6 V / Ignition switch ON Ambient temperature 30 sampai 50°C (86 sampai 122°F): 0.6 sampai 1 V |
| `[HEATING / AIR CONDITIONING] G32-9 (DATA) - G32-1 (GND1)` | Warna Kabel: P - LG — Sinyal ambient temperature sensor | Ignition switch ON: Pembangkitan pulsa |
| `[HEATING / AIR CONDITIONING] G19-6 (+S) - G19-22 (EP)` | Warna Kabel: V-R - Y — Sinyal kecepatan kendaraan | Pengendaraan sekitar 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang) |
| `[HEATING / AIR CONDITIONING] G34-10 (IG+) - G34-18 (GND)` | Warna Kabel: R-L - L — Ignition power supply | Ignition switch ON: 11 sampai 14 V / Ignition switch off: Dibawah 1 V |
| `[HEATING / AIR CONDITIONING] G34-18 (GND) - Body ground` | Warna Kabel: L - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G34-2 (ACT) - G34-18 (GND)` | Warna Kabel: R-L - L — Magnet clutch pada permit signal | Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch ON: 5 sampai 6 V / Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch OFF: Dibawah 1 V |
| `[HEATING / AIR CONDITIONING] G34-8 (SG-1) - Body ground` | Warna Kabel: P - Body ground — Ground untuk cooler thermistor No. 1 | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G34-13 (IND-) - G34-18 (GND)` | Warna Kabel: R-L - L — Sinyal cooler switch indicator | Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch mati atau cooler switch hidup.: 11 sampai 14 V / Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch ON: Dibawah 1 V |
| `[HEATING / AIR CONDITIONING] G88-24 (AC1) - C75-3 (E1)` | Warna Kabel: Y - BR — Sinyal pemesan idle-up | Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch ON (magnet clutch ON): Dibawah 1 V / Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch mati atau cooler switch hidup (magnet clutch  |
| `[HEATING / AIR CONDITIONING] G88-25 (ACT) - C75-3 (E1)` | Warna Kabel: R-L - BR — Magnet clutch dari sinyal permit output | Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch OFF: Dibawah 1 V / Mesin idle Blower switch di-set ke 1 atau lebih tinggi Cooler switch ON: 11 sampai 14 V |
| `[HEATING / AIR CONDITIONING] G95-9 (VER) - Body ground*` | Warna Kabel: R - Body ground — Sinyal informasi lokasi steering wheel | Selalu: Dibawah 1 Ω |
| `[HEATING / AIR CONDITIONING] G32-3 (TH+) - G32-2 (SG)` | Warna Kabel: W-G - BR-Y — Sinyal thermistor assembly | Ignition switch ON Ambient temperature 20 sampai 30°C (68 sampai 86°F): 1 sampai 1.6 V / Ignition switch ON Ambient temperature 30 sampai 50°C (86 sampai 122°F): 0.6 sampai 1 V |
| `[HEATING / AIR CONDITIONING] G32-9 (DATA) - G32-1 (GND1)` | Warna Kabel: P - LG — Sinyal ambient temperature | Ignition switch ON: Pembangkitan pulsa |
| `[WINDOW / GLASS] I5-6 (B) - Body ground` | Warna Kabel: L - Body ground — Ignition power supply | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[WINDOW / GLASS] I5-7 (BW) - Body ground` | Warna Kabel: L-B - Body ground — Power suplay untuk regulator motor | Selalu: 11 sampai 14 V |
| `[WINDOW / GLASS] I5-1 (E) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[WINDOW / GLASS] I5-2 (GND) - Body ground` | Warna Kabel: L-O - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[WINDOW / GLASS] H8-6 (B) - Body ground` | Warna Kabel: L - Body ground — Ignition power supply | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[WINDOW / GLASS] H8-7 (BW) - Body ground` | Warna Kabel: L-B - Body ground — Power suplay untuk regulator motor | Selalu: 11 sampai 14 V |
| `[WINDOW / GLASS] H8-1 (E) - Body ground` | Warna Kabel: W-B - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[WINDOW / GLASS] H8-2 (GND) - Body ground` | Warna Kabel: L-O - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[WINDOW / GLASS] I5-4 (U) - I5-1 (E)` | Warna Kabel: R - W-B — Output naik dari front power window regulator motor assembly LH | Ignition switch ON, driver side power window switch OFF → UP (pengoperasian manual): Dibawah 1 V → 11 sampai 14 V / Ignition switch ON, driver side power window terbuka sepenuhnya → driver side power window switch UP (pe |
| `[WINDOW / GLASS] I5-9 (D) - I5-1 (E)` | Warna Kabel: L-R - W-B — Output turun dari front power window regulator motor assembly LH | Ignition switch ON, driver side power window switch OFF → DOWN (pengoperasian manual): Dibawah 1 V → 11 sampai 14 V / Ignition switch ON, driver side power window tertutup sepenuhnya → driver side power window switch DOW |
| `[WINDOW / GLASS] I5-13 (U) - I5-1 (E)` | Warna Kabel: R-L - W-B — Output naik dari front power window regulator motor assembly RH | Window lock switch OFF Ignition switch ON, front passenger side power window remote manual switch OFF → UP: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] I5-15 (D) - I5-1 (E)` | Warna Kabel: G-W - W-B — Output turun dari front power window regulator motor assembly RH | Window lock switch OFF Ignition switch ON, front passenger side power window remote manual switch OFF → DOWN: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] I5-12 (U) - I5-1 (E)` | Warna Kabel: R-Y - W-B — Output naik dari rear power window regulator motor assembly LH | Window lock switch OFF Ignition switch ON, rear power window LH remote manual switch OFF→ UP: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] I5-10 (D) - I5-1 (E)` | Warna Kabel: G-Y - W-B — Output turun dari rear power window regulator motor assembly LH | Window lock switch OFF Ignition switch ON, rear power window LH remote manual switch OFF→ DOWN: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] I5-18 (U) - I5-1 (E)` | Warna Kabel: R-B - W-B — Output naik dari rear power window regulator motor assembly RH | Window lock switch OFF Ignition switch ON, rear power window RH remote manual switch OFF→ UP: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] I5-16 (D) - I5-1 (E)` | Warna Kabel: G-B - W-B — Output turun dari rear power window regulator motor assembly RH | Window lock switch OFF Ignition switch ON, rear power window RH remote manual switch OFF→ DOWN: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] I5-3 (VCC) - I5-2 (GND)` | Warna Kabel: BR - L-O — Power source untuk power window regulator motor sensor | Ignition switch ON, driver side power window switch off → up atau down: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] I5-14 (PLS) - Body ground` | Warna Kabel: P-G - Body ground — Output naik atau turun dari front power window regulator motor assembly LH | Ignition switch ON, driver side power window switch off → up atau down: Bentuk gelombang pulsa di-output |
| `[WINDOW / GLASS] I5-17 (PLS2) - Body ground` | Warna Kabel: B - Body ground — Output naik atau turun dari front power window regulator motor assembly LH | Ignition switch ON, driver side power window switch off → up atau down: Bentuk gelombang pulsa di-output |
| `[WINDOW / GLASS] H8-4 (U) - H8-1 (E)` | Warna Kabel: B - W-B — Output naik dari front power window regulator motor assembly RH | Ignition switch ON, driver side power window switch OFF → UP (pengoperasian manual): Dibawah 1 V → 11 sampai 14 V / Ignition switch ON, driver side power window terbuka sepenuhnya → driver side power window switch UP (pe |
| `[WINDOW / GLASS] H8-9 (D) - H8-1 (E)` | Warna Kabel: L-R - W-B — Output turun dari front power window regulator motor assembly RH | Ignition switch ON, driver side power window switch OFF → DOWN (pengoperasian manual): Dibawah 1 V → 11 sampai 14 V / Ignition switch ON, driver side power window tertutup sepenuhnya → driver side power window switch DOW |
| `[WINDOW / GLASS] H8-13 (U) - H8-1 (E)` | Warna Kabel: R-L - W-B — Output naik dari front power window regulator motor assembly LH | Window lock switch OFF Ignition switch ON, front passenger side power window remote manual switch OFF → UP: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] H8-15 (D) - H8-1 (E)` | Warna Kabel: G-W - W-B — Output turun dari front power window regulator motor assembly LH | Window lock switch OFF Ignition switch ON, front passenger side power window remote manual switch OFF → DOWN: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] H8-12 (U) - H8-1 (E)` | Warna Kabel: R-Y - W-B — Output naik dari rear power window regulator motor assembly LH | Window lock switch OFF Ignition switch ON, rear power window LH remote manual switch OFF→ UP: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] H8-10 (D) - H8-1 (E)` | Warna Kabel: G-Y - W-B — Output turun dari rear power window regulator motor assembly LH | Window lock switch OFF Ignition switch ON, rear power window LH remote manual switch OFF→ DOWN: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] H8-18 (U) - H8-1 (E)` | Warna Kabel: R-B - W-B — Output naik dari rear power window regulator motor assembly RH | Window lock switch OFF Ignition switch ON, rear power window RH remote manual switch OFF→ UP: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] H8-16 (D) - H8-1 (E)` | Warna Kabel: G-B - W-B — Output turun dari rear power window regulator motor assembly RH | Window lock switch OFF Ignition switch ON, rear power window RH remote manual switch OFF→ DOWN: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] H8-3 (VCC) - H8-2 (GND)` | Warna Kabel: BR - L-O — Power source untuk power window regulator motor sensor | Ignition switch ON, driver side power window switch off → up atau down: Dibawah 1 V → 11 sampai 14 V |
| `[WINDOW / GLASS] H8-14 (PLS) - Body ground` | Warna Kabel: P-G - Body ground — Output naik atau turun dari front power window regulator motor assembly RH | Ignition switch ON, driver side power window switch off → up atau down: Bentuk gelombang pulsa di-output |
| `[WINDOW / GLASS] H8-17 (PLS2) - Body ground` | Warna Kabel: B - Body ground — Output naik atau turun dari front power window regulator motor assembly RH | Ignition switch ON, driver side power window switch off → up atau down: Bentuk gelombang pulsa di-output |
| `[PENERANGAN (EXT)] G100-1 (IG) - Body ground` | Warna Kabel: R-L - Body ground — Ignition power supply | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G100-9 (E1) - Body ground` | Warna Kabel: GR - Body ground — Ground | Selalu: Dibawah 1 Ω |
| `[PENERANGAN (EXT)] G100-3 (B2) - G100-9 (E1)` | Warna Kabel: P- GR — Input sinyal low beam headlight | Low beam headlight on: Dibawah 1 V / Low beam headlight off: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G100-5 (SPDL) - G100-9 (E1)` | Warna Kabel: V- GR — Input sinyal inisialisasi | Terminal LVL dan terminal CG pada DLC3 terhubung: Dibawah 1 V / Terminal LVL dan terminal CG of DLC3 tidak terhubung: 4.5 sampai 5.5 V |
| `[PENERANGAN (EXT)] G100-6 (WNG) - G100-9 (E1)` | Warna Kabel: B-L - GR — Drive output indikaotr peringatan | Warning indicator on: Dibawah 1 V / Warning indicator off: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G100-10 (RH+) - G100-9 (E1)` | Warna Kabel: R - GR — Power supply leveling motor RH | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G100-11 (LH+) - G100-9 (E1)` | Warna Kabel: Y - GR — Power supply leveling motor LH | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G100-12 (SBR) - G100-21 (SGR)` | Warna Kabel: B - G — Power supply sensor kontrol tinggi belakang | Ignition switch off: Dibawah 1 V / Ignition switch ON: 4.75 sampai 5.25 V |
| `[PENERANGAN (EXT)] G100-16 (SPDR) - G100-9 (E1)` | Warna Kabel: L - GR — Input sinyal kecepatan kendaraan | Kendaraan dikemudikan sekitar 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[PENERANGAN (EXT)] G100-17 (RHE) - G100-9 (E1)` | Warna Kabel: LG - GR — Input sinyal kerja leveling motor RH | Dengan low beam headlight ON, tinggi kendaraan tidak berubah: Dibawah 1 V / Dengan low beam headlight ON, ubah tinggi kendaraan dan jaga selama lebih dari 3 detik.: 1.0 sampai 14.4 V |
| `[PENERANGAN (EXT)] G100-18 (LHE) - G100-9 (E1)` | Warna Kabel: W - GR — Input sinyal kerja leveling motor LH | Dengan low beam headlight ON, tinggi kendaraan tidak berubah: Dibawah 1 V / Dengan low beam headlight ON, ubah tinggi kendaraan dan jaga selama lebih dari 3 detik.: 1.0 sampai 14.4 V |
| `[PENERANGAN (EXT)] G100-19 (SHRL) - G100-21 (SGR)` | Warna Kabel: L - G — Input sinyal sensor kontrol tinggi belakang | Ignition switch off: Dibawah 1 V / Ignition switch ON: 0.5 sampai 4.5 V |
| `[PENERANGAN (EXT)] G100-21 (SGR) - G100-9 (E1)` | Warna Kabel: G- GR — Masa sensor kontrol ketinggian belakang | Selalu: Dibawah 1 Ω |
| `[PENERANGAN (EXT)] G100-23 (RH-) - G100-9 (E1)` | Warna Kabel: B-O - GR — Ground leveling motor RH | Selalu: Dibawah 1 Ω |
| `[PENERANGAN (EXT)] G100-24 (LH-) - G100-9 (E1)` | Warna Kabel: GR - GR — Ground leveling motor LH | Selalu: Dibawah 1 Ω |
| `[PENERANGAN (EXT)] G96-1 (IG) - Body ground` | Warna Kabel: R-L - Body ground — Ignition power supply | Ignition switch off: Dibawah 1 V / Ignition switch ON: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G96-2 (B) - Body ground` | Warna Kabel: L-Y - Body ground — Power supply baterai | Selalu: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G96-6 (A) - Body ground` | Warna Kabel: P-L - Body ground — Ground | Headlight dimmer switch dalam posisi AUTO: Dibawah 1 Ω / Headlight dimmer switch tidak dalam posisi AUTO: 10 kΩ atau lebih tinggi |
| `[PENERANGAN (EXT)] G96-3 (CTY) - Body ground` | Warna Kabel: R-B - Body ground — Input sinyal front door courtesy light switch LH | Front door LH dibuka: Dibawah 1 V / Front door LH ditutup: 11 sampai 14 V |
| `[PENERANGAN (EXT)] G96-5 (H) - Body ground` | Warna Kabel: GR - Body ground — Output H-LP relay drive | Ignition switch ON Headlight dimmer switch dalam posisi AUTO Automatic light control sensor tutuplah dengan tangan Low beam headlight menyala: Dibawah 1 V / Ignition switch ON Headlight dimmer switch dalam posisi AUTO Au |
| `[PENERANGAN (EXT)] G96-7 (T) - Body ground` | Warna Kabel: LG-B - Body ground — Output taillight relay drive | Ignition switch ON Headlight dimmer switch dalam posisi AUTO Automatic light control sensor tutuplah dengan tangan Taillight menyala: Dibawah 1 V / Ignition switch ON Headlight dimmer switch dalam posisi AUTO Automatic l |

---

## 3. Katalog Lengkap Prosedur Pemeriksaan Kode DTC (OBD-II & Flash Code)

### DTC `01-21` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] ROM Error (Dokumen: RM00000183S06CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] ROM Error (Dokumen: RM00000183S06EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] ROM Error (Dokumen: RM00000183S0
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terdapat malfungsi dalam ROM.; Kondisi Deteksi: Terdapat malfungsi dalam RAM.; Kondisi Deteksi: Terdapat malfungsi dalam bus.; Kondisi Deteksi: Terdapat malfungsi internal power source.; Kondisi Deteksi: Terdapat malfungsi dalam internal hardware (CPU fan, malfungsi video decoder, GVIF IC, MOST [INIC]).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `01-22` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] RAM Error (Dokumen: RM00000183S06CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] RAM Error (Dokumen: RM00000183S06EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] RAM Error (Dokumen: RM00000183S0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terdapat malfungsi dalam ROM.; Kondisi Deteksi: Terdapat malfungsi dalam RAM.; Kondisi Deteksi: Terdapat malfungsi dalam bus.; Kondisi Deteksi: Terdapat malfungsi internal power source.; Kondisi Deteksi: Terdapat malfungsi dalam internal hardware (CPU fan, malfungsi video decoder, GVIF IC, MOST [INIC]).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `01-23` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Bus Malfunction (Dokumen: RM00000183S06CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Bus Malfunction (Dokumen: RM00000183S06EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Bus Malfunction (Dok
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terdapat malfungsi dalam ROM.; Kondisi Deteksi: Terdapat malfungsi dalam RAM.; Kondisi Deteksi: Terdapat malfungsi dalam bus.; Kondisi Deteksi: Terdapat malfungsi internal power source.; Kondisi Deteksi: Terdapat malfungsi dalam internal hardware (CPU fan, malfungsi video decoder, GVIF IC, MOST [INIC]).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `01-2A` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Internal Power Supply (Dokumen: RM00000183S06CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Internal Power Supply (Dokumen: RM00000183S06EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Internal
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terdapat malfungsi dalam ROM.; Kondisi Deteksi: Terdapat malfungsi dalam RAM.; Kondisi Deteksi: Terdapat malfungsi dalam bus.; Kondisi Deteksi: Terdapat malfungsi internal power source.; Kondisi Deteksi: Terdapat malfungsi dalam internal hardware (CPU fan, malfungsi video decoder, GVIF IC, MOST [INIC]).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `01-2B` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Internal Hardware (Dokumen: RM00000183S06CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Internal Hardware (Dokumen: RM00000183S06EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Internal Hardwar
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terdapat malfungsi dalam ROM.; Kondisi Deteksi: Terdapat malfungsi dalam RAM.; Kondisi Deteksi: Terdapat malfungsi dalam bus.; Kondisi Deteksi: Terdapat malfungsi internal power source.; Kondisi Deteksi: Terdapat malfungsi dalam internal hardware (CPU fan, malfungsi video decoder, GVIF IC, MOST [INIC]).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `01-2E` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] EEPROM Error (Dokumen: RM00000183S06CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] EEPROM Error (Dokumen: RM00000183S06EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] EEPROM Error (Dokumen: RM0
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terdapat malfungsi dalam ROM.; Kondisi Deteksi: Terdapat malfungsi dalam RAM.; Kondisi Deteksi: Terdapat malfungsi dalam bus.; Kondisi Deteksi: Terdapat malfungsi internal power source.; Kondisi Deteksi: Terdapat malfungsi dalam internal hardware (CPU fan, malfungsi video decoder, GVIF IC, MOST [INIC]).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `01-E0` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Registration Complete Indication Error (Dokumen: RM000001WQS05CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Registration Complete Indication Error (Dokumen: RM000001WQS05EX)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: -; Kondisi Deteksi: Sinyal "Registration complete" dari master device tidak dapat diterima.; Kondisi Deteksi: Sinyal permintaan registrasi dari slave device yang muncul, atau sinyal permintaan registrasi yang muncul dengan menerima sinyal konfirmasi hubungan dari sub-master device.; Kondisi Deteksi: Multiple frame transmission tidak berhasil.; Kondisi Deteksi: Sinyal "Registration complete" dari perangkat master tid
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — Periksa soket, kabel harness, dan komponen Registration Complete Indication Error sesuai dokumen Toyota GSIC RM000001WQS05CX.

### DTC `01-E2` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] ON / OFF Indication Parameter Error (Dokumen: RM00000183Z066X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] ON / OFF Indication Parameter Error (Dokumen: RM00000183Z068X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Ti
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terdapat problem perintah untuk mengontrol ON/OFF dari master device.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Perintah untuk ON / OFF kontrol dari perangkat master memiliki problem.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `01-E3` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Registration Demand Transmission (Dokumen: RM000001WQS05CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Registration Demand Transmission (Dokumen: RM000001WQS05EX)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: -; Kondisi Deteksi: Sinyal "Registration complete" dari master device tidak dapat diterima.; Kondisi Deteksi: Sinyal permintaan registrasi dari slave device yang muncul, atau sinyal permintaan registrasi yang muncul dengan menerima sinyal konfirmasi hubungan dari sub-master device.; Kondisi Deteksi: Multiple frame transmission tidak berhasil.; Kondisi Deteksi: Sinyal "Registration complete" dari perangkat master tid
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — Periksa soket, kabel harness, dan komponen Registration Demand Transmission sesuai dokumen Toyota GSIC RM000001WQS05CX.

### DTC `01-E4` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Multiple Frame Incomplete (Dokumen: RM000001WQS05CX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Multiple Frame Incomplete (Dokumen: RM000001WQS05EX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: -; Kondisi Deteksi: Sinyal "Registration complete" dari master device tidak dapat diterima.; Kondisi Deteksi: Sinyal permintaan registrasi dari slave device yang muncul, atau sinyal permintaan registrasi yang muncul dengan menerima sinyal konfirmasi hubungan dari sub-master device.; Kondisi Deteksi: Multiple frame transmission tidak berhasil.; Kondisi Deteksi: Sinyal "Registration complete" dari perangkat master tid
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — Periksa soket, kabel harness, dan komponen Multiple Frame Incomplete sesuai dokumen Toyota GSIC RM000001WQS05CX.

### DTC `60-10` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] AM Tuner PLL Tidak Terkunci (Dokumen: RM00000200N06SX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] AM Tuner PLL tidak Terkunci (Dokumen: RM00000200N06UX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receive
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: AM tuner PLL (phase locked loop) synchronization adalah tidak memungkinkan.; Kondisi Deteksi: FM tuner PLL (phase locked loop) synchronization adalah tidak memungkinkan.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: AM tuner PLL (fase loop terkunci) sinkronisasi adalah mustahil.; Kondisi Deteksi: FM tuner PLL (fase loop terkunci) sinkronisasi adal
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `60-11` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] FM Tuner PLL tidak Terkunci (Dokumen: RM00000200N06SX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] FM Tuner PLL tidak Terkunci (Dokumen: RM00000200N06UX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receive
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: AM tuner PLL (phase locked loop) synchronization adalah tidak memungkinkan.; Kondisi Deteksi: FM tuner PLL (phase locked loop) synchronization adalah tidak memungkinkan.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: AM tuner PLL (fase loop terkunci) sinkronisasi adalah mustahil.; Kondisi Deteksi: FM tuner PLL (fase loop terkunci) sinkronisasi adal
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `60-12` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] FM/AM Tuner Communication Malfunction (Dokumen: RM00000200Q070X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Malfungsi FM/AM Tuner Communication (Dokumen: RM00000200Q072X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk 
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Komunikasi tuner adalah abnormal.; Kondisi Deteksi: Power source dari tuner adalah abnormal.; Kondisi Deteksi: AM tuner adalah abnormal.; Kondisi Deteksi: FM tuner adalah abnormal.; Kondisi Deteksi: Terjadi problem dalam IC di dalam tuner unit dan radio penerima adalah tidak normal.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `60-42` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Tuner Power Source Error (Dokumen: RM00000200Q070X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Tuner Power Source Error (Dokumen: RM00000200Q072X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Tu
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Komunikasi tuner adalah abnormal.; Kondisi Deteksi: Power source dari tuner adalah abnormal.; Kondisi Deteksi: AM tuner adalah abnormal.; Kondisi Deteksi: FM tuner adalah abnormal.; Kondisi Deteksi: Terjadi problem dalam IC di dalam tuner unit dan radio penerima adalah tidak normal.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `60-43` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] AM Tuner Error (Dokumen: RM00000200Q070X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] AM Tuner Error (Dokumen: RM00000200Q072X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] AM Tuner Error (Dokume
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Komunikasi tuner adalah abnormal.; Kondisi Deteksi: Power source dari tuner adalah abnormal.; Kondisi Deteksi: AM tuner adalah abnormal.; Kondisi Deteksi: FM tuner adalah abnormal.; Kondisi Deteksi: Terjadi problem dalam IC di dalam tuner unit dan radio penerima adalah tidak normal.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `60-44` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] FM Tuner Error (Dokumen: RM00000200Q070X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] FM Tuner Error (Dokumen: RM00000200Q072X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] FM Tuner Error (Dokume
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Komunikasi tuner adalah abnormal.; Kondisi Deteksi: Power source dari tuner adalah abnormal.; Kondisi Deteksi: AM tuner adalah abnormal.; Kondisi Deteksi: FM tuner adalah abnormal.; Kondisi Deteksi: Terjadi problem dalam IC di dalam tuner unit dan radio penerima adalah tidak normal.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `60-50` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Malfungsi dalam Internal IC (Dokumen: RM00000200Q070X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Malfungsi dalam Internal IC (Dokumen: RM00000200Q072X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receive
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Komunikasi tuner adalah abnormal.; Kondisi Deteksi: Power source dari tuner adalah abnormal.; Kondisi Deteksi: AM tuner adalah abnormal.; Kondisi Deteksi: FM tuner adalah abnormal.; Kondisi Deteksi: Terjadi problem dalam IC di dalam tuner unit dan radio penerima adalah tidak normal.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-10` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] CD Player Mechanical Error (Dokumen: RM0000020EW04WX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD Player Mechanical Error (Dokumen: RM0000020EW04YX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Mechanical error dalam CD player terdeteksi selama CD tidak dimasukkan atau dikeluarkan.; Kondisi Deteksi: Pemasukan atau pengeluaran CD gagal.; Kondisi Deteksi: Terjadi problem pembacaan CD.; Kondisi Deteksi: Terjadi kegagalan mekanikal.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `62-11` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] CD Insertion and Ejection Error (Dokumen: RM0000020EW04WX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD Insertion dan Ejection Error (Dokumen: RM0000020EW04YX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Mechanical error dalam CD player terdeteksi selama CD tidak dimasukkan atau dikeluarkan.; Kondisi Deteksi: Pemasukan atau pengeluaran CD gagal.; Kondisi Deteksi: Terjadi problem pembacaan CD.; Kondisi Deteksi: Terjadi kegagalan mekanikal.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `62-12` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] CD Reading Abnormal (Dokumen: RM0000020EW04WX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD Reading Abnormal (Dokumen: RM0000020EW04YX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD Reading A
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Mechanical error dalam CD player terdeteksi selama CD tidak dimasukkan atau dikeluarkan.; Kondisi Deteksi: Pemasukan atau pengeluaran CD gagal.; Kondisi Deteksi: Terjadi problem pembacaan CD.; Kondisi Deteksi: Terjadi kegagalan mekanikal.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `62-14` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Mechanical Malfunction (Dokumen: RM0000020EW04WX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Mechanical Malfunction (Dokumen: RM0000020EW04YX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Mechan
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Mechanical error dalam CD player terdeteksi selama CD tidak dimasukkan atau dikeluarkan.; Kondisi Deteksi: Pemasukan atau pengeluaran CD gagal.; Kondisi Deteksi: Terjadi problem pembacaan CD.; Kondisi Deteksi: Terjadi kegagalan mekanikal.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY: Ganti radio penerimar assembly (Lihat halaman ).
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 1 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY: Ganti radio receiver assembly (Lihat halaman ).

### DTC `62-41` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Disc Salah (Dokumen: RM0000020EY04XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Wrong Disc (Dokumen: RM0000020EY04ZX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Wrong Disc (Dokumen: RM0000020
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Disc Radio penerima assembly; Kondisi Deteksi: Disc yang tidak sesuai dimasukkan.; Kondisi Deteksi: Disc tidak dapat dibaca.; [AUDIO / VIDEO] Area Gangguan: Disc Radio receiver assembly; Kondisi Deteksi: Memasukkan CD yang tidak cocok.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DISC: Periksa bahwa disc tidak berubah bentuk atau retak.
  - Langkah 2 (AUDIO / VIDEO) — MEMBERSIHKAN DISC: Membersihkan disc
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — GANTI DISC DENGAN YANG LAIN DAN PERIKSA ULANG: Ganti disc dengan disc lain yang normal. -> Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 5 (AUDIO / VIDEO) — UBAH DISC
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — SELESAI
  - Langkah 8 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY

### DTC `62-42` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Disc Tidak Dapat Dibaca (Dokumen: RM0000020EY04XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Disc tidak dapat Dibaca (Dokumen: RM0000020EY04ZX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Disc
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Disc Radio penerima assembly; Kondisi Deteksi: Disc yang tidak sesuai dimasukkan.; Kondisi Deteksi: Disc tidak dapat dibaca.; [AUDIO / VIDEO] Area Gangguan: Disc Radio receiver assembly; Kondisi Deteksi: Memasukkan CD yang tidak cocok.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DISC: Periksa bahwa disc tidak berubah bentuk atau retak.
  - Langkah 2 (AUDIO / VIDEO) — MEMBERSIHKAN DISC: Membersihkan disc
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — GANTI DISC DENGAN YANG LAIN DAN PERIKSA ULANG: Ganti disc dengan disc lain yang normal. -> Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 5 (AUDIO / VIDEO) — UBAH DISC
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — SELESAI
  - Langkah 8 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY

### DTC `62-43` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] CD-ROM Abnormal (Dokumen: RM0000020EZ04WX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD-ROM Abnormal (Dokumen: RM0000020EZ04YX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD-ROM Abnormal (Dok
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: CD Radio penerima assembly; Kondisi Deteksi: Pengoperasian CD-ROM adalah abnormal.; [AUDIO / VIDEO] Area Gangguan: CD Radio receiver assembly; Kondisi Deteksi: Pengoperasian CD-ROM abnormal.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA APAKAH CD YANG BENAR DIMASUKKAN: Pastikan apakah CD adalah audio CD atau CD dengan file MP3 atau WMA, dan pastikan juga bahwa CD tidak rusak, retak, bernoda, terbakar atau cacat lainnya.
  - Langkah 2 (AUDIO / VIDEO) — GANTI CD DENGAN YANG LAIN DAN PERIKSA ULANG: Ganti CD dengan CD lain yang normal. -> Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — GANTI CD
  - Langkah 4 (AUDIO / VIDEO) — SELESAI
  - Langkah 5 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA APAKAH CD YANG DIMASUKKAN SESUAI: Pastikan bahwa CD berupa audio CD atau CD dengan file MP3 atau WMA, dan bahwa CD tersebut itu tidak berubah bentuk, cacat, bernoda, terbakar, atau rusak.
  - Langkah 2 (AUDIO / VIDEO) — GANTI CD DENGAN YANG LAIN DAN PERIKSA ULANG: Ganti CD dengan yang normal. -> Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 5 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-44` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] CD Abnormal (Dokumen: RM0000020F004XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD Abnormal (Dokumen: RM0000020F004ZX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD Abnormal (Dokumen: RM0000
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Operation error dalam mekanisme CD.; Kondisi Deteksi: Arus berlebihan terdapat dalam CD player; Kondisi Deteksi: Malfungsi dalam sistem insertion/ejection (memasukan/mengeluarkan).; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Kesalahan pengoperasian dalam mekanisme CD.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-45` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Eject Error (Dokumen: RM0000020F104VX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Eject Error (Dokumen: RM0000020F104XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Eject Error (Dokumen: RM0000
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Disc tidak dapat dikeluarkan.; Kondisi Deteksi: Terjadi error mekanikal selama pengoperasian elevator.; Kondisi Deteksi: Error terdeteksi dalam klem CD player.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Disc tidak dapat keluar (eject).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO PENERIMA ASSEMBLY: Periksa apakah disc dapat diganti, dimasukkan atau dikeluarkan secara normal.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO RECEIVER ASSEMBLY: Periksa apakah disk dapat diganti, dimasukkan atau dikeluarkan secara normal.
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-46` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Disc Tergores / Terbalik (Dokumen: RM0000020F204WX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Tergores / Disc Terbalik (Dokumen: RM0000020F204YX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Te
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Disc Radio penerima assembly; Kondisi Deteksi: Tergores atau kotor ditemukan pada permukaan disc atau dimasukkan terbalik.; [AUDIO / VIDEO] Area Gangguan: Disc Radio receiver assembly; Kondisi Deteksi: Goresan atau kotoran ditemukan pada permukaan disk atau disk dimasukkan terbalik.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA BAHWA DISC DIMASUKKAN DENGAN BENAR: Periksa apakah disc dimasukkan terbalik atau tidak.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DISC: Periksa bahwa disc tidak berubah bentuk atau retak.
  - Langkah 3 (AUDIO / VIDEO) — MEMBERSIHKAN DISC: Jika terdapat kotoran pada permukaan disc, bersihkan dengan kain yang lembut dari bagian dalam ke bagian luar dengan arah berputar.
  - Langkah 4 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 5 (AUDIO / VIDEO) — MASUKKAN ULANG DISC DENGAN BENAR: Ganti disc dengan disc lain yang normal. -> Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 6 (AUDIO / VIDEO) — MASUKKAN DISC SECARA BENAR
  - Langkah 7 (AUDIO / VIDEO) — UBAH DISC
  - Langkah 8 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA

### DTC `62-47` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Temperatur Tinggi (Dokumen: RM0000020F304VX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] High Temperature (Dokumen: RM0000020F304XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] High Temperature 
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Sensor mendeteksi bahwa temperatur unit CD adalah tinggi (lebih dari 80°C [176°F]).; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Sensor mendeteksi bahwa suhu unit CD yang tinggi (lebih tinggi dari 80° C [176° F]).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO PENERIMA ASSEMBLY: Parkirkan kendaraan ditempat yang dingin. -> Periksa bahwa temperatur dari radio penerima assembly telah cukup dingin, dan kemudian hidupkan mesin. Periksa apakah malfungsi hilang.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO RECEIVER ASSEMBLY: Parkir kendaraan di tempat yang teduh. -> Periksa suhu radio receiver assembly telah menjadi cukup rendah, dan kemudian hidupkan mesin. Periksa apakah malfungsi hilang.
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-48` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Arus Berlebihan (Dokumen: RM0000020F004XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Excess Current (Dokumen: RM0000020F004ZX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Excess Current (Dokum
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Operation error dalam mekanisme CD.; Kondisi Deteksi: Arus berlebihan terdapat dalam CD player; Kondisi Deteksi: Malfungsi dalam sistem insertion/ejection (memasukan/mengeluarkan).; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Kesalahan pengoperasian dalam mekanisme CD.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-50` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Tray Insertion / Ejection Error (Dokumen: RM0000020F004XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Tray Insertion / Ejection Error (Dokumen: RM0000020F004ZX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Operation error dalam mekanisme CD.; Kondisi Deteksi: Arus berlebihan terdapat dalam CD player; Kondisi Deteksi: Malfungsi dalam sistem insertion/ejection (memasukan/mengeluarkan).; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Kesalahan pengoperasian dalam mekanisme CD.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-51` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Elevator Error (Dokumen: RM0000020F104VX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Elevator Error (Dokumen: RM0000020F104XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Elevator Error (Dokume
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Disc tidak dapat dikeluarkan.; Kondisi Deteksi: Terjadi error mekanikal selama pengoperasian elevator.; Kondisi Deteksi: Error terdeteksi dalam klem CD player.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Disc tidak dapat keluar (eject).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO PENERIMA ASSEMBLY: Periksa apakah disc dapat diganti, dimasukkan atau dikeluarkan secara normal.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO RECEIVER ASSEMBLY: Periksa apakah disk dapat diganti, dimasukkan atau dikeluarkan secara normal.
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-52` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Clamp Error (Dokumen: RM0000020F104VX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Clamp Error (Dokumen: RM0000020F104XX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Clamp Error (Dokumen: RM0000
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Disc tidak dapat dikeluarkan.; Kondisi Deteksi: Terjadi error mekanikal selama pengoperasian elevator.; Kondisi Deteksi: Error terdeteksi dalam klem CD player.; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Disc tidak dapat keluar (eject).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO PENERIMA ASSEMBLY: Periksa apakah disc dapat diganti, dimasukkan atau dikeluarkan secara normal.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO RECEIVER ASSEMBLY: Periksa apakah disk dapat diganti, dimasukkan atau dikeluarkan secara normal.
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-78` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] DSP Error (Dokumen: RM0000020FB04LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] DSP Error (Dokumen: RM0000020FB04NX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] DSP Error (Dokumen: RM0000020FB0
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio penerima assembly; Kondisi Deteksi: Terjadi error selama proses decode (MP3 / WMA).; [AUDIO / VIDEO] Area Gangguan: Radio receiver assembly; Kondisi Deteksi: Terjadi kesalahan selama proses membaca (MP3/WMA).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — SELASAI (KODE INI MUNGKIN MUNCUL MESKIPUN TIDAK TERDAPAT MALFUNGSI)
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI (KODE INI MUNGKIN TETAP DI-OUTPUT JIKA TIDAK TERDAPAT MALFUNGSI)
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-7D` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Disc tidak dapat Dimainkan (Dokumen: RM0000020S404LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Disc tidak dapat dimainkan (Dokumen: RM0000020S404NX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Disc Radio penerima assembly; Kondisi Deteksi: Copy-protected file, yang tidak dapat dimainkan, digunakan.; [AUDIO / VIDEO] Area Gangguan: Disc Radio receiver assembly; Kondisi Deteksi: File copy-dilindungi, yang tidak dapat dimainkan, digunakan.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — UBAH DISC: Masukkan disc dengan playable file dan periksa apakah disc dapat dimainkan dengan benar.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI DISC: Masukkan disk dengan file dimainkan dan memeriksa apakah disc dapat diputar dengan benar.
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-7E` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Tidak Ada File yang Dapat Dimainkan (Dokumen: RM0000020S404LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] No Playable Files (Dokumen: RM0000020S404NX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Disc Radio penerima assembly; Kondisi Deteksi: Copy-protected file, yang tidak dapat dimainkan, digunakan.; [AUDIO / VIDEO] Area Gangguan: Disc Radio receiver assembly; Kondisi Deteksi: File copy-dilindungi, yang tidak dapat dimainkan, digunakan.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — UBAH DISC: Masukkan disc dengan playable file dan periksa apakah disc dapat dimainkan dengan benar.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI DISC: Masukkan disk dengan file dimainkan dan memeriksa apakah disc dapat diputar dengan benar.
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `62-7F` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Copyright Protection Error (Dokumen: RM0000020S404LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Copyright Protection Error (Dokumen: RM0000020S404NX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Disc Radio penerima assembly; Kondisi Deteksi: Copy-protected file, yang tidak dapat dimainkan, digunakan.; [AUDIO / VIDEO] Area Gangguan: Disc Radio receiver assembly; Kondisi Deteksi: File copy-dilindungi, yang tidak dapat dimainkan, digunakan.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — UBAH DISC: Masukkan disc dengan playable file dan periksa apakah disc dapat dimainkan dengan benar.
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI DISC: Masukkan disk dengan file dimainkan dan memeriksa apakah disc dapat diputar dengan benar.
  - Langkah 3 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `B1000` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 31] Malfungsi Center Airbag Sensor Assembly (Dokumen: RM000000YTI0BEX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 31] Center Airbag Sensor Assembly Malfungsi (Dokumen: RM000000YTI0BFX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Center airbag sensor assembly; Kondisi Deteksi: Center airbag sensor malfungsi.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — LANJUTKAN KE BAGAN DIAGNOSTIC TROUBLE CODE
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY

### DTC `B1550` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi Tuner DAB (Dokumen: RM000004N7L003X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] DAB Tuner Malfungsi (Dokumen: RM000004N7L005X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] DAB
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Malfungsi pada digital radio tuner.; Kondisi Deteksi: Malfungsi pada extension module.; [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly Harness atau konektor; Kondisi Deteksi: Terlepas hubungan pada digital radio tuner.; Kondisi Deteksi: Terlepas hubungan pada extension module.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO DAN DISPLAY RECEIVER ASSEMBLY: Lepas hubungan konektor untuk peralatan opsional dari radio dan display receiver assembly. -> Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor radio dan display receiver assembly.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR: Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor peralatan opsional.
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI PARALATAN OPSIONAL: Lihat ke buku pedoman paralatan opsional untuk informasi perbaikan.
  - Langkah 5 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR

### DTC `B1552` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi Extension Module (Dokumen: RM000004N7L003X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Extension Module Malfungsi (Dokumen: RM000004N7L005X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Malfungsi pada digital radio tuner.; Kondisi Deteksi: Malfungsi pada extension module.; [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly Harness atau konektor; Kondisi Deteksi: Terlepas hubungan pada digital radio tuner.; Kondisi Deteksi: Terlepas hubungan pada extension module.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO DAN DISPLAY RECEIVER ASSEMBLY: Lepas hubungan konektor untuk peralatan opsional dari radio dan display receiver assembly. -> Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor radio dan display receiver assembly.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR: Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor peralatan opsional.
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI PARALATAN OPSIONAL: Lihat ke buku pedoman paralatan opsional untuk informasi perbaikan.
  - Langkah 5 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR

### DTC `B1564` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Lepas hubungan Radio Digital (Dokumen: RM000004N7L003X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Digital Radio Terputus (Dokumen: RM000004N7L005X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan D
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Malfungsi pada digital radio tuner.; Kondisi Deteksi: Malfungsi pada extension module.; [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly Harness atau konektor; Kondisi Deteksi: Terlepas hubungan pada digital radio tuner.; Kondisi Deteksi: Terlepas hubungan pada extension module.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO DAN DISPLAY RECEIVER ASSEMBLY: Lepas hubungan konektor untuk peralatan opsional dari radio dan display receiver assembly. -> Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor radio dan display receiver assembly.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR: Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor peralatan opsional.
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI PARALATAN OPSIONAL: Lihat ke buku pedoman paralatan opsional untuk informasi perbaikan.
  - Langkah 5 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR

### DTC `B156C` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Lepas hubungan Module Extension (Dokumen: RM000004N7L003X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Extension Module Terputus (Dokumen: RM000004N7L005X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Malfungsi pada digital radio tuner.; Kondisi Deteksi: Malfungsi pada extension module.; [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly Harness atau konektor; Kondisi Deteksi: Terlepas hubungan pada digital radio tuner.; Kondisi Deteksi: Terlepas hubungan pada extension module.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO DAN DISPLAY RECEIVER ASSEMBLY: Lepas hubungan konektor untuk peralatan opsional dari radio dan display receiver assembly. -> Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor radio dan display receiver assembly.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR: Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor peralatan opsional.
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI PARALATAN OPSIONAL: Lihat ke buku pedoman paralatan opsional untuk informasi perbaikan.
  - Langkah 5 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR

### DTC `B1579` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Lepas hubungan Voice Recognition Microphone (Dokumen: RM000004N7O004X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Voice Recognition Microphone Terputus (Dokumen: RM000004N7O006X) | [AUDIO / VIDEO — SISTEM AUDIO DAN 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Lampu peta assembly (telephone microphone assembly) Radio dan display receiver assembly; Kondisi Deteksi: Sinyal telephon microphone adalah hilang.; [AUDIO / VIDEO] Area Gangguan: Map light assembly (telephone microphone assembly) Radio and display receiver assembly; Kondisi Deteksi: Sinyal telephone microphone hilang.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA MICROPHONE (PERIKSA PENGOPERASIAN): Masuk layar "Microphone & Voice Recognition Check" (Lihat halaman ). -> Bila voice di-input ke dalam microphone, periksa bahwa meter level input microphone berubah sesuai dengan input voice.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR (RADIO DAN DISPLAY RECEIVER - LAMPU PETA): Lepas hubungan konektor G127 radio dan display receiver assembly. -> Lepas hubungan konektor N2 lampu peta assembly -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA RADIO DAN DISPLAY RECEIVER ASSEMBLY: Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
  - Langkah 4 (AUDIO / VIDEO) — GANTI TELEPHONE MICROPHONE DENGAN YANG LAIN DAN PERIKSA: Ganti telephone microphone dengan yang satu yang normal (Lihat halaman ). -> Periksa jika terjadi problem yang sama lagi.
  - Langkah 5 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 7 (AUDIO / VIDEO) — GANTI LAMPU PETA ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — SELESAI (TELEPHONE MICROPHONE ASSEMBLY ADALAH RUSAK)
- **Spesifikasi Standar Multimeter**:
  - `[AUDIO / VIDEO] Tahanan Standar: G127-4 (MACC) - N2-4 (MACC) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G127-5 (MIN+) - N2-3 (MCO+) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G127-19 (MIN-) - N2-2 (MCO-) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G127-6 (SNS2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G127-4 (MACC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Tahanan Standar: G127-5 (MIN+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Tahanan Standar: G127-19 (MIN-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Tahanan Standar: G127-18 (SGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B157E` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Lepas hubungan Antena Bluetooth (Dokumen: RM000004N7L003X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Bluetooth Antenna Terputus (Dokumen: RM000004N7L005X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radi
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Malfungsi pada digital radio tuner.; Kondisi Deteksi: Malfungsi pada extension module.; [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly Harness atau konektor; Kondisi Deteksi: Terlepas hubungan pada digital radio tuner.; Kondisi Deteksi: Terlepas hubungan pada extension module.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO DAN DISPLAY RECEIVER ASSEMBLY: Lepas hubungan konektor untuk peralatan opsional dari radio dan display receiver assembly. -> Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor radio dan display receiver assembly.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR: Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor peralatan opsional.
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI PARALATAN OPSIONAL: Lihat ke buku pedoman paralatan opsional untuk informasi perbaikan.
  - Langkah 5 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR

### DTC `B1585` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi Peralatan USB (Dokumen: RM000003WFQ02EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] USB Device Malfungsi (Dokumen: RM000003WFQ02GX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB atau "iPod" Radio dan display receiver assembly; [AUDIO / VIDEO] Area Gangguan: USB device atau "iPod" Radio and display receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter assembly No. 1. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jac
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT PERALATAN USB TIDAK KOMPATIBEL, VERSI "iPod" TIDAK SESUAI, ATAU PERALATAN USB ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly No. 1. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adap
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT USB DEVICE TIDAK SESUAI, VERSI "iPod" TIDAK SESUAI, ATAU USB DEVICE ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO AND DISPLAY RECEIVER ASSEMBLY

### DTC `B158A` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi Extension Module Noise Adjustment (Dokumen: RM000004N7L003X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Extension Module Noise Adjustment Malfunction (Dokumen: RM000004N7L005X) | [AUDIO / VIDEO — SISTEM AU
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Malfungsi pada digital radio tuner.; Kondisi Deteksi: Malfungsi pada extension module.; [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly Harness atau konektor; Kondisi Deteksi: Terlepas hubungan pada digital radio tuner.; Kondisi Deteksi: Terlepas hubungan pada extension module.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA RADIO DAN DISPLAY RECEIVER ASSEMBLY: Lepas hubungan konektor untuk peralatan opsional dari radio dan display receiver assembly. -> Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor radio dan display receiver assembly.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR: Periksa bahwa tidak ada kerusakan dalam terminal atau part pada konektor peralatan opsional.
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 4 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI PARALATAN OPSIONAL: Lihat ke buku pedoman paralatan opsional untuk informasi perbaikan.
  - Langkah 5 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 6 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR

### DTC `B15A2` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi DVD Player (Dokumen: RM000003WFL02EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] DVD Player Malfungsi (Dokumen: RM000003WFL02GX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] D
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Kesalahan dalam sikuit gambar.; Kondisi Deteksi: Kesalahan komunikasi tunner.; Kondisi Deteksi: Malfungsi "Bluetooth" module.; [AUDIO / VIDEO] Area Gangguan: Radio and display receiver assembly; Kondisi Deteksi: Error daalm sirkuit picture.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO AND DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B15B0` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi Display Screen (Dokumen: RM000003WFL02EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Display Screen Malfungsi (Dokumen: RM000003WFL02GX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Dis
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Kesalahan dalam sikuit gambar.; Kondisi Deteksi: Kesalahan komunikasi tunner.; Kondisi Deteksi: Malfungsi "Bluetooth" module.; [AUDIO / VIDEO] Area Gangguan: Radio and display receiver assembly; Kondisi Deteksi: Error daalm sirkuit picture.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO AND DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B15B3` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi Radio Tuner (Dokumen: RM000003WFL02EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Radio Tuner Malfungsi (Dokumen: RM000003WFL02GX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)]
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Kesalahan dalam sikuit gambar.; Kondisi Deteksi: Kesalahan komunikasi tunner.; Kondisi Deteksi: Malfungsi "Bluetooth" module.; [AUDIO / VIDEO] Area Gangguan: Radio and display receiver assembly; Kondisi Deteksi: Error daalm sirkuit picture.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO AND DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B15B4` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi CD Changer (Dokumen: RM000003WFL02EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] CD Changer Malfungsi (Dokumen: RM000003WFL02GX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] C
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Kesalahan dalam sikuit gambar.; Kondisi Deteksi: Kesalahan komunikasi tunner.; Kondisi Deteksi: Malfungsi "Bluetooth" module.; [AUDIO / VIDEO] Area Gangguan: Radio and display receiver assembly; Kondisi Deteksi: Error daalm sirkuit picture.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO AND DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B15B5` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi DVD Changer (Dokumen: RM000003WFL02EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] DVD Changer Malfungsi (Dokumen: RM000003WFL02GX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)]
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Kesalahan dalam sikuit gambar.; Kondisi Deteksi: Kesalahan komunikasi tunner.; Kondisi Deteksi: Malfungsi "Bluetooth" module.; [AUDIO / VIDEO] Area Gangguan: Radio and display receiver assembly; Kondisi Deteksi: Error daalm sirkuit picture.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO AND DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B15B7` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Malfungsi Bluetooth Module (Dokumen: RM000003WFL02EX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Bluetooth Module Malfungsi (Dokumen: RM000003WFL02GX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Radio dan display receiver assembly; Kondisi Deteksi: Kesalahan dalam sikuit gambar.; Kondisi Deteksi: Kesalahan komunikasi tunner.; Kondisi Deteksi: Malfungsi "Bluetooth" module.; [AUDIO / VIDEO] Area Gangguan: Radio and display receiver assembly; Kondisi Deteksi: Error daalm sirkuit picture.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul trouble yang sama lagi.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO DAN DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah masalah yang sama terjadi kembali.
  - Langkah 2 (AUDIO / VIDEO) — GANTI RADIO AND DISPLAY RECEIVER ASSEMBLY
  - Langkah 3 (AUDIO / VIDEO) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B15C3` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Short pada Output Speaker (Dokumen: RM000004933006X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Display)] Speaker Output Short (Dokumen: RM000004933008X) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio dan Displa
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Speaker Radio dan display receiver assembly Harness atau konektor; Kondisi Deteksi: Sebuah short terdeteksi dalam sirkuit output speaker.; [AUDIO / VIDEO] Area Gangguan: Speaker Radio and display receiver assembly Harness atau konektor; Kondisi Deteksi: Mendeteksi short dalam sirkuit output speaker.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Lepas hubungan konektor G129 dan G128 radio dan display receiver assembly. -> Hapus DTC (Lihat halaman ). -> Periksa bila muncul DTC B15C3
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hubungkan kembali konektor G128 radio dan display receiver assembly. -> Hapus DTC (Lihat halaman ). -> Periksa bila muncul DTC B15C3
  - Langkah 3 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR (RADIO DAN DISPLAY RECEIVER - SPEAKER NO. 2 DEPAN): Lepas hubungan konektor G129 radio dan display receiver assembly. -> Lepas hubungan konektor H6*1 dan/atau I6*2 speaker. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR (SPEAKER NO. 2 DEPAN - SPEAKER NO. 1 DEPAN): Lepas hubungan konektor H6*1 dan/atau I6*2 speaker. -> Lepas hubungan konektor H4*1 dan/atau I1*2 speaker. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (AUDIO / VIDEO) — MEMERIKSA SPEAKER NO. 1 DEPAN ASSEMBLY: Lepas hubungan konektor H4*1 dan/atau I1*2 speaker. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (AUDIO / VIDEO) — MEMERIKSA SPEAKER NO. 2 DEPAN ASSEMBLY: Ganti sementara speaker dengan yang baru atau yang berfungsi normal (Lihat halaman ). -> Periksa apakah malfungsi hilang.
  - Langkah 7 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR (RADIO DAN DISPLAY RECEIVER - KABEL SPIRAL): Lepas hubungan konektor G128 radio dan display receiver assembly. -> Lepas hubungan konektor J7*1 dan/atau J3*2 speaker. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (AUDIO / VIDEO) — MEMERIKSA SPEAKER BELAKANG ASSEMBLY: Lepas hubungan konektor J7*1 dan/atau J3*2 speaker. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[AUDIO / VIDEO] Tahanan Standar: G129-1 (FR+) - H6-4 (TWR+) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G129-5 (FR-) - H6-2 (TWR-) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G129-1 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Tahanan Standar: G129-5 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Tahanan Standar: G129-2 (FL+) - I6-4 (TWL+) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G129-6 (FL-) - I6-2 (TWL-) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: G129-2 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Tahanan Standar: G129-6 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B1610` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 13] Malfungsi Airbag Sensor Depan RH (Dokumen: RM000003876019X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 13] Front Airbag Sensor RH Malfungsi (Dokumen: RM00000387601AX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 13] Fron
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel utama ruang mesin Front airbag sensor RH Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Engine room main wire Front airbag sensor RH Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA HUBUNGAN KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Periksa bahwa konektor terhubung dengan sempurna pada center airbag sensor dan airbag sensor depan RH.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Lepas hubungan konektor dari center airbag sensor dan airbag sensor depan RH. -> Periksa bahwa konektor (pada sisi center airbag sensor dan sisi airbag sensor depan RH) tidak rusak.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT AIRBAG SENSOR DEPAN RH: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG SENSOR DEPAN RH: Hubungkan konektor ke center airbag sensor. -> Pertukarkan airbag sensor depan RH dengan LH dan hubungkan konektor-konektornya. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition swit
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari kabel utama ruang mesin. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai da
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — HUBUNGKAN KONEKTOR DENGAN SEMPURNA
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI HARNESS DAN KONEKTOR
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: A30-2 (+SR) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: A30-1 (-SR) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A30-2 (+SR) - A30-1 (-SR) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A30-2 (+SR) - A30-1 (-SR) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A30-2 (+SR) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A30-1 (-SR) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: AG3-1 (+SR) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: AG3-2 (-SR) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1615` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 14] Malfungsi Airbag Sensor Depan LH (Dokumen: RM0000038AX01DX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 14] Front Airbag Sensor LH Malfungsi (Dokumen: RM0000038AX01EX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 14] Fron
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel utama ruang mesin Front airbag sensor LH Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Engine room main wire Front airbag sensor LH Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA HUBUNGAN KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Periksa bahwa konektor terhubung dengan sempurna pada center airbag sensor dan airbag sensor depan LH.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Lepas hubungan konektor dari center airbag sensor dan airbag sensor depan LH. -> Periksa bahwa konektor (pada sisi center airbag sensor dan sisi airbag sensor depan LH) tidak rusak.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT AIRBAG SENSOR DEPAN LH: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG SENSOR DEPAN LH: Hubungkan konektor ke center airbag sensor. -> Pertukarkan airbag sensor depan LH dengan RH dan hubungkan konektor untuk keduanya. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition s
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari kabel utama ruang mesin. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai da
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — HUBUNGKAN KONEKTOR DENGAN SEMPURNA
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI HARNESS DAN KONEKTOR
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: A31-2 (+SL) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: A31-1 (-SL) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A31-2 (+SL) - A31-1 (-SL) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A31-2 (+SL) - A31-1 (-SL) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A31-2 (+SL) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: A31-1 (-SL) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: AG3-3 (+SL) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: AG3-4 (-SL) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1800` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short Circuit dalam Squib Sisi Pengemudi (Dokumen: RM000000XFI0DTX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short dalam Sirkuit Driver Side Squib (Dokumen: RM000000XFI0DUX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash 
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Spiral cable sub-assembly Steering pad (Squib sisi pengemudi) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Spiral cable sub-assembly Steering pad (Driver side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω) ke konektor E (konektor 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke steering pad dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -> Hapus DTC (Lihat h
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari spiral cable. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel d
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SPIRAL CABLE SUB-ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 2 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 1 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 1 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-1 (D+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-2 (D-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1801` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Open Circuit dalam Squib Sisi Pengemudi (Dokumen: RM000000XFI0DTX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Open Circuit dalam Driver Side Squib (Dokumen: RM000000XFI0DUX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Co
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Spiral cable sub-assembly Steering pad (Squib sisi pengemudi) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Spiral cable sub-assembly Steering pad (Driver side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω) ke konektor E (konektor 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke steering pad dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -> Hapus DTC (Lihat h
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari spiral cable. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel d
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SPIRAL CABLE SUB-ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 2 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 1 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 1 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-1 (D+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-2 (D-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1802` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke GND dalam Sirkuit Squib Sisi Pengemudi (Dokumen: RM000000XFI0DTX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke GND dalam Sirkuit Driver Side Squib (Dokumen: RM000000XFI0DUX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM A
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Spiral cable sub-assembly Steering pad (Squib sisi pengemudi) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Spiral cable sub-assembly Steering pad (Driver side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω) ke konektor E (konektor 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke steering pad dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -> Hapus DTC (Lihat h
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari spiral cable. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel d
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SPIRAL CABLE SUB-ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 2 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 1 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 1 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-1 (D+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-2 (D-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1803` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke B+ dalam Sirkuit Squib Sisi Pengemudi (Dokumen: RM000000XFI0DTX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke B+ dalam Sirkuit Squib Sisi Pengemudi (Dokumen: RM000000XFI0DUX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM 
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Spiral cable sub-assembly Steering pad (Squib sisi pengemudi) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Spiral cable sub-assembly Steering pad (Driver side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω) ke konektor E (konektor 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke steering pad dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -> Hapus DTC (Lihat h
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari spiral cable. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel d
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SPIRAL CABLE SUB-ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 2 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: 1 (D) - Masa bodi (Ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D+) - 1 (D-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 2 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: 1 (D) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-1 (D+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: G52-2 (D-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1805` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ0E8X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short Sirkuit dalam Front Passenger Side Squib (Dokumen: RM000000XFJ0E9X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM 
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang panel instrumen assembly (Squib sisi penumpang depan) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Instrument panel wire assembly Instrument panel passenger airbag assembly (Front passenger side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY (SQUIB SISI PENUMPANG DEPAN): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag penumpang depan panel instrumen. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke airbag penumpang panel instrumen dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan n
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-2 (P-) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1806` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Open dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ0E8X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Open dalam Sirkuit Front Passenger Side Squib (Dokumen: RM000000XFJ0E9X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AI
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang panel instrumen assembly (Squib sisi penumpang depan) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Instrument panel wire assembly Instrument panel passenger airbag assembly (Front passenger side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY (SQUIB SISI PENUMPANG DEPAN): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag penumpang depan panel instrumen. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke airbag penumpang panel instrumen dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan n
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-2 (P-) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1807` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke GND dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ0E8X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke GND dalam Sirkuit Front Passenger Side Squib (Dokumen: RM000000XFJ0E9X) | [SUPPLEMENTAL RESTRAINT SY
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang panel instrumen assembly (Squib sisi penumpang depan) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Instrument panel wire assembly Instrument panel passenger airbag assembly (Front passenger side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY (SQUIB SISI PENUMPANG DEPAN): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag penumpang depan panel instrumen. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke airbag penumpang panel instrumen dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan n
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-2 (P-) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B1808` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke B+ dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ0E8X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke B+ dalam Sirkuit Front Passenger Side Squib (Dokumen: RM000000XFJ0E9X) | [SUPPLEMENTAL RESTRAINT SYST
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang panel instrumen assembly (Squib sisi penumpang depan) Center airbag sensor assembly; [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Instrument panel wire Instrument panel wire assembly Instrument panel passenger airbag assembly (Front passenger side squib) Center airbag sensor assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY (SQUIB SISI PENUMPANG DEPAN): Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag penumpang depan panel instrumen. -> Hubungkan sisi kabel putih SST (tahanan 2.1 Ω
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar ignition switch ke off. -> Lepas hubungan kabel terminal negatif (-) baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Lepas hubungan konektor dari center airbag sensor. -> Periksa bahwa konektor (
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke off. -> Lepas hubungan kabe
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Hubungkan konektor ke airbag penumpang panel instrumen dan center airbag sensor. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON, dan tunggu minimal selama 60 detik. -
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Hubungkan kabel ke terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan n
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG PENUMPANG PANEL INSTRUMEN ASSEMBLY
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI CENTER AIRBAG SENSOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: F1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - F1-2 (P-) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-1 (P+) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan Standar: F1-2 (P-) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-1 (P+) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tegangan Standar: GF1-2 (P-) - Masa bodi (ignition switch ON)` : **Di bawah 1 V**

### DTC `B2416` — [PENERANGAN (EXT) — SISTEM PENERANGAN] Height Control Sensor Malfunction (Dokumen: RM0000011SX05DX) | [PENERANGAN (EXT) — SISTEM PENERANGAN] Height Control Sensor Malfunction (Dokumen: RM0000011SX0A5X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [PENERANGAN (EXT)] Area Gangguan: Rear height control sensor sub-assembly LH Harness atau konektor Headlight leveling ECU assembly; Kondisi Deteksi: Malfungsi dalam rear height control sensor. Open atau short dalam sirkuit rear height control sensor.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (PENERANGAN (EXT)) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (PENERANGAN (EXT)) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (REAR HEIGHT CONTROL SENSOR): Menggunakan intelligent tester, baca Data List (Lihat halaman ).
  - Langkah 3 (PENERANGAN (EXT)) — PERIKSA HARNESS DAN KONEKTOR (HEADLIGHT LEVELING ECU ASSEMBLY - REAR HEIGHT CONTROL SENSOR SUB-ASSEMBLY LH): Lepas hubungan konektor G100 headlight leveling. -> Lepas hubungan konektor L10 rear height control sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (PENERANGAN (EXT)) — MEMERIKSA REAR HEIGHT CONTROL SENSOR SUB-ASSEMBLY LH: Lepas rear height control sensor (Lihat halaman ). -> Hubungkan 3 baterai sel kering (1.5 V) secara seri. -> Hubungkan ujung positif (+) pada baterai ke terminal 3 (SHB) rear height control sensor dan ujung negatif (-) pada baterai ke termi
  - Langkah 5 (PENERANGAN (EXT)) — GANTI HEADLIGHT LEVELING ECU ASSEMBLY
  - Langkah 6 (PENERANGAN (EXT)) — GANTI REAR HEIGHT CONTROL SENSOR SUB-ASSEMBLY LH
  - Langkah 7 (PENERANGAN (EXT)) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (PENERANGAN (EXT)) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-12 (SBR) - L10-3 (SHB) (Selalu)` : **Dibawah 1 Ω**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-19 (SHRL) - L10-2 (SHRR) (Selalu)` : **Dibawah 1 Ω**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-21 (SGR) - L10-1 (SHG) (Selalu)` : **Dibawah 1 Ω**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-12 (SBR) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-19 (SHRL) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-21 (SGR) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[PENERANGAN (EXT)] Voltase Standar: 2 (SHRR) - 1 (SHG) (High (+))` : **4.34 sampai 4.6 V**
  - `[PENERANGAN (EXT)] Voltase Standar: 2 (SHRR) - 1 (SHG) (Normal)` : **3.0 sampai 3.3 V**

### DTC `B241A` — [PENERANGAN (EXT) — SISTEM PENERANGAN] Rear Height Control Sensor (Dokumen: RM0000011SX05DX) | [PENERANGAN (EXT) — SISTEM PENERANGAN] Rear Height Control Sensor (Dokumen: RM0000011SX0A5X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [PENERANGAN (EXT)] Area Gangguan: Rear height control sensor sub-assembly LH Harness atau konektor Headlight leveling ECU assembly; Kondisi Deteksi: Malfungsi dalam rear height control sensor. Open atau short dalam sirkuit rear height control sensor.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (PENERANGAN (EXT)) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (PENERANGAN (EXT)) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (REAR HEIGHT CONTROL SENSOR): Menggunakan intelligent tester, baca Data List (Lihat halaman ).
  - Langkah 3 (PENERANGAN (EXT)) — PERIKSA HARNESS DAN KONEKTOR (HEADLIGHT LEVELING ECU ASSEMBLY - REAR HEIGHT CONTROL SENSOR SUB-ASSEMBLY LH): Lepas hubungan konektor G100 headlight leveling. -> Lepas hubungan konektor L10 rear height control sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (PENERANGAN (EXT)) — MEMERIKSA REAR HEIGHT CONTROL SENSOR SUB-ASSEMBLY LH: Lepas rear height control sensor (Lihat halaman ). -> Hubungkan 3 baterai sel kering (1.5 V) secara seri. -> Hubungkan ujung positif (+) pada baterai ke terminal 3 (SHB) rear height control sensor dan ujung negatif (-) pada baterai ke termi
  - Langkah 5 (PENERANGAN (EXT)) — GANTI HEADLIGHT LEVELING ECU ASSEMBLY
  - Langkah 6 (PENERANGAN (EXT)) — GANTI REAR HEIGHT CONTROL SENSOR SUB-ASSEMBLY LH
  - Langkah 7 (PENERANGAN (EXT)) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (PENERANGAN (EXT)) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-12 (SBR) - L10-3 (SHB) (Selalu)` : **Dibawah 1 Ω**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-19 (SHRL) - L10-2 (SHRR) (Selalu)` : **Dibawah 1 Ω**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-21 (SGR) - L10-1 (SHG) (Selalu)` : **Dibawah 1 Ω**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-12 (SBR) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-19 (SHRL) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[PENERANGAN (EXT)] Tahanan Standar: G100-21 (SGR) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[PENERANGAN (EXT)] Voltase Standar: 2 (SHRR) - 1 (SHG) (High (+))` : **4.34 sampai 4.6 V**
  - `[PENERANGAN (EXT)] Voltase Standar: 2 (SHRR) - 1 (SHG) (Normal)` : **3.0 sampai 3.3 V**

### DTC `B2420` — [PENERANGAN (EXT) — SISTEM PENERANGAN] HL AutoLeveling ECU Failure (Dokumen: RM0000011T006RX) | [PENERANGAN (EXT) — SISTEM PENERANGAN] HL AutoLeveling ECU Failure (Dokumen: RM0000011T00CUX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [PENERANGAN (EXT)] Area Gangguan: Headlight leveling ECU assembly; Kondisi Deteksi: Malfungsi dalam headlight leveling ECU.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (PENERANGAN (EXT)) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (PENERANGAN (EXT)) — GANTI HEADLIGHT LEVELING ECU ASSEMBLY
  - Langkah 3 (PENERANGAN (EXT)) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B2450` — [PENERANGAN (EXT) — SISTEM PENERANGAN] Inisialisasi belum Dilakukan (Dokumen: RM0000011T006SX) | [PENERANGAN (EXT) — SISTEM PENERANGAN] Inisialisasi belum Dilakukan (Dokumen: RM0000011T00CVX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [PENERANGAN (EXT)] Area Gangguan: Kondisi kendaraan ketika inisialisasi Headlight leveling ECU assembly; Kondisi Deteksi: Inisialisasi pada headlight leveling ECU belum dilakukan.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (PENERANGAN (EXT)) — MELAKUKAN INISIALISASI HEADLIGHT LEVELING ECU: Lakukan inisialisasi pada headlight leveling ECU (Lihat halaman ).
  - Langkah 2 (PENERANGAN (EXT)) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (PENERANGAN (EXT)) — SELESAI
  - Langkah 4 (PENERANGAN (EXT)) — GANTI HEADLIGHT LEVELING ECU ASSEMBLY

### DTC `B2451` — [PENERANGAN (EXT) — SISTEM PENERANGAN] Spesifikasi kendaraan belum tersimpan (Dokumen: RM000002GAV04CX) | [PENERANGAN (EXT) — SISTEM PENERANGAN] Spesifikasi kendaraan belum tersimpan (Dokumen: RM000002GAV09IX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [PENERANGAN (EXT)] Area Gangguan: Headlight leveling ECU assembly; Kondisi Deteksi: Spesifikasi kendaraan belum tersimpan.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (PENERANGAN (EXT)) — GANTI HEADLIGHT LEVELING ECU ASSEMBLY: Ganti headlight leveling ECU dengan ECU lainnya yang telah menyimpan spesifikasi kendaraan (Lihat halaman ).
  - Langkah 2 (PENERANGAN (EXT)) — MELAKUKAN INISIALISASI HEADLIGHT LEVELING ECU: Lakukan inisialisasi pada headlight leveling ECU (Lihat halaman ).
  - Langkah 3 (PENERANGAN (EXT)) — SELESAI

### DTC `B2452` — [PENERANGAN (EXT) — SISTEM PENERANGAN] Height Control Sensor Diluar Range Ketika Inisialisasi (Dokumen: RM000002XGM033X) | [PENERANGAN (EXT) — SISTEM PENERANGAN] Height Control Sensor Diluar Range Ketika Inisialisasi (Dokumen: RM000002XGM05RX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [PENERANGAN (EXT)] Area Gangguan: Kondisi kendaraan ketika inisialisasi Headlight leveling ECU assembly; Kondisi Deteksi: Nilai dari rear height control sensor berada dalam range normal range ketika inisialisasi.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (PENERANGAN (EXT)) — MELAKUKAN INISIALISASI HEADLIGHT LEVELING ECU: Lakukan inisialisasi pada headlight leveling ECU (Lihat halaman ).
  - Langkah 2 (PENERANGAN (EXT)) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (PENERANGAN (EXT)) — SELESAI
  - Langkah 4 (PENERANGAN (EXT)) — GANTI HEADLIGHT LEVELING ECU ASSEMBLY

### DTC `B2453` — [PENERANGAN (EXT) — SISTEM PENERANGAN] Variation Error (Dokumen: RM000004GM6007X) | [PENERANGAN (EXT) — SISTEM PENERANGAN] Variation Error (Dokumen: RM000004GM600PX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [PENERANGAN (EXT)] Area Gangguan: Headlight leveling ECU assembly; Kondisi Deteksi: Variasi kendaraan tidak disimpan.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (PENERANGAN (EXT)) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (PENERANGAN (EXT)) — GANTI HEADLIGHT LEVELING ECU ASSEMBLY
  - Langkah 3 (PENERANGAN (EXT)) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B2780` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Tekan Switch / Switch Peringatan Kunci Unlock Malfungsi (Dokumen: RM000000Z3A00LX) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Tekan Switch / Switch Peringatan Kunci Unlock Malfungsi (Dokumen: RM000000Z3A013X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Unlock warning switch assembly Harness atau konektor Transponder key ECU assembly; Kondisi Deteksi: Unlock warning switch assembly tidak mendeteksi saat ignition switch di ON (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — MEMERIKSA UNLOCK WARNING SWITCH ASSEMBLY: Lepas unlock warning switch assembly (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HARNESS DAN KONEKTOR (UNLOCK WARNING SWITCH - TRANSPONDER KEY ECU DAN BODY GROUND): Lepas hubungan konektor G10 unlock warning switch assembly. -> Lepas hubungan konektor G26 transponder key ECU assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI TRANSPONDER KEY ECU ASSEMBLY
  - Langkah 6 (THEFT DETERRENT / KEYLESS ENTRY) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 7 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI UNLOCK WARNING SWITCH ASSEMBLY
  - Langkah 8 (THEFT DETERRENT / KEYLESS ENTRY) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: 1 - 2 (Ditekan)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: 1 - 2 (Tidak didorong)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G10-1 - G26-3 (KSW) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G10-1 atau G26-3 (KSW) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G10-2 - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `B2784` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Koil Antena Open / Short (Dokumen: RM000000Z3F00LX) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Koil Antena Open / Short (Dokumen: RM000000Z3F013X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Transponder key amplifier; Kondisi Deteksi: Antenna coil dibuat menyatu dengan transponder key amplifier open atau shorted (ditentukan oleh komunikasi dengan transponder key ECU assembly) (1 trip detection logic*). Terminal VC5, TEXT atau CODE open. Antenna coil d
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 4 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI TRANSPONDER KEY AMPLIFIER

### DTC `B2793` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Chip Transponder Malfungsi (Dokumen: RM000000Z3B00LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key; Kondisi Deteksi: Transponder chip malfungsi (1 trip detection logic*).; Kondisi Deteksi: Sebuah kunci dengan kode kunci tidak lengkap dimasukkan ke dalam ignition key cylinder (1 trip detection logic*).; Kondisi Deteksi: Kunci dengan serial number kendaraan yang berbeda dimasukkan ke dalam ignition key cylinder (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — REGISTRASI KUNCI: Hapus DTC (Lihat halaman ). -> Regristrasi kunci dan periksa bahwa mesin dapat dihidupkan dengan kunci tersebut.
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI (KODE KUNCI TIDAK REGISTRASI DENGAN NORMAL)
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI KUNCI

### DTC `B2794` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Kode Encryption tidak match (Dokumen: RM000000Z3B00LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key; Kondisi Deteksi: Transponder chip malfungsi (1 trip detection logic*).; Kondisi Deteksi: Sebuah kunci dengan kode kunci tidak lengkap dimasukkan ke dalam ignition key cylinder (1 trip detection logic*).; Kondisi Deteksi: Kunci dengan serial number kendaraan yang berbeda dimasukkan ke dalam ignition key cylinder (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — REGISTRASI KUNCI: Hapus DTC (Lihat halaman ). -> Regristrasi kunci dan periksa bahwa mesin dapat dihidupkan dengan kunci tersebut.
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI (KODE KUNCI TIDAK REGISTRASI DENGAN NORMAL)
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI KUNCI

### DTC `B2795` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Kode kunci tidak match (Dokumen: RM000000Z3B00LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key; Kondisi Deteksi: Transponder chip malfungsi (1 trip detection logic*).; Kondisi Deteksi: Sebuah kunci dengan kode kunci tidak lengkap dimasukkan ke dalam ignition key cylinder (1 trip detection logic*).; Kondisi Deteksi: Kunci dengan serial number kendaraan yang berbeda dimasukkan ke dalam ignition key cylinder (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — REGISTRASI KUNCI: Hapus DTC (Lihat halaman ). -> Regristrasi kunci dan periksa bahwa mesin dapat dihidupkan dengan kunci tersebut.
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI (KODE KUNCI TIDAK REGISTRASI DENGAN NORMAL)
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI KUNCI

### DTC `B2796` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Tidak ada Komunikasi dalam Sistem Immobiliser (Dokumen: RM000000Z3800LX) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Tidak ada Komunikasi dalam Sistem Immobiliser (Dokumen: RM000000Z38013X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key Transponder key amplifier Harness atau konektor Transponder key ECU assembly; Kondisi Deteksi: Kode kunci tidak dapat memancarkan (1 trip detection logic*).; [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key; Kondisi Deteksi: Kode kunci identifikasi tidak dapat diselesaikan dalam waktu tertentu (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (SISTEM ENGINE IMMOBILISER): Gunakan Data List untuk memeriksa bila sistem engine immobiliser berfungsi dengan baik (Lihat halaman ).
  - Langkah 4 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Periksa apakah mesin dapat dihidupkan dengan kunci kendaraan sudah terdaftar.
  - Langkah 5 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HARNESS DAN KONEKTOR (TRANSPONDER KEY ECU - TRANSPONDER KEY AMPLIFIER): Lepas hubungan konektor G26 transponder key ECU assembly. -> Lepas hubungan konektor G28 transponder key amplifier. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI TRANSPONDER KEY AMPLIFIER: Ganti sementara transponder key amplifier dengan yang baru atau yang berfungsi secara normal (Lihat halaman ).
  - Langkah 7 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN: Periksa bahwa mesin dapat dihidupkan secara normal.
  - Langkah 8 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI (TRANSPONDER KEY AMPLIFIER RUSAK)
- **Spesifikasi Standar Multimeter**:
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-14 (VC5) - G28-1 (VC5) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-15 (CODE) - G28-4 (CODE) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-4 (TXCT) - G28-5 (TXCT) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-5 (AGND) - G28-7 (AGND) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-14 (VC5) atau G28-1 (VC5) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-15 (CODE) atau G28-4 (CODE) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-4 (TXCT) atau G28-5 (TXCT) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-5 (AGND) atau G28-7 (AGND) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2797` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Malfungsi Komunikasi No. 1 (Dokumen: RM000000Z3900LX) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Malfungsi Komunikasi No. 1 (Dokumen: RM000000Z39014X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key Harness atau konektor Transponder key amplifier Transponder key ECU assembly; Kondisi Deteksi: Kunci dengan BCC malfungsi dimasukkan ke dalam ignition key cylinder (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA KUNCI: Periksa apakah ignition key yang digunakan berdekatan dengan ignition key yang lain, seperti ditunjukkan dalam gambar. Juga, periksa apakah ring kunci berhubungan dengan pegangan kunci.
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Pisahkan kunci dari yang lain, atau lepas ring kunci. -> Hapus DTC (Lihat halaman ). -> Masukan kunci ke dalam ignition key cylinder, dan kemudian cabut kunci tersebut. Ulangi kembali untuk semua kunci yang lain. -> Periksa bahwa tidak terd
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HARNESS DAN KONEKTOR (TRANSPONDER KEY ECU - TRANSPONDER KEY AMPLIFIER): Lepas hubungan konektor G26 transponder key ECU assembly. -> Lepas hubungan konektor G28 transponder key amplifier. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA TRANSPONDER KEY ECU ASSEMBLY: Menggunakan oscilloscope atau intelligent tester, periksa noise dalam bentuk gelombang antara terminal pada konektoe G28 transponder key amplifier dan konektoe G26 transponder key ECU assembly.
  - Langkah 5 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI TRANSPONDER KEY AMPLIFIER (PENGOPERASIAN): Ganti sementara transponder key amplifier dengan yang baru atau yang berfungsi secara normal (Lihat halaman ).
  - Langkah 6 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN: Periksa bahwa mesin dapat dihidupkan secara normal.
  - Langkah 7 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI (TRANSPONDER KEY AMPLIFIER RUSAK)
  - Langkah 8 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-15 (CODE) - G28-4 (CODE) (Selalu)` : **Dibawah 1 Ω**

### DTC `B2798` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Malfungsi Komunikasi No. 2 (Dokumen: RM000000Z3800LX) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Malfungsi Komunikasi No. 2 (Dokumen: RM000000Z38013X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key Transponder key amplifier Harness atau konektor Transponder key ECU assembly; Kondisi Deteksi: Kode kunci tidak dapat memancarkan (1 trip detection logic*).; [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Key; Kondisi Deteksi: Kode kunci identifikasi tidak dapat diselesaikan dalam waktu tertentu (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (SISTEM ENGINE IMMOBILISER): Gunakan Data List untuk memeriksa bila sistem engine immobiliser berfungsi dengan baik (Lihat halaman ).
  - Langkah 4 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Periksa apakah mesin dapat dihidupkan dengan kunci kendaraan sudah terdaftar.
  - Langkah 5 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HARNESS DAN KONEKTOR (TRANSPONDER KEY ECU - TRANSPONDER KEY AMPLIFIER): Lepas hubungan konektor G26 transponder key ECU assembly. -> Lepas hubungan konektor G28 transponder key amplifier. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI TRANSPONDER KEY AMPLIFIER: Ganti sementara transponder key amplifier dengan yang baru atau yang berfungsi secara normal (Lihat halaman ).
  - Langkah 7 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN: Periksa bahwa mesin dapat dihidupkan secara normal.
  - Langkah 8 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI (TRANSPONDER KEY AMPLIFIER RUSAK)
- **Spesifikasi Standar Multimeter**:
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-14 (VC5) - G28-1 (VC5) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-15 (CODE) - G28-4 (CODE) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-4 (TXCT) - G28-5 (TXCT) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-5 (AGND) - G28-7 (AGND) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-14 (VC5) atau G28-1 (VC5) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-15 (CODE) atau G28-4 (CODE) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-4 (TXCT) atau G28-5 (TXCT) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-5 (AGND) atau G28-7 (AGND) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2799` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Sistem Engine Immobiliser Malfungsi (Dokumen: RM000000Z3D00SX) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Sistem Engine Immobiliser Malfungsi (Dokumen: RM000000Z3D01EX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Harness atau konektor Transponder key ECU assembly ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — REREGISRASI ECU COMMUNICATION ID: Reregister ECU - ECM communication ID (Lihat Buletin Layanan).
  - Langkah 4 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 5 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 6 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HUBUNGAN KONEKTOR: Putar ignition switch ke off. -> Periksa apakah konektor terhubung dengan benar ke ECM dan transponder key ECU assembly.
  - Langkah 7 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HARNESS DAN KONEKTOR (SFI ATAU ECD COMMUNICATION LINE): Lepas hubungan konektor G26 transponder key ECU assembly. -> Lepas hubungan konektor G38*1 atau G88*2 ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI ECM: Ganti sementara ECM dengan yang baru.
- **Spesifikasi Standar Multimeter**:
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) - G38-30 (IMI) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-12 (EFII) - G38-29 (IMO) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) atau G38-30 (IMI) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-12 (EFII) atau G38-29 (IMO) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) - G88-16 (IMI) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-12 (EFII) - G88-15 (IMO) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) atau G88-16 (IMI) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-12 (EFII) atau G88-15 (IMO) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B279A` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] High Fixation Line Komunikasi Sistem Anti Pencurian (Dokumen: RM000002X2F02JX) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] High Fixation Line Komunikasi Sistem Anti Pencurian (Dokumen: RM000002X2F04LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: Harness atau konektor Transponder key ECU assembly ECM; Kondisi Deteksi: Communication line (EFIO-IMI) antara ECM dan transponder key ECU assembly macet pada HI output (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HARNESS DAN KONEKTOR (SFI ATAU ECD COMMUNICATION LINE): Lepas hubungan konektor G26 transponder key ECU assembly. -> Lepas hubungan konektor G38*1 atau G88*2 ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA TRANSPONDER KEY ECU ASSEMBLY (TERMINAL EFIO): Gunakaan oscilloscope, periksa bentuk gelombang.
  - Langkah 5 (THEFT DETERRENT / KEYLESS ENTRY) — PERIKSA HARNESS DAN KONEKTOR (ECU KUNCI TRANSPONDER - BATERAI DAN BODY GROUND): Lepas hubungan konektor G26 transponder key ECU assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI ECM: Ganti sementara ECM dengan yang baru.
  - Langkah 7 (THEFT DETERRENT / KEYLESS ENTRY) — REGRISTRASI ULANG ID KOMUNIKASI ECU: Reregister ECU - ECM communication ID (Lihat Buletin Layanan).
  - Langkah 8 (THEFT DETERRENT / KEYLESS ENTRY) — HAPUS DTC: Hapus DTC (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) - G38-30 (IMI) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) atau G38-30 (IMI) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) - G88-16 (IMI) (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-13 (EFIO) atau G88-16 (IMI) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Voltase Standar: G26-13 (EFIO) atau G38-30 (IMI) - Body ground (Selalu)` : **Dibawah 1 V**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Voltase Standar: G26-13 (EFIO) atau G88-16 (IMI) - Body ground (Selalu)` : **Dibawah 1 V**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Tahanan Standar: G26-16 (GND) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[THEFT DETERRENT / KEYLESS ENTRY] Voltase Standar: G26-1 (+B) - Body ground (Selalu)` : **11 sampai 14 V**

### DTC `B279C` — [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Deteksi Adanya Sistem Anti Pencurian (Dokumen: RM000003SC5006X) | [THEFT DETERRENT / KEYLESS ENTRY — ENGINE IMMOBILISER SYSTEM] Deteksi Adanya Sistem Anti Pencurian (Dokumen: RM000003SC500UX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [THEFT DETERRENT / KEYLESS ENTRY] Area Gangguan: ECM; Kondisi Deteksi: ECM yang tidak sesuai dengan sistem engine immobiliser dipasang (1 trip detection logic*).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (THEFT DETERRENT / KEYLESS ENTRY) — GANTI ECM YANG ADA DENGAN ECM YANG TEPAT: Ganti arus ECM dengan ECM pantas.
  - Langkah 2 (THEFT DETERRENT / KEYLESS ENTRY) — SELESAI

### DTC `C0200` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 31] Sirkuit Speed Sensor Depan RH (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 31] Front Speed Sensor RH Circuit (Dokumen: RM000000XI90HLX) | [SISTEM KONTROL REM / KONTROL DINAMIS — 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C0205` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 32] Sirkuit Speed Sensor Depan LH (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 32] Front Speed Sensor LH Circuit (Dokumen: RM000000XI90HLX) | [SISTEM KONTROL REM / KONTROL DINAMIS — 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C0210` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 33] Sirkuit Speed Sensor Belakang RH (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 33] Rear Speed Sensor RH Circuit (Dokumen: RM000000XIA0D7X) | [SISTEM KONTROL REM / KONTROL DINAMIS 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C0215` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 34] Sirkuit Speed Sensor Belakang LH (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 34] Rear Speed Sensor LH Circuit (Dokumen: RM000000XIA0D7X) | [SISTEM KONTROL REM / KONTROL DINAMIS 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C0226` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 21] Sirkuit Solenoid SFR (Dokumen: RM000000XI80A8X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 21] SFR Solenoid Circuit (Dokumen: RM000000XI80AAX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SY
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SFRR atau SFRH) Aktuator rem assembly; Kondisi Deteksi: Open circuit atau short circuit dalam sirkuit solenoid berlanjut selama 0.05 detik atau lebih.; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SFLR atau SFLH) Aktuator rem assembly; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SRRR atau SRRH) Aktuator rem assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih. -> Periksa apakah DTC yang sama di-output (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DINAMIS) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DINAMIS) — GANTI BRAKE ACTUATOR ASSEMBLY

### DTC `C0236` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 22] Sirkuit Solenoid SFL (Dokumen: RM000000XI80A8X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 22] SFL Solenoid Circuit (Dokumen: RM000000XI80AAX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SY
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SFRR atau SFRH) Aktuator rem assembly; Kondisi Deteksi: Open circuit atau short circuit dalam sirkuit solenoid berlanjut selama 0.05 detik atau lebih.; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SFLR atau SFLH) Aktuator rem assembly; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SRRR atau SRRH) Aktuator rem assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih. -> Periksa apakah DTC yang sama di-output (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DINAMIS) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DINAMIS) — GANTI BRAKE ACTUATOR ASSEMBLY

### DTC `C0246` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 23] Sirkuit Solenoid SRR (Dokumen: RM000000XI80A8X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 23] SRR Solenoid Circuit (Dokumen: RM000000XI80AAX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SY
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SFRR atau SFRH) Aktuator rem assembly; Kondisi Deteksi: Open circuit atau short circuit dalam sirkuit solenoid berlanjut selama 0.05 detik atau lebih.; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SFLR atau SFLH) Aktuator rem assembly; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit solenoid (SRRR atau SRRH) Aktuator rem assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih. -> Periksa apakah DTC yang sama di-output (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DINAMIS) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DINAMIS) — GANTI BRAKE ACTUATOR ASSEMBLY

### DTC `C0273` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 13] Membuka Sirkuit Relay Motor ABS (Dokumen: RM000001JD608JX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 13] Membuka Sirkuit Relay Motor ABS (Dokumen: RM000001JD608LX) | [SISTEM KONTROL REM / KONTROL DINAMI
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Fuse ABS NO.1 Sirkuit relay motor ABS Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit relay motor ABS Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Ketika motor relay OFF, relay VSC NO.2 tetap tertutup selama 4 detik atau lebih.; [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: Fuse ABS NO. 1 Sirkuit ABS motor relay 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (RELAY MOTOR ABS): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Active Test. -> Periksa suara kerja dari relay motor ABS ketika m
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL ECU (TERMINAL +BM): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT MASA): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-23 (+BM) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-2 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-24 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-23 (+BM) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-2 (GND1) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-24 (GND2) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `C0274` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 14] Short ke B+ pada Sirkuit Relay Motor ABS (Dokumen: RM000001JD608JX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 14] Short ke B+ pada Sirkuit ABS Motor Relay (Dokumen: RM000001JD608LX) | [SISTEM KONTROL RE
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Fuse ABS NO.1 Sirkuit relay motor ABS Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit relay motor ABS Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Ketika motor relay OFF, relay VSC NO.2 tetap tertutup selama 4 detik atau lebih.; [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: Fuse ABS NO. 1 Sirkuit ABS motor relay 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (RELAY MOTOR ABS): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Active Test. -> Periksa suara kerja dari relay motor ABS ketika m
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL ECU (TERMINAL +BM): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT MASA): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-23 (+BM) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-2 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-24 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-23 (+BM) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-2 (GND1) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-24 (GND2) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `C0278` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 11] Membuka Solenoid ABS Relay Circuit (Dokumen: RM000000XI708FX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 11] Open in ABS Solenoid Relay Circuit (Dokumen: RM000000XI708HX) | [SISTEM KONTROL REM / KONTROL 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Fuse ABS NO.2 Solenoid ABS relay circuit Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Solenoid ABS relay circuit Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Dengan segera setelah ignition switch diputar keON, hubungan solenoid relay ditutup selama 0.2 detik ketika relay diputar ke off.; [SISTEM KONTROL REM / KONTROL DINAMIS]
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL (TERMINAL +BS): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT MASA): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — PERIKAS VOLTASE TERMINAL (TERMINAL +BS): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (brake actuator assembly). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-1 (+BS) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-2 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-24 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-1 (+BS) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-2 (GND1) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-24 (GND2) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `C0279` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 12] Short pada B+ dalam Solenoid ABS Relay Circuit (Dokumen: RM000000XI708FX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 12] Short pada B+ dalam Solenoid ABS Relay Circuit (Dokumen: RM000000XI708HX) | [SISTE
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Fuse ABS NO.2 Solenoid ABS relay circuit Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Solenoid ABS relay circuit Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Dengan segera setelah ignition switch diputar keON, hubungan solenoid relay ditutup selama 0.2 detik ketika relay diputar ke off.; [SISTEM KONTROL REM / KONTROL DINAMIS]
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL (TERMINAL +BS): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT MASA): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — PERIKAS VOLTASE TERMINAL (TERMINAL +BS): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (brake actuator assembly). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-1 (+BS) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-2 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-24 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-1 (+BS) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-2 (GND1) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-24 (GND2) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `C1235` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 35] Benda Asing Menempel pada Ujung Speed Sensor Depan RH (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 35] Benda Asing Menempel pada Ujung Front Speed Sensor RH (Dokumen: RM000000XI9
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1236` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 36] Benda Asing Menempel pada Ujung Speed Sensor Depan LH (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 36] Benda Asing Menempel pada Ujung Front Speed Sensor LH (Dokumen: RM000000XI9
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1238` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 38] Benda Asing Menempel pada Ujung Speed Sensor Belakang RH (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 38] Benda Asing Menempel pada Ujung Rear Speed Sensor RH (Dokumen: RM000000X
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1239` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 39] Benda Asing Menempel pada Ujung Speed Sensor Belakang LH (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 39] Benda Asing Menempel pada Ujung Rear Speed Sensor LH (Dokumen: RM000000X
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1241` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 41] Tegangan Positif Baterai Lemah atau Tinggi Tegangan Positif Baterai Abnormal (Dokumen: RM000000XW60ASX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 41] Voltase Positif Baterai Lemah atau Tinggi Voltase Po
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Fuse ECU-IG&GAUGE Baterai Sistem pengisian Sirkuit power source Sirkuit internal power supply dari skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: ECU-IG fuse NO. 2 Baterai Sistem pengisian Sirkuit power source Sirkuit internal power supply dari skid control ECU (Brake actuator assembly)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA BATERAI: Periksa tegangan baterai.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL (TERMINAL IG1): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT MASA): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA ATAU GANTI BATERAI ATAU SISTEM PENGISIAN
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-25 (IG1) - Masa bodi (ignition switch ON)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-2 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-24 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-25 (IG1) - Body ground (Ignition switch ON)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-2 (GND1) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-24 (GND2) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `C1243` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 43] Malfungsi Macet dari Decelation Sensor (Dokumen: RM000001FZV00JX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 43] Deceleration Sensor Stuck Malfunction (Dokumen: RM000001FZV00LX) | [SISTEM KONTROL REM / K
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Ketika kecepatan kendaraan menurun dari 30 km/jam (18 mph) ke 0 km/jam (0 mph), sinyal sensor tidak berubah 16 kali atau lebih.; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Pemasangan sensor Skid control ECU (Aktuator rem assem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (DECELERATION SENSOR 1): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List. -> Periksa bahwa nilai deselerasi dari de
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 30 km/h (18 mph) atau lebih selama 60 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA DECELERATION SENSOR: Putar ignition switch ke off. -> Lepas deceleration sensor (Lihat halaman ). -> Periksa deceleration sensor (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SKID CONTROL ECU - DECELERATION SENSOR): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Lepas hubungan konektor deceleration sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI DECELERATION SENSOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - K5-2 (GGND) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - K5-1 (GL1) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1244` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 44] Open atau Short dalam Sirkuit Deceleration Sensor (Dokumen: RM000001FZV00JX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 44] Open or Short in Deceleration Sensor Circuit (Dokumen: RM000001FZV00LX) | [SIST
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Ketika kecepatan kendaraan menurun dari 30 km/jam (18 mph) ke 0 km/jam (0 mph), sinyal sensor tidak berubah 16 kali atau lebih.; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Pemasangan sensor Skid control ECU (Aktuator rem assem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (DECELERATION SENSOR 1): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List. -> Periksa bahwa nilai deselerasi dari de
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 30 km/h (18 mph) atau lebih selama 60 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA DECELERATION SENSOR: Putar ignition switch ke off. -> Lepas deceleration sensor (Lihat halaman ). -> Periksa deceleration sensor (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SKID CONTROL ECU - DECELERATION SENSOR): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Lepas hubungan konektor deceleration sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI DECELERATION SENSOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - K5-2 (GGND) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - K5-1 (GL1) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1245` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 45] Malfungsi Output dari Deceleration Sensor (Dokumen: RM000001FZV00JX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 45] Deceleration Sensor Output Malfunction (Dokumen: RM000001FZV00LX) | [SISTEM KONTROL REM
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Ketika kecepatan kendaraan menurun dari 30 km/jam (18 mph) ke 0 km/jam (0 mph), sinyal sensor tidak berubah 16 kali atau lebih.; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Pemasangan sensor Skid control ECU (Aktuator rem assem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (DECELERATION SENSOR 1): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List. -> Periksa bahwa nilai deselerasi dari de
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 30 km/h (18 mph) atau lebih selama 60 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA DECELERATION SENSOR: Putar ignition switch ke off. -> Lepas deceleration sensor (Lihat halaman ). -> Periksa deceleration sensor (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SKID CONTROL ECU - DECELERATION SENSOR): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Lepas hubungan konektor deceleration sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI DECELERATION SENSOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - K5-2 (GGND) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - K5-1 (GL1) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1248` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 48] Open Circuit dalam Rear Differential Lock (Dokumen: RM000001L4900LX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 48] Open Circuit in Rear Differential Lock (Dokumen: RM000001L4900MX) | [SISTEM KONTROL REM
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit terminal EXI2 Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: DTC ini mungkin disimpan karena terdapat malfungsi pada sirkuit terminal EXI2.; [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: Sirkuit terminal EXI2 Skid control ECU (Brake actuator assembly); Kondisi Deteksi: DTC ini mungkin menyimpan akibat terjadi malfungsi sirkuit terminal EXI2.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL (TERMINAL EXI2): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 50 km/h (31 mph) atau lebih selama 3 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — PERIKSA VOLTASE TERMINAL (TERMINAL EXI2): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (brake actuator assembly). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DINAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 50 km/jam (31 mph) atau lebih selama 3 detik atau lebih. -> Periksa apakah DTC yang sama di-output (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DINAMIS) — GANTI BRAKE ACTUATOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-22 (EXI2) - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-22 (EXI2) - Body ground (Ignition switch ON)` : **11 sampai 14 V**

### DTC `C1249` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 49] Open pada Sirkuit Stop Light Switch (Dokumen: RM000000XIE0DYX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 49] Open pada Sirkuit Stop Light Switch (Dokumen: RM000000XIE0E0X) | [SISTEM KONTROL REM / KONTRO
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sirkuit stop light switch Sirkuit lampu rem LH dan RH Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: Sirkuit stop light switch Sirkuit stop light LH dan RH Skid control ECU (Brake actuator assembly)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA KERJA LAMPU REM: Periksa bahwa lampu rem LH dan RH menyala ketika pedal rem diinjak, dan padam ketika pedal dibebaskan.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (STOP LIGHT SW): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List. -> Menggunakan intelligent tester, periks
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL (TERMINAL STP): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LANJUTKAN KE SISTEM PENERANGAN (TABEL GEJALA PROBLEM)
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] OK: Pedal rem ditekan` : **On**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] OK: Pedal rem dibebaskan` : **Off**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-10 (STP) - Masa bodi (Pedal rem ditekan)` : **8 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-10 (STP) - Masa bodi (Pedal rem dibebaskan)` : **Di bawah 1,5 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] OK: Brake pedal ditekan` : **On**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] OK: Brake pedal dibebaskan` : **Off**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-10 (STP) - Body ground (Brake pedal ditekan)` : **8 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-10 (STP) - Body ground (Brake pedal dibebaskan)` : **Dibawah 1.5 V**

### DTC `C1251` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 51] Open pada Sirkuit Pump Circuit (Dokumen: RM000000XIF08SX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 51] Open pada Sirkuit Pump Motor (Dokumen: RM000000XIF08UX) | [SISTEM KONTROL REM / KONTROL DINAMIS — 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Aktuator rem assembly (Sirkuit masa) Aktuator rem assembly (Motor circuit); [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: Brake actuator assembly (Sirkuit ground) Brake actuator assembly (Sirkuit motor)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (RELAY MOTOR ABS): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Active Test. -> Periksa suara kerja dari relay motor ABS ketika m
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT MASA): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/h (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (ABS MOTOR RELAY): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Active Test. -> Periksa suara kerja dari relay motor ABS ketika 
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DINAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT GROUND): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (brake actuator assembly). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-2 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-24 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-2 (GND1) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-24 (GND2) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `C1271` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 71] Sinyal Output Speed Sensor Depan RH Lemah (Test Mode DTC) (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 71] Sinyal Output Front Speed Sensor RH Lemah (Test Mode DTC) (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1272` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 72] Sinyal Output Speed Sensor Depan LH Lemah (Test Mode DTC) (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 72] Sinyal Output Front Speed Sensor LH Lemah (Test Mode DTC) (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1273` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 73] Sinyal Output Lemah dari Speed Sensor Belakang RH (Test Mode DTC) (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 73] Sinyal Output Lemah dari Rear Speed Sensor RH (Test Mode DTC) (
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1274` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 74] Sinyal Output Lemah dari Speed Sensor Belakang LH (Test Mode DTC) (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 74] Sinyal Output Lemah dari Rear Speed Sensor LH (Test Mode DTC) (
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1275` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 75] Perubahan Abnormal dalam Sinyal Output Speed Sensor Depan RH (Test Mode DTC) (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 75] Perubahan Abnormal dalam Sinyal Output Front Speed S
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1276` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 76] Perubahan Abnormal dalam Sinyal Output Speed Sensor Depan LH (Test Mode DTC) (Dokumen: RM000000XI90HJX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 76] Perubahan Abnormal dalam Sinyal Output Front Speed S
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Front skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor depan Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Front skid control rotor 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (FR/FL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam Prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa konektor skid control ECU (aktuator rem assembly) dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar ignition switch ke off. -> Periksa pemasangan speed sensor (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR ROTOR DEPAN: Putar ignition switch ke off. -> Lepas speed sensor depan (untuk 2WD: Lihat halaman , untuk 4WD dan Pre-Runner: Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - A12-1 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-9 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - A12-2 (FL-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-8 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - A11-1 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-31 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - A11-2 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-30 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1277` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 77] Perubahan Abnormal dalam Sinyal Output Speed Sensor Belakang RH (Test Mode DTC) (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 77] Perubahan Abnormal dalam Sinyal Output Rear Speed
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1278` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 78] Perubahan Abnormal dalam Sinyal Output Speed Sensor Belakang LH (Test Mode DTC) (Dokumen: RM000000XIA0D5X) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 78] Perubahan Abnormal dalam Sinyal Output Rear Speed
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Rear skid control rotor RH/LH Pemasangan sensor Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Sirkuit speed sensor belakang Pemasangan sensor; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Speed sensor belakang RH/LH Pemasangan sensor Rear skid c
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa dari kemungkinan adanya pemutusan sesaat dalam wire harness dan konektor yang terkait dengan DTC (Lihat halaman ).
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (RR/RL WHEEL SPEED): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Hidupkan intelligent tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List, dan kemudian jalankan kendaraan. -> Periksa bahwa outp
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LAKUKAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA BAHWA KONEKTOR SKID CONTROL ECU DAN SPEED SENSOR BELAKANG TELAH DIHUBUNGKAN DENGAN SEMPURNA: Periksa bahwa skid control ECU (aktuator rem assembly) dan konektor speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Periksa pemasangan speed sensor belakang (Lihat halaman ).
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA UJUNG SPEED SENSOR BELAKANG: Putar ignition switch ke off. -> Lepas speed sensor belakang (Lihat halaman ). -> Periksa ujung speed sensor.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - L3-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-11 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - L3-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-12 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - L7-2 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-33 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - L7-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-34 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1279` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 79] Malfungsi Tegangan Output Deceleration Sensor (Test Mode DTC) (Dokumen: RM000001FZV00JX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 79] Deceleration Sensor Output Voltage Malfunction (Test Mode DTC) (Dok
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Ketika kecepatan kendaraan menurun dari 30 km/jam (18 mph) ke 0 km/jam (0 mph), sinyal sensor tidak berubah 16 kali atau lebih.; [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Deceleration sensor Sirkuit deceleration sensor Pemasangan sensor Skid control ECU (Aktuator rem assem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (DECELERATION SENSOR 1): Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / ABS/VSC/TRC / Data List. -> Periksa bahwa nilai deselerasi dari de
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 30 km/h (18 mph) atau lebih selama 60 detik atau lebih. -> Periksa apakah DTC yang sama muncul (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA DECELERATION SENSOR: Putar ignition switch ke off. -> Lepas deceleration sensor (Lihat halaman ). -> Periksa deceleration sensor (Lihat halaman ).
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SKID CONTROL ECU - DECELERATION SENSOR): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Lepas hubungan konektor deceleration sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI DECELERATION SENSOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-28 (VGS) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - K5-2 (GGND) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-7 (GGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - K5-1 (GL1) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-4 (GL1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - K5-3 (VGS) (Selalu)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-28 (VGS) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1282` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 82] Malfungsi Switch Posisi Center Differential Lock (Test Mode DTC) (Dokumen: RM000003NTU00IX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 82] Center Differential Lock Position Switch Malfunction (Test Mode 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Sistem transfer Harness atau konektor Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Pendeteksian hanya selama Test Mode.; [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: Sistem transfer Harness atau konektor Skid control ECU (Brake actuator assembly)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA TAGANGAN TERMINAL (TERMINAL EXI): Atur kendaraan ke status 4WD menggunakan transfer shift lever. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan konektor skid control ECU (akt
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PEMERIKSAAN TEST MODE DTC: Switch kendaraan ke Test Mode, lakukuan pemeriksaan pengoperasian shift H2 ke L4, dan periksa bahwa DTC C1282/82 is tidak disimpan (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT EXI): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Lepas hubungan konektor 4WD detection switch (differential vacuum actuator assembly). -> Lepas hubungan konektor 4 wheel drive control ECU.
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — LANJUTKAN KE SISTEM TRANSFER (TABEL GEJALA PROBLEM)
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — PERIKSA VOLTASE TERMINAL (TERMINAL EXI): Atur kendaraan ke center differential lock state menggunakan transfer shift lever. -> Lepas hubungan konektor skid control ECU (brake actuator assembly). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan konektor
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-17 (EXI) - Masa bodi (Ignition switch ON Posisi shift transfer H4)` : **Di bawah 1,5 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tegangan Standar: A13-17 (EXI) - Masa bodi (Ignition switch ON Posisi shift transfer H2)` : **11 sampai 14 V**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-17 (EXI) - C31-3 (ADD) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-17 (EXI) - C37-8 (ADD) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-17 (EXI) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: C31-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-17 (EXI) - Body ground (Ignition switch ON Transfer shift position HL)` : **Dibawah 1.5 V**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Voltase Standar: A13-17 (EXI) - Body ground (Ignition switch ON Transfer shift position H)` : **11 sampai 14 V**

### DTC `C1283` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 83] Malfungsi Switch Posisi L4 (Test Mode DTC) (Dokumen: RM000003NTS00NX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 83] L4 Position Switch Malfunction (Test Mode DTC) (Dokumen: RM000003NTS00OX) | [SISTEM KO
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: L4 position switch (switch indikator transfer No. 1) Sirkuit terminal EXI4 Skid control ECU (Aktuator rem assembly); Kondisi Deteksi: Tidak ada sinyal yang di-input ke terminal EXI4 dari skid control ECU.; [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: LL position switch (transfer indicator switch No. 1) Sirkuit terminal EXI4 Skid control ECU (Brake actuator assembly); Kondisi Deteksi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PEMERIKSAAN SIRKUIT TERMINAL EXI4: Atur kendaraan ke status l4 menggunakan transfer shift lever. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan konektor skid control ECU (aktua
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PEMERIKSAAN TEST MODE DTC: Switch kendaraan ke Test Mode, lakukuan pemeriksaan pengoperasian shift H2 ke L4, dan periksa bahwa DTC C1283/83 is tidak disimpan (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT TERMINAL EXI4): Putar ignition switch ke off. -> Lepas hubungan konektor skid control ECU (aktuator rem assembly) -> Lepas hubungan konektorL4 position switch (No. 1 transfer indicator switch). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah in
  - Langkah 4 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — MEMERIKSA L4 POSITION SWITCH: Putar ignition switch ke off. -> Lepas L4 position switch (No. 1 transfer indicator switch) (Lihat halaman ). -> Periksa L4 position switch (No. 1 transfer indicator switch) (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 7 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI SWITCH INDIKATOR TRANSFER NO.1
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-3 (EXI4) - Masa bodi (Posisi shift transfer L4)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-3 (EXI4) - Masa bodi (Posisi shift transfer H2)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-3 (EXI4) - C29-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: A13-3 (EXI4) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DIMANAMIS] Tahanan Standar: C29-2 - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-3 (EXI4) - Body ground (Transfer shift position LL)` : **Dibawah 1 Ω**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-3 (EXI4) - Body ground (Transfer shift position H)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL REM / KONTROL DINAMIS] Tahanan Standar: A13-3 (EXI4) - C29-1 (Selalu)` : **Dibawah 1 Ω**

### DTC `C1337` — [SISTEM KONTROL REM / KONTROL DIMANAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 37] Diameter Ban tidak seragam (Dokumen: RM00000104I01NX) | [SISTEM KONTROL REM / KONTROL DINAMIS — ANTI-LOCK BRAKE SYSTEM / Flash Code 37] Diameter semua ban adalah tidak sama (Dokumen: RM00000104I01PX) | [SISTEM KONTROL REM / KONTROL DINAMI
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL REM / KONTROL DIMANAMIS] Area Gangguan: Ukuran ban Skid control ECU (Aktuator rem assembly); [SISTEM KONTROL REM / KONTROL DINAMIS] Area Gangguan: Ukuran ban Skid control ECU (Brake actuator assembly)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — PEMERIKSAAN UKURAN BAN: Periksa diameter semua 4 ban.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI BAN DENGAN 4 BAN BERUKURAN SAMA SEMUA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DIMANAMIS) — GANTI ACTUATOR REM ASSEMBLY
  - Langkah 1 (SISTEM KONTROL REM / KONTROL DINAMIS) — PERIKSA UKURAN BAN: Periksa diameter semua 4 ban.
  - Langkah 2 (SISTEM KONTROL REM / KONTROL DINAMIS) — GANTI BAN DENGAN 4 BAN BERUKURAN SAMA SEMUA
  - Langkah 3 (SISTEM KONTROL REM / KONTROL DINAMIS) — GANTI BRAKE ACTUATOR ASSEMBLY

### DTC `CB-10` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] System Microcomputer Malfunction (Dokumen: RM000003XYR02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] System Microcomputer Malfunction (Dokumen: RM000003XYR02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Rad
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: - "iPod" atau peralatan USB Radio penerima assembly; Kondisi Deteksi: System microcomputer malfungsi; Kondisi Deteksi: Sebuah malfungsi pada media interface microcomputer.; Kondisi Deteksi: Sebuah malfungsi pada CD-LSI (large scale integration).; [AUDIO / VIDEO] Area Gangguan: Perlengkapan USB atau "iPod" Radio receiver assembly; Kondisi Deteksi: Malfungsi sistem microcomputer.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan perlengkapan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB atau "iPod" ke stereo jack adapter.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (USB DEVICE ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-11` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] Media Interface Microcomputer Malfunction (Dokumen: RM000003XYR02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] Media Interface Microcomputer Malfunction (Dokumen: RM000003XYR02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISU
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: - "iPod" atau peralatan USB Radio penerima assembly; Kondisi Deteksi: System microcomputer malfungsi; Kondisi Deteksi: Sebuah malfungsi pada media interface microcomputer.; Kondisi Deteksi: Sebuah malfungsi pada CD-LSI (large scale integration).; [AUDIO / VIDEO] Area Gangguan: Perlengkapan USB atau "iPod" Radio receiver assembly; Kondisi Deteksi: Malfungsi sistem microcomputer.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan perlengkapan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB atau "iPod" ke stereo jack adapter.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (USB DEVICE ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-12` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] CD-LSI Malfunction (Dokumen: RM000003XYR02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD-LSI Malfunction (Dokumen: RM000003XYR02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] CD-LSI Malfunc
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: - "iPod" atau peralatan USB Radio penerima assembly; Kondisi Deteksi: System microcomputer malfungsi; Kondisi Deteksi: Sebuah malfungsi pada media interface microcomputer.; Kondisi Deteksi: Sebuah malfungsi pada CD-LSI (large scale integration).; [AUDIO / VIDEO] Area Gangguan: Perlengkapan USB atau "iPod" Radio receiver assembly; Kondisi Deteksi: Malfungsi sistem microcomputer.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan perlengkapan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB atau "iPod" ke stereo jack adapter.
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (USB DEVICE ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-13` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] USB Over Current Detection (Dokumen: RM000003XYS02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] USB Over Current Detection (Dokumen: RM000003XYS02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: - "iPod" atau peralatan USB Harness atau konektor Stereo jack adapter No. 1 assembly Radio penerima assembly; Kondisi Deteksi: Sebuah malfungsi arus berlebihan pada "iPod" atau peralatan USB; [AUDIO / VIDEO] Area Gangguan: Perlengkapan USB atau "iPod" Harness atau konektor Stereo jack adapter assembly No. 1 Radio receiver assembly; Kondisi Deteksi: Malfungsi arus berlebih pada perangkat USB atau "iPod"
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — PERALATAN USB ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — PERIKSA RADIO PENERIMA ASSEMBLY: Lepas hubungan konektor z1 stereo jack adapter assembly No. 1. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (AUDIO / VIDEO) — GANTI STEREO JACK ADAPTER ASSEMBLY NO. 1
  - Langkah 6 (AUDIO / VIDEO) — PERIKSA HARNESS DAN KONEKTOR (RADIO PENERIMA - STEREO JACK ADAPTER): Lepas hubungan konektor z2 radio penerima assembly. -> Lepas hubungan konektor z1 stereo jack adapter assembly No. 1. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 8 (AUDIO / VIDEO) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[AUDIO / VIDEO] Tegangan Standar: z1-1 (UPI) - z1-4 (UJSG) (Selalu)` : **4.5 sampai 5.5 V**
  - `[AUDIO / VIDEO] Tahanan Standar: z2-1 (USV1) - z1-1 (UPI) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: z2-4 (UGD1) - z1-4 (UJSG) (Selalu)` : **Di bawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: z2-1 (USV1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Tahanan Standar: z2-4 (UGD1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUDIO / VIDEO] Voltase Standar: z1-1 (UPI) - z1-4 (UJSG) (Selalu)` : **4.5 sampai 5.5 V**
  - `[AUDIO / VIDEO] Tahanan Standar: z2-1 (USV1) - z1-1 (UPI) (Selalu)` : **Dibawah 1 Ω**
  - `[AUDIO / VIDEO] Tahanan Standar: z2-4 (UGD1) - z1-4 (UJSG) (Selalu)` : **Dibawah 1 Ω**

### DTC `CB-43` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] USB Device Class/Protocol Error (Dokumen: RM000003XYT02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] USB Device Class/Protocol Error (Dokumen: RM000003XYT02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Terhubung dengan non-mass-storage class atau peralatan USB dengan sebuah protocol yang tidak kompatibel.; Kondisi Deteksi: Terhubung dengan sebuah sistem file yang tidak kompatibel atau peralatan USB dengan corrupted atau incompatible File Allocation Table (FAT).; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi "iPod"; 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT PERALATAN USB TIDAK KOMPATIBEL, VERSI "iPod" TIDAK SESUAI, ATAU PERALATAN USB ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT USB DEVICE TIDAK SESUAI, VERSI "iPod" TIDAK SESUAI, ATAU USB DEVICE ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-44` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] USB File System Error (Dokumen: RM000003XYT02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] USB File System Error (Dokumen: RM000003XYT02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] USB File
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Terhubung dengan non-mass-storage class atau peralatan USB dengan sebuah protocol yang tidak kompatibel.; Kondisi Deteksi: Terhubung dengan sebuah sistem file yang tidak kompatibel atau peralatan USB dengan corrupted atau incompatible File Allocation Table (FAT).; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi "iPod"; 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT PERALATAN USB TIDAK KOMPATIBEL, VERSI "iPod" TIDAK SESUAI, ATAU PERALATAN USB ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT USB DEVICE TIDAK SESUAI, VERSI "iPod" TIDAK SESUAI, ATAU USB DEVICE ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-45` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] USB Communication Error (Dokumen: RM000003XYU02MX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] USB Communication Error (Dokumen: RM000003XYU02OX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] USB 
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Error komunikasi dengan peralatan USB.; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi software kontrol "iPod".; Kondisi Deteksi: Error komunikasi dengan "iPod".; [AUDIO / VIDEO] Area Gangguan: USB device Radio receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (USB DEVICE ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-46` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] iPod Control Error (Dokumen: RM000003XYU02MX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Control Error (Dokumen: RM000003XYU02OX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Control E
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Error komunikasi dengan peralatan USB.; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi software kontrol "iPod".; Kondisi Deteksi: Error komunikasi dengan "iPod".; [AUDIO / VIDEO] Area Gangguan: USB device Radio receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (USB DEVICE ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-47` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] iPod Communication Error (Dokumen: RM000003XYU02MX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Communication Error (Dokumen: RM000003XYU02OX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iP
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Error komunikasi dengan peralatan USB.; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi software kontrol "iPod".; Kondisi Deteksi: Error komunikasi dengan "iPod".; [AUDIO / VIDEO] Area Gangguan: USB device Radio receiver assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — SELESAI (USB DEVICE ATAU "iPod" RUSAK)
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-50` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] iPod Malfunction (Dokumen: RM000003XYT02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Malfunction (Dokumen: RM000003XYT02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Malfunction (
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Terhubung dengan non-mass-storage class atau peralatan USB dengan sebuah protocol yang tidak kompatibel.; Kondisi Deteksi: Terhubung dengan sebuah sistem file yang tidak kompatibel atau peralatan USB dengan corrupted atau incompatible File Allocation Table (FAT).; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi "iPod"; 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT PERALATAN USB TIDAK KOMPATIBEL, VERSI "iPod" TIDAK SESUAI, ATAU PERALATAN USB ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT USB DEVICE TIDAK SESUAI, VERSI "iPod" TIDAK SESUAI, ATAU USB DEVICE ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-51` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] iPod Protocol Error (Dokumen: RM000003XYT02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Protocol Error (Dokumen: RM000003XYT02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Protoco
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Terhubung dengan non-mass-storage class atau peralatan USB dengan sebuah protocol yang tidak kompatibel.; Kondisi Deteksi: Terhubung dengan sebuah sistem file yang tidak kompatibel atau peralatan USB dengan corrupted atau incompatible File Allocation Table (FAT).; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi "iPod"; 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT PERALATAN USB TIDAK KOMPATIBEL, VERSI "iPod" TIDAK SESUAI, ATAU PERALATAN USB ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT USB DEVICE TIDAK SESUAI, VERSI "iPod" TIDAK SESUAI, ATAU USB DEVICE ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-52` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] No Playable iPod File Exists (Dokumen: RM000003XYV02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] No Playable iPod File Exists (Dokumen: RM000003XYV02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Recei
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Tidak ada file yang dapat dimainkan pada "iPod".; [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Tidak ada file yang dapat dimainkan pada peralatan USB.; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio receiver assembly; Kondisi Deteksi: Tidak ada file dimainkan pada "iPod".
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Periksa apakah file-file yang dapat dimainkan terdapat pada peralatan USB atau "iPod".
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assembly.
  - Langkah 4 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 5 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 6 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Periksa file yang dimainkan present pada USB device atau "iPod".
  - Langkah 3 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter assembly.

### DTC `CB-7D` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] iPod Protocol Unsupported (Dokumen: RM000003XYT02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] iPod Protocol Unsupported (Dokumen: RM000003XYT02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] 
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Terhubung dengan non-mass-storage class atau peralatan USB dengan sebuah protocol yang tidak kompatibel.; Kondisi Deteksi: Terhubung dengan sebuah sistem file yang tidak kompatibel atau peralatan USB dengan corrupted atau incompatible File Allocation Table (FAT).; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Malfungsi "iPod"; 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assem
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT PERALATAN USB TIDAK KOMPATIBEL, VERSI "iPod" TIDAK SESUAI, ATAU PERALATAN USB ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter as
  - Langkah 2 (AUDIO / VIDEO) — PERIKSA DARI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan memeriksa apakah DTC yang sama terjadi kembali.
  - Langkah 3 (AUDIO / VIDEO) — FORMAT USB DEVICE TIDAK SESUAI, VERSI "iPod" TIDAK SESUAI, ATAU USB DEVICE ATAU "iPod" RUSAK
  - Langkah 4 (AUDIO / VIDEO) — GANTI RADIO RECEIVER ASSEMBLY

### DTC `CB-7E` — [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Penerima)] No Playable USB File Exists (Dokumen: RM000003XYV02JX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receiver)] No Playable USB File Exists (Dokumen: RM000003XYV02LX) | [AUDIO / VIDEO — SISTEM AUDIO DAN VISUAL (untuk Tipe Radio Receive
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [AUDIO / VIDEO] Area Gangguan: "iPod" Radio penerima assembly; Kondisi Deteksi: Tidak ada file yang dapat dimainkan pada "iPod".; [AUDIO / VIDEO] Area Gangguan: Peralatan USB Radio penerima assembly; Kondisi Deteksi: Tidak ada file yang dapat dimainkan pada peralatan USB.; [AUDIO / VIDEO] Area Gangguan: "iPod" Radio receiver assembly; Kondisi Deteksi: Tidak ada file dimainkan pada "iPod".
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA PERALATAN USB ATAU "iPod": Lepas hubungan peralatan USB atau "iPod" dari stereo jack adapter. -> Periksa apakah file-file yang dapat dimainkan terdapat pada peralatan USB atau "iPod".
  - Langkah 2 (AUDIO / VIDEO) — SELESAI
  - Langkah 3 (AUDIO / VIDEO) — GANTI PERALATAN USB ATAU "iPod": Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan peralatan USB atau "iPod" yang telah diketahui dalam kondisi baik ke stereo jack adapter assembly.
  - Langkah 4 (AUDIO / VIDEO) — PERIKSA TERHADAP DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC dan periksa apakah muncul DTC yang sama lagi.
  - Langkah 5 (AUDIO / VIDEO) — SELESAI (PERALATAN USB ATAU "iPod" RUSAK)
  - Langkah 6 (AUDIO / VIDEO) — GANTI RADIO PENERIMA ASSEMBLY
  - Langkah 1 (AUDIO / VIDEO) — PERIKSA USB DEVICE ATAU "iPod": Lepas hubungan USB device atau "iPod" atau "iPod" dari stereo jack adapter assembly. -> Periksa file yang dimainkan present pada USB device atau "iPod".
  - Langkah 3 (AUDIO / VIDEO) — GANTI USB DEVICE ATAU "iPod": Putar ignition switch ke off. -> Putar ignition switch ke ACC. -> Hubungkan perangkat yang dikenal baik USB device atau "iPod" ke stereo jack adapter assembly.

### DTC `DTC-11` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 11] Room Temperature Sensor Circuit (Dokumen: RM000001DT800PX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 11] Room Temperature Sensor Circuit (Do
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Cooler thermistor Air conditioning amplifier assembly Harness atau konektor; Kondisi Deteksi: Open atau short dalam room temperature sensor circuit.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — PERIKSA COOLER THERMISTOR: Lepas cooler thermistor (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSA AIR CONDITIONING AMPLIFIER ASSEMBLY: Lepas air conditioning amplifier assembly dengan konektor yang masih terhubung (Lihat halaman ). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (COOLER THERMISTOR - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G76 cooler thermistor. -> Lepas hubungan konektor G95 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (HEATING / AIR CONDITIONING) — GANTI COOLER THERMISTOR
  - Langkah 5 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
  - Langkah 6 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 7 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (10°C (50°F))` : **3.00 sampai 3.73 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (15°C (59°F))` : **2.45 sampai 2.88 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (20°C (68°F))` : **1.95 sampai 2.30 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (25°C (77°F))` : **1.60 sampai 1.80 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (30°C (86°F))` : **1.28 sampai 1.47 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (35°C (95°F))` : **1.00 sampai 1.22 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (40°C (104°F))` : **0.80 sampai 1.00 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (45°C (113°F))` : **0.65 sampai 0.85 kΩ**

### DTC `DTC-12` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 12] Ambient Temperature Sensor Circuit (Dokumen: RM000001DT900PX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 12] Ambient Temperature Sensor Circu
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Thermistor assembly Accessory meter assembly Air conditioning amplifier assembly Harness atau konektor; Kondisi Deteksi: Open atau short dalam ambient temperature sensor circuit
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — PERIKSA ACCESSORY METER ASSEMBLY: Periksa perbedaan antara nilai temperatur sekitar yang ditampilkan pada accessory meter assembly dan temperatur sekitar sesungguhnya.
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (ACCESSORY METER - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G32 accessory meter assembly. -> Lepas hubungan konektor G94 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — PERIKSA THERMISTOR ASSEMBLY: Lepas thermistor assembly (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (THERMISTOR - ACCESSORY METER): Lepas hubungan konektor A22 thermistor assembly. -> Lepas hubungan konektor G32 accessory meter assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (HEATING / AIR CONDITIONING) — GANTI ACCESSORY METER ASSEMBLY
  - Langkah 6 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 7 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G32-9 (DATA) - G94-18 (TAMO) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G32-9 (DATA) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (10°C (50°F))` : **3.00 sampai 3.73 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (15°C (59°F))` : **2.45 sampai 2.88 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (20°C (68°F))` : **1.95 sampai 2.30 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (25°C (77°F))` : **1.60 sampai 1.80 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (30°C (86°F))` : **1.28 sampai 1.47 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (35°C (95°F))` : **1.00 sampai 1.22 kΩ**

### DTC `DTC-13` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 13] Evaporator Temperature Sensor Circuit (Dokumen: RM000001DTA00QX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 13] Evaporator Temperature Sensor
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Cooler thermistor No. 1 Air conditioning amplifier assembly Harness atau konektor; Kondisi Deteksi: Open atau short dalam evaporator temperature sensor circuit
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — PERIKSA AIR CONDITIONING AMPLIFIER ASSEMBLY: Lepas air conditioning amplifier assembly dengan konektor yang masih terhubung (Lihat halaman ). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSAAN THERMISTOR PENDINGIN NO.1: Lepas cooler thermistor Np. 1 (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (COOLER THERMISTOR NO. 1 - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G30 cooler thermistor No. 1. -> Lepas hubungan konektor G95 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 5 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
  - Langkah 6 (HEATING / AIR CONDITIONING) — GANTI COOLER THERMISTOR NO. 1
  - Langkah 7 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Voltase Standar: G95-1 (TE) - G95-14 (SG-4) (Ignition switch ON Evaporator temperature 0°C (32°F))` : **2.0 sampai 2.4 V**
  - `[HEATING / AIR CONDITIONING] Voltase Standar: G95-1 (TE) - G95-14 (SG-4) (Ignition switch ON Evaporator temperature 15°C (59°F))` : **1.4 sampai 1.8 V**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (-10°C (14°F))` : **7.30 sampai 9.10 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (-5°C (23°F))` : **5.65 sampai 6.95 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (0°C (32°F))` : **4.40 sampai 5.35 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (5°C (41°F))` : **3.40 sampai 4.15 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (10°C (50°F))` : **2.70 sampai 3.25 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 - 2 (15°C (59°F))` : **2.14 sampai 2.58 kΩ**

### DTC `DTC-14` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 14] Engine Coolant Temperature Communication Circuit (Dokumen: RM000001LZL00GX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 14] Engine Coolant Tem
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Sistem ECD Air conditioning amplifier assembly Harness atau konektor; Kondisi Deteksi: Open atau short dalam engine coolant temperature communication circuit
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — PERIKSA UNTUK DTC (SISTEM KONTROL MESIN): Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (AIR CONDITIONING AMPLIFIER - ECM): Lepas hubungan konektor G94 air conditioning amplifier assembly. -> Lepas hubungan konektor G39 ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 4 (HEATING / AIR CONDITIONING) — LANJUTKAN KE SISTEM ECD
  - Langkah 5 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G94-8 (TW) - G39-2 (THWO) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G94-8 (TW) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `DTC-21` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 21] Solar Sensor Circuit (Dokumen: RM000001DTK00TX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 21] Solar Sensor Circuit (Dokumen: RM000001DTK01UX
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Cooler thermistor (solar sensor) Harness atau konektor Air conditioning amplifier assembly; Kondisi Deteksi: Open dalam Sirkuit cooler thermistor (solar sensor) (Bila melakukan pengecekkan di tempat yang gelap, DTC 21 mungkin tersimpan)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — PERIKSA AIR CONDITIONING AMPLIFIER ASSEMBLY: Lepas air conditioning amplifier assembly dengan konektor yang masih terhubung (Lihat halaman ). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (HEATING / AIR CONDITIONING) — MEMERIKSA COOLER THERMISTOR (SOLAR SENSOR): Lepas cooler thermistor (solar sensor) (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (SOLAR SENSOR - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G77 cooler thermistor (solar sensor). -> Lepas hubungan konektor G95 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 5 (HEATING / AIR CONDITIONING) — GANTI COOLER THERMISTOR (SOLAR SENSOR)
  - Langkah 6 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Voltase Standar: G95-2 (S5-3) - G95-7 (TS) (Ignition switch ON Solar sensor ditujukan untuk electric light Vehi` : **0.8 sampai 4.3 V**
  - `[HEATING / AIR CONDITIONING] Voltase Standar: G95-2 (S5-3) - G95-7 (TS) (Ignition switch ON Menutupi solar sensor dengan kain Vehicle indoor` : **Dibawah 0.8 V**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 (SS+) - 2 (SS-) (Vehicle indoor Solar sensor ditujukan untuk electric light)` : **Dibawah 10 kΩ**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: 1 (SS+) - 2 (SS-) (Vehicle indoor Menutupi solar sensor dengan kain)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G95-2 (S5-3) - G77-1 (SS+) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G95-7 (TS) - G77-2 (SS-) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G95-2 (S5-3) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G95-7 (TS) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `DTC-23` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 23] Pressure Switch Circuit (Dokumen: RM000001DTB00PX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 23] Pressure Switch Circuit (Dokumen: RM000001D
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Air conditioner tube & accessory assembly (air conditioner pressure sensor) Refrigerant dan refrigerant pipe line Air conditioning amplifier assembly Harness atau konektor
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — PERIKSA TEKANAN REFRIGERANT: Pasang manifold gauge. -> Periksa tekanan refrigerant (Lihat halaman ).
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSA PENGOPERASIAN AIR CONDITIONING: Lepas hubungan konektor A16 air conditioner pressure sensor. -> Menggunakan service wire, hubungkan terminal 1 dan 2 dari konektor pada vehicle wire harness side. -> Hidupkan mesin. -> Putar switch A/C ke ON dan periksa magnet clutch.
  - Langkah 3 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (AIR CONDITIONER PRESSURE SENSOR - AIR CONDITIONING AMPLIFIER DAN BODY GROUND): Lepas hubungan konektor A16 air conditioner pressure sensor. -> Lepas hubungan konektor G95 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
  - Langkah 5 (HEATING / AIR CONDITIONING) — PERIKSA REFRIGERANT DAN REFRIGERANT PIPE LINE
  - Langkah 6 (HEATING / AIR CONDITIONING) — GANTU AIR CONDITIONING TUBE & ACCESSORY ASSEMBLY (AIR CONDITIONER PRESSURE SENSOR)
  - Langkah 7 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 8 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G95-5 (PSW) - A16-2 (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: A16-1 - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G95-5 (PSW) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `DTC-41` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 41] Air Mix Damper Control Servo Motor Circuit (Sisi Penumpang) (Dokumen: RM000001LZM00EX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 41] Air Mix
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Air mix damper servo sub-assembly Air conditioning amplifier assembly Harness atau konektor; Kondisi Deteksi: Air mix control damper position tidak berubah ketika air conditioning amplifier assembly mengoperasikan air mix damper servo sub-assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — MELAKUKAN PEMERIKSAAN ACTUATOR: Panaskan mesin. -> Enter actuator check mode (Lihat halaman ). -> Letakkan tangan Anda di depan ventilasi dan periksa bahwa posisi air mix control damper berubah (temperatur dari perubahan udara) sesuai pada tampilan kode.
  - Langkah 2 (HEATING / AIR CONDITIONING) — CHECK HARNESS AND CONNECTOR (AIR MIX DAMPER SERVO - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G81 air mix damper servo sub-assembly. -> Lepas hubungan konektor G94 dan G95 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — GANTI AIR MIX DAMPER SERVO SUB-ASSEMBLY: Sementara ganti air mix damper servo sub-assembly dengan yang baru atau yang berfungsi normal (Lihat halaman ). -> Periksa air mix control damper bekerja dengan normal.
  - Langkah 4 (HEATING / AIR CONDITIONING) — SELESAI (AIR MIX DAMPER SERVO YANG CACAT)
  - Langkah 5 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
  - Langkah 6 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 7 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-5 (MHD) - G94-17 (AMH) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-4 (MCD) - G94-19 (AMC) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-3 (MHP) - G95-23 (PMB) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-2 (MCP) - G95-24 (PMA) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-1 (SG) - G95-20 (SG-1) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-1 (SG) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-2 (MCP) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G81-3 (MHP) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `DTC-42` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 42] Air Inlet Damper Control Servo Motor Circuit (Dokumen: RM000001DTC00PX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 42] Air Inlet Damper Contr
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Recirculation damper servo sub-assembly Harness atau konektor Air conditioning amplifier assembly; Kondisi Deteksi: Air inlet control damper position tidak berubah ketika air conditioning amplifier assembly mengoperasikan recirculation damper servo sub-assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — MELAKUKAN PEMERIKSAAN ACTUATOR: Lepas glove box untuk pemeriksaan secara visual pengoperasian recirculation damper servo sub-assembly (Lihat halaman ). -> Enter actuator check mode (Lihat halaman ). -> Periksa bahwa air inlet control damper position berubah sesuai pada ta
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (RECIRCULATION DAMPER SERVO - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G103 recirculation damper servo sub-assembly. -> Lepas hubungan konektor G94 dan G95 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — GANTI RECIRCULATION DAMPER SERVO SUB-ASSEMBLY: Sementara ganti recirculation damper servo sub-assembly dengan yang baru atau yang berfungsi normal (Lihat halaman ). -> Periksa air inlet control damper bekerja dengan normal.
  - Langkah 4 (HEATING / AIR CONDITIONING) — SELESAI (RECIRCULATION DAMPER SERVO YANG CACAT)
  - Langkah 5 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
  - Langkah 6 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 7 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (RECIRCULATION DAMPER SERVO - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G103 recirculation damper servo sub-assembly. -> Lepas hubungan konektor G94 dan G95 amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-5 (REC) - G94-22 (AIR) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-4 (FRS) - G94-23 (AIF) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-2 (B) - G95-17 (PIA) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-3 (L) - G95-16 (AGND) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-1 (SG) - G95-21 (AUXO) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-5 (REC) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-4 (FRS) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G103-2 (B) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `DTC-43` — [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 43] Air Outlet Damper Control Servo Motor Circuit (Dokumen: RM000001DTD00PX) | [HEATING / AIR CONDITIONING — SISTEM AIR CONDITIONING (untuk Sistem Air Conditioning Otomatis) / Flash Code 43] Air Outlet Damper Con
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [HEATING / AIR CONDITIONING] Area Gangguan: Mode damper servo sub-assembly Air conditioning amplifier assembly Harness atau konektor; Kondisi Deteksi: Posisi mode damper tidak berubah ketika air conditioning amplifier assembly mengoperasikan mode damper servo sub-assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (HEATING / AIR CONDITIONING) — MELAKUKAN PEMERIKSAAN ACTUATOR: Panaskan mesin. -> Enter actuator check mode (Lihat halaman ). -> Letakkan tangan Anda di depan ventilasi dan periksa bahwa posisi mode damper berubah sesuai pada tampilan kode.
  - Langkah 2 (HEATING / AIR CONDITIONING) — PERIKSA HARNESS DAN KONEKTOR (MODE DAMPER SERVO - AIR CONDITIONING AMPLIFIER): Lepas hubungan konektor G79 mode damper servo sub-assembly. -> Lepas hubungan konektor G94 dan G95 air conditioning amplifier assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (HEATING / AIR CONDITIONING) — GANTI MODE DAMPER SERVO SUB-ASSEMBLY: Sementara ganti mode damper servo sub-assembly dengan yang baru atau yang berfungsi normal (Lihat halaman ). -> Periksa mode damper bekerja dengan normal.
  - Langkah 4 (HEATING / AIR CONDITIONING) — SELESAI (MODE DAMPER SERVO YANG CACAT)
  - Langkah 5 (HEATING / AIR CONDITIONING) — LANJUTKAN KE AREA YANG DICURIGAI BERIKUTNYA SEPERTI DITUNJUKKAN DALAM TABEL GEJALA PROBLEM
  - Langkah 6 (HEATING / AIR CONDITIONING) — GANTI AIR CONDITIONING AMPLIFIER ASSEMBLY
  - Langkah 7 (HEATING / AIR CONDITIONING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-4 (DEF) - G94-4 (AOD) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-5 (FACE) - G94-3 (AOF) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-2 (FDEF) - G95-26 (POA) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-3 (HEAT) - G95-25 (POB) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-1 (SG) - G95-11 (SG-2) (Selalu)` : **Dibawah 1 Ω**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-4 (DEF) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-5 (FACE) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[HEATING / AIR CONDITIONING] Tahanan Standar: G79-2 (FDEF) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0010` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit Aktuator Posisi Camshaft "A" (Bank 1) (Dokumen: RM000000PDW0I0X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Aktuator Posisi Camshaft "A" (Bank 1) (Dokumen: RM000000PDW0IAX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Aktuator Posisi Camshaft "A" (Bank 1) (Dokumen: RM000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Open atau short circuit dalam camshaft timing oil control valve untuk sirkuit intake camshaft (untuk Bank 1) Camshaft timing oil control valve assembly untuk intake camshaft (untuk Bank 1) ECM; Kondisi Deteksi: Open atau short circuit dalam camshaft timing oil control valve untuk sirkuit intake camshaft (untuk Bank 1) (1 trip detection logic).; [KONTROL MESIN 2TR-FE] Area Gangguan: Open atau short dalam sirk
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC: Hapus DTC setelah mencatat freeze frame data dan DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Start mesin dan biarkan dalam idle. Kemudian periksa DTC. -> Periksa bahwa P0010 tidak muncul.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — MEMERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY: Periksa camshaft timing oil control valve assembly (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (CAMSHAFT TIMING OIL CONTROL VALVE - ECM): Lepas hubungan konektor camshaft timing oil control valve. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — GANTI CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA DARI DTC: Hapus DTC setelah merekan freeze frame data dan DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Start mesin dan biarkan dalam idle. Kemudian periksa DTC. -> Periksa bahwa P0010 tidak di-output.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C74-2 - C75-13 (OC1+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C74-1 - C75-12 (OC1-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C74-2 atau C75-13 (OC1+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C74-1 atau C75-12 (OC1-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C74-2 - C75-13 (OC1+) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C74-1 - C75-12 (OC1-) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C74-2 atau C75-13 (OC1+) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C74-1 atau C75-12 (OC1-) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0011` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Posisi Camshaft "A" - Timing Over-Advanced atau System Performance (Bank 1) (Dokumen: RM000000PDU0JLX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Posisi Camshaft "A" - Timing Over-Advanced atau System Performance (Bank 1) (Dokumen: RM000000PDU0JVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] P
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem mekanikal (Timing chain lompat gigi atau rantai memanjang) Camshaft timing oil control valve assembly Filter oil control valve Camshaft timing gear assembly ECM; Kondisi Deteksi: Intake valve timing macet pada nilai tertentu ketika dalam rentang memajukan(advance) (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem mekanikal (Rantai timing lompat gigi atau rantai memanjang) Camsha
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC LAIN YANG MUNCUL (SEBAGAI TAMBAHAN UNTUK DTC P011 atau POO12): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (MENGOPERASIKAN CAMSHAFT TIMING OIL CONTROL VALVE): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Panaskan mesin. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / Active Test / Control VVT Linear (Bank 1). -> Periksa putaran mesin samb
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0011 ATAU P0012): Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan panaskan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan 
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA VALVE TIMING (PERIKSA TERHADAP KEKENDURAN PADA TIMING CHAIN DAN APAKAH TIMING CHAIN TELAH LOMPAT GIGI ATAU TIDAK): Lepas cover cylinder head. -> Putar crankshaft sehingga luruskan tanda timing pada crankshaft. -> Luruskan alur crankshaft pulley dengan posisi "0". -> Pastikan apakah tanda timing pulley camshaft dan cover cylinder head saling berhadapan s
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — MEMERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY: Periksa camshaft timing oil control valve assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — MEMERIKSA FILTER OIL CONTROL VALVE: Lepas filter oil control valve (Lihat halaman ). -> Periksa bahwa filter tidak tersumbat.
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — GANTI CAMSHAFT TIMING GEAR ASSEMBLY: Ganti camshaft timing gear assembly (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] OK: 0%` : **Putaran mesin normal**
  - `[ENGINE CONTROL 1TR-FE] OK: 100%` : **Idle mesin kasar atau mati mendadak**
  - `[KONTROL MESIN 2TR-FE] OK: 0%` : **Putaran mesin normal**
  - `[KONTROL MESIN 2TR-FE] OK: 100%` : **Idle mesin kasar atau mati mendadak**

### DTC `P0012` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Posisi Camshaft "A" - Timing Over-Retarded (Bank 1) (Dokumen: RM000000PDU0JLX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Posisi Camshaft "A" - Timing Over-Retarded (Bank 1) (Dokumen: RM000000PDU0JVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Posisi Camshaft "A" - Timing Over-Retarded (Bank 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem mekanikal (Timing chain lompat gigi atau rantai memanjang) Camshaft timing oil control valve assembly Filter oil control valve Camshaft timing gear assembly ECM; Kondisi Deteksi: Intake valve timing macet pada nilai tertentu ketika dalam rentang memajukan(advance) (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem mekanikal (Rantai timing lompat gigi atau rantai memanjang) Camsha
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC LAIN YANG MUNCUL (SEBAGAI TAMBAHAN UNTUK DTC P011 atau POO12): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (MENGOPERASIKAN CAMSHAFT TIMING OIL CONTROL VALVE): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Panaskan mesin. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / Active Test / Control VVT Linear (Bank 1). -> Periksa putaran mesin samb
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0011 ATAU P0012): Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan panaskan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan 
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA VALVE TIMING (PERIKSA TERHADAP KEKENDURAN PADA TIMING CHAIN DAN APAKAH TIMING CHAIN TELAH LOMPAT GIGI ATAU TIDAK): Lepas cover cylinder head. -> Putar crankshaft sehingga luruskan tanda timing pada crankshaft. -> Luruskan alur crankshaft pulley dengan posisi "0". -> Pastikan apakah tanda timing pulley camshaft dan cover cylinder head saling berhadapan s
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — MEMERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY: Periksa camshaft timing oil control valve assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — MEMERIKSA FILTER OIL CONTROL VALVE: Lepas filter oil control valve (Lihat halaman ). -> Periksa bahwa filter tidak tersumbat.
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — GANTI CAMSHAFT TIMING GEAR ASSEMBLY: Ganti camshaft timing gear assembly (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] OK: 0%` : **Putaran mesin normal**
  - `[ENGINE CONTROL 1TR-FE] OK: 100%` : **Idle mesin kasar atau mati mendadak**
  - `[KONTROL MESIN 2TR-FE] OK: 0%` : **Putaran mesin normal**
  - `[KONTROL MESIN 2TR-FE] OK: 100%` : **Idle mesin kasar atau mati mendadak**

### DTC `P0016` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Posisi Crankshaft - Korelasi Posisi Camshaft (Bank 1 Sensor A) (Dokumen: RM000000PDV0HXX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Posisi Crankshaft - Korelasi Posisi Camshaft (Bank 1 Sensor A) (Dokumen: RM000000PDV0I6X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Posisi Crankshaft - Korelas
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Valve timing Camshaft timing oil control valve assembly (bank 1) Camshaft timing gear assembly ECM; Kondisi Deteksi: Penyimpangan sinyal crankshaft position sensor dan sinyal camshaft position sensor (2 trip detection logic); [KONTROL MESIN 2TR-FE] Area Gangguan: Valve timing Camshaft timing oil control valve assembly (bank 1) Camshaft timing gear assembly ECM; Kondisi Deteksi: Penyimpangan dalam sinyal cran
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC LAIN YANG MUNCUL (SEBAGAI TAMBAHAN KE DTC P0016): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (MENGOPERASIKAN CAMSHAFT TIMING OIL CONTROL VALVE): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Hidupkan intelligent tester. -> Panaskan mesin. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / Active Test / Control the VVT Linear (Bank 1) / All Data / VVT Change An
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — SETEL VALVE TIMING: Setel valve timing (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — MEMERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY: Periksa camshaft timing oil control valve assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — MEMERIKSA FILTER OIL CONTROL VALVE: Lepas filter oil control valve (Lihat halaman ). -> Periksa bahwa filter tidak tersumbat.
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — GANTI CAMSHAFT TIMING GEAR ASSEMBLY: Ganti camshaft timing gear assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan panaskan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — LANJUTKAN KE BAGAN DTC

### DTC `P0046` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Range / Performance pada Sirkuit Turbocharger / Supercharger Boost Control Solenoid (Dokumen: RM000002NCM015X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Range / Performance pada Sirkuit Turbocharger / Supercharger Boost Control Solenoid (Doku
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Motor DC (turbocharger sub-assembly) Turbo motor driver; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Motor DC (turbocharger sub-assembly) Turbo motor driver; [KONTROL MESIN 1KD-FTV] Area Gangguan: DC motor (turbocharger sub-assembly) Turbo motor driver; [KONTROL MESIN 2KD-FTV] Area Gangguan: DC motor (turbocharger sub-assembly) Turbo motor driver
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DI SAMPING DTC P0046): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBOCHARGER SUB-ASSEMBLY (PENGOPERASIAN MOTOR DC): Putar ignition switch ke ON. -> Putar ignition switch ke off dan periksa pengoperasian motor DC (periksa gerakan operation link).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBO MOTOR DRIVER: Pemeriksaan Tegangan -> Pemeriksaan Bentuk Gelombang Output
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBOCHARGER SUB-ASSEMBLY (TAHANAN MOTOR DC): Lepas hubungan konektor motor DC. -> Ukur tahanan motor DC.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MOTOR DC - TURBO MOTOR DRIVER): Lepas hubungan konektor motor DC. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali konektor motor DC.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH OUTPUT DTC BERULANG ATAU TIDAK (DTC P0046): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Lepas fuse EFI dari relay block ruang mesin dan junction block assembly selama lebi
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY: Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C39-3 (+B) - C39-4 (GND) (Selalu)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] OK: C39-2 (VNTI) - C39-4 (GND) (Ignition switch ON)` : **Betulkan bentuk gelombang seperti ditunjukkan berikut**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-12 (M+) - C41-2 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-5 (M-) - C41-1 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-12 (M+) atau C41-2 (M+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-5 (M-) atau C41-1 (M-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C39-3 (+B) - C39-4 (GND) (Selalu)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] OK: C39-2 (VNTI) - C39-4 (GND) (Ignition switch ON)` : **Betulkan bentuk gelombang seperti ditunjukkan berikut**

### DTC `P0047` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low pada Sirkuit "A" Turbocharger / Supercharger Boost Control (Dokumen: RM000002PPL02VX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low pada Sirkuit "A" Turbocharger / Supercharger Boost Control (Dokumen: RM000002PPL02WX) | [KONTROL MESIN 1KD
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open pada sirkuit motor DC Turbo motor driver Motor DC (turbocharger sub-assembly); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short pada sirkuit motor DC Turbo motor driver Motor DC (turbocharger sub-assembly); Kondisi Deteksi: Arus motor DC 6.5 A atau lebih selama 0.5 detik atau lebih (1 trip detection logic); [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open pada sirkuit motor DC Turbo motor driver Motor DC (tur
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBOCHARGER SUB-ASSEMBLY (PENGOPERASIAN MOTOR DC): Putar ignition switch ke ON. -> Putar ignition switch ke off dan periksa pengoperasian motor DC (periksa gerakan operation link).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBOCHARGER SUB-ASSEMBLY (MOTOR DC): Lepas hubungan konektor motor DC. -> Ukur tahanan motor DC.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MOTOR DC - TURBO MOTOR DRIVER): Lepas hubungan konektor motor DC. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali konektor motor DC.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0047 DAN/ATAU P0048): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Kendarai kendaraan dengan pola pengendaraan dalam kota selama minimal 10 menit. -> Masuk ke menu berikut ini: Powert
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY: Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Lepas fuse EFI dari relay block ruang mesin dan junction block assembly selama lebi
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-12 (M+) - C41-2 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-5 (M-) - C41-1 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-12 (M+) atau C41-2 (M+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-5 (M-) atau C41-1 (M-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-12 (M+) - C41-2 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-5 (M-) - C41-1 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-12 (M+) atau C41-2 (M+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-5 (M-) atau C41-1 (M-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0048` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High pada Sirkuit "A" Turbocharger / Supercharger Boost Control (Dokumen: RM000002PPL02VX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High pada Sirkuit "A" Turbocharger / Supercharger Boost Control (Dokumen: RM000002PPL02WX) | [KONTROL MESIN 1
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open pada sirkuit motor DC Turbo motor driver Motor DC (turbocharger sub-assembly); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short pada sirkuit motor DC Turbo motor driver Motor DC (turbocharger sub-assembly); Kondisi Deteksi: Arus motor DC 6.5 A atau lebih selama 0.5 detik atau lebih (1 trip detection logic); [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open pada sirkuit motor DC Turbo motor driver Motor DC (tur
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBOCHARGER SUB-ASSEMBLY (PENGOPERASIAN MOTOR DC): Putar ignition switch ke ON. -> Putar ignition switch ke off dan periksa pengoperasian motor DC (periksa gerakan operation link).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBOCHARGER SUB-ASSEMBLY (MOTOR DC): Lepas hubungan konektor motor DC. -> Ukur tahanan motor DC.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MOTOR DC - TURBO MOTOR DRIVER): Lepas hubungan konektor motor DC. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali konektor motor DC.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0047 DAN/ATAU P0048): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Kendarai kendaraan dengan pola pengendaraan dalam kota selama minimal 10 menit. -> Masuk ke menu berikut ini: Powert
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY: Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Lepas fuse EFI dari relay block ruang mesin dan junction block assembly selama lebi
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-12 (M+) - C41-2 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-5 (M-) - C41-1 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-12 (M+) atau C41-2 (M+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-5 (M-) atau C41-1 (M-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-12 (M+) - C41-2 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-5 (M-) - C41-1 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-12 (M+) atau C41-2 (M+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C39-5 (M-) atau C41-1 (M-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0087` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Tekanan Fuel Rail / Sistem - Terlalu Rendah (Dokumen: RM000001880046X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Tekanan Fuel Rail / Sistem - Terlalu Rendah (Dokumen: RM000001880047X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Tekanan Fuel Rail 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) Bahan bakar tidak sesuai Bahan bakar beku ECM; Kondisi Deteksi: Tegangan output fuel pressure sensor dipertahankan pada nilai yang tetap selama 90 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (SENSOR TEKANAN BAHAN BAKAR - ECM): Lepas hubungan konektor fuel pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel pressure sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA ECM (TEGANGAN FUEL PRESSURE SENSOR): Lepas hubungan konektor fuel pressure sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor fuel pressure sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI PRESSURE SENSOR (COMMON RAIL ASSEMBLY): Mengganti common rail assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0087, P0190, P0192, P0193): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 60 detik, dan kemudian naikkan putaran mesin ke 2500 rpm dengan cepat secara berulang-kali
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) - C22-26 (PCR1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) - C22-33 (PCR2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-1 (VCS) - C23-2 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-6 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-4 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-3 (E2S) - C23-1 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) atau C22-26 (PCR1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) atau C22-33 (PCR2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0088` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Tekanan Fuel Rail /Sistem - Terlalu Tinggi (Dokumen: RM00000188403WX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Tekanan Fuel Rail /Sistem - Terlalu Tinggi (Dokumen: RM00000188403XX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Tekanan Fuel Rail /S
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Suction control valve (fuel supply pump assembly) Pressure discharge valve (common rail assembly) Open atau short dalam sirkuit suction control valve Fuel pressure sensor (common rail assembly) ECM; Kondisi Deteksi: Tekanan bahan bakar di common rail melebihi 200000 kPa (2039 kgf/cm 2 , 29000 psi) (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Suction control valve (fuel supply pump asse
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA SETIAP OUTPUT LAINNYA (DI SAMPING DTC P0088): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca Current DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA FREEZE FRAME DATA (FUEL PRESS): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Rekaman yang disimpan DTC dan freeze frame data.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA ECM (TEGANGAN OUTPUT FUEL PRESSURE SENSOR): Hubungkan probe positif (+) oscilloscope ke terminal input fuel pressure sensor dari konektor ECM dan probe negatif (-) ke masa bodi. -> Putar ignition switch ke ON. -> Periksa dari noise apapun dalam bentuk gelombang ketika diberikan getar
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (SUCTION CONTROL VALVE): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — LAKUKAN INISIALISASI SUPPLY PUMP BAHAN BAKAR: Lakukan inisialisasi fuel supply pump (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON dan hidupkan mesin. -> Setelah idling selama 60 detik, naikkan putaran dari idli
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C22-26 (PCR1) - Masa bodi (Getaran diterapkan untuk wire harness dan konektor-konektor)` : **Tidak ada noise dalam bentuk gelombang.**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C22-26 (PCR1) - Masa bodi (Getaran diterapkan untuk wire harness dan konektor-konektor)` : **Tidak ada noise dalam bentuk gelombang.**
  - `[KONTROL MESIN 1KD-FTV] Voltase Standar: C22-26 (PCR1) - Body ground (Getaran diberikan ke wire harness dan konektor)` : **Tidak terdapat noise dalam bentuk gelombang**
  - `[KONTROL MESIN 2KD-FTV] Voltase Standar: C22-26 (PCR1) - Body ground (Getaran diberikan ke wire harness dan konektor)` : **Tidak terdapat noise dalam bentuk gelombang**

### DTC `P0093` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Terdeteksi Kebocoran Sistem Bahan Bakar - Kebocoran Besar (Dokumen: RM0000012X902CX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Terdeteksi Kebocoran Sistem Bahan Bakar - Kebocoran Besar (Dokumen: RM0000012X902DX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbo
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Saluran bahan bakar antara fuel supply pump dan common rail assembly Saluran bahan bakar antara common rail assembly dan setiap injektor assembly Suction control valve (fuel supply pump assembly) Common rail assembly Injector assembly Pressure discharge valve (common rail assembly) Fuel pressure sensor (common rail assembly) Crankshaft position sensor Elemen filter bahan bakar sub-assembly Open atau short d
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — Periksa kebocoran bahan bakar dalam area tekanan tinggi.: Sebelum menghidupkan mesin, periksa secara visual kebocoran bahan bakar dari fuel supply pump assembly, injector assembly, common rail assembly, dan pipa-pipa bahan bakar dalam area tekanan tinggi.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA SETIAP DTC YANG MUNCUL LAINNYA (DISAMPING DTC P0093) DAN MEREKAM DTC DAN FREEZE FRAME DATA YANG DISIMPAN (PROSEDUR 2): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON dan hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC dan freeze frame data.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA FUEL RECEIVER GAUGE (JUMLAH BAHAN BAKAR): Periksa apakah level bahan bakar rendah.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — TAMBAH BAHAN BAKAR: Tambah bahan bakar.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0093): Menggunakan hand pump yang terpasang pada fuel filter cap, buang udara dari sistem bahan bakar. Terus pompa hingga tahanan pompa bertambah. -> Hidupkan mesin. -> Putar ignition switch ke off. -> Hubungkan intelligent tester ke DLC3. -> Puta
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA FREEZE FRAME DATA (INJECTION FEEDBACK VAL #1 TO #4): Baca nilai dari Injection Feedback Val #1 sampai #4 dalam rekaman freeze frame data dalam Prosedur 2.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (FUEL PRESS): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT/ Data List /Fuel Press. -> Hidupkan mesin. -> Baca nilai Teka
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INJECTION FEEDBACK VAL #1 KE #4): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hidupkan mesin dan panaskan mesin. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Injection Feedback Val #1 sampai #4. -> 
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Standar: Injection Feedback Val #1 Injection Feedback Val #2 Injection Feedback Val #3 Injection Feedback Val #4 (I` : **-3.0 mm 3 /st sampai 3.0 mm 3 /st**
  - `[ENGINE CONTROL 1KD-FTV] Standar: Engine Speed (Cranking)` : **50 sampai 400 rpm**
  - `[ENGINE CONTROL 1KD-FTV] Standar: Engine Speed (Idling dengan mesin panas)` : **700 sampai 800 rpm**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C22-26 (PCR1) - Masa bodi (Getaran diterapkan untuk wire harness dan konektor-konektor)` : **Tidak ada noise dalam bentuk gelombang.**
  - `[ENGINE CONTROL 2KD-FTV] Standar: Injection Feedback Val #1 Injection Feedback Val #2 Injection Feedback Val #3 Injection Feedback Val #4 (I` : **-3.0 mm 3 /st sampai 3.0 mm 3 /st**
  - `[ENGINE CONTROL 2KD-FTV] Standar: Engine Speed (Cranking)` : **50 sampai 400 rpm**
  - `[ENGINE CONTROL 2KD-FTV] Standar: Engine Speed (Idling dengan mesin panas)` : **700 sampai 800 rpm**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C22-26 (PCR1) - Masa bodi (Getaran diterapkan untuk wire harness dan konektor-konektor)` : **Tidak ada noise dalam bentuk gelombang.**

### DTC `P0095` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit 2 Intake Air Temperature Sensor (Dokumen: RM00000188103GX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit 2 Intake Air Temperature Sensor (Dokumen: RM00000188103IX) | [KONTROL MESIN 1KD-FTV — SISTEM ECD] Intake Air Temperature Sens
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short di sirkuit temperatur udara sekitar sensor (turbo) Intake air temperature sensor (turbo) ECM; Kondisi Deteksi: Open atau short dalam sirkuit intake air temperature sensor (turbo) selama 0.5 detik (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short dalam sirkuit intake air temperature sensor (turbo) Intake air temperature sensor (turbo) ECM; Kondisi Deteksi: Short dalam si
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE [TURBO]): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air Temp (Turbo). -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor intake air temperature sensor (turbo). -> Hubungkan terminals 1 dan 2 dari konektor sisi wire harness intake air temperature sensor (turbo). -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INTAKE AIR TEMPERATURE SENSOR - ECM): Lepas hubungan konektor intake air temperature sensor (turbo). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor intake air temperature sensor (turbo). -> Hubungka
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor intake air temperature sensor (turbo). -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air T
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INTAKE AIR TEMPERATURE SENSOR [TURBO] - ECM): Lepas hubungan konektor intake air temperature sensor (turbo). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor intake air temperature sensor (turbo). -> Hubungka
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. BILA OK, GANTI INTAKE AIR TEMPERATURE SENSOR (TURBO).: Ganti intake air temperature sensor (turbo) (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-2 atau C22-20 (THIA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-2 atau C22-20 (THIA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0097` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Sirkuit 2 Intake Air Temperature Sensor (Dokumen: RM00000188103GX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low Sirkuit 2 Intake Air Temperature Sensor (Dokumen: RM00000188103IX) | [KONTROL MESIN 1KD-FTV — SISTEM ECD] Low Sirkuit pada In
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short di sirkuit temperatur udara sekitar sensor (turbo) Intake air temperature sensor (turbo) ECM; Kondisi Deteksi: Open atau short dalam sirkuit intake air temperature sensor (turbo) selama 0.5 detik (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short dalam sirkuit intake air temperature sensor (turbo) Intake air temperature sensor (turbo) ECM; Kondisi Deteksi: Short dalam si
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE [TURBO]): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air Temp (Turbo). -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor intake air temperature sensor (turbo). -> Hubungkan terminals 1 dan 2 dari konektor sisi wire harness intake air temperature sensor (turbo). -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INTAKE AIR TEMPERATURE SENSOR - ECM): Lepas hubungan konektor intake air temperature sensor (turbo). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor intake air temperature sensor (turbo). -> Hubungka
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor intake air temperature sensor (turbo). -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air T
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INTAKE AIR TEMPERATURE SENSOR [TURBO] - ECM): Lepas hubungan konektor intake air temperature sensor (turbo). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor intake air temperature sensor (turbo). -> Hubungka
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. BILA OK, GANTI INTAKE AIR TEMPERATURE SENSOR (TURBO).: Ganti intake air temperature sensor (turbo) (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-2 atau C22-20 (THIA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-2 atau C22-20 (THIA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0098` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Sirkuit 2 Intake Air Temperature Sensor (Dokumen: RM00000188103GX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Sirkuit 2 Intake Air Temperature Sensor (Dokumen: RM00000188103IX) | [KONTROL MESIN 1KD-FTV — SISTEM ECD] High Sirkuit pada
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short di sirkuit temperatur udara sekitar sensor (turbo) Intake air temperature sensor (turbo) ECM; Kondisi Deteksi: Open atau short dalam sirkuit intake air temperature sensor (turbo) selama 0.5 detik (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short dalam sirkuit intake air temperature sensor (turbo) Intake air temperature sensor (turbo) ECM; Kondisi Deteksi: Short dalam si
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE [TURBO]): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air Temp (Turbo). -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor intake air temperature sensor (turbo). -> Hubungkan terminals 1 dan 2 dari konektor sisi wire harness intake air temperature sensor (turbo). -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INTAKE AIR TEMPERATURE SENSOR - ECM): Lepas hubungan konektor intake air temperature sensor (turbo). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor intake air temperature sensor (turbo). -> Hubungka
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor intake air temperature sensor (turbo). -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air T
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INTAKE AIR TEMPERATURE SENSOR [TURBO] - ECM): Lepas hubungan konektor intake air temperature sensor (turbo). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor intake air temperature sensor (turbo). -> Hubungka
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. BILA OK, GANTI INTAKE AIR TEMPERATURE SENSOR (TURBO).: Ganti intake air temperature sensor (turbo) (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C18-2 atau C22-20 (THIA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C18-2 atau C22-20 (THIA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C18-2 - C22-20 (THIA) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C18-1 - C22-28 (E2) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0100` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Mass Air Flow Malfungsi (Dokumen: RM00000187J02XX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Mass Air Flow Malfungsi (Dokumen: RM00000187J02YX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Mass Air Flow Malfungsi (Dokumen: 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit mass air flow meter Mass air flow meter ECM; Kondisi Deteksi: Tegangan mass air flow meter 0.2 V atau kurang, atau 4.9 V atau lebih dengan putaran mesin pada 4000 rpm atau kurang selama 3 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan mass air flow meter 0.2 V atau kurang dengan putaran mesin pada 4000 rpm atau kurang selama 3 detik (1 trip detection logic).; [ENGIN
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA MASS AIR FLOW METER (SIRKUIT POWER SOURCE ): Lepas hubungan konektor mass air flow. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor mass air flow.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ENGINE ROOM RELAY BLOCK DAN JUNCTION BLOCK ASSEMBLY): Lepas hubungan konektor mass air flow. -> Lepas integration relay No. 1 dari relay block ruang mesin dan junction block assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. 
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA SIRKUIT POWER SOURCE ECM: Periksa sirkuit power ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI MASS AIR FLOW METER: Ganti mass air flow meter (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0100, P0102 DAN/ATAU P0103): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan tunggu selama 3 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C36-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-3 - C23-24 (VG) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-2 - C23-32 (EVG) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-3 atau C23-24 (VG) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-1 - 1J-5 (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-1 atau 1J-5 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C36-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-3 - C23-24 (VG) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0102` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Sirkuit pada Mass Air Flow (Dokumen: RM00000187J02XX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Sirkuit pada Mass Air Flow (Dokumen: RM00000187J02YX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low Sirkuit pada Mass Air Flow (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit mass air flow meter Mass air flow meter ECM; Kondisi Deteksi: Tegangan mass air flow meter 0.2 V atau kurang, atau 4.9 V atau lebih dengan putaran mesin pada 4000 rpm atau kurang selama 3 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan mass air flow meter 0.2 V atau kurang dengan putaran mesin pada 4000 rpm atau kurang selama 3 detik (1 trip detection logic).; [ENGIN
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA MASS AIR FLOW METER (SIRKUIT POWER SOURCE ): Lepas hubungan konektor mass air flow. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor mass air flow.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ENGINE ROOM RELAY BLOCK DAN JUNCTION BLOCK ASSEMBLY): Lepas hubungan konektor mass air flow. -> Lepas integration relay No. 1 dari relay block ruang mesin dan junction block assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. 
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA SIRKUIT POWER SOURCE ECM: Periksa sirkuit power ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI MASS AIR FLOW METER: Ganti mass air flow meter (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0100, P0102 DAN/ATAU P0103): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan tunggu selama 3 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C36-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-3 - C23-24 (VG) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-2 - C23-32 (EVG) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-3 atau C23-24 (VG) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-1 - 1J-5 (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-1 atau 1J-5 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C36-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-3 - C23-24 (VG) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0103` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Sirkuit pada Mass Air Flow (Dokumen: RM00000187J02XX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Sirkuit pada Mass Air Flow (Dokumen: RM00000187J02YX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Sirkuit pada Mass Air Flow (Dokumen: 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit mass air flow meter Mass air flow meter ECM; Kondisi Deteksi: Tegangan mass air flow meter 0.2 V atau kurang, atau 4.9 V atau lebih dengan putaran mesin pada 4000 rpm atau kurang selama 3 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan mass air flow meter 0.2 V atau kurang dengan putaran mesin pada 4000 rpm atau kurang selama 3 detik (1 trip detection logic).; [ENGIN
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA MASS AIR FLOW METER (SIRKUIT POWER SOURCE ): Lepas hubungan konektor mass air flow. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor mass air flow.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ENGINE ROOM RELAY BLOCK DAN JUNCTION BLOCK ASSEMBLY): Lepas hubungan konektor mass air flow. -> Lepas integration relay No. 1 dari relay block ruang mesin dan junction block assembly. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. 
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA SIRKUIT POWER SOURCE ECM: Periksa sirkuit power ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI MASS AIR FLOW METER: Ganti mass air flow meter (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0100, P0102 DAN/ATAU P0103): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan tunggu selama 3 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C36-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-3 - C23-24 (VG) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-2 - C23-32 (EVG) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-3 atau C23-24 (VG) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-1 - 1J-5 (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-1 atau 1J-5 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C36-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-3 - C23-24 (VG) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0105` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Tekanan Absolute Manifold / Tekanan Barometric (Dokumen: RM00000187U03ZX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Tekanan Absolute Manifold / Tekanan Barometric (Dokumen: RM00000187U040X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharge
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Manifold absolute pressure sensor ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Manifold absolute pressure sensor ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: Open atau short sirkuit pada manifold absolute pressure sensor Manifold absolute pressure sensor ECM; [KONTROL MESIN 2KD-FTV] A
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (MANIFOLD ABSOLUTE PRESSURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / MAP. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (MANIFOLD ABSOLUTE PRESSURE SENSOR - ECM): Lepas hubungan konektor manifold absolute pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor manifold absolute pressure sensor. -> Hubungkan kembal
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL ECM (VC TERMINAL): Lepas hubungan konektor manifold absolute pressure sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor manifold absolute pressure sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI MANIFOLD ABSOLUTE PRESSURE SENSOR: Ganti manifold absolute pressure sensor (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0105, P0107 ATAU P0108): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Matikan tester. -> Hidupkan mesin. -> Setelah mesin mulai hidup selama 2 detik, pacu mesin selama 1 detik. -
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Matikan tester. -> Putar ignition switch ke ON selama 3 detik dan hidupkan tester. -> Setelah mesin mulai hi
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-2 (PIM) - C23-28 (PIM) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-3 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-1 (E) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-2 (PIM) atau C23-28 (PIM) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-3 (VC) atau C22-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C20-3 (VC) - C20-1 (E) (Ignition switch ON)` : **4.75 sampai 5.25 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C20-2 (PIM) - C23-28 (PIM) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C20-3 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0107` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit Tekanan Absolute Manifold / Barometric (Dokumen: RM00000187U03ZX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit Tekanan Absolute Manifold / Barometric (Dokumen: RM00000187U040X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Va
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Manifold absolute pressure sensor ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Manifold absolute pressure sensor ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: Open atau short sirkuit pada manifold absolute pressure sensor Manifold absolute pressure sensor ECM; [KONTROL MESIN 2KD-FTV] A
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (MANIFOLD ABSOLUTE PRESSURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / MAP. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (MANIFOLD ABSOLUTE PRESSURE SENSOR - ECM): Lepas hubungan konektor manifold absolute pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor manifold absolute pressure sensor. -> Hubungkan kembal
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL ECM (VC TERMINAL): Lepas hubungan konektor manifold absolute pressure sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor manifold absolute pressure sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI MANIFOLD ABSOLUTE PRESSURE SENSOR: Ganti manifold absolute pressure sensor (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0105, P0107 ATAU P0108): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Matikan tester. -> Hidupkan mesin. -> Setelah mesin mulai hidup selama 2 detik, pacu mesin selama 1 detik. -
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Matikan tester. -> Putar ignition switch ke ON selama 3 detik dan hidupkan tester. -> Setelah mesin mulai hi
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-2 (PIM) - C23-28 (PIM) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-3 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-1 (E) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-2 (PIM) atau C23-28 (PIM) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-3 (VC) atau C22-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C20-3 (VC) - C20-1 (E) (Ignition switch ON)` : **4.75 sampai 5.25 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C20-2 (PIM) - C23-28 (PIM) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C20-3 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0108` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit Tekanan Absolute Manifold / Barometrik (Dokumen: RM00000187U03ZX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit Tekanan Absolute Manifold / Barometrik (Dokumen: RM00000187U040X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Manifold absolute pressure sensor ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Manifold absolute pressure sensor ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: Open atau short sirkuit pada manifold absolute pressure sensor Manifold absolute pressure sensor ECM; [KONTROL MESIN 2KD-FTV] A
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (MANIFOLD ABSOLUTE PRESSURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / MAP. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (MANIFOLD ABSOLUTE PRESSURE SENSOR - ECM): Lepas hubungan konektor manifold absolute pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor manifold absolute pressure sensor. -> Hubungkan kembal
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL ECM (VC TERMINAL): Lepas hubungan konektor manifold absolute pressure sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor manifold absolute pressure sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI MANIFOLD ABSOLUTE PRESSURE SENSOR: Ganti manifold absolute pressure sensor (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0105, P0107 ATAU P0108): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Matikan tester. -> Hidupkan mesin. -> Setelah mesin mulai hidup selama 2 detik, pacu mesin selama 1 detik. -
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Matikan tester. -> Putar ignition switch ke ON selama 3 detik dan hidupkan tester. -> Setelah mesin mulai hi
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-2 (PIM) - C23-28 (PIM) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-3 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-1 (E) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-2 (PIM) atau C23-28 (PIM) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C20-3 (VC) atau C22-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C20-3 (VC) - C20-1 (E) (Ignition switch ON)` : **4.75 sampai 5.25 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C20-2 (PIM) - C23-28 (PIM) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C20-3 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0110` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Temperatur Udara Masuk (Dokumen: RM00000187L02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Temperatur Udara Masuk (Dokumen: RM00000187L02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Temperatur Udara Masuk (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit IAT sensor IAT sensor (menyatu dalam mass air flow sensor) ECM; Kondisi Deteksi: IAT sensor mengalami open atau short selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short dalam sirkuit IAT sensor IAT sensor (menyatu dalam mass air flow sensor) ECM; Kondisi Deteksi: Short di IAT sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTR
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor mass air flow. -> Hubungkan terminal 4 (THA) dan 5 (E2) dari mass air flow meter sisi konektor wire harness. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke me
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor mass air flow. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilainya. -> Hub
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. BILA OK, GANTI MASS AIR FLOW METER: Ganti mass air flow meter (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-4 (THA) - C22-31 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-5 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-4 (THA) atau C22-31 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-4 (THA) - C22-31 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-5 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-4 (THA) atau C22-31 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C36-4 (THA) - C76-29 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C36-5 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0112` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit Temperatur Udara Intake (Dokumen: RM00000187L02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit Temperatur Udara Intake (Dokumen: RM00000187L02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low Input pa
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit IAT sensor IAT sensor (menyatu dalam mass air flow sensor) ECM; Kondisi Deteksi: IAT sensor mengalami open atau short selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short dalam sirkuit IAT sensor IAT sensor (menyatu dalam mass air flow sensor) ECM; Kondisi Deteksi: Short di IAT sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTR
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor mass air flow. -> Hubungkan terminal 4 (THA) dan 5 (E2) dari mass air flow meter sisi konektor wire harness. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke me
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor mass air flow. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilainya. -> Hub
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. BILA OK, GANTI MASS AIR FLOW METER: Ganti mass air flow meter (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-4 (THA) - C22-31 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-5 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-4 (THA) atau C22-31 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-4 (THA) - C22-31 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-5 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-4 (THA) atau C22-31 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C36-4 (THA) - C76-29 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C36-5 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0113` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit Temperatur Udara Masuk (Dokumen: RM00000187L02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit Temperatur Udara Masuk (Dokumen: RM00000187L02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Input p
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit IAT sensor IAT sensor (menyatu dalam mass air flow sensor) ECM; Kondisi Deteksi: IAT sensor mengalami open atau short selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short dalam sirkuit IAT sensor IAT sensor (menyatu dalam mass air flow sensor) ECM; Kondisi Deteksi: Short di IAT sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTR
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor mass air flow. -> Hubungkan terminal 4 (THA) dan 5 (E2) dari mass air flow meter sisi konektor wire harness. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke me
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor mass air flow. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilainya. -> Hub
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor mass air flow. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor mass air flow. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. BILA OK, GANTI MASS AIR FLOW METER: Ganti mass air flow meter (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-4 (THA) - C22-31 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-5 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C36-4 (THA) atau C22-31 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-4 (THA) - C22-31 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-5 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C36-4 (THA) atau C22-31 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C36-4 (THA) - C76-29 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C36-5 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0115` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM00000187M02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM00000187M02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Temperatur Cai
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam engine coolant temperature sensor Engine coolant temperature sensor ECM; Kondisi Deteksi: Open atau short circuit dalam engine coolant temperature sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short circuit dalam engine coolant temperature sensor Engine coolant temperature sensor ECM; Kondisi Deteksi: Short circuit dalam engine coola
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE COOLANT TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor engine coolant temperature sensor. -> Hubungkan terminal 1 dan 2 dari sisi konektor wire harness engine coolant temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ENGINE COOLANT TEMPERATURE SENSOR - ECM): Lepas hubungan konektor engine coolant temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor engine coolant temperature sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor engine coolant temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. ->
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ENGINE COOLANT TEMPERATURE SENSOR - ECM): Lepas hubungan konektor engine coolant temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor engine coolant temperature sensor. -> Hubungkan kembal
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. JIKA OK, GANTI ENGINE COOLANT TEMPERATURE SENSOR.: Ganti engine coolant temperature sensor (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-2 - C22-19 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-1 - C22-18 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-2 atau C22-19 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-2 - C22-19 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-1 - C22-18 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-2 atau C22-19 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C17-2 - C75-32 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C17-1 - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0117` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM00000187M02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM00000187M02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turboch
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam engine coolant temperature sensor Engine coolant temperature sensor ECM; Kondisi Deteksi: Open atau short circuit dalam engine coolant temperature sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short circuit dalam engine coolant temperature sensor Engine coolant temperature sensor ECM; Kondisi Deteksi: Short circuit dalam engine coola
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE COOLANT TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor engine coolant temperature sensor. -> Hubungkan terminal 1 dan 2 dari sisi konektor wire harness engine coolant temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ENGINE COOLANT TEMPERATURE SENSOR - ECM): Lepas hubungan konektor engine coolant temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor engine coolant temperature sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor engine coolant temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. ->
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ENGINE COOLANT TEMPERATURE SENSOR - ECM): Lepas hubungan konektor engine coolant temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor engine coolant temperature sensor. -> Hubungkan kembal
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. JIKA OK, GANTI ENGINE COOLANT TEMPERATURE SENSOR.: Ganti engine coolant temperature sensor (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-2 - C22-19 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-1 - C22-18 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-2 atau C22-19 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-2 - C22-19 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-1 - C22-18 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-2 atau C22-19 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C17-2 - C75-32 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C17-1 - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0118` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM00000187M02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM00000187M02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbo
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam engine coolant temperature sensor Engine coolant temperature sensor ECM; Kondisi Deteksi: Open atau short circuit dalam engine coolant temperature sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short circuit dalam engine coolant temperature sensor Engine coolant temperature sensor ECM; Kondisi Deteksi: Short circuit dalam engine coola
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE COOLANT TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor engine coolant temperature sensor. -> Hubungkan terminal 1 dan 2 dari sisi konektor wire harness engine coolant temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ENGINE COOLANT TEMPERATURE SENSOR - ECM): Lepas hubungan konektor engine coolant temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor engine coolant temperature sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor engine coolant temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. ->
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ENGINE COOLANT TEMPERATURE SENSOR - ECM): Lepas hubungan konektor engine coolant temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor engine coolant temperature sensor. -> Hubungkan kembal
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR. JIKA OK, GANTI ENGINE COOLANT TEMPERATURE SENSOR.: Ganti engine coolant temperature sensor (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-2 - C22-19 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-1 - C22-18 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C17-2 atau C22-19 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-2 - C22-19 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-1 - C22-18 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C17-2 atau C22-19 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C17-2 - C75-32 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C17-1 - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0120` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Malfungsi Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KJX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Malfungsi Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Malfungsi Sirkuit "A" Sensor 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) ECM; Kondisi Deteksi: Tegangan output VTA1 berfluktuasi dengan cepat melampaui batas bawah dan atas malfungsi selama 2 detik bila pedal akselerator di tekan (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) Sirkuit throttle positio
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / Throttle Position No. 1 dan Throttle Position No. 2. ->
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM (TEGANGAN VC): Lepas hubungan throttle body dengan konektor motor -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC THROTTLE POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi P
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) - C75-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) - C75-20 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) - C75-19 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-3 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) atau C75-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) atau C75-20 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) atau C75-19 (VTA2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C67-5 (VC) - C67-3 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P0121` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Problem Range / Performance pada Sirkuit "A" dari Throttle / Pedal Position Sensor / Switch (Dokumen: RM000000PF60KJX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Problem Range / Performance Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KVX) | [KONTROL MESIN 2T
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) ECM; Kondisi Deteksi: Tegangan output VTA1 berfluktuasi dengan cepat melampaui batas bawah dan atas malfungsi selama 2 detik bila pedal akselerator di tekan (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) Sirkuit throttle positio
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / Throttle Position No. 1 dan Throttle Position No. 2. ->
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM (TEGANGAN VC): Lepas hubungan throttle body dengan konektor motor -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC THROTTLE POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi P
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) - C75-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) - C75-20 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) - C75-19 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-3 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) atau C75-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) atau C75-20 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) atau C75-19 (VTA2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C67-5 (VC) - C67-3 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P0122` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM00000187N030X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM00000187N031X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Throttle position sensor Open atau short dalam sirkuit VLU Open dalam sirkuit VC ECM; Kondisi Deteksi: Output throttle position sensor (VLU) di bawah 0.2 V selama 3 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Throttle position sensor Open dalam sirkuit E2 Sirkuit VCdan VLU mengalami short-circuit ECM; Kondisi Deteksi: Output throttle position sensor (VLU) lebih tinggi dari 4.8 V
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan konektor throttle position sensor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor throttle position sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL ECM (VC TERMINAL): Lepas hubungan konektor throttle position sensor -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor throttle position sensor.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — GANTI DIESEL THROTTLE BODY ASSEMBLY: Ganti diesel throttle body assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON dan hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Actual Throttle position. -> Periks
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tunggu selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 3 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-1 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-3 (VTA) - C23-29 (VLU) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-2 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-1 (VC) atau C22-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-3 (VTA) atau C23-29 (VLU) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-2 (E2) atau C22-28 (E2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C9-1 (VC) - C9-2 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C9-1 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0123` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit "A" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM00000187N030X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit "A" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM00000187N031X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable N
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Throttle position sensor Open atau short dalam sirkuit VLU Open dalam sirkuit VC ECM; Kondisi Deteksi: Output throttle position sensor (VLU) di bawah 0.2 V selama 3 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Throttle position sensor Open dalam sirkuit E2 Sirkuit VCdan VLU mengalami short-circuit ECM; Kondisi Deteksi: Output throttle position sensor (VLU) lebih tinggi dari 4.8 V
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan konektor throttle position sensor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor throttle position sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL ECM (VC TERMINAL): Lepas hubungan konektor throttle position sensor -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor throttle position sensor.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — GANTI DIESEL THROTTLE BODY ASSEMBLY: Ganti diesel throttle body assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON dan hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Actual Throttle position. -> Periks
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tunggu selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 3 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-1 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-3 (VTA) - C23-29 (VLU) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-2 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-1 (VC) atau C22-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-3 (VTA) atau C23-29 (VLU) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C9-2 (E2) atau C22-28 (E2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C9-1 (VC) - C9-2 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C9-1 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0130` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Malfungsi Sirkuit Oxygen Sensor (Bank 1 Sensor 1) (Dokumen: RM000000ZQ900HX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Malfungsi Sirkuit Sensor Oksigen (Bank 1 Sensor 1) (Dokumen: RM000000ZQ900LX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Malfungsi Sirkuit Sensor Oksigen (Bank 1 Sensor 1) (
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Open atau short dalam sirkuit heated oxygen sensor (sensor 1) Heated oxygen sensor (sensor 1) ECM; Kondisi Deteksi: Tegangan output heated oxygen sensor adalah di bawah 0.45 V selama 75 detik atau lebih (1 trip detection logic).; [KONTROL MESIN 2TR-FE] Area Gangguan: Open atau short sirkuit pada heated oxygen sensor (sensor 1) Heated oxygen sensor (sensor 1) ECM; Kondisi Deteksi: Voltase output heated oxygen
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA DTC YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (OUTPUT VOLTAGE OF HEATED OXYGEN SENSOR): Hubungkan intelligent tester ke DLC3 -> Start mesin dan hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / O2S B1S1. -> Panaskan sensor heated oxygen dengan menghidupkan mesin pada 2.500 rpm
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — LAKUKAN KONFIRMASI POLA PENGENDARAAN: Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi Pola Pengendaraan.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0130 MUNCUL LAGI): Hubungkan intelligent tester ke DLC3. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT/ Utility / All Readiness. -> Input DTC: P0130. -> Periksa bahwa monitor DTC adalah NORMAL. Jika monitor DTC adal
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PASTIKAN BILA BAHAN BAKAR KENDARAAN TERSENDAT DI MASA LALU: Apakah sebelumnya kendaraan pernah kehabisan bahan bakar?
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERIKSA SELANG PCV: Periksa sambungan selang PCV (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — MEMERIKSA HEATED OXYGEN SENSOR: Periksa heated oxygen sensor (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — MEMERIKSA INTEGRATION RELAY NO.1 (MAIN) (TEGANGAN POWER SOURCE): Lepas integration relay No. 1 dari relay block ruang mesin dan junction block. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: 1J-5 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-1 (HT1A) - C75-1 (HA1A) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-3 (OX1A) - C75-21 (A1A+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-4 (E2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-1 (HT1A) atau C75-1 (HA1A) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-3 (OX1A) atau C75-21 (A1A+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Voltase Standar: 1J-5 - Body ground (Ignition switch ON)` : **11 sampai 14 V**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C78-1 (HT1A) - C75-1 (HA1A) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0135` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit Oxygen Sensor Heater (Bank 1 Sensor 1) (Dokumen: RM000000ZQC00HX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Oxygen Sensor Heater Circuit (Bank 1 Sensor 1) (Dokumen: RM000000ZQC00LX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Oxygen Sensor Heater Circuit (Bank 1 Sensor 1) (Dokumen: RM
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Open atau short dalam sirkuit heater dari oxygen sensor Heated oxygen sensor ECM; Kondisi Deteksi: Open atau short circuit dalam oxygen sensor selama 0.5 detik atau lebih (1 trip detection logic).; [KONTROL MESIN 2TR-FE] Area Gangguan: Open arau short dalam sirkuit heater pada oxygen sensor Heated oxygen sensor ECM; Kondisi Deteksi: Open atau short dalam sirkuir heater pada oxygen sensor selama 0.5 detik ata
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA HEATED OXYGEN SENSOR: Periksa heated oxygen sensor (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA TEGANGAN TERMINAL (+B DARI HEATED OXYGEN SENSOR): Lepas hubungan konektor heated oxygen sensor. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (HEATED OXYGEN SENSOR - ECM): Lepas hubungan konektor heated oxygen sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi P
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — MEMERIKSA INTEGRATION RELAY NO.1 (MAIN): Periksa the No. 1 integration relay (EDU) (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (HEATED OXYGEN SENSOR - INTEGRATION RELAY NO.1): Lepas hubungan konektor heated oxygen sensor. -> Lepas integration relay No. 1 dari relay block ruang mesin dan junction block. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI HEATED OXYGEN SENSOR
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C78-2 (+B) - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-1 (HT1A) - C75-1 (HA1A) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-1 (HT1A) atau C75-1 (HA1A) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-2 (+B) - 1J-5 (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C78-2 (+B) atau 1J-5 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Voltase Standar: C78-2 (+B) - Body ground (Ignition switch ON)` : **11 sampai 14 V**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C78-1 (HT1A) - C75-1 (HA1A) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C78-1 (HT1A) atau C75-1 (HA1A) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0168` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Temperatur Bahan Bakar Terlalu Tinggi (Dokumen: RM00000187Z038X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Temperatur Bahan Bakar Terlalu Tinggi (Dokumen: RM00000187Z039X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Temperatur Bahan Bakar Terlalu
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Fuel cooler (Problem pendingin bahan bakar) Saluran bahan bakar atau fuel filter tersumbat; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Fuel cooler (Problem pendingin bahan bakar) Saluran bahan bakar atau fuel filter tersumbat; [KONTROL MESIN 1KD-FTV] Area Gangguan: Fuel cooler (Masalah pada cooling fuel) Fuel line atau fuel filter tersumbat; [KONTROL MESIN 2KD-FTV] Area Gangguan: Fuel cooler (Masalah pada cool
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DI SAMPING DTC P0168): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MELEPAS FUEL SUPPLY PUMP ASSEMBLY: Lakukan pemeriksan visual dari bagian luar fuel supply pump assembly dan memeriksa bahwa tidak ada kebocoran bahan bakar.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA SISTEM BAHAN BAKAR: Periksa apakah kotoran menyumbat sirip fuel cooler. Bersihkan sirip jika tersumbat dengan kotoran.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY: Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — LAKUKAN INISIALISASI SUPPLY PUMP BAHAN BAKAR: Lakukan inisialisasi fuel supply pump (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke-ON dan hidupkan tester. -> Hidupkan mesin. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Fuel Temperature. -> Kendara
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — LANJUTKAN KE BAGAN DTC

### DTC `P0180` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit "A" Fuel Temperature Sensor (Dokumen: RM00000188B02QX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit "A" Fuel Temperature Sensor (Dokumen: RM00000188B02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit "A" Fuel Temperature Senso
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel temperature sensor Fuel temperature sensor (fuel supply pump assembly) ECM; Kondisi Deteksi: Open atau short circuit dalam fuel temperature sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short circuit dalam fuel temperature sensor Fuel temperature sensor (fuel supply pump assembly) ECM; Kondisi Deteksi: Short circuit dalam fuel t
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (FUEL TEMPERATURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT/ Data List /Fuel Temp. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor fuel temperature sensor. -> Hubungkan terminal 2 dan 1 dari konektor fuel temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini:
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (FUEL TEMPERATURE SENSOR): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (FUEL TEMPERATURE SENSOR - ECM): Lepas hubungan konektor fuel temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel temperature sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM. BILA OK, GANTI ECM.: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor fuel temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT/ Data List /Fuel Temp. -> Baca nilainya.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (FUEL TEMPERATURE SENSOR): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (FUEL TEMPERATURE SENSOR - ECM): Lepas hubungan konektor fuel temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel temperature sensor. -> Hubungkan kembali konektor ECM.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-2 atau C22-29 (THF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-2 atau C22-29 (THF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0182` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit "A" Fuel Temperature Sensor (Dokumen: RM00000188B02QX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit "A" Fuel Temperature Sensor (Dokumen: RM00000188B02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel temperature sensor Fuel temperature sensor (fuel supply pump assembly) ECM; Kondisi Deteksi: Open atau short circuit dalam fuel temperature sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short circuit dalam fuel temperature sensor Fuel temperature sensor (fuel supply pump assembly) ECM; Kondisi Deteksi: Short circuit dalam fuel t
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (FUEL TEMPERATURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT/ Data List /Fuel Temp. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor fuel temperature sensor. -> Hubungkan terminal 2 dan 1 dari konektor fuel temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini:
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (FUEL TEMPERATURE SENSOR): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (FUEL TEMPERATURE SENSOR - ECM): Lepas hubungan konektor fuel temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel temperature sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM. BILA OK, GANTI ECM.: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor fuel temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT/ Data List /Fuel Temp. -> Baca nilainya.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (FUEL TEMPERATURE SENSOR): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (FUEL TEMPERATURE SENSOR - ECM): Lepas hubungan konektor fuel temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel temperature sensor. -> Hubungkan kembali konektor ECM.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-2 atau C22-29 (THF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-2 atau C22-29 (THF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0183` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit "A" Fuel Temperature Sensor (Dokumen: RM00000188B02QX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit "A" Fuel Temperature Sensor (Dokumen: RM00000188B02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Hi
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel temperature sensor Fuel temperature sensor (fuel supply pump assembly) ECM; Kondisi Deteksi: Open atau short circuit dalam fuel temperature sensor selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short circuit dalam fuel temperature sensor Fuel temperature sensor (fuel supply pump assembly) ECM; Kondisi Deteksi: Short circuit dalam fuel t
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (FUEL TEMPERATURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT/ Data List /Fuel Temp. -> Baca nilainya.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (PERIKSA TERHADAP OPEN DALAM WIRE HARNESS): Lepas hubungan konektor fuel temperature sensor. -> Hubungkan terminal 2 dan 1 dari konektor fuel temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini:
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (FUEL TEMPERATURE SENSOR): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (FUEL TEMPERATURE SENSOR - ECM): Lepas hubungan konektor fuel temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel temperature sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM. BILA OK, GANTI ECM.: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor fuel temperature sensor. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT/ Data List /Fuel Temp. -> Baca nilainya.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (FUEL TEMPERATURE SENSOR): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (FUEL TEMPERATURE SENSOR - ECM): Lepas hubungan konektor fuel temperature sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel temperature sensor. -> Hubungkan kembali konektor ECM.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C19-2 atau C22-29 (THF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C19-2 atau C22-29 (THF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C19-2 - C22-29 (THF) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: C19-1 - C22-28 (E2) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0190` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM000001880046X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM000001880047X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Fuel Rail Pressure Sensor (Dok
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) Bahan bakar tidak sesuai Bahan bakar beku ECM; Kondisi Deteksi: Tegangan output fuel pressure sensor dipertahankan pada nilai yang tetap selama 90 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (SENSOR TEKANAN BAHAN BAKAR - ECM): Lepas hubungan konektor fuel pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel pressure sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA ECM (TEGANGAN FUEL PRESSURE SENSOR): Lepas hubungan konektor fuel pressure sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor fuel pressure sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI PRESSURE SENSOR (COMMON RAIL ASSEMBLY): Mengganti common rail assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0087, P0190, P0192, P0193): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 60 detik, dan kemudian naikkan putaran mesin ke 2500 rpm dengan cepat secara berulang-kali
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) - C22-26 (PCR1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) - C22-33 (PCR2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-1 (VCS) - C23-2 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-6 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-4 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-3 (E2S) - C23-1 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) atau C22-26 (PCR1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) atau C22-33 (PCR2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0191` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Range/Performance pada Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM00000187H030X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Range/Performance pada Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM00000187H031X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turboch
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail) ECM; Kondisi Deteksi: Perbedaan antara output tegangan utama dan sub dari fuel pressure sensor adalah 0.04 V atau kurang, atau 1.06 V atau lebih tinggi selama 1 detik atau lebih (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (FUEL PRESS DAN TARGET COMMON RAIL PRESSURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Fuel Press, dan Target Common Rail Pressure. -> Hidupkan mesin. -> Periksa per
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (SENSOR TEKANAN BAHAN BAKAR - ECM): Lepas hubungan konektor fuel pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel pressure sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0191): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 1 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI COMMON RAIL: Mengganti common rail (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0191): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 1 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) - C22-26 (PCR1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) - C22-33 (PCR2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-1 (VCS) - C23-2 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-6 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-4 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-3 (E2S) - C23-1 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) atau C22-26 (PCR1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) atau C22-33 (PCR2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0192` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM000001880046X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM000001880047X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low Inpu
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) Bahan bakar tidak sesuai Bahan bakar beku ECM; Kondisi Deteksi: Tegangan output fuel pressure sensor dipertahankan pada nilai yang tetap selama 90 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (SENSOR TEKANAN BAHAN BAKAR - ECM): Lepas hubungan konektor fuel pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel pressure sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA ECM (TEGANGAN FUEL PRESSURE SENSOR): Lepas hubungan konektor fuel pressure sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor fuel pressure sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI PRESSURE SENSOR (COMMON RAIL ASSEMBLY): Mengganti common rail assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0087, P0190, P0192, P0193): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 60 detik, dan kemudian naikkan putaran mesin ke 2500 rpm dengan cepat secara berulang-kali
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) - C22-26 (PCR1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) - C22-33 (PCR2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-1 (VCS) - C23-2 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-6 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-4 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-3 (E2S) - C23-1 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) atau C22-26 (PCR1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) atau C22-33 (PCR2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0193` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM000001880046X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit Fuel Rail Pressure Sensor (Dokumen: RM000001880047X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High I
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) Bahan bakar tidak sesuai Bahan bakar beku ECM; Kondisi Deteksi: Tegangan output fuel pressure sensor dipertahankan pada nilai yang tetap selama 90 detik (1 trip detection logic).; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short circuit dalam fuel pressure sensor Fuel pressure sensor (common rail assembly) 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA WIRE HARNESS DAN KONEKTOR (SENSOR TEKANAN BAHAN BAKAR - ECM): Lepas hubungan konektor fuel pressure sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor fuel pressure sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA ECM (TEGANGAN FUEL PRESSURE SENSOR): Lepas hubungan konektor fuel pressure sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor fuel pressure sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI PRESSURE SENSOR (COMMON RAIL ASSEMBLY): Mengganti common rail assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0087, P0190, P0192, P0193): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 60 detik, dan kemudian naikkan putaran mesin ke 2500 rpm dengan cepat secara berulang-kali
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) - C22-26 (PCR1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) - C22-33 (PCR2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-1 (VCS) - C23-2 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-6 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-4 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-3 (E2S) - C23-1 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-5 (PR) atau C22-26 (PCR1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C16-2 (PR2) atau C22-33 (PCR2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0200` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Injector/Open (Dokumen: RM00000187V026X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Injector/Open (Dokumen: RM00000187V027X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Injector/Open (Dokumen: RM00000187V028X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit injector Injector assembly Injector driver ECM; Kondisi Deteksi: Open atau short dalam sirkuit injector driver atau injector bahan bakar (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sirkuit injector Injector assembly Injector driver ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit injector drive Injector assem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL SUMBER TENAGA INJECTOR DRIVER: Lepas hubungan konektor injector driver. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor injector driver.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA INJECTOR ASSEMBLY (RESISTANCE): Periksa injector assembly (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INJECTOR ASSEMBLY - INJECTOR DRIVER): Lepas hubungan konektor injector assembly. -> Lepas hubungan konektor injector driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor injector assembly. -> Hubungkan kembali konektor injector 
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (INJECTOR DRIVER - ECM): Lepas hubungan konektor injector driver. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor injector driver. -> Hubungkan kembali konektor ECM.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI INJECTOR DRIVER: Mengganti injector driver (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Hidupkan mesin dan idle selama 10 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. ->
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — LANJUTKAN KE SIRKUIT INJECTOR: Lanjutkan ke sirkuit injector (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C43-2 (+B) - C43-3 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C1-1 - C43-1 (IJ1+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C1-2 - C44-6 (IJ1-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C2-1 - C43-6 (IJ2+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C2-2 - C44-4 (IJ2-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C3-1 - C43-5 (IJ3+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C3-2 - C44-2 (IJ3-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C4-1 - C44-3 (IJ4+) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0220` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KJX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit "B" Sensor / Switch Posisi Throttle / Ped
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) ECM; Kondisi Deteksi: Tegangan output VTA1 berfluktuasi dengan cepat melampaui batas bawah dan atas malfungsi selama 2 detik bila pedal akselerator di tekan (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) Sirkuit throttle positio
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / Throttle Position No. 1 dan Throttle Position No. 2. ->
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM (TEGANGAN VC): Lepas hubungan throttle body dengan konektor motor -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC THROTTLE POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi P
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) - C75-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) - C75-20 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) - C75-19 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-3 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) atau C75-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) atau C75-20 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) atau C75-19 (VTA2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C67-5 (VC) - C67-3 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P0222` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Low Input pada Sirkuit "B" Sensor /Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KJX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Low Input Sirkuit "B" Sensor /Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Low Input Sirkuit "B" Sens
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) ECM; Kondisi Deteksi: Tegangan output VTA1 berfluktuasi dengan cepat melampaui batas bawah dan atas malfungsi selama 2 detik bila pedal akselerator di tekan (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) Sirkuit throttle positio
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / Throttle Position No. 1 dan Throttle Position No. 2. ->
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM (TEGANGAN VC): Lepas hubungan throttle body dengan konektor motor -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC THROTTLE POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi P
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) - C75-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) - C75-20 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) - C75-19 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-3 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) atau C75-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) atau C75-20 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) atau C75-19 (VTA2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C67-5 (VC) - C67-3 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P0223` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] High Input pada Sirkuit "B" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KJX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] High Input Sirkuit "B" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] High Input Sirkuit "B" Sen
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) ECM; Kondisi Deteksi: Tegangan output VTA1 berfluktuasi dengan cepat melampaui batas bawah dan atas malfungsi selama 2 detik bila pedal akselerator di tekan (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) Sirkuit throttle positio
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / Throttle Position No. 1 dan Throttle Position No. 2. ->
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM (TEGANGAN VC): Lepas hubungan throttle body dengan konektor motor -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC THROTTLE POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi P
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) - C75-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) - C75-20 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) - C75-19 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-3 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) atau C75-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) atau C75-20 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) atau C75-19 (VTA2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C67-5 (VC) - C67-3 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P0327` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Low Input pada Sirkuit Knock Sensor 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT0IXX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Low Input Sirkuit Sensor Knock 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT0J9X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Low Input Sirkuit Sensor K
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Short dalam sirkuit knock sensor Knock sensor ECM; Kondisi Deteksi: Tegangan output dari knock sensor (untuk Bank 1 Sensor 1) adalah 0.5 V atau kurang (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Open dalam sirkuit knock sensor Knock sensor ECM; Kondisi Deteksi: Tegangan output dari knock sensor (untuk Bank 1 Sensor 1) adalah 4.5 V atau kurang (1 trip detection logic).; [ENGINE CONTROL 1
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA KNOCK SENSOR: Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM: Lepas hubungan konektor CS1. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (ECM - KNOCK SENSOR): Lepas hubungan konektor ECM. -> Lepas hubungan konektor knock sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI KNOCK SENSOR
  - Langkah 1 (KONTROL MESIN 2TR-FE) — MEMERIKSA KNOCK SENSOR: Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C75-29 (KNK1) - C75-30 (EKNK) (20°C (68°F))` : **120 sampai 280 kΩ**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: Konektor perempuan CS1 1 - 2 (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-2 - C75-29 (KNK1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-1 - C75-30 (EKNK) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-2 atau C75-29 (KNK1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-1 atau C75-30 (EKNK) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C75-29 (KNK1) - C75-30 (EKNK) (20°C (68°F))` : **120 sampai 280 kΩ**
  - `[KONTROL MESIN 2TR-FE] Voltase Standar: Konektor CS1 female 1 - 2 (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P0328` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] High Input pada Sirkuit Knock Sensor 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT0IXX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] High Input pada Sirkuit Sensor Knock 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT0J9X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] High Input pada Sir
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Short dalam sirkuit knock sensor Knock sensor ECM; Kondisi Deteksi: Tegangan output dari knock sensor (untuk Bank 1 Sensor 1) adalah 0.5 V atau kurang (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Open dalam sirkuit knock sensor Knock sensor ECM; Kondisi Deteksi: Tegangan output dari knock sensor (untuk Bank 1 Sensor 1) adalah 4.5 V atau kurang (1 trip detection logic).; [ENGINE CONTROL 1
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA KNOCK SENSOR: Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM: Lepas hubungan konektor CS1. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (ECM - KNOCK SENSOR): Lepas hubungan konektor ECM. -> Lepas hubungan konektor knock sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI KNOCK SENSOR
  - Langkah 1 (KONTROL MESIN 2TR-FE) — MEMERIKSA KNOCK SENSOR: Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C75-29 (KNK1) - C75-30 (EKNK) (20°C (68°F))` : **120 sampai 280 kΩ**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: Konektor perempuan CS1 1 - 2 (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-2 - C75-29 (KNK1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-1 - C75-30 (EKNK) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-2 atau C75-29 (KNK1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: S1-1 atau C75-30 (EKNK) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C75-29 (KNK1) - C75-30 (EKNK) (20°C (68°F))` : **120 sampai 280 kΩ**
  - `[KONTROL MESIN 2TR-FE] Voltase Standar: Konektor CS1 female 1 - 2 (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P0335` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Crankshaft Position Sensor "A" (Dokumen: RM00000187F02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Crankshaft Position Sensor "A" (Dokumen: RM00000187F02TX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Crankshaft Position 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit crankshaft position sensor Crankshaft position sensor Crankshaft position sensor plate No. 1 (crankshaft) ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit crankshaft position sensor Crankshaft position sensor Crankshaft position sensor plate No. 1 (crankshaft) Camshaft timing pulley ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sir
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA CRANKSHAFT POSITION SENSOR: Periksa crankshaft position sensor (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (CRANKSHAFT POSITION SENSOR - ECM): Lepas hubungan konektor crankshaft position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor crankshaft position sensor. -> Hubungkan kembali konektor ECM
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA CRANKSHAFT POSITION SENSOR (PEMASANGAN SENSOR): Periksa pemasangan sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA CRANKSHAFT POSITION SENSOR PLATE NO.1: Periksa gigi plat sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA CAMSHAFT TIMING PULLEY: Periksa gigi dari camshaft timing pulley.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI CRANKSHAFT POSITION SENSOR: Ganti crankshaft position sensor (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-1 (NE+) - C22-27 (NE+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-2 (NE-) - C22-34 (NE-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-3 (E) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-1 (NE+) atau C22-27 (NE+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-2 (NE-) atau C22-34 (NE-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C6-1 (NE+) - C22-27 (NE+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C6-2 (NE-) - C22-34 (NE-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C6-3 (E) - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `P0339` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Intermittent pada Sirkuit "A" Crankshaft Position Sensor (Dokumen: RM00000187F02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Intermittent pada Sirkuit "A" Crankshaft Position Sensor (Dokumen: RM00000187F02TX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turboch
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit crankshaft position sensor Crankshaft position sensor Crankshaft position sensor plate No. 1 (crankshaft) ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit crankshaft position sensor Crankshaft position sensor Crankshaft position sensor plate No. 1 (crankshaft) Camshaft timing pulley ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sir
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA CRANKSHAFT POSITION SENSOR: Periksa crankshaft position sensor (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (CRANKSHAFT POSITION SENSOR - ECM): Lepas hubungan konektor crankshaft position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor crankshaft position sensor. -> Hubungkan kembali konektor ECM
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA CRANKSHAFT POSITION SENSOR (PEMASANGAN SENSOR): Periksa pemasangan sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA CRANKSHAFT POSITION SENSOR PLATE NO.1: Periksa gigi plat sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA CAMSHAFT TIMING PULLEY: Periksa gigi dari camshaft timing pulley.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI CRANKSHAFT POSITION SENSOR: Ganti crankshaft position sensor (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-1 (NE+) - C22-27 (NE+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-2 (NE-) - C22-34 (NE-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-3 (E) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-1 (NE+) atau C22-27 (NE+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C6-2 (NE-) atau C22-34 (NE-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C6-1 (NE+) - C22-27 (NE+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C6-2 (NE-) - C22-34 (NE-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C6-3 (E) - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `P0340` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit "A" Camshaft Position Sensor (Bank 1 atau Single Sensor) (Dokumen: RM00000187G02RX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit "A" Camshaft Position Sensor (Bank 1 atau Single Sensor) (Dokumen: RM00000187G02SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Noz
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit camshaft position sensor Camshaft position sensor Camshaft timing pulley Crank shaft position sensor ECM; Kondisi Deteksi: STA on: Tidak ada sinyal camshaft position sensor dikirim ke ECM saat cranking selama 4 detik atau lebih (2 trip detection logic); [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sirkuit camshaft position sensor Camshaft position sensor Camsha
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA CAMSHAFT POSITION SENSOR: Periksa camshaft position sensor (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (CAMSHAFT POSITION SENSOR - ECM): Lepas hubungan konektor camshaft position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor camshaft position sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA CAMSHAFT POSITION SENSOR (PEMASANGAN SENSOR): Periksa pemasangan sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA CAMSHAFT TIMING PULLEY: Periksa kondisi dari camshaft timing pulley.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT CRANKSHAFT POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tunggu selama 30 detik atau lebih. -> Hidupkan mesin dan biarkan idle selama 4 deti
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI CAMSHAFT POSITION SENSOR: Ganti camshaft position sensor (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C7-1 - C23-23 (G+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C7-2 - C23-31 (G-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C7-1 atau C23-23 (G+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C7-2 atau C23-31 (G-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C7-1 - C23-23 (G+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C7-2 - C23-31 (G-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C7-1 atau C23-23 (G+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C7-2 atau C23-31 (G-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0341` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Range / Performance pada Sirkuit "A" dari Crankshaft Position Sensor (Bank 1 atau Single Sensor) (Dokumen: RM000000WBZ0ERX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Camshaft Position Sensor "A" Circuit Range / Performance (Bank 1 atau Single Sensor) (Dokumen: RM000000WBZ0F1X) | [KONTRO
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Open atau short dalam sirkuit camshaft position sensor Camshaft position sensor Camshaft timing gear assembly Timing chain terhadap lompat gigi intake camshaft ECM; Kondisi Deteksi: Selama crankshaft berputar dua kali, sinyal camshaft position sensor meng-input ke ECM 12 kali atau lebih (1 trip detection logic); [ENGINE CONTROL 1TR-FE] Area Gangguan: Idling; Kondisi Deteksi: 5 V/DIV, 20 ms/DIV; [KONTROL MESI
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA CAMSHAFT POSITION SENSOR (TAHANAN): Periksa camshaft position sensor (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (CAMSHAFT POSITION SENSOR - ECM): Lepas hubungan konektor camshaft position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA PEMASANGAN SENSOR (CAMSHAFT POSITION SENSOR): Periksa camshaft position sensor.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — MEMERIKSA CAMSHAFT TIMING GEAR ASSEMBLY (GIGI): Periksa gigi dari camshaft timing gear assembly.
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — GANTI CAM POSITION SENSOR: Ganti camshaft position sensor (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan biarkan idle selama 10 menit atau lebih. -> Masuk ke menu berikut ini: Powertrain / E
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI CAMSHAFT POSITION SENSOR
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C68-1 - C75-26 (G2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C68-2 - C75-34 (NE-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C68-1 atau C75-26 (G2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C68-2 atau C75-34 (NE-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C68-1 - C75-26 (G2) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C68-2 - C75-34 (NE-) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C68-1 atau C75-26 (G2) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C68-2 atau C75-34 (NE-) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0351` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Ignition Coil "A" (Dokumen: RM000000XH40KRX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Secondary / Ignition Coil "A" Primary (Dokumen: RM000000XH40L2X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Secondary / Ignition Coil "A" Primary (Dokumen: RM000000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem ignition Open atau short dalam sirkuit IGF1 atau sirkuit IGT (1 sampai 4) antara ignition coil dan ECM Ignition coil assembly No. 1 sampai No. 4 ECM; Kondisi Deteksi: Tidak ada sinyal IGF yang dikirim ke ECM sementara mesin sedang hidup (ECM tidak menerima sinyal IGF meskipun ECM mengirim sinyal IGT ke igniter) (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Idling; Kondisi Deteksi: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (IGNITION COIL - ECM): Lepas hubungan konektor ignition coil. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan ignition coil assembly (antara cylinder No. 1 sampai cylinder No. 4 ). -> Jal
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — GANTI IGNITION COIL ASSEMBLY
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C70-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C71-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C72-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C73-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C70-1 (+B) - C70-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C71-1 (+B) - C71-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C72-1 (+B) - C72-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C73-1 (+B) - C73-4 (GND) (ignition switch ON)` : **11 sampai 14 V**

### DTC `P0352` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Ignition Coil "B" (Dokumen: RM000000XH40KRX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Primer/ Sekunder Koil Pengapian "B" (Dokumen: RM000000XH40L2X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Primer/ Sekunder Koil Pengapian "B" (Dokumen: RM000000XH40
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem ignition Open atau short dalam sirkuit IGF1 atau sirkuit IGT (1 sampai 4) antara ignition coil dan ECM Ignition coil assembly No. 1 sampai No. 4 ECM; Kondisi Deteksi: Tidak ada sinyal IGF yang dikirim ke ECM sementara mesin sedang hidup (ECM tidak menerima sinyal IGF meskipun ECM mengirim sinyal IGT ke igniter) (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Idling; Kondisi Deteksi: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (IGNITION COIL - ECM): Lepas hubungan konektor ignition coil. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan ignition coil assembly (antara cylinder No. 1 sampai cylinder No. 4 ). -> Jal
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — GANTI IGNITION COIL ASSEMBLY
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C70-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C71-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C72-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C73-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C70-1 (+B) - C70-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C71-1 (+B) - C71-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C72-1 (+B) - C72-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C73-1 (+B) - C73-4 (GND) (ignition switch ON)` : **11 sampai 14 V**

### DTC `P0353` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Ignition Coil "C" (Dokumen: RM000000XH40KRX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Primer/ Sekunder Koil Pengapian "C" (Dokumen: RM000000XH40L2X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Primer/ Sekunder Koil Pengapian "C" (Dokumen: RM000000XH40
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem ignition Open atau short dalam sirkuit IGF1 atau sirkuit IGT (1 sampai 4) antara ignition coil dan ECM Ignition coil assembly No. 1 sampai No. 4 ECM; Kondisi Deteksi: Tidak ada sinyal IGF yang dikirim ke ECM sementara mesin sedang hidup (ECM tidak menerima sinyal IGF meskipun ECM mengirim sinyal IGT ke igniter) (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Idling; Kondisi Deteksi: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (IGNITION COIL - ECM): Lepas hubungan konektor ignition coil. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan ignition coil assembly (antara cylinder No. 1 sampai cylinder No. 4 ). -> Jal
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — GANTI IGNITION COIL ASSEMBLY
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C70-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C71-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C72-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C73-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C70-1 (+B) - C70-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C71-1 (+B) - C71-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C72-1 (+B) - C72-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C73-1 (+B) - C73-4 (GND) (ignition switch ON)` : **11 sampai 14 V**

### DTC `P0354` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Ignition Coil "D" (Dokumen: RM000000XH40KRX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Primer/ Sekunder Koil Pengapian "D" (Dokumen: RM000000XH40L2X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Primer/ Sekunder Koil Pengapian "D" (Dokumen: RM000000XH40
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Sistem ignition Open atau short dalam sirkuit IGF1 atau sirkuit IGT (1 sampai 4) antara ignition coil dan ECM Ignition coil assembly No. 1 sampai No. 4 ECM; Kondisi Deteksi: Tidak ada sinyal IGF yang dikirim ke ECM sementara mesin sedang hidup (ECM tidak menerima sinyal IGF meskipun ECM mengirim sinyal IGT ke igniter) (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Idling; Kondisi Deteksi: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (IGNITION COIL - ECM): Lepas hubungan konektor ignition coil. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan ignition coil assembly (antara cylinder No. 1 sampai cylinder No. 4 ). -> Jal
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — GANTI IGNITION COIL ASSEMBLY
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA IGNITION COIL ASSEMBLY (POWER SOURCE): Lepas hubungan konektor ignition coil. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Putar ignition switch ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C70-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C71-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C72-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C73-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C70-1 (+B) - C70-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C71-1 (+B) - C71-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C72-1 (+B) - C72-4 (GND) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C73-1 (+B) - C73-4 (GND) (ignition switch ON)` : **11 sampai 14 V**

### DTC `P0400` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Aliran Exhaust Gas Recirculation (Dokumen: RM0000041P800SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Aliran Exhaust Gas Recirculation (Dokumen: RM0000041P800TX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Aliran Exhaust Gas Recirculation (Dokume
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: EGR valve macet EGR valve tidak bergerak lembut Electric vacuum regulating valve assembly Vacuum switching valve (untuk EGR Cut) Sirkuit electric vacuum regulating valve assembly Sirkuit vacuum switching valve (untuk EGR Cut) Saluran EGR tersumbat antara exhaust manifold dan intake manifold Mass air flow meter Sistem intake (bocor atau tersumbat) Sistem exhaust (gas buang bocor) ECM; Kondisi Deteksi: Mass a
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA SETIAP DTC LAINNYA (DI SAMPING DTC P0400): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (ACTIVATE THE EGR VALVE CLOSE): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan panaskan mesin,dan memastikan switch A/C dan semua accessory off. -> Putar ignition switch ke off. Tunggu selama 30 detik, dan kemudian start kembali mesin. -> Hidupkan tester. -> 
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA SLANG VACUUM: Periksa slang vacuum.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA ELECTRIC VACUUM REGULATING VALVE ASSEMBLY: Periksa electric vacuum regulating valve assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA VACUUM SWITCHING VALVE (UNTUK EGR CUT): Periksa vacuum switching valve (untuk EGR cut) (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA ELECTRIC EGR CONTROL VALVE ASSEMBLY (OPERASI EGR VALVE ): Periksa electric EGR control valve assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA ENDAPAN (SALURAN EGR): Memeriksa penyumbatan disaluran gas EGR antara exhaust manifold dan electric EGR control valve assembly.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI SELANG VACUUM: Perbaiki atau ganti selang vacuum.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Referensi: Open (55%) (Tekanan atmosfer: 101 kPa Temperatur udara masuk: 30℃ (86℉) Temperatur cairan pendingin mesi` : **3,0 sampai 9,0 gm/s**
  - `[ENGINE CONTROL 1KD-FTV] Referensi: Close (0%) (Tekanan atmosfer: 101 kPa Temperatur udara masuk: 30℃ (86℉) Temperatur cairan pendingin mesi` : **15 sampai 22 gm/s**
  - `[ENGINE CONTROL 2KD-FTV] Referensi: Open (55%) (Tekanan atmosfer: 101 kPa Temperatur udara masuk: 30℃ (86℉) Temperatur cairan pendingin mesi` : **3,0 sampai 9,0 gm/s**
  - `[ENGINE CONTROL 2KD-FTV] Referensi: Close (0%) (Tekanan atmosfer: 101 kPa Temperatur udara masuk: 30℃ (86℉) Temperatur cairan pendingin mesi` : **13 sampai 20 gm/s**
  - `[ENGINE CONTROL 2KD-FTV] Referensi: Close (0%) (Tekanan atmosfer: 101 kPa Temperatur udara masuk: 30℃ (86℉) Temperatur cairan pendingin mesi` : **15 sampai 22 gm/s**
  - `[KONTROL MESIN 1KD-FTV] Referensi: Terbuka (55%) (Tekanan atmosfir: 101 kPa Temperatur udara intake: 30°C (86°F) Temperatur engine coolant: ` : **3.0 sampai 9.0 gm/s**
  - `[KONTROL MESIN 1KD-FTV] Referensi: Tertutup (0%) (Tekanan atmosfir: 101 kPa Temperatur udara intake: 30°C (86°F) Temperatur engine coolant: ` : **15 sampai 22 gm/s**
  - `[KONTROL MESIN 2KD-FTV] Referensi: Terbuka (55%) (Tekanan atmosfir: 101 kPa Temperatur udara intake: 30°C (86°F) Temperatur engine coolant: ` : **3.0 sampai 9.0 gm/s**

### DTC `P0405` — [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low pada Sirkuit "A" Exhaust Gas Recirculation Sensor (Dokumen: RM00000187T03SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low pada Sirkuit "A" Exhaust Gas Recirculation Sensor (Dokumen: RM00000187T03TX) | [KONTROL MESIN 2KD-FTV — SISTEM ECD]
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sirkuit EGR valve position sensor EGR valve position sensor ECM; Kondisi Deteksi: Tegangan output EGR valve position sensor di bawah 0.1 V selama lebih dari 5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan output EGR valve position sensor lebih dari 4.9 V untuk lebih tinggi dari 5 detik (1 trip detection logic).; [KONTROL MESIN 2KD-FTV] Area Gangguan: Open atau short dalam 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — PERIKSA TEGANGAN TERMINAL (KONEKTOR EGR VALVE POSITION SENSOR): Lepas hubungan konektor EGR valve position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor electric vacuum regulating valve assembly.
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — MEMERIKSA EGR VALVE POSITION SENSOR: Periksa EGR valve position sensor (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (EGR VALVE POSITION SENSOR - ECM): Lepas hubungan konektor EGR valve position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor electric vacuum regulating valve assembly. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 2KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 2KD-FTV) — GANTI ELECTRIC EGR CONTROL VALVE ASSEMBLY: Ganti electric EGR control valve assembly (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 2KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 2KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON selama 5 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 8 (ENGINE CONTROL 2KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C56-1 (VC) - C56-2 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-1 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-3 (EGLS) - C23-33 (EGLS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-2 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-1 (VC) atau C22-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-3 (EGLS) atau C23-33 (EGLS) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2KD-FTV] Voltase Standar: C56-1 (VC) - C56-2 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[KONTROL MESIN 2KD-FTV] Tahanan Standar: C56-1 (VC) - C22-18 (VC) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0406` — [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Sirkuit "A" pada Exhaust Gas Recirculation Sensor (Dokumen: RM00000187T03SX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Sirkuit "A" pada Exhaust Gas Recirculation Sensor (Dokumen: RM00000187T03TX) | [KONTROL MESIN 2KD-FTV — SISTEM EC
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sirkuit EGR valve position sensor EGR valve position sensor ECM; Kondisi Deteksi: Tegangan output EGR valve position sensor di bawah 0.1 V selama lebih dari 5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan output EGR valve position sensor lebih dari 4.9 V untuk lebih tinggi dari 5 detik (1 trip detection logic).; [KONTROL MESIN 2KD-FTV] Area Gangguan: Open atau short dalam 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — PERIKSA TEGANGAN TERMINAL (KONEKTOR EGR VALVE POSITION SENSOR): Lepas hubungan konektor EGR valve position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor electric vacuum regulating valve assembly.
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — MEMERIKSA EGR VALVE POSITION SENSOR: Periksa EGR valve position sensor (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (EGR VALVE POSITION SENSOR - ECM): Lepas hubungan konektor EGR valve position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor electric vacuum regulating valve assembly. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 2KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 2KD-FTV) — GANTI ELECTRIC EGR CONTROL VALVE ASSEMBLY: Ganti electric EGR control valve assembly (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 2KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 2KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON selama 5 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 8 (ENGINE CONTROL 2KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C56-1 (VC) - C56-2 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-1 (VC) - C22-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-3 (EGLS) - C23-33 (EGLS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-2 (E2) - C22-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-1 (VC) atau C22-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C56-3 (EGLS) atau C23-33 (EGLS) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2KD-FTV] Voltase Standar: C56-1 (VC) - C56-2 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[KONTROL MESIN 2KD-FTV] Tahanan Standar: C56-1 (VC) - C22-18 (VC) (Selalu)` : **Dibawah 1 Ω**

### DTC `P0488` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Range / Performance pada Exhaust Gas Recirculation Throttle Position Control (Dokumen: RM00000188703VX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Range / Performance pada Exhaust Gas Recirculation Throttle Position Control (Dokumen: RM00000188703WX) | [ENGINE CONTROL 2KD-FTV — SISTEM
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Throttle valve macet Throttle valve tidak bergerak lancar Open atau short dalam sirkuit throttle control motor ECM; Kondisi Deteksi: Throttle motor mengaktifkan duty lebih dari nilai standar selama 30 detik (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Throttle valve macet Throttle valve tidak bergerak lancar Open atau short dalam sirkuit throttle control motor ECM; [KONTROL MESIN 1KD-F
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE CONTROL MOTOR POWER SOURCE): Lepas hubungan konektor throttle control motor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor throttle control motor.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (SIRKUIT MASA): Lepas hubungan konektor throttle control motor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor throttle control motor.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE CONTROL MOTOR - ECM): Lepas hubungan konektor throttle control motor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor throttle control motor. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI DIESEL THROTTLE BODY ASSEMBLY: Ganti diesel throttle body assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Selama periode 10 detik atau lebih, perlahan-lahan naikkan putaran mesin ke 3000 rpm dan turunkan
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (THROTTLE CONTROL MOTOR - BATERAI): Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C15-2 (B) - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C15-3 (RSC) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C15-1 (RSO) - C23-4 (LUSL) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C15-1 (RSO) atau C23-4 (LUSL) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C15-2 (B) - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C15-3 (RSC) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C15-1 (RSO) - C23-4 (LUSL) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C15-1 (RSO) atau C23-4 (LUSL) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0489` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low pada Sirkuit Exhaust Gas Recirculation Control (Dokumen: RM000003U7Q018X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low pada Sirkuit Exhaust Gas Recirculation Control (Dokumen: RM000003U7Q019X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Electric vacuum regulating valve assembly Open atau short dalam sirkuit electric vacuum regulating valve assembly ECM; Kondisi Deteksi: Open atau short dalam sirkuit electric vacuum regulating valve assembly selama 5 detik atau lebih (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Electric vacuum regulating valve assembly Open atau short dalam sirkuit electric vacuum regulating valve asse
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA ELECTRIC VACUUM REGULATING VALVE ASSEMBLY: Periksa electric vacuum regulating valve assembly (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL (POWER SOURCE): Lepas hubungan konektor electric vacuum regulating valve assembly. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor electric vacuum regulating valve assembly.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ELECTRIC VACUUM REGULATING VALVE ASSEMBLY - ECM): Lepas hubungan konektor electric vacuum regulating valve assembly. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor electric vacuum regulating valve assembly. -> 
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ELECTRIC VACUUM REGULATING VALVE ASSEMBLY: Ganti electric vacuum regulating valve assembly (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Hidupkan mesin. -> Jalankan mesin idle selama 5 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain /
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C8-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C8-2 - C23-9 (EGR) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C8-2 atau C23-9 (EGR) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C8-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C8-2 - C23-9 (EGR) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C8-2 atau C23-9 (EGR) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C90-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C90-2 - C23-9 (EGR) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0490` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Sirkuit pada Gas Recirculation Control (Dokumen: RM000003U7Q018X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Sirkuit pada Gas Recirculation Control (Dokumen: RM000003U7Q019X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Sirkuit pada 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Electric vacuum regulating valve assembly Open atau short dalam sirkuit electric vacuum regulating valve assembly ECM; Kondisi Deteksi: Open atau short dalam sirkuit electric vacuum regulating valve assembly selama 5 detik atau lebih (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Electric vacuum regulating valve assembly Open atau short dalam sirkuit electric vacuum regulating valve asse
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA ELECTRIC VACUUM REGULATING VALVE ASSEMBLY: Periksa electric vacuum regulating valve assembly (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL (POWER SOURCE): Lepas hubungan konektor electric vacuum regulating valve assembly. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor electric vacuum regulating valve assembly.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ELECTRIC VACUUM REGULATING VALVE ASSEMBLY - ECM): Lepas hubungan konektor electric vacuum regulating valve assembly. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor electric vacuum regulating valve assembly. -> 
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ELECTRIC VACUUM REGULATING VALVE ASSEMBLY: Ganti electric vacuum regulating valve assembly (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Hidupkan mesin. -> Jalankan mesin idle selama 5 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain /
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C8-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C8-2 - C23-9 (EGR) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C8-2 atau C23-9 (EGR) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C8-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C8-2 - C23-9 (EGR) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C8-2 atau C23-9 (EGR) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: C90-1 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C90-2 - C23-9 (EGR) (Selalu)` : **Di bawah 1 Ω**

### DTC `P0500` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Vehicle Speed Sensor "A" (Dokumen: RM0000012ME0AGX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Vehicle Speed Sensor "A" (Dokumen: RM0000012ME0AHX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Vehicle Speed Sensor "A" (Dokumen: RM0000012ME0AIX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit speedometer Speedometer assembly ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sirkuit speedometer Speedometer assembly ECM; [ENGINE CONTROL 1TR-FE] Area Gangguan: Open atau short dalam sirkuit sinyal kecepatan Vehicle speed sensor Meter kombinasi assembly ECM; Kondisi Deteksi: Saat kendaraan sedang dijalankan, tidak ada sinyal kecepatan kendaraan yang di-i
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA CARA KERJA SPEEDOMETER: Jalankan kendaraan dan periksa apakah speedometer dalam meter kombinasi assembly bekerja secara bormal.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (VEHICLE SPEED): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON dan hidupkan mesin. -> Hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / Data List / All Data / Engine Speed. -> Jalankan kendaraan. -> Baca nil
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR: Lepas hubungan konektor meter kombinasi assembly. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor meter kombinasi assembly.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA METER KOMBINASI (SPD BENTUK GELOMBANG SINYAL): Pindahkan shift lever ke netral. -> Dongkrak kendaraan. -> Periksa tegangan antara terminal meter kombinasi assembly dan bodi masa sambil memutar roda secara perlahan.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (METER KOMBINASI ASSEMBLY - ECM): Lepas hubungan konektor meter kombinasi assembly. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor meter kombinasi assembly. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA SIRKUIT SPEEDOMETER: Periksa sirkuit speedometer (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI METER KOMBINASI ASSEMBLY: Ganti meter kombinasi assembly (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G19-6 (+S) - Masa bodi (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G19-6 (+S) - Masa bodi (Ignition switch ON)` : **Tegangan dibangkitkan secara terputus-putus**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G19-6 (+S) - G38-17 (SPD) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G19-6 (+S) atau G38-17 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: G19-6 (+S) - Masa bodi (Ignition switch ON)` : **4.5 sampai 5.5 V**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: G19-6 (+S) - Masa bodi (Ignition switch ON)` : **Tegangan dibangkitkan secara terputus-putus**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: G19-6 (+S) - G38-17 (SPD) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: G19-6 (+S) atau G38-17 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0504` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Switch Rem "A" / "B" Berhubungan (Dokumen: RM000000XCT0KGX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Switch Rem "A" / "B" Berhubungan (Dokumen: RM000000XCT0KHX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Switch Rem "A" / "B" Berhubungan (Dokume
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: ON; Kondisi Deteksi: OFF; Kondisi Deteksi: ON; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit sinyal stop light switch Fuse STOP Fuse IGN Stop light switch ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: ON; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sirkuit sinyal stop light switch Fuse STOP Fuse IGN Stop light switch ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA STOP LIGHT SWITCH ASSEMBLY (TEGANGAN TERMINAL B): Lepas hubungan konektor stop light switch. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor stop light switch.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA STOP LIGHT SWITCH ASSEMBLY: Periksa stop light switch assembly (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA ECM (TEGANGAN - STP DAN ST1): Lepas hubungan konektor ECM. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI STOP LIGHT SWITCH ASSEMBLY: Mengganti stop light switch assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Putar ignition switch ke-ON dan hidupkan tester. -> Tekan dan bebaskan pedal rem. -> Masuk ke menu berikut ini: Powertrain / Engine dan
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: A24-2 - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: A24-3 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G38-14 (ST1-) - Masa bodi (Dibebaskan)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G38-14 (ST1-) - Masa bodi (Ditekan)` : **0 sampai 3 V**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G38-15 (STP) - Masa bodi (Dibebaskan)` : **0 sampai 3 V**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G38-15 (STP) - Masa bodi (Ditekan)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: A24-2 - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: A24-3 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**

### DTC `P0560` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Tegangan Sistem (Dokumen: RM000000T8P0S7X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Tegangan Sistem (Dokumen: RM000000T8P0S8X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Tegangan Sistem (Dokumen: RM000000T8P0S9X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open di sirkuit backup power source (ke terminal BATT) Baterai Terminal baterai Fuse EFI ECM; Kondisi Deteksi: Tegangan pada terminal BATT turun berlebihan selama 3 detik dan dan bagian dari nilai-nilai yang disimpan dalam ECM diinisialisasi (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open di sirkuit backup power source (ke terminal BATT) Baterai Terminal baterai Fuse EFI ECM; [TRANSM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TEGANGAN TERMINAL ECM (BATT): Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA BATERAI: Periksa bahwa filter tidak tersumbat.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TERMINAL BATERAI: Periksa bahwa terminal baterai tidak kendur atau berkarat.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Putar ignition switch ke ON selama 3 detik. -> Masuk ke menu berikut ini: Powertrai
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — RECHARGE ATAU GANTI BATERAI: Recharge atau ganti baterai.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI TERMINAL BATERAI: Perbaiki atau ganti terminal baterai.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G38-2 (BATT) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 2KD-FTV] Tegangan Standar: G38-2 (BATT) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: G41-5 (BATT) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-1 (E1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Voltase Standar: G38-2 (BATT) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[KONTROL MESIN 2KD-FTV] Voltase Standar: G38-2 (BATT) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Voltase Standar: G41-5 (BATT) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-1 (E1) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `P0604` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Random Access Memory (RAM) (Akses Memory Secara Acak) (Dokumen: RM000002KQO06CX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Random Access Memory (RAM) (Dokumen: RM000002KQO06LX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Random Access Memory (RAM) (Dokumen: RM000002KQO0AMX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan ECM RAM (Kegagalan Main CPU dan sub CPU mirroring) (1 trip detection logic).; [KONTROL MESIN 2TR-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan ECM RAM (Main CPU dan sub CPU mirroring) (1 trip detection logic).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Matikan intelligent tester. -> Putar ignition switch ke off. -> Lepas hubungan intelligent tester. -> Le
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA DARI DTC: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Matikan intelligent tester. -> Putar ignition switch ke off. -> Lepas hubungan intelligent tester. -> Le
  - Langkah 2 (KONTROL MESIN 2TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (KONTROL MESIN 2TR-FE) — GANTI ECM

### DTC `P0606` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] ECM / PCM Processor (Dokumen: RM00000324205WX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] ECM / PCM Processor (Dokumen: RM000003242065X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] ECM / PCM Processor (Dokumen: RM0000032420ATX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: ECM; [KONTROL MESIN 2TR-FE] Area Gangguan: ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Matikan intelligent tester. -> Putar ignition switch ke off. -> Lepas hubungan intelligent tester. -> Le
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA DARI DTC: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Matikan intelligent tester. -> Putar ignition switch ke off. -> Lepas hubungan intelligent tester. -> Le
  - Langkah 2 (KONTROL MESIN 2TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (KONTROL MESIN 2TR-FE) — GANTI ECM

### DTC `P0607` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Control Module Performance (Dokumen: RM00000187R03IX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Control Module Performance (Dokumen: RM00000187R03JX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Control Module Performance (Dokumen: RM00000187R03KX
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: ECM; Kondisi Deteksi: Kerusakan (Error) dalam ECM (1 trip detection logic); [ENGINE CONTROL 2KD-FTV] Area Gangguan: ECM; [ENGINE CONTROL 1TR-FE] Area Gangguan: ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: ECM; Kondisi Deteksi: ECM internal error (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DISAMPING DTC P0607 DAN/ATAU P1611): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 1 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — SELESAI
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — LANJUTKAN KE BAGAN DTC
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DISAMPING DTC P0607 DAN/ATAU P1611): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 1 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC.

### DTC `P0617` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Sirkuit pada Starter Rela (Dokumen: RM000000TA00UXX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Sirkuit pada Starter Rela (Dokumen: RM000000TA00UYX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Sirkuit pada Starter Rela (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Sirkuit relay starter Ignition switch Park/neutral position switch assembly* ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Sirkuit relay starter Ignition switch ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: Starter relay circuit Ignition switch Park/neutral position switch assembly ECM; [KONTROL MESIN 2KD-FTV] Area Gangguan: Starter relay circuit Ignition switch Park/neutral position switch assembly* ECM; [AUT
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (STARTER SIGNAL): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Starter Signal. -> Baca nilai yang di tampilkan pada tester bila ignition swit
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA SWITCH POSISI PARKIR/NETRAL ASSEMBLY: Periksa park/neutral position switch assembly (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA IGNITION SWITCH: Periksa ignition switch (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (IGNITION SWITCH - ECM): Lepas hubungan konektor ignition switch. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor ignition switch. -> Hubungkan kembali konektor ECM.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI PARK/NEUTRAL POSITION SWITCH ASSEMBLY: Ganti park/neutral position switch assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI IGNITION SWITCH: Ganti ignition switch (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] OK: ON` : **OFF**
  - `[ENGINE CONTROL 1KD-FTV] OK: START` : **ON**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G9-7 (ST2) atau G39-7 (STA) - Masa bodi dan terminal lainnya. (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] OK: ON` : **OFF**
  - `[ENGINE CONTROL 2KD-FTV] OK: START` : **ON**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: G9-7 (ST2) atau G39-7 (STA) - Masa bodi dan terminal lainnya. (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] OK: ON` : **OFF**
  - `[KONTROL MESIN 1KD-FTV] OK: START` : **ON**

### DTC `P0627` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Fuel Pump / Open (Dokumen: RM00000188502MX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Fuel Pump / Open (Dokumen: RM00000188502NX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Fuel Pump / Open (Dokumen: RM00000188502OX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short dalam sirkuit suction control valve Suction control valve (fuel supply pump assembly) ECM; Kondisi Deteksi: Meskipun CPU (command area di dalam ECU) adalah keluaran operation duty suction control valve, sinyal memonitor output kurang selama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Open atau short dalam sirkuit suction control valve Suction control valve (f
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA FUEL SUPPLY PUMP ASSEMBLY (SUCTION CONTROL VALVE): Memeriksa fuel supply pump assembly (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (SUCTION CONTROL VALVE - ECM): Lepas hubungan konektor suction control valve. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor suction control valve. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3 -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan biarkan idle selama 1 detik atau lebih. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT 
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (SUCTION CONTROL VALVE): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — LAKUKAN INISIALISASI SUPPLY PUMP BAHAN BAKAR: Lakukan inisialisasi fuel supply pump (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-1 - C22-2 (PCV+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-2 - C22-1 (PCV-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-1 atau C22-2 (PCV+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-2 atau C22-1 (PCV-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-1 - C22-2 (PCV+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-2 - C22-1 (PCV-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-1 atau C22-2 (PCV+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-2 atau C22-1 (PCV-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0657` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sirkuit Tegangan Suplai Aktuator / Open (Dokumen: RM000002I3U087X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Voltase Suplai Aktuator / Open (Dokumen: RM000002I3U08HX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sirkuit Voltase Suplai Aktuator / Open (Dokumen: RM000002I3U0D4X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: ECM; Kondisi Deteksi: Ini adalah kesalahan power suplai dari throttle actuator (1 trip detection logic).; [KONTROL MESIN 2TR-FE] Area Gangguan: ECM; Kondisi Deteksi: Terdapat kesalahan pada power supply throttle actuator (1 trip detection logic).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Matikan intelligent tester. -> Putar ignition switch ke off. -> Lepas hubungan intelligent tester. -> Le
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — PERIKSA DARI DTC: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Matikan intelligent tester. -> Putar ignition switch ke off. -> Lepas hubungan intelligent tester. -> Le
  - Langkah 2 (KONTROL MESIN 2TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (KONTROL MESIN 2TR-FE) — GANTI ECM

### DTC `P0705` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Malfungsi Sirkuit Transmission Range Sensor (Input PRNDL) (Dokumen: RM000000W840Q2X) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Malfungsi Sirkuit Transmission Range Sensor (Input PRNDL) (Dokumen: RM000000W840Q3X) | [AUTOM
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short dalam sirkuit park/neutral position switch Park/neutral position switch Shift lock control ECU (Shift lock control unit assembly) TCM; [AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Area Gangguan: Open atau short sirkuit dalam park/neutral position switch Park/neutral position switch Shift lock control ECU (Shift lock control unit assembly) TCM; [AUTOMATIC TRANSMISSION / TRANSAXLE A3
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA PARK/NEUTRAL POSITION SWITCH ASSEMBLY (SUBER DAYA): Lepas hubungan konektor C26 park/neutral position switch. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (TEGANGAN TERMINAL NSW): Lepas hubungan konektor ECM G39. -> Lepas hubungan konektor C26 park/neutral position switch. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA PARK/NEUTRAL POSITION SWITCH ASSEMBLY: Lepas hubungan konektor C26 park/neutral position switch. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT LOCK CONTROL ECU: Lepas hubungan konektor G37 shift lock control ECU. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (PARK/NEUTRAL POSITION SWITCH - SHIFT LOCK CONTROL ECU): Lepas hubungan konektor G37 shift lock control ECU. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (PARK/NEUTRAL POSITION SWITCH - TCM): Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (PARK/NEUTRAL POSITION SWITCH - TCM): Lepas hubungan konektor C26 park/neutral position switch. -> Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: C26-2 (RB) - Bodi masa (Ignition switch ON)` : **11 sampai 14 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: C26-2 (RB) - Bodi masa (Ignition switch off)` : **Di bawah 1 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: C26-4 (B) - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: C26-4 (B) - Masa bodi (Ignition switch off)` : **Di bawah 1 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 4 (B) - 5 (L) (Shift lever dalam P)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 2 (RB) - 1 (RL) (Shift lever dalam posisi R)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 4 (B) - 5 (L) (Shift lever dalam N)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 2 (RB) - 7 (DL) (Shift lever di D atau 3)` : **Di bawah 1 Ω**

### DTC `P0710` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Sirkuit Transmission Fluid Temperature Sensor "A" (Dokumen: RM0000012XR04VX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340F — SISTEM AUTOMATIC TRANSMISSION] Sirkuit Transmission Fluid Temperature Sensor "A" (Dokumen: RM0000012XR04XX) | [AUTOMATIC TRANSMISSIO
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Shift point terlalu trendah; Kondisi Deteksi: Temperatur ATF lebih dari 130℃ (266℉); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Lock-up di gigi ke 4 atau ke 3*; Kondisi Deteksi: Temperatur cairan pendingin mesin lebih tinggi dari 95°C (203°F); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short dalam sirkuit ATF temperature sensor ATF temperature sensor TCM; Kondisi Dete
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA ATF TEMPERATURE SENSOR: Lepas hubungan hubungan konektor C14 ATF temperature sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (ATF TEMPERATURE SENSOR - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI ATF TEMPERATURE SENSOR
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340F) — MEMERIKSA ATF TEMPERATURE SENSOR: Lepas hubungan konektor C14 ATF temperature sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (AUTOMATIC TRANSMISSION / TRANSAXLE A340F) — PERIKSA HARNESS DAN KONEKTOR (ATF TEMPERATURE SENSOR - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (AUTOMATIC TRANSMISSION / TRANSAXLE A340F) — GANTI TCM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (Selalu)` : **79 Ω sampai 156 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 2 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 20°C (68°F)` : **10.3 sampai 13.9 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 120℃ (248℉)` : **0.58 sampai 0.65 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-24 (THOC) - C24-23 (E2) (Selalu)` : **79 Ω sampai 156 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-24 (THOC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-23 (E2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0712` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Low Input pada Sirkuit "A" Fluid Temperature Sensor (Dokumen: RM0000012XR04VX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Low Input Surkuit pada Transmission Fluid Temperature Sensor "A" (Dokumen: RM0000012XR04WX) | [AUTO
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Shift point terlalu trendah; Kondisi Deteksi: Temperatur ATF lebih dari 130℃ (266℉); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Lock-up di gigi ke 4 atau ke 3*; Kondisi Deteksi: Temperatur cairan pendingin mesin lebih tinggi dari 95°C (203°F); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short dalam sirkuit ATF temperature sensor ATF temperature sensor TCM; Kondisi Dete
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA ATF TEMPERATURE SENSOR: Lepas hubungan hubungan konektor C14 ATF temperature sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (ATF TEMPERATURE SENSOR - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI ATF TEMPERATURE SENSOR
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA ATF TEMPERATURE SENSOR: Lepas hubungan konektor C14 ATF temperature sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — PERIKSA HARNESS DAN KONEKTOR (ATF TEMPERATURE SENSOR - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — GANTI TCM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (Selalu)` : **79 Ω sampai 156 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 2 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 20°C (68°F)` : **10.3 sampai 13.9 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 120℃ (248℉)` : **0.58 sampai 0.65 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-24 (THOC) - C24-23 (E2) (Selalu)` : **79 Ω sampai 156 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-24 (THOC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-23 (E2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0713` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] High Input pada Sirkuit "A" Fluid Temperature Sensor (Dokumen: RM0000012XR04VX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] High Input Sirkuit pada Transmission Fluid Temperature Sensor "A" (Dokumen: RM0000012XR04WX) | [AU
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Shift point terlalu trendah; Kondisi Deteksi: Temperatur ATF lebih dari 130℃ (266℉); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Lock-up di gigi ke 4 atau ke 3*; Kondisi Deteksi: Temperatur cairan pendingin mesin lebih tinggi dari 95°C (203°F); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short dalam sirkuit ATF temperature sensor ATF temperature sensor TCM; Kondisi Dete
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA ATF TEMPERATURE SENSOR: Lepas hubungan hubungan konektor C14 ATF temperature sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (ATF TEMPERATURE SENSOR - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI ATF TEMPERATURE SENSOR
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA ATF TEMPERATURE SENSOR: Lepas hubungan konektor C14 ATF temperature sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — PERIKSA HARNESS DAN KONEKTOR (ATF TEMPERATURE SENSOR - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — GANTI TCM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (Selalu)` : **79 Ω sampai 156 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 2 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 20°C (68°F)` : **10.3 sampai 13.9 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 120℃ (248℉)` : **0.58 sampai 0.65 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-24 (THOC) - C24-23 (E2) (Selalu)` : **79 Ω sampai 156 kΩ**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-24 (THOC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-23 (E2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0717` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Tidak ada Sinyal pada Turbine Speed Sensor (Dokumen: RM000000W7Y06PX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Tidak ada Sinyal pada Turbine Speed Sensor (Dokumen: RM000000W7Y06QX) | [AUTOMATIC TRANSMISSION / TRANSAXLE 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short pada sirkuit speed sensor NC0 Speed sensor NC0 TCM Transmisi otomatis (clutch, brake, gear dll.); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Mesin idling(Shift lever di P atau N); Kondisi Deteksi: 5 V/DIV., 0,5 mili detik/DIV.; [AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Area Gangguan: Open atau short sirkuit dalam speed sensor NC0 Speed sensor NC0 TCM Automatic transmiss
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA PEMASANGAN SPEED SENSOR NC0: Periksa pemasangan speed sensor NC0.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SPEED SENSOR NC0: Lepas hubungan konektor speed sensor C11. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (SPEED SENSOR NC0 - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — AMAN MEMASANG ATAU GANTI SPEED SENSOR NC0
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SPEED SENSOR NC0
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA PAMASANGAN SPEED SENSOR NC0: Periksa pemasangan speed sensor NC0.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (20°C (68°F))` : **560 sampai 680 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-3 (NC0+) - C24-2 (NC0-) (20°C (68°F))` : **560 sampai 680 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-3 (NC0+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-2 (NC0-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 1 - 2 (20°C (68°F))` : **560 sampai 680 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-3 (NC0+) - C24-2 (NC0-) (20°C (68°F))` : **560 sampai 680 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-3 (NC0+) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-2 (NC0-) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0722` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Tidak ada Sinyal pada Sirkuit Speed Sensor Output (Dokumen: RM0000012TD04UX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Tidak ada Sinyal pada Output Speed Sensor (Dokumen: RM0000012TD04VX) | [AUTOMATIC TRANSMISSION / TRAN
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short dalam sirkuit speed sensor (SP2) Speed sensor SP2 TCM Transmisi otomatis (clutch, brake, gear dll.); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Kecepatan kendaraan 20 km/jam (12 mph); Kondisi Deteksi: 2 V/DIV., 20 mili detik/DIV.; [AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Area Gangguan: Open atau short dalam sirkuit speed sensor SP2 Speed sensor SP2 TCM Automatic transm
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA PEMASANGAN SPEED SENSOR SP2: Periksa pemasangan speed sensor SP2.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SPEED SENSOR (SP2): Lepas hubungan konektor speed sensor C13. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (SPEED SENSOR SP2 - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — AMAN MEMASANG ATAU GANTI SPEED SENSOR SP2
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SPEED SENSOR SP2
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA PEMASANGAN SPEED SENSOR SP2: Periksa pemasangan speed sensor SP2.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (20°C (68°F))` : **560 sampai 680 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-30 (SP2+) - C24-29 (SP2-) (20°C (68°F))` : **560 sampai 680 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-30 (SP2+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-29 (SP2-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 1 - 2 (20°C (68°F))` : **560 sampai 680 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-30 (SP2+) - C24-29 (SP2-) (20°C (68°F))` : **560 sampai 680 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-30 (SP2+) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-29 (SP2-) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0724` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] High Sirkuit "B" pada Brake Switch (Dokumen: RM000000W880KBX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Brake Switch "B" Circuit High (Dokumen: RM000000W880KCX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340F — SISTEM AUTOMA
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short dalam sirkuit sinyal stop light switch Stop light switch TCM; Kondisi Deteksi: Stop light switch tetap on meskipun saat kendaraan dijalankan dalam pola stop (kurang dari 3 km/jam (2 mph)) dan go (30 km/jam (19 mph) atau lebih) sebanyak 5 kali (2-trip detection logic).; [AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Area Gangguan: Short sirkuit dalam sinyal stop light switch Stop light switch T
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA STOP LIGHT SWITCH ASSEMBLY: Lepas stop light switch assembly (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (BATERAI - TCM): Lepas hubungan konektor G41 TCM -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI STOP LIGHT SWITCH ASSEMBLY
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA STOP LIGHT SWITCH ASSEMBLY: Lepas stop light switch assembly (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — PERIKSA HARNESS DAN KONEKTOR (BATERAI - TCM): Lepas hubungan konektor TCM G41. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — GANTI TCM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (Pin tidak ditekan)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 3 - 4 (Pin terdorong)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (Pin terdorong)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 3 - 4 (Pin tidak ditekan)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: G41-14 (STP) - Masa bodi (Pedal rem ditekan)` : **7.5 sampai 14 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: G41-14 (STP) - Masa bodi (Pedal rem dibebaskan)` : **Di bawah 1 V**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 1 - 2 (Pin tidak ditekan)` : **Dibawah 1 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 3 - 4 (Pin terdorong)` : **Dibawah 1 Ω**

### DTC `P0818` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Driveline Disconnect Switch Input Circuit (Dokumen: RM0000012UV037X) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340F — SISTEM AUTOMATIC TRANSMISSION] Driveline Disconnect Switch Input Circuit (Dokumen: RM0000012UV02ZX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short dalam sirkuit switch posisi netral transfer Switch posisi netral transfer TCM; [AUTOMATIC TRANSMISSION / TRANSAXLE A340F] Area Gangguan: Short sirkuit dalam transfer neutral position switch Transfer neutral position switch TCM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA WIRE HARNESS DAN KONEKTOR (SWITCH INDIKATOR TRANSFER NO.2 - MASA BODI): Lepas hubungan konektor C30 Switch Indikator Transfer No. 2. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SWITCH INDIKATOR TRANSFER NO.2 (SWITCH POSISI NETRAL TRANSFER): Lepas switch indikator transfer No. 2. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA WIRE HARNESS DAN KONEKTOR (SWITCH INDIKATOR TRANSFER NO.2 - TCM): Lepas hubungan konektor C30 Switch Indikator Transfer No. 2. -> Lepas hubungan konektor G40 TCM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SWITCH INDIKATOR TRANSFER NO.2 (SWITCH POSISI NETRAL TRANSFER)
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340F) — PERIKSA HARNESS DAN KONEKTOR (TRANSFER INDICATOR SWITCH NO. 2 - BODY GROUND): Lepas hubungan konektor C30 Transfer Indicator Switch No. 2. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C30-2 - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (Tidak didorong)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (Didorong)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C30-1 - G40-16 (TFN) (Selalu)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C30-1 atau G40-16 (TFN) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340F] Tahanan Standar: C30-2 - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340F] Tahanan Standar: 1 - 2 (Tidak didorong)` : **10 kΩ atau lebih tinggi**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340F] Tahanan Standar: 1 - 2 (Ditekan)` : **Dibawah 1 Ω**

### DTC `P0973` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Low Sirkuit pada Kontrol Shift Solenoid "A" (Shift Solenoid Valve S1) (Dokumen: RM000000W8608KX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Shift Solenoid "A" Control Circuit Low (Shift Solenoid Valve S1) (Dokumen: RM0000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 TCM; Kondisi Deteksi: TCM mendeteksi short dalam sirkuit solenoid valve S1 4 kali ketika solenoid valve S1 dioperasikan (1-trip detection logic); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 TCM; Kondisi Deteksi: TCM mendeteksi open cirkuit pada solenoid v
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor kabel transmisi C12. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT SOLENOID VALVE S1: Lepas shift solenoid valve S1. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Berilah tegangan baterai 12 V ke shift solenoid valve dan periksa valve bergerak dan mengeluarkan suara kerja.
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SHIFT SOLENOID VALVE S1
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA TRANSMISSION WIRE (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor C12 transmission wire. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 4 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-18 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: Konektor shift solenoid velve S1 - Bodi shift solenoid valve S1 (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] OK: Positif baterai (+) → Konektor shift solenoid valve S1 Negatif baterai (-) → Bodi shift solenoid va` : **Valve bergerak dan mengeluarkan suara kerja.**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 4 (S1) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-18 (S1) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: Konektor terminal shift solenoid valve S1 - Bodi shift solenoid valve S1 (20°C (` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] OK: Positif (+) baterai → Konektor shift solenoid valve S1 Negatif (-) baterai → Bodi shift solen` : **Valve bergerak dan mengeluarkan noise pengoperasian.**

### DTC `P0974` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] High Sirkuit pada Kontrol Shift Solenoid "A" (Shift Solenoid Valve S1) (Dokumen: RM000000W8608KX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Shift Solenoid "A" Control Circuit High (Shift Solenoid Valve S1) (Dokumen: RM00
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 TCM; Kondisi Deteksi: TCM mendeteksi short dalam sirkuit solenoid valve S1 4 kali ketika solenoid valve S1 dioperasikan (1-trip detection logic); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 TCM; Kondisi Deteksi: TCM mendeteksi open cirkuit pada solenoid v
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor kabel transmisi C12. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT SOLENOID VALVE S1: Lepas shift solenoid valve S1. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Berilah tegangan baterai 12 V ke shift solenoid valve dan periksa valve bergerak dan mengeluarkan suara kerja.
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SHIFT SOLENOID VALVE S1
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA TRANSMISSION WIRE (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor C12 transmission wire. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 4 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-18 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: Konektor shift solenoid velve S1 - Bodi shift solenoid valve S1 (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] OK: Positif baterai (+) → Konektor shift solenoid valve S1 Negatif baterai (-) → Bodi shift solenoid va` : **Valve bergerak dan mengeluarkan suara kerja.**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 4 (S1) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-18 (S1) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: Konektor terminal shift solenoid valve S1 - Bodi shift solenoid valve S1 (20°C (` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] OK: Positif (+) baterai → Konektor shift solenoid valve S1 Negatif (-) baterai → Bodi shift solen` : **Valve bergerak dan mengeluarkan noise pengoperasian.**

### DTC `P0976` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Low Sirkuit pada Kontrol Shift Solenoid "B" (Shift Solenoid Valve S2) (Dokumen: RM000000W8708EX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Shift Solenoid "B" Control Circuit Low (Shift Solenoid Valve S2) (Dokumen: RM0000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 TCM; Kondisi Deteksi: TCM mendeteksi short dalam sirkuit solenoid valve S2, 4 kali ketika solenoid valve S2 dioperasikan (1-trip detection logic); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 TCM; Kondisi Deteksi: TCM mendeteksi open cirkuit pada solenoid 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor kabel transmisi C12. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT SOLENOID VALVE S2: Lepas shift solenoid valve S2. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Berilah tegangan baterai 12 V ke shift solenoid valve dan periksa valve bergerak dan mengeluarkan suara kerja.
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SHIFT SOLENOID VALVE S2
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor C12 transmission wire. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 8 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-17 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: Terminal konektor shift solenoid valve S2 - Bodi shift solenoid valve S2 (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] OK: Positif baterai (+) → Konektor shift solenoid valve S2 Negatif baterai (-) → Bodi shift solenoid va` : **Valve bergerak dan mengeluarkan suara kerja.**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 8 (S2) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-17 (S2) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: Konektor terminal shift solenoid valve S2 - Bodi shift solenoid valve S2 (20°C (` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] OK: Positif (+) baterai → Konektor shift solenoid valve S2 Negatif (-) baterai → Bodi shift solen` : **Valve bergerak dan mengeluarkan noise pengoperasian.**

### DTC `P0977` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] High Sirkuit pada Kontrol Shift Solenoid "B" (Shift Solenoid Valve S2) (Dokumen: RM000000W8708EX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Shift Solenoid "B" Control Circuit High (Shift Solenoid Valve S2) (Dokumen: RM00
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 TCM; Kondisi Deteksi: TCM mendeteksi short dalam sirkuit solenoid valve S2, 4 kali ketika solenoid valve S2 dioperasikan (1-trip detection logic); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 TCM; Kondisi Deteksi: TCM mendeteksi open cirkuit pada solenoid 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor kabel transmisi C12. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT SOLENOID VALVE S2: Lepas shift solenoid valve S2. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Berilah tegangan baterai 12 V ke shift solenoid valve dan periksa valve bergerak dan mengeluarkan suara kerja.
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SHIFT SOLENOID VALVE S2
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor C12 transmission wire. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 8 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-17 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: Terminal konektor shift solenoid valve S2 - Bodi shift solenoid valve S2 (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] OK: Positif baterai (+) → Konektor shift solenoid valve S2 Negatif baterai (-) → Bodi shift solenoid va` : **Valve bergerak dan mengeluarkan suara kerja.**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 8 (S2) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-17 (S2) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: Konektor terminal shift solenoid valve S2 - Bodi shift solenoid valve S2 (20°C (` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] OK: Positif (+) baterai → Konektor shift solenoid valve S2 Negatif (-) baterai → Bodi shift solen` : **Valve bergerak dan mengeluarkan noise pengoperasian.**

### DTC `P1229` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sistem Fuel Pump (Dokumen: RM000001AR101AX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sistem Fuel Pump (Dokumen: RM000001AR101BX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sistem Fuel Pump (Dokumen: RM000001AR101CX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Short sirkuit di fuel supply pump assembly (suction control valve) Fuel supply pump assembly (suction control valve) Fuel pressure sensor (common rail assembly) ECM; Kondisi Deteksi: Tekanan bahan bakar yang sebenarnya melebihi target tekanan bahan bakar untuk 5000 kPa atau lebih tinggi selama 30 detik. (1 trip detection logic); [ENGINE CONTROL 2KD-FTV] Area Gangguan: Short sirkuit di fuel supply pump assem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (FUEL PRESS DAN TARGET COMMON RAIL PRESSURE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hidupkan mesin dan panaskan mesin. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Fuel Press, dan Target Common Rail Press
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (SUCTION CONTROL VALVE - ECM): Lepas hubungan konektor suction control valve. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor suction control valve. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (TEST THE FUEL LEAK): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Active Test / Test the Fuel Leak / Data List / Fuel Press, Target Common Rail Pressure. ->
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ELEMENT FILTER BAHAN BAKAR SUB-ASSEMBLY: Mengganti elemen filter bahan bakar sub- assembly (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI FUEL SUPPLY PUMP ASSEMBLY (SUCTION CONTROL VALVE): Mengganti fuel supply pump assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — BLEEDING UDARA DARI SISTEM BAHAN BAKAR: Buang udara dari sistem bahan bakar (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-1 - C22-2 (PCV+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-2 - C22-1 (PCV-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-1 atau C22-2 (PCV+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C5-2 atau C22-1 (PCV-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-1 - C22-2 (PCV+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-2 - C22-1 (PCV-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-1 atau C22-2 (PCV+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] Tahanan Standar: C5-2 atau C22-1 (PCV-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P1251` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Turbocharger / Supercharger Overboost Condition (Terlalu Tinggi) (Dokumen: RM000002NOW02DX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Turbocharger / Supercharger Overboost Condition (Terlalu Tinggi) (Dokumen: RM000002NOW02EX) | [KONTROL MESIN
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Turbocharger sub-assembly Malfungsi macet VN turbo link Tegangan batarai sangat rendah (P0560 disimpan secara bersamaan) Sistem intake Sistem exhaust Electric EGR control valve assembly Injector assembly Diesel throttle body assembly ECM; Kondisi Deteksi: Boost pressure lebih tinggi dari batas minimal* selama 0.5 detik. (1 trip detection logic):; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Turbocharger sub-asse
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TERHADAP DTC LAIN YANG MUNCUL (CATAT DTC YANG DISIMPAN DAN FREEZE FRAME DATA): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA SISTEM AIR INTAKE: Periksa apakah selang antara air cleaner dan turbocharger, dan turbocharger dan intake manifold rusak atau terlepas hubungannya.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI SISTEM AIR INTAKE: Perbaiki atau ganti parts malmungsi di sistem air intake
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBOCHARGER SUB-ASSEMBLY (PENGOPERASIAN MOTOR DC): Putar ignition switch ke ON. -> Putar ignition switch ke off dan periksa pengoperasian motor DC (periksa gerakan operation link).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (ACTIVATE THE EGR VALVE CLOSE): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan panaskan mesin,dan memastikan switch A/C dan semua accessory off. -> Putar ignition switch ke off. Tunggu selama 30 detik, dan kemudian start kembali mesin. -> Hidupkan tester. -> 
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA ELECTRIC EGR CONTROL VALVE ASSEMBLY (PEMERIKSAAN VAKUM): Lepas hubungan selang vakum dari electric EGR control valve assembly. -> Hidupkan mesin. -> Periksa apakah terdapat isapan dari selang vakum selama idling.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — BERSIHKAN ENDAPAN (ELECTRIC EGR CONTROL VALVE ASSEMBLY): Lepas electric EGR control valve assembly (Lihat halaman ). -> Secara visual periksa electric EGR control valve assembly (Lihat halaman ). Jika terdapat endapan, bersihkan electric EGR control valve assembly. -> Pasang kembali electric EGR 
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI SELANG VACUUM: Perbaiki atau ganti selang vakum sistem EGR valve.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Referensi: Open (55%) (Tekanan atmosfer: 101 kPa Temperatur udara masuk: 30℃ (86℉) Temperatur cairan pendingin mesi` : **3,0 sampai 9,0 gm/s**
  - `[ENGINE CONTROL 1KD-FTV] Referensi: Close (0%) (Tekanan atmosfer: 101 kPa Temperatur udara masuk: 30℃ (86℉) Temperatur cairan pendingin mesi` : **15 sampai 22 gm/s**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C41-2 (M+) - C39-12 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C41-1 (M-) - C39-5 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) - C39-9 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) - C39-8 (VNE2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-3 (VNVC) - C39-1 (VNVC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-4 (VTA2) - C39-10 (VTA2) (Selalu)` : **Di bawah 1 Ω**

### DTC `P1264` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Malfungsi pada VN Turbo Controller (Dokumen: RM000002PPM01NX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Malfungsi pada VN Turbo Controller (Dokumen: RM000002PPM01OX) | [KONTROL MESIN 1KD-FTV — SISTEM ECD] VN Turbo Controller Malfunction (Doku
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Turbo motor driver Open atau short di dalam sirkuit turbo motor driver Problem masa pada turbo motor driver ECM; Kondisi Deteksi: Bila terjadi kiesalahan komunikasi antara turbo motor dan ECM (1 trip detection logic); [ENGINE CONTROL 2KD-FTV] Area Gangguan: Turbo motor driver Open atau short di dalam sirkuit turbo motor driver Problem masa pada turbo motor driver ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBO MOTOR DRIVER: Lepas hubungan konektor turbo motor driver. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor tur
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (TURBO MOTOR DRIVER - ECM): Lepas hubungan konektor ECM. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA ECM (TEGANGAN VNTO): Selama mesin idling, periksa bentuk gelombang dari konektor ECM menggunakan oscilloscope.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA ECM (TEGANGAN VNTI): Selama mesin idling, periksa bentuk gelombang dari konektor ECM menggunakan oscilloscope.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Lepas fuse EFI dari relay block ruang mesin dan junction block assembly selama lebi
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C39-3 (+B) - C39-4 (GND) (Selalu)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C39-4 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C22-10 (VNTO) - C39-7 (VNTO) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C22-17 (VNTI) - C39-2 (VNTI) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C22-10 (VNTO) atau C39-7 (VNTO) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C22-17 (VNTI) atau C39-2 (VNTI) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C22-10 (VNTO) - C23-7 (E1) (Idling)` : **Betulkan bentuk gelombang seperti ditunjukkan berikut**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C22-17 (VNTI) - C23-7 (E1) (Idling)` : **Betulkan bentuk gelombang seperti ditunjukkan berikut**

### DTC `P1271` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Fuel Regulator Malfungsi (EDU Drive) (Dokumen: RM00000188C03CX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Fuel Regulator Malfungsi (EDU Drive) (Dokumen: RM00000188C03DX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Fuel Reg
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short sirkuit di dalam pressure discharge valve Pressure discharge valve Injector driver; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short sirkuit di pressure discharge valve (P1271 secara serempak disimpan). Pressure discharge valve Injector driver ECM; Kondisi Deteksi: Pressure discharge valve tidak terbuka Penurunan tingkat tekanan aktual menyimpang simulasi tingkat tekanan berkurang set
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON. -> Jalankan kendaraan pada 50 km/jam (31 mph) di gigi ke 3, dan kemudian desele
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA COMMON RAIL ASSEMBLY (OPERASI PRESSURE DISCHARGE VALVE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain /Engine / Utility / Pressure Discharge Valve Check (Lihat halaman ). -> Pilih "Close to Open Check". -> Baca 
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA COMMON RAIL ASSEMBLY (RESISTAN PRESSURE DISCHARGE VALVE): Memeriksa common rail assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (PRESSURE DISCHARGE VALVE - INJECTOR DRIVER): Lepas hubungan konektor injector driver. -> Lepas hubungan konektor pressure discharge valve. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor injector driver. -> Hubungkan kembali konektor pres
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ECM-INJECTOR DRIVER): Lepas hubungan konektor injector driver. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor injector driver. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA INJECTOR DRIVER (POWER SOURCE CIRCUIT): Lepas hubungan konektor injector driver. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor injector driver.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI INJECTOR DRIVER: Mengganti injector driver (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI (DTC P1271 DAN/ATAU P1272): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON. -> Jalankan kendaraan pada 50 km/jam (31 mph) di gigi ke 3, dan kemudian desele
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-2 - C43-4 (RLF+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-1 - C44-1 (RLF-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-2 atau C43-4 (RLF+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-1 atau C44-1 (RLF-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-2 (PRD) - C22-32 (PRD) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-5 (INJF) - C22-25 (INJF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-2 (PRD) atau C22-32 (PRD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-5 (INJF) atau C22-25 (INJF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P1272` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Fuel Pressure Regulator Malfungsi (Dokumen: RM00000188C03CX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Fuel Pressure Regulator Malfungsi (Dokumen: RM00000188C03DX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Fuel Pressure Regulator Malfungsi (Dok
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short sirkuit di dalam pressure discharge valve Pressure discharge valve Injector driver; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Open atau short sirkuit di pressure discharge valve (P1271 secara serempak disimpan). Pressure discharge valve Injector driver ECM; Kondisi Deteksi: Pressure discharge valve tidak terbuka Penurunan tingkat tekanan aktual menyimpang simulasi tingkat tekanan berkurang set
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON. -> Jalankan kendaraan pada 50 km/jam (31 mph) di gigi ke 3, dan kemudian desele
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA COMMON RAIL ASSEMBLY (OPERASI PRESSURE DISCHARGE VALVE): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain /Engine / Utility / Pressure Discharge Valve Check (Lihat halaman ). -> Pilih "Close to Open Check". -> Baca 
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA COMMON RAIL ASSEMBLY (RESISTAN PRESSURE DISCHARGE VALVE): Memeriksa common rail assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (PRESSURE DISCHARGE VALVE - INJECTOR DRIVER): Lepas hubungan konektor injector driver. -> Lepas hubungan konektor pressure discharge valve. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor injector driver. -> Hubungkan kembali konektor pres
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ECM-INJECTOR DRIVER): Lepas hubungan konektor injector driver. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor injector driver. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA INJECTOR DRIVER (POWER SOURCE CIRCUIT): Lepas hubungan konektor injector driver. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor injector driver.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI INJECTOR DRIVER: Mengganti injector driver (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI (DTC P1271 DAN/ATAU P1272): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON. -> Jalankan kendaraan pada 50 km/jam (31 mph) di gigi ke 3, dan kemudian desele
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-2 - C43-4 (RLF+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-1 - C44-1 (RLF-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-2 atau C43-4 (RLF+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C49-1 atau C44-1 (RLF-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-2 (PRD) - C22-32 (PRD) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-5 (INJF) - C22-25 (INJF) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-2 (PRD) atau C22-32 (PRD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C45-5 (INJF) atau C22-25 (INJF) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P1601` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Injector Correction Circuit Malfunction (EEPROM) (Dokumen: RM000001AR0034X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Injector Correction Circuit Malfunction (EEPROM) (Dokumen: RM000001AR0035X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Injector
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Kode kompensasi injector Injector pilot quantity learning value ECM; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Kode kompensasi injector Injector pilot quantity learning value ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: Kode kompensasi injector Nilai injector pilot quantity learning ECM; [KONTROL MESIN 2KD-FTV] Area Gangguan: Kode kompensasi injector Nilai injector pilot quantity learning ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — KONFIRMASI LEARNING VALUE: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Utility / Learning values confirmation (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — REGISTERASI KODE KOMPENSASI INJEKTOR: Registerasi kode kompensasi injector (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — LEARNING VALUES WRITE: Install ECM lama. -> Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON dan hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Utility / Learning values save (Lihat halaman ). -> Lepas
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — KONFIRMASI LEARNING VALUE: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Utility / Learning values confirmation (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PILOT QUANTITY LEARNING: Lakukan injector pilot quantity learning (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC YANG MUNCUL: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan meninggalkan kendaraan selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 1 detik. -> Masuk ke menu berikut ini: Powertr
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan meninggalkan kendaraan selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 1 detik. -> Masuk ke menu berikut ini: Powertr

### DTC `P1604` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Malfungsi Startability (Dokumen: RM000003U7V02YX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Malfungsi Startability (Dokumen: RM000003U7V02ZX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Malfungsi Startability (Dokumen: RM000003U7V030X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Baterai Entry and start system Sistem engine immobiliser Bahan bakar irregular Kekurangan bahan bakar Suction control valve (fuel supply pump assembly) Injector assembly Elemen filter bahan bakar sub-assembly Sistem glow Injector driver Engine coolant temperature sensor Sistem intake Sistem exhaust Mesin rusak, seized up Kehilangan kompresi Pressure discharge valve (common rail assembly) Fuel pressure senso
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA DTC YANG MUNCUL (CATAT DTC DAN FREEZE FRAME DATA YANG DISIMPAN) (PROSEDUR 1): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Rekaman yang disimpan DTC dan freeze frame data.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA SETIAP DTC LAINNYA (DI SAMPING DTC P1604): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MENGAMBIL SNAPSHOT SELAMA STARTING DAN IDLING (PROSEDUR 3): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data. -> Lakukan snapshot dari Data List item berikut dengan intelligent t
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MENENTUKAN PENYEBAB DARI PROBLEM (CEK FREEZE FRAME DATA DAN SNAPSHOT): Menentukan penyebab problem berdasarkan reeze frame data yang tercatat dalam prosedur 1 dan nilai Data List yang tercatat dalam prosedur 3 saat menghidupkan mesin.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — MESIN SULIT DIHIDUPKAN ATAU MATI
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — LANJUTKAN KE BAGAN DTC
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — BACA DTC YANG MUNCUL (CATAT DTC DAN FREEZE FRAME DATA YANG DISIMPAN) (PROSEDUR 1): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Rekaman yang disimpan DTC dan freeze frame data.
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — PERIKSA SETIAP DTC LAINNYA (DI SAMPING DTC P1604): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.

### DTC `P1605` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Idling kasar (Dokumen: RM00000361A02DX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Idling kasar (Dokumen: RM00000361A02EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Idling kasar (Dokumen: RM00000361A02FX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Injector assembly Kode kompensasi injector Bahan bakar bocor Sistem glow Sistem udara masuk bocor Sistem udara masuk tersumbat Sistem EGR Sistem throttle valve Suction control valve (fuel supply pump assembly) Bahan bakar berkualitas rendah Problem buang udara Elemen filter bahan bakar sub-assembly Problem aksesori (A/C, generator, dll.) Mesin assembly ECM; Kondisi Deteksi: Putaran mesin turun menjadi kuran
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DI SAMPING DTC P1605): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — LANJUT KE IDLING KASAR ATAU GETARAN MESIN BERLEBIHAN
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — LANJUTKAN KE BAGAN DTC
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DI SAMPING DTC P1605): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — LANJUT KE IDLING KASAR ATAU GETARAN MESIN BERLEBIHAN
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — LANJUTKAN KE BAGAN DTC
  - Langkah 1 (KONTROL MESIN 1KD-FTV) — PERIKSA SETIAP OUTPUT PADA DTC YANG BERBEDA (SEBAGAI TAMBAHAN UNTUK DTC P1605): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (KONTROL MESIN 1KD-FTV) — LANJUTKAN KE IDLE KASAR ATAU GETARAN MESIN BERLEBIH

### DTC `P1611` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit IC Malfungsi (Dokumen: RM00000187R03IX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit IC Malfungsi (Dokumen: RM00000187R03JX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit IC Malfungsi (Dokumen: RM00000187R03KX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: ECM; Kondisi Deteksi: Kerusakan (Error) dalam ECM (1 trip detection logic); [ENGINE CONTROL 2KD-FTV] Area Gangguan: ECM; [KONTROL MESIN 1KD-FTV] Area Gangguan: ECM; Kondisi Deteksi: ECM internal error (1 trip detection logic); [KONTROL MESIN 2KD-FTV] Area Gangguan: ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DISAMPING DTC P0607 DAN/ATAU P1611): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 1 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — SELESAI
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — LANJUTKAN KE BAGAN DTC
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DISAMPING DTC P0607 DAN/ATAU P1611): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off selama 30 detik atau lebih. -> Putar ignition switch ke ON selama 1 detik. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC.

### DTC `P2006` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Intake Manifold Runner Control Macet Tertutup (Bank 1) (Dokumen: RM000000YGW01XX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Intake Manifold Runner Control Macet Tertutup (Bank 1) (Dokumen: RM000000YGW01YX) | [KONTROL MESIN 1KD-FTV — SISTEM EC
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Vacuum switching valve (untuk swirl control valve) Open atau short dalam sirkuit vacuum switching valve (untuk swirl control valve) Intake manifold (swirl control valve) Electric EGR control valve assembly Turbocharger sub-assembly Mass air flow meter Air cleaner hose Selang vakum Air cleaner element tersumbat Selang intake terlepas hubungan ECM; Kondisi Deteksi: Bila terdeteksi volume udara masuk aktual ol
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA DTC LAIN YANG MUNCUL (DI SAMPING DTC P2006): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA SISTEM AIR INTAKE: Periksa kebocoran udara dan penyumbatan antara air cleaner case dan turbocharger, dan antara turbocharger dan intake manifold.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI SISTEM AIR INTAKE: Perbaiki atau ganti parts malmungsi di sistem air intake
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA INTAKE MANIFOLD (PENGOPERASIAN SWIRL CONTROL VALVE): Periksa gerakan swirl control valve segera setelah menghidupkan mesin.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (MAF AND MAP): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Panaskan mesin (temperatur cairan pendingin mesin 70°C (158°F) atau lebih tinggi). -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / Data List / MAP d
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — BERSIHKAN MASS AIR FLOW METER: Bersihkan deposit yang menempel ke mass air flow meter.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERIKSA ATAU GANTI TURBOCHARGER SUB-ASSEMBLY: Periksa turbocharger sub-assembly (Lihat halaman ). -> Mengganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERIKSA HUBUNGAN SELANG VAKUM: Periksa hubungan selang vakum pada sistem swirl control valve.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] OK: VSV ON` : **Udara dari port E aliran keluar melalui port F.**
  - `[ENGINE CONTROL 1KD-FTV] OK: VSV OFF` : **Udara dari port E mengalir ke luar melalui filter udara**
  - `[ENGINE CONTROL 2KD-FTV] OK: VSV ON` : **Udara dari port E aliran keluar melalui port F.**
  - `[ENGINE CONTROL 2KD-FTV] OK: VSV OFF` : **Udara dari port E mengalir ke luar melalui filter udara**
  - `[KONTROL MESIN 1KD-FTV] OK: VSV ON` : **Udara dari port E mengalir keluar melalui port F**
  - `[KONTROL MESIN 1KD-FTV] OK: VSV OFF` : **Udara dari port E mengalir keluar melalui air filter**
  - `[KONTROL MESIN 2KD-FTV] OK: VSV ON` : **Udara dari port E mengalir keluar melalui port F**
  - `[KONTROL MESIN 2KD-FTV] OK: VSV OFF` : **Udara dari port E mengalir keluar melalui air filter**

### DTC `P2009` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Sirkuit pada Intake Manifold Runner Control (Bank 1) (Dokumen: RM000002NPB021X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low Sirkuit pada Intake Manifold Runner Control (Bank 1) (Dokumen: RM000002NPB022X) | [KONTROL MESIN 1KD-FTV — SISTE
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Vacuum switching valve (untuk swirl control valve) Open dalam sirkuit vacuum switching valve (untuk swirl control valve) ECM; Kondisi Deteksi: Open dalam sirkuit vacuum switching valve (untuk swirl control valve) selama 0.5 detik (2 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Vacuum switching valve (untuk swirl control valve) Short dalam sirkuit vacuum switching valve (untuk swirl control
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (ACTIVATE THE VSV FOR SWIRL CONTROL VALVE): Hubungkan intelligent tester ke DLC3. -> Lepas hubungan selang vakum dari vacuum switching valve (untuk Swirl Control Valve). -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Ac
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA VACUUM SWITCHING VALVE UNTUK SWIRL CONTROL VALVE (TAHANAN): Periksa vacuum switching valve (untuk swirl control valve) (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA VACUUM SWITCHING VALVE (UNTUK SWIRL CONTROL VALVE (TEGANGAN POWER SOURCE): Lepas hubungan konektor vacuum switching valve (untuk swirl control valve). -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (VACUUM SWITCHING VALVE [UNTUK SWIRL CONTROL VALVE] - ECM): Lepas hubungan konektor vacuum switching valve (untuk swirl control valve). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor vacuum switching valve (untuk swirl c
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (VACUUM SWITCHING VALVE [UNTUK SWIRL CONTROL VALVE] - INTEGRATION RELAY NO.1): Lepas integration relay No. 1 dari relay block ruang mesin dan junction block assembly. -> Lepas hubungan konektor integration relay No. 1. -> Lepas hubungan konektor vacuum switching valve (untuk swirl control valve). -> Ukur tahanan sesua
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA SIRKUIT POWER SOURCE ECM: Periksa sirkuit power ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI VACUUM SWITCHING VALVE (UNTUK SWIRL CONTROL VALVE): Ganti vacuum switching valve (untuk swirl control valve) (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] OK: VSV ON` : **Udara dari port E aliran keluar melalui port F.**
  - `[ENGINE CONTROL 1KD-FTV] OK: VSV OFF` : **Udara dari port E mengalir ke luar melalui filter udara**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C42-2 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C42-1 - C22-15 (SCV) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C42-1 or C22-15 (SCV) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: 1J-5 - C42-2 (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: 1J-5 atau C42-2 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] OK: VSV ON` : **Udara dari port E aliran keluar melalui port F.**

### DTC `P2010` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Sirkuit pada Intake Manifold Runner Control (Bank 1) (Dokumen: RM000002NPB021X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Sirkuit pada Intake Manifold Runner Control (Bank 1) (Dokumen: RM000002NPB022X) | [KONTROL MESIN 1KD-FTV — SIS
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Vacuum switching valve (untuk swirl control valve) Open dalam sirkuit vacuum switching valve (untuk swirl control valve) ECM; Kondisi Deteksi: Open dalam sirkuit vacuum switching valve (untuk swirl control valve) selama 0.5 detik (2 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Vacuum switching valve (untuk swirl control valve) Short dalam sirkuit vacuum switching valve (untuk swirl control
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (ACTIVATE THE VSV FOR SWIRL CONTROL VALVE): Hubungkan intelligent tester ke DLC3. -> Lepas hubungan selang vakum dari vacuum switching valve (untuk Swirl Control Valve). -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Ac
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA VACUUM SWITCHING VALVE UNTUK SWIRL CONTROL VALVE (TAHANAN): Periksa vacuum switching valve (untuk swirl control valve) (Lihat halaman ).
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA VACUUM SWITCHING VALVE (UNTUK SWIRL CONTROL VALVE (TEGANGAN POWER SOURCE): Lepas hubungan konektor vacuum switching valve (untuk swirl control valve). -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (VACUUM SWITCHING VALVE [UNTUK SWIRL CONTROL VALVE] - ECM): Lepas hubungan konektor vacuum switching valve (untuk swirl control valve). -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor vacuum switching valve (untuk swirl c
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (VACUUM SWITCHING VALVE [UNTUK SWIRL CONTROL VALVE] - INTEGRATION RELAY NO.1): Lepas integration relay No. 1 dari relay block ruang mesin dan junction block assembly. -> Lepas hubungan konektor integration relay No. 1. -> Lepas hubungan konektor vacuum switching valve (untuk swirl control valve). -> Ukur tahanan sesua
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA SIRKUIT POWER SOURCE ECM: Periksa sirkuit power ECM (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI VACUUM SWITCHING VALVE (UNTUK SWIRL CONTROL VALVE): Ganti vacuum switching valve (untuk swirl control valve) (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] OK: VSV ON` : **Udara dari port E aliran keluar melalui port F.**
  - `[ENGINE CONTROL 1KD-FTV] OK: VSV OFF` : **Udara dari port E mengalir ke luar melalui filter udara**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: C42-2 - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C42-1 - C22-15 (SCV) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C42-1 or C22-15 (SCV) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: 1J-5 - C42-2 (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: 1J-5 atau C42-2 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 2KD-FTV] OK: VSV ON` : **Udara dari port E aliran keluar melalui port F.**

### DTC `P2102` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Low Sirkuit pada Throttle Actuator Control Motor (Dokumen: RM000000PFU0K8X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Low Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM000000PFU0KKX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Low Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM0000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Open dalam sirkuit throttle actuator Throttle actuator ECM; [ENGINE CONTROL 1TR-FE] Area Gangguan: Short dalam sirkuit throttle actuator Throttle actuator Throttle valve Throttle body dengan motor assembly ECM; [KONTROL MESIN 2TR-FE] Area Gangguan: Open dalam sirkuit aktuator throttle Throttle actuator ECM; [KONTROL MESIN 2TR-FE] Area Gangguan: Short dalam sirkuit aktuator throttle Throttle actuator Throttle
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY (TAHANAN THROTTLE ACTUATOR): Periksa throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE ACTUATOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY: Periksa adanya benda asing antara throttle valve dan housing.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PEMERIKSA THROTTLE VALVE: Periksa apakah throttle valve membuka dan menutup dengan lembut.
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — SINGKIRKAN BENDA ASING DAN BERSIHKAN THROTTLE BODY
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-2 (M+) - C75-5 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-1 (M-) - C75-4 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-2 (M+) atau C75-5 (M+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-1 (M-) atau C75-4 (M-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-2 (M+) - C75-5 (M+) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-1 (M-) - C75-4 (M-) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-2 (M+) atau C75-5 (M+) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-1 (M-) atau C75-4 (M-) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P2103` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] High Sirkuit pada Throttle Actuator Control Motor (Dokumen: RM000000PFU0K8X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] High Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM000000PFU0KKX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] High Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Open dalam sirkuit throttle actuator Throttle actuator ECM; [ENGINE CONTROL 1TR-FE] Area Gangguan: Short dalam sirkuit throttle actuator Throttle actuator Throttle valve Throttle body dengan motor assembly ECM; [KONTROL MESIN 2TR-FE] Area Gangguan: Open dalam sirkuit aktuator throttle Throttle actuator ECM; [KONTROL MESIN 2TR-FE] Area Gangguan: Short dalam sirkuit aktuator throttle Throttle actuator Throttle
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY (TAHANAN THROTTLE ACTUATOR): Periksa throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE ACTUATOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY: Periksa adanya benda asing antara throttle valve dan housing.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PEMERIKSA THROTTLE VALVE: Periksa apakah throttle valve membuka dan menutup dengan lembut.
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — SINGKIRKAN BENDA ASING DAN BERSIHKAN THROTTLE BODY
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-2 (M+) - C75-5 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-1 (M-) - C75-4 (M-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-2 (M+) atau C75-5 (M+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-1 (M-) atau C75-4 (M-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-2 (M+) - C75-5 (M+) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-1 (M-) - C75-4 (M-) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-2 (M+) atau C75-5 (M+) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C67-1 (M-) atau C75-4 (M-) - Body ground (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P2111` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sistem Kontrol Throttle Actuator - Macet pada posisi Terbuka (Dokumen: RM000000PFV0N1X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sistem Kontrol Aktuator Throttle - Macet pada posisi Terbuka (Dokumen: RM000000PFV0NGX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sistem Kontrol Aktuator Throttl
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle actuator Throttle valve Throttle body dengan motor assembly Wire harness atau konektor; Kondisi Deteksi: Throttle actuator tidak menutup meskipun ECM memerintahkan untuk menutup (1 trip detection logic).; Kondisi Deteksi: Throttle actuator tidak membuka meskipun ECM memerintahkan untuk membuka (1 trip detection logic).; [KONTROL MESIN 2TR-FE] Area Gangguan: Throttle actuator Throttle valve Throttle 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC LAIN YANG MUNCUL (SEBAGAI TAMBAHAN UNTUK DTC P2111 ATAU P2112): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY (PEMERIKSAAN VISUAL THROTTLE VALVE): Periksa kontaminasi antara throttle valve dan housing. Bila perlu, bersihkan throttle body. Juga, periksa throttle valve bergerak dengan lancar.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu minimal selama 30 detik. -> Putar ignition switch ke ON. -> Masu
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (ECM - THROTTLE BODY DENGAN MOTOR): Sejak DTC disimpan karena perubahan tahanan kontak dari konektor, perbaiki atau ganti wire harness atau konektor (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2111 ATAU P2112): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin, tekan penuh dan bebaskan pedal akselerator dengan cepat untuk membuka dan menutup thrott
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — GANTI ECM

### DTC `P2112` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Sistem Kontrol Throttle Actuator - Macet pada posisi Tertutup (Dokumen: RM000000PFV0N1X) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sistem Kontrol Aktuator Throttle - Macet pada posisi Tertutup (Dokumen: RM000000PFV0NGX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Sistem Kontrol Aktuator Throt
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle actuator Throttle valve Throttle body dengan motor assembly Wire harness atau konektor; Kondisi Deteksi: Throttle actuator tidak menutup meskipun ECM memerintahkan untuk menutup (1 trip detection logic).; Kondisi Deteksi: Throttle actuator tidak membuka meskipun ECM memerintahkan untuk membuka (1 trip detection logic).; [KONTROL MESIN 2TR-FE] Area Gangguan: Throttle actuator Throttle valve Throttle 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC LAIN YANG MUNCUL (SEBAGAI TAMBAHAN UNTUK DTC P2111 ATAU P2112): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY (PEMERIKSAAN VISUAL THROTTLE VALVE): Periksa kontaminasi antara throttle valve dan housing. Bila perlu, bersihkan throttle body. Juga, periksa throttle valve bergerak dengan lancar.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu minimal selama 30 detik. -> Putar ignition switch ke ON. -> Masu
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (ECM - THROTTLE BODY DENGAN MOTOR): Sejak DTC disimpan karena perubahan tahanan kontak dari konektor, perbaiki atau ganti wire harness atau konektor (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2111 ATAU P2112): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin, tekan penuh dan bebaskan pedal akselerator dengan cepat untuk membuka dan menutup thrott
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — GANTI ECM

### DTC `P2118` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Range / Performance pada Arus Throttle Actuator Control Motor (Dokumen: RM000000PFW0KJX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Throttle Actuator Control Motor Current Range / Performance (Dokumen: RM000000PFW0KXX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Throttle Actuator Control Motor
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Open dalam sirkuit power source ETCS Baterai Terminal baterai Fuse ETCS ECM; Kondisi Deteksi: Open dalam sirkuit (+BM) power source ETCS (1 trip detection logic); [KONTROL MESIN 2TR-FE] Area Gangguan: Open dalam sirkuit power source ETCS Baterai Terminal baterai Fuse ETCS ECM; Kondisi Deteksi: Open dalam sirkuit ETCS power source (+BM) (1 trip detection logic).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (+B TEGANGAN ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / +BM Voltage. -> Baca nilai yang ditampilkan pada intell
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (ECM - BATERAI, MASA BODI): Lepas hubungan konektor ECM. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 1 (KONTROL MESIN 2TR-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (+B VOLTASE ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / +BM Voltage. -> Baca nilai yang ditampilkan pada intell
  - Langkah 2 (KONTROL MESIN 2TR-FE) — PERIKSA HARNESS DAN KONEKTOR (ECM - BATERAI, BODY GROUND): Lepas hubungan konektor ECM. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL MESIN 2TR-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: G89-7 (+BM) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C75-3 (E1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C76-3 (ME01) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Voltase Standar: G89-7 (+BM) - Body ground (Selalu)` : **11 sampai 14 V**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C75-3 (E1) - Body ground (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 2TR-FE] Tahanan Standar: C76-3 (ME01) - Body ground (Selalu)` : **Dibawah 1 Ω**

### DTC `P2119` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Range / Performance pada Throttle Actuator Control Throttle Body (Dokumen: RM000000PFX0NGX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Throttle Actuator Control Throttle Body Range / Performance (Dokumen: RM000000PFX0NVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Throttle Actuator Control Th
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: ETCS ECM Wire harness atau konektor; Kondisi Deteksi: Sudut buka throtle valve terus menerus ke sangat besar dari sudut buka target (1 trip detection logic); [KONTROL MESIN 2TR-FE] Area Gangguan: ETCS ECM Wire harness atau konektor; Kondisi Deteksi: Sudut buka throttle valve terus bervariasi dari sudut pembukaan sasaran (1 trip detection logic).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — PERIKSA TERHADAP DTC LAIN YANG MUNCUL (SEBAGAI TAMBAHAN KE DTC P2119): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu minimal selama 30 detik. -> Putar ignition switch ke ON. -> Masu
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY (TAHANAN THROTTLE ACTUATOR): Periksa throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — MEMERIKSA THROTTLE BODY DENGAN MOTOR ASSEMBLY (PEMERIKSAAN VISUAL THROTTLE VALVE): Periksa kontaminasi antara throttle valve dan housing. Bila perlu, bersihkan throttle body. Juga, periksa throttle valve bergerak dengan lancar.
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu minimal selama 30 detik. -> Putar ignition switch ke ON. -> Masu
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (ECM - THROTTLE BODY DENGAN MOTOR): Sejak DTC disimpan karena perubahan tahanan kontak dari konektor, perbaiki atau ganti wire harness atau konektor (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2119): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 15 detik atau lebih. -> Tekan penuh dan bebaskan pedal akselerator beberapa ka

### DTC `P2120` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Throttle / Pedal Position Sensor / Switch "D" Circuit (Dokumen: RM0000018WX03EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Throttle / Pedal Position Sensor / Switch "D" Circuit (Dokumen: RM0000018WX03FX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit VCPA Sirkuit VPA open atau shorted ke masa Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit EPA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TAGANGAN TERMINAL ECM (TERMINAL VCPA DAN VCP2): Lepas hubungan konektor accelerator pedal position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor accelerator pedal position sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2121` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Range / Performance pada Sirkuit "D" Throttle / Pedal Position Sensor / Switch (Dokumen: RM0000018WY03DX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Range / Performance pada Sirkuit "D" Throttle / Pedal Position Sensor / Switch (Dokumen: RM0000018WY03EX) | [ENGINE CONTROL 2KD-FTV — SI
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Sirkuit accelerator pedal position sensor Accelerator pedal position sensor ECM; Kondisi Deteksi: Perbedaan tegangan antara VPA and VPA2 lebih dari 1.4 V, atau lebih dari 1.2 Vselama 0.5 detik (1 trip detection logic).; [ENGINE CONTROL 2KD-FTV] Area Gangguan: Sirkuit accelerator pedal position sensor Accelerator pedal position sensor ECM; [ENGINE CONTROL 1TR-FE] Area Gangguan: Accelerator pedal position sen
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2121): Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau lebih, tekan sebagian selama 3 detik atau lebih, dan kemudian tekan sepenuhn
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau lebih, tekan sebagian selama 3 detik atau l
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2122` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03FX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit VCPA Sirkuit VPA open atau shorted ke masa Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit EPA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TAGANGAN TERMINAL ECM (TERMINAL VCPA DAN VCP2): Lepas hubungan konektor accelerator pedal position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor accelerator pedal position sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2123` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03FX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variab
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit VCPA Sirkuit VPA open atau shorted ke masa Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit EPA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TAGANGAN TERMINAL ECM (TERMINAL VCPA DAN VCP2): Lepas hubungan konektor accelerator pedal position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor accelerator pedal position sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2125` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Throttle / Sensor Pedal Posisi / Switch Sirkuit"B" (Dokumen: RM0000018WX03EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Throttle / Sensor Pedal Posisi / Switch Sirkuit"B" (Dokumen: RM0000018WX03FX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Thro
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit VCPA Sirkuit VPA open atau shorted ke masa Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit EPA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TAGANGAN TERMINAL ECM (TERMINAL VCPA DAN VCP2): Lepas hubungan konektor accelerator pedal position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor accelerator pedal position sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2127` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03FX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit VCPA Sirkuit VPA open atau shorted ke masa Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit EPA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TAGANGAN TERMINAL ECM (TERMINAL VCPA DAN VCP2): Lepas hubungan konektor accelerator pedal position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor accelerator pedal position sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2128` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03FX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variab
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit VCPA Sirkuit VPA open atau shorted ke masa Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit EPA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TAGANGAN TERMINAL ECM (TERMINAL VCPA DAN VCP2): Lepas hubungan konektor accelerator pedal position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor accelerator pedal position sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2135` — [ENGINE CONTROL 1TR-FE — SISTEM SFI] Korelasi Tegangan "A" / "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KJX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Korelasi Voltase "A" / "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF60KVX) | [KONTROL MESIN 2TR-FE — SFI SYSTEM] Korelasi Voltase "
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) ECM; Kondisi Deteksi: Tegangan output VTA1 berfluktuasi dengan cepat melampaui batas bawah dan atas malfungsi selama 2 detik bila pedal akselerator di tekan (1 trip detection logic).; [ENGINE CONTROL 1TR-FE] Area Gangguan: Throttle position sensor (dibuat menyatu dalam throttle body with motor assembly) Sirkuit throttle positio
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1TR-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (THROTTLE POSITION ): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / All Data / Throttle Position No. 1 dan Throttle Position No. 2. ->
  - Langkah 2 (ENGINE CONTROL 1TR-FE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR - ECM): Lepas hubungan throttle body dengan konektor motor -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE CONTROL 1TR-FE) — MEMERIKSA ECM (TEGANGAN VC): Lepas hubungan throttle body dengan konektor motor -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (ENGINE CONTROL 1TR-FE) — GANTI THROTTLE BODY DENGAN MOTOR ASSEMBLY: Ganti throttle body dengan motor assembly (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1TR-FE) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC THROTTLE POSITION SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hidupkan intelligent tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan sesuai dengan pola pengendaraan yang dijelaskan dalam Konfirmasi P
  - Langkah 6 (ENGINE CONTROL 1TR-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE CONTROL 1TR-FE) — GANTI ECM
  - Langkah 8 (ENGINE CONTROL 1TR-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) - C75-18 (VC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) - C75-20 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) - C75-19 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-3 (E2) - C75-28 (E2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-5 (VC) atau C75-18 (VC) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-6 (VTA) atau C75-20 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tahanan Standar: C67-4 (VTA2) atau C75-19 (VTA2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1TR-FE] Tegangan Standar: C67-5 (VC) - C67-3 (E2) (Ignition switch ON)` : **4.5 sampai 5.5 V**

### DTC `P2138` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Korelasi Tegangan "D" / "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03EX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Korelasi Tegangan "D" / "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM0000018WX03FX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variab
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit VCPA Sirkuit VPA open atau shorted ke masa Accelerator pedal assembly Batang pedal akselerator (lengan) cacat ECM; [ENGINE CONTROL 1KD-FTV] Area Gangguan: Accelerator pedal position sensor Open dalam sirkuit EPA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ACCELERATOR PEDAL POSITION): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine and ECT / Data List / Accel Sens. No. 1 Volt % dan Accel Sens. No. 2 Volt %. -> Baca nilai.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor accelerator pedal position sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor accelerator pedal position sensor. -> Hubungkan kembal
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TAGANGAN TERMINAL ECM (TERMINAL VCPA DAN VCP2): Lepas hubungan konektor accelerator pedal position sensor. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor accelerator pedal position sensor.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI ROD PEDAL AKSELERATOR ASSEMBLY: Ganti accelerator pedal rod assembly (Lihat halaman )
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke off dan tinggalkan kendaraan selama 30 detik. -> Putar ignition switch ke ON. -> Pedal akselerator dibebaskan sepenuhnya selama 3 detik atau le
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Dibebaskan (8 sampai 28%)` : **30 sampai 55%**
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: Ditekan (51 sampai 86%)` : **73 sampai 98%**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-1 (VCP2) - G39-27 (VCP2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-2 (EP2) - G39-29 (EPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-3 (VPA2) - G39-23 (VPA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-4 (VCPA) - G39-26 (VCPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-5 (EPA) - G39-28 (EPA) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G6-6 (VPA) - G39-22 (VPA) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2226` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Sirkuit Tekanan Barometrik (Dokumen: RM0000018X203MX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Sirkuit Tekanan Barometrik (Dokumen: RM0000018X203NX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Sirkuit Tekanan Barometrik (Dokumen: RM0000018X203OX
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: ECM; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 1.4 V atau kurang, atau 4.0 V atau lebih tinggi selama 0.5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 1.4 V atau kurang selama 0.5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 4.0 V atau lebih tinggi selama 0.5 detik (1 trip detection logic).; [ENGINE CONT
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu selama 1 detik atau lebih. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — SELESAI
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu selama 1 detik atau lebih. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — SELESAI
  - Langkah 1 (KONTROL MESIN 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (KONTROL MESIN 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI DENGAN SEMPURNA ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON dan tunggu selama 1 dalam atau lebih. -> Konfirmasikan DTC tidak di-output kembali.

### DTC `P2228` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low Input pada Sirkuit Tekanan Barometrik (Dokumen: RM0000018X203MX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] Low Input pada Sirkuit Tekanan Barometrik (Dokumen: RM0000018X203NX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low Input pada Sirkuit
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: ECM; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 1.4 V atau kurang, atau 4.0 V atau lebih tinggi selama 0.5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 1.4 V atau kurang selama 0.5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 4.0 V atau lebih tinggi selama 0.5 detik (1 trip detection logic).; [ENGINE CONT
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu selama 1 detik atau lebih. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — SELESAI
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu selama 1 detik atau lebih. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — SELESAI
  - Langkah 1 (KONTROL MESIN 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (KONTROL MESIN 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI DENGAN SEMPURNA ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON dan tunggu selama 1 dalam atau lebih. -> Konfirmasikan DTC tidak di-output kembali.

### DTC `P2229` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High Input pada Sirkuit Tekanan Barometrik (Dokumen: RM0000018X203MX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD] High Input pada Sirkuit Tekanan Barometrik (Dokumen: RM0000018X203NX) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High Input pada Sirk
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: ECM; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 1.4 V atau kurang, atau 4.0 V atau lebih tinggi selama 0.5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 1.4 V atau kurang selama 0.5 detik (1 trip detection logic).; Kondisi Deteksi: Tegangan sensor tekanan atmosfer adalah 4.0 V atau lebih tinggi selama 0.5 detik (1 trip detection logic).; [ENGINE CONT
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu selama 1 detik atau lebih. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — SELESAI
  - Langkah 1 (ENGINE CONTROL 2KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (ENGINE CONTROL 2KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON, dan tunggu selama 1 detik atau lebih. -> Konfirmasi bahwa DTC tidak muncul lagi.
  - Langkah 3 (ENGINE CONTROL 2KD-FTV) — SELESAI
  - Langkah 1 (KONTROL MESIN 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 2 (KONTROL MESIN 1KD-FTV) — PASTIKAN APAKAH MALFUNGSI TELAH BERHASIL DIPERBAIKI DENGAN SEMPURNA ATAU BELUM: Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke ON. -> Hapus DTC (Lihat halaman ). -> Putar ignition switch ke ON dan tunggu selama 1 dalam atau lebih. -> Konfirmasikan DTC tidak di-output kembali.

### DTC `P2563` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Turbocharger/Supercharger Boost Control Position Sensor "A" Circuit Range/Performance (Dokumen: RM000002PPN026X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Turbocharger/Supercharger Boost Control Position Sensor "A" Circuit Range/Performance (
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly); Kondisi Deteksi: Perbedaan tegangan antara VTA1 dan VTA2 adalah 0.8 V atau lebih selama 0.5 detik atau lebih (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly) Open atau short dalam sirkuit nozzle vane position sensor Turbo motor driver; Kondisi Deteksi: Tegangan VTA1 adalah 0.5 V 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TERHADAP DTC LAIN Y ANG MUNCUL (SEBAGAI TAMBAHAN KE DTC P2563, P2564, P2565, P2588 DAN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (NOZZLE VANE POSITION SENSOR - TURBO MOTOR DRIVER): Lepas hubungan konektor nozzle vane position sensor. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali kone
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBO MOTOR DRIVER (POWER SOURCE SENSOR): Lepas hubungan konektor nozzle vane position sensor. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor nozzle vane position sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBO MOTOR DRIVER (TEGANGAN VTA1, VTA2): Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Periksa perbedaan antara nilai tegangan.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2563, P2564, P2565, P2588 AN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 5 deti
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY (NOZZLE VANE POSITION SENSOR): Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) - C39-9 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) - C39-8 (VNE2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-3 (VNVC) - C39-1 (VNVC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-4 (VTA2) - C39-10 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-5 (E2S) - C39-11 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-6 (VCS) - C39-6 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) atau C39-9 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) atau C39-8 (VNE2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P2564` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low pada Sirkuit "A" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM000002PPN026X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low pada Sirkuit "A" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly); Kondisi Deteksi: Perbedaan tegangan antara VTA1 dan VTA2 adalah 0.8 V atau lebih selama 0.5 detik atau lebih (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly) Open atau short dalam sirkuit nozzle vane position sensor Turbo motor driver; Kondisi Deteksi: Tegangan VTA1 adalah 0.5 V 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TERHADAP DTC LAIN Y ANG MUNCUL (SEBAGAI TAMBAHAN KE DTC P2563, P2564, P2565, P2588 DAN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (NOZZLE VANE POSITION SENSOR - TURBO MOTOR DRIVER): Lepas hubungan konektor nozzle vane position sensor. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali kone
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBO MOTOR DRIVER (POWER SOURCE SENSOR): Lepas hubungan konektor nozzle vane position sensor. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor nozzle vane position sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBO MOTOR DRIVER (TEGANGAN VTA1, VTA2): Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Periksa perbedaan antara nilai tegangan.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2563, P2564, P2565, P2588 AN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 5 deti
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY (NOZZLE VANE POSITION SENSOR): Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) - C39-9 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) - C39-8 (VNE2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-3 (VNVC) - C39-1 (VNVC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-4 (VTA2) - C39-10 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-5 (E2S) - C39-11 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-6 (VCS) - C39-6 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) atau C39-9 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) atau C39-8 (VNE2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P2565` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High pada Sirkuit "A" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM000002PPN026X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High pada Sirkuit "A" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly); Kondisi Deteksi: Perbedaan tegangan antara VTA1 dan VTA2 adalah 0.8 V atau lebih selama 0.5 detik atau lebih (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly) Open atau short dalam sirkuit nozzle vane position sensor Turbo motor driver; Kondisi Deteksi: Tegangan VTA1 adalah 0.5 V 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TERHADAP DTC LAIN Y ANG MUNCUL (SEBAGAI TAMBAHAN KE DTC P2563, P2564, P2565, P2588 DAN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (NOZZLE VANE POSITION SENSOR - TURBO MOTOR DRIVER): Lepas hubungan konektor nozzle vane position sensor. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali kone
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBO MOTOR DRIVER (POWER SOURCE SENSOR): Lepas hubungan konektor nozzle vane position sensor. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor nozzle vane position sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBO MOTOR DRIVER (TEGANGAN VTA1, VTA2): Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Periksa perbedaan antara nilai tegangan.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2563, P2564, P2565, P2588 AN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 5 deti
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY (NOZZLE VANE POSITION SENSOR): Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) - C39-9 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) - C39-8 (VNE2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-3 (VNVC) - C39-1 (VNVC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-4 (VTA2) - C39-10 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-5 (E2S) - C39-11 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-6 (VCS) - C39-6 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) atau C39-9 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) atau C39-8 (VNE2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P2588` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Low pada Sirkuit "B" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM000002PPN026X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] Low pada Sirkuit "B" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly); Kondisi Deteksi: Perbedaan tegangan antara VTA1 dan VTA2 adalah 0.8 V atau lebih selama 0.5 detik atau lebih (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly) Open atau short dalam sirkuit nozzle vane position sensor Turbo motor driver; Kondisi Deteksi: Tegangan VTA1 adalah 0.5 V 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TERHADAP DTC LAIN Y ANG MUNCUL (SEBAGAI TAMBAHAN KE DTC P2563, P2564, P2565, P2588 DAN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (NOZZLE VANE POSITION SENSOR - TURBO MOTOR DRIVER): Lepas hubungan konektor nozzle vane position sensor. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali kone
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBO MOTOR DRIVER (POWER SOURCE SENSOR): Lepas hubungan konektor nozzle vane position sensor. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor nozzle vane position sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBO MOTOR DRIVER (TEGANGAN VTA1, VTA2): Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Periksa perbedaan antara nilai tegangan.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2563, P2564, P2565, P2588 AN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 5 deti
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY (NOZZLE VANE POSITION SENSOR): Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) - C39-9 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) - C39-8 (VNE2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-3 (VNVC) - C39-1 (VNVC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-4 (VTA2) - C39-10 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-5 (E2S) - C39-11 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-6 (VCS) - C39-6 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) atau C39-9 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) atau C39-8 (VNE2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P2589` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] High pada Sirkuit "B" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM000002PPN026X) | [ENGINE CONTROL 2KD-FTV — SISTEM ECD (untuk Variable Nozzle Vane Turbocharger)] High pada Sirkuit "B" Turbocharger / Supercharger Boost Control Position Sensor (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly); Kondisi Deteksi: Perbedaan tegangan antara VTA1 dan VTA2 adalah 0.8 V atau lebih selama 0.5 detik atau lebih (1 trip detection logic); [ENGINE CONTROL 1KD-FTV] Area Gangguan: Nozzle vane position sensor (Turbocharger sub-assembly) Open atau short dalam sirkuit nozzle vane position sensor Turbo motor driver; Kondisi Deteksi: Tegangan VTA1 adalah 0.5 V 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA TERHADAP DTC LAIN Y ANG MUNCUL (SEBAGAI TAMBAHAN KE DTC P2563, P2564, P2565, P2588 DAN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (NOZZLE VANE POSITION SENSOR - TURBO MOTOR DRIVER): Lepas hubungan konektor nozzle vane position sensor. -> Lepas hubungan konektor turbo motor driver. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor turbo motor driver. -> Hubungkan kembali kone
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA TURBO MOTOR DRIVER (POWER SOURCE SENSOR): Lepas hubungan konektor nozzle vane position sensor. -> Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor nozzle vane position sensor.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA TURBO MOTOR DRIVER (TEGANGAN VTA1, VTA2): Putar ignition switch ke ON. -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah ini. -> Periksa perbedaan antara nilai tegangan.
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — GANTI TURBO MOTOR DRIVER: Ganti turbo motor driver (Lihat halaman ).
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC P2563, P2564, P2565, P2588 AN/ATAU P2589): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 5 deti
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — GANTI TURBOCHARGER SUB-ASSEMBLY (NOZZLE VANE POSITION SENSOR): Ganti turbocharger sub-assembly (Lihat halaman ).
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR: Perbaiki atau ganti harness atau konektor.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) - C39-9 (VTA1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) - C39-8 (VNE2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-3 (VNVC) - C39-1 (VNVC) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-4 (VTA2) - C39-10 (VTA2) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-5 (E2S) - C39-11 (E2S) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-6 (VCS) - C39-6 (VCS) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-1 (VTA1) atau C39-9 (VTA1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: C40-2 (VNE2) atau C39-8 (VNE2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P2716` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Kelistrikan Pressure Control Solenoid "D" (Shift Solenoid Valve SLT) (Dokumen: RM000000W8A0CWX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Kelistrikan Pressure Control Solenoid "D" (Shift Solenoid Valve SLT) (Dokumen: RM0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SLT Shift solenoid valve SLT TCM; Kondisi Deteksi: Open atau short telah dideteksi dalam sirkuit shift solenoid valve SLT selama 1 detik atau lebih selama pengendaraan (1-trip detection logic).; [AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SLT Shift solenoid valve SLT TCM; Kondisi D
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SLT): Lepas hubungan konektor kabel transmisi C12. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT SOLENOID VALVE SLT: Lepas shift solenoid valve SLT. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Berilah tegangan baterai 12 V ke shift solenoid valve dan periksa valve bergerak dan mengeluarkan suara kerja.
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SHIFT SOLENOID VALVE SLT
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SLT): Lepas hubungan konektor C12 transmission wire. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 2 (SLT+) - 6 (SLT-) (20°C (68°F))` : **5.0 sampai 5.6 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 2 (SLT+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 6 (SLT-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-20 (SLT+) - C24-19 (SLT-) (20°C (68°F))` : **5.0 sampai 5.6 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-20 (SLT+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-19 (SLT-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 1 - 2 (20°C (68°F))` : **5.0 sampai 5.6 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] OK: Positif baterai (+) dengan lampu 21 W → Terminal 2 Negatif (-) baterai → Terminal 1` : **Valve bergerak dan mengeluarkan suara kerja.**

### DTC `P2769` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Torque Converter Clutch Solenoid Circuit Low (Shift Solenoid Valve SL) (Dokumen: RM0000013TU01GX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Torque Converter Clutch Solenoid Circuit Low (Shift Solenoid Valve SL) (Dokumen:
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short sirkuit dalam shift solenoid valve SL Shift solenoid valve SL TCM; Kondisi Deteksi: TCM mendeteksi short dalam sirkuit shift solenoid valve SL (sekali) saat shift solenoid valve SL dioperasikan (1-trip detection logic); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open sirkuit dalam shift solenoid valve SL Shift solenoid valve SL TCM; Kondisi Deteksi: TCM mendeteksi open dalam sirku
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor kabel transmisi C12. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (SHIFT SOLENOID VALVE SL - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS DAN KONEKTOR
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT SOLENOID VALVE SL: Lepas shift solenoid valve SL. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Berilah tegangan baterai 12 V ke shift solenoid valve dan periksa valve bergerak dan mengeluarkan suara kerja.
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SHIFT SOLENOID VALVE SL
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI KABEL TRANSMISI
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor C12 transmission wire. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 7 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-16 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: Terminal konektor shift solenoid velve SL - Bodi shift solenoid valve SL (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] OK: Positif baterai (+) → Konektor shift solenoid valve SL Negatif baterai (-) → Bodi shift solenoid va` : **Valve bergerak dan mengeluarkan suara kerja.**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 7 (SL) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-16 (SL) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: Konektor terminal shift solenoid valve SL - Bodi shift solenoid valve SL (20°C (` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] OK: Positif (+) baterai → Konektor shift solenoid valve SL Negatif (-) baterai → Bodi shift solen` : **Valve bergerak dan mengeluarkan noise pengoperasian.**

### DTC `P2770` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] High Sirkuit pada Torque Converter Clutch Solenoid (Shift Solenoid Valve SL) (Dokumen: RM0000013TU01GX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Torque Converter Clutch Solenoid Circuit High (Shift Solenoid Valve SL) (D
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Short sirkuit dalam shift solenoid valve SL Shift solenoid valve SL TCM; Kondisi Deteksi: TCM mendeteksi short dalam sirkuit shift solenoid valve SL (sekali) saat shift solenoid valve SL dioperasikan (1-trip detection logic); [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open sirkuit dalam shift solenoid valve SL Shift solenoid valve SL TCM; Kondisi Deteksi: TCM mendeteksi open dalam sirku
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor kabel transmisi C12. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (SHIFT SOLENOID VALVE SL - TCM): Lepas hubungan konektor TCM C24. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS DAN KONEKTOR
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — MEMERIKSA SHIFT SOLENOID VALVE SL: Lepas shift solenoid valve SL. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Berilah tegangan baterai 12 V ke shift solenoid valve dan periksa valve bergerak dan mengeluarkan suara kerja.
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI SHIFT SOLENOID VALVE SL
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI KABEL TRANSMISI
  - Langkah 1 (AUTOMATIC TRANSMISSION / TRANSAXLE A340E) — MEMERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor C12 transmission wire. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: 7 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-16 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: Terminal konektor shift solenoid velve SL - Bodi shift solenoid valve SL (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] OK: Positif baterai (+) → Konektor shift solenoid valve SL Negatif baterai (-) → Bodi shift solenoid va` : **Valve bergerak dan mengeluarkan suara kerja.**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: 7 (SL) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: C24-16 (SL) - Body ground (20°C (68°F))` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Tahanan Standar: Konektor terminal shift solenoid valve SL - Bodi shift solenoid valve SL (20°C (` : **11 sampai 15 Ω**
  - `[AUTOMATIC TRANSMISSION / TRANSAXLE A340E] OK: Positif (+) baterai → Konektor shift solenoid valve SL Negatif (-) baterai → Bodi shift solen` : **Valve bergerak dan mengeluarkan noise pengoperasian.**

### DTC `U0100` — [TRANSMISI/TRANSAXLE OTOMATIS A340F — SISTEM TRANSMISI OTOMATIS] Lost Communication with ECM / PCM "A" (Dokumen: RM0000012XN01GX) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E — SISTEM AUTOMATIC TRANSMISSION] Kehilangan Komunikasi dengan ECM/PCM "A" (Dokumen: RM0000012XN019X) | [AUTOMATIC TRANSMISSION / TRANSAXLE A340E —
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI/TRANSAXLE OTOMATIS A340F] Area Gangguan: Open atau short dalam TCM dan sirkuit ECM TCM ECM; Kondisi Deteksi: Tidak ada komunikasi dari ECM untuk periode waktu tertentu (1-trip detection logic); [AUTOMATIC TRANSMISSION / TRANSAXLE A340E] Area Gangguan: Open atau short sirkuit dalam TCM dan ECM TCM ECM; Kondisi Deteksi: Tidak terdapat komunikasi dari ECM untuk periode waktu tertentu (1-trip detection logic); [AUTOMATIC TRANSMISSION / TRA
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA ECM (TEGANGAN +B, MASA E1): Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Putar ignition switch ke off. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA TCM (TEGANGAN IG2, MASA E1): Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Putar ignition switch ke off. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERIKSA HARNESS DAN KONEKTOR (ECM - TCM): Lepas hubungan konektor ECM G38. -> Lepas hubungan konektor TCM G41 -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — KONFIRMASI DTC: Menghapus DTC. -> Ganti TCM. -> Hidupkan mesin. -> Baca DTC.
  - Langkah 5 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — LANJUTKAN KE SISTEM ECD (SIRKUIT ECM POWER SOURCE )
  - Langkah 6 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — LANJUTKAN KE SIRKUIT POWER SOURCE
  - Langkah 7 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (TRANSMISI/TRANSAXLE OTOMATIS A340F) — GANTI TCM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: G39-1 (+B) - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C23-7 (E1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tegangan Standar: G41-6 (IG2) - Masa bodi (Ignition switch ON)` : **11 sampai 14 V**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: C24-1 (E1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: G38-22 (CAN+) - G41-21 (CAN+) (Selalu)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: G38-21 (CAN-) - G41-20 (CAN-) (Selalu)` : **Di bawah 1 Ω**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: G38-22 (CAN+) atau G41-21 (CAN+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI/TRANSAXLE OTOMATIS A340F] Tahanan Standar: G38-21 (CAN-) atau G41-20 (CAN-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `U0101` — [ENGINE CONTROL 1KD-FTV — SISTEM ECD] Kehilangan komunikasi dengan TCM (Dokumen: RM000001O2V077X) | [KONTROL MESIN 1KD-FTV — SISTEM ECD] Kehilangan komunikasi dengan TCM (Dokumen: RM000001O2V078X) | [KONTROL MESIN 1KD-FTV — SISTEM ECD] Kehilangan komunikasi dengan TCM (Dokumen: RM000001O2V0ANX)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE CONTROL 1KD-FTV] Area Gangguan: ECM TCM ECM ke sirkuit TCM; [KONTROL MESIN 1KD-FTV] Area Gangguan: ECM TCM ECM ke sirkuit TCM; [KONTROL MESIN 2KD-FTV] Area Gangguan: ECM TCM ECM ke sirkuit TCM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE CONTROL 1KD-FTV) — PERIKSA SETIAP DTC OUTPUT LAINNYA (DI SAMPING DTC U0101): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (ENGINE CONTROL 1KD-FTV) — MEMERIKSA SIRKUIT POWER SOURCE TCM (POWER SOURCE DAN MASA BODI): Lepas hubungan konektor TCM -> Ukur tegangan sesuaikan dengan nilai dalam tabel di bawah. -> Hubungkan kembali konektor TCM
  - Langkah 3 (ENGINE CONTROL 1KD-FTV) — PERIKSA HARNESS DAN KONEKTOR (ECM - TCM): Lepas hubungan konektor TCM -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor TCM -> Hubungkan kembali konektor ECM.
  - Langkah 4 (ENGINE CONTROL 1KD-FTV) — GANTI ECM: Ganti ECM (Lihat halaman ).
  - Langkah 5 (ENGINE CONTROL 1KD-FTV) — PERIKSA APAKAH DTC MUNCUL LAGI ATAU TIDAK (DTC U0101): Hubungkan intelligent tester ke DLC3. -> Putar ignition switch ke-ON dan hidupkan tester. -> Masuk ke menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 6 (ENGINE CONTROL 1KD-FTV) — LANJUTKAN KE BAGAN DTC
  - Langkah 7 (ENGINE CONTROL 1KD-FTV) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (ENGINE CONTROL 1KD-FTV) — GANTI TCM
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE CONTROL 1KD-FTV] Tegangan Standar: G41-5 (BATT) - C24-1 (E1) (Ignition switch ON)` : **11 sampai 14 V**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G38-22 (CAN+) - G41-21 (CAN+) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G38-21 (CAN-) - G41-20 (CAN-) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G38-22 (CAN+) atau G41-21 (CAN+) - Masa bodi atau terminal lainnya (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[ENGINE CONTROL 1KD-FTV] Tahanan Standar: G38-21 (CAN-) atau G41-20 (CAN-) - Masa bodi atau terminal lainnya (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[KONTROL MESIN 1KD-FTV] Voltase Standar: G41-5 (BATT) - C24-1 (E1) (Ignition switch ON)` : **11 sampai 14 V**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: G38-22 (CAN+) - G41-21 (CAN+) (Selalu)` : **Dibawah 1 Ω**
  - `[KONTROL MESIN 1KD-FTV] Tahanan Standar: G38-21 (CAN-) - G41-20 (CAN-) (Selalu)` : **Dibawah 1 Ω**
