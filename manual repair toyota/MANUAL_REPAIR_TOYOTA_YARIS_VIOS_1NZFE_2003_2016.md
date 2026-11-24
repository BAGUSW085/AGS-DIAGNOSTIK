# Buku Pedoman Reparasi Resmi Toyota Yaris & Vios / Limo (RMO2C4EL & RMO5K3EL · Mesin 1NZ-FE 1.5L VVT-i & Transaxle Otomatis U340E)

- **Pack ID AGOS**: `toyota_yaris_vios_1nzfe_2003_2016`
- **Merek & Model**: Toyota Yaris / Vios / Sienta (Toyota Yaris (NCP91) & Vios / Limo (NCP93) — Mesin 1NZ-FE 1.5L VVT-i)
- **Rentang Tahun**: 2003–2016
- **Kode Mesin Tercakup**: `1NZ-FE`
- **Total Kode DTC Terindeks**: **208 Kode DTC**
- **Total Pinout Terminal ECM/ECU**: **885 Terminal**
- **Total Spesifikasi Sensor & Data List**: **431 Parameter**

---

## 1. Ringkasan Bab & Sistem (`toc_rpr.xml`)

| Kategori Servis | Nama Sistem / Mesin | Jumlah Sub-Bab Prosedur |
| :--- | :--- | :---: |
| PENDAHULUAN | PENDAHULUAN | 10 |
| PENDAHULUAN | KATA PENGANTAR / PERINGATAN / TOC BAB | 2 |
| PENDAHULUAN | TOC2 | 2 |
| PENDAHULUAN | TOC3 | 2 |
| PERSIAPAN | PERSIAPAN | 113 |
| SPESIFIKASI SERVIS | SPESIFIKASI SERVIS | 72 |
| MESIN | SISTEM KONTROL MESIN 1NZ-FE | 95 |
| MESIN | MEKANISME MESIN 1NZ-FE | 39 |
| MESIN | BAHAN BAKAR 1NZ-FE | 20 |
| MESIN | KONTROL EMISI 1NZ-FE | 26 |
| MESIN | EXHAUST 1NZ-FE | 3 |
| MESIN | PENDINGINAN 1NZ-FE | 27 |
| MESIN | PELUMASAN 1NZ-FE | 11 |
| MESIN | PENGAPIAN 1NZ-FE | 8 |
| MESIN | STARTING 1NZ-FE | 72 |
| MESIN | PENGISIAN 1NZ-FE | 10 |
| TRANSMISI | TRANSAXLE OTOMATIS U340E | 104 |
| TRANSMISI | KOPLING | 35 |
| TRANSMISI | TRANSAXLE MANUAL C50 | 43 |
| DRIVE LINE | DRIVE SHAFT | 6 |
| SUSPENSI & AXLE | AXLE | 20 |
| SUSPENSI & AXLE | SUSPENSI | 49 |
| SUSPENSI & AXLE | BAN DAN RODA | 4 |
| REM | KONTROL REM | 92 |
| REM | REM | 63 |
| REM | REM PARKIR | 12 |
| STEERING | STEERING COLUMN | 37 |
| STEERING | POWER STEERING | 48 |
| SISTEM HEATER & AIR CONDITIONING | AIR CONDITIONING | 69 |
| RESTRAINT | SUPPLEMENTAL RESTRAINT SYSTEM | 55 |
| RESTRAINT | SEAT BELT | 38 |
| KEAMANAN | ANTI PENCURIAN | 33 |
| KEAMANAN | ENGINE IMMOBILISER | 42 |
| KELISTRIKAN BODI | PENERANGAN | 112 |
| KELISTRIKAN BODI | WIPER DAN WASHER | 39 |
| KELISTRIKAN BODI | DOOR LOCK | 131 |
| KELISTRIKAN BODI | METER | 35 |
| KELISTRIKAN BODI | AUDIO / VISUAL | 59 |
| KELISTRIKAN BODI | HORN | 12 |
| KELISTRIKAN BODI | SISTEM LAINNYA | 3 |
| BODI | KACA DEPAN / KACA JENDELA | 65 |
| BODI | KACA SPION | 20 |
| BODI | PANEL INSTRUMEN | 13 |
| BODI | TEMPAT DUDUK | 25 |
| BODI | KAP MESIN / PINTU | 17 |
| BODI | EKSTERIOR | 55 |
| BODI | INTERIOR | 11 |
| SISTEM KOMUNIKASI | KOMUNIKASI CAN | 48 |
| MESIN | INTAKE 1NZ-FE | 7 |

---

## 2. Tabel Pinout & Tegangan Standar Terminal ECM / ECU

| Terminal (Simbol & Pin) | Warna Kabel & Deskripsi | Kondisi & Standar Tegangan / Tahanan |
| :--- | :--- | :--- |
| `[1NZ-FE] BATT (A21-20) - E1 (C20-104)` | Warna Kabel: Y - W — Baterai (untuk mengukur voltase baterai dan untuk memori ECM) | Selalu: 11 sampai 14 V |
| `[1NZ-FE] +B (A21-2) - E1 (C20-104)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] +B2 (A21-1) - E1 (C20-104)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] +BM (A21-3) - ME01 (C20-43)` | Warna Kabel: GR - BR — Power source aktuator throttle | Selalu: 11 sampai 14 V |
| `[1NZ-FE] IGT1 (C20-85) - E1 (C20-104)` | Warna Kabel: W - W — Koil pengapian dengan igniter (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] IGT2 (C20-84) - E1 (C20-104)` | Warna Kabel: O - W — Koil pengapian dengan igniter (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] IGT3 (C20-83) - E1 (C20-104)` | Warna Kabel: G - W — Koil pengapian dengan igniter (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] IGT4 (C20-82) - E1 (C20-104)` | Warna Kabel: LG - W — Koil pengapian dengan igniter (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] IGF1 (C20-81) - E1 (C20-104)` | Warna Kabel: Y - W — Koil pengapian dengan igniter (sinyal konfirmasi pengapian) | Switch pengapian on (IG): 4.5 sampai 5.5 V / Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] NE+ (C20-122) - NE- (C20-121)` | Warna Kabel: L - P — Sensor posisi crankshaft | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[1NZ-FE] G2+ (C20-99) - NE- (C20-121)` | Warna Kabel: B - P — Sensor posisi camshaft | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[1NZ-FE] #10 (C20-108) - E01 (C20-45)` | Warna Kabel: SB - BR — Injektor | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] #20 (C20-107) - E01 (C20-45)` | Warna Kabel: GR - BR — Injektor | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] #30 (C20-106) - E01 (C20-45)` | Warna Kabel: P - BR — Injektor | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] #40 (C20-105) - E01 (C20-45)` | Warna Kabel: L - BR — Injektor | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] HT1A (C20-109) - E03 (C20-86)` | Warna Kabel: G - W — Heater sensor heated oxygen (sensor 1) | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] OX1A (C20-112) - EX1A (C20-90)` | Warna Kabel: W - L — Sensor heated oxygen (sensor 1) | Putaran mesin dipertahankan pada 2,500 rpm selama 2 menit setelah sensor dipanaskan: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[1NZ-FE] HT1B (C20-47) - E03 (C20-86)` | Warna Kabel: LG - W — Heater sensor heated oxygen (sensor 2) | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] OX1B (C20-64) - EX1B (C20-87)` | Warna Kabel: G- GR — Sensor heated oxygen (sensor 2) | Putaran mesin dipertahankan pada 2,500 rpm selama 2 menit setelah sensor dipanaskan: Pembangkitan pulsa (lihat bentuk gelombang 4) |
| `[1NZ-FE] KNK1 (C20-110) - EKNK (C20-111)` | Warna Kabel: R - G — Sensor knock | Biarkan putaran mesin pada 4,000 rpm setelah memanaskan mesin: Pembangkitan pulsa (lihat bentuk gelombang 5) |
| `[1NZ-FE] SPD (A21-8) - E1 (C20-104)` | Warna Kabel: V - W — Sinyal kecepatan dari meter kombinasi | Dikendarai pada 20 km/jam (12 mph): Pembangkitan pulsa (lihat bentuk gelombang 6) |
| `[1NZ-FE] THW (C20-97) - ETHW (C20-96)` | Warna Kabel: L - P — Sensor temperatur cairan pendingin mesin | Idling, Temperatur cairan pendingin mesin 80°C (176°F): 0.2 sampai 1.0 V |
| `[1NZ-FE] ACCR (A21-13) - E01 (C20-45)` | Warna Kabel: G - BR — Sinyal kontrol relay ACC (Accessory) | Cranking: Di bawah 1.5 V |
| `[1NZ-FE] THA (C20-65) - ETHA (C20-88)` | Warna Kabel: P - O — Sensor temperatur udara masuk | Idling, temperatur udara masuk 20°C (68°F): 1.5 sampai 3.0 V |
| `[1NZ-FE] VG (C20-118) - E2G (C20-116)` | Warna Kabel: GR - LG — Mass air flow meter | Idling, Posisi shift lever P atau N, switch A/C OFF: 0.5 sampai 3.0 V |
| `[1NZ-FE] W (A21-24) - E1 (C20-104)` | Warna Kabel: B - W — MIL | Switch pengapian on (IG): Di bawah 1.5 V / Idling: 11 sampai 14 V |
| `[1NZ-FE] STA (A21-48) - E1 (C20-104)` | Warna Kabel: BR - W — Sinyal starter | Cranking: 5.5 V atau lebih |
| `[1NZ-FE] VTA1 (C20-115) - ETA (C20-91)` | Warna Kabel: Y - V — Sensor posisi throttle (untuk kontrol mesin) | Switch pengapian on (IG), Throttle valve tertutup penuh: 0.5 sampai 1.2 V / Switch pengapian on (IG), Throttle valve terbuka penuh: 3.2 sampai 4.8 V |
| `[1NZ-FE] VTA2 (C20-114) - ETA (C20-91)` | Warna Kabel: GR - V — Sensor posisi throttle (untuk deteksi malfungsi sensor) | Switch pengapian on (IG), Throttle valve tertutup penuh: 2.1 sampai 3.1 V / Switch pengapian on (IG), Throttle valve terbuka penuh: 4.5 sampai 5.5 V |
| `[1NZ-FE] VCTA (C20-67) - ETA (C20-91)` | Warna Kabel: W - V — Power source sensor (voltase spesifikasi) | Switch pengapian on (IG): 4.5 sampai 5.5 V |
| `[1NZ-FE] M+ (C20-42) - ME01 (C20-43)` | Warna Kabel: G - BR — Aktuator throttle | Idling dengan mesin panas: Pembangkitan pulsa (lihat bentuk gelombang 7) |
| `[1NZ-FE] M- (C20-41) - ME01 (C20-43)` | Warna Kabel: R - BR — Aktuator throttle | Idling dengan mesin panas: Pembangkitan pulsa (lihat bentuk gelombang 8) |
| `[1NZ-FE] VCPA (A21-57) - EPA (A21-59)` | Warna Kabel: B - G — Power source untuk sensor posisi pedal akselerator (untuk VPA) | Switch pengapian on (IG): 4.5 sampai 5.5 V |
| `[1NZ-FE] VPA (A21-55) - EPA (A21-59)` | Warna Kabel: R - G — Sensor posisi pedal akselerator (untuk kontrol mesin) | Switch pengapian (IG), pedal akselerator dibebaskan: 0.5 sampai 1.1 V / Switch pengapian on (IG), pedal akselerator ditekan penuh: 2.6 sampai 4.5 V |
| `[1NZ-FE] VPA2 (A21-56) - EPA2 (A21-60)` | Warna Kabel: L - BR — Sensor posisi pedal akselerator (untuk deteksi malfungsi sensor) | Switch pengapian (IG), pedal akselerator dibebaskan: 1.2 sampai 2.0 V / Switch pengapian on (IG), pedal akselerator ditekan penuh: 3.4 sampai 5.0 V |
| `[1NZ-FE] VCP2 (A21-58) - EPA2 (A21-60)` | Warna Kabel: W - BR — Power source untuk sensor posisi pedal akselerator (untuk VPA2) | Switch pengapian on (IG): 4.5 sampai 5.5 V |
| `[1NZ-FE] STP (A21-36) - E1 (C20-104)` | Warna Kabel: G - W — Switch lampu rem | Pedal rem ditekan: 11 sampai 14 V / Pedal rem dibebaskan: Di bawah 1.5 V |
| `[1NZ-FE] ST1- (A21-35) - E1 (C20-104)` | Warna Kabel: Y - W — Switch lampu rem (berlawanan untuk terminal STP) | Switch pengapian on (IG), pedal rem ditekan: Di bawah 1.5 V / Switch pengapian (IG), pedal rem dibebaskan: 11 sampai 14 V |
| `[1NZ-FE] PRG (C20-49) - E01 (C20-45)` | Warna Kabel: L - BR — VSV untuk EVAP | Switch pengapian on (IG): 11 sampai 14 V / Idling: Pembangkitan pulsa (lihat bentuk gelombang 9) |
| `[1NZ-FE] FC (A21-7) - E01 (C20-45)` | Warna Kabel: V - BR — Kontrol pompa bahan bakar | Switch pengapian on (IG): 11 sampai 14 V / Idling: Di bawah 1.5 V |
| `[1NZ-FE] TACH (A21-15) - E1 (C20-104)` | Warna Kabel: LG - W — Putaran mesin | Idling: Pembangkitan pulsa (lihat bentuk gelombang 10) |
| `[1NZ-FE] TC (A21-27) - E1 (C20-104)` | Warna Kabel: P - W — Terminal TC dari DLC 3 | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] OC1+ (C20-100) - OC1- (C20-123)` | Warna Kabel: BR - R — Camshaft timing oil control valve (OCV) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 11) |
| `[1NZ-FE] CANH (A21-41) - E1 (C20-104)` | Warna Kabel: L - W — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 12) |
| `[1NZ-FE] CANL (A21-49) - E1 (C20-104)` | Warna Kabel: W - W — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 13) |
| `[1NZ-FE] ELS (A21-31) - E1 (C20-104)` | Warna Kabel: G - W — Beban kelistrikan | Switch lampu belakang on: 7.5 sampai 14 V / Switch lampu belakang off: Di bawah 1.5 V |
| `[1NZ-FE] ELS3 (A21-33) - E1 (C20-104)` | Warna Kabel: V - W — Beban kelistrikan | Switch lampu kabut ON: 7.5 sampai 14 V / Switch lampu kabut off: Di bawah 1.5 V |
| `[1NZ-FE] FAN2 (A21-22) - E1 (C20-104)` | Warna Kabel: LG - W — Relay fan No. 2 | Idling dengan temperatur cairan pendingin mesin tinggi: Di bawah 1.5 V |
| `[1NZ-FE] ALT (C20-50) - E1 (C20-104)` | Warna Kabel: P - W — Generator | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] IGSW (A21-28) - E1 (C20-104)` | Warna Kabel: R - W — Switch pengapian | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] MREL (A21-44) - E1 (C20-104)` | Warna Kabel: GR - W — Relay EFI | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] STSW (A21-14) - E1 (C20-104)` | Warna Kabel: B - W — Sinyal switch pengapian | Posisi shift lever P atau N, switch pengapian START: 6.0 V atau lebih |
| `[1NZ-FE] STAR (C20-52) - E1 (C20-104)` | Warna Kabel: O - W — Kontrol relay starter | Switch pengapian on (IG): Di bawah 1.5 V / Cranking: 6.0 V atau lebih |
| `[STARTING 1NZ-FE] BECU (4B-30) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[STARTING 1NZ-FE] AM1 (D65-1) - Masa bodi` | Warna Kabel: O - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[STARTING 1NZ-FE] AM2 (D64-6) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[STARTING 1NZ-FE] SSW1 (D65-10) - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal switch pengapian | Dorong switch pengapian: Di bawah 1 Ω / Switch pengapian tidak didorong: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] SSW2 (D65-9) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal switch pengapian | Dorong switch pengapian: Di bawah 1 Ω / Switch pengapian tidak didorong: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] GND1 (4E-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] GND2 (D65-4) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] LIN1 (4D-9) - Masa bodi` | Warna Kabel: P - Masa bodi — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] ACCD (D64-4) - GND2 (D65-4)` | Warna Kabel: LG - W-B — Sinyal ACC | Switch pengapian on (ACC): 10 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[STARTING 1NZ-FE] IG2D (D65-5) - GND2 (D65-4)` | Warna Kabel: P - W-B — Sinyal IG2 | Switch pengapian on (IG): 10 sampai 14 V / Switch pengapian on (ACC): Di bawah 1 V |
| `[STARTING 1NZ-FE] SLR+ (D64-7) - GND2 (D65-4)` | Warna Kabel: L - W-B — Sinyal motor steering lock | Motor steering lock bekerja: Di bawah 1 V / Motor steering lock motor tidak bekerja: 10 sampai 14 V |
| `[STARTING 1NZ-FE] SLP (D64-18) - GND2 (D65-4)` | Warna Kabel: GR - W-B — Sinyal posisi aktuator steering lock | Steering lock telah terkunci: 10 sampai 14 V / Kunci steering dibebaskan: Di bawah 1 V |
| `[STARTING 1NZ-FE] SPD (4C-8) - GND2 (D65-4)` | Warna Kabel: SB - W-B — Sinyal kecepatan dari meter kombinasi | Switch pengapian on (IG), putar roda penggerak perlahan-lahan: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[STARTING 1NZ-FE] TACH (D66-2) - GND2 (D65-4)` | Warna Kabel: L - W-B — Sinyal Tachometer | Mesin hidup: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[STARTING 1NZ-FE] STSW (D66-4) - GND2 (D65-4)` | Warna Kabel: B - W-B — Sinyal permintaan aktivasi starter | Pedal rem diinjak, switch pengapian didorong sekali: 10 sampai 14 V* |
| `[STARTING 1NZ-FE] STP (D64-14) - GND2 (D65-4)` | Warna Kabel: G - W-B — Switch lampu rem | Pedal rem ditekan: Di bawah 1 V |
| `[STARTING 1NZ-FE] STR (D66-3) - GND2 (D65-4)` | Warna Kabel: GR - W-B — Switch posisi parkir/netral | Posisi shift lever P atau N: Di bawah 1 V |
| `[STARTING 1NZ-FE] STR2 (D66-14) - GND2 (D65-4)` | Warna Kabel: O - W-B — Sinyal starter | Pedal rem diinjak, posisi shift lever P atau N, switch pengapian on(ST): 10 sampai 14 V* |
| `[STARTING 1NZ-FE] INDS (D66-1) - GND2 (D65-4)` | Warna Kabel: SB - W-B — Sinyal kondisi kendaraan | Pedal rem diinjak, switch pengapian off, on (ACC, IG): 10 sampai 14 V |
| `[STARTING 1NZ-FE] INDW (D66-8) - GND2 (D65-4)` | Warna Kabel: Y - W-B — Sinyal kondisi kendaraan | Pedal rem dibebaskan, switch pengapian off, on (ACC, IG): 10 sampai 14 V |
| `[STARTING 1NZ-FE] SWIL (D65-8) - GND2 (D65-4)` | Warna Kabel: LG - W-B — Sinyal penerangan | Switch kontrol lampu TAIL atau HEAD: 10 sampai 14 V |
| `[STARTING 1NZ-FE] P (D64-15) - GND2 (D65-4)` | Warna Kabel: P - W-B — Sinyal shift lock | Posisi shift lever P: 10 sampai 14 V / Posisi shift lever kecuali P: Di bawah 1 V |
| `[STARTING 1NZ-FE] +B1 (D60-1) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[STARTING 1NZ-FE] IG (D60-18) - Masa bodi` | Warna Kabel: BR - Masa bodi — Power supply pengapian | Switch pengapian on (IG): 10 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[STARTING 1NZ-FE] LIN (D60-10) - Masa bodi` | Warna Kabel: P - Masa bodi — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] E (D60-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] BATT (A21-20) - E1 (C20-104)` | Warna Kabel: Y - W — Baterai (untuk mengukur voltase baterai dan untuk memori ECM) | Selalu: 10 sampai 14 V |
| `[STARTING 1NZ-FE] +B (A21-2) - E1 (C20-104)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 10 sampai 14 V |
| `[STARTING 1NZ-FE] +B2 (A21-1) - E1 (C20-104)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 10 sampai 14 V |
| `[STARTING 1NZ-FE] IGSW (A21-28) - E1 (C20-104)` | Warna Kabel: R - W — Sinyal switch pengapian | Switch pengapian on (IG): 10 sampai 14 V |
| `[STARTING 1NZ-FE] E1 (C20-104) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] E01 (C20-45) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] E02 (C20-44) - Masa bodi` | Warna Kabel: B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] E03 (C20-86) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] STA (A21-48) - E1 (C20-104)` | Warna Kabel: BR - W — Sinyal kerja relay starter | Cranking: 5.5 V atau lebih |
| `[STARTING 1NZ-FE] STSW (A21-14) - E1 (C20-104)` | Warna Kabel: B - W — Sinyal kerja relay starter | Tuas pemindah gigi p atau N , switch pengapian START: 6.0 V atau lebih |
| `[STARTING 1NZ-FE] ACCR (C21-13) - E1 (C20-104)` | Warna Kabel: G - W — Sinyal pemutus relay ACC (output) | Cranking: Di bawah 1.5 V |
| `[STARTING 1NZ-FE] TACH (A21-15) - E1 (C20-104)` | Warna Kabel: LG - W — Sinyal putaran mesin (output) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[STARTING 1NZ-FE] STAR (C20-52) - E1 (C20-104)` | Warna Kabel: O - W — Sinyal penggerak relay starter | Cranking: 6.0 V atau lebih |
| `[STARTING 1NZ-FE] B (D56-7) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[STARTING 1NZ-FE] IG2 (D56-6) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply pengapian | Switch pengapian on (IG): 10 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[STARTING 1NZ-FE] GND (D56-1) - Masa bod` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] SGND (D56-2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] SLP1 (D56-4) - GND (D56-1)` | Warna Kabel: GR - W-B — Sinyal posisi aktuator steering lock | Steering lock telah terkunci: 10 sampai 14 V / Kunci steering dibebaskan: Di bawah 1 V |
| `[A/T U340E] L (C20-74) - E1 (C20-104)` | Warna Kabel: V - W — Sinyal switch posisi pemindahan L | Switch pengapian on (IG) dan shift lever posisi L: 10 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi L: Di bawah 1 V |
| `[A/T U340E] 2 (C20-55) - E1 (C20-104)` | Warna Kabel: G - W — 2 sinyal switch posisi pemindahan | Switch pengapian on (IG) dan shift lever posisi 2: 10 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi 2: Di bawah 1 V |
| `[A/T U340E] ODMS (A21-26) - E1 (C20-104)` | Warna Kabel: O - W — 3 sinyal switch posisi pemindahan | Switch pengapian on (IG) dan shift lever posisi 3: 10 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi 3: Di bawah 1 V |
| `[A/T U340E] D (C20-56) - E1 (C20-104)` | Warna Kabel: L - W — Sinyal switch posisi pemindahan D | Switch pengapian on (IG) dan shift lever posisi D atau 3: 10 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi posisi D atau 3: Di bawah 1 V |
| `[A/T U340E] R (C20-53) - E1 (C20-104)` | Warna Kabel: R - W — Sinyal switch posisi pemindahan R | Switch pengapian on (IG) dan shift lever posisi R: 10 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi R: Di bawah 1 V |
| `[A/T U340E] N (C20-54) - E1 (C20-104)` | Warna Kabel: SB - W — Sinyal switch posisi pemindahan N | Switch pengapian on (IG) dan shift lever posisi N: 10 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi N: Di bawah 1 V |
| `[A/T U340E] P (C20-73) - E1 (C20-104)` | Warna Kabel: R - W — Sinyal switch posisi pemindahan P | Switch pengapian on (IG) dan shift lever posisi P: 10 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi P: Di bawah 1 V |
| `[A/T U340E] NT+ (C20-125) - NT- (C20-124)` | Warna Kabel: B - G — Sinyal speed sensor (NT) | Mesin hidup: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[A/T U340E] STP (A21-36) - E1 (C20-104)` | Warna Kabel: G - W — Sinyal switch lampu rem | Pedal rem ditekan: 7.5 sampai 14 V / Pedal rem dibebaskan: Di bawah 1.5 V |
| `[A/T U340E] SPD (A21-8) - E1 (C20-104)` | Warna Kabel: V - W — Sinyal kecepatan | Switch pengapian on (IG), dan putar roda penggerak perlahan-lahan: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T U340E] S1 (C20-79) - E1 (C20-104)` | Warna Kabel: SB - W — Sinyal solenoid S1 | Switch pengapian on (IG): 10 sampai 14 V / gear ke-1 atau ke-2: 10 sampai 14 V / gigi ke-3 atau gigi ke-4: Di bawah 1 V |
| `[A/T U340E] S2 (C20-78) - E1 (C20-104)` | Warna Kabel: L - W — Sinyal solenoid S2 | Switch pengapian on (IG): Di bawah 1 V / gigi ke-1 atau gigi ke-4: 10 sampai 14 V / gigi ke-2 atau gigi ke-3: Di bawah 1 V |
| `[A/T U340E] ST (C20-80) - E1 (C20-104)` | Warna Kabel: GR - W — Sinyal solenoid ST | Posisi D (gear ke-3 ←→ gear ke-4): Di bawah 1 V ←→ 10 sampai 14 V |
| `[A/T U340E] SLT+ (C20-76) - SLT- (C20-75)` | Warna Kabel: G - W — Sinyal solenoid SLT | Putaran idle mesin: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[A/T U340E] SL (C20-57) - E1 (C20-104)` | Warna Kabel: P - W — Sinyal solenoid SL | Switch pengapian on (IG): Di bawah 1 V / Pengendaraan kendaraan dalam lock up rage: 10 sampai 14 V |
| `[A/T U340E] THO1 (C20-72) - ETHO (C20-95)` | Warna Kabel: Y - B — Sinyal sensor temperatur ATF (Automatic Transmission Fluid) | Temperatur ATF: 10°C (50 °F) sampai 145 °C (293 °F): 4 sampai 0 V |
| `[KONTROL REM] +BS (A15-1) - Masa bodi` | Warna Kabel: W - Masa bodi — Power source solenoid valve | Selalu: 10 sampai 14 V |
| `[KONTROL REM] GND1 (A15-2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa ECU skid control | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] STP (A15-10) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu rem | Switch lampu rem ON Pedal rem ditekan: 8 sampai 14 V / Switch lampu rem OFF Pedal rem dibebaskan: Di bawah 1.5 V |
| `[KONTROL REM] +BM (A15-23) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply relay motor | Selalu: 10 sampai 14 V |
| `[KONTROL REM] GND2 (A15-24) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa aktuator pump motor | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] IG1 (A15-25) - Masa bodi` | Warna Kabel: B - Masa bodi — Power source ECU | Switch pengapian on (IG): 10 sampai 14 V |
| `[KONTROL REM] PKB (4C-2) - Masa bodi` | Warna Kabel: Y - Masa bodi — Input switch rem parkir | Switch rem parkir ON: Di bawah 1 Ω / Switch rem parkir OFF: 10 kΩ atau lebih tinggi |
| `[KONTROL REM] A38-1 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa ECU skid control | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] A38-12 (+BS) - Masa bodi` | Warna Kabel: W - Masa bodi — Power source solenoid relay | Selalu: 11 sampai 14 V |
| `[KONTROL REM] A38-13 (GND2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa pump motor | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] A38-28 (STP) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu rem | Switch lampu rem ON → OFF (Pedal rem ditekan → dibebaskan): 8 sampai 14 V → Di bawah 1.5 V |
| `[KONTROL REM] A38-24 (+BM) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply relay motor | Selalu: 11 sampai 14 V |
| `[KONTROL REM] A38-25 (CANH) - A38-14 (CANL)` | Warna Kabel: G - W — CAN BUS | Switch pengapian off: 54 sampai 69 Ω |
| `[KONTROL REM] A38-34 (IG1) - Masa bodi` | Warna Kabel: B - Masa bodi — Power source ECU | Switch pengapian ON: 11 sampai 14 V |
| `[AIR CONDITIONING] PSW (E8-12) - GND (E8-24)` | Warna Kabel: GR - W-B — Switch sinyal tekanan air conditioning | Tekanan refrigerant: normal: Di bawah 1 V / Tekanan refrigerant: Abnormal (kurang dari 0.196 kPa (2.0 kgf/cm 2 ] atau lebih dari 3.14 MPa [32 kgf/cm 2 ]): 10 sampai 14 V |
| `[AIR CONDITIONING] IG+ (E8-14) - GND (E8-24)` | Warna Kabel: Y - W-B — Power source (IG) | Switch pengapian: on (IG): 10 sampai 14 V |
| `[AIR CONDITIONING] MGC (E8-15) - GND (E8-24)` | Warna Kabel: LG - W-B — HTR SUB1 / AC MG Sinyal operasi relay | Mesin idle: 10 sampai 14 V → Di bawah 1 V / Kontrol heater (switch blower): 0 → 1: 10 sampai 14 V → Di bawah 1 V / Volume Cooler: ON: 10 sampai 14 V → Di bawah 1 V |
| `[AIR CONDITIONING] AC1 (E8-17) - GND (E8-24)` | Warna Kabel: R - W-B — Sinyal pemesan idle-up | Mesin idle: 10 sampai 14 V / Magnet Clutch tidak mengait: 10 sampai 14 V / Mesin idle: Di bawah 1 V / Magnet Clutch mengait: Di bawah 1 V |
| `[AIR CONDITIONING] ACT (E8-19) - GND (E8-24)` | Warna Kabel: B - W-B — Magnet pada permit signal | Mesin idle: 4.5 sampai 5.5 V / Switch A/C: OFF: 4.5 sampai 5.5 V / Switch blower: ON: 4.5 sampai 5.5 V / Mesin idle: Di bawah 1 V / Switch A/C: OFF: Di bawah 1 V / Switch blower: ON: Di bawah 1 V |
| `[AIR CONDITIONING] SBLW (E8-21) - GND (E8-24)` | Warna Kabel: BR - W-B — Sinyal motor blower ON | Switch pengapian: on (IG): 10 sampai 14 V → Di bawah 1 V / Kontrol heater (switch blower): 0 → 1: 10 sampai 14 V → Di bawah 1 V |
| `[AIR CONDITIONING] TE (E8-22) - SG-2 (E8-23)` | Warna Kabel: GR - L — Sinyal sensor temperatur evaporator | Switch pengapian: on (IG): 1.0 sampai 1.3 V / Temperatur dekat evaporator: 15°C (59°F): 1.0 sampai 1.3 V |
| `[AIR CONDITIONING] SG-2 (E8-23) - Masa bodi` | Warna Kabel: L - Masa bodi — Masa untuk sensor temperatur evaporator | Selalu: Di bawah 1.0 Ω |
| `[AIR CONDITIONING] GND (E8-24) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa untuk power supply utama | Selalu: Di bawah 1.0 Ω |
| `[AIR CONDITIONING] B/V (E8-26) - SG-2 (E8-23)` | Warna Kabel: LG - Masa bodi — Sinyal penyetelan temperatur ruang | Switch pengapian: on (IG): 4.5 sampai 5.5 V → Di bawah 1 V / Knob kontrol heater No. 3: OFF → Max cool: 4.5 sampai 5.5 V → Di bawah 1 V |
| `[SEAT BELT] D1-1 (IG2) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal switch pengapian | Switch pengapian off → on (IG): Di bawah 1 V → 11 sampai 14 V |
| `[SEAT BELT] D1-2 (ECUB) - Masa Bodi` | Warna Kabel: L - Masa Bodi — Baterai | Selalu: 11 sampai 14 V |
| `[SEAT BELT] D1-24 (ET) - Masa Bodi` | Warna Kabel: BR - Masa Bodi — Masa | Selalu: Di bawah 1 Ω |
| `[SEAT BELT] D1-20 (CANH) - D1-24 (ET)` | Warna Kabel: G - BR — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[SEAT BELT] D1-21 (CANL) - D1-24 (ET)` | Warna Kabel: W - BR — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[SEAT BELT] 4B-30 (ECUB) - 4E-17 (GND1)` | Warna Kabel: L - W-B — Baterai | Selalu: 11 sampai 14 V |
| `[SEAT BELT] 4E-17 (GND1) - Masa Bodi` | Warna Kabel: W-B - Masa Bodi — Masa | Selalu: Di bawah 1 Ω |
| `[SEAT BELT] D64-26 (DBKL)*1 - Masa bodi` | Warna Kabel: W - Masa Bodi — Sinyal seat inner belt assembly depan (sisi pengemudi) | Switch pengapian on (IG) Tongue plate telah dikenakan: Di bawah 1 V |
| `[SEAT BELT] D64-26 (DBKL)*1 - Masa Bodi` | Warna Kabel: W - Masa Bodi — Sinyal seat inner belt assembly depan (sisi pengemudi) | Switch pengapian on (IG) Tongue plate tidak dikenakan: 11 sampai 14 V |
| `[SEAT BELT] D66-15 (CANH)*1 - 4E-17 (GND1)` | Warna Kabel: R - W-B — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[SEAT BELT] D66-16 (CANL)*1 - 4E-17 (GND1)` | Warna Kabel: W - W-B — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[SEAT BELT] D33-9 (DBKL)*2 - Masa Bodi` | Warna Kabel: W - Masa Bodi — Sinyal seat inner belt assembly depan (sisi pengemudi) | Switch pengapian on (IG) Tongue plate telah dikenakan: Di bawah 1 V / Switch pengapian on (IG) Tongue plate tidak dikenakan: 11 sampai 14 V |
| `[SEAT BELT] D33-23 (CANH)*2 - Masa Bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[SEAT BELT] D33-22 (CANL)*2 - Masa Bodi` | Warna Kabel: W - masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ANTI PENCURIAN] +B1 (D74-11) - Bodi masa` | Warna Kabel: B - Masa bodi — Baterai | Selalu: 10 sampai 14 V |
| `[ANTI PENCURIAN] +B2 (D74-13) - Bodi masa` | Warna Kabel: BR - Masa bodi — Baterai | Selalu: 10 sampai 14 V |
| `[ANTI PENCURIAN] IG (D74-9) - E (D74-16)` | Warna Kabel: GR - W-B — Sinyal switch pengapian | Switch pengapian OFF → ON: Di bawah 1 V → 10 sampai 14 V |
| `[ANTI PENCURIAN] LSR* (D74-6) - Bodi masa` | Warna Kabel: O* - Bodi masa — Sinyal switch deteksi unlock pintu bagasi. | Pintu bagasi LOCK → UNLOCK: 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] E (D74-16) - Bodi masa` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ANTI PENCURIAN] BRK+ (D74-24) - Bodi masa` | Warna Kabel: P - Masa bodi — Komunikasi Alarm BERKES | Sistem anti pencurian dalam status membunyikan alarm:: Pembangkitan pulsa (1.5 V ← → Di bawah 1.2 V) |
| `[ANTI PENCURIAN] BRK- (D74-25) - Bodi masa` | Warna Kabel: O - Masa bodi — Komunikasi Alarm BERKES | Semua pintu telah dikunci menggunakan kunci (Sistem anti pencurian dalam status persiapan siaga).: Pembangkitan pulsa (1.5 V ← → Di bawah 1.2 V) |
| `[ANTI PENCURIAN] SH- (D74-15) - Bodi masa` | Warna Kabel: O - Masa bodi — Horn keamanan | Horn kemanan sedang berbunyi (Sistem anti pencurian dalam status membunyikan alarm).: Pembangkitan pulsa (10 sampai 14 V ← → Di bawah 1 V) |
| `[ANTI PENCURIAN] +B1 (D74-11) - E (D74-16)` | Warna Kabel: B - W-B — Power supply +B | Selalu: 10 sampai 14 V |
| `[ANTI PENCURIAN] KSW (D74-7) - E (D74-16)` | Warna Kabel: Y - W-B — Input switch peringatan unlock kunci | Switch peringatan kunci unlock ON (Kunci telah dimasukkan) → OFF (Kunci dicabut dari silinder kunci pengapian): Di bawah 1 V → 10 sampai 14 V |
| `[ANTI PENCURIAN] IND (D74-29) - E (D74-16)` | Warna Kabel: G - W-B — Indikator keamanan | Lampu indikator keamanan menyala (menyala selama 30 detik dalam status membunyikan alarm. Lampu itu menyala ketika sistem immobiliser sedang bekerja).: 5 V atau lebih |
| `[ANTI PENCURIAN] DSWH (D74-4) - E (D74-16)` | Warna Kabel: W - W-B — Input switch courtesy kap mesin | Switch courtesy kap mesin OFF (Tertutup) → ON (Terbuka): 10 sampai 14 V → Di bawah 1 V |
| `[ANTI PENCURIAN] D74-11 (+B1) - Bodi masa` | Warna Kabel: B - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN] D74-13 (+B2) - Bodi masa` | Warna Kabel: BR - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN] D74-9 (IG) - D74-16 (E)` | Warna Kabel: GR - W-B — Sinyal switch pengapian | Switch pengapian OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[ANTI PENCURIAN] D74-6 (LSR) - Masa bod*` | Warna Kabel: BE - Masa bodi — Sinyal switch deteksi unlock pintu bagasi. | Pintu bagasi LOCK → UNLOCK: 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] D74-16 (E) - Bodi masa` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ANTI PENCURIAN] D74-24 (BRK+) - Masa bodi` | Warna Kabel: P - Masa bodi — Komunikasi Alarm BERKES | Sistem anti pencurian dalam status membunyikan alarm:: Pembangkitan pulsa (1.5 V ← → Di bawah 1.2 V) |
| `[ANTI PENCURIAN] D74-25 (BRK-) - Masa bodi` | Warna Kabel: BE - Masa bodi — Komunikasi Alarm BERKES | Semua pintu telah dikunci menggunakan kunci (Sistem anti pencurian dalam status persiapan siaga).: Pembangkitan pulsa (1.5 V ← → Di bawah 1.2 V) |
| `[ANTI PENCURIAN] D74-15 (SH-) - Masa bodi` | Warna Kabel: BE - Masa bodi — Horn keamanan | Horn kemanan sedang berbunyi (Sistem anti pencurian dalam status membunyikan alarm).: Pembangkitan pulsa (11 sampai 14 V ← → Di bawah 1 V) |
| `[ANTI PENCURIAN] D74-11 (+B1) - D74-16 (E)` | Warna Kabel: B - W-B — Power supply +B | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN] D74-7 (KSW) - D74-16 (E)` | Warna Kabel: Y - W-B — Input switch peringatan unlock kunci | Switch peringatan kunci unlock ON (Kunci telah dimasukkan) → OFF (Kunci dicabut dari silinder kunci pengapian): Di bawah 1 V → 11 sampai 14 V |
| `[ANTI PENCURIAN] D74-29 (IND) - D74-16 (E)` | Warna Kabel: G - W-B — Indikator keamanan | Lampu indikator keamanan menyala (menyala selama 30 detik dalam status membunyikan alarm. Lampu itu menyala ketika sistem immobiliser sedang bekerja).: 5 V atau lebih |
| `[ANTI PENCURIAN] D74-4 (DSWH) - D74-16 (E)` | Warna Kabel: W - W-B — Input switch courtesy kap mesin | Switch courtesy kap mesin OFF (Tertutup) → ON (Terbuka): 11 sampai 14 V → Di bawah 1 V |
| `[ENGINE IMMOBILISER] GND (D55-5) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] AGND (D55-8) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] VC5 (D55-14) - AGND (D55-8)` | Warna Kabel: P - BR — Power supply | Sistem engine immobiliser dalam kondisi set (kunci tidak di dalam kabin): Di bawah 1 V / Tekan switch pengapian*: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] CODE (D55-10) - AGND (D55-8)` | Warna Kabel: O - BR — Sinyal demodulasi dari data kode kunci | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch pengapian telah ditekan dan kunci dipegang dekat switch pengapian*: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] TXCT (D55-9) - AGND (D55-8)` | Warna Kabel: V - BR — Sinyal output kode kunci | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch pengapian telah ditekan dan kunci dipegang dekat switch pengapian*: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] E (D60-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] +B1 (D60-1) - E (D60-17)` | Warna Kabel: B - W-B — Power supply +B | Selalu: 10 sampai 14 V |
| `[ENGINE IMMOBILISER] IG (D60-18) - E (D60-17)` | Warna Kabel: BR - W-B — Power supply pengapian | Switch pengapian off: Di bawah 1 V |
| `[ENGINE IMMOBILISER] AGND (D60-40) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa switch pengapian | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] VC5 (D60-30) - AGND (D60-40)` | Warna Kabel: P - BR — Catu daya switch pengapian | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch pengapian telah ditekan*: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] CODE (D60-9) - AGND (D60-40)` | Warna Kabel: O - BR — KODE input switch pengapian | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch pengapian telah ditekan dan kunci dipegang dekat switch pengapian*: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] TXCT (D60-8) - AGND (D60-40)` | Warna Kabel: V - BR — Output TX dari switch pengapian | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch pengapian telah ditekan dan kunci dipegang dekat switch pengapian*: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] GND (D58-8) - Masa bodI` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] EGND (D58-7) - Masa body` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] +B (D58-1) - GND (D58-8)` | Warna Kabel: L - W-B — Power supply +B | Selalu: 10 sampai 14 V |
| `[ENGINE IMMOBILISER] EFII (D58-5) - EGND (D58-7)` | Warna Kabel: O - BR — Sinyal input ECM | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): Timbul pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] EFIO(D58-6) - EGND (D58-7)` | Warna Kabel: W - BR — Sinyal output ECM | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): Timbul pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] SGND (D56-2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] GND (D56-1) - Masa bod` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] B (D56-7) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[ENGINE IMMOBILISER] IG2 (D56-6) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply pengapian | Switch pengapian off: 0 V / Switch pengapian on (IG): 10 sampai 14 V |
| `[ENGINE IMMOBILISER] E1 (C20-104) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] E0M (A21-9) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] BATT (A21-20) - E1 (C20-104)` | Warna Kabel: Y - W — Baterai (untuk mengukur voltase baterai dan untuk memori ECM) | Selalu: 10 sampai 14 V |
| `[ENGINE IMMOBILISER] IGSW (A21-28) - E1 (C20-104)` | Warna Kabel: R - W — Switch pengapian | Switch pengapian on (IG): 10 sampai 14 V |
| `[ENGINE IMMOBILISER] +B (A21-2) - E1 (C20-104)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 10 sampai 14 V |
| `[ENGINE IMMOBILISER] +B2 (A21-1) - E1 (C20-104)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 10 sampai 14 V |
| `[ENGINE IMMOBILISER] IMI (A21-11) - E1 (C20-104)` | Warna Kabel: W - BR — Sinyal input ID kode box | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] IMO (A21-10) - E1 (C20-104)` | Warna Kabel: O - BR — Sinyal output ID kode box | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] GND1 (4E-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] GND2 (D65-4) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] AM1 (D65-1) - Masa bodi` | Warna Kabel: O - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[ENGINE IMMOBILISER] AM2 (D64-6) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[ENGINE IMMOBILISER] SSW1 (D65-10) - Masa bodi` | Warna Kabel: R - Masa bodi — Switch pengapian | Switch pengapian off: 10 kΩ atau lebih tinggi / Switch pengapian on (IG): Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] SSW2 (D65-9) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch pengapian | Switch pengapian off: 10 kΩ atau lebih tinggi / Switch pengapian on (IG): Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] BECU (4B-30) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[ENGINE IMMOBILISER] LIN1 (4D-9) - Masa bodi` | Warna Kabel: P - Masa bodi — Alur komunikasi LIN | Selalu: 10 kΩ atau lebih tinggi |
| `[ENGINE IMMOBILISER] D24-7 (AGND) - Masa bodi` | Warna Kabel: GR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D24-1 (VC5) - D24-7 (AGND)` | Warna Kabel: P- GR — Power source | Tidak terdapat kunci dalam silinder kunci pengapian: Di bawah 1 V / Kunci di dalam silinder kunci pengapian: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] D24-4 (CODE) - D24-7 (AGND)` | Warna Kabel: G- GR — Sinyal demodulasi dari data kode kunci | Tidak terdapat kunci dalam silinder kunci pengapian: Di bawah 1 V / Kunci di dalam silinder kunci pengapian: Bentuk gelombang 1 |
| `[ENGINE IMMOBILISER] D24-5 (TXCT) - D24-7 (AGND)` | Warna Kabel: V- GR — Sinyal output kode kunci | Tidak terdapat kunci dalam silinder kunci pengapian: Di bawah 1 V / Kunci di dalam silinder kunci pengapian: Bentuk gelombang 2 |
| `[ENGINE IMMOBILISER] D23-16 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D23-1 (+B) - D23-16 (GND)` | Warna Kabel: L - W-B — Baterai | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D23-2 (IG) - D23-16 (GND)` | Warna Kabel: R - W-B — Sinyal switch pengapian | Switch pengapian off: Di bawah 1 V / Switch pengapian ON: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D23-3 (KSW) - D23-16 (GND)` | Warna Kabel: O - W-B — Sinyal switch peringatan unlock | Tidak terdapat kunci dalam silinder kunci pengapian: 10 kΩ atau lebih tinggi / Kunci di dalam silinder kunci pengapian: Di bawah 1 Ω / Tidak terdapat kunci dalam silinder kunci pengapian: 11 sampai 14 V / Kunci di dalam  |
| `[ENGINE IMMOBILISER] D23-5 (AGND) - Masa bodi` | Warna Kabel: GR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D23-14 (VC5) - D23-5 (AGND)` | Warna Kabel: P- GR — Power source | Tidak terdapat kunci dalam silinder kunci pengapian: Di bawah 1 V / Kunci di dalam silinder kunci pengapian: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] D23-4 (TXCT) - D23-5 (AGND)` | Warna Kabel: V- GR — Sinyal komunikasi transponder kunci amplifier | Tidak terdapat kunci dalam silinder kunci pengapian: Di bawah 1 V / Kunci di dalam silinder kunci pengapian: Bentuk gelombang 1 |
| `[ENGINE IMMOBILISER] D23-15 (CODE) - D23-5 (AGND)` | Warna Kabel: G- GR — Sinyal komunikasi transponder kunci amplifier | Tidak terdapat kunci dalam silinder kunci pengapian: Di bawah 1 V / Kunci di dalam silinder kunci pengapian: Bentuk gelombang 2 |
| `[ENGINE IMMOBILISER] D23-13 (EFIO) - D23-16 (GND)` | Warna Kabel: W - W-B — Sinyal output ECM | Switch pengapian off: Di bawah 1 V / Switch pengapian ON: Bentuk gelombang 3 |
| `[ENGINE IMMOBILISER] D23-12 (EFII) - D23-16 (GND)` | Warna Kabel: O - W-B — Sinyal input ECM | Switch pengapian off: Di bawah 1 V / Switch pengapian ON: Bentuk gelombang 4 |
| `[ENGINE IMMOBILISER] D23-9 (D) - D23-16 (GND)` | Warna Kabel: W - W-B — Komunikasi tester diagnostik | Tanpa komunikasi: Di bawah 1 V / Selama komunikasi: Pembangkitan pulsa |
| `[ENGINE IMMOBILISER] D23-7 (CTY) - D23-16 (GND)` | Warna Kabel: B - W-B — Sinyal courtesy pintu | Switch ditekan: 11 sampai 14 V / Switch bebas: Di bawah 1 V |
| `[ENGINE IMMOBILISER] D23-8 (IND) - D23-16 (GND)` | Warna Kabel: LG - W-B — Sinyal indikator keamanan | Lampu indikator keamanan menyala: 11 sampai 14 V / Lampu indikator keamanan padam: Di bawah 1 V |
| `[ENGINE IMMOBILISER] C20-104 (E1) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] A21-11 (IMI) - C20-104 (E1)` | Warna Kabel: W - W — Sinyal input ECU kunci transponder | Switch pengapian off: Di bawah 1 V / Switch pengapian ON: Bentuk gelombang 1 |
| `[ENGINE IMMOBILISER] A21-10 (IMO) - C20-104 (E1)` | Warna Kabel: O - W — Sinyal output transponder kunci ECU | Switch pengapian off: Di bawah 1 V / Switch pengapian ON: Bentuk gelombang 2 |
| `[PENERANGAN] ECUB (4B-30) - GND1 (4E-17)` | Warna Kabel: L - W-B — Baterai (Power supply) | Selalu: 10 sampai 14 V |
| `[PENERANGAN] GND1 (4E-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[PENERANGAN] GND2 (D65-4)* - Masa Bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[PENERANGAN] DCTY (4A-21) - Masa bodi` | Warna Kabel: R - Masa bodi — Input switch courtesy pintu pengemudi | Pintu pengemudi ditutup: 10 sampai 14 V / Pintu pengemudi terbuka: 0 V |
| `[PENERANGAN] PCTY (4A-24) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch input courtesy pintu penumpang depan | Pintu penumpang tertutup: 10 sampai 14 V / Pintu penumpang terbuka: 0 V |
| `[PENERANGAN] RRCY (4A-20) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch input courtesy pintu belakang RH | Pintu belakang RH tertutup: 10 sampai 14 V / Pintu belakang RH terbuka: 0 V |
| `[PENERANGAN] RRCY (4A-5) - Masa bodi` | Warna Kabel: G - Masa bodi — Switch input courtesy pintu belakang LH | Pintu belakang LH tertutup: 10 sampai 14 V / Pintu belakang LH terbuka: 0 V |
| `[PENERANGAN] BCTY (4A-7) - Masa Bodi` | Warna Kabel: SB - Masa bodi — Switch input courtesy pintu bagasi | Pintu bagasi ditutup: 10 sampai 14 V / Pintu bagasi terbuka: 0 V |
| `[PENERANGAN] SWIL (D65-8)* - GND2 (D65-4)*` | Warna Kabel: LG* - W-B* — Sinyal Illuminasi (ke iluminasi switch pengapian) | Switch kontrol lampu TAIL atau HEAD: 10 sampai 14 V / Switch kontrol lampu OFF: 0 V |
| `[DOOR LOCK] ECUB (4B-30) - GND1 (4E-17)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] GND1 (4E-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] KSW (4D-7) - GND1 (4E-17)` | Warna Kabel: Y - W-B — Input switch peringatan unlock kunci | Kunci telah disisipkan: 10 sampai 14 V / Tidak terdapat kunci dalam silinder kunci pengapian: 0 V |
| `[DOOR LOCK] DCTY (4A-21) - Masa bodi` | Warna Kabel: R - Masa bodi — Input switch courtesy pintu sisi pengemudi | Pintu sisi pengemudi tertutup: 10 sampai 14 V / Pintu samping pengemudi terbuka: 0 V |
| `[DOOR LOCK] PCTY (4A-24) - Masa bodi` | Warna Kabel: L - Masa bodi — Input switch courtesy pintu sisi penumpang | Pintu sisi penumpang tertutup: 10 sampai 14 V / Pintu samping penumpang terbuka: 0 V |
| `[DOOR LOCK] RRCY (4A-20) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch input courtesy pintu belakang RH | Pintu belakang RH tertutup: 10 sampai 14 V / Pintu belakang RH terbuka: 0 V |
| `[DOOR LOCK] RRCY (4A-5) - Masa bodi` | Warna Kabel: G - Masa bodi — Switch input courtesy pintu belakang LH | Pintu belakang LH tertutup: 10 sampai 14 V / Pintu belakang LH terbuka: 0 V |
| `[DOOR LOCK] BCTY (4A-7) - Masa Bodi` | Warna Kabel: SB - Masa bodi — Switch input courtesy pintu bagasi | Pintu bagasi tertutup: 10 sampai 14 V / Pintu bagasi terbuka: 0 V |
| `[DOOR LOCK] L1 (4H-4) - Masa bodi` | Warna Kabel: LG - Masa bodi — Input lock switch kontrol pintu | Switch kontrol pintu OFF: 10 sampai 14 V / Switch kontrol pintu ON (LOCK): 0 V |
| `[DOOR LOCK] UL1 (4H-5) - Masa bodi` | Warna Kabel: O - Masa bodi — Input unlock switch kontrol pintu | Switch kontrol pintu OFF: 10 sampai 14 V / Switch kontrol pintu ON (UNLOCK): 0 V |
| `[DOOR LOCK] ACT+ (4H-8) - Masa bodi` | Warna Kabel: O - Masa bodi — Output penggerak LOCK motor door lock sisi pengemudi | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF: 0 V / Switch kontrol pintu atau silinder kunci pintu sisi pengemudi ON (LOCK): 10 sampai 14 V → 0 V |
| `[DOOR LOCK] ACT+ (4H-17) - Masa bodi` | Warna Kabel: W - Masa bodi — Output penggerak LOCK motor door lock sisi penumpang | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF: 0 V / Switch kontrol pintu atau silinder kunci pintu sisi pengemudi ON (LOCK): 10 sampai 14 V → 0 V |
| `[DOOR LOCK] ACT+ (4A-3) - Masa bodi` | Warna Kabel: GR - Masa bodi — Output pengggerak LOCK motor door lock belakang | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF: 0 V / Switch kontrol pintu atau silinder kunci pintu sisi pengemudi ON (LOCK): 10 sampai 14 V → 0 V |
| `[DOOR LOCK] ACT- (4H-18) - Masa bodi` | Warna Kabel: P - Masa bodi — Output penggerak UNLOCK motor door lock sisi pengemudi | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF: 0 V / Switch kontrol pintu atau silinder kunci pintu sisi pengemudi ON (UNLOCK): 10 sampai 14 V → 0 V |
| `[DOOR LOCK] ACT- (4H-9) - Masa bodi` | Warna Kabel: SB - Masa bodi — Output penggerak UNLOCK motor door lock sisi penumpang | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF: 0 V / Switch kontrol pintu atau silinder kunci pintu sisi pengemudi ON (UNLOCK): 10 sampai 14 V → 0 V |
| `[DOOR LOCK] ACT- (4A-4) - Masa bodi` | Warna Kabel: P - Masa bodi — Output pengggerak UNLOCK motor door lock belakang | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF: 0 V / Switch kontrol pintu atau silinder kunci pintu sisi pengemudi ON (LOCK): 10 sampai 14 V → 0 V |
| `[DOOR LOCK] LSWD (D64-25) - Masa bodi*1` | Warna Kabel: L - Masa bodi — Input switch posisi lock pintu sisi pengemudi | Pintu sisi pengemudi UNLOCK: 0 V / Pintu sisi pengemudi LOCK: 10 sampai 14 V |
| `[DOOR LOCK] LSWD (D33-21) - Masa bodi*2` | Warna Kabel: L - Masa bodi — Input switch posisi lock pintu sisi pengemudi | Pintu sisi pengemudi UNLOCK: 0 V / Pintu sisi pengemudi LOCK: 10 sampai 14 V |
| `[DOOR LOCK] LSWP (D64-10) - Masa bodi*1*3` | Warna Kabel: L - Masa bodi — Input switch posisi lock pintu sisi penumpang | Pintu sisi penumpang UNLOCK: 0 V / Pintu sisi penumpang LOCK: 10 sampai 14 V |
| `[DOOR LOCK] LSWP (D33-5) - Masa bodi*2*3` | Warna Kabel: L - Masa bodi — Input switch posisi lock pintu sisi penumpang | Pintu sisi penumpang UNLOCK: 0 V / Pintu sisi penumpang LOCK: 10 sampai 14 V |
| `[DOOR LOCK] L2 (4H-7) - Masa bodi` | Warna Kabel: BR - Masa bodi — Input key-linked switch pintu sisi pengemudi | Silinder kunci pintu sisi pengemudi OFF: 10 sampai 14 V / Silinder kunci pintu sisi pengemudi ON (UNLOCK): 0 V |
| `[DOOR LOCK] L2 (4H-16) - Masa bodi*2*3` | Warna Kabel: B - Masa bodi — Input key-linked switch pintu sisi penumpang | Silinder kunci pintu sisi penumpang OFF: 10 sampai 14 V / Silinder kunci pintu sisi penumpang ON (UNLOCK): 0 V |
| `[DOOR LOCK] UL2 (4H-6) - Masa bodi` | Warna Kabel: G - Masa bodi — Input key-linked switch pintu sisi pengemudi | Silinder kunci pintu sisi pengemudi OFF: 10 sampai 14 V / Silinder kunci pintu sisi pengemudi ON (UNLOCK): 0 V |
| `[DOOR LOCK] UL2 (4H-15) - Masa bodi*2*3` | Warna Kabel: Y - Masa bodi — Input key-linked switch pintu sisi penumpang | Silinder kunci pintu sisi penumpang OFF: 10 sampai 14 V / Silinder kunci pintu sisi penumpang ON (UNLOCK): 0 V |
| `[DOOR LOCK] HAZ (4S-17) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal lampu peringatan hazard | Answer-back ON: Pembangkitan pulsa / Answer-back OFF: 10 sampai 14 V |
| `[DOOR LOCK] +B1 (D60-1) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply +B | Selalu: 9 sampai 14 V |
| `[DOOR LOCK] IG (D60-18) - Masa bodi` | Warna Kabel: BR - Masa bodi — Power supply pengapian | Switch pengapian on (IG): 9 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[DOOR LOCK] LIN (D60-10) - Masa bodi` | Warna Kabel: P - Masa bodi — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] E (D60-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] RSSI (D60-39) - Masa bodi` | Warna Kabel: W - Masa bodi — Output receiver kontrol pintu. | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: 10 sampai 14 V → Di bawah 1 V |
| `[DOOR LOCK] RDA (D60-38) - Masa bodi` | Warna Kabel: R - Masa bodi — Input receiver kontrol pintu | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: Di bawah 1 V → 10 sampai 14 V → Di bawah 1 V |
| `[DOOR LOCK] RCO (D60-29) - Masa bodi` | Warna Kabel: L - Masa bodi — Input receiver kontrol pintu | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: 5 sampai 0V → 5 V |
| `[DOOR LOCK] GND (J13-1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] RSSI (J13-2) - Masa bodi` | Warna Kabel: W - Masa bodi — Output receiver kontrol pintu. | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: 11 sampai 14 V → Di bawah 1 V |
| `[DOOR LOCK] DATA (J13-5) - Masa bodi` | Warna Kabel: R - Masa bodi — Input receiver kontrol pintu | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: Di bawah 1 V → 11 sampai 14 V → Di bawah 1 V |
| `[DOOR LOCK] +5 (J13-4) - Masa bodi` | Warna Kabel: L - Masa bodi — Input receiver kontrol pintu | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: 5 sampai 0V → 5 V |
| `[DOOR LOCK] PRG (D33-17) - Masa bodi` | Warna Kabel: W - Masa bodi — Output receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): 6 sampai 7 V → Di bawah 1 V → 6 sampai 7 V |
| `[DOOR LOCK] RDA (D33-16) - Masa bodi` | Warna Kabel: R - Masa bodi — Input receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): Di bawah 1 V → 6 sampai 7 V → Di bawah 1 V |
| `[DOOR LOCK] +B (J13-5) - GND (J13-1)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] PRG (J13-3) - Masa bodi` | Warna Kabel: W - Masa bodi — Output receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): 6 sampai 7 V → Di bawah 1 V → 6 sampai 7 V |
| `[DOOR LOCK] RDA (J13-2) - Masa bodi` | Warna Kabel: R - Masa bodi — Input receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): Di bawah 1 V → 6 sampai 7 V → Di bawah 1 V |
| `[DOOR LOCK] +B (D60-1) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] TSW1 (D60-3) - E (D60-17)` | Warna Kabel: W - W-B — Sinyal switch lock handel pintu luar (sisi pengemudi) | Switch dibebaskan.: 10 kΩ atau lebih tinggi / Switch ditekan ke dalam: Di bawah 1 Ω |
| `[DOOR LOCK] TSW5 (D60-7) - E (D60-17)` | Warna Kabel: BR - W-B — Sinyal switch unlock handel luar pintu bagasi | Switch dibebaskan.: 10 kΩ atau lebih tinggi / Switch ditekan ke dalam: Di bawah 1 Ω |
| `[DOOR LOCK] LIN (D60-10) - E (D60-17)` | Warna Kabel: P - W-B — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] CLG1 (D60-33) - CG1B (D60-34)` | Warna Kabel: GR - P — Oscillator Kunci Elektrik Pintu (sisi pengemudi) sinyal sensor | Semua pintu tertutup, semua pintu terkunci dan switch pengapian off: Alternator antara 5 V dan di bawah 1 V / Pintu tidak dikunci atau pintu terbuka: Di bawah 1 V |
| `[DOOR LOCK] SEN1 (D60-22) - E (D60-17)` | Warna Kabel: R - W-B — Sentuh sinyal deteksi sensor | Menyentuh handel pintu sisi luar: 10 sampai 14 V / Handel pintu luar tidak disentuh: Di bawah 1 V |
| `[DOOR LOCK] SEL1 (D60-5) - E (D60-17)` | Warna Kabel: R - W-B — Sinyal sentuh mengaktifkan sinyal kontrol | Kunci minimal 3 m (9.8 ft.) jauhnya dari pintu: 10 sampai 14 V / Kunci dekat ke pintu: Di bawah 1 V |
| `[DOOR LOCK] CLG5 (D60-11) - CG5B (D60-12)` | Warna Kabel: LG - G — Oscillator Kunci Elektrik Indoor (depan) sinyal sensor | 30 detik setelah pintu pengemudi dibuka dan ditutup, switch pengapian off: Alternator antara 5 V dan di bawah 1 V / Dalam 30 detik pintu pengemudi dibuka dan ditutup, switch pengapian off: Di bawah 1 V |
| `[DOOR LOCK] CLG7 (D60-15) - CG7B (D60-16)` | Warna Kabel: V - P — Oscillator Kunci Elektrik Indoor (belakang) sinyal sensor | 30 detik setelah pintu pengemudi dibuka dan ditutup, switch pengapian off: Alternator antara 5 V dan di bawah 1 V / Dalam 30 detik pintu pengemudi dibuka dan ditutup, switch pengapian off: Di bawah 1 V |
| `[DOOR LOCK] CLG8 (D60-31) - CG8B (D60-32)` | Warna Kabel: LG - SB — Sinyal sensor oscillator kunci elektronik pintu (pintu bagasi) | Switch unlock pintu bagasi OFF: Alternator antara 5 V dan di bawah 1 V / Switch unlock pintu bagasi ON: Di bawah 1 V |
| `[DOOR LOCK] RC0 (D60-29) - E (D60-17)` | Warna Kabel: L - W-B — Power source receiver kontrol pintu | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: 5 sampai 0V → 5 V |
| `[DOOR LOCK] RSSI (D60-39) - E (D60-17)` | Warna Kabel: W - W-B — Sinyal keberadaan gelombang elektrik receiver kontrol pintu | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: Di bawah 1 V → 10 sampai 14 V → Di bawah 1 V |
| `[DOOR LOCK] RDA (D60-38) - E (D60-17)` | Warna Kabel: R - W-B — Sinyal input data receiver kontrol pintu | Switch pengapian off, semua pintu ditutup dan switch transmitter tidak ditekan → ditekan: 10 sampai 14 V → Di bawah 1 V |
| `[DOOR LOCK] +B (R2-1) - GND (R2-7)` | Warna Kabel: Y - BR — Power supply +B | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] GND (R2-7) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] CLG (R2-10) - GND (R2-7)` | Warna Kabel: R - BR — Oscillator Kunci Elektrik Pintu (sisi pengemudi) sinyal sensor | Semua pintu tertutup, semua pintu terkunci dan switch pengapian off: Alternator antara 5 V dan di bawah 1 V / Pintu tidak dikunci atau pintu terbuka: Di bawah 1 V |
| `[DOOR LOCK] SEL (R2-4) - GND (R2-7)` | Warna Kabel: O - BR — Sinyal sentuh mengaktifkan sinyal kontrol | Kunci minimal 3 m (9.8 ft.) jauhnya dari pintu: 10 sampai 14 V / Kunci dekat ke pintu: Di bawah 1 V |
| `[DOOR LOCK] SENS (R2-6) - GND (R2-7)` | Warna Kabel: V - BR — Sentuh sinyal deteksi sensor | Menyentuh handel pintu sisi luar: 10 sampai 14 V / Handel pintu luar tidak disentuh: Di bawah 1 V |
| `[DOOR LOCK] CLG5 (J37-1) - CLGB (J37-2)` | Warna Kabel: LG - SB — Sinyal sensor oscillator kunci elektronik pintu (pintu bagasi) | Switch unlock pintu bagasi OFF: Alternator antara 5 V dan di bawah 1 V / Switch unlock pintu bagasi ON: Di bawah 1 V |
| `[DOOR LOCK] ECUB (4B-30) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] AM1 (D65-1) - Masa bodi` | Warna Kabel: O - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] AM2 (D64-6) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply +B | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] TR+ (D64-1) - Masa bodi` | Warna Kabel: O - Masa bodi — Sinyal pintu bagasi | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] IG (4S-7) - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal IG2 | Switch pengapian on (IG): 10 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[DOOR LOCK] ACC (4S-6) - Masa bodi` | Warna Kabel: GR - Masa bodi — Sinyal ACC | Switch pengapian on (ACC): 10 sampai 14 V |
| `[DOOR LOCK] GND2 (D65-4) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] CANH (D66-15) - Masa bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] CANL (D66-16) - Masa bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] LIN1 (4D-9) - Masa bodi` | Warna Kabel: P - Masa bodi — Alur komunikasi LIN | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] BDSU(D64-12) - Masa bodi` | Warna Kabel: Y - Masa bodi — Sinyal switch lock handel luar pintu bagasi | Switch dibebaskan.: 10 kΩ atau lebih tinggi / Switch ditekan ke dalam: Di bawah 1 Ω |
| `[DOOR LOCK] IG2 (D1-1) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal switch pengapian | Switch pengapian OFF → ON: Di bawah 1 V → 10 sampai 14 V |
| `[DOOR LOCK] ECUB (D1-2) - Masa Bodi` | Warna Kabel: L - Masa bodi — Baterai | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] CANH (D1-20) - Masa Bodi` | Warna Kabel: G - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[DOOR LOCK] CANL (D1-21) - Masa Bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[DOOR LOCK] ET (D1-24) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] KSW (4D-7) - Masa Bodi` | Warna Kabel: Y - Masa bodi — Input switch peringatan unlock kunci | Kunci telah dimasukkan Kunci dicabut dari silinder kunci pengapian.: Di bawah 1 V → 10 sampai 14V |
| `[DOOR LOCK] ECUB (4B-30) - Masa bodi` | Warna Kabel: L - Masa bodi — Baterai | Selalu: 10 sampai 14 V |
| `[DOOR LOCK] DTCY (4A-21) - Masa Bodi` | Warna Kabel: R - Masa bodi — Input switch courtesy pintu pengemudi | Pintu pengemudi ditutup → dibuka: 10 sampai 14 V → Di bawah 1 V |
| `[DOOR LOCK] CANL (D33-22) - Masa Bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[DOOR LOCK] CANH (D33-23) - Masa bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[METER] D1-1 (IG2) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal switch pengapian | Switch pengapian off → on (IG): Di bawah 1 V → 11 sampai 14 V |
| `[METER] D1-2 (ECU-B) - Masa bodi` | Warna Kabel: L - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[METER] D1-24 (ET) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER] D1-3 (L) - Masa bodi` | Warna Kabel: V - Masa bodi — Sinyal permukaan bahan bakar | Switch pengapian on (IG): 12 sampai 415 Ω |
| `[METER] D1-14 (ILL+) - Masa bodi` | Warna Kabel: G - Masa bodi — Sinyal Taillight | Switch kontrol lampu OFF→ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] D1-16 (+S) - Masa bodi` | Warna Kabel: SB - Masa bodi — Sinyal kecepatan (Output) | Kira-kira pada pengendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[METER] D1-17 (SI) - Masa bodi` | Warna Kabel: P - Masa bodi — Sinyal kecepatan (Input) | Kira-kira pada pengendaraan 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[METER] D1-20 (CANH) - Masa bodi` | Warna Kabel: G - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] D1-21 (CANL) - Masa bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] D2-1 (CHG-) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal lampu peringatan pengisian | Hidupkan mesin Lampu peringatan pengisian ON→OFF: Di bawah 1 V → 11 sampai 14 V |
| `[METER] D2-2 (SW) - Masa bodi` | Warna Kabel: V - Masa bodi — Sinyal lampu peringatan level minyak rem | Switch pengapian on (IG) Lampu peringatan level minyak rem ON→OFF: Di bawah 1 V → 11 sampai 14 V |
| `[METER] D2-4 (EFI) - Masa bodi` | Warna Kabel: B - Masa bodi — Periksa sinyal lampu peringatan mesin | Periksa sinyal lampu peringatan mesin ON→OFF: Di bawah 2 V → 11 sampai 14 V |
| `[METER] D2-6 (S)*1 - Masa bodi` | Warna Kabel: SB - Masa bodi — Sinyal kabut belakang | Switch pengapian on (IG) Switch lampu kabut OFF→ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] D2-7 (FOG)*2 - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal kabut depan | Switch pengapian on (IG) Switch lampu kabut depan OFF→ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] D2-8 (B) - Masa bodi` | Warna Kabel: LG - Masa bodi — Sinyal tanda belok LH | Switch pengapian on (IG) Lampu indikator tanda belok LH OFF→ON→OFF: Di bawah 1 V → 11 sampai 14 V → Di bawah 1 V |
| `[METER] D2-11 (BEAM-) - Masa bodi` | Warna Kabel: P - Masa bodi — Sinyal indikator HI-BEAM (-) | Switch dimmer OFF→ON: Di bawah 1 V |
| `[METER] D2-12 (OIL P) - Masa bodi` | Warna Kabel: Y - Masa bodi — Sinyal tekanan oli mesin | Lampu peringatan tekanan oli mesin ON→OFF: Di bawah 1 V → 11 sampai 14 V |
| `[METER] D2-14 (BEAM+) - Masa bodi` | Warna Kabel: GR - Masa bodi — Sinyal indikator HI-BEAM (+) | Selalu: 11 sampai 14 V |
| `[METER] D2-15 (B) - Masa bodi` | Warna Kabel: BR - Masa bodi — Sinyal tanda belok RH | Switch pengapian on (IG) Lampu indikator tanda belok RH OFF→ON→OFF: Di bawah 1 V → 11 sampai 14 V → Di bawah 1 V |
| `[METER] D2-16 (IND) - Masa bodi` | Warna Kabel: G - Masa bodi — Sinyal indikator taillight | Switch kontrol lampu OFF→ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] 4A-5 (RRCY) - 4E-17 (GND1)` | Warna Kabel: G - W-B — Sinyal switch courtesy pintu belakang (LH) | Pintu Belakang (LH) TUTUP→ BUKA: 11 sampai 14 V → Di bawah 1 V / Pintu belakang (LH) TUTUP→ BUKA: 11 sampai 14 V → Di bawah 1 V |
| `[METER] 4A-7 (BCTY) - 4E-17 (GND1)` | Warna Kabel: SB - W-B — Sinyal switch courtesy pintu bagasi | Pintu bagasi TUTUP→ BUKA: 11 sampai 14 V → Di bawah 1 V |
| `[METER] 4A-20 (RRCY) - 4E-17 (GND1)` | Warna Kabel: L - W-B — Sinyal switch courtesy pintu belakang (RH) | Pintu belakang (RH) TUTUP→ BUKA: 11 sampai 14 V → Di bawah 1 V / Pintu belakang (RH) TUTUP →BUKA: 11 sampai 14 V → Di bawah 1 V |
| `[METER] 4A-21 (DCTY) - 4E-17 (GND1)` | Warna Kabel: R - W-B — Sinyal switch courtesy pintu depan (Sisi pengemudi) | Pintu depan (Sisi Pengemudi) TUTUP→ BUKA: 11 sampai 14 V → Di bawah 1 V / Pintu depan (Sisi pengemudi) TUTUP →BUKA: 11 sampai 14 V → Di bawah 1 V |
| `[METER] 4A-24 (PCTY) - 4E-17 (GND1)` | Warna Kabel: L - W-B — Sinyal switch courtesy pintu depan (Sisi Penumpang) | Pintu depan (Sisi Penumpang) TUTUP→BUKA: 11 sampai 14 V → Di bawah 1 V |
| `[METER] 4C-2 (PKB) - 4E-17 (GND1)` | Warna Kabel: Y - W-B — Sinyal rem parkir | Lampu peringatan rem parkir ON→OFF: 11 sampai 14 V → Di bawah 1 V |
| `[METER] 4D-7 (KSW) -4E-17 (GND1)` | Warna Kabel: Y - W-B — Input switch peringatan unlock kunci | Kunci dimasukkan→Dicabut: 11 sampai 14 V → Di bawah 1 V |
| `[METER] 4E-17 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER] D64-26 (DBKL) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal kondisi seat belt (Sisi pengemudi) | Lampu peringatan seat belt pengemudi OFF→ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] D66-15 (CANH) - Masa bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] D66-16 (CANL) - Masa bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] D33-9 (DBKL) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal kondisi seat belt (Sisi pengemudi) | Lampu peringatan seat belt pengemudi OFF→ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] D33-22 (CANL) - Masa Bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] D33-23 (CANH)- Masa Bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[AUDIO / VISUAL] D10-7 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[AUDIO / VISUAL] D10-3 (ACC) - D10-7 (GND)` | Warna Kabel: GR - W-B — Power supply ACC | Switch Pengapian ACC: 11 sampai 14 V |
| `[AUDIO / VISUAL] D10-4 (B) - D10-7 (GND)` | Warna Kabel: L - W-B — Power supply baterai | Selalu: 11 sampai 14 V |
| `[AUDIO / VISUAL] D10-1 (FR+) - D10-7 (GND)` | Warna Kabel: GR - W-B — Sinyal suara (kanan depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-2 (FL+) - D10-7 (GND)` | Warna Kabel: P - W-B — Sinyal suara (kiri depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-5 (FR-) D10-7 - (GND)` | Warna Kabel: Y - W-B — Sinyal suara (kanan depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-6 (FL-) - D10-7 (GND)` | Warna Kabel: V - W-B — Sinyal suara (kiri depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D11-1 (RR+) - D10-7 (GND)` | Warna Kabel: R - W-B — Sinyal suara (kanan belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D11-2 (RL+) - D10-7 (GND)` | Warna Kabel: B - W-B — Sinyal suara (kiri belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D11-3 (RR-) - D10-7 (GND)` | Warna Kabel: W - W-B — Sinyal suara (kanan belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D11-6 (RL-) - D10-7 (GND)` | Warna Kabel: Y - W-B — Sinyal suara (kiri belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-8 (ANT) - D10-7 (GND)` | Warna Kabel: B - W-B — Power source antena | Switch radio ON (AM atau FM): 11 sampai 14 V |
| `[AUDIO / VISUAL] D53-6 (SWG) - Masa bodi*1` | Warna Kabel: LG - Masa bodi — Masa switch steering pad | Selalu: Di bawah 1 V |
| `[AUDIO / VISUAL] D53-7 (SW1) - D53-6 (SWG)*1` | Warna Kabel: P - LG — Sinyal switch steering pad | Switch steering pad tidak ditekan: 4 V atau lebih tinggi / Switch SEEK+ pada steering pad ditekan: Sekitar 0.1 V / Switch SEEK- pada steering pad ditekan: Sekitar 0.9 V / Switch VOL+ pada steering pad ditekan: Sekitar 1. |
| `[AUDIO / VISUAL] D53-8 (SW2) - D53-6 (SWG)*1` | Warna Kabel: BE - LG — Sinyal switch steering pad | Switch steering pad tidak ditekan: 4 V atau lebih tinggi / Switch MODE pada steering pad ditekan: Di bawah 1 V |
| `[AUDIO / VISUAL] D53-15 (ARI) - D10-7 (GND)*2` | Warna Kabel: R - W-B — Sinyal suara (Kanan) | Peralatan eksternal sedang dimainkan (Bila stereo jack digunakan): Bentuk gelombang disinkronkan dengan suara yang di-output |
| `[AUDIO / VISUAL] D53-16 (ASGN) - Masa bodi*2` | Warna Kabel: B - Masa bodi — Masa stereo jack adapter | Selalu: Di bawah 1 V |
| `[AUDIO / VISUAL] D53-17 (ALI) - D10-7 (GND)*2` | Warna Kabel: W - W-B — Sinyal suara (Kiri) | Peralatan eksternal sedang dimainkan (Bila stereo jack digunakan): Bentuk gelombang disinkronkan dengan suara yang di-output |
| `[AUDIO / VISUAL] D53-18 (AGND) - Masa bodi*2` | Warna Kabel: Pelindung - Masa bodi — Masa Pelindung | Selalu: Di bawah 1 V |
| `[AUDIO / VISUAL] D53-19 (AUXI) - D10-7 (GND)*2` | Warna Kabel: R - W-B — Sinyal deteksi hubungan peralatan eksternal | Peralatan eksternal dihubungkan: Di bawah 1 V |
| `[KACA DEPAN / KACA JENDELA] E (F8-1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] +B (F8-2) - E (F8-1)` | Warna Kabel: LG - W-B — Power supply baterai | Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] U (F8-10) - E (F8-1)` | Warna Kabel: R - W-B — Motor power window pintu sisi pengemudi UP | Switch pengapian on (IG), switch power window sisi pengemudi OFF → UP (pengoperasian manual) → power window sisi pengemudi ditutup sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] D (F8-7) - E (F8-1)` | Warna Kabel: G - W-B — Motor power window pintu sisi pengemudi DOWN | Switch pengapian on (IG), switch power window sisi pengemudi OFF → DOWN (pengoperasian manual) → power window sisi pengemudi terbuka sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] LED (F8-5) - E (F8-1)` | Warna Kabel: W - W-B — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] E (F7-9) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] B (F7-6) - Masa bodi` | Warna Kabel: GR - Masa bodi — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[KACA DEPAN / KACA JENDELA] U (F7-1) - E (F7-9)` | Warna Kabel: R - W-B — Output motor power window pintu sisi pengemudi UP | Switch pengapian on (IG), switch power window sisi pengemudi OFF: 11 sampai 14 V / Switch pengapian on (IG), switch power window sisi pengemudi OFF → UP (pengoperasian manual) → power window sisi pengemudi ditutup sepenu |
| `[KACA DEPAN / KACA JENDELA] D (F7-5) - E (F7-9)` | Warna Kabel: G - W-B — Output motor power window pintu sisi pengemudi DOWN | Switch pengapian on (IG), switch power window sisi pengemudi OFF → DOWN (pengoperasian manual) → power window sisi pengemudi terbuka sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V / Switch pengapian on (IG),  |
| `[KACA DEPAN / KACA JENDELA] B (G7-3) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply pengapian | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] U (G7-4) - Masa bodi` | Warna Kabel: R - Masa bodi — Output motor power window pintu sisi penumpang UP | Switch pengapian on (IG), switch power window OFF → UP: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] D (G7-1) - Bodi masa` | Warna Kabel: G - Masa bodi — Output motor power window pintu sisi penumpang DOWN | Switch pengapian on (IG), switch power window OFF → DOWN: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] SU (G7-5) - Masa bodi` | Warna Kabel: W - Masa bodi — Input motor power window UP (Remote) | Switch pengapian on (IG), switch utama power window OFF → UP (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] SD (G7-2) - Masa bodi` | Warna Kabel: P - Masa bodi — Input motor power window DOWN (Remote) | Switch pengapian on (IG), switch utama power window OFF → DOWN (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] B (3) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply pengapian | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] U (4) - Masa bodi` | Warna Kabel: Y - Masa bodi — Output UP motor power window | Switch pengapian on (IG), switch power window OFF → UP: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] D (2) - Masa bodi` | Warna Kabel: B - Masa bodi — Output DOWN motor power window | Switch pengapian on (IG), switch power window OFF → DOWN: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] SU (5) - Masa bodi` | Warna Kabel: R - Masa bodi — Input motor power window UP (Remote) | Switch pengapian on (IG), switch utama power window OFF → UP (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] SD (1) - Masa bodi` | Warna Kabel: G - Masa bodi — Input motor power window DOWN (Remote) | Switch pengapian on (IG), switch utama power window OFF → DOWN (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] ECUB (4B-30) - GND1 (4E-17)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] IG (4S-7) - GND1 (4E-17)` | Warna Kabel: R - W-B — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[KACA DEPAN / KACA JENDELA] DCTY (4A-21) - Masa bodi` | Warna Kabel: R - Masa bodi — Input switch lampu courtesy pintu pengemudi | Pintu sisi pengemudi tertutup: 10 kΩ atau lebih tinggi / Pintu samping pengemudi terbuka: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] PCTY (4A-24) - Masa bodi` | Warna Kabel: L - Masa bodi — Input switch lampu courtesy pintu sisi penumpang | Pintu sisi penumpang tertutup: 10 kΩ atau lebih tinggi / Pintu samping penumpang terbuka: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] CANP (D64-23)*1 - Masa bodi` | Warna Kabel: BR - Masa bodi — Line komunikasi CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[KACA DEPAN / KACA JENDELA] CANP (D33-4)*2 - Masa bodi` | Warna Kabel: BR - Masa bodi — Line komunikasi CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[KACA DEPAN / KACA JENDELA] GND1 (4E-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] E (G8-1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] +B (G8-2) - E (G8-1)` | Warna Kabel: LG - W-B — Power supply baterai | Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] U (G8-10) - E (G8-1)` | Warna Kabel: R - W-B — Motor power window pintu sisi pengemudi UP | Switch pengapian on (IG), switch power window sisi pengemudi OFF → UP (pengoperasian manual) → power window sisi pengemudi ditutup sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] D (G8-7) - E (G8-1)` | Warna Kabel: G - W-B — Motor power window pintu sisi pengemudi DOWN | Switch pengapian on (IG), switch power window sisi pengemudi OFF → DOWN (pengoperasian manual) → power window sisi pengemudi terbuka sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] LED (G8-5) - E (G8-1)` | Warna Kabel: W - W-B — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] E (G1-1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] B (G1-6) - Masa bodi` | Warna Kabel: GR - Masa bodi — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[KACA DEPAN / KACA JENDELA] U (G1-8) - E (G1-1)` | Warna Kabel: R - W-B — Output motor power window pintu sisi pengemudi UP | Switch pengapian on (IG), switch power window sisi pengemudi OFF: 11 sampai 14 V / Switch pengapian on (IG), switch power window sisi pengemudi OFF → UP (pengoperasian manual) → power window sisi pengemudi ditutup sepenu |
| `[KACA DEPAN / KACA JENDELA] D (G1-5) - E (G1-1)` | Warna Kabel: G - W-B — Output motor power window pintu sisi pengemudi DOWN | Switch pengapian on (IG), switch power window sisi pengemudi OFF → DOWN (pengoperasian manual) → power window sisi pengemudi terbuka sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V / Switch pengapian on (IG),  |
| `[KACA DEPAN / KACA JENDELA] B (F1-3) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply pengapian | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] U (F1-4) - Masa bodi` | Warna Kabel: R - Masa bodi — Output motor power window pintu sisi penumpang UP | Switch pengapian on (IG), switch power window OFF → UP: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] D (F1-1) - Bodi masa` | Warna Kabel: G - Masa bodi — Output motor power window pintu sisi penumpang DOWN | Switch pengapian on (IG), switch power window OFF → DOWN: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] SU (F1-5) - Masa bodi` | Warna Kabel: W - Masa bodi — Input motor power window UP (Remote) | Switch pengapian on (IG), switch utama power window OFF → UP (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] SD (F1-2) - Masa bodi` | Warna Kabel: P - Masa bodi — Input motor power window DOWN (Remote) | Switch pengapian on (IG), switch utama power window OFF → DOWN (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] BECU (4B-30) - GND1 (4E-17)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 11 sampai 14 V |
| `[1NZ-FE] A20-20 (BATT) - C23-104 (E1)` | Warna Kabel: Y - W — Baterai (untuk mengukur voltase baterai dan untuk memori ECM) | Selalu: 11 sampai 14 V |
| `[1NZ-FE] A20-2 (+B) - C23-104 (E1)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] A20-1 (+B2) - C23-104 (E1)` | Warna Kabel: B - W — Power source ECM | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] A20-3 (+BM) - C23-43 (ME01)` | Warna Kabel: GR - BR — Power source aktuator throttle | Selalu: 11 sampai 14 V |
| `[1NZ-FE] C23-85 (IGT1) - C23-104 (E1)` | Warna Kabel: W - W — Koil pengapian (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] C23-84 (IGT2) - C23-104 (E1)` | Warna Kabel: O - W — Koil pengapian (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] C23-83 (IGT3) - C23-104 (E1)` | Warna Kabel: G - W — Koil pengapian (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] C23-82 (IGT4) - C23-104 (E1)` | Warna Kabel: LG - W — Koil pengapian (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] C23-81 (IGF1) - C23-104 (E1)` | Warna Kabel: Y - W — Koil pengapian (sinyal konfirmasi pengapian) | Switch pengapian on (IG): 4.5 sampai 5.5 V / Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] C23-122 (NE+) - C23-121 (NE-)` | Warna Kabel: L - P — Sensor posisi crankshaft | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[1NZ-FE] C23-99 (G2+) - C23-121 (NE-)` | Warna Kabel: B - P — Sensor posisi camshaft | Idling: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[1NZ-FE] C23-108 (#10) - C23-45 (E01)` | Warna Kabel: SB - BR — Injektor bahan bakar | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] C23-107 (#20) - C23-45 (E01)` | Warna Kabel: GR - BR — Injektor bahan bakar | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] C23-106 (#30) - C23-45 (E01)` | Warna Kabel: P - BR — Injektor bahan bakar | Idling: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[1NZ-FE] C23-105 (#40) - C23-45 (E01)` | Warna Kabel: L - BR — Injektor bahan bakar | Idling: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[1NZ-FE] C23-109 (HT1A) - C23-86 (E03)` | Warna Kabel: G - W — Heater sensor heated oxygen (sensor 1) | Switch pengapian on (IG): 11 sampai 14 V / Idling: Di bawah 3.0 V |
| `[1NZ-FE] C23-112 (OX1A) - C23-90 (EX1A)` | Warna Kabel: W - L — Sensor heated oxygen (sensor 1) | Putaran mesin dipertahankan pada 2,500 rpm selama 2 menit setelah pemanasan sensor: Pembangkitan pulsa (lihat bentuk gelombang 4) |
| `[1NZ-FE] C23-47 (HT1B) - C23-86 (E03)` | Warna Kabel: LG - W — Heater sensor heated oxygen (sensor 2) | Switch pengapian on (IG): 11 sampai 14 V / Idling: Di bawah 3.0 V |
| `[1NZ-FE] C23-64 (OX1B) - C23-87 (EX1B)` | Warna Kabel: G- GR — Sensor heated oxygen (sensor 2) | Putaran mesin dipertahankan pada 2,500 rpm selama 2 menit setelah pemanasan sensor: Pembangkitan pulsa (lihat bentuk gelombang 5) |
| `[1NZ-FE] C23-110 (KNK1) - C23-111 (EKNK)` | Warna Kabel: R - G — Sensor knock | Putaran mesin dipertahankan pada 4000 rpm setelah mesin dipanaskan: Pembangkitan pulsa (lihat bentuk gelombang 6) |
| `[1NZ-FE] A20-8 (SPD) - C23-104 (E1)` | Warna Kabel: V - W — Sinyal kecepatan dari meter kombinasi | Dikendarai pada 20 km/jam (12 mph): Pembangkitan pulsa (lihat bentuk gelombang 7) |
| `[1NZ-FE] C23-97 (THW) - C23-96 (ETHW)` | Warna Kabel: L - P — Sensor temperatur cairan pendingin mesin | Idling, Temperatur cairan pendingin mesin 80°C (176°F): 0.2 sampai 1.0 V |
| `[1NZ-FE] C23-65 (THA) - C23-88 (ETHA)` | Warna Kabel: P - O — Sensor temperatur udara intake (menyatu dalam mass air flow sensor) | Idling, temperatur udara masuk 20°C (68°F): 0.5 sampai 3.4 V |
| `[1NZ-FE] C23-118 (VG) - C23-116 (E2G)` | Warna Kabel: GR - LG — Mass air flow meter | Idling, gigi transmisi netral, switch A/C posisi OFF.: 0.5 sampai 3.0 V |
| `[1NZ-FE] A20-24 (W) - C23-104 (E1)` | Warna Kabel: B - W — MIL | Switch pengapian on (IG) (MIL nyala): Di bawah 3.0 V / Idling: 11 sampai 14 V |
| `[1NZ-FE] A20-48 (STA) - C23-104 (E1)` | Warna Kabel: BR - W — Sinyal starter | Switch pengapian on (IG): Di bawah 1.5 V / Cranking: 5.5 V atau lebih |
| `[1NZ-FE] C23-52 (STAR) - C23-104 (E1)` | Warna Kabel: O - W — Kontrol relay starter | Switch pengapian on (IG): Di bawah 1.5 V / Cranking: 5.5 V atau lebih |
| `[1NZ-FE] A20-13 (ACCR) - C23-45 (E01)` | Warna Kabel: G - BR — Sinyal kontrol relay ACC (cut) | Switch pengapian on (IG): 11 sampai 14 V / Cranking: Di bawah 1.5 V |
| `[1NZ-FE] A20-14 (STSW) - C23-104 (E1)` | Warna Kabel: B - W — Sinyal kerja relay starter | Switch pengapian on (IG): Di bawah 1.5 V / Cranking: 11 sampai 14 V |
| `[1NZ-FE] C23-115 (VTA1) - C23-91 (ETA)` | Warna Kabel: Y - V — Sensor posisi throttle (untuk kontrol mesin) | Switch pengapian on (IG), Throttle valve tertutup penuh: 0.5 sampai 1.1 V / Switch pengapian on (IG), Throttle valve terbuka penuh: 3.3 sampai 4.9 V |
| `[1NZ-FE] C23-114 (VTA2) - C23-91 (ETA)` | Warna Kabel: GR - V — Sensor posisi throttle (untuk deteksi malfungsi sensor) | Switch pengapian (IG), pedal akselerator dibebaskan: 2.1 sampai 3.1 V / Switch pengapian on (IG), pedal akselerator ditekan: 4.6 sampai 5.5 V |
| `[1NZ-FE] C23-67 (VCTA) - C23-91 (ETA)` | Warna Kabel: W - V — Power source sensor (voltase spesifikasi) | Switch pengapian on (IG): 4.5 sampai 5.5 V |
| `[1NZ-FE] A20-57 (VCPA) - A20-59 (EPA)` | Warna Kabel: B - G — Power source untuk sensor posisi pedal akselerator (untuk VPA) | Switch pengapian on (IG): 4.5 sampai 5.5 V |
| `[1NZ-FE] A20-55 (VPA) - A20-59 (EPA)` | Warna Kabel: R - G — Sensor posisi pedal akselerator (untuk kontrol mesin) | Switch pengapian (IG), pedal akselerator dibebaskan: 0.5 sampai 1.1 V / Switch pengapian on (IG), pedal akselerator ditekan penuh: 2.6 sampai 4.5 V |
| `[1NZ-FE] A20-56 (VPA2) - A20-60 (EPA2)` | Warna Kabel: L - BR — Sensor posisi pedal akselerator (untuk deteksi malfungsi sensor) | Switch pengapian (IG), pedal akselerator dibebaskan: 1.2 sampai 2.0 V / Switch pengapian on (IG), pedal akselerator ditekan penuh: 3.4 sampai 5.5 V |
| `[1NZ-FE] A20-58 (VCP2) - A20-60 (EPA2)` | Warna Kabel: W - BR — Power source untuk sensor posisi pedal akselerator (untuk VPA2) | Switch pengapian on (IG): 4.5 sampai 5.5 V |
| `[1NZ-FE] C23-42 (M+) - C23-43 (ME01)` | Warna Kabel: G - BR — Aktuator throttle | Idling dengan mesin panas: Pembangkitan pulsa (lihat bentuk gelombang 8) |
| `[1NZ-FE] C23-41 (M-) - C23-43 (ME01)` | Warna Kabel: R - BR — Aktuator throttle | Idling dengan mesin panas: Pembangkitan pulsa (lihat bentuk gelombang 9) |
| `[1NZ-FE] A20-36 (STP) - C23-104 (E1)` | Warna Kabel: G - W — Switch lampu rem | Pedal rem ditekan: 11 sampai 14 V / Pedal rem dibebaskan: Di bawah 1.5 V |
| `[1NZ-FE] A20-35 (ST1-) - C23-104 (E1)` | Warna Kabel: Y - W — Switch lampu rem | Switch pengapian on (IG), pedal rem ditekan: Di bawah 1.5 V / Switch pengapian (IG), pedal rem dibebaskan: 11 sampai 14 V |
| `[1NZ-FE] C23-49 (PRG) - C23-45 (E01)` | Warna Kabel: L - BR — Purge VSV | Switch pengapian on (IG): 11 sampai 14 V / Idling, dalam purge control: Pembangkitan pulsa (lihat bentuk gelombang 10) |
| `[1NZ-FE] A20-7 (FC) - C23-45 (E01)` | Warna Kabel: V - BR — Kontrol pompa bahan bakar | Switch pengapian on (IG): 11 sampai 14 V / Idling: Di bawah 1.5 V |
| `[1NZ-FE] A20-15 (TACH) - C23-104 (E1)` | Warna Kabel: LG - W — Putaran mesin | Idling: Pembangkitan pulsa (lihat bentuk gelombang 11) |
| `[1NZ-FE] A20-27 (TC) - C23-104 (E1)` | Warna Kabel: P - W — Terminal TC dari DLC3 | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] C23-100 (OC1+) - C23-123 (OC1-)` | Warna Kabel: BR - R — Camshaft timing oil control valve (OCV) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 12) |
| `[1NZ-FE] A20-41 (CANH) - C23-104 (E1)` | Warna Kabel: L - W — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 13) |
| `[1NZ-FE] A20-49 (CANL) - C23-104 (E1)` | Warna Kabel: W - W — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 14) |
| `[1NZ-FE] C23-50 (ALT) - C23-104 (E1)` | Warna Kabel: P - W — Generator | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] A20-22 (FAN2) - C23-104 (E1)` | Warna Kabel: LG - W — Relay FAN No. 2 | Idling dengan temperatur cairan pendingin mesin tinggi: Di bawah 1.5 V |
| `[1NZ-FE] A20-28 (IGSW) - C23-104 (E1)` | Warna Kabel: R - W — Switch pengapian | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] A20-44 (MREL) - C23-104 (E1)` | Warna Kabel: GR - W — Relay EFI | Switch pengapian on (IG): 11 sampai 14 V |
| `[1NZ-FE] A20-31 (ELS) - C23-104 (E1)` | Warna Kabel: G - W — Beban kelistrikan | Switch lampu belakang on: 7.5 sampai 14 V / Switch lampu belakang off: Di bawah 1.5 V |
| `[1NZ-FE] A20-33 (ELS3) - C23-104 (E1)` | Warna Kabel: V - W — Beban kelistrikan | Switch lampu kabut ON: 7.5 sampai 14 V / Switch lampu kabut off: Di bawah 1.5 V |
| `[1NZ-FE] C23-84 (IGT2) - C23-104 (E1)` | Warna Kabel: BE - W — Koil pengapian (sinyal pengapian) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[1NZ-FE] C23-65 (THA) - C23-88 (ETHA)` | Warna Kabel: P - BE — Sensor temperatur udara intake (menyatu dalam mass air flow sensor) | Idling, temperatur udara masuk 20°C (68°F): 0.5 sampai 3.4 V |
| `[1NZ-FE] C23-52 (STAR) - C23-104 (E1)` | Warna Kabel: BE - W — Kontrol relay starter | Switch pengapian on (IG): Di bawah 1.5 V / Cranking: 5.5 V atau lebih |
| `[STARTING 1NZ-FE] D35-1 (AM1) - Masa bodi` | Warna Kabel: O - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] D34-6 (AM2) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] D35-10 (SSW1) - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal switch mesin | Switch mesin ditekan: Di bawah 1 Ω / Switch mesin tidak ditekan: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] D35-9 (SSW2) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal switch mesin | Switch mesin ditekan: Di bawah 1 Ω / Switch mesin tidak ditekan: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] D36-15 (CANH) - Masa Bodi` | Warna Kabel: R - Masa bodi — Line CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] D36-16 (CANL) - Masa bodi` | Warna Kabel: W - Masa bodi — Line CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] 4E-17 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] D35-4 (GND2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] 4D-9 (LIN1) - Masa bodi` | Warna Kabel: P - Masa bodi — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] D36-11 (ACCR) - D35-4 (GND2)` | Warna Kabel: G - W-B — Sinyal assist starter (ACC cut signal) | Pedal rem ditekan, shift lever posisi P, switch mesin ditekan sekali → on (IG): 0.1 sampai 0.8 V *1 → Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] D34-4 (ACCD) - D35-4 (GND2)` | Warna Kabel: LG - W-B — Sinyal ACC | Switch mesin on (ACC): Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. / Switch mesin off: Di bawah 1 V |
| `[STARTING 1NZ-FE] D35-5 (IG2D) - D35-4 (GND2)` | Warna Kabel: P - W-B — Sinyal IG2 | Switch mesin on (IG): Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. / Switch mesin on (ACC): Di bawah 1 V |
| `[STARTING 1NZ-FE] D35-6 (SRX) - D35-4 (GND2)` | Warna Kabel: G - W-B — sinyal IG1 | Switch mesin on (IG): Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. / Switch mesin on (ACC): Di bawah 1 V |
| `[STARTING 1NZ-FE] D34-7 (SLR+) - D35-4 (GND2)` | Warna Kabel: L - W-B — Sinyal motor steering lock | Motor steering lock bekerja: Di bawah 1 V / Motor steering lock motor tidak bekerja: Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] D34-18 (SLP) - D35-4 (GND2)` | Warna Kabel: GR - W-B — Sinyal posisi aktuator steering lock | Steering lock telah terkunci: Pembangkitan pulsa (lihat bentuk gelombang 1) / Kunci steering dibebaskan: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[STARTING 1NZ-FE] 4C-8 (SPD) - D35-4 (GND2)` | Warna Kabel: SB - W-B — Sinyal kecepatan dari meter kombinasi | Switch mesin on (IG), Putar roda penggerak perlahan-lahan: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[STARTING 1NZ-FE] D36-2 (TACH) - D35-4 (GND2)` | Warna Kabel: L - W-B — Sinyal Tachometer | Mesin hidup: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[STARTING 1NZ-FE] D36-4 (STSW) - D35-4 (GND2)` | Warna Kabel: B - W-B — Sinyal permintaan aktivasi starter | Pedal rem ditekan, switch mesin ditahan on (ST): Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] D36-3 (STR) - D35-4 (GND2)` | Warna Kabel: GR - W-B — Sinyal switch start netral | Pedal rem diinjak, posisi shift lever P atau N, switch mesin on (ST): Di bawah 2 V → Pembangkitan pulsa *2 |
| `[STARTING 1NZ-FE] D36-14 (STR2) - D35-4 (GND2)` | Warna Kabel: O - W-B — Sinyal starter (Sub) | Pedal rem diinjak, posisi shift lever P atau N, switch mesin on (ST): Output voltase pada terminal AM1 atau AM2 adalah -3.5 V atau lebih. *3 |
| `[STARTING 1NZ-FE] D36-1 (INDS) - D35-4 (GND2)` | Warna Kabel: SB - W-B — Sinyal kondisi kendaraan | Pedal rem diinjak, engine switch off, on (ACC, IG): Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] D36-8 (INDW) - D35-4 (GND2)` | Warna Kabel: Y - W-B — Sinyal kondisi kendaraan | Pedal rem diinjak, engine switch off, on (ACC, IG): Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] D35-8 (SWIL) - D35-4 (GND2)` | Warna Kabel: LG - W-B — Sinyal penerangan | Switch kontrol lampu TAIL atau HEAD: Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] D34-14 (STP) - D35-4 (GND2)` | Warna Kabel: G - W-B — Switch lampu rem | Pedal rem ditekan: Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. / Pedal rem dibebaskan: Di bawah 1 V |
| `[STARTING 1NZ-FE] D34-15 (P) - D35-4 (GND2)` | Warna Kabel: P - W-B — Sinyal shift lock | Posisi shift lever P: Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. / Posisi shift lever kecuali P: Di bawah 1 V |
| `[STARTING 1NZ-FE] 4S-6 (ACC) - Masa bodi` | Warna Kabel: GR - Masa bodi — Power supply ACC | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] 4S-7 (IG) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply IG | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] D28-1 (+B) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] D28-10 (LIN) - Masa bodi` | Warna Kabel: P - Masa bodi — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[STARTING 1NZ-FE] D28-17 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] D28-18 (IG) - Masa bodi` | Warna Kabel: BR - Masa bodi — Power supply pengapian | Switch mesin on (IG): 11 sampai 14 V / Switch mesin off: Di bawah 1 V |
| `[STARTING 1NZ-FE] A20-20 (BATT) - Masa bodi` | Warna Kabel: Y - Masa bodi — Baterai (untuk mengukur voltase baterai dan untuk memori ECM) | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] A20-2 (+B) - Masa bodi` | Warna Kabel: B - Masa bodi — Power source ECM | Switch mesin on (IG): 11 sampai 14 V |
| `[STARTING 1NZ-FE] A20-1 (+B2) - Masa bodi` | Warna Kabel: B - Masa bodi — Power source ECM | Switch mesin on (IG): 11 sampai 14 V |
| `[STARTING 1NZ-FE] A20-28 (IGSW-) - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal switch mesin | Switch mesin on (IG): 11 sampai 14 V |
| `[STARTING 1NZ-FE] C23-104 (E1) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] C23-45 (E01) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] C23-44 (E02) - Masa bodi` | Warna Kabel: B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] C23-86 (E03) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] C23-43 (ME01) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] A20-32 (EC) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] A20-13 (ACCR) - C23-104 (E1)` | Warna Kabel: G - W — Sinyal pemutus relay ACC (output) | Pedal rem ditekan, tuas shift di posisi P,atau N, engine switch ditekan sekali → on (IG): 0.1 sampai 0.8 V *1 → Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] A20-14 (STSW) - C23-104 (E1)` | Warna Kabel: B - W — Sinyal permintaan aktivasi starter | Pedal rem ditekan, engine switch ditahan (IG): Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih. |
| `[STARTING 1NZ-FE] A20-48 (STA) - C23-104 (E1)` | Warna Kabel: BR - W — Sinyal kerja relay starter | Cranking: 11 sampai 14 V |
| `[STARTING 1NZ-FE] C23-52 (STAR) - C23-104 (E1)` | Warna Kabel: O - W — Sinyal starter (Main) | Pedal rem diinjak, posisi shift lever P atau N, switch mesin on (ST): 11 sampai 14 V |
| `[STARTING 1NZ-FE] A20-15 (TACH) - C23-104 (E1)` | Warna Kabel: LG - W — Sinyal putaran mesin (output) | Idling: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[STARTING 1NZ-FE] A20-36 (STP) - C23-104 (E1)` | Warna Kabel: G - W — Sinyal switch lampu rem (input) | Pedal rem ditekan: 7.5 sampai 14 V / Pedal rem dibebaskan: Di bawah 1.5 V |
| `[STARTING 1NZ-FE] D22-7 (B) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] D22-6 (IG2) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply pengapian | Switch mesin on (IG): 11 sampai 14 V / Switch mesin off: Di bawah 1 V |
| `[STARTING 1NZ-FE] D22-1 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] D22-2 (SGND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STARTING 1NZ-FE] D22-4 (SLP1) - D22-1 (GND)` | Warna Kabel: GR - W-B — Sinyal posisi aktuator steering lock | Steering lock telah terkunci: 11 sampai 14 V / Kunci steering dibebaskan: Di bawah 1 V |
| `[STARTING 1NZ-FE] D35-1 (AM1) - Masa bodi` | Warna Kabel: BE - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[STARTING 1NZ-FE] D36-14 (STR2) - D35-4 (GND2)` | Warna Kabel: BE - W-B — Sinyal starter (Sub) | Pedal rem diinjak, posisi shift lever P atau N, switch mesin on (ST): Output voltase pada terminal AM1 atau AM2 adalah -3.5 V atau lebih. *3 |
| `[STARTING 1NZ-FE] C23-52 (STAR) - C23-104 (E1)` | Warna Kabel: BE - W — Sinyal starter (Main) | Pedal rem diinjak, posisi shift lever P atau N, switch mesin on (ST): 11 sampai 14 V |
| `[A/T U340E] C23-74 (L) - C23-104 (E1)` | Warna Kabel: V - W — Sinyal switch posisi pemindahan L | Switch pengapian on (IG) dan shift lever posisi L: 11 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi L: Di bawah 1 V |
| `[A/T U340E] C23-55 (2) - C23-104 (E1)` | Warna Kabel: G - W — 2 sinyal switch posisi pemindahan | Switch pengapian on (IG) dan shift lever posisi 2: 11 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi 2: Di bawah 1 V |
| `[A/T U340E] A20-26 (ODMS) - C23-104 (E1)` | Warna Kabel: O - W — 3 sinyal switch posisi pemindahan | Switch pengapian on (IG) dan shift lever posisi 3: 11 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi 3: Di bawah 1 V |
| `[A/T U340E] C23-56 (D) - C23-104 (E1)` | Warna Kabel: L - W — Sinyal switch posisi pemindahan D | Switch pengapian on (IG) dan shift lever posisi D atau 3: 11 sampai 14 V / Switch pengapian on (IG) dan tuas pemindah gigi selain posisi D dan 3: Di bawah 1 V |
| `[A/T U340E] C23-53 (R) - C23-104 (E1)` | Warna Kabel: R - W — Sinyal switch posisi pemindahan R | Switch pengapian on (IG) dan shift lever posisi R: 11 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi R: Di bawah 1 V |
| `[A/T U340E] C23-54 (N) - C23-104 (E1)` | Warna Kabel: SB - W — Sinyal switch posisi pemindahan N | Switch pengapian on (IG) dan shift lever posisi N: 11 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi N: Di bawah 1 V |
| `[A/T U340E] C23-73 (P) - C23-104 (E1)` | Warna Kabel: R - W — Sinyal switch posisi pemindahan P | Switch pengapian on (IG) dan shift lever posisi P: 11 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi P: Di bawah 1 V |
| `[A/T U340E] C23-52 (STAR(NSW)) - C23-104 (E1)` | Warna Kabel: O - W — Sinyal switch posisi Parkir/Netral | Switch pengapian on (IG) dan tuas pemindah gigi posisi P atau N: Di bawah 2 V / Switch pengapian on (IG) dan tuas pemindah gigi selain posisi P dan N: 11 sampai 14 V |
| `[A/T U340E] C23-125 (NT+) - C23-124 (NT-)` | Warna Kabel: B - G — Sinyal sensor kecepatan NT | Mesin hidup: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[A/T U340E] A20-36 (STP) - C23-104 (E1)` | Warna Kabel: G - W — Sinyal switch lampu rem | Pedal rem ditekan: 7.5 sampai 14 V / Pedal rem dibebaskan: Di bawah 1.5 V |
| `[A/T U340E] A20-8 (SPD) - C23-104 (E1)` | Warna Kabel: V - W — Sinyal kecepatan | Switch pengapian on (IG), dan putar roda penggerak perlahan-lahan: Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[A/T U340E] C23-79 (S1) - C23-104 (E1)` | Warna Kabel: SB - W — Sinyal solenoid S1 | Switch pengapian on (IG): 11 sampai 14 V / gear ke-1 atau ke-2: 11 sampai 14 V / gigi ke-3 atau gigi ke-4: Di bawah 1 V |
| `[A/T U340E] C23-78 (S2) - C23-104 (E1)` | Warna Kabel: L - W — Sinyal solenoid S2 | Switch pengapian on (IG): Di bawah 1 V / gigi ke-1 atau gigi ke-4: 11 sampai 14 V / gigi ke-2 atau gigi ke-3: Di bawah 1 V |
| `[A/T U340E] C23-80 (ST) - C23-104 (E1)` | Warna Kabel: GR - W — Sinyal solenoid ST | Posisi D (gear ke-3 ←→ gear ke-4): Dibawah 1 V ←→ 11 sampai 14 V |
| `[A/T U340E] C23-76 (SLT+) - C23-75 (SLT-)` | Warna Kabel: G - W — Sinyal solenoid SLT | Putaran idle mesin: Pembangkitan pulsa (Lihat bentuk gelombang 3) |
| `[A/T U340E] C23-57 (SL) - C23-104 (E1)` | Warna Kabel: P - W — Sinyal solenoid SL | Switch pengapian on (IG): Di bawah 1 V / Kendaraan dikendarai dalam lock-up range: 11 sampai 14 V |
| `[A/T U340E] C23-72 (THO1) - C23-95 (ETHO)` | Warna Kabel: Y - B — Sinyal sensor temperatur ATF (Automatic Transmission Fluid) | Temperatur ATF: 10°C (50 °F) sampai 145 °C (293 °F): 4 sampai 0 V |
| `[A/T U340E] A20-26 (ODMS) - C23-104 (E1)` | Warna Kabel: BE - W — 3 sinyal switch posisi pemindahan | Switch pengapian on (IG) dan shift lever posisi 3: 11 sampai 14 V / Switch pengapian on (IG) dan shift lever selain posisi 3: Di bawah 1 V |
| `[A/T U340E] C23-52 (STAR(NSW)) - C23-104 (E1)` | Warna Kabel: BE - W — Sinyal switch posisi Parkir/Netral | Switch pengapian on (IG) dan tuas pemindah gigi posisi P atau N: Di bawah 2 V / Switch pengapian on (IG) dan tuas pemindah gigi selain posisi P dan N: 11 sampai 14 V |
| `[KONTROL REM] A15-1 (+BS) - Masa bodi` | Warna Kabel: W - Masa bodi — Power source solenoid valve | Selalu: 11 sampai 14 V |
| `[KONTROL REM] A15-2 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa ECU skid control | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] A15-10 (STP) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu rem | Switch lampu rem ON Pedal rem ditekan: 11 sampai 14 V / Switch lampu rem OFF Pedal rem dibebaskan: Di bawah 1.5 V |
| `[KONTROL REM] A15-23 (+BM) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply relay motor | Selalu: 11 sampai 14 V |
| `[KONTROL REM] A15-24 (GND2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa aktuator pump motor | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] A15-25 (IG1) - Masa bodi` | Warna Kabel: B - Masa bodi — Power source ECU | Switch pengapian on (IG): 11 sampai 14 V |
| `[KONTROL REM] A27-1 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa ECU skid control | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] A27-12 (+BS) - Masa bodi` | Warna Kabel: W - Masa bodi — Power source solenoid relay | Selalu: 11 sampai 14 V |
| `[KONTROL REM] A27-13 (GND2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa pump motor | Selalu: Di bawah 1 Ω |
| `[KONTROL REM] A27-28 (STP) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu rem | Switch lampu rem ON → OFF (Pedal rem ditekan → dibebaskan): 8 sampai 14 V → Di bawah 1.5 V |
| `[KONTROL REM] A27-24 (+BM) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply relay motor | Selalu: 11 sampai 14 V |
| `[KONTROL REM] A27-25 (CANH) - A27-14 (CANL)` | Warna Kabel: G - W — CAN BUS | Switch pengapian off: 54 sampai 69 Ω |
| `[KONTROL REM] A27-34 (IG1) - Masa bodi` | Warna Kabel: B - Masa bodi — Power source ECU | Switch pengapian ON: 11 sampai 14 V |
| `[STEERING COLUMN] D22-1 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[STEERING COLUMN] D22-2 (SGND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa sinyal | Selalu: Di bawah 1 Ω |
| `[STEERING COLUMN] D22-3 (IGE) - D22-1 (GND)` | Warna Kabel: L - W-B — Catu daya untuk menggerakan motor | Motor saat bekerja: Di bawah 1 V / Motor saat tidak bekerja: 11 sampai 14 V |
| `[STEERING COLUMN] D22-4 (SLP1) - D22-2 (SGND)` | Warna Kabel: GR - W-B — Sinyal output sensor posisi unlock | Steering terkunci: 11 sampai 14 V / Steering lock dibebaskan: Di bawah 1 V |
| `[STEERING COLUMN] D22-5 (LIN) - D22-2 (SGND)` | Warna Kabel: P - W-B — Bus komunikasi LIN | Switch mesin on (IG): Pembangkitan pulsa |
| `[STEERING COLUMN] D22-6 (IG2) - D22-1 (GND)` | Warna Kabel: R - W-B — Input sinyal IG | Switch mesin on (IG): 11 sampai 14 V |
| `[STEERING COLUMN] D22-7 (B) - D22-1 (GND)` | Warna Kabel: R - W-B — Power source | Selalu: 11 sampai 14 V |
| `[POWER STEERING] A18-1 (PIG) - A18-2 (PGND)` | Warna Kabel: W - W-B — Fuse EPS | Selalu: 11 sampai 14 V |
| `[POWER STEERING] A18-2 (PGND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa bodi | Selalu: Di bawah 1 Ω |
| `[POWER STEERING] U1-1 (M1) - A18-2 (PGND)` | Warna Kabel: R - W-B — Motor power steering | Dengan switch pengapian on (IG), putar steering wheel ke kiri: Di bawah 1 V / Dengan switch pengapian on (IG), putar steering wheel ke kanan: 11 sampai 14 V |
| `[POWER STEERING] U1-2 (M2) - A18-2 (PGND)` | Warna Kabel: B - W-B — Motor power steering | Dengan switch pengapian on (IG), putar steering wheel ke kiri: 11 sampai 14 V / Dengan switch pengapian on (IG), putar steering wheel ke kanan: Di bawah 1 V |
| `[POWER STEERING] D29-1 (CANH) - D29-7 (CANL)` | Warna Kabel: SB - W — CAN BUS | Switch pengapian off: 108 sampai 132 Ω |
| `[POWER STEERING] D29-2 (SIL) - A18-2 (PGND)` | Warna Kabel: P - W-B — DLC3 | Komunikasi dibuat dengan menghubungkan intelligent tester ke DLC3: Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[POWER STEERING] D29-5 (SPD)* - A18-2 (PGND)` | Warna Kabel: R - W-B — Sinyal kecepatan | Switch pengapian on (IG): Pembangkitan pulsa (Lihat bentuk gelombang 2) |
| `[POWER STEERING] D29-6 (IG) - A18-2 (PGND)` | Warna Kabel: L - W-B — Fuse ECU-IG | Switch pengapian on (IG): 11 sampai 14 V |
| `[POWER STEERING] D29-11 (TS) - A18-2 (PGND)` | Warna Kabel: LG - W-B — DLC3 | Switch pengapian on (IG): 11 sampai 14 V |
| `[POWER STEERING] V1-5 (TRQ1) - A18-2 (PGND)` | Warna Kabel: W - W-B — Sensor torsi | Dengan switch pengapian on (IG), putar steering wheel ke kiri dan kanan: 0.3 sampai 4.7 V |
| `[POWER STEERING] V1-6 (TRQV) - A18-2 (PGND)` | Warna Kabel: R - W-B — Sensor torsi | Switch pengapian on (IG): 7.5 sampai 8.5 V |
| `[POWER STEERING] V1-7 (TRQ2) - A18-2 (PGND)` | Warna Kabel: Y - W-B — Sensor torsi | Dengan switch pengapian on (IG), putar steering wheel ke kiri dan kanan: 0.3 sampai 4.7 V |
| `[POWER STEERING] V1-8 (TRQG) - A18-2 (PGND)` | Warna Kabel: B - W-B — Sensor torsi | Selalu: Di bawah 1 Ω |
| `[AIR CONDITIONING] E7-12 (PSW) - E7-24 (GND)` | Warna Kabel: GR - W-B — Switch sinyal tekanan air conditioning | Tekanan refrigerant: normal: Di bawah 1 V / Tekanan refrigerant: Abnormal (kurang dari 0.196 kPa (2.0 kgf/cm 2 ] atau lebih dari 3.14 MPa [32 kgf/cm 2 ]): 11 sampai 14 V |
| `[AIR CONDITIONING] E7-14 (IG+) - E7-24 (GND)` | Warna Kabel: Y - W-B — Power source (IG) | Switch pengapian: on (IG): 11 sampai 14 V |
| `[AIR CONDITIONING] E7-15 (MGC) - E7-24 (GND)` | Warna Kabel: LG - W-B — HTR SUB1 / AC MG Sinyal operasi relay | Mesin idle: 11 sampai 14 V → Dibawah 1 V / Kontrol heater (switch blower): 0 → 1: 11 sampai 14 V → Dibawah 1 V / Volume Cooler: ON: 11 sampai 14 V → Dibawah 1 V |
| `[AIR CONDITIONING] E7-17 (AC1) - E7-24 (GND)` | Warna Kabel: R - W-B — Sinyal pemesan idle-up | Mesin idle: 11 sampai 14 V / Magnet Clutch tidak mengait: 11 sampai 14 V / Mesin idle: Di bawah 1 V / Magnet Clutch mengait: Di bawah 1 V |
| `[AIR CONDITIONING] E7-19 (ACT) - E7-24 (GND)` | Warna Kabel: B - W-B — Magnet pada permit signal | Mesin idle → Pedal akselerator ditekan (Air conditioning memutus output signal ketika beban mesin ditambah dengan cepat): 11 sampai 14 V → Dibawah 1 V |
| `[AIR CONDITIONING] E7-21 (SBLW) - E7-24 (GND)` | Warna Kabel: BR - W-B — Sinyal motor blower ON | Switch pengapian: on (IG): 11 sampai 14 V → Dibawah 1 V / Kontrol heater (switch blower): 0 → 1: 11 sampai 14 V → Dibawah 1 V |
| `[AIR CONDITIONING] E7-22 (TE) - E7-23 (SG-2)` | Warna Kabel: GR - L — Sinyal sensor temperatur evaporator | Switch pengapian: on (IG): 1.0 sampai 1.3 V / Temperatur dekat evaporator: 15°C (59°F): 1.0 sampai 1.3 V |
| `[AIR CONDITIONING] E7-23 (SG-2) - Masa bodi` | Warna Kabel: L - Masa bodi — Masa untuk sensor temperatur evaporator | Selalu: Di bawah 1 Ω |
| `[AIR CONDITIONING] E7-24 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa untuk power supply utama | Selalu: Di bawah 1 Ω |
| `[AIR CONDITIONING] E7-26 (B/V) - E7-23 (SG-2)` | Warna Kabel: LG - L — Sinyal penyetelan temperatur ruang | Switch pengapian: on (IG): 3.0 sampai 3.7 V → Dibawah 1 V / Knob kontrol heater No. 3: OFF → Max cool: 3.0 sampai 3.7 V → Dibawah 1 V |
| `[SEAT BELT] 4B-30 (BECU) - 4E-17 (GND1)` | Warna Kabel: L - W-B — Baterai | Selalu: 11 sampai 14 V |
| `[SEAT BELT] D34-26 (DBKL)*1 - Masa bodi` | Warna Kabel: W - Masa Bodi — Sinyal seat inner belt assembly depan (sisi pengemudi) | Switch pengapian on (IG) Tongue plate telah dikenakan: Di bawah 1 V / Switch pengapian on (IG) Tongue plate tidak dikenakan: 11 sampai 14 V |
| `[SEAT BELT] D36-15 (CANH)*1 - 4E-17 (GND1)` | Warna Kabel: R - W-B — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[SEAT BELT] D36-16 (CANL)*1 - 4E-17 (GND1)` | Warna Kabel: W - W-B — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[SEAT BELT] D33-23 (CANH)*2 - 4E-17 (GND1)` | Warna Kabel: R - W-B — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[SEAT BELT] D33-22 (CANL)*2 - 4E-17 (GND1)` | Warna Kabel: W - W-B — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ANTI PENCURIAN] D26-11 (+B1) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN] D26-13 (+B2) - Masa bodi` | Warna Kabel: BR - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN] D26-9 (IG) - D26-16 (E)` | Warna Kabel: GR - W-B — Power supply pengapian (Sinyal IG) | Switch mesin off → on (IG) *1 Switch pengapian OFF → ON *2: Di bawah 1 V → 11 sampai 14 V |
| `[ANTI PENCURIAN] D26-7 (KSW) *2 - D26-16 (E)` | Warna Kabel: Y *2 - W-B — Input swich peringatan unlock | Kunci tidak dalam silinder kunci pengapian (OF) → Kunci disisipkan (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] D26-4 (DSWH) - D26-16 (E)` | Warna Kabel: W - W-B — Switch courtesy kap mesin | Kap mesin TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] D26-16 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ANTI PENCURIAN] D26-24 (BRK+) - D26-16 (E)` | Warna Kabel: P - W-B — Komunikasi Alarm BERKES | Sistem anti pencurian dalam status membunyikan alarm: Pembangkitan pulsa (1.5 V ← → Dibawah 1.2 V) |
| `[ANTI PENCURIAN] D26-25 (BRK-) - D26-16 (E)` | Warna Kabel: O - W-B — Komunikasi Alarm BERKES | Semua pintu telah dikunci menggunakan kunci (Sistem anti pencurian dalam status persiapan siaga).: Pembangkitan pulsa (1.5 V ← → Dibawah 1.2 V) |
| `[ANTI PENCURIAN] D26-15 (SH-) - Masa bodi` | Warna Kabel: O - Masa bodi — Horn keamanan | Horn kemanan sedang berbunyi (Sistem anti pencurian dalam status membunyikan alarm).: Pembangkitan pulsa (11 sampai 14 V ← → Dibawah 1 V) |
| `[ANTI PENCURIAN] D26-29 (IND) - D26-16 (E)` | Warna Kabel: G - W-B — Output indikator keamanan | Indikator keamanan menyala (Menyala hanya pada status persiapan siaga atau dalam status membunyikan alarm. Berkedip ketika immobilisier bekerja.): 3 sampai 6 V |
| `[ANTI PENCURIAN] D26-31 (HORN) - D26-16 (E)` | Warna Kabel: G - W-B — Penggerak (drive) horn kendaraan | Horn kemanan berbunyi (Sistem anti pencurian dalam status membunyikan alarm): Pembangkitan pulsa (0 V ←→ 12 V) |
| `[ANTI PENCURIAN] 4B-30 (BECU) * - Masa bodi` | Warna Kabel: L * - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN] 4E-17 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ANTI PENCURIAN] 4C-6 (DCTY) - Masa bodi` | Warna Kabel: B - Masa bodi — Input switch lampu courtesy pintu pengemudi | Pintu sisi pengemudi TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] 4A-24 (PCTY) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch input lampu courtesy sisi penumpang | Pintu sisi penumpang TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω (1.5 V ← → Dibawah 1.2 V) |
| `[ANTI PENCURIAN] 4A-20 (RRCY) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch input lampu courtesy belakang RH | Pintu belakang RH TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] 4A-5 (RRCY) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu courtesy belakang LH | Pintu belakang LH TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] 4A-7 (BCTY) - Masa bodi` | Warna Kabel: SB - Masa bodi — Switch courtesy pintu kompartmen bagasi | Pintu kompartmen bagasi TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[ANTI PENCURIAN] 4S-6 (ACC) - Masa bodi` | Warna Kabel: GR - Masa bodi — Power supply pengapian (Sinyal ACC) | Switch pengapian on (ACC) → off: 11 sampai 14 V → Dibawah 1 V |
| `[ANTI PENCURIAN] 4S-7 (IG) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply pengapian (Sinyal IG) | Power supply pengapian (Sinyal IG): 11 sampai 14 V → Dibawah 1 V |
| `[ANTI PENCURIAN] 4S-17 (HAZ) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal relay flasher tanda belok | Sistem dalam status membunyikan alarm: Di bawah 1 V |
| `[ANTI PENCURIAN] D28-1 (+B) - D28-17 (E)` | Warna Kabel: B - W-B — Power supply baterai | Selalu: 11 sampai 14 V |
| `[ANTI PENCURIAN] D28-17 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ANTI PENCURIAN] D28-18 (IG) - D28-17 (E)` | Warna Kabel: BR - W-B — Power supply IG | Switch mesin on (IG): 11 sampai 14 V |
| `[ANTI PENCURIAN] D28-24 (SEC1) - D28-17 (E)` | Warna Kabel: P - W-B — Komunikasi BERKES alarm | Sistem anti pencurian dalam status membunyikan alarm: Pembangkitan pulsa (1.5 V ← → Dibawah 1.2 V) |
| `[ANTI PENCURIAN] D28-25 (SEC0) - D28-17 (E)` | Warna Kabel: O - W-B — Komunikasi BERKES alarm | Sistem anti pencurian dalam status persiapan alarm: Pembangkitan pulsa (1.5 V ← → Dibawah 1.2 V) |
| `[ANTI PENCURIAN] D26-25 (BRK-) - D26-16 (E)` | Warna Kabel: BE - W-B — Komunikasi Alarm BERKES | Semua pintu telah dikunci menggunakan kunci (Sistem anti pencurian dalam status persiapan siaga).: Pembangkitan pulsa (1.5 V ← → Dibawah 1.2 V) |
| `[ANTI PENCURIAN] D26-15 (SH-) - Masa bodi` | Warna Kabel: BE - Masa bodi — Horn keamanan | Horn kemanan sedang berbunyi (Sistem anti pencurian dalam status membunyikan alarm).: Pembangkitan pulsa (11 sampai 14 V ← → Dibawah 1 V) |
| `[ANTI PENCURIAN] D28-25 (SEC0) - D28-17 (E)` | Warna Kabel: BE - W-B — Komunikasi BERKES alarm | Sistem anti pencurian dalam status persiapan alarm: Pembangkitan pulsa (1.5 V ← → Dibawah 1.2 V) |
| `[ENGINE IMMOBILISER] D18-8 (AGND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D18-14 (VC5) - D18-8 (AGND)` | Warna Kabel: P - BR — Power supply | Sistem engine immobiliser dalam kondisi set (kunci tidak di dalam kabin): Di bawah 1 V / Tekan engine switch*: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] D18-10 (CODE) - D18-8 (AGND)` | Warna Kabel: O - BR — Sinyal demodulasi dari data kode kunci | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch mesin telah ditekan dan kunci dipegang dekat engine switch*: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] D18-9 (TXCT) - D18-8 (AGND)` | Warna Kabel: V - BR — Sinyal output kode kunci | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch mesin telah ditekan dan kunci dipegang dekat engine switch*: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] D28-17 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D28-1 (+B1) - D28-17 (E)` | Warna Kabel: B - W-B — Power supply +B | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D28-18 (IG) - D28-17 (E)` | Warna Kabel: BR - W-B — Power supply pengapian | Switch mesin off: Di bawah 1 V |
| `[ENGINE IMMOBILISER] D28-40 (AGND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa engine switch | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D28-30 (VC5) - D28-40 (AGND)` | Warna Kabel: P - BR — Power supply engine switch | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch mesin ditekan*: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] D28-9 (CODE) - D28-40 (AGND)` | Warna Kabel: O - BR — Input KODE engine switch | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch mesin telah ditekan dan kunci dipegang dekat engine switch*: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] D28-8 (TXCT) - D28-40 (AGND)` | Warna Kabel: V - BR — Output TXCT engine switch | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch mesin telah ditekan dan kunci dipegang dekat engine switch*: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] D24-8 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D24-1 (+B) - GND (D24-8)` | Warna Kabel: L - W-B — Power supply +B | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D24-5 (EFII) - D24-8 (GND)` | Warna Kabel: O - W-B — Sinyal input ECM | Switch mesin off: Di bawah 1 V / Switch mesin on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] D24-6 (EFIO) - D24-8 (GND)` | Warna Kabel: W - W-B — Sinyal output ECM | Switch mesin off: Di bawah 1 V / Switch mesin on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] D22-2 (SGND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D22-1 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D22-7 (B) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D22-6 (IG2) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply pengapian | Switch mesin off: 0 V / Switch mesin on (IG): 11 sampai 14 V |
| `[ENGINE IMMOBILISER] A20-9 (EOM) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] C23-104 (E1) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] C23-45 (E01) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] C23-86 (E03) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] C23-43 (ME01) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] A20-20 (BATT) - C23-104 (E1)` | Warna Kabel: Y - W — Baterai (untuk mengukur voltase baterai dan untuk memori ECM) | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] A20-28 (IGSW) - C23-104 (E1)` | Warna Kabel: R - W — Switch mesin | Switch mesin on (IG): 11 sampai 14 V |
| `[ENGINE IMMOBILISER] A20-2 (+B) - C23-104 (E1)` | Warna Kabel: B - W — Power source ECM | Switch mesin on (IG): 11 sampai 14 V |
| `[ENGINE IMMOBILISER] A20-1 (+B2) - C23-104 (E1)` | Warna Kabel: B - W — Power source ECM | Switch mesin on (IG): 11 sampai 14 V |
| `[ENGINE IMMOBILISER] A20-3 (+BM) - C23-43 (ME01)` | Warna Kabel: GR - BR — Power source ECM | Switch mesin on (IG): 11 sampai 14 V |
| `[ENGINE IMMOBILISER] A20-11 (IMI) - A20-9 (EOM)` | Warna Kabel: W - BR — Sinyal input ID kode box | Switch mesin off: Di bawah 1 V / Switch mesin on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] A20-10 (IMO) - A20-9 (EOM)` | Warna Kabel: O - BR — Sinyal output ID kode box | Switch mesin off: Di bawah 1 V / Switch mesin on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] 4E-17 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D35-4 (GND2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D35-1 (AM1) - Masa bodi` | Warna Kabel: O - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D34-6 (AM2) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D35-10 (SSW1) - Masa bodi` | Warna Kabel: R - Masa bodi — Switch mesin | Switch mesin off: 10 kΩ atau lebih tinggi / Switch mesin on (IG): Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D35-9 (SSW2) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch mesin | Switch mesin off: 10 kΩ atau lebih tinggi / Switch mesin on (IG): Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] 4B-30 (BECU) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] 4D-9 (LIN1) - Masa bodi` | Warna Kabel: P - Masa bodi — Alur komunikasi LIN | Selalu: 10 kΩ atau lebih tinggi |
| `[ENGINE IMMOBILISER] D18-10 (CODE) - D18-8 (AGND)` | Warna Kabel: BE - BR — Sinyal demodulasi dari data kode kunci | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch mesin telah ditekan dan kunci dipegang dekat engine switch*: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] D28-9 (CODE) - D28-40 (AGND)` | Warna Kabel: BE - BR — Input KODE engine switch | Sistem engine immobiliser dalam posisi set (kunci tidak di dalam kabin): Di bawah 1 V / Switch mesin telah ditekan dan kunci dipegang dekat engine switch*: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] D24-5 (EFII) - D24-8 (GND)` | Warna Kabel: BE - W-B — Sinyal input ECM | Switch mesin off: Di bawah 1 V / Switch mesin on (IG): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] A20-10 (IMO) - A20-9 (EOM)` | Warna Kabel: BE - BR — Sinyal output ID kode box | Switch mesin off: Di bawah 1 V / Switch mesin on (IG): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] D35-1 (AM1) - Masa bodi` | Warna Kabel: BE - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D54-7 (AGND) - Masa bodi` | Warna Kabel: GR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D54-1 (VC5) - D54-7 (AGND)` | Warna Kabel: P- GR — Power source | 1: Tidak terdapat kunci dalam silinder kunci pengapian → 2: Kunci telah disisipkan: 1: 0 V → 2: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] D54-4 (CODE) - D54-7 (AGND)` | Warna Kabel: G- GR — Sinyal demodulasi dari data kode kunci | Tidak terdapat kunci dalam silinder kunci pengapian → Kunci telah disisipkan: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] D54-5 (TXCT) - D54-7 (AGND)` | Warna Kabel: V- GR — Sinyal output kode kunci | Tidak terdapat kunci dalam silinder kunci pengapian → Kunci telah disisipkan: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] D53-16 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] D53-1 (+B) - D53-16 (GND)` | Warna Kabel: L - W-B — Baterai | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D53-2 (IG) - D53-16 (GND)` | Warna Kabel: R - W-B — Switch pengapian | Switch pengapian 1: OFF → 2: Kunci telah disisipkan: 1: 0 V → 2: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] D53-3 (KSW) - D53-5 (AGND)` | Warna Kabel: O - GR — Switch peringatan unlock | 1: Tidak terdapat kunci dalam silinder kunci pengapian → 2: Kunci telah disisipkan: 1: 11 sampai 14 V→ 2: Di bawah 1 V |
| `[ENGINE IMMOBILISER] D53-14 (VC5) - D53-5 (AGND)` | Warna Kabel: P- GR — Power source | 1: Tidak terdapat kunci dalam silinder kunci pengapian → 2: Kunci telah disisipkan: 1: 0 V → 2: 4.6 sampai 5.4 V |
| `[ENGINE IMMOBILISER] D53-4 (TXCT) - D53-5 (AGND)` | Warna Kabel: V- GR — Sinyal komunikasi transponder kunci amplifier | Tidak terdapat kunci dalam silinder kunci pengapian → Kunci telah disisipkan: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] D53-15 (CODE) - D53-5 (AGND)` | Warna Kabel: G- GR — Sinyal komunikasi transponder kunci amplifier | Tidak terdapat kunci dalam silinder kunci pengapian → Kunci telah disisipkan: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] D53-13 (EFIO) - D53-16 (GND)` | Warna Kabel: W - W-B — Sinyal output ECM | Switch pengapian OFF → ON: Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[ENGINE IMMOBILISER] D53-12 (EFII) - D53-16 (GND)` | Warna Kabel: O - W-B — Sinyal input ECM | Switch pengapian OFF → ON: Pembangkitan pulsa (lihat bentuk gelombang 4) |
| `[ENGINE IMMOBILISER] D53-7 (CTY) - D53-16 (GND)` | Warna Kabel: B - W-B — Sinyal Courtesy | 1: Pintu sisi pengemudi terbuka → 2: tertutup: 1: 11 sampai 14 V → 2: Di bawah 1 V |
| `[ENGINE IMMOBILISER] D53-8 (IND) - D53-16 (GND)` | Warna Kabel: LG - W-B — Sinyal indikator keamanan | Sistem engine immobiliser 1: SET → 2: UNSET: 1: 3 sampai 5 V → 2: Di bawah 1 V |
| `[ENGINE IMMOBILISER] D53-9 (D) - D53-16 (GND)` | Warna Kabel: W - W-B — Komunikasi diagnosis tester | Switch pengapian ON: Pembangkitan pulsa |
| `[ENGINE IMMOBILISER] D53-5 (AGND) - D53-16 (GND)` | Warna Kabel: GR - W-B — Sirkuit masa amplifier | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] A20-11 (IMI) - A20-9 (EOM)` | Warna Kabel: W - BR — Sinyal input ECU kunci transponder | Tidak terdapat kunci dalam silinder kunci pengapian → Kunci telah disisipkan: Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[ENGINE IMMOBILISER] A20-10 (IMO) - A20-9 (EOM)` | Warna Kabel: O - BR — Sinyal output transponder kunci ECU | Tidak terdapat kunci dalam silinder kunci pengapian → Kunci telah disisipkan: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[ENGINE IMMOBILISER] D53-3 (KSW) - D53-5 (AGND)` | Warna Kabel: BE - GR — Switch peringatan unlock | 1: Tidak terdapat kunci dalam silinder kunci pengapian → 2: Kunci telah disisipkan: 1: 11 sampai 14 V→ 2: Di bawah 1 V |
| `[ENGINE IMMOBILISER] D53-12 (EFII) - D53-16 (GND)` | Warna Kabel: BE - W-B — Sinyal input ECM | Switch pengapian OFF → ON: Pembangkitan pulsa (lihat bentuk gelombang 4) |
| `[ENGINE IMMOBILISER] A20-10 (IMO) - A20-9 (EOM)` | Warna Kabel: BE - BR — Sinyal output transponder kunci ECU | Tidak terdapat kunci dalam silinder kunci pengapian → Kunci telah disisipkan: Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[PENERANGAN] 4B-30 (BECU) - 4E-17 (GND1)` | Warna Kabel: L - W-B — Baterai (Power supply) | Selalu: 11 sampai 14 V |
| `[PENERANGAN] 4E-17 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[PENERANGAN] D35-4 (GND2) * - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 V |
| `[PENERANGAN] 4A-21 (DCTY) - Masa bodi` | Warna Kabel: R - Masa bodi — Input switch lampu courtesy pintu pengemudi | Pintu pengemudi ditutup: 11 sampai 14 V / Pintu pengemudi terbuka: Di bawah 1 V |
| `[PENERANGAN] 4A-24 (PCTY) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch input lampu courtesy pintu penumpang depan | Pintu penumpang depan ditutup: 11 sampai 14 V / Pintu penumpang depan terbuka: Di bawah 1 V |
| `[PENERANGAN] 4A-20 (RRCY) - Masa bodi` | Warna Kabel: L - Masa bodi — Input switch lampu courtesy pintu belakang RH | Pintu belakang RH tertutup: 11 sampai 14 V / Pintu belakang RH terbuka: Di bawah 1 V |
| `[PENERANGAN] 4A-5 (RRCY) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu courtesy pintu belakang LH | Pintu belakang LH tertutup: 11 sampai 14 V / Pintu belakang LH terbuka: Di bawah 1 V |
| `[PENERANGAN] 4A-7 (BCTY) - Masa bodi` | Warna Kabel: SB - Masa bodi — Input switch luggage compartment door courtesy | Pintu kompartmen bagasi tertutup: 11 sampai 14 V / Pintu kompartmen bagasi terbuka: Di bawah 1 V |
| `[PENERANGAN] 4C-2 (PKB) - Masa bodi` | Warna Kabel: Y - Masa bodi — Input switch rem parkir | Switch rem parkir ON: Di bawah 1 V / Switch rem parkir OFF: 11 sampai 14 V |
| `[PENERANGAN] 4K-2 (ILE) - Masa bodi` | Warna Kabel: P - Masa bodi — Sinyal iluminasi (ke lampu ruangan assembly) | Switch lampu ruang dalam posisi DOOR, dan lampu ruangan menyala: 11 sampai 14 V / Switch lampu ruang dalam posisi OFF, dan lampu ruangan assembly padam: Di bawah 1 V |
| `[PENERANGAN] D35-8 (SWIL) * - D35-4 (GND2) *` | Warna Kabel: LG * - W-B * — Sinyal Illuminasi (ke iluminasi switch pengapian) | Switch kontrol lampu TAIL atau HEAD: 11 sampai 14 V / Switch kontrol lampu OFF: Di bawah 1 V |
| `[PENERANGAN] A21-1 (IG) - Masa bodi` | Warna Kabel: V - Masa bodi — Power supply IG | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[PENERANGAN] A21-9 (E1) - Masa bodi` | Warna Kabel: W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[PENERANGAN] A21-21 (SGR) - Masa bodi` | Warna Kabel: R - Masa bodi — Masa sensor kontrol ketinggian belakang | Selalu: Di bawah 1 Ω |
| `[PENERANGAN] A21-23 (RH-) - Masa bodi` | Warna Kabel: BR - Masa bodi — Ground leveling motor RH | Selalu: Di bawah 1 Ω |
| `[PENERANGAN] A21-24 (LH-) - Masa bodi` | Warna Kabel: LG - Masa bodi — Ground leveling motor LH | Selalu: Di bawah 1 Ω |
| `[PENERANGAN] A21-3 (B2) - Masa bodi` | Warna Kabel: O - Masa bodi — Input sinyal low beam headlight | Low beam headlight ON.: Di bawah 1.5 V / Low beam headlight OFF: 11 sampai 14 V |
| `[PENERANGAN] A21-5 (PRST) - Masa bodi` | Warna Kabel: B - Masa bodi — Input sinyal inisialisasi | Terminal OP3 dan terminal GND dari DLC3 terhubung: Di bawah 1 V / Terminal OP3 dan terminal GND dari DLC3 tidak terhubung: 11 sampai 14 V |
| `[PENERANGAN] A21-6 (WNG) - Masa bodi` | Warna Kabel: SB - Masa bodi — Drive output indikaotr peringatan | Indikator peringatan ON: 11 sampai 14 V / Indikator peringatan OFF: Di bawah 1 V |
| `[PENERANGAN] A21-10 (RH+) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply leveling motor RH | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[PENERANGAN] A21-11 (LH+) - Masa bodi` | Warna Kabel: G - Masa bodi — Power supply leveling motor LH | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[PENERANGAN] A21-12 (SBR) - Masa bodi` | Warna Kabel: P - Masa bodi — Power supply sensor kontrol tinggi belakang | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[PENERANGAN] A21-16 (SPDR) - A21-9 (E1)` | Warna Kabel: GR - W — Input sinyal kecepatan kendaraan | Dikendarai pada 20 km/jam (12 mph): Pembangkitan pulsa (Lihat bentuk gelombang 1) |
| `[PENERANGAN] A21-17 (RHT) - Masa bodi` | Warna Kabel: W - Masa bodi — Input sinyal kerja leveling motor RH | Dengan low beam headlight ON, tinggi kendaraan tidak berubah: Di bawah 1 V / Dengan low beam headlight ON, ubah tinggi kendaraan dan jaga selama lebih dari 3 detik.: 1.1 sampai 12.6 V |
| `[PENERANGAN] A21-18 (LHT) - Masa bodi` | Warna Kabel: R - Masa bodi — Input sinyal kerja leveling motor LH | Dengan low beam headlight ON, tinggi kendaraan tidak berubah: Di bawah 1 V / Dengan low beam headlight ON, ubah tinggi kendaraan dan jaga selama lebih dari 3 detik.: 1.1 sampai 12.6 V |
| `[PENERANGAN] A21-19 (SHRL) - Masa bodi` | Warna Kabel: G - Masa bodi — Input sinyal sensor kontrol tinggi belakang | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 0.5 sampai 4.5 V |
| `[PENERANGAN] A21-3 (B2) - Masa bodi` | Warna Kabel: BE - Masa bodi — Input sinyal low beam headlight | Low beam headlight ON.: Di bawah 1.5 V / Low beam headlight OFF: 11 sampai 14 V |
| `[DOOR LOCK] 4B-30 (BECU) *1 - 4E-17 (GND1)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] 4E-17 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] 4D-7 (KSW) *2 - 4E-17 (GND1)` | Warna Kabel: Y - W-B — Input switch peringatan unlock kunci | Kunci telah disisipkan: 0 V / Tidak terdapat kunci dalam silinder kunci pengapian: 11 sampai 14 |
| `[DOOR LOCK] 4A-21 (DCTY) - Masa bodi` | Warna Kabel: R - Masa bodi — Input switch lampu courtesy pintu pengemudi | Pintu sisi pengemudi tertutup: 11 sampai 14 V / Pintu samping pengemudi terbuka: 0 V |
| `[DOOR LOCK] 4A-24 (PCTY) - Masa bodi` | Warna Kabel: L - Masa bodi — Input switch lampu courtesy pintu sisi penumpang | Pintu sisi penumpang tertutup: 11 sampai 14 V / Pintu samping penumpang terbuka: 0 V |
| `[DOOR LOCK] 4A-20 (RRCY) - Masa bodi` | Warna Kabel: L - Masa bodi — Input switch lampu courtesy pintu belakang RH | Pintu belakang RH tertutup: 11 sampai 14 V / Pintu belakang RH terbuka: 0 V |
| `[DOOR LOCK] 4A-5 (RRCY) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu courtesy pintu belakang LH | Pintu belakang LH tertutup: 11 sampai 14 V / Pintu belakang LH terbuka: 0 V |
| `[DOOR LOCK] 4A-7 (BCTY) - Masa bodi` | Warna Kabel: SB - Masa bodi — Switch input lampu courtesy pintu bagasi kompartmen. | Pintu kompartmen bagasi tertutup: 11 sampai 14 V / Pintu kompartmen bagasi terbuka: 0 V |
| `[DOOR LOCK] 4H-4 (L1) - Masa bodi` | Warna Kabel: LG - Masa bodi — Input penguncian switch lampu kontrol door lock | Switch kontrol pintu OFF: 11 sampai 14 V / Switch kontrol pintu ON (LOCK): 0 V |
| `[DOOR LOCK] 4H-5 (UL1) - Masa bodi` | Warna Kabel: O - Masa bodi — Input unlock switch kontrol pintu | Switch kontrol pintu OFF: 11 sampai 14 V / Switch kontrol pintu ON (UNLOCK): 0 V |
| `[DOOR LOCK] 4H-17 (ACT+) - Masa bodi` | Warna Kabel: W - Masa bodi — Output penggerak LOCK motor door lock (Semua pintu) | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF→LOCK→OFF: 11 sampai 14V → Di bawah 1V → 11 sampai 14V |
| `[DOOR LOCK] 4H-8 (ACT+) - Masa bodi` | Warna Kabel: O - Masa bodi — Output penggerak LOCK motor door lock (Semua pintu) | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF→LOCK→OFF: 11 sampai 14V → Di bawah 1V → 11 sampai 14V |
| `[DOOR LOCK] 4A-3 (ACT+) - Masa bodi` | Warna Kabel: GR - Masa bodi — Output penggerak LOCK motor door lock (Semua pintu) | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF→LOCK→OFF: 11 sampai 14V → Di bawah 1V → 11 sampai 14V |
| `[DOOR LOCK] 4H-9 (ACT-) - Masa bodi` | Warna Kabel: SB - Masa bodi — Output penggerak UNLOCK motor door lock (Semua pintu) | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF→LOCK→OFF: 11 sampai 14V → Di bawah 1V → 11 sampai 14V |
| `[DOOR LOCK] 4H-18 (ACT-) - Masa bodi` | Warna Kabel: P - Masa bodi — Output penggerak UNLOCK motor door lock (Semua pintu) | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF→LOCK→OFF: 11 sampai 14V → Di bawah 1V → 11 sampai 14V |
| `[DOOR LOCK] 4A-4 (ACT-) - Masa bodi` | Warna Kabel: P - Masa bodi — Output penggerak UNLOCK motor door lock (Semua pintu) | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF→LOCK→OFF: 11 sampai 14V → Di bawah 1V → 11 sampai 14V |
| `[DOOR LOCK] D34-25 (LSWD) - Masa bodi *1` | Warna Kabel: L - Masa bodi — Input switch posisi door lock sisi pengemudi | Pintu sisi pengemudi UNLOCK: 0 V / Pintu sisi pengemudi LOCK: 11 sampai 14 V |
| `[DOOR LOCK] D33-21 (LSWD) - Masa bodi *2` | Warna Kabel: L - Masa bodi — Input switch posisi door lock sisi pengemudi | Pintu sisi pengemudi UNLOCK: 0 V / Pintu sisi pengemudi LOCK: 11 sampai 14 V |
| `[DOOR LOCK] D34-10 (LSWP) - Masa bodi *1` | Warna Kabel: L - Masa bodi — Input switch posisi door lock sisi penumpang | Pintu sisi penumpang UNLOCK: 0 V / Pintu sisi penumpang LOCK: 11 sampai 14 V |
| `[DOOR LOCK] D33-5 (LSWP) - Masa bodi *2` | Warna Kabel: L - Masa bodi — Input switch posisi door lock sisi penumpang | Pintu sisi penumpang UNLOCK: 0 V / Pintu sisi penumpang LOCK: 11 sampai 14 V |
| `[DOOR LOCK] 4H-7 (L2) - Masa bodi` | Warna Kabel: BR - Masa bodi — Input key-linked switch pintu sisi pengemudi | Silinder kunci pintu sisi pengemudi OFF: 11 sampai 14 V / Silinder kunci pintu sisi pengemudi ON (UNLOCK): 0 V |
| `[DOOR LOCK] 4H-16 (L2) - Masa bodi *2` | Warna Kabel: B - Masa bodi — Input key-linked switch pintu sisi penumpang | Silinder kunci pintu sisi penumpang OFF: 11 sampai 14 V / Silinder kunci pintu sisi penumpang ON (UNLOCK): 0 V |
| `[DOOR LOCK] 4H-6 (UL2) - Masa bodi` | Warna Kabel: G - Masa bodi — Input key-linked switch pintu sisi pengemudi | Silinder kunci pintu sisi pengemudi OFF: 11 sampai 14 V / Silinder kunci pintu sisi pengemudi ON (UNLOCK): 0 V |
| `[DOOR LOCK] 4H-15 (UL2) - Masa bodi *2` | Warna Kabel: Y - Masa bodi — Input key-linked switch pintu sisi penumpang | Silinder kunci pintu sisi penumpang OFF: 11 sampai 14 V / Silinder kunci pintu sisi penumpang ON (UNLOCK): 0 V |
| `[DOOR LOCK] 4H-5 (UL1) - Masa bodi` | Warna Kabel: BE - Masa bodi — Input unlock switch kontrol pintu | Switch kontrol pintu OFF: 11 sampai 14 V / Switch kontrol pintu ON (UNLOCK): 0 V |
| `[DOOR LOCK] 4H-8 (ACT+) - Masa bodi` | Warna Kabel: BE - Masa bodi — Output penggerak LOCK motor door lock (Semua pintu) | Switch kontrol pintu atau silinder kunci pintu sisi pengemudi OFF→LOCK→OFF: 11 sampai 14V → Di bawah 1V → 11 sampai 14V |
| `[DOOR LOCK] 4B-30 (BECU) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] 4A-20 (RRCY) - Masa bodi` | Warna Kabel: L - Masa bodi — Switch input lampu courtesy belakang RH | Pintu belakang RH TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[DOOR LOCK] 4A-5 (RRCY) - Masa bodi` | Warna Kabel: G - Masa bodi — Input switch lampu courtesy belakang LH | Pintu belakang LH TERTUTUP (OFF) → TERBUKA (ON): 10 kΩ atau lebih tinggi → Di bawah 1 Ω |
| `[DOOR LOCK] 4S-6 (ACC) - Masa bodi` | Warna Kabel: GR - Masa bodi — Power supply pengapian (Sinyal ACC) | Switch mesin on (ACC) → off: 11 sampai 14 V → Dibawah 1 V |
| `[DOOR LOCK] 4S-7 (IG) - Masa bodi` | Warna Kabel: R - Masa bodi — Power supply pengapian (Sinyal IG) | Switch mesin on (IG) → off: 11 sampai 14 V → Dibawah 1 V |
| `[DOOR LOCK] 4G-1 (ALTB) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply +B (sistem power untuk sistem alternator) | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] D35-4 (GND2) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] 4S-8 (HAZ) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal relay flasher tanda belok | Switch transmitter manapun ditekan → tidak ditekan: Di bawah 1 V → 11 sampai 14 V *1 |
| `[DOOR LOCK] D34-1 (TR+) - Masa bodi` | Warna Kabel: O - Masa bodi — Motor pembuka pintu kompartemen bagasi | Pintu kompartemen bagasi CLOSED (LOCKED) → OPEN (UNLOCKED): Di bawah 1 V → 11 sampai 14 V *2 |
| `[DOOR LOCK] D28-1 (+B) - D28-17 (E)` | Warna Kabel: B - W-B — Power supply baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] D28-17 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] D28-18 (IG) - D28-17 (E)` | Warna Kabel: BR - W-B — Power supply IG | Switch mesin on (IG): 11 sampai 14 V / Switch mesin off: Di bawah 1 V |
| `[DOOR LOCK] D28-29 (RC0) - D28-17 (E)` | Warna Kabel: L - W-B — Power source receiver kontrol pintu. | Engine switch off, semua pintu ditutup dan switch transmitter tidak ditekan.: Di bawah 1 V / Engine switch off, semua pintu ditutup dan switch transmitter ditekan.: 4.6 sampai 5.4 V |
| `[DOOR LOCK] D28-38 (RDA) - D28-17 (E)` | Warna Kabel: R - W-B — Sinyal output receiver kontrol pintu | Sinyal output receiver kontrol pintu: 11 sampai 14 V / Sinyal output receiver kontrol pintu: Pembangkitan pulsa |
| `[DOOR LOCK] D34-1 (TR+) - Masa bodi` | Warna Kabel: BE - Masa bodi — Motor pembuka pintu kompartemen bagasi | Pintu kompartemen bagasi CLOSED (LOCKED) → OPEN (UNLOCKED): Di bawah 1 V → 11 sampai 14 V *2 |
| `[DOOR LOCK] 4B-30 (BECU) - 4E-17 (GND1)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] 4D-7 (KSW) -4E-17 (GND1)` | Warna Kabel: Y - W-B — Input switch peringatan unlock kunci | Kunci telah disisipkan: 0 V / Tidak terdapat kunci dalam silinder kunci pengapian: 11 sampai 14 V |
| `[DOOR LOCK] 4A-7 (BCTY) - Masa bodi` | Warna Kabel: SB - Masa bodi — Input switch lampu courtesy pintu bagasi | Pintu bagasi tertutup: 11 sampai 14 V / Pintu bagasi terbuka: 0 V |
| `[DOOR LOCK] D33-17 (PRG) - Masa bodi` | Warna Kabel: W - Masa bodi — Output receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): Pembangkitan pulsa (lihat bentuk gelombang 1) |
| `[DOOR LOCK] E33-16 (RDA) - Masa bodi` | Warna Kabel: R - Masa bodi — Input receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): Pembangkitan pulsa (lihat bentuk gelombang 2) |
| `[DOOR LOCK] 4S-17 (HAZ) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal lampu peringatan hazard | Answer-back ON: Pembangkitan pulsa / Answer-back OFF: 11 sampai 14 V |
| `[DOOR LOCK] J13-5 (+B) - J13-1 (GND)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] J13-1 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] J13-3 (PRG) - Masa bodi` | Warna Kabel: W - Masa bodi — Output receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): Pembangkitan pulsa (lihat bentuk gelombang 3) |
| `[DOOR LOCK] J13-2 (RDA) - Masa bodi` | Warna Kabel: R - Masa bodi — Input receiver kontrol pintu. | Switch transmitter ON OFF (Tidak ada kunci dalam silinder kunci pengapian, semua pintu ditutup): Pembangkitan pulsa (lihat bentuk gelombang 4) |
| `[DOOR LOCK] D28-1 (+B) - Masa bodi` | Warna Kabel: B - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] D28-3 (TSW1) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal switch kunci entry (sisi pengemudi) | Switch lock depan tidak ditekan: 10 kΩ atau lebih tinggi / Switch lock depan ditekan: Di bawah 1 Ω |
| `[DOOR LOCK] D28-7 (TSW5) - Masa bodi` | Warna Kabel: BR - Masa bodi — Sinyal switch luar pembuka pintu kompartemen bagasi | Switch pembuka OFF: 10 kΩ atau lebih tinggi / Switch pembuka ON: Di bawah 1 Ω |
| `[DOOR LOCK] D28-10 (LIN) - Masa bodi` | Warna Kabel: P - Masa bodi — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] D28-27 (CANH) - Masa bodi` | Warna Kabel: GR - Masa bodi — Alur CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] D28-28 (CANH) - Masa bodi` | Warna Kabel: W - Masa bodi — Alur CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] D28-40 (AGND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] D28-18 (IG) - Masa bodi` | Warna Kabel: BR - Masa bodi — Power supply pengapian | Switch mesin off: Di bawah 1 V / Switch mesin on (IG): 11 sampai 14 V |
| `[DOOR LOCK] D28-19 (ACC) - Masa bodi` | Warna Kabel: Y - Masa bodi — Power supply ACC | Switch mesin off: Di bawah 1 V / Switch mesin on (ACC): 11 sampai 14 V |
| `[DOOR LOCK] D28-33 (CLG1) - D28-17 (E)` | Warna Kabel: GR - W-B — Oscillator Kunci Elektrik Pintu (sisi pengemudi) sinyal sensor | Semua pintu tertutup, semua pintu terkunci dan engine switch off: Alternator antara 5 V dan di bawah 1 V / Pintu tidak dikunci atau pintu terbuka: Di bawah 1 V |
| `[DOOR LOCK] D28-22 (SEN1) - D28-17 (E)` | Warna Kabel: R - W-B — Sinyal pendeteksian sensor sentuh (sisi pengemudi) | Menyentuh handel pintu sisi luar: Di bawah 1 V / Handel pintu luar tidak disentuh (Letakkan kunci elektrik keluar kabin ): 11 sampai 14 V |
| `[DOOR LOCK] D28-5 (SEL1) - D28-17 (E)` | Warna Kabel: R - W-B — Sinyal kontrol aktifasi sensor sentuh (sisi pengemudi) | Jauhkan kunci elektrik lebih dari 5 m (16.4 ft) dari pintu depan: 11 sampai 14 V / Gerakkan kunci elektrik ke handel luar: Di bawah 1 V |
| `[DOOR LOCK] D28-11 (CLG5) - D28-12 (CG5B)` | Warna Kabel: LG - G — Oscillator Kunci Elektrik Indoor (depan) sinyal sensor | Dalam 30 detik pintu pengemudi terbuka dan tertutup, switch pengapian off: Alternator antara 5 V dan di bawah -5 V / Switch mesin on (IG): Di bawah 1 V |
| `[DOOR LOCK] D28-13 (CLG6) - D28-14 (CG6B)` | Warna Kabel: V - P — Oscillator Kunci Elektrik Indoor (belakang) sinyal sensor | Dalam 30 detik pintu pengemudi terbuka dan tertutup, engine switch off: Alternator antara 5 V dan di bawah -5 V / Switch mesin on (IG): Di bawah 1 V |
| `[DOOR LOCK] D28-15 (CLG7) - D28-16 (CG7B)` | Warna Kabel: O - W — Oscillator Kunci Elektrik Indoor (kompartemen bagasi) sinyal sensor | Switch pembuka pintu kompartemen bagasi ON: Alternator antara 5 V dan di bawah -5 V / Switch pembuka pintu kompartemen bagasi OFF: Di bawah 1 V |
| `[DOOR LOCK] D28-31 (CLG8) - D28-32 (CG8B)` | Warna Kabel: LG - SB — Oscillator Kunci Elektrik Luar (kompartemen bagasi) sinyal sensor | Switch pembuka pintu kompartemen bagasi ON: Alternator antara 5 V dan di bawah -5 V / Switch pembuka pintu kompartemen bagasi OFF: Di bawah 1 V |
| `[DOOR LOCK] D28-29 (RC0) - D28-17 (E)` | Warna Kabel: L - W-B — Power source receiver kontrol pintu entry. | Engine switch off, semua pintu ditutup dan switch kunci elektronik on.: 4.5 sampai 5.5 V / Engine switch off, semua pintu ditutup dan switch kunci elektronik off.: Di bawah 1 V |
| `[DOOR LOCK] D28-39 (RSSI) - D28-17 (E)` | Warna Kabel: W - W-B — Sinyal keberadaan gelombang elektrik penerima kontrol pintu entry | Engine switch off, semua pintu tertutup , kunci elektrik tidak dalam area pendeteksian.: 11 sampai 14 V / Engine switch off, semua pintu tertutup ,dan kunci elektrik dalam area pendeteksian.: Di bawah 1 V |
| `[DOOR LOCK] D28-38 (RDA) - D28-17 (E)` | Warna Kabel: R - W-B — Sinyal input data receiver kontrol pintu entry | Engine switch off, semua pintu ditutup dan switch kunci elektronik off.: 11 sampai 14 V (Pembangkitan pulsa) / Engine switch off, semua pintu ditutup dan switch kunci elektronik on.: Pembangkitan pulsa / Engine switch of |
| `[DOOR LOCK] D28-37 (ASEL) - Masa bodi` | Warna Kabel: LG - Masa bodi — Sinyal memilih receiver kabin/barang | Engine switch off, pintu kompartemen bagasi tertutup dan kunci elektrik dalam area pendeteksian.: 4.6 sampai 6.0 V / Engine switch off, pintu kompartemen bagasi terbuka: Di bawah 1 V |
| `[DOOR LOCK] D28-21 (BZR) - Masa bodi` | Warna Kabel: GR - Masa bodi — Sinyal buzzer wireless door lock | Buzzer Door Lock Wireless OFF: Di bawah 1 V / Buzzer Door Lock Wireless ON: Pembangkitan pulsa |
| `[DOOR LOCK] D35-1 (AM1) - Masa bodi` | Warna Kabel: O - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] D34-6 (AM2) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] D34-14 (STP) - Masa bodi` | Warna Kabel: G - Masa bodi — Sinyal switch lampu rem | Pedal rem ditekan: 11 sampai 14 V / Pedal rem dibebaskan: Di bawah 1 V |
| `[DOOR LOCK] D36-15 (CANH) - Masa Bodi` | Warna Kabel: R - Masa bodi — Line CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] D36-16 (CANL) - Masa bodi` | Warna Kabel: W - Masa bodi — Line CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] 4D-9 (LIN1) - Masa bodi` | Warna Kabel: P - Masa bodi — LIN line | Selalu: 10 kΩ atau lebih tinggi |
| `[DOOR LOCK] D28-15 (CLG7) - D28-16 (CG7B)` | Warna Kabel: BE - W — Oscillator Kunci Elektrik Indoor (kompartemen bagasi) sinyal sensor | Switch pembuka pintu kompartemen bagasi ON: Alternator antara 5 V dan di bawah -5 V / Switch pembuka pintu kompartemen bagasi OFF: Di bawah 1 V |
| `[DOOR LOCK] D35-1 (AM1) - Masa bodi` | Warna Kabel: BE - Masa bodi — Power supply +B | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] D1-1 (IG2) - Masa bodi` | Warna Kabel: B - Masa bodi — Sinyal switch pengapian | Switch pengapian OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[DOOR LOCK] D1-2 (BECU) - Masa bodi` | Warna Kabel: L - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] D1-20 (CANH) - Masa bodi` | Warna Kabel: G - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[DOOR LOCK] D1-21 (CANL) - Masa bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[DOOR LOCK] D1-24 (ET) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] 4D-7 (KSW) - Masa bodi` | Warna Kabel: Y - Masa bodi — Input switch peringatan unlock kunci | Kunci telah dimasukkan Kunci dicabut dari silinder kunci pengapian.: Di bawah 1 V → 11 sampai 14V |
| `[DOOR LOCK] 4B-30 (BECU) - Masa bodi` | Warna Kabel: L - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[DOOR LOCK] 4A-21 (DTCY) - Masa bodi` | Warna Kabel: R - Masa bodi — Input switch courtesy pintu pengemudi | Pintu pengemudi ditutup → dibuka: 11 sampai 14 V → Dibawah 1 V |
| `[DOOR LOCK] D33-22 (CANL) - Masa Bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[DOOR LOCK] D33-23 (CANH)- Masa Bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Switch pengapian ON: Pembangkitan pulsa |
| `[METER] D2-3 (ODO) - Masa bodi` | Warna Kabel: L - Masa bodi — Sinyal switch ODO/TRIP | Switch pengapian on (IG): 5 V |
| `[METER] D2-5 (LVWG) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal lampu indikator kontrol level headlight beam | Switch pengapian on (IG) Lampu indikator LEVELING ON→OFF: Dibawah 1 V →11 sampai 14 V |
| `[METER] D2-6 (CLK) - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal switch jam | Switch pengapian on (ACC): 5 V |
| `[METER] D2-7 (S) - Masa bodi` | Warna Kabel: Y - Masa bodi — Sinyal tekanan oli mesin | Lampu peringatan tekanan oli mesin ON→OFF: Dibawah 1 V→11 sampai 14 V |
| `[METER] D2-8 (E1) - Masa bodi` | Warna Kabel: GR - Masa bodi — Masa | Switch pengapian on (IG): Di bawah 1 V |
| `[METER] D2-9 (-) - Masa bodi` | Warna Kabel: P - Masa bodi — Sinyal indikator HI-BEAM | Lampu indikator Hi beam ON→OFF: Dibawah 1 V →11 sampai 14 V |
| `[METER] D2-11 (-)*1 - Masa bodi` | Warna Kabel: SB - Masa bodi — Sinyal kabut belakang | Lampu kabut belakang OFF → ON: Dibawah 1 V →11 sampai 14 V |
| `[METER] D2-12 (FOG)*2 - Masa bodi` | Warna Kabel: R - Masa bodi — Sinyal kabut depan | Lampu kabut depan OFF → ON: Dibawah 1 V →11 sampai 14 V |
| `[METER] D2-13 (B) - Masa bodi` | Warna Kabel: LG - Masa bodi — Tanda belok kiri | Lampu indikator belok kiri OFF → ON: Dibawah 1 V →11 sampai 14 V |
| `[METER] D2-14 (+) - Masa bodi` | Warna Kabel: GR - Masa bodi — Sinyal Hi beam | Selalu: 11 sampai 14 V |
| `[METER] D2-15 (B) - Masa bodi` | Warna Kabel: BR - Masa bodi — Tanda belok kanan | Lampu indikator belok kanan OFF → ON: Dibawah 1 V →11 sampai 14 V |
| `[METER] D2-16 (IND) - Masa bodi` | Warna Kabel: G - Masa bodi — Indikator lampu belakang | Switch dimmer headlight (Tail) OFF → ON: 11 sampai 14 V → Dibawah 1V |
| `[METER] RRCY (4A-5) - GND1 (4E-17)` | Warna Kabel: G - W-B — Sinyal switch lampu courtesy pintu belakang (LH) | Pintu Belakang (LH) TUTUP→ BUKA: 11 sampai 14 V → Dibawah 1 V / Pintu belakang (LH) TUTUP→ BUKA: 11 sampai 14 V → Dibawah 1 V |
| `[METER] RRCY (4A-20) - GND1 (4E-17)` | Warna Kabel: L - W-B — Sinyal switch lampu courtesy pintu belakang (RH) | Pintu belakang (RH) TUTUP→ BUKA: 11 sampai 14 V → Dibawah 1 V / Pintu belakang (RH) TUTUP →BUKA: 11 sampai 14 V → Dibawah 1 V |
| `[METER] DCTY (4A-21) - GND1 (4E-17)` | Warna Kabel: R - W-B — Sinyal switch lampu courtesy pintu depan (Sisi pengemudi) | Pintu depan (Sisi Pengemudi) TUTUP→ BUKA: 11 sampai 14 V → Dibawah 1 V / Pintu depan (Sisi pengemudi) TUTUP →BUKA: 11 sampai 14 V → Dibawah 1 V |
| `[METER] PCTY (4A-24) - GND1 (4E-17)` | Warna Kabel: L - W-B — Sinyal switch lampu courtesy pintu depan (Sisi Penumpang) | Pintu depan (Sisi Penumpang) TUTUP→BUKA: 11 sampai 14 V → Dibawah 1 V |
| `[METER] PKB (4C-2) - GND1 (4E-17)` | Warna Kabel: Y - W-B — Sinyal rem parkir | Lampu peringatan rem parkir ON→OFF: Dibawah 1 V→11 sampai 14 V |
| `[METER] KSW (4D-7) - GND1 (4E-17)` | Warna Kabel: Y - W-B — Input switch peringatan unlock kunci | Kunci dimasukkan→Dicabut: Dibawah 1 V→11 sampai 14 V |
| `[METER] GND1 (4E-17) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER] CANH (D36-15) - Masa bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] CANL (D36-16) - Masa bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] DBKL (D34-26) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal kondisi seat belt (Sisi pengemudi) | Lampu peringatan seat belt pengemudi OFF→ON: 11 sampai 14 V → Dibawah 1 V |
| `[METER] CANL (D33-22) - Masa bodi` | Warna Kabel: W - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] CANH (D33-23) - Masa bodi` | Warna Kabel: R - Masa bodi — Line komunikasi CAN | Switch pengapian on (IG): Pembangkitan pulsa |
| `[METER] DBKL(D33-9) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal kondisi seat belt (Sisi pengemudi) | Lampu peringatan seat belt pengemudi OFF→ON: 11 sampai 14 V → Dibawah 1 V |
| `[AUDIO / VISUAL] D9-7 (GND) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[AUDIO / VISUAL] D9-3 (ACC) - D9-7 (GND)` | Warna Kabel: GR - W-B — Power supply ACC | Switch Pengapian ACC: 11 sampai 14 V |
| `[AUDIO / VISUAL] D9-4 (B) - D9-7 (GND)` | Warna Kabel: L - W-B — Power supply baterai | Selalu: 11 sampai 14 V |
| `[AUDIO / VISUAL] D9-1 (FR+) - D9-7 (GND)` | Warna Kabel: GR - W-B — Sinyal suara (kanan depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D9-2 (FL+) - D9-7 (GND)` | Warna Kabel: P - W-B — Sinyal suara (kiri depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D9-5 (FR-) - D9-7 (GND)` | Warna Kabel: Y - W-B — Sinyal suara (kanan depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D9-6 (FL-) - D9-7 (GND)` | Warna Kabel: V - W-B — Sinyal suara (kiri depan) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-1 (RR+)*3 - D9-7 (GND)` | Warna Kabel: R - W-B — Sinyal suara (kanan belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-2 (RL+)*3 - D9-7 (GND)` | Warna Kabel: B - W-B — Sinyal suara (kiri belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-3 (RR-)*3 - D9-7 (GND)` | Warna Kabel: W - W-B — Sinyal suara (kanan belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D10-6 (RL-)*3 - D9-7 (GND)` | Warna Kabel: Y - W-B — Sinyal suara (kiri belakang) | Kerja sistem audio: Bentuk gelombang disamakan dengan output suara |
| `[AUDIO / VISUAL] D9-8 (ANT) - D9-7 (GND)` | Warna Kabel: B - W-B — Power source antena | Switch radio ON (AM atau FM): 11 sampai 14 V |
| `[AUDIO / VISUAL] D11-3 (SPD)*2 - D9-7 (GND)` | Warna Kabel: G - W-B — Sinyal kecepatan | Switch pengapian ON, putar roda perlahan-lahan: Pembangkitan pulsa |
| `[AUDIO / VISUAL] D11-6 (SWG)*1 - D9-7 (GND)` | Warna Kabel: LG - W-B — Masa switch steering pad | Selalu: Di bawah 1 V |
| `[AUDIO / VISUAL] D11-7 (SW1)*1 - D9-7 (GND)` | Warna Kabel: P - W-B — Sinyal switch steering pad | Switch steering pad tidak bekerja → Switch SEEK+ ditekan → Switch SEEK- ditekan → Switch VOL+ ditekan → switch VOL- ditekan: 4 V atau lebih tinggi → Sekitar 0.5 V → Sekitar 0.9 V → Sekitar 2.0 V → Sekitar 3.4 V |
| `[AUDIO / VISUAL] D11-8 (SW2)*1 - D9-7 (GND)` | Warna Kabel: O - W-B — Sinyal switch steering pad | Switch steering pad tidak dioperasikan → switch MODE ditekan: 4 V atau lebih → Di bawah 2.5 V |
| `[AUDIO / VISUAL] D11-8 (SW2)*1 - D9-7 (GND)` | Warna Kabel: BE - W-B — Sinyal switch steering pad | Switch steering pad tidak dioperasikan → switch MODE ditekan: 4 V atau lebih → Di bawah 2.5 V |
| `[AUDIO / VISUAL] D76-3 (SPD)*2 - D9-7 (GND)` | Warna Kabel: G - W-B — Sinyal kecepatan | Switch pengapian ON, putar roda perlahan-lahan: Pembangkitan pulsa |
| `[AUDIO / VISUAL] D76-6 (SWG)*1 - D9-7 (GND)` | Warna Kabel: LG - W-B — Masa switch steering pad | Selalu: Di bawah 1 V |
| `[AUDIO / VISUAL] D76-7 (SW1)*1 - D9-7 (GND)` | Warna Kabel: P - W-B — Sinyal switch steering pad | Switch steering pad tidak bekerja → Switch SEEK+ ditekan → Switch SEEK- ditekan → Switch VOL+ ditekan → switch VOL- ditekan: 5 V atau lebih tinggi → Sekitar 0.6 V → Sekitar 1.4 V → Sekitar 2.3 V → Sekitar 3.6 V |
| `[AUDIO / VISUAL] D76-8 (SW2)*1 - D9-7 (GND)` | Warna Kabel: BE - W-B — Sinyal switch steering pad | Switch steering pad tidak dioperasikan → switch MODE ditekan: 4 V atau lebih → Di bawah 2.5 V |
| `[AUDIO / VISUAL] D76-15 (ARI)*4 - D9-7 (GND)` | Warna Kabel: R - W-B — Sinyal suara (Kanan) | Memainkan peralatan eksternal (Bila stereo jack digunakan): Bentuk gelombang disinkronkan dengan suara yang di-output |
| `[AUDIO / VISUAL] D76-16 (ASGN)*4 - D9-7 (GND)` | Warna Kabel: B - W-B — Masa stereo jack adapter | Selalu: Di bawah 1 V |
| `[AUDIO / VISUAL] D76-17 (ALI)*4 - D9-7 (GND)` | Warna Kabel: W - W-B — Sinyal suara (Kiri) | Memainkan peralatan eksternal (Bila stereo jack digunakan): Bentuk gelombang disinkronkan dengan suara yang di-output |
| `[AUDIO / VISUAL] D76-18 (AGND)*4 - D9-7 (GND)` | Warna Kabel: Shield - W-B — Masa Pelindung | Selalu: Di bawah 1 V |
| `[AUDIO / VISUAL] D76-19 (AUXI)*4 - D9-7 (GND)` | Warna Kabel: R - W-B — Sinyal deteksi hubungan peralatan eksternal | Peralatan eksternal dihubungkan: 2.1 sampai 3 V |
| `[KACA DEPAN / KACA JENDELA] F3-1 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] F3-2 (+B) - F3-1 (E)` | Warna Kabel: LG - W-B — Power supply baterai | Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] F3-10 (U) - F3-1 (E)` | Warna Kabel: R - W-B — Motor power window pintu sisi pengemudi UP | Switch pengapian menyala (IG), switch power window pengemudi → UP (cara kerja manual) → power window sisi pengemudi tertutup sepenuhnya.: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] F3-7 (D) - F3-1 (E)` | Warna Kabel: G - W-B — Motor power window pintu sisi pengemudi DOWN | Switch pengapian on (IG), switch power window sisi pengemudi OFF → DOWN (pengoperasian manual) → power window sisi pengemudi terbuka sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] F3-5 (LED) - F3-1 (E)` | Warna Kabel: W - W-B — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] F1-9 (E) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] F1-6 (B) - Masa bodi` | Warna Kabel: GR - Masa bodi — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[KACA DEPAN / KACA JENDELA] F1-1 (U) - F1-9 (E)` | Warna Kabel: R - W-B — Output motor power window pintu sisi pengemudi UP | Switch pengapian menyala (IG), switch power window pengemudi OFF: 11 sampai 14 V / Switch pengapian menyala (IG), switch power window pengemudi → UP (cara kerja manual) → power window sisi pengemudi tertutup sepenuhnya.: |
| `[KACA DEPAN / KACA JENDELA] F1-5 (D) - F1-9 (E)` | Warna Kabel: G - W-B — Output motor power window pintu sisi pengemudi DOWN | Switch pengapian on (IG), switch power window sisi pengemudi OFF → DOWN (pengoperasian manual) → power window sisi pengemudi terbuka sepenuhnya: 11 sampai 14 V → Di bawah 1 V → 11 sampai 14 V / Switch pengapian on (IG),  |
| `[KACA DEPAN / KACA JENDELA] G1-3 (B) - Masa bodi` | Warna Kabel: L - Masa bodi — Power supply pengapian | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] G1-4 (U) - Masa bodi` | Warna Kabel: R - Masa bodi — Output motor power window pintu sisi penumpang UP | Switch pengapian on (IG), switch power window OFF → UP: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] G1-1(D) - Bodi masa` | Warna Kabel: G - Masa bodi — Output motor power window pintu sisi penumpang DOWN | Switch pengapian on (IG), switch power window OFF → DOWN: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] G1-5 (SU) - Masa bodi` | Warna Kabel: W - Masa bodi — Input motor power window UP (Remote) | Switch pengapian on (IG), switch utama power window OFF → UP (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] G1-2 (SD) - Masa bodi` | Warna Kabel: P - Masa bodi — Input motor power window DOWN (Remote) | Switch pengapian on (IG), switch utama power window OFF → DOWN (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] 3 (B) - Masa bodi` | Warna Kabel: SB - Masa bodi — Power supply pengapian | Switch pengapian off: Di bawah 1 V / Switch pengapian on (IG): 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] 4 (U) - Masa bodi` | Warna Kabel: Y - Masa bodi — Output motor power window pintu sisi penumpang UP | Switch pengapian on (IG), switch power window OFF → UP: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] 1 (D) - Masa bodi` | Warna Kabel: B - Masa bodi — Output motor power window pintu sisi penumpang DOWN | Switch pengapian on (IG), switch power window OFF → DOWN: Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] 5 (SU) - Masa bodi` | Warna Kabel: R - Masa bodi — Input motor power window UP (Remote) | Switch pengapian on (IG), switch utama power window OFF → UP (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] 2 (SD) - Masa bodi` | Warna Kabel: G - Masa bodi — Input motor power window DOWN (Remote) | Switch pengapian on (IG), switch utama power window OFF → DOWN (Remote): Di bawah 1 V → 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] 4B-30 (BECU) - 4E-17 (GND1)` | Warna Kabel: L - W-B — Baterai (power supply) | Selalu: 11 sampai 14 V |
| `[KACA DEPAN / KACA JENDELA] 4S-7 (IG) - 4E-17 (GND1)` | Warna Kabel: R - W-B — Power supply pengapian | Switch pengapian on (IG): 11 sampai 14 V / Switch pengapian off: Di bawah 1 V |
| `[KACA DEPAN / KACA JENDELA] 4A-21 (DCTY) - Masa bodi` | Warna Kabel: R - Masa bodi — Input switch lampu courtesy pintu pengemudi | Pintu sisi pengemudi tertutup: 10 kΩ atau lebih tinggi / Pintu samping pengemudi terbuka: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] 4A-24 (PCTY) - Masa bodi` | Warna Kabel: L - Masa bodi — Input switch lampu courtesy pintu sisi penumpang | Pintu sisi penumpang tertutup: 10 kΩ atau lebih tinggi / Pintu samping penumpang terbuka: Di bawah 1 Ω |
| `[KACA DEPAN / KACA JENDELA] D34-23 (CANP)*1 - Masa bodi` | Warna Kabel: BR - Masa bodi — Line komunikasi CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[KACA DEPAN / KACA JENDELA] D33-4 (CANP)*2 - Masa bodi` | Warna Kabel: BR - Masa bodi — Line komunikasi CAN | Selalu: 10 kΩ atau lebih tinggi |
| `[KACA DEPAN / KACA JENDELA] 4E-17 (GND1) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Masa | Selalu: Di bawah 1 Ω |

---

## 3. Katalog Lengkap Prosedur Pemeriksaan Kode DTC (OBD-II & Flash Code)

### DTC `B1000` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 31] Malfungsi Sensor Airbag Tengah Assembly (Dokumen: RM000000YTI00FX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 31] Malfungsi Sensor Airbag Tengah Assembly (Dokumen: RM000000YTI020X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag tengah assembly; Kondisi Deteksi: Malfungsi sensor airbag tengah assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pen
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `B1242` — [DOOR LOCK — SISTEM KONTROL KUNCI PINTU WIRELESS (dengan Sistem Entry dan Start)] Malfungsi Sirkuit Tuner Kunci Pintu Wireless (Dokumen: RM000001TP3001X) | [DOOR LOCK — SISTEM KONTROL KUNCI PINTU WIRELESS (tanpa Sistem Entry dan Start)] Malfungsi Sirkuit Tuner Kunci Pintu Wireless (Dokumen: RM000001TQK001X) | [DOOR LOC
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [DOOR LOCK] Area Gangguan: Wire harness Receiver kontrol pintu. ECU Sertifikasi Main body ECU; Kondisi Deteksi: Short dalam RDA atau masa RSSI antara ECU sertifikasi dan receiver kontrol pintu Short dalam RDA atau masa RSSI bila output RCO (5 V) dari ECU off.; [DOOR LOCK] Area Gangguan: Wire harness Receiver kontrol pintu. Main body ECU; Kondisi Deteksi: Dalam mode diagnosis, penerapan sinyal RDA tidak dapat diterima dalam 1 detik setelah sinyal 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (DOOR LOCK) — PERIKSA HARNESS DAN KONEKTOR (RECEIVER KONTROL PINTU - ECU SERTIFIKASI): Lepas hubungan konektor D60 ECU sertifikasi. -> Lepas hubungan konektor J13 receiver kontrol pintu. -> Ukur tahanan. -> Hubungkan kembali konektor ECU sertifikasi. -> Sambungkan kembali konektor receiver kontrol pintu .
  - Langkah 2 (DOOR LOCK) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECU SERTIFIKASI): Lepas hubungan konektor 4D pada main body ECU. -> Lepas hubungan konektor D60 ECU sertifikasi. -> Ukur tahanan. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor ECU sertifikasi.
  - Langkah 3 (DOOR LOCK) — PERIKSA RECEIVER KONTROL PINTU (+B TERMINAL): Ukur voltase.
  - Langkah 4 (DOOR LOCK) — PERIKSA RECEIVER KONTROL PINTU (GND TERMINAL): Lepas hubungan konektor J13 receiver kontrol pintu. -> Ukur tahanan. -> Sambungkan kembali konektor receiver kontrol pintu .
  - Langkah 5 (DOOR LOCK) — GANTI RECEIVER KONTROL PINTU: Ganti receiver kontrol pintu. -> Lakukan prosedur REGISTRASI.
  - Langkah 6 (DOOR LOCK) — PEMERIKSAAN ULANG DTC: Menghapus DTC. -> Periksa apakah DTC yang sama terdeteksi
  - Langkah 7 (DOOR LOCK) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (DOOR LOCK) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[DOOR LOCK] Tahanan standar: D60-38 (RDA) - J13-5 (DATA)` : **Di bawah 1 Ω**
  - `[DOOR LOCK] Tahanan standar: D60-38 (RDA) atau J13-5 (DATA) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[DOOR LOCK] Tahanan standar: D60-39 (RSSI) - J13-2 (RSSI)` : **Di bawah 1 Ω**
  - `[DOOR LOCK] Tahanan standar: D60-39 (RSSI) atau J13-2 (RSSI) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[DOOR LOCK] Tahanan standar: D60-29 (RCO) - J13-4 (+5)` : **Di bawah 1 Ω**
  - `[DOOR LOCK] Tahanan standar: D60-29 (RCO) atau J13-4 (+5) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[DOOR LOCK] Tahanan standar: 4D-9 (LIN1) - D60-10 (LIN)` : **Di bawah 1 Ω**
  - `[DOOR LOCK] Tahanan standar: 4D-9 (LIN1) atau D60-10 (LIN) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B1269` — [ANTI PENCURIAN — SISTEM ANTI PENCURIAN] Komunikasi ECU Anti Pencurian Berhenti (Dokumen: RM000001K7I001X) | [ANTI PENCURIAN — SISTEM ANTI PENCURIAN] Komunikasi ECU Anti Pencurian Berhenti (Dokumen: RM000001K7I009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ANTI PENCURIAN] Area Gangguan: ECU peringatan pencurian assembly Wire harness dan konektor; Kondisi Deteksi: Tidak ada komunikasi dari ECU peringatan pencurian selama lebih dari 3.5 detik.; Kondisi Deteksi: Tidak ada komunikasi dari ECU sertifikasi assembly selama lebih dari 10 detik.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ANTI PENCURIAN) — PERIKSA HARNESS DAN KONEKTOR (ECU ANTI PENCURI - MAIN BODY ECU - DAN ECU SERTIFIKASI): Lepas hubungan konektor D74 ECU anti pencurian. -> Lepas hubungan D33 main body ECU atau konektor D60 ECU sertifikasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali ECU peringatan pencuri dan konektor main body ECU. 
  - Langkah 2 (ANTI PENCURIAN) — PERIKSA ECU PERINGATAN PENCURI ASSEMBLY: Lepas hubungan konektor D74 ECU anti pencurian. -> Periksa voltase antara wire harness sisi konektor dan bodi masa. -> Hubungkan kembali konektor ECU peringatan pencurian
  - Langkah 3 (ANTI PENCURIAN) — GANTI ECU PERINGATAN PENCURIAN ASSEMBLY
  - Langkah 4 (ANTI PENCURIAN) — PERBAIKI ATAU GANTI HARNESS DAN KONEKTOR
  - Langkah 1 (ANTI PENCURIAN) — PERIKSA HARNESS DAN KONEKTOR (ECU PERINGATAN PENCURIAN - MAIN BODY ECU ATAU ECU SERTIFIKASI): Lepas hubungan konektor D26 ECU peringatan pencurian. -> Lepaskan konektor D33 *1 main body ECU atau konektor D28 *2 ECU sertifikasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali ECU peringatan pencuri dan konektor 
  - Langkah 2 (ANTI PENCURIAN) — PERIKSA HARNESS DAN KONEKTOR (VOLTASE BATERAI): Lepas hubungan konektor D26 ECU peringatan pencurian. -> Periksa voltase antara wire harness sisi konektor dan bodi masa. -> Hubungkan kembali konektor ECU peringatan pencurian
  - Langkah 3 (ANTI PENCURIAN) — PERIKSA DARI DTC: Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Hapus DTC (lihat halaman ). -> Periksa apakah DTC yang sama terdeteksi
  - Langkah 4 (ANTI PENCURIAN) — GANTI ECU PERINGATAN PENCURIAN ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[ANTI PENCURIAN] Tahanan standar: D74-25 (BRK+) - D33-18 (SRX)` : **Di bawah 1 Ω**
  - `[ANTI PENCURIAN] Tahanan standar: D74-24 (BRK-) - D33-19 (STX)` : **Di bawah 1 Ω**
  - `[ANTI PENCURIAN] Tahanan standar: D74-25 (BRK+) atau D33-18 (SRX) - Bodi masa` : **10 kΩ atau lebih tinggi**
  - `[ANTI PENCURIAN] Tahanan standar: D74-24 (BRK-) atau D33-19 (STX) - Bodi masa` : **10 kΩ atau lebih tinggi**
  - `[ANTI PENCURIAN] Tahanan standar: D74-16 (E) - Bodi masa` : **Di bawah 1 Ω**
  - `[ANTI PENCURIAN] Tahanan standar: D74-25 (BRK+) - D60-24 (SECI)` : **Di bawah 1 Ω**
  - `[ANTI PENCURIAN] Tahanan standar: D74-24 (BRK-) - D60-25 (SECO)` : **Di bawah 1 Ω**
  - `[ANTI PENCURIAN] Tahanan standar: D74-25 (BRK+) atau D60-24 (SECI) - Bodi masa` : **10 kΩ atau lebih tinggi**

### DTC `B1610` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 13] Malfungsi Sirkuit Sensor Airbag Depan RH (Dokumen: RM000001BHH002X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 13] Malfungsi Sirkuit Sensor Airbag Depan RH (Dokumen: RM000001BHH009X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel utama ruang mesin Sensor airbag depan RH Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalur sinyal hubung pendek, sinyal hubungan terbuka, sinyal hubung pendek ke masa, atau sinyal hubung pendek ke B+ dalam sirkuit sensor airbag depan selama 2 detik. Malfungsi sens
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTPUT DTC: Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. -> Hapus DTC yang tersimpan dalam memori (Lihat halaman ). -> Putar switch pengapian ke off. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. ->
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA HUBUNGAN KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Periksa apakah konektor terpasang dengan sesuai pada sensor airbag tengah assembly dan sensor airbag de
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (DARI OPEN): Lepas hubungan konektor dari sensor airbag tengah assembly dan sensor airbag depan RH. -> Menggunakan kabel servis, hubungkan A6-1 dan A6-2 konektor E. -> Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (DARI HUBUNG PENDEK): Lepas hubungan kabel servis dari konektor E. -> Ukur tahanan.
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (KE B+): Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (KE MASA): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Ukur tahanan.
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SENSOR AIRBAG DEPAN RH: Hubungkan konektor ke sensor airbag tengah assembly. -> Pertukarkan sensor airbag depan LH dengan RH dan hubungkan konektor untuk keduanya. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar swit
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D16-29 (+SR) - D16-27 (-SR) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D16-29 (+SR) - D16-27 (-SR) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D16-29 (+SR) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D16-29 (+SR) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: AD1-1 (+SR) - AD1-2 (-SR) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: AD1-1 (+SR) - AD1-2 (-SR) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: AD1-1 (+SR) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: AD1-2 (-SR) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**

### DTC `B1615` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 14] Malfungsi Sirkuit Sensor Airbag Depan LH (Dokumen: RM000001BHI002X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 14] Malfungsi Sirkuit Sensor Airbag Depan LH (Dokumen: RM000001BHI009X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel utama ruang mesin Sensor airbag depan LH Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalur sinyal hubung pendek, sinyal hubungan terbuka, sinyal hubung pendek ke masa, atau sinyal hubung pendek ke B+ dalam sirkuit sensor airbag depan LH selama 2 detik. Malfungsi s
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC: Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. -> Hapus DTC yang tersimpan dalam memori (Lihat halaman ). -> Putar switch pengapian ke off. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. ->
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA HUBUNGAN KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Periksa apakah konektor terpasang dengan sesuai pada sensor airbag tengah assembly dan sensor airbag de
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN LH (DARI OPEN): Lepas hubungan konektor dari sensor airbag tengah assembly dan sensor airbag depan LH. -> Menggunakan kabel servis, hubungkan A12-1 dan 12-2 dari konektor E. -> Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN LH (DARI HUBUNG PENDEK): Lepas hubungan kabel servis dari konektor E. -> Ukur tahanan.
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN LH (KE B+): Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN LH (KE MASA): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Ukur tahanan.
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SENSOR AIRBAG DEPAN LH: Hubungkan konektor ke sensor airbag tengah assembly. -> Pertukarkan sensor airbag depan LH dengan RH dan hubungkan konektor untuk keduanya. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar swit
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D16-30 (+SL) - D16-28 (-SL) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D16-30 (+SL) - D16-28 (-SL) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D16-30 (+SL) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D16-28 (-SL) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Hambatan standar: D16-30 (+SL) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Hambatan standar: D16-28 (-SL) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: AD1-3 (+SL) - AD1-4 (-SL) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: AD1-3 (+SL) - AD1-4 (-SL) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1662` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 45] Malfungsi Sirkuit Lampu Indikator (Dokumen: RM000001CHO003X) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 45] Malfungsi Sirkuit Lampu Indikator (Dokumen: RM000001CHO00OX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Meter kombinasi Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalur sinyal hubung pendek, sinyal hubungan terbuka, sinyal hubung pendek ke masa, atau sinyal hubung pendek ke B+ dalam sirkuit lampu indikator selama 2 detik. Malfungsi sirkuit 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC (SISTEM AIRBAG): Putar switch pengapian ke on (IG). -> Hapus DTC yang tersimpan dalam memori (Lihat halaman ). -> Putar switch pengapian ke off. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA DTC (SISTEM KOMUNIKASI CAN): Putar switch pengapian ke on (IG). -> Periksa DTC (Lihat halaman ).
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA HUBUNGAN KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Periksa apakah konektor terpasang dengan sesuai pada sensor airbag tengah assembly dan sensor meter kom
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Ganti sensor airbag tengah assembly (Lihat halaman ). -> Periksa konektor untuk ke sensor airbag tengah
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — SELESAI
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SISTEM KOMUNIKASI CAN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — HUBUNGKAN KONEKTOR

### DTC `B1800` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short Circuit dalam Squib Sisi Pengemudi (Dokumen: RM000000XFI00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short Circuit dalam Squib Sisi Pengemudi (Dokumen: RM000000XFI01YX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Fla
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel spiral Steering pad (Squib sisi pengemudi) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal jalur hubung pendek dalam sirkuit squib sisi pengemudi 5 kali selama pengecekan primer. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalu
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel warna putih dari SST (Tahanan 2.1Ω) 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel spiral (pada sisi steering pad) tid
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Lepas hubungan konektor dari sensor airbag tengah assembly dan steering pad. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirku
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. -> Hapus 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubu
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-1(D-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-2(D+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-2(D+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-1 (D+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-2 (D-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**

### DTC `B1801` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Open Circuit dalam Squib Sisi Pengemudi (Dokumen: RM000000XFI00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Open Circuit dalam Squib Sisi Pengemudi (Dokumen: RM000000XFI01YX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel spiral Steering pad (Squib sisi pengemudi) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal jalur hubung pendek dalam sirkuit squib sisi pengemudi 5 kali selama pengecekan primer. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalu
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel warna putih dari SST (Tahanan 2.1Ω) 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel spiral (pada sisi steering pad) tid
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Lepas hubungan konektor dari sensor airbag tengah assembly dan steering pad. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirku
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. -> Hapus 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubu
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-1(D-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-2(D+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-2(D+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-1 (D+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-2 (D-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**

### DTC `B1802` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke GND dalam Sirkuit Squib Sisi Pengemudi (Dokumen: RM000000XFI00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke GND dalam Sirkuit Squib Sisi Pengemudi (Dokumen: RM000000XFI01YX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTE
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel spiral Steering pad (Squib sisi pengemudi) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal jalur hubung pendek dalam sirkuit squib sisi pengemudi 5 kali selama pengecekan primer. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalu
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel warna putih dari SST (Tahanan 2.1Ω) 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel spiral (pada sisi steering pad) tid
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Lepas hubungan konektor dari sensor airbag tengah assembly dan steering pad. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirku
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. -> Hapus 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubu
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-1(D-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-2(D+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-2(D+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-1 (D+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-2 (D-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**

### DTC `B1803` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke B+ dalam Sirkuit Squib Sisi Pengemudi (Dokumen: RM000000XFI00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 51] Short ke B+ dalam Sirkuit Squib Sisi Pengemudi (Dokumen: RM000000XFI01YX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM 
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel spiral Steering pad (Squib sisi pengemudi) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal jalur hubung pendek dalam sirkuit squib sisi pengemudi 5 kali selama pengecekan primer. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalu
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari steering pad. -> Hubungkan sisi kabel warna putih dari SST (Tahanan 2.1Ω) 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel spiral (pada sisi steering pad) tid
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENGEMUDI: Lepas hubungan konektor dari sensor airbag tengah assembly dan steering pad. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirku
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik. -> Hapus 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubu
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI STEERING PAD
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-1(D-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: W1-2(D+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-2(D+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: W1-1(D-) - W1-2(D+) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-1 (D+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D18-2 (D-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**

### DTC `B1805` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ021X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang depan assembly (Squib sisi penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib sisi penumpang depan 5 kali selama pengecekan primer. Malfungsi squib sisi penumpang depan Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Sens
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag assembly penumpang depan. -> Hubungkan sisi kabel warna putih dari 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel panel instrumen assembly (pada sisi
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Lepas hubungan konektor dari sensor airbag tengah assembly dan sensor airbag depan assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke 
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik.
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. ->
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN ASSEMBLY: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-2 (P+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-1 (P-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-1 (P-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-1 (P+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-2 (P-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: DQ2-1 (P+) - DQ2-2 (P-) (Selalu)` : **Di bawah 1 Ω**

### DTC `B1806` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Open dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Open dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ021X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang depan assembly (Squib sisi penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib sisi penumpang depan 5 kali selama pengecekan primer. Malfungsi squib sisi penumpang depan Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Sens
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag assembly penumpang depan. -> Hubungkan sisi kabel warna putih dari 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel panel instrumen assembly (pada sisi
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Lepas hubungan konektor dari sensor airbag tengah assembly dan sensor airbag depan assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke 
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik.
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. ->
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN ASSEMBLY: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-2 (P+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-1 (P-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-1 (P-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-1 (P+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-2 (P-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: DQ2-1 (P+) - DQ2-2 (P-) (Selalu)` : **Di bawah 1 Ω**

### DTC `B1807` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke GND dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke GND dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ021X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang depan assembly (Squib sisi penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib sisi penumpang depan 5 kali selama pengecekan primer. Malfungsi squib sisi penumpang depan Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Sens
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag assembly penumpang depan. -> Hubungkan sisi kabel warna putih dari 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel panel instrumen assembly (pada sisi
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Lepas hubungan konektor dari sensor airbag tengah assembly dan sensor airbag depan assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke 
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik.
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. ->
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN ASSEMBLY: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-2 (P+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-1 (P-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-1 (P-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-1 (P+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-2 (P-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: DQ2-1 (P+) - DQ2-2 (P-) (Selalu)` : **Di bawah 1 Ω**

### DTC `B1808` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke B+ dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ00GX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 52] Short ke B+ dalam Sirkuit Squib Sisi Penumpang Depan (Dokumen: RM000000XFJ021X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Kabel panel instrumen assembly Airbag penumpang depan assembly (Squib sisi penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib sisi penumpang depan 5 kali selama pengecekan primer. Malfungsi squib sisi penumpang depan Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Sens
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari airbag assembly penumpang depan. -> Hubungkan sisi kabel warna putih dari 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor E. -> Periksa bahwa konektor kabel panel instrumen assembly (pada sisi
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SQUIB SISI PENUMPANG DEPAN: Lepas hubungan konektor dari sensor airbag tengah assembly dan sensor airbag depan assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke 
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu minimal selama 60 detik.
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN: Kembalikan mekanisme pencegahan aktivasi dari konektor B yang telah dibebaskan ke kondisi aslinya. -> Lepas hubungan konektor kabel panel instrumen dari kabel panel instrumen assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. ->
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN ASSEMBLY: Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-2 (P+) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: Q1-1 (P-) - Masa Bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-2 (P+) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: Q1-1 (P-) - Masa Bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-1 (P+) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: DQ2-2 (P-) - Masa bodi (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: DQ2-1 (P+) - DQ2-2 (P-) (Selalu)` : **Di bawah 1 Ω**

### DTC `B1900` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Short dalam Sirkuit Squib Pretensioner Sisi Depan Pengemudi (Dokumen: RM000001BX300CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Short dalam Sirkuit Squib Pretensioner Sisi Depan Pengemudi (Dokumen: RM000001BX300EX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi pengemudi) (LHD) Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi pengemudi) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalur sinyal hubung pendek dalam sirkuit squib pretensioner depan sisi pengemudi 5 kali selama pengecekan primer. Malfung
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari outer belt tempat duduk depan sisi pengemudi assembly. -> Hubungkan sisi k
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt tempat
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENGEMUDI): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu min
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-2 (L+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1901` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Open dalam Sirkuit Squib Pretensioner Sisi Depan Penumpang (Dokumen: RM000001BX300CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Open dalam Sirkuit Squib Pretensioner Sisi Depan Penumpang (Dokumen: RM000001BX300EX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi pengemudi) (LHD) Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi pengemudi) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalur sinyal hubung pendek dalam sirkuit squib pretensioner depan sisi pengemudi 5 kali selama pengecekan primer. Malfung
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari outer belt tempat duduk depan sisi pengemudi assembly. -> Hubungkan sisi k
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt tempat
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENGEMUDI): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu min
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-2 (L+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1902` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Short ke GND dalam Sirkuit Squib Pretensioner Depan Sisi Pengemudi (Dokumen: RM000001BX300CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Short ke GND dalam Sirkuit Squib Pretensioner Depan Sisi Pengemudi (Dokumen: RM000001BX300EX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi pengemudi) (LHD) Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi pengemudi) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalur sinyal hubung pendek dalam sirkuit squib pretensioner depan sisi pengemudi 5 kali selama pengecekan primer. Malfung
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari outer belt tempat duduk depan sisi pengemudi assembly. -> Hubungkan sisi k
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt tempat
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENGEMUDI): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu min
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-2 (L+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1903` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Short ke B+ dalam Sirkuit Squib Pretensioner Depan Sisi Pengemudi (Dokumen: RM000001BX300CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 73] Short ke B+ dalam Sirkuit Squib Pretensioner Depan Sisi Pengemudi (Dokumen: RM000001BX300EX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi pengemudi) (LHD) Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi pengemudi) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi jalur sinyal hubung pendek dalam sirkuit squib pretensioner depan sisi pengemudi 5 kali selama pengecekan primer. Malfung
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENGEMUDI): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor dari outer belt tempat duduk depan sisi pengemudi assembly. -> Hubungkan sisi k
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt tempat
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENGEMUDI): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on (IG), dan tunggu min
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-2 (L+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1905` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Short dalam Sirkut Squib Pretensioner Sisi Depan Penumpang (Dokumen: RM000001BX400CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Short dalam Sirkut Squib Pretensioner Sisi Depan Penumpang (Dokumen: RM000001BX400EX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi penumpang depan) (LHD) Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi penumpang depan) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib pretensioner depan sisi penumpang depan 5 kali selama pengecek
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor outer belt tempat duduk depan sisi penumpang depan assembly. -> Hubungkan sisi 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt assemb
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENUMPANG DEPAN): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan sisi penumpangdepan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-2 (R+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1906` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Open dalam Sirkut Squib Pretensioner Sisi Depan Penumpang (Dokumen: RM000001BX400CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Open dalam Sirkut Squib Pretensioner Sisi Depan Penumpang (Dokumen: RM000001BX400EX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi penumpang depan) (LHD) Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi penumpang depan) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib pretensioner depan sisi penumpang depan 5 kali selama pengecek
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor outer belt tempat duduk depan sisi penumpang depan assembly. -> Hubungkan sisi 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt assemb
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENUMPANG DEPAN): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan sisi penumpangdepan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-2 (R+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1907` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Short ke GND dalam Sirkuit Squib Pretensioner Sisi Penumpang Depan (Dokumen: RM000001BX400CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Short ke GND dalam Sirkuit Squib Pretensioner Sisi Penumpang Depan (Dokumen: RM000001BX400EX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi penumpang depan) (LHD) Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi penumpang depan) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib pretensioner depan sisi penumpang depan 5 kali selama pengecek
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor outer belt tempat duduk depan sisi penumpang depan assembly. -> Hubungkan sisi 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt assemb
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENUMPANG DEPAN): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan sisi penumpangdepan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-2 (R+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B1908` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Short ke B+ dalam Sirkuit Pretensioner Squib Depan Sisi Penumpang Depan (Dokumen: RM000001BX400CX) | [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG / Flash Code 74] Short ke B+ dalam Sirkuit Pretensioner Squib Depan Sisi Penumpang Depan (Dokumen: RM000001B
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel lantai Outer belt tempat duduk depan assembly RH (Squib pretensioner depan sisi penumpang depan) (LHD) Outer belt tempat duduk depan assembly LH (Squib pretensioner depan sisi penumpang depan) (RHD) Sensor airbag tengah assembly; Kondisi Deteksi: Sensor airbag tengah assembly mendeteksi sinyal hubung pendek jalur dalam sirkuit squib pretensioner depan sisi penumpang depan 5 kali selama pengecek
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA OUTER BELT ASSEMBLY TEMPAT DUDUK DEPAN (SISI PRETENSIONER SQUIB DEPAN SISI PENUMPANG DEPAN): Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan konektor outer belt tempat duduk depan sisi penumpang depan assembly. -> Hubungkan sisi 
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR: Putar switch pengapian ke off. -> Lepas hubungan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepas hubungan SST dari konektor C. -> Periksa bahwa konektor kabel lantai (pada sisi outer belt assemb
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL LANTAI (SIRKUIT SQUIB PRETENSIONER DEPAN SISI PENUMPANG DEPAN): Lepas hubungan konektor dari sensor airbag tengah assembly. -> Periksa dari hubungan pendek ke B+ dalam sirkuit. -> Periksa dari hubungan terbuka (open) dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa da
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke sisi outer belt assembly tempat duduk depan sisi penumpangdepan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke on 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODE SIMULASI UNTUK PERIKSA
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY RH (LHD)
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI OUTER BELT TEMPAT DUDUK DEPAN ASSEMBLY LH (RHD)
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL LANTAI
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-1 (R-) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J20-2 (R+) - Masa bodi (*1) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-1 (L-) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: J21-2 (L+) - Masa bodi (*2) (Switch pengapian on (IG))` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - J20-2 (R+) (*1) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J21-1 (L-) - J21-2 (L+) (*2) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-1 (R-) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: J20-2 (R+) - Masa bodi (*1) (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `B2271` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Malfungsi pada Ignition Hold Monitor (Dokumen: RM000000XEK00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Malfungsi pada Ignition Hold Monitor (Dokumen: RM000000XEK019X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Fuse AM2 Wire harness; Kondisi Deteksi: Sirkuit aktuator relay IG1 atau sirkuit aktuasi relay bagian dalam main body ECUadalah abnormal; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Fuse AM2 Wire harness atau konektor; Kondisi Deteksi: Tahan sirkuit , relay IG1 menggerakkan sirkuit atau relay IG2 menggerakkan sirkuit di dalam main body ECU open atau short.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Hapus DTC. -> Hidupkan mesin. -> Biarkan mesin idle dalam waktu 1 menit atau lebih. -> Pilih item menu berikut ini: Bodi / ECU Bodi / DTC.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA FUSE (AM2): Lepas fuse ECU-B dari ruang mesin R/B dan J/B. -> Periksa tahanan fuse. -> Pasang kembali fuse AM2.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - BATERAI DAN MASA BODI): Lepaskan konektor D64 dan D65 pada main body ECU. -> Ukur voltase dan tahanan sisi konektor wire harness. -> Hubungkan kembali konektor pada main body ECU.
  - Langkah 4 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 5 (STARTING 1NZ-FE) — SISTEM OK
  - Langkah 6 (STARTING 1NZ-FE) — GANTI FUSE
  - Langkah 7 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG ATAU TIDAK (DTC B2271): Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Hapus DTC (lihat halaman ). -> Periksa ulang DTC.
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Voltase standar: D65-1 (AM1) - Masa bodi` : **10 sampai 14 V**
  - `[STARTING 1NZ-FE] Voltase standar: D64-6 (AM2) - Masa bodi` : **10 sampai 14 V**
  - `[STARTING 1NZ-FE] Tahanan standar: D65-4 (GND2) - Masa bodi` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: Fuse AM2 (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Voltase standar: D35-1 (AM1) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[STARTING 1NZ-FE] Voltase standar: D34-6 (AM2) - Masa bodi (Selalu)` : **11 sampai 14 V**

### DTC `B2272` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Pengapian 1 Memonitor Malfungsi (Dokumen: RM000000XEL00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Pengapian 1 Memonitor Malfungsi (Dokumen: RM000000XEL012X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Relay IG1 Wire harness; Kondisi Deteksi: Sirkuit aktuasi relay IG1 pada bagian dalam main body ECU atau sirkuit lain yang berhubungan sedang mengalami malfungsi; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Relay IG1 Wire harness atau konektor
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (IG1 RELAY MONITOR (INSIDE)): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body/ Main Body ECU/ Data List / IG1 Relay Mon2. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA KONDISI SWITCH (SWITCH PENGAPIAN): Pastikan kunci elektrik berada di dalam kabin. -> Periksa apakah terdapat perubahan mode catu daya seperti tampak di bawah setiap kali pengapian di-switch-kan.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA RELAY (IG1): Lepas relay IG1 dari main body ECU. -> Periksa tahanan. -> Pasang kembali relay.
  - Langkah 4 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 5 (STARTING 1NZ-FE) — NORMAL
  - Langkah 6 (STARTING 1NZ-FE) — LANJUT KE MODE CATU DAYA TIDAK BERUBAH
  - Langkah 7 (STARTING 1NZ-FE) — GANTI RELAY PENGAPIAN NO. 1
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGUNAKAN INTELLIGENT TESTER (MONITOR RELAY IG1 (BAGIAN LUAR)): Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Pilih item di bawah dalam DATA LIST dan baca tampilannya pada tester.
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Main Body ECU: IG1 Relay Mon2 (Bagian dalam relay monitor IG1 / ON atau OFF)` : **ON: Switch pengapian on (IG) OFF: Switch pengapian off**
  - `[STARTING 1NZ-FE] Tahanan standar: 3 - 5` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 3 - 5` : **Dibawah 1 Ω (Ketika voltage baterai diberikan ke terminal 1 dan 2)**
  - `[STARTING 1NZ-FE] Main Body ECU: IG1 Relay Monitor (outside) (Status dari IG1 relay monitor (outside) / ON atau OFF)` : **ON: Engine switch on (IG) (relay IG1 ON) OFF: Engine switch off (relay IG1 OFF)**
  - `[STARTING 1NZ-FE] Tahanan standar: 3 - 5 ((Bila voltase baterai tidak digunakan ke terminal 1 dan 2))` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 3 - 5 (Bila voltase baterai diberikan pada terminal 1 dan 2)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4F-3 - D35-6 (SRX) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D35-6 (SRX) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2273` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Pengapian 2 Memonitor Malfungsi (Dokumen: RM000000XEM00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Pengapian 2 Memonitor Malfungsi (Dokumen: RM000000XEM019X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Relay IG2 Wire harness; Kondisi Deteksi: Sirkuit aktuasi relay IG1 pada bagian dalam main body ECU atau sirkuit lain yang berhubungan sedang mengalami malfungsi; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Relay IG2 Wire harness atau konektor
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (IG2 RELAY MONITOR (INSIDE)): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body/ Main Body ECU/ Data List / IG2 Relay Mon2. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA KONDISI SWITCH (SWITCH PENGAPIAN): Pastikan kunci elektrik berada di dalam kabin. -> Periksa apakah terdapat perubahan mode catu daya seperti tampak di bawah setiap kali pengapian di-switch-kan.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA RELAY INTEGRASI NO. 1 (RELAY IG2): Lepas relay integrasi dari relay block ruang mesin. -> Ukur tahanan relay. -> Pasang kembali relay integrasi.
  - Langkah 4 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (RELAY INTEGRASI - MAIN BODY ECU): Lepas relay integrasi dari relay block ruang mesin. -> Lepaskan konektor D64 pada main body ECU. -> Ukur tahanan pada wire harness sisi konektor. -> Pasang kembali relay integrasi. -> Hubungkan kembali konektor main body ECU.
  - Langkah 5 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 6 (STARTING 1NZ-FE) — NORMAL
  - Langkah 7 (STARTING 1NZ-FE) — LANJUT KE MODE CATU DAYA TIDAK BERUBAH
  - Langkah 8 (STARTING 1NZ-FE) — GANTI RELAY INTEGRASI NO. 1
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Main Body ECU: Mon2 Relay IG2 (Bagian dalam relay monitor IG2 / ON atau OFF)` : **ON: Switch pengapian on (IG) OFF: Switch pengapian off**
  - `[STARTING 1NZ-FE] Tahanan standar: 1B-4 - 1C-1` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 1B-4 - 1C-1` : **Di bawah 1 Ω (Ketika voltage baterai diberikan ke terminal 1B-2 dan 1B-3)**
  - `[STARTING 1NZ-FE] Tahanan standar: 1B-2 (Relay integrasi) - D65-5 (IG2D)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 1B-3 (Relay integrasi) - Masa bodi` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 1B-2 (Relay integrasi) atau D65-5 (IG2D) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: Fuse AM2 (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Main Body ECU: Monitor Relay IG2 (outside) (Status monitor relay IG2 (outside)/ ON atau OFF)` : **ON: Engine switch on (IG) (relay IG2 ON) OFF: Engine switch off (relay IG2 OFF)**

### DTC `B2274` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Monitor ACC Malfungsi (Dokumen: RM000000XEN00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Monitor ACC Malfungsi (Dokumen: RM000000XEN012X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Relay pemutus ACC Wire harness; Kondisi Deteksi: Sirkuit aktuator ACC cut relay di dalam main body ECU atau sirkuit lain yang berhubungan sedang malfungsi; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Relay ACC Wire harness atau konektor; Kondisi Deteksi: Sirkuit aktuasi relay ACC pada bagian dalam main body ECU atau sirkuit lain yang berhubungan sedang mengalami malfungsi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (MONITOR RELAY ACC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body/ Main Body ECU/ Data List / ACC Relay Mon. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA KONDISI SWITCH (SWITCH PENGAPIAN): Pastikan kunci elektrik berada di dalam kabin. -> Periksa apakah terdapat perubahan mode catu daya seperti tampak di bawah setiap kali pengapian di-switch-kan.
  - Langkah 3 (STARTING 1NZ-FE) — NORMAL
  - Langkah 4 (STARTING 1NZ-FE) — PERIKSA RELAY (ACC CUT RELAY): Lepas relay cut ACC. -> Periksa tahanan. -> Pasang kembali relay.
  - Langkah 5 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ACC CUT RELAY): Lepas relay cut ACC. -> Lepas hubungan konektor D64 main body ECU. -> Periksa tahanan. -> Pasang kembali ACC cut relay. -> Hubungkan kembali konektor main body ECU.
  - Langkah 6 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 7 (STARTING 1NZ-FE) — LANJUT KE MODE CATU DAYA TIDAK BERUBAH
  - Langkah 8 (STARTING 1NZ-FE) — GANTI RELAY (ACC CUT RELAY)
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Main Body ECU: Monitor Relay ACC (Monitor relay ACC / ON atau OFF)` : **ON: Switch pengapian on (ACC) OFF: Switch pengapian off**
  - `[STARTING 1NZ-FE] Tahanan standar: 3 - 5` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 3 - 5` : **Di bawah 1 Ω (Bila voltase baterai digunakan ke terminal 1 dan 2)**
  - `[STARTING 1NZ-FE] Tahanan standar: Relay pemutus ACC (D73-2) - ACCD (D64-4)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Main Body: Monitor Relay ACC (Status ACC Monitor Relay / ON atau OFF)` : **ON: Switch mesin on (ACC) OFF: Switch mesin off**
  - `[STARTING 1NZ-FE] Tahanan standar: D49-2 (ACC relay holder) - D34-4 (ACCD) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D49-1 (ACC relay holder) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Voltase standar: D49-5 (ACC relay holder) - Masa bodi (Selalu)` : **11 sampai 14 V**

### DTC `B2275` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Monitor STSW Malfungsi (Dokumen: RM000000XES00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Monitor STSW Malfungsi (Dokumen: RM000000XES01AX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Sistem SFI (1NZ-FE) Wire harness; Kondisi Deteksi: Sirkuit sinyal permintaan start mesin pada bagian dalam main body ECU atau sirkuit lain yang berhubungan sedang mengalami malfungsi; [STARTING 1NZ-FE] Area Gangguan: Main body ECU ECM Wire harness atau konektor; Kondisi Deteksi: Sirkuit output STSW (sirkuit sinyal permintaan start mesin) di dalam main body ECU atau sirkuit lain yang berhubungan menga
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Hapus DTC. -> Putar switch pengapian ke on (IG), tunggu sedikitnya 15 detik`dan cek apakah paling terjadi pengulangan DTC B2275.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA MAIN BODY ECU: Lepas hubungan konektor D66 main body ECU. -> Periksa ketinggian pedal rem secara penuh. -> Ukur tahanan antara terminal masa ECU dan masa bodi saat switch pengapian dioperasikan untuk meng-crank mesin. -> Hubungkan kembali konektor main bo
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECM): Lepas hubungan konektor D66 main body ECU. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (STARTING 1NZ-FE) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN ATAU TIDAK: Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Periksa apakah mesin dapat di-start dengan normal
  - Langkah 5 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 6 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STARTING 1NZ-FE) — TERUSKAN KE SISTEM SFI (1NZ-FE)
  - Langkah 8 (STARTING 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Voltase standar: STSW (D66-4) - Masa bodi` : **10 sampai 14 V**
  - `[STARTING 1NZ-FE] Tahanan standar: STSW (D66-4) - STSW (A21-14)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: STSW (D66-4) atau STSW (A21-14) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Voltase standar: A20-14 (STSW) - Masa bodi (Start Mesin)` : **6 V atau lebih**
  - `[STARTING 1NZ-FE] Tahanan standar: D36-4 (STSW) - A20-14 (STSW) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D36-4 (STSW) or A20-14 (STSW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2276` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Sirkuit sinyal ACCR Malfungsi (Dokumen: RM000000Y7W00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sirkuit sinyal ACCR Malfungsi (Dokumen: RM000000Y7W015X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Sistem SFI (1NZ-FE) Wire harness; Kondisi Deteksi: Sirkuit output ACCR pada bagian dalam main body ECU atau sirkuit lain yang berhubungan sedang mengalami malfungsi; [STARTING 1NZ-FE] Area Gangguan: Main body ECU ECM Wire harness atau konektor; Kondisi Deteksi: Sirkuit input ACCR pada bagian dalam main body ECU atau sirkuit lain yang berhubungan mengalami malfungsi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Hapus DTC. -> Periksa apakah DTC B2276 terulang dalam 50 detik atau lebih setelah switch pengapian diputar ke on (IG).
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA MAIN BODY ECU: Lepas hubungan konektor D66 main body ECU. -> Ukur voltase antara terminal ECU dan masa bodi saat switch pengapian dioperasikan untuk men-start mesin. -> Hubungkan kembali konektor main body ECU.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECM): Lepas hubungan konektor D66 main body ECU. -> Lepas hubungan konektor A21 ECM. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor main body ECU.
  - Langkah 4 (STARTING 1NZ-FE) — PERIKSA MAIN BODY ECU: Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Periksa apakah DTC B2276 berulang lagi atau tidak dengan mengulang prosedur 1
  - Langkah 5 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 6 (STARTING 1NZ-FE) — SISTEM OK
  - Langkah 7 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (STARTING 1NZ-FE) — TERUSKAN KE SISTEM SFI (1NZ-FE)
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Voltase standar: ACCR (D66-11) - Masa bodi` : **10 sampai 14 V**
  - `[STARTING 1NZ-FE] Tahanan standar: D66-11 (ACCR) - A21-13 (ACCR)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D66-11 (ACCR) atau A21-13 (ACCR) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: D36-11 (ACCR) - A20-13 (ACCR) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D36-11 (ACCR) atau A20-13 (ACCR) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Voltase standar: D36-11 (ACCR) - Masa bodi (Pedal rem ditekan, tuas shift di posisi P, atau N, engine switch ditekan sekal` : **0.1 sampai 0.8 V *1 → Output voltase pada terminal AM1 atau AM2 adalah -2 V atau lebih.**

### DTC `B2277` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Mendeteksi Kendaraan Terendam (Dokumen: RM000000XET00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Mendeteksi Kendaraan Terendam (Dokumen: RM000000XET018X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU; Kondisi Deteksi: Monitor submersion circuit bagian dalam main body ECU mendeteksi bahwa mobil telah teredam di dalam air.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Hapus DTC. -> Periksa apakah DTC B2277 terulang dalam 30 detik atau lebih setelah switch pengapian diputar ke on (IG).
  - Langkah 2 (STARTING 1NZ-FE) — SISTEM OK
  - Langkah 3 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA KERUSAKAN KARENA AIR: Periksa main body ECU, komponen pheripheral, dan wire harness dari bekas air.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK: Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Hapus DTC (lihat halaman ). -> Periksa ulang DTC.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 4 (STARTING 1NZ-FE) — AMBIL UKURAN YANG COCOK TERHADAP PENYEBAB KERUSAKAN KARENA AIR DAN GANTI MAIN BODY ECU
  - Langkah 5 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU

### DTC `B2278` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Sirkuit Engine Switch Malfungsi (Dokumen: RM000000Y7Z00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sirkuit Engine Switch Malfungsi (Dokumen: RM000000Y7Z01NX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Switch pengapian Wire harness; Kondisi Deteksi: Komunikasi abnormal antara main body ECU dan switch pengapian atau switch pengapian rusak; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Switch mesin Wire harness atau konektor; Kondisi Deteksi: Komunikasi abnormal antara main body ECU dan engine switch atau engine switch rusak
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (SWITCH START 1 DAN 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body / Main Body ECU / Data List / St SW1 and St SW2. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA KONDISI SWITCH (SWITCH PENGAPIAN): Pastikan kunci elektrik berada di dalam kabin. -> Periksa apakah terdapat perubahan mode catu daya seperti tampak di bawah setiap kali pengapian di-switch-kan.
  - Langkah 3 (STARTING 1NZ-FE) — SISTEM OK
  - Langkah 4 (STARTING 1NZ-FE) — PERIKSA SWITCH PENGAPIAN ASSEMBLY: Lepas switch pengapian. -> Ukur tahanan pada switch. -> Pasang kembali switch pengapian.
  - Langkah 5 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SWITCH PENGAPIAN - MAIN BODY ECU DAN MASA BODI): Lepas hubungan konektor D55 switch pengapian. -> Lepaskan konektor D64 pada main body ECU. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor switch pengapian.
  - Langkah 6 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 7 (STARTING 1NZ-FE) — LANJUT KE MODE CATU DAYA TIDAK BERUBAH
  - Langkah 8 (STARTING 1NZ-FE) — GANTI SWITCH PENGAPIAN ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: 7 (SS1) - 5 (GND) (Ditekan)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 2 (SS2) - 5 (GND) (Ditekan)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 7 (SS1) - 5 (GND) (Tidak didorong)` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 2 (SS2) - 5 (GND) (Tidak didorong)` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: D55-7 (SS1) - D65-10 (SSW1)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D55-2 (SS2) - D65-9 (SSW2)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D55-5 (GND) - Masa bodi` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D55-7 (SS1) atau D65-10 (SSW1) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B2281` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Sinyal "P" Malfungsi (Dokumen: RM000000XEU00BX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sinyal "P" Malfungsi (Dokumen: RM000000XEU00UX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sinyal "P" Malfungsi (Dokumen: RM000000XEU02AX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU ECU kontrol pengunci pemindah gigi Wire harness; Kondisi Deteksi: Informasi kabel dan informasi CAN antara main body ECU dan shift lock control ECU tidak konsisten; [STARTING 1NZ-FE] Area Gangguan: Sistem komunikasi CAN Main body ECU ECU kontrol pengunci pemindah gigi Wire harness atau konektor
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (SINYAL SHIFT P): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body / Main Body ECU / Data List / Shift P Sig. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SHIFT LOCK CONTROL ECU - MAIN BODY ECU): Lepas hubungan konektor D64 main body ECU. -> Lepaskan konektor D22 pada shift lock control ECU. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor shift lock control 
  - Langkah 3 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (SINYAL SHIFT P): Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body / Main Body ECU / Da
  - Langkah 4 (STARTING 1NZ-FE) — GANTI SHIFT LOCK CONTROL ECU
  - Langkah 5 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 6 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STARTING 1NZ-FE) — LANJUTKAN KE SISTEM KOMUNIKASI CAN
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA SISTEM KOMUNIKASI CAN: Periksa DTC sistem komunikasi CAN (lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: D64-15 (P) - D22-11 (P2)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D64-15 (P) atau D22-11 (P2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Main Body: Shift P Signal (Posisi posisi P/ ON atau OFF)` : **ON: Posisi shift pada P OFF: Posisi shift kecuali pada P**
  - `[STARTING 1NZ-FE] Tahanan standar: D34-15 (P) - D23-11 (P2) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D34-15 (P) atau D23-11 (P2) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2282` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Sinyal kecepatan kendaraam Malfungsi (Dokumen: RM000000XEV00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sinyal kecepatan kendaraam Malfungsi (Dokumen: RM000000XEV01RX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sinyal kecepatan kendaraam Malfungsi (Dokumen: 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Meter kombinasi Wire harness; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Meter kombinasi Speed sensor ECU skid control Wire harness; [STARTING 1NZ-FE] Area Gangguan: Sistem komunikasi CAN Sistem meter kombinasi Main body ECU Wire harness atau konektor; Kondisi Deteksi: Informasi kabel dan informasi CAN antara main body ECU dan meter kombinasi tidak konsisten.; [STARTING 1NZ-FE] Area Gangguan: Are
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (SINYAL KECEPATAN MESIN ): Hubungkan intelligent tester ke DLC3. -> Start mesin dan hidupkan tester ke ON. -> Pilih item menu berikut ini: Body / Main Body ECU / Data List / Vehicle Spd Sig. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - METER KOMBINASI): Lepaskan konektor 4C pada main body ECU. -> Lepas hubungan konektor D1 meter kombinasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor meter kombinasi. -> Hubungkan kembali konektor main body ECU.
  - Langkah 4 (STARTING 1NZ-FE) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN ATAU TIDAK: Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Periksa apakah mesin dapat di-start dengan normal
  - Langkah 5 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 6 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STARTING 1NZ-FE) — KE SISTEM METER KOMBINASI
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA SISTEM KOMUNIKASI CAN: Periksa DTC sistem komunikasi CAN (lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) - D1-16 (+S)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) atau D1-16 (+S) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) atau D1-16 (+S) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2283` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Malfungsi Speed Sensor Kendaraan (Dokumen: RM000000XEV00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Malfungsi Speed Sensor Kendaraan (Dokumen: RM000000XEV01RX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Malfungsi Speed Sensor Kendaraan (Dokumen: RM000000XEV0
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Meter kombinasi Wire harness; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Meter kombinasi Speed sensor ECU skid control Wire harness; [STARTING 1NZ-FE] Area Gangguan: Sistem komunikasi CAN Sistem meter kombinasi Main body ECU Wire harness atau konektor; Kondisi Deteksi: Informasi kabel dan informasi CAN antara main body ECU dan meter kombinasi tidak konsisten.; [STARTING 1NZ-FE] Area Gangguan: Are
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (SINYAL KECEPATAN MESIN ): Hubungkan intelligent tester ke DLC3. -> Start mesin dan hidupkan tester ke ON. -> Pilih item menu berikut ini: Body / Main Body ECU / Data List / Vehicle Spd Sig. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - METER KOMBINASI): Lepaskan konektor 4C pada main body ECU. -> Lepas hubungan konektor D1 meter kombinasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor meter kombinasi. -> Hubungkan kembali konektor main body ECU.
  - Langkah 4 (STARTING 1NZ-FE) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN ATAU TIDAK: Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Periksa apakah mesin dapat di-start dengan normal
  - Langkah 5 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 6 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STARTING 1NZ-FE) — KE SISTEM METER KOMBINASI
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA SISTEM KOMUNIKASI CAN: Periksa DTC sistem komunikasi CAN (lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) - D1-16 (+S)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) atau D1-16 (+S) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4C-8 (SPD) atau D1-16 (+S) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2285` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Sirkuit Sinyal Posisi Steering Lock Malfungsi (Dokumen: RM000000YD300AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sirkuit Sinyal Posisi Steering Lock Malfungsi (Dokumen: RM000000YD301OX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sirkuit Sinyal Posisi Steerin
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Sistem steering lock Wire harness; Kondisi Deteksi: Informasi kabel dan informasi CAN antara main body ECU dan ECU pengunci steering tidak konsisten; Kondisi Deteksi: Setelah memutar switch pengapian dari off ke on (IG), steering wheel tidak unlock selama beberapa piriode waktu (ECU membebaskan steering wheel hanya ketika menerima sinyal unlock dari komunikasi LIN dan kabel); [STARTING 1NZ-FE] Area G
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (KONDISI LOCK STEERING): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body/ Main Body ECU/ Data List / Str Unlock SW. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECU KUNCI STEERING): Lepas hubungan konektor D64 main body ECU. -> Lepaskan konektor D56 pada ECU steering lock. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor ECU steering lock. -> Hubungkan kembali konektor main body ECU.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN ATAU TIDAK: Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Periksa apakah mesin dapat di-start dengan normal
  - Langkah 4 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 5 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 6 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STARTING 1NZ-FE) — MENUJU KE SISTEM KUNCI STEERING
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (KONDISI LOCK STEERING): Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Periksa Data List untuk memastikan fungsi steering lock.
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: D64-18 (SLP) - D56-4 (SLP1)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D64-18 (SLP) atau D56-4 (SLP1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Main Body: Switch Steering Unlock (Kondisi steering lock / ON atau OFF)` : **ON: Steering tidak terkunci OFF: Steering terkunci**
  - `[STARTING 1NZ-FE] Tahanan standar: D34-18 (SLP) - D22-4 (SLP1) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) - D22-5 (LIN) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D34-18 (SLP) atau D22-4 (SLP1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) atau D22-5 (LIN) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2286` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Sinyal Runnable Malfungsi (Dokumen: RM000000YD400AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sinyal Runnable Malfungsi (Dokumen: RM000000YD401NX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sinyal Runnable Malfungsi (Dokumen: RM000000YD4079X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Sistem SFI (1NZ-FE) Wire harness; Kondisi Deteksi: Informasi kabel dan informasi CAN antara main body ECU dan ECM tidak konsisten; [STARTING 1NZ-FE] Area Gangguan: Sistem komunikasi CAN Main body ECU ECM Wire harness atau konektor; Kondisi Deteksi: Sinyal komunikasi serial dan sinyal komunikasi CAN dalam sirkuit antara main body ECU dan ECM tidak konsisten.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (KONDISI MESIN): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body / Main Body ECU / Data List / E/G Cond. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECM): Lepas hubungan konektor D66 main body ECU. -> Lepas hubungan konektor A21 ECM. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN ATAU TIDAK: Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Periksa apakah mesin dapat di-start dengan normal
  - Langkah 4 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 5 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 6 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STARTING 1NZ-FE) — TERUSKAN KE SISTEM SFI (1NZ-FE)
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (ENGINE RPM): Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Hidupkan mesin. -> Baca Data List sesuai tampilan prompts pada tester.
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: D66-2 (TACH) - A21-15 (TACH)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D66-2 (TACH) atau A21-15 (TACH) - Masa body` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: D36-2 (TACH) - A20-15 (TACH) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D36-2 (TACH) atau A20-15 (TACH) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2287` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Master komunikasi LIN Malfungsi (Dokumen: RM000000XEY00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Master komunikasi LIN Malfungsi (Dokumen: RM000000XEY01LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU ECU Sertifikasi Wire harness; Kondisi Deteksi: Komunikasi atau jalur komunikasi adalah abnormal antara main body ECU dan ECU sertifikasi; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Sistem engine immobiliser Wire harness Switch pengapian Fungsi entry Kunci Elektrik; [STARTING 1NZ-FE] Area Gangguan: Main body ECU ECU Sertifikasi Wire harness atau konektor; Kondisi Deteksi: Terdapat open , short ata
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECU SERTIFIKASI): Lepas hubungan konektor 4D pada main body ECU. -> Lepas hubungan konektor D60 ECU sertifikasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor ECU sertifikasi.
  - Langkah 2 (STARTING 1NZ-FE) — MEMERIKSA ECU SERTIFIKASI: Untuk sementara ganti ECU sertifikasi dengan yang baru atau yang berfungsi normal. -> Periksa ulang DTC.
  - Langkah 3 (STARTING 1NZ-FE) — SELESAI (ECU SERTIFIKASI RUSAK)
  - Langkah 4 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG ATAU TIDAK (DTC B2287): Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Hapus DTC (lihat halaman ). -> Periksa ulang DTC.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECU SERTIFIKASI): Lepas hubungan konektor 4D pada main body ECU. -> Lepas hubungan konektor D28 ECU sertifikasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor ECU sertifikasi.
  - Langkah 3 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU: Ganti main body ECU dengan yang baru atau yang berfungsi normal.
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) - D60-10 (LIN)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) atau D60-10 (LIN) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) - D28-10 (LIN) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) atau D28-10 (LIN) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2288` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Sirkuit Sinyal Steering Lock Malfungsi (Dokumen: RM000000YD300AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Sirkuit Sinyal Steering Lock Malfungsi (Dokumen: RM0000020S700QX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU Sistem steering lock Wire harness; Kondisi Deteksi: Informasi kabel dan informasi CAN antara main body ECU dan ECU pengunci steering tidak konsisten; Kondisi Deteksi: Setelah memutar switch pengapian dari off ke on (IG), steering wheel tidak unlock selama beberapa piriode waktu (ECU membebaskan steering wheel hanya ketika menerima sinyal unlock dari komunikasi LIN dan kabel); [STARTING 1NZ-FE] Area G
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (KONDISI LOCK STEERING): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body/ Main Body ECU/ Data List / Str Unlock SW. -> Baca display pada tester.
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECU KUNCI STEERING): Lepas hubungan konektor D64 main body ECU. -> Lepaskan konektor D56 pada ECU steering lock. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor ECU steering lock. -> Hubungkan kembali konektor main body ECU.
  - Langkah 3 (STARTING 1NZ-FE) — PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN ATAU TIDAK: Untuk sementara ganti main body ECU dengan yang baru atau yang berfungsi normal. -> Periksa apakah mesin dapat di-start dengan normal
  - Langkah 4 (STARTING 1NZ-FE) — SELESAI (MAIN BODY ECU RUSAK)
  - Langkah 5 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 6 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STARTING 1NZ-FE) — MENUJU KE SISTEM KUNCI STEERING
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA DARI DTC: Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Setelah semua DTC dihapus, periksa jika terjadi lagi trouble pada 18 detik sampai 22 detik setelah engine switch dip
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: D64-18 (SLP) - D56-4 (SLP1)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D64-18 (SLP) atau D56-4 (SLP1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: D34-18 (SLP) - D22-4 (SLP1) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: D34-18 (SLP) atau D22-4 (SLP1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2289` — [STARTING 1NZ-FE — SISTEM ENTRY DAN START] Key Collation Menunggu Waktu Selesai (Dokumen: RM000000XEY00AX) | [STARTING 1NZ-FE — SISTEM SMART ENTRY DAN START] Key Collation Menunggu Waktu Selesai (Dokumen: RM0000020S800RX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STARTING 1NZ-FE] Area Gangguan: Main body ECU ECU Sertifikasi Wire harness; Kondisi Deteksi: Komunikasi atau jalur komunikasi adalah abnormal antara main body ECU dan ECU sertifikasi; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Sistem engine immobiliser Wire harness Switch pengapian Fungsi entry Kunci Elektrik; [STARTING 1NZ-FE] Area Gangguan: Main body ECU Wire harness atau konektor ECU Sertifikasi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECU SERTIFIKASI): Lepas hubungan konektor 4D pada main body ECU. -> Lepas hubungan konektor D60 ECU sertifikasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor ECU sertifikasi.
  - Langkah 2 (STARTING 1NZ-FE) — MEMERIKSA ECU SERTIFIKASI: Untuk sementara ganti ECU sertifikasi dengan yang baru atau yang berfungsi normal. -> Periksa ulang DTC.
  - Langkah 3 (STARTING 1NZ-FE) — SELESAI (ECU SERTIFIKASI RUSAK)
  - Langkah 4 (STARTING 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU
  - Langkah 1 (STARTING 1NZ-FE) — PERIKSA DARI DTC: Hubungkan intelligent tester ke DLC3. -> Hidupkan engine switch (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Periksa untuk DTC B2289 (Waktu tunggu key collection berlebih) dan B2785 (Komunikasi malfungsi antara ECU yang dihub
  - Langkah 2 (STARTING 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MAIN BODY ECU - ECU SERTIFIKASI): Lepas hubungan konektor 4D pada main body ECU. -> Lepas hubungan konektor D28 ECU sertifikasi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor main body ECU. -> Hubungkan kembali konektor ECU s
  - Langkah 3 (STARTING 1NZ-FE) — GANTI MAIN BODY ECU: Ganti main body ECU dengan yang baru atau yang berfungsi normal.
- **Spesifikasi Standar Multimeter**:
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) - D60-10 (LIN)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) atau D60-10 (LIN) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-9 (LIN1) - D28-10 (LIN) (Selalu)` : **Di bawah 1 Ω**
  - `[STARTING 1NZ-FE] Tahanan standar: 4D-19 (LIN1) atau D28-10 (LIN) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2321` — [KACA DEPAN / KACA JENDELA — SISTEM KONTROL POWER WINDOW] Komunikasi ECU Pintu Sisi Pengemudi Stop (Dokumen: RM000001NLJ009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KACA DEPAN / KACA JENDELA] Area Gangguan: Motor regulator power window (sisi pengemudi) Main body ECU Wire harness; Kondisi Deteksi: Tidak ada komunikasi dari motor regulator power window (sisi pengemudi) selama lebih dari 10 detik
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KACA DEPAN / KACA JENDELA) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (MOTOR PINTU D KOMUNIKASI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body/ Main Body / Data List / Communication D-Door Motor. -> Baca hasil yang ditampilkan pada tester.
  - Langkah 2 (KACA DEPAN / KACA JENDELA) — PERIKSA HARNESS DAN KONEKTOR (ECU BODI UTAMA - MOTOR REGULATOR POWER WINDOW DEPAN RH): Lepaskan konektor F3 motor regulator power window depan assembly RH. -> Lepaskan konektor D33 pada ECU bodi utama. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor motor regulator power window depan assembly RH
  - Langkah 3 (KACA DEPAN / KACA JENDELA) — GANTI MOTOR REGULATOR POWER WINDOW DEPAN ASSEMBLY RH: Ganti motor regulator power window depan assembly RH dengan yang baru atau yang berfungsi normal (lihat halaman ).
  - Langkah 4 (KACA DEPAN / KACA JENDELA) — PERIKSA APAKAH OUTPUT DTC BERULANG (DTC B2321 DAN/ATAU B2325): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Hapus DTC. -> Periksa apakah DTC B2321 terulang dalam 10 detik atau lebih setelah switch pengapian diputar ke on (IG).
  - Langkah 5 (KACA DEPAN / KACA JENDELA) — AKHIR (MOTOR REGULATOR POWER WINDOW DEPAN ASSEMBLY RH RUSAK)
  - Langkah 6 (KACA DEPAN / KACA JENDELA) — KE SIMULASI GEJALA
  - Langkah 7 (KACA DEPAN / KACA JENDELA) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (KACA DEPAN / KACA JENDELA) — GANTI MAIN BODY ECU
- **Spesifikasi Standar Multimeter**:
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (dengan sistem smart entry dan start): F3-9 (MPX2) - D34-23 (CANP) (Selalu)` : **Di bawah 1 Ω**
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (dengan sistem smart entry dan start): F3-9 (MPX2) or D34-23 (CANP) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (tanpa sistem smart entry dan start): F3-9 (MPX2) - D33-4 (CANP) (Selalu)` : **Di bawah 1 Ω**
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (tanpa sistem smart entry dan start): F3-9 (MPX2) or D33-4 (CANP) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2325` — [KACA DEPAN / KACA JENDELA — SISTEM KONTROL POWER WINDOW] Malfungsi Bus Komunikasi LIN (Dokumen: RM000001NLJ009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KACA DEPAN / KACA JENDELA] Area Gangguan: Motor regulator power window (sisi pengemudi) Main body ECU Wire harness; Kondisi Deteksi: Tidak ada komunikasi dari motor regulator power window (sisi pengemudi) selama lebih dari 10 detik
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KACA DEPAN / KACA JENDELA) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (MOTOR PINTU D KOMUNIKASI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Pilih item menu berikut ini: Body/ Main Body / Data List / Communication D-Door Motor. -> Baca hasil yang ditampilkan pada tester.
  - Langkah 2 (KACA DEPAN / KACA JENDELA) — PERIKSA HARNESS DAN KONEKTOR (ECU BODI UTAMA - MOTOR REGULATOR POWER WINDOW DEPAN RH): Lepaskan konektor F3 motor regulator power window depan assembly RH. -> Lepaskan konektor D33 pada ECU bodi utama. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor motor regulator power window depan assembly RH
  - Langkah 3 (KACA DEPAN / KACA JENDELA) — GANTI MOTOR REGULATOR POWER WINDOW DEPAN ASSEMBLY RH: Ganti motor regulator power window depan assembly RH dengan yang baru atau yang berfungsi normal (lihat halaman ).
  - Langkah 4 (KACA DEPAN / KACA JENDELA) — PERIKSA APAKAH OUTPUT DTC BERULANG (DTC B2321 DAN/ATAU B2325): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke ON. -> Hapus DTC. -> Periksa apakah DTC B2321 terulang dalam 10 detik atau lebih setelah switch pengapian diputar ke on (IG).
  - Langkah 5 (KACA DEPAN / KACA JENDELA) — AKHIR (MOTOR REGULATOR POWER WINDOW DEPAN ASSEMBLY RH RUSAK)
  - Langkah 6 (KACA DEPAN / KACA JENDELA) — KE SIMULASI GEJALA
  - Langkah 7 (KACA DEPAN / KACA JENDELA) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (KACA DEPAN / KACA JENDELA) — GANTI MAIN BODY ECU
- **Spesifikasi Standar Multimeter**:
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (dengan sistem smart entry dan start): F3-9 (MPX2) - D34-23 (CANP) (Selalu)` : **Di bawah 1 Ω**
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (dengan sistem smart entry dan start): F3-9 (MPX2) or D34-23 (CANP) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (tanpa sistem smart entry dan start): F3-9 (MPX2) - D33-4 (CANP) (Selalu)` : **Di bawah 1 Ω**
  - `[KACA DEPAN / KACA JENDELA] Tahanan standar (tanpa sistem smart entry dan start): F3-9 (MPX2) or D33-4 (CANP) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2780` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Tekan Switch / Switch Peringatan Kunci Unlock Malfungsi (Dokumen: RM000001GV0012X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Tekan Switch / Switch Peringatan Kunci Unlock Malfungsi (Dokume
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Wire harness atau konektor Switch peringatan unlock ECU kunci transponder; Kondisi Deteksi: "Switch peringatan unlock ON" tidak terdeteksi bila switch pengapian ON.; [ENGINE IMMOBILISER] Area Gangguan: Switch peringatan unlock assembly Wire harness ECU kunci transponder; Kondisi Deteksi: Switch peringatan unlock ON tidak terdeteksi ketika switch pengapian ON
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Masuk ke menu berikut ini: Body / Immobiliser / Data List. -> Sesuai dengan yang ditampilkan pada tester, baca Data List.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA SWITCH PERINGATAN UNLOCK: Lepas switch peringatan unlock (Lihat halaman ). -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Pasang kembali switch peringatan unlock
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (SWITCH PERINGATAN UNLOCK ASSEMBLY - MASA BODI): Lepas hubungan konektor D19 switch peringatan unlock. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor switch peringatan unlock.
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ECU KUNCI TRANSPONDER - SWITCH PERINGATAN UNLOCK): Lepas hubungan konektor D23 ECU kunci transponder. -> Lepas hubungan konektor switch peringatan unlock. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor ECU kunci transponder. -> Hubungkan kemba
  - Langkah 5 (ENGINE IMMOBILISER) — GANTI ECU KUNCI TRANSPONDER
  - Langkah 6 (ENGINE IMMOBILISER) — GANTI SWITCH PERINGATAN UNLOCK
  - Langkah 7 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (ENGINE IMMOBILISER) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dengan kunci yang tidak dapat menghidupkan mesin. -> Pada Intelligent tester, masuk (enter) ke menu berikut: DIAGNOSIS/OBD MOBD/DATA LIST/IMMOBILISER/KEY SW. Baca nilai.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan Standar: 1 - 2 (Switch ditekan (Set kunci))` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: 1 - 2 (Switch bebas (Kunci dilepas))` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D19-2 - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-3 (KSW) - D19-1 (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D19-1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: 1 - 2 (Ditekan)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: 1 - 2 (Bebas)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: D19-2 - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `B2781` — [STEERING COLUMN — SISTEM KUNCI STEERING] Open / Short dalam Steering Lock ECU (Dokumen: RM000000YQZ005X) | [STEERING COLUMN — SISTEM KUNCI STEERING] Open / Short dalam Steering Lock ECU (Dokumen: RM000000YQZ00SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STEERING COLUMN] Area Gangguan: Aktuator kunci kemudi assembly (ECU steering lock) Harness atau konektor dari jalur LIN bus ECU Sertifikasi; Kondisi Deteksi: Malfungsi sirkuit power motor penggerak steering lock Kedua sesor posisi lock dan unlock mendeteksi (ON)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STEERING COLUMN) — PERIKSA DTC (ECU SERTIFIKASI): Hubungkan intelligent tester ke DLC3. -> Tekan switch mesin ke-on (IG) dan hidupkan tester. -> Baca DTC pada ECU sertifikasi dengan mengikuti prompt yang ditampilkan pada intelligent tester.
  - Langkah 2 (STEERING COLUMN) — GANTI AKTUATOR KUNCI STEERING ASSEMBLY
  - Langkah 3 (STEERING COLUMN) — PERIKSA SISTEM KOMUNIKASI (LIN)
  - Langkah 4 (STEERING COLUMN) — SELESAI
  - Langkah 2 (STEERING COLUMN) — GANTI AKTUATOR STEERING LOCK ASSEMBLY (ECU STEERING LOCK)

### DTC `B2782` — [STEERING COLUMN — SISTEM KUNCI STEERING] Malfungsi ECU Kontrol Power Source (Dokumen: RM000000YR0005X) | [STEERING COLUMN — SISTEM KUNCI STEERING] Malfungsi ECU Kontrol Power Source (Dokumen: RM000000YR000SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STEERING COLUMN] Area Gangguan: Harness atau konektor Aktuator kunci kemudi assembly (ECU steering lock) Main body ECU; Kondisi Deteksi: Malfungsi sirkuit power supply IGE
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STEERING COLUMN) — PERIKSA DTC (ECU SERTIFIKASI): Hubungkan intelligent tester ke DLC3. -> Tekan switch mesin ke-on (IG) dan hidupkan tester. -> Baca DTC pada ECU sertifikasi dengan mengikuti prompt yang ditampilkan pada intelligent tester.
  - Langkah 2 (STEERING COLUMN) — PERIKSA AKTUATOR STEERING LOCK ASSEMBLY: Ukur voltase.
  - Langkah 3 (STEERING COLUMN) — PERIKSA HARNESS DAN KONEKTOR (AKTUATOR KUNCI KEMUDI - MASA BODI): Lepas hubungan konektor dari aktuator steering lock assembly. -> Ukur tahanan.
  - Langkah 4 (STEERING COLUMN) — PERIKSA HARNESS DAN KONEKTOR (AKTUATOR KUNCI STEERING ASSEMBLY - MAIN BODY ECU): Lepas hubungan konektor dari main body ECU. -> Ukur tahanan.
  - Langkah 5 (STEERING COLUMN) — PERIKSA SISTEM KOMUNIKASI (LIN)
  - Langkah 6 (STEERING COLUMN) — GANTI AKTUATOR KUNCI STEERING ASSEMBLY
  - Langkah 7 (STEERING COLUMN) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (STEERING COLUMN) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[STEERING COLUMN] Voltase standar: IGE (D56-3) - SGND (D56-2) (Switch mesin off)` : **10 sampai 14 V**
  - `[STEERING COLUMN] Voltase standar: IGE (D56-3) - SGND (D56-2) (Putar engine switch dari off ke-on (IG))` : **Motor tidak aktif: 10 sampai 14 V ↓ Motor aktif : Di bawah 1 V ↓ Motor tidak aktif: 10 sampai 14 V**
  - `[STEERING COLUMN] Voltase standar: IGE (D56-3) - SGND (D56-2) (Switch mesin on (IG))` : **10 sampai 14 V**
  - `[STEERING COLUMN] Voltase standar: IGE (D56-3) - SGND (D56-2) (Setel shift lever ke posisi P ↓ Putar engine switch ke-off ↓ Buka pintu penge` : **Motor tidak aktif: 10 sampai 14 V ↓ Motor aktif : Di bawah 1 V ↓ Motor tidak aktif: 10 sampai 14 V**
  - `[STEERING COLUMN] Tahanan standar: SGND (D56-2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[STEERING COLUMN] Tahanan standar: IGE (D56-3) - SLR+ (D64-7) (Selalu)` : **Di bawah 1 Ω**
  - `[STEERING COLUMN] Tahanan standar: IGE (D56-3) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[STEERING COLUMN] Voltase standar: D22-3 (IGE) - D22-1 (GND) (Switch mesin off)` : **11 sampai 14 V**

### DTC `B2784` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Koil Antena Open / Short (Dokumen: RM000000QYJ00BX) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Koil Antena Open / Short (Dokumen: RM000001GV5011X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMM
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: ECU Sertifikasi Switch pengapian; Kondisi Deteksi: Koil Antenna terbuka/pendek; [ENGINE IMMOBILISER] Area Gangguan: Wire harness atau konektor Amplifier kunci transponder ECU kunci transponder; Kondisi Deteksi: Ketika melakukan set/unset immobiliser, sirkuit koil antena di-open atau short-kan selama 5 detik. Ketika melakukan set/unset immobiliser, switch mesin tidak dihubungkan selama 5 detik.; [ENGINE IMMOBILI
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DTC: Hapus DTC (lihat halaman ). -> Periksa ulang dari adanya DTC.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA IGNITION SWITCH ASSEMBLY: Seteleh mengganti switch pengapian dengan switch yang normal, periksa apakah mesin dapat di-start.
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI ECU SERTIFIKASI
  - Langkah 4 (ENGINE IMMOBILISER) — NORMAL
  - Langkah 5 (ENGINE IMMOBILISER) — SELESAI (SWITCH PENGAPIAN RUSAK)
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ECU KUNCI TRANSPONDER - AMPLIFIER KUNCI TRANSPONDER): Lepas hubungan konektor D23 ECU kunci transponder. -> Lepas hubungan konektor D24 amplifier kunci transponder. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali amplifier dan konektor ECU.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA ECU KUNCI TRANSPONDER (POWER SOURCE AMPLIFIER KUNCI TRANSPONDER DAN MASA): Ukur voltase dan tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI AMPLIFIER KUNCI TRANSPONDER: Ganti sementara amplifier kunci transponder dengan yang baru atau yang berfungsi normal (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-4 (TXCT) - D24-5 (TXCT) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-5 (AGND) - D24-7 (AGND) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-14 (VC5) - D24-1 (VC5) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-15 (CODE) - D24-4 (CODE) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-4 (TXCT) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-5 (AGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-14 (VC5) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-15 (CODE) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2785` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Malfungsi Komunikasi antara ECU yang Dihubungkan oleh LIN (Dokumen: RM000001002009X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Malfungsi Komunikasi antara ECU yang Dihubungkan oleh LIN (
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: ECU Sertifikasi ID code box Main body ECU ECU kunci kemudi Open atau short dalam wire harness antar ECU; Kondisi Deteksi: Komunikasi LIN dari ECU sertifikasi berhenti untuk jangka waktu tertentu.; [ENGINE IMMOBILISER] Area Gangguan: ECU Sertifikasi ID code box Main body ECU ECU kunci kemudi Wire harness; Kondisi Deteksi: Kesalahan dalam komunikasi LIN antara ECU dan terdapat open atau short dalam line komunikas
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DTC: Hapus DTC (lihat halaman ). -> Periksa ulang dari adanya DTC.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (JALUR KOMUNIKASI LIN DAN MASA BODI): Lepas hubungan konektor D56, D58, D60 dan 4D ECU. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor ECU.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA ECU SERTIFIKASI: Setelah penggantian ECU sertifikasi dengan yang normal, periksa DTC.
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA MAIN BODY ECU: Setelah penggantian main body ECU dengan yang normal, periksa DTC.
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA ECU KUNCI KEMUDI: Setelah penggantian ECU kunci kemudi dengan yang normal, periksa DTC.
  - Langkah 6 (ENGINE IMMOBILISER) — GANTI ID KODE BOX
  - Langkah 7 (ENGINE IMMOBILISER) — NORMAL
  - Langkah 8 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-10 (LIN) - D58-3 (LIN1)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-10 (LIN) - 4D-9 (LIN1)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-10 (LIN) - D56-5 (LIN)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-10 (LIN), D58-3 (LIN1), 4D-9 (LIN1) atau D56-5 (LIN) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-10 (LIN) - D24-3 (LIN1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-10 (LIN) - 4D-9 (LIN1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-10 (LIN) - D22-5 (LIN) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-10 (LIN), D24-3 (LIN1), 4D-9 (LIN1) atau D22-5 (LIN) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2786` — [STEERING COLUMN — SISTEM KUNCI STEERING] Tidak Ada Respon dari ECU Kunci Steering (Dokumen: RM000001003009X) | [STEERING COLUMN — SISTEM KUNCI STEERING] Tidak Ada Respon dari ECU Kunci Steering (Dokumen: RM00000100300RX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STEERING COLUMN] Area Gangguan: Wire harness ECU Sertifikasi Aktuator kunci kemudi assembly (ECU steering lock); Kondisi Deteksi: ECU sertifikasi tidak menerima sinyal komunikasi LIN dari ECU steering lock selama10 detik.; [STEERING COLUMN] Area Gangguan: Harness atau konektor ECU Sertifikasi Aktuator kunci kemudi assembly (ECU steering lock)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STEERING COLUMN) — PERIKSA DTC: Hubungkan intelligent tester ke DLC3. -> Tekan switch mesin ke-on (IG) dan hidupkan tester. -> Hapus DTC pada ECU sertifikasi dengan mengikuti tampilan prompt pada intelligent tester. -> Periksa ulang DTC.
  - Langkah 2 (STEERING COLUMN) — PERIKSA HARNESS DAN KONEKTOR (ECU SERTIFIKASI - AKTUATOR STEERING LOCK ASSEMBKY): Lepas hubungan konektor dari ECU sertifikasi dan aktuator steering lock assembly. -> Ukur tahanan. -> Hubungkan kembali konektor.
  - Langkah 3 (STEERING COLUMN) — PERIKSA DTC (ECU SERTIFIKASI): Setelah penggantian ECU sertifikasi dengan yang normal, periksa DTC.
  - Langkah 4 (STEERING COLUMN) — GANTI AKTUATOR KUNCI STEERING ASSEMBLY
  - Langkah 5 (STEERING COLUMN) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 6 (STEERING COLUMN) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (STEERING COLUMN) — GANTI ECU SERTIFIKASI
  - Langkah 2 (STEERING COLUMN) — PERIKSA KABEL (HARNESS) DAN KONEKTOR (ECU SERTIFIKASI - STEERING LOCK ECU): Lepaskan konektor dari ECU sertifikasi dan ECU steering lock. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor.
- **Spesifikasi Standar Multimeter**:
  - `[STEERING COLUMN] Tahanan standar: LIN (D60-10) - LIN (D56-5)` : **Di bawah 1 Ω**
  - `[STEERING COLUMN] Tahanan standar: LIN (D56-5) - Masa bodi` : **10 kΩ atau lebih**
  - `[STEERING COLUMN] Tahanan standar: D28-10 (LIN) - D22-5 (LIN) (Selalu)` : **Di bawah 1 Ω**
  - `[STEERING COLUMN] Tahanan standar: D28-10 (LIN) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2788` — [STEERING COLUMN — SISTEM KUNCI STEERING] Malfungsi Sinyal IG2 (Dokumen: RM000000YR1005X) | [STEERING COLUMN — SISTEM KUNCI STEERING] Malfungsi Sinyal IG2 (Dokumen: RM000000YR100SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [STEERING COLUMN] Area Gangguan: Harness atau konektor Aktuator kunci kemudi assembly (ECU steering lock) Sirkuit relay IG2; Kondisi Deteksi: Open atau short dalam sirkuit sinyal IG2
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (STEERING COLUMN) — PERIKSA AKTUATOR STEERING LOCK ASSEMBLY: Ukur voltase.
  - Langkah 2 (STEERING COLUMN) — PERIKSA HARNESS DAN KONEKTOR (AKTUATOR KUNCI KEMUDI - MASA BODI): Lepas hubungan konektor dari aktuator steering lock assembly. -> Ukur tahanan.
  - Langkah 3 (STEERING COLUMN) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 4 (STEERING COLUMN) — GANTI AKTUATOR KUNCI STEERING ASSEMBLY
  - Langkah 5 (STEERING COLUMN) — PERIKSA SIRKUIT RELAY (RELAY IG2)
  - Langkah 1 (STEERING COLUMN) — PERIKSA AKTUATOR STEERING LOCK ASSEMBLY (ECU STEERING LOCK): Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (STEERING COLUMN) — PERIKSA HARNESS DAN KONNEKTOR (ECU STEERING LOCK - MASA BODI): Lepaskan konektor dari ECU steering lock. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (STEERING COLUMN) — GANTI AKTUATOR STEERING LOCK ASSEMBLY (ECU STEERING LOCK)
- **Spesifikasi Standar Multimeter**:
  - `[STEERING COLUMN] Voltase standar: IG2 (D56-6) - Masa bodi (Switch mesin on (IG))` : **10 sampai 14 V**
  - `[STEERING COLUMN] Voltase standar: IG2 (D56-6) - Masa bodi (Switch mesin off)` : **Di bawah 1 V**
  - `[STEERING COLUMN] Tahanan standar: GND (D56-1) - Masa bod (Selalu)` : **Di bawah 1 Ω**
  - `[STEERING COLUMN] Tahanan standar: SGND (D56-2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[STEERING COLUMN] Voltase standar: D22-6 (IG2) - Masa bodi (Switch mesin on (IG))` : **11 sampai 14 V**
  - `[STEERING COLUMN] Voltase standar: D22-6 (IG2) - Masa bodi (Switch mesin off)` : **Di bawah 1 V**
  - `[STEERING COLUMN] Tahanan standar: D22-1 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[STEERING COLUMN] Tahanan standar: D22-2 (SGND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `B2789` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Tidak ada Respon dari ID BOX (Dokumen: RM000000Y7V008X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Tidak ada Respon dari ID BOX (Dokumen: RM000000Y7V00QX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: ID code box ECU Sertifikasi Open atau short dalam wire harness antar ECU; Kondisi Deteksi: ECU sertifikasi tidak menerima sinyal komunikasi dari ID code box melalui LIN selama 10 detik.; [ENGINE IMMOBILISER] Area Gangguan: ID code box ECU Sertifikasi Wire harness; Kondisi Deteksi: Komunikasi antra ECU sertifikasi daN ID code box selama lebih dari 10 detik.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DTC: Hapus DTC (lihat halaman ). -> Periksa ulang dari adanya DTC.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA KABEL (HARNESS) DAN KONEKTOR (ECU SERTIFIKASI - ID CODE BOX): Lepas hubungan konektor D60 ECU sertifikasi. -> Lepas hubungan konektor D58 ID code box. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor ECU sertifikasi. -> Hubungkan kembali konektor ID code box.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA ECU SERTIFIKASI: Setelah penggantian ECU sertifikasi dengan yang normal, periksa DTC.
  - Langkah 4 (ENGINE IMMOBILISER) — SELESAI (ECU SERTIFIKASI RUSAK)
  - Langkah 5 (ENGINE IMMOBILISER) — NORMAL
  - Langkah 6 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE IMMOBILISER) — GANTI ID KODE BOX
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Hapus DTC (lihat halaman ). -> Periksa kembali dari DTC (lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-10 (LIN) - D58-3 (LIN1)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-10 (LIN) atau D58-3 (LIN1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-10 (LIN) - D24-3 (LIN1) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-10 (LIN) atau D24-3 (LIN1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: D24-8 (GND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Voltase standar: D24-1 (+B) - Masa bodi (Selalu)` : **11 sampai 14 V**

### DTC `B278A` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Hubung Pendek (Short) ke GND dalam Sirkuit Power Source Sistem Immobiliser (Dokumen: RM000000TUF00AX) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Hubung Pendek (Short) ke GND dalam Sirkuit
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Wire harness Switch pengapian ECU Sertifikasi; Kondisi Deteksi: Line sumber catu daya switch pengapian hubung terbuka atau hubung pendek.; [ENGINE IMMOBILISER] Area Gangguan: Wire harness Switch mesin ECU Sertifikasi; Kondisi Deteksi: Line pensuplai power source engine switch terjadi open atau short.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA KABEL (HARNESS) DAN KONEKTOR (ECU SERTIFIKASI - SWITCH PENGAPIAN): Lepas hubungan konektor D55 switch pengapian. -> Lepas hubungan konektor D60 ECU sertifikasi. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor switch pengapian. -> Hubungkan kembali konektor ECU sertifikasi.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA IGNITION SWITCH: Seteleh mengganti switch pengapian dengan switch yang normal, periksa apakah mesin dapat di-start.
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI ECU SERTIFIKASI
  - Langkah 4 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (ENGINE IMMOBILISER) — SELESAI (SWITCH PENGAPIAN RUSAK)
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA KABEL (HARNESS) DAN KONEKTOR (ECU SERTIFIKASI - ENGINE SWITCH): Lepas hubungan konektor D18 engine switch. -> Lepas hubungan konektor D28 ECU sertifikasi. -> Periksa tahanan. -> Hubungkan kembali konektor engine switch. -> Hubungkan kembali konektor ECU sertifikasi.
  - Langkah 2 (ENGINE IMMOBILISER) — GANTI ENGINE SWITCH: Ganti engine switch dengan yang baru (lihat halaman ).
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Hapus DTC (lihat halaman ). -> Periksa ulang dari DTC.
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-30 (VC5) - D55-14 (VC5)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-40 (AGND) - D55-8 (AGND)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-30 (VC5) atau D55-14 (VC5) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: D60-40 (AGND) atau D55-8 (AGND) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-30 (VC5) - D18-14 (VC5) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-40 (AGND) - D18-8 (AGND) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-17 (E) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: D28-30 (VC5) atau D18-14 (VC5) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2790` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Malfungsi ID BOX EEPROM (Dokumen: RM000000TUG009X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Malfungsi ID BOX EEPROM (Dokumen: RM000000TUG00WX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: ID code box; Kondisi Deteksi: ID code box mendeteksi malfungsi internal
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — GANTI ID KODE BOX
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI

### DTC `B2791` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Kesalahan Kondisi Komunikasi antara ECM (Dokumen: RM000001004009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Wire harness ID code box ECM; Kondisi Deteksi: ID code box tidak merespon ke sinyal permintaan verifikasi dari ECM. Kesalahan komunikasi antara ID code box dan ECM Malfungsi jalur komunikasi Verifikasi kode ID salah
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA ENGINE STARTING: Periksa bahwa switch pengapian dapat diputar ke on (IG) dan start mesin.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ID CODE BOX - ECM): Lepas hubungan konektor D58 ID code box. -> Lepas hubungan konektor A21 ECM. -> Ukur tahanan pada konektor sisi wire harness. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor ID code box.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA ID CODE BOX: Hapus DTC (Lihat halaman ). -> Setelah penggantian ID code box dengan yang normal, periksa DTC.
  - Langkah 4 (ENGINE IMMOBILISER) — SELESAI (ID CODE BOX RUSAK)
  - Langkah 5 (ENGINE IMMOBILISER) — SELESAI (SISTEM NORMAL)
  - Langkah 6 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (ENGINE IMMOBILISER) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: EFII (D58-5) - IMO (A21-10)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: EFIO (D58-6) - IMI (A21-11)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: EGND (D58-7) - E0M (A21-9)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: EFII (D58-5) atau IMO (A21-10) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: EFIO (D58-6) atau IMI (A21-11) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B2793` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Chip Transponder Malfungsi (Dokumen: RM000001GV100VX) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Chip Transponder Malfungsi (Dokumen: RM0000012F9008X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci; Kondisi Deteksi: Bila mencoba melakukan registerasi sebuah kode ID yang tidak selesai secara normal.; Kondisi Deteksi: Sebuah kunci yang teregisterasi dimasukkan ke dalam silinder kunci pengapian. tetapi pembanding kunci menunjukkan bahwa kode keamanan tidak tepat.; Kondisi Deteksi: Sebuah kunci dengan kode ID berbeda (kunci tidak teregisterasi) dimasukan ke dalam silinder kunci pengapian.; Kondisi Detek
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (ENGINE IMMOBILISER) — REGISTRASI ULANG KUNCI: Regristrasi kunci kode dengan ECU kunci transponder.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA START MESIN: Periksa bahwa mesin dapat dihidupkan.
  - Langkah 4 (ENGINE IMMOBILISER) — GANTI KUNCI
  - Langkah 5 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 1 (ENGINE IMMOBILISER) — REGISTRASI ULANG KUNCI: Hapus DTC (Lihat halaman ). -> Regristrasi ulang kunci dan periksa bahwa mesin dapat dihidupkan dengan kunci itu.
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI (PEMERIKSAAN SELESAI)
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI KUNCI

### DTC `B2794` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Kode Encryption tidak match (Dokumen: RM000001GV100VX) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Kode Encryption tidak match (Dokumen: RM0000012FA008X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci; Kondisi Deteksi: Bila mencoba melakukan registerasi sebuah kode ID yang tidak selesai secara normal.; Kondisi Deteksi: Sebuah kunci yang teregisterasi dimasukkan ke dalam silinder kunci pengapian. tetapi pembanding kunci menunjukkan bahwa kode keamanan tidak tepat.; Kondisi Deteksi: Sebuah kunci dengan kode ID berbeda (kunci tidak teregisterasi) dimasukan ke dalam silinder kunci pengapian.; Kondisi Detek
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (ENGINE IMMOBILISER) — REGISTRASI ULANG KUNCI: Regristrasi kunci kode dengan ECU kunci transponder.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA START MESIN: Periksa bahwa mesin dapat dihidupkan.
  - Langkah 4 (ENGINE IMMOBILISER) — GANTI KUNCI
  - Langkah 5 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 1 (ENGINE IMMOBILISER) — GANTI KUNCI: Ganti kunci
  - Langkah 2 (ENGINE IMMOBILISER) — PENDAFTARAN KUNCI: Registrasi kunci.
  - Langkah 3 (ENGINE IMMOBILISER) — SELESAI

### DTC `B2795` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Kode kunci tidak match (Dokumen: RM000001GV100VX) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Kode kunci tidak match (Dokumen: RM0000012F5008X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci; Kondisi Deteksi: Bila mencoba melakukan registerasi sebuah kode ID yang tidak selesai secara normal.; Kondisi Deteksi: Sebuah kunci yang teregisterasi dimasukkan ke dalam silinder kunci pengapian. tetapi pembanding kunci menunjukkan bahwa kode keamanan tidak tepat.; Kondisi Deteksi: Sebuah kunci dengan kode ID berbeda (kunci tidak teregisterasi) dimasukan ke dalam silinder kunci pengapian.; Kondisi Detek
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 2 (ENGINE IMMOBILISER) — REGISTRASI ULANG KUNCI: Regristrasi kunci kode dengan ECU kunci transponder.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA START MESIN: Periksa bahwa mesin dapat dihidupkan.
  - Langkah 4 (ENGINE IMMOBILISER) — GANTI KUNCI
  - Langkah 5 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 1 (ENGINE IMMOBILISER) — HAPUS DTC DAN MASUKKAN SEMUA KUNCI YANG BISA DIPAKAI UNTUK PERIKSA APAKAH MESIN DAPAT DIHIDUPKAN ATAU TIDAK: Hapus DTC dan masukkan semua kunci yang bisa dipakai untuk memeriksa apakah mesin dapat dihidupkan atau tidak
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI (KARENA REGISTRASI ULANG KUNCI)
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI KUNCI YANG TAK DAPAT MENGHIDUPKAN MESIN

### DTC `B2796` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Tidak ada Komunikasi dalam Sistem Immobiliser (Dokumen: RM000001GUX012X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Tidak ada Komunikasi dalam Sistem Immobiliser (Dokumen: RM0000012F6008X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci Amplifier kunci transponder ECU kunci transponder Wire harness atau konektor; Kondisi Deteksi: Sebuah kunci tanpa kode ID (tanpa chip IC komunikasi) dimasukan ke dalam silinder kunci pengapian. Komunikasi tidak terjadi dalam waktu selama sekitar20 detik setelah kunci dimasukkan.; [ENGINE IMMOBILISER] Area Gangguan: Kunci Wire harness Amplifier kunci transponder ECU kunci transponder; Kondisi Deteksi: Tida
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Periksa apakah mesin dapat dihidupkan dengan kunci kendaraan yang telah diregisterasi.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ECU KUNCI TRANSPONDER - AMPLIFIER KUNCI TRANSPONDER): Lepas hubungan konektor D23 ECU. -> Lepas hubungan konektor D24 amplifier. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor ECU. -> Hubungkan kembali konektor amplifier.
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI AMPLIFIER KUNCI TRANSPONDER: Ganti amplifier kunci transponder (Lihat halaman ).
  - Langkah 4 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 6 (ENGINE IMMOBILISER) — GANTI ECU KUNCI TRANSPONDER
  - Langkah 7 (ENGINE IMMOBILISER) — SELESAI (AMPLIFIER KUNCI TRANSPONDER RUSAK)
  - Langkah 8 (ENGINE IMMOBILISER) — REGRISTRASI ULANG ATAU GANTI KUNCI YANG TIDAK DAPAT MENGHIDUPKAN MESIN
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-4 (TXCT) - D24-5 (TXCT) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-5 (AGND) - D24-7 (AGND) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-14 (VC5) - D24-1 (VC5) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-15 (CODE) - D24-4 (CODE) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-4 (TXCT) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-5 (AGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-14 (VC5) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-15 (CODE) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2797` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Malfungsi Komunikasi No. 1 (Dokumen: RM000001GUY012X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Malfungsi Komunikasi No. 1 (Dokumen: RM0000012F7008X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci Amplifier kunci transponder ECU kunci transponder; Kondisi Deteksi: Terjadi error komunikasi selama sekitar20 detik setelah kunci dimasukkan.; [ENGINE IMMOBILISER] Area Gangguan: Kunci Wire harness Amplifier kunci transponder ECU kunci transponder; Kondisi Deteksi: Kunci diletakkan berdekatan satu sama lain, atau terjadi noise dalam line komunikasi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA KUNCI: Periksa apakah kunci pengapian yang digunakan berdekatan dengan kunci pengapian yang lain, seperti ditunjukkan dalam gambar. Juga, periksa apakah ring kunci berhubungan dengan pegangan kunci.
  - Langkah 2 (ENGINE IMMOBILISER) — BEBASKAN SUMBER NOISE: Pisahkan kunci dari yang lain, atau lepas ring kunci.
  - Langkah 3 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Masukan kunci ke dalam silinder kunci pengapian dan lepas kunci. -> Periksa DTC (Lihat halaman ).
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Periksa apakah mesin dapat dihidupkan dengan kunci kendaraan yang telah diregisterasi.
  - Langkah 6 (ENGINE IMMOBILISER) — GANTI AMPLIFIER KUNCI TRANSPONDER: Ganti amplifier kunci transponder (Lihat halaman ).
  - Langkah 7 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 8 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Masukan kunci ke dalam silinder kunci pengapian dan lepas kunci. Ulangi untuk semua kunci yang lain dari kendaraan. -> Periksa DTC (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari open): D53-15 (CODE) - D54-4 (CODE) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari short): D53-15 (CODE) atau D54-4 (CODE) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2798` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Malfungsi Komunikasi No. 2 (Dokumen: RM000001GUY012X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Malfungsi Komunikasi No. 2 (Dokumen: RM0000012F6008X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci Amplifier kunci transponder ECU kunci transponder; Kondisi Deteksi: Terjadi error komunikasi selama sekitar20 detik setelah kunci dimasukkan.; [ENGINE IMMOBILISER] Area Gangguan: Kunci Wire harness Amplifier kunci transponder ECU kunci transponder; Kondisi Deteksi: Tidak ada komunikasi; [ENGINE IMMOBILISER] Area Gangguan: Kunci; Kondisi Deteksi: Komunikasi error
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA KUNCI: Periksa apakah kunci pengapian yang digunakan berdekatan dengan kunci pengapian yang lain, seperti ditunjukkan dalam gambar. Juga, periksa apakah ring kunci berhubungan dengan pegangan kunci.
  - Langkah 2 (ENGINE IMMOBILISER) — BEBASKAN SUMBER NOISE: Pisahkan kunci dari yang lain, atau lepas ring kunci.
  - Langkah 3 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Masukan kunci ke dalam silinder kunci pengapian dan lepas kunci. -> Periksa DTC (Lihat halaman ).
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Periksa apakah mesin dapat dihidupkan dengan kunci kendaraan yang telah diregisterasi.
  - Langkah 6 (ENGINE IMMOBILISER) — GANTI AMPLIFIER KUNCI TRANSPONDER: Ganti amplifier kunci transponder (Lihat halaman ).
  - Langkah 7 (ENGINE IMMOBILISER) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 8 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Masukan kunci ke dalam silinder kunci pengapian dan lepas kunci. Ulangi untuk semua kunci yang lain dari kendaraan. -> Periksa DTC (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari open): D53-14 (VC5) - D54-1 (VC5) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari open): D53-15 (CODE) - D54-4 (CODE) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari open): D53-4 (TXCT) - D54-5 (TXCT) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari open): D53-5 (AGND) - D54-7 (AGND) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari short): D53-14 (VC5) atau D54-1 (VC5) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari short): D53-15 (CODE) atau D54-4 (CODE) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari short): D53-4 (TXCT) atau D54-5 (TXCT) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari short): D53-5 (AGND) atau D54-7 (AGND) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B2799` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Sistem Engine Immobiliser Malfungsi (Dokumen: RM000000SJV009X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Sistem Engine Immobiliser Malfungsi (Dokumen: RM000002M6X00UX) | [ENGINE IMMOBILIS
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Wire harness ID code box ECM; [ENGINE IMMOBILISER] Area Gangguan: Wire harness atau konektor ECM ECU kunci transponder; Kondisi Deteksi: Bila pengapian adalah ON dan terjadi error komunikasi atau errpr line komunikasi antara ECM dan ECU kunci transponder selama 6 detik. Bila pengapian adalah ON dan ECM mesin menerima ID komunikasi yang berbeda selama 6 de; [ENGINE IMMOBILISER] Area Gangguan: Wire harness ECM; K
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DTC: Hapus DTC (lihat halaman ). -> Periksa ulang dari adanya DTC.
  - Langkah 2 (ENGINE IMMOBILISER) — REGISTER ULANG REGISTRASI ID KOMUNIKASI ECU (ID CODE BOX - ECM): Hapus DTC (lihat halaman ). -> Register ID komunikasi ECU antara ID code box dan ECM. -> Putar switch pengapian on (IG) dan periksa tidak ada output DTC.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ID CODE BOX - ECM): Lepas hubungan konektor D58 ID code box. -> Lepas hubungan konektor A21 ECM. -> Ukur tahanan pada konektor wire harness. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor ID code box.
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA CARA KERJA ID CODE BOX: Setelah penggantian ID code box dengan yang normal, periksa apakah mesin dapat di-start.
  - Langkah 5 (ENGINE IMMOBILISER) — GANTI ECM
  - Langkah 6 (ENGINE IMMOBILISER) — NORMAL
  - Langkah 7 (ENGINE IMMOBILISER) — SELESAI (PROBLEM DISEBABKAN OLEH KESALAHAN REGISTRASI)
  - Langkah 8 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: EFII (D58-5) - IMO (A21-10)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: EFIO (D58-6) - IMI (A21-11)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: EGND (D58-7) - E0M (A21-9)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: EFII (D58-5) atau IMO (A21-10) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: EFIO (D58-6) atau IMI (A21-11) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-12 (EFII) - A21-10 (IMO) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-13 (EFIO) - A21-11 (IMI) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan Standar: D23-12 (EFII) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `B279A` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] High Fixation Line Komunikasi Sistem Anti Pencurian (Dokumen: RM000002X2F003X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] High Fixation Line Komunikasi Sistem Anti Pencurian (Dokumen: RM00
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Wire harness ID code box ECM; Kondisi Deteksi: Bila line komunikasi (EFIO-IMI) antara ECM dan ID code box macet pada HI output selama 6 detik atau lebih.; [ENGINE IMMOBILISER] Area Gangguan: Wire harness ECU kunci transponder ECM; Kondisi Deteksi: Bila line komunikasi (EFIO-IMI) antara ECM dan ECU kunci transponder macet pada HI output selama 6 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Hapus DTC (lihat halaman ). -> Periksa apakah B279A tidak ditampilkan.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ID CODE BOX - ECM): Lepaskan konektor A20 ECM. -> Lepas hubungan konektor D24 ID code box. -> Tekan switch mesin ke on (IG). -> Ukur voltase antara terminal IMI dari konektor ECM dan Masa bodi. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungka
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA ID CODE BOX (INPUT): Ukur bentuk gelombang.
  - Langkah 4 (ENGINE IMMOBILISER) — GANTI ECM
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA ID CODE BOX (POWER SOURCE): Tekan switch mesin ke on (IG). -> Ukur voltase antara konektor dari terminal ID code box.
  - Langkah 6 (ENGINE IMMOBILISER) — GANTI ID KODE BOX
  - Langkah 7 (ENGINE IMMOBILISER) — LANJUTKAN KE BAGAN DTC
  - Langkah 8 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Voltase standar: A20-11 (IMI) - Masa bodi (Switch mesin on (IG))` : **Di bawah 1 V**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari open): A20-11 (IMI) - D24-6 (EFIO) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Voltase standar: D24-1 (+B) - D24-8 (GND) (Switch mesin on (IG))` : **11 sampai 14 V**
  - `[ENGINE IMMOBILISER] Voltase standar: A20-11 (IMI) - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari open): A20-11 (IMI) - D53-13 (EFIO) (Selalu)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar (Periksa dari short): A20-11 (IMI) atau D53-13 (EFIO) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Voltase standar: D53-1 (+B) - D53-16 (GND) (Switch Pengapian ON)` : **11 sampai 14 V**

### DTC `B279C` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (dengan Sistem Smart Entry dan Start)] Deteksi Adanya Sistem Anti Pencurian (Dokumen: RM000002X2G003X) | [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER (tanpa Sistem Smart Entry dan Start)] Deteksi Adanya Sistem Anti Pencurian (Dokumen: RM000002X2G002X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: ECM; Kondisi Deteksi: ECM untuk kendaraan tanpa sistem smart entry dan start yang dipasang pada kendaraan dengan sistem smart entry dan start.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DARI DTC: Hapus DTC (lihat halaman ). -> Periksa apakah B279C tidak ditampilkan.
  - Langkah 2 (ENGINE IMMOBILISER) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI ECM YANG ADA DENGAN ECM YANG TEPAT
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA DTC: Hapus DTC (lihat halaman ). -> Periksa apakah B279C tidak ditampilkan.
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI (SISTEM NORMAL)
  - Langkah 3 (ENGINE IMMOBILISER) — GANTI ECM

### DTC `C0200` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 31] Sinyal Speed Sensor Roda Kanan Depan (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 31] Sinyal Speed Sensor Roda Kanan Depan (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C0205` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 32] Sinyal Speed Sensor Roda Kiri Depan (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 32] Sinyal Speed Sensor Roda Kiri Depan (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C0210` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 33] Sinyal Speed Sensor Roda Kanan Belakang (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 33] Sinyal Speed Sensor Roda Kanan Belakang (Dokumen: RM000000WE300YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C0215` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 34] Sinyal Speed Sensor Roda Kiri Belakang (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 34] Sinyal Speed Sensor Roda Kiri Belakang (Dokumen: RM000000WE300YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C0226` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SFR (Dokumen: RM000000XI805RX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 21] Sirkuit Solenoid SFR (Dokumen: RM000000OS9009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SFR (Dokumen: RM000000XI805YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sirkuit solenoid Aktuator rem assembly; Kondisi Deteksi: Bila relay solenoid tetap ON dan voltase terminal IG1 adalah 17.4 V atau kurang, berarti terjadi open atau short dalam sirkuit solenoid selama 0.05 detik atau lebih.; [KONTROL REM] Area Gangguan: Aktuator rem; Kondisi Deteksi: Open atau short dalam sirkuit solenoid secara kontinu selama 0,05 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 3 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) atau lebih untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — GANTI AKTUATOR REM
  - Langkah 3 (KONTROL REM) — SELESAI
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `C0236` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SFL (Dokumen: RM000000XI805RX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 22] Sirkuit Solenoid SFL (Dokumen: RM000000OS9009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SFL (Dokumen: RM000000XI805YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sirkuit solenoid Aktuator rem assembly; Kondisi Deteksi: Bila relay solenoid tetap ON dan voltase terminal IG1 adalah 17.4 V atau kurang, berarti terjadi open atau short dalam sirkuit solenoid selama 0.05 detik atau lebih.; [KONTROL REM] Area Gangguan: Aktuator rem; Kondisi Deteksi: Open atau short dalam sirkuit solenoid secara kontinu selama 0,05 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 3 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) atau lebih untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — GANTI AKTUATOR REM
  - Langkah 3 (KONTROL REM) — SELESAI
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `C0246` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SRR (Dokumen: RM000000XI805RX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 23] Sirkuit Solenoid SRR (Dokumen: RM000000OS9009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SRR (Dokumen: RM000000XI805YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sirkuit solenoid Aktuator rem assembly; Kondisi Deteksi: Bila relay solenoid tetap ON dan voltase terminal IG1 adalah 17.4 V atau kurang, berarti terjadi open atau short dalam sirkuit solenoid selama 0.05 detik atau lebih.; [KONTROL REM] Area Gangguan: Aktuator rem; Kondisi Deteksi: Open atau short dalam sirkuit solenoid secara kontinu selama 0,05 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 3 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) atau lebih untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — GANTI AKTUATOR REM
  - Langkah 3 (KONTROL REM) — SELESAI
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `C0256` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SRL (Dokumen: RM000000XI805RX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 24] Sirkuit Solenoid SRL (Dokumen: RM000000OS9009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Sirkuit Solenoid SRL (Dokumen: RM000000XI805YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sirkuit solenoid Aktuator rem assembly; Kondisi Deteksi: Bila relay solenoid tetap ON dan voltase terminal IG1 adalah 17.4 V atau kurang, berarti terjadi open atau short dalam sirkuit solenoid selama 0.05 detik atau lebih.; [KONTROL REM] Area Gangguan: Aktuator rem; Kondisi Deteksi: Open atau short dalam sirkuit solenoid secara kontinu selama 0,05 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 3 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) atau lebih untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — GANTI AKTUATOR REM
  - Langkah 3 (KONTROL REM) — SELESAI
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada 6 km/jam (4 mph) untuk mengaktifkan pemeriksaan awal (initial check). -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `C0273` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Membuka Sirkuit Relay Motor ABS (Dokumen: RM000001JD6048X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 13] Open Circuit atau Short Circuit pada Sirkuit Relay Motor ABS (Dokumen: RM000000WEZ009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Membuka Sirkuit Relay Motor ABS (Dok
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sirkuit relay motor ABS Aktuator rem assembly (Relay motor ABS); Kondisi Deteksi: Ketika motor relay OFF, relay VSC NO. 2 tetap tertutup selama 4 detik atau lebih.; [KONTROL REM] Area Gangguan: Fuse ABS1/VSC1 Wire harness (Sirkuit +BM) Aktuator rem; Kondisi Deteksi: Ketika relay motor off, relay motor tetap tertutup selama 4 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (RELAY MOTOR ABS): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Pilih mode Active Test pada intelligent tester (Lihat halaman ). -> Periksa suara kerja dari relay motor ABS ketika mengoperasikan relay motor ABS dengan intelligent tester.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL +BM): Putar switch pengapian ke off. -> Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL GND): Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Putar switch pengapian ke off. -> Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila 
  - Langkah 5 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 6 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR(SIRKUIT +BM)
  - Langkah 7 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (SIRKUIT GND)
  - Langkah 8 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Voltase Standar: A38-24 (+BM) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A38-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-13 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A15-23 (+BM) - Masa bodi` : **10 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A15-2 (GND1) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A15-24 (GND2) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A27-24 (+BM) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A27-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `C0274` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Short dalam Sirkuit Relay Motor ABS (Dokumen: RM000001JD6048X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 14] Short ke B+ pada Sirkuit Relay Motor ABS (Dokumen: RM000000WEZ009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Short dalam Sirkuit Relay Motor ABS (Dokumen: RM0000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sirkuit relay motor ABS Aktuator rem assembly (Relay motor ABS); Kondisi Deteksi: Ketika motor relay OFF, relay VSC NO. 2 tetap tertutup selama 4 detik atau lebih.; [KONTROL REM] Area Gangguan: Fuse ABS1/VSC1 Wire harness (Sirkuit +BM) Aktuator rem; Kondisi Deteksi: Ketika relay motor off, relay motor tetap tertutup selama 4 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (RELAY MOTOR ABS): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Pilih mode Active Test pada intelligent tester (Lihat halaman ). -> Periksa suara kerja dari relay motor ABS ketika mengoperasikan relay motor ABS dengan intelligent tester.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL +BM): Putar switch pengapian ke off. -> Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL GND): Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Putar switch pengapian ke off. -> Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila 
  - Langkah 5 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 6 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR(SIRKUIT +BM)
  - Langkah 7 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (SIRKUIT GND)
  - Langkah 8 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Voltase Standar: A38-24 (+BM) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A38-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-13 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A15-23 (+BM) - Masa bodi` : **10 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A15-2 (GND1) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A15-24 (GND2) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A27-24 (+BM) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A27-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `C0278` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Membuka Solenoid ABS Relay Circuit (Dokumen: RM000000XI7050X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 11] Open Circuit atau Short Circuit pada Sirkuit Relay Solenoid ABS (Dokumen: RM000000WF0009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Membuka Solenoid ABS Relay Cir
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Solenoid ABS relay circuit Aktuator rem assembly (Relay solenoid ABS); Kondisi Deteksi: Dengan segera setelah switch pengapian diputar keON, hubungan solenoid relay ditutup selama 4.5 detik ketika relay diputar ke off.; [KONTROL REM] Area Gangguan: Fuse ABS2/VSC2 Wire harness (Sirkuit +BS) Aktuator rem; Kondisi Deteksi: Segera setelah switch pengapian diputar ke on (IG), kontak relay solenoid tertutup selama 0.2 detik
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL +BS): Lepas hubungan konektor ECU skid control. -> Periksa case konektor dan terminal dari deformasi dan korosi. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL GND): Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — KONFIRMASI ULANG DTC: Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halam
  - Langkah 4 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 5 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR(SIRKUIT +BS)
  - Langkah 6 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (SIRKUIT GND)
  - Langkah 7 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 1 (KONTROL REM) — PERIKSA FUSE (ABS2/VSC2): Lepas fuse ABS2/VSC2 dari ruang mesin R/B. -> Ukur tahanan.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Voltase Standar: A38-12 (+BS) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A38-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A15-1 (+BS) - Masa bodi` : **10 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A15-2 (GND1) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A15-24 (GND2) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A27-12 (+BS) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A27-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar: Fuse ABS2/VSC2 (Selalu)` : **Di bawah 1 Ω**

### DTC `C0279` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Short dalam Sirkuit Relay Solenoid ABS (Dokumen: RM000000XI7050X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 12] Short pada B+ dalam Solenoid ABS Relay Circuit (Dokumen: RM000000WF0009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Short dalam Sirkuit Relay Solenoid ABS (Dok
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Solenoid ABS relay circuit Aktuator rem assembly (Relay solenoid ABS); Kondisi Deteksi: Dengan segera setelah switch pengapian diputar keON, hubungan solenoid relay ditutup selama 4.5 detik ketika relay diputar ke off.; [KONTROL REM] Area Gangguan: Fuse ABS2/VSC2 Wire harness (Sirkuit +BS) Aktuator rem; Kondisi Deteksi: Segera setelah switch pengapian diputar ke on (IG), kontak relay solenoid tertutup selama 0.2 detik
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL +BS): Lepas hubungan konektor ECU skid control. -> Periksa case konektor dan terminal dari deformasi dan korosi. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL GND): Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — KONFIRMASI ULANG DTC: Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halam
  - Langkah 4 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 5 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR(SIRKUIT +BS)
  - Langkah 6 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (SIRKUIT GND)
  - Langkah 7 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 1 (KONTROL REM) — PERIKSA FUSE (ABS2/VSC2): Lepas fuse ABS2/VSC2 dari ruang mesin R/B. -> Ukur tahanan.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Voltase Standar: A38-12 (+BS) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A38-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A15-1 (+BS) - Masa bodi` : **10 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A15-2 (GND1) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A15-24 (GND2) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A27-12 (+BS) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A27-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar: Fuse ABS2/VSC2 (Selalu)` : **Di bawah 1 Ω**

### DTC `C1235` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 35] Benda Asing Menempel pada Ujung Speed Sensor Depan RH (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 35] Benda Asing Menempel pada Ujung Speed Sensor Depan RH (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C1236` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 36] Benda Asing Menempel pada Ujung Speed Sensor Depan LH (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 36] Benda Asing Menempel pada Ujung Speed Sensor Depan LH (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C1238` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 38] Benda Asing Menempel pada Ujung Speed Sensor Belakang RH (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 38] Benda Asing Menempel pada Ujung Speed Sensor Belakang RH (Dokumen: RM000000WE300YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C1239` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 39] Benda Asing Menempel pada Ujung Speed Sensor Belakang LH (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 39] Benda Asing Menempel pada Ujung Speed Sensor Belakang LH (Dokumen: RM000000WE300YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C1241` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Voltase Rendah Power Supply (Dokumen: RM000000XW6060X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 41] Voltase Positif Baterai Lemah atau Tinggi Voltase Positif Baterai Abnormal (Dokumen: RM000000OSD009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Voltas
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Baterai Sistem pengisian Sirkuit power source Sirkuit internal power source dari ECU skid control.; [KONTROL REM] Area Gangguan: Baterai Sistem pengisian Sirkuit power source Sirkit internal sumber daya ECU skid control.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA BATERAI: Pasang fuse ECU-IG. -> Periksa voltase baterai.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL IG1): Lepas hubungan konektor ECU skid control. -> Periksa case konektor dan terminal dari deformasi dan korosi. -> Putar switch pengapian ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL GND): Putar switch pengapian ke off. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halam
  - Langkah 5 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 6 (KONTROL REM) — PERIKSA ATAU GANTI BATERAI ATAU SISTEM PENGISIAN
  - Langkah 7 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (SIRKUIT IG1)
  - Langkah 8 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (SIRKUIT GND)
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Voltase Standar: A38-34 (IG1) - Masa bodi (Switch pengapian ON)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A38-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A15-25 (IG1) - Masa bodi` : **10 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: 3 - 5 (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 3 - 5 (Berikan B+ antara terminal-terminal 1 dan 2)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A15-2 (GND1) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A15-24 (GND2) - Masa bodi` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A27-34 (IG1) - Masa bodi (Switch pengapian ON)` : **11 sampai 14 V**

### DTC `C1249` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 49] Open pada Sirkuit Switch Lampu Rem (Dokumen: RM000001HY4009X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 49] Open pada Sirkuit Switch Lampu Rem (Dokumen: RM000001HY400WX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Switch lampu rem Sirkuit switch lampu rem Aktuator rem; Kondisi Deteksi: Ketika voltase terminal IGI 9.5 sampi 17.2 V, terjadi hubungan terbuka pada switch lampu rem secara kontinu selama 3 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — CEK CARA KERJA SWITCH LAMPU REM: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih mode DATA LIST pada intelligent tester. -> Periksa bahwa "Stop Lamp SW" diputar ke ON dan OFF ketika pedal rem ditekan dan dibebaskan.
  - Langkah 2 (KONTROL REM) — PERIKSA VOLTASE TERMINAL ECU SKID CONTROL (STP): Lepas hubungan konektor ECU skid control. -> Ukur voltase.
  - Langkah 3 (KONTROL REM) — PERIKSA FUSE (STOP): Cabut fuse STOP dari main body ECU. -> Ukur tahanan.
  - Langkah 4 (KONTROL REM) — PERIKSA SWITCH LAMPU REM ASSEMBLY: Lepas hubungan konektor switch lampu rem. -> Ukur tahanan.
  - Langkah 5 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SWITCH LAMPU REM): Lepaskan konektor ECU skid control dan konektor switch lampu rem. -> Ukur tahanan.
  - Langkah 6 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Periksa apakah DTC yang sama di-output (Lihat halaman ).
  - Langkah 7 (KONTROL REM) — GANTI AKTUATOR REM
  - Langkah 8 (KONTROL REM) — GANTI SWITCH LAMPU REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Voltase Standar: A15-10 (STP) - Masa bodi (Pedal rem ditekan)` : **8 sampai 14 V**
  - `[KONTROL REM] Voltase Standar: A15-10 (STP) - Masa bodi (Pedal rem dibebaskan)` : **Di bawah 4.0 V**
  - `[KONTROL REM] Tahanan Standar: 1 - 2 (Pin switch dibebaskan)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: 3 - 4 (Pin switch dibebaskan)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 - 2 (Pin switch ditekan ke dalam)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 3 - 4 (Pin switch ditekan ke dalam)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A15-10 (STP) - A13-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] OK: Pedal rem ditekan` : **ON**

### DTC `C1251` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 51] Open pada Sirkuit Pump Circuit (Dokumen: RM000001CQX008X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 51] Open pada Sirkuit Pump Circuit (Dokumen: RM000001CQX00PX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Aktuator rem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 6 km/jam (4 mph) atau lebih selama beberapa detik. -> Periksa apakah DTC yang sama di-output (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — SELESAI
  - Langkah 3 (KONTROL REM) — GANTI AKTUATOR REM
  - Langkah 2 (KONTROL REM) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `C1271` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 71] Sinyal Output Speed Sensor Depan RH Lemah (Test Mode DTC) (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 71] Sinyal Output Speed Sensor Depan RH Lemah (Test Mode DTC) (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C1272` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 72] Sinyal Output Speed Sensor Depan LH Lemah (Test Mode DTC) (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 72] Sinyal Output Speed Sensor Depan LH Lemah (Test Mode DTC) (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C1273` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 73] Sinyal Output Lemah dari Speed Sensor Belakang RH (Test Mode DTC) (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 73] Sinyal Output Lemah dari Speed Sensor Belakang RH (Test Mode DTC) (Dokumen: RM000000WE300YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C1274` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 74] Sinyal Output Lemah dari Speed Sensor Belakang LH (Test Mode DTC) (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 74] Sinyal Output Lemah dari Speed Sensor Belakang LH (Test Mode DTC) (Dokumen: RM000000WE300YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C1275` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 75] Perubahan Abnormal dalam Sinyal Output Speed Sensor Depan RH (Test Mode DTC) (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 75] Perubahan Abnormal dalam Sinyal Output Speed Sensor Depan RH (Test Mode DTC) (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C1276` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 76] Perubahan Abnormal dalam Sinyal Output Speed Sensor Depan LH (Test Mode DTC) (Dokumen: RM000000WE200AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 76] Perubahan Abnormal dalam Sinyal Output Speed Sensor Depan LH (Test Mode DTC) (Dokumen: RM000000WE200YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Speed sensor depan (open) Sirkuit speed sensor depan (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor depan Sirkuit speed sensor depan Pemasangan sensor Rotor speed sensor depan Aktuator rem; [KONTROL REM] Area Gangguan: Speed sensor depan P
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan konektor dari speed sensor.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (FRONT SPEED SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "FR (FL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Periksa bahwa baut speed sensor telah dikencangkan dengan benar.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR DEPAN: Secara visual periksa speed sensor dari perubahan bentuk dan kecacatan.
  - Langkah 7 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor (Lihat halaman ). -> Periksa ujung sensor.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Konfirmasi apakah konektor ECU skid control dan konektor speed sensor telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor speed sensor depan. -> Periksalah kedua case konektor dan terminal dari deformasi dan kor
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): A15-9 (FL+) - A11-2 (FL+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): A15-8 (FL-) - A11-1 (FL-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-31 (FR+) - A7-2 (FR+)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): A15-30 (FR-) - A7-1 (FR-)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A11-2 (FL+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Voltase Standar: A7-2 (FR+) - Masa bodi (Switch pengapian on (IG))` : **5.7 sampai 17.3 V**
  - `[KONTROL REM] Tahanan standar (LH): A15-9 (FL+) - A10-2 (FL+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan standar (LH): A15-8 (FL-) - A10-1 (FL-) (Selalu)` : **Di bawah 1 Ω**

### DTC `C1277` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 77] Perubahan Abnormal dalam Sinyal Output Speed Sensor Belakang RH (Test Mode DTC) (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 77] Perubahan Abnormal dalam Sinyal Output Speed Sensor Belakang RH (Test Mode DTC) (Dokumen: RM000000WE3
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C1278` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 78] Perubahan Abnormal dalam Sinyal Output Speed Sensor Belakang LH (Test Mode DTC) (Dokumen: RM000000WE300AX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 78] Perubahan Abnormal dalam Sinyal Output Speed Sensor Belakang LH (Test Mode DTC) (Dokumen: RM000000WE3
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sensor skid control Kabel sensor skid control Sirkuit sensor skid control Pemasangan sensor Benda asing pada rotor sensor; [KONTROL REM] Area Gangguan: Sensor skid control (open) Sirkuit sensor skid control (open); Kondisi Deteksi: Pendeteksian hanya selama test mode.; [KONTROL REM] Area Gangguan: Speed sensor belakang Sirkuit speed sensor belakang Pemasangan sensor Rotor speed sensor belakang Aktuator rem; [KONTROL R
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Menggunakan intelligent tester, periksa beberapa momentary interruption dalam wire harness dan sensor skid control.
  - Langkah 2 (KONTROL REM) — BACA NILAI MENGGUNAKAN DATA LIST (SKID CONTROL SENSOR): Hubungkan intelligent tester ke DLC3. -> Start mesin dan kemudikan kendaraan. -> Hidupkan tester. -> Baca nilai kecepatan kendaraan menggunakan intelligent tester. -> Pilih item "RR (RL) Wheel Speed" pada DATA LIST dan baca nilai yang ditam
  - Langkah 3 (KONTROL REM) — LAKUKAN PEMERIKSAAN TEST MODE (PEMERIKSAAN SINYAL): Lakukan pemeriksaan TEST MODE dan periksa dari DTC (Lihat halaman )
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 20 km/jam (12 mph) atau lebih minimal selama 60 detik. -> Periksa jika terdapat output DTC yang sama (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SENSOR SKID CONTROL: Putar switch pengapian ke OFF. -> Secara visual periksa sensor skid control dari perubahan bentuk dan kerusakan.
  - Langkah 6 (KONTROL REM) — PERIKSALAH KABEL SENSOR SKID CONTROL: Lepas hubungan kabel sensor skid control. -> Ukur tahanan.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SENSOR SKID CONTROL): Konfirmasi bahwa konektor ECU skid control dan konektor sensor skid control telah terpasang dengan benar. -> Lepaskan konektor ECU skid control dan konektor skid cpntol. -> Periksalah kedua case konektor dan terminal dari deformasi dan koro
  - Langkah 8 (KONTROL REM) — CEK SENSOR SKID CONTROL (VOLTASE INPUT): Lepaskan konektor sensor skid control. -> Putar switch pengapian ke on (IG). -> Ukur voltase.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - aJ1-2` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-1 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-1` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - aJ1-2` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (LH): a1-2 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-1` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar (RH): Z1-1 - ZJ1-2` : **10 kΩ atau lebih tinggi**

### DTC `C1401` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Depan RH Malfungsi (Dokumen: RM000000XI908TX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Depan RH Malfungsi (Dokumen: RM000000XI9096X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 2 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor depan (Lihat halaman ). -> Periksa ujung speed sensor.
  - Langkah 3 (KONTROL REM) — PERIKSA ROTOR SPEED SENSOR DEPAN: Periksa rotor speed sensor depan.
  - Langkah 4 (KONTROL REM) — GANTI SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Ganti speed sensor depan (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 6 (KONTROL REM) — GANTI BEARING AXLE HUB DEPAN: Putar switch pengapian ke off. -> Ganti bearing axle hub depan (Lihat halaman ).
  - Langkah 7 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 8 (KONTROL REM) — PASANG SPEED SENSOR DEPAN DENGAN BENAR

### DTC `C1402` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Depan LH Malfungsi (Dokumen: RM000000XI908TX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Depan LH Malfungsi (Dokumen: RM000000XI9096X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 2 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor depan (Lihat halaman ). -> Periksa ujung speed sensor.
  - Langkah 3 (KONTROL REM) — PERIKSA ROTOR SPEED SENSOR DEPAN: Periksa rotor speed sensor depan.
  - Langkah 4 (KONTROL REM) — GANTI SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Ganti speed sensor depan (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 6 (KONTROL REM) — GANTI BEARING AXLE HUB DEPAN: Putar switch pengapian ke off. -> Ganti bearing axle hub depan (Lihat halaman ).
  - Langkah 7 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 8 (KONTROL REM) — PASANG SPEED SENSOR DEPAN DENGAN BENAR

### DTC `C1403` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Belakang RH Malfungsi (Dokumen: RM000000XIA072X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Belakang RH Malfungsi (Dokumen: RM000000XIA07CX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 2 (KONTROL REM) — PERIKSA SPEED SENSOR BELAKANG: Lepaskan konektor speed sensor belakang. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 4 (KONTROL REM) — GANTI AXLE HUB BELAKANG DAN BEARING ASSEMBLY (SPEED SENSOR BELAKANG)
  - Langkah 5 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 6 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 1 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1404` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Belakang LH Malfungsi (Dokumen: RM000000XIA072X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Speed Sensor Belakang LH Malfungsi (Dokumen: RM000000XIA07CX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 2 (KONTROL REM) — PERIKSA SPEED SENSOR BELAKANG: Lepaskan konektor speed sensor belakang. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 4 (KONTROL REM) — GANTI AXLE HUB BELAKANG DAN BEARING ASSEMBLY (SPEED SENSOR BELAKANG)
  - Langkah 5 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
  - Langkah 6 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 1 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1405` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Depan RH (Dokumen: RM000000XI908UX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Depan RH (Dokumen: RM000000XI9097X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PEMERIKSAAN SPEED SENSOR DEPAN: Pasang speed sensor depan. -> Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepas hubungan konektor speed sensor depan. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (KONTROL REM) — PERIKSA ECU SKID CONTROL (INPUT SENSOR): Hubungkan kembali konektor ECU skid control. -> Putar switch pengapian ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (KONTROL REM) — GANTI SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Ganti speed sensor depan (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 2 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - A7-2 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - A7-1 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1406` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Depan LH (Dokumen: RM000000XI908UX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Depan LH (Dokumen: RM000000XI9097X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PEMERIKSAAN SPEED SENSOR DEPAN: Pasang speed sensor depan. -> Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepas hubungan konektor speed sensor depan. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR DEPAN): Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (KONTROL REM) — PERIKSA ECU SKID CONTROL (INPUT SENSOR): Hubungkan kembali konektor ECU skid control. -> Putar switch pengapian ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (KONTROL REM) — GANTI SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Ganti speed sensor depan (Lihat halaman ).
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 2 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - A7-2 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - A7-1 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1407` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Belakang RH (Dokumen: RM000000XIA073X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Belakang RH (Dokumen: RM000000XIA07DX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Sirkuit speed sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR BELAKANG DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA SPEED SENSOR BELAKANG: Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepaskan konektor speed sensor belakang. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (KABEL SPEED SENSOR): Lepas hubungan kabel speed sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR BELAKANG): Hubungkan kembali kabel speed sensor. -> Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (KONTROL REM) — PERIKSA ECU SKID CONTROL (INPUT SENSOR): Hubungkan kembali konektor ECU skid control. -> Putar switch pengapian ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 1 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-1 (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-2 (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-2 - ZJ1-1 (Selalu)` : **Di bawah 1 Ω**

### DTC `C1408` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Belakang LH (Dokumen: RM000000XIA073X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open atau Short dalam Sirkuit Speed Sensor Belakang LH (Dokumen: RM000000XIA07DX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Sirkuit speed sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR BELAKANG DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA SPEED SENSOR BELAKANG: Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepaskan konektor speed sensor belakang. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 6 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (KABEL SPEED SENSOR): Lepas hubungan kabel speed sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR BELAKANG): Hubungkan kembali kabel speed sensor. -> Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (KONTROL REM) — PERIKSA ECU SKID CONTROL (INPUT SENSOR): Hubungkan kembali konektor ECU skid control. -> Putar switch pengapian ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 1 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-1 (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-2 (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-2 - ZJ1-1 (Selalu)` : **Di bawah 1 Ω**

### DTC `C1413` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Depan RH Malfungsi (Dokumen: RM000000XI908VX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Depan RH Malfungsi (Dokumen: RM000000XI9098X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 6 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor depan (Lihat halaman ). -> Periksa ujung speed sensor.
  - Langkah 7 (KONTROL REM) — PERIKSA ROTOR SPEED SENSOR DEPAN: Periksa rotor speed sensor depan.
  - Langkah 8 (KONTROL REM) — PEMERIKSAAN SPEED SENSOR DEPAN: Pasang speed sensor depan. -> Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepas hubungan konektor speed sensor depan. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 2 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - A7-2 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - A7-1 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1414` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Depan LH Malfungsi (Dokumen: RM000000XI908VX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Depan LH Malfungsi (Dokumen: RM000000XI9098X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Sirkuit speed sensor Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH depan Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR DEPAN DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor depan telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR DEPAN: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 6 (KONTROL REM) — PERIKSA UJUNG SPEED SENSOR DEPAN: Lepas speed sensor depan (Lihat halaman ). -> Periksa ujung speed sensor.
  - Langkah 7 (KONTROL REM) — PERIKSA ROTOR SPEED SENSOR DEPAN: Periksa rotor speed sensor depan.
  - Langkah 8 (KONTROL REM) — PEMERIKSAAN SPEED SENSOR DEPAN: Pasang speed sensor depan. -> Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepas hubungan konektor speed sensor depan. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 2 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (FL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (FL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - A7-2 (FR+) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-7 (FR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - A7-1 (FR-) (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-6 (FR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1415` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Belakang RH Malfungsi (Dokumen: RM000000XIA074X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Belakang RH Malfungsi (Dokumen: RM000000XIA07EX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Sirkuit speed sensor Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR BELAKANG DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR BELAKANG: Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepaskan konektor speed sensor belakang. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (KABEL SPEED SENSOR): Lepas hubungan kabel speed sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR BELAKANG): Hubungkan kembali kabel speed sensor. -> Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 1 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-1 (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-2 (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-2 - ZJ1-1 (Selalu)` : **Di bawah 1 Ω**

### DTC `C1416` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Belakang LH Malfungsi (Dokumen: RM000000XIA074X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Output Speed Sensor Belakang LH Malfungsi (Dokumen: RM000000XIA07EX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Sirkuit speed sensor Rotor speed sensor Pemasangan sensor Aktuator rem assembly (ECU Skid control); [KONTROL REM] Area Gangguan: Speed sensor RH/LH belakang Pemasangan sensor Rotor speed sensor; Kondisi Deteksi: Pendeteksian hanya selama Test Mode.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (GANGGUAN SESAAT): Menggunakan intelligent tester, periksa kemungkinan adanya gangguan sesaat dalam wire harness dan konektor yang berhubungan dengan DTC (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 3 (KONTROL REM) — PERIKSA APAKAH KONEKTOR ECU SKID CONTROL DAN SPEED SENSOR BELAKANG DIHUBUNGKAN DENGAN SEMPURNA: Periksa apakah konektor ECU skid control dan speed sensor belakang telah dihubungkan dengan sempurna.
  - Langkah 4 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecapatan 40 km/jam (25 mph) atau lebih minimal selama 60 detik. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 5 (KONTROL REM) — PERIKSA PEMASANGAN SPEED SENSOR BELAKANG: Putar switch pengapian ke off. -> Periksa pemasangan speed sensor.
  - Langkah 6 (KONTROL REM) — PERIKSA SPEED SENSOR BELAKANG: Pastikan bahwa tidak ada kekenduran pada bagian penguncian dan bagian penghubung konektor. -> Lepaskan konektor speed sensor belakang. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (KABEL SPEED SENSOR): Lepas hubungan kabel speed sensor. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SPEED SENSOR BELAKANG): Hubungkan kembali kabel speed sensor. -> Lepas hubungan konektor ECU skid control. -> Periksalah kedua case konektor dan terminal dari deformasi dan korosi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: 1 (RR-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RR+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 1 (RL-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: 2 (RL+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-1 (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - ZJ1-2 (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: Z1-1 - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[KONTROL REM] Tahanan Standar: Z1-2 - ZJ1-1 (Selalu)` : **Di bawah 1 Ω**

### DTC `C1417` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Voltase Tinggi Power Supply (Dokumen: RM000000XW6061X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Voltase Tinggi Power Supply (Dokumen: RM000000XW606AX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Baterai Sistem pengisian Sirkuit power source Sirkuit internal power source dari ECU skid control.; Kondisi Deteksi: Voltase terminal IG lebih dari 17.4 V selama 0.8 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA BATERAI: Periksa voltase baterai.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL IG1): Lepas hubungan konektor ECU skid control. -> Periksa case konektor dan terminal dari deformasi dan korosi. -> Putar switch pengapian ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — KONFIRMASI ULANG DTC: Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila DTC yang sama direkam (Lihat halam
  - Langkah 4 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 5 (KONTROL REM) — PERIKSA ATAU GANTI BATERAI ATAU SISTEM PENGISIAN
  - Langkah 6 (KONTROL REM) — PERIKSA SIRKUIT POWER SOURCE (SIRKUIT IG1)
  - Langkah 7 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Voltase Standar: A38-34 (IG1) - Masa bodi (Switch pengapian ON)` : **11 sampai 14 V**
  - `[KONTROL REM] Voltase Standar: A27-34 (IG1) - Masa bodi (Switch pengapian ON)` : **11 sampai 14 V**

### DTC `C1425` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open pada Sirkuit Switch Lampu Rem (Dokumen: RM000000XIE07GX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Open pada Sirkuit Switch Lampu Rem (Dokumen: RM000000XIE07OX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Switch lampu rem Sirkuit switch lampu rem Aktuator rem assembly (ECU Skid control); Kondisi Deteksi: Bila voltase terminal IG1 9.5 V atau lebih, sirkuit switch lampu rem open secara terus-menerus selama 3 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — PERIKSA KERJA LAMPU REM: Periksa bahwa lampu rem menyala ketika pedal rem diinjak dan segera padam ketika pedal rem dibebaskan.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL STP): Lepas hubungan konektor ECU skid control. -> Periksa case konektor dan terminal dari deformasi dan korosi. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL IG1): Putar switch pengapian ke ON. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 4 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL GND): Putar switch pengapian ke off. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 5 (KONTROL REM) — KONFIRMASI ULANG DTC: Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Tekan pedal rem beberapa kali untuk mengetes sirkuit lampu rem. -> Periksa bila DTC yang sama direkam (Lihat halaman ).
  - Langkah 6 (KONTROL REM) — PERIKSA STOP LIGHT SWITCH (TERMINAL POWER SOUCE): Lepas hubungan konektor switch lampu rem. -> Periksa case konektor dan terminal dari deformasi dan korosi. -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 7 (KONTROL REM) — PERIKSA SWITCH LAMPU REM: Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 8 (KONTROL REM) — PERIKSA HARNESS DAN KONEKTOR (ECU SKID CONTROL - SWITCH LAMPU REM): Lepas hubungan konektor ECU skid control. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] OK: Pedal rem ditekan` : **ON**
  - `[KONTROL REM] OK: Pedal rem dibebaskan` : **OFF**
  - `[KONTROL REM] Voltase Standar: A38-28 (STP) - Masa bodi (Switch lampu rem ON (Pedal rem ditekan))` : **8 sampai 14 V**
  - `[KONTROL REM] Voltase Standar: A38-28 (STP) - Masa bodi (Switch lampu rem OFF (Pedal rem dibebaskan))` : **Di bawah 1.5 V**
  - `[KONTROL REM] Voltase Standar: A38-34 (IG1) - Masa bodi (Switch pengapian ON)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: A38-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Voltase Standar: A13-2 - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[KONTROL REM] Tahanan Standar: 1 - 2 (Pin switch bebas)` : **Di bawah 1 Ω**

### DTC `C1427` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Motor (Dokumen: RM000000XIF058X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Motor (Dokumen: RM000000XIF05GX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Aktuator rem assembly (Sirkuit masa) Aktuator rem assembly (Open dalam sirkuit motor); Kondisi Deteksi: Aktuator pump motor tidak bekerja secara sempurna.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (RELAY MOTOR ABS): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Pilih mode Active Test pada intelligent tester (Lihat halaman ). -> Periksa suara kerja dari relay motor ABS ketika mengoperasikan relay motor ABS dengan intelligent tester.
  - Langkah 2 (KONTROL REM) — PERIKSA ECU SKID CONTROL (TERMINAL GND): Putar switch pengapian ke off. -> Lepas hubungan konektor ECU skid control. -> Periksa case konektor dan terminal dari deformasi dan korosi. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 3 (KONTROL REM) — KONFIRMASI ULANG DTC: Putar switch pengapian ke off. -> Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila 
  - Langkah 4 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 5 (KONTROL REM) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (SIRKUIT GND)
  - Langkah 6 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[KONTROL REM] Tahanan Standar: A38-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A38-13 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A27-1 (GND1) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[KONTROL REM] Tahanan Standar: A27-13 (GND2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `C1428` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Sirkuit Motor (Dokumen: RM000000XIF059X) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Malfungsi Sirkuit Motor (Dokumen: RM000000XIF05HX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Aktuator rem assembly (Short dalam sirkuit motor); Kondisi Deteksi: Selama motor ABS tidak bekerja, open dalam sirkuit motor secara terus menerus selama 2 detik atau lebih.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Putar switch pengapian ke off. -> Hubungkan kembali konektor ECU skid control. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Jalankan kendaraan pada kecepatan 20 km/jam (12 mph) atau lebih selama 30 detik atau lebih. -> Periksa bila 
  - Langkah 2 (KONTROL REM) — PERIKSA DARI PROBLEM INTERMITTENT (SIMULASI GEJALA)
  - Langkah 3 (KONTROL REM) — GANTI AKTUATOR REM ASSEMBLY

### DTC `C1511` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 11] Malfungsi Sensor Torsi 1 (Dokumen: RM000001AKH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 11] Malfungsi Sensor Torsi 1 (Dokumen: RM000001AKH007X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 11] Malfungsi Sensor Torsi 1 (Dokum
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor torsi (dibuat menyatu dalam steering column assembly) ECU power steering; Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ1); Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ2); Kondisi Deteksi: Deviasi antara sensor torsi TRQ1 dan TRQ2 melebihi nilai spesifikasi; Kondisi Deteksi: Error voltase power source sensor torsi; Kondisi Deteksi: Kontrol sementara yang disebabkan oleh 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN DATA LIST (TORQUE SENSOR OUTPUT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item [Torque Sensor 1 Output] and [Torque Sensor 2 Output] dalam DATA LIST. -> Ukur voltase. -> Periksa perbedaan nilai antara [Output 
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (OUTPUT): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 3 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (SENSOR TORSI): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 4 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 5 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 6 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (OUTPUT SENSOR TORSI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / EMPS / Data List. -> Pilih item Torque Sensor 1 Output dalam Torque Sensor 2 Output dalam Da
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (VOLTASE TRQV): Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase standar: TRQV (c1-6) - TRQG (c1-8) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: V1-6 (TRQV) - V1-8 (TRQG) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**

### DTC `C1512` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 12] Malfungsi Sirkuit Sensor Torsi (Dokumen: RM000001AKH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 12] Malfungsi Sirkuit Sensor Torsi (Dokumen: RM000001AKH007X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 12] Malfungsi Sirkuit S
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor torsi (dibuat menyatu dalam steering column assembly) ECU power steering; Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ1); Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ2); Kondisi Deteksi: Deviasi antara sensor torsi TRQ1 dan TRQ2 melebihi nilai spesifikasi; Kondisi Deteksi: Error voltase power source sensor torsi; Kondisi Deteksi: Kontrol sementara yang disebabkan oleh 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN DATA LIST (TORQUE SENSOR OUTPUT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item [Torque Sensor 1 Output] and [Torque Sensor 2 Output] dalam DATA LIST. -> Ukur voltase. -> Periksa perbedaan nilai antara [Output 
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (OUTPUT): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 3 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (SENSOR TORSI): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 4 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 5 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 6 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (OUTPUT SENSOR TORSI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / EMPS / Data List. -> Pilih item Torque Sensor 1 Output dalam Torque Sensor 2 Output dalam Da
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (VOLTASE TRQV): Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase standar: TRQV (c1-6) - TRQG (c1-8) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: V1-6 (TRQV) - V1-8 (TRQG) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**

### DTC `C1513` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 13] Malfungsi Sirkuit Sensor Torsi (Dokumen: RM000001AKH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 13] Malfungsi Sirkuit Sensor Torsi (Dokumen: RM000001AKH007X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 13] Malfungsi Sirkuit S
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor torsi (dibuat menyatu dalam steering column assembly) ECU power steering; Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ1); Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ2); Kondisi Deteksi: Deviasi antara sensor torsi TRQ1 dan TRQ2 melebihi nilai spesifikasi; Kondisi Deteksi: Error voltase power source sensor torsi; Kondisi Deteksi: Kontrol sementara yang disebabkan oleh 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN DATA LIST (TORQUE SENSOR OUTPUT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item [Torque Sensor 1 Output] and [Torque Sensor 2 Output] dalam DATA LIST. -> Ukur voltase. -> Periksa perbedaan nilai antara [Output 
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (OUTPUT): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 3 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (SENSOR TORSI): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 4 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 5 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 6 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (OUTPUT SENSOR TORSI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / EMPS / Data List. -> Pilih item Torque Sensor 1 Output dalam Torque Sensor 2 Output dalam Da
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (VOLTASE TRQV): Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase standar: TRQV (c1-6) - TRQG (c1-8) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: V1-6 (TRQV) - V1-8 (TRQG) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**

### DTC `C1514` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 14] Malfungsi Sirkuit Power Source Sensor Torsi (Dokumen: RM000001AKH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 14] Malfungsi Sirkuit Power Source Sensor Torsi (Dokumen: RM000001AKH007X) | [POWER STEERING — SISTEM POWER STEERING / Flash Co
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor torsi (dibuat menyatu dalam steering column assembly) ECU power steering; Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ1); Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ2); Kondisi Deteksi: Deviasi antara sensor torsi TRQ1 dan TRQ2 melebihi nilai spesifikasi; Kondisi Deteksi: Error voltase power source sensor torsi; Kondisi Deteksi: Kontrol sementara yang disebabkan oleh 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN DATA LIST (TORQUE SENSOR OUTPUT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item [Torque Sensor 1 Output] and [Torque Sensor 2 Output] dalam DATA LIST. -> Ukur voltase. -> Periksa perbedaan nilai antara [Output 
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (OUTPUT): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 3 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (SENSOR TORSI): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 4 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 5 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 6 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (OUTPUT SENSOR TORSI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / EMPS / Data List. -> Pilih item Torque Sensor 1 Output dalam Torque Sensor 2 Output dalam Da
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (VOLTASE TRQV): Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase standar: TRQV (c1-6) - TRQG (c1-8) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: V1-6 (TRQV) - V1-8 (TRQG) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**

### DTC `C1515` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 15] Penyetelan Titik Nol Sensor Torsi tidak di-inisialiasi (Dokumen: RM000001WCS001X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 15] Penyetelan Titik Nol Sensor Torsi tidak di-inisialiasi (Dokumen: RM000001WCS003X) | [POWER STEERING — SISTEM POW
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Kalibrasi titik nol sensor torsi Steering column assembly; Kondisi Deteksi: Kalibrasi titik nol sensor torsi tidak dilakukan.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — LAKUKAN KALIBRASI TITIK NOL (SENSOR TORSI): Lakukan kalibrasi titik nol sensor torsi (Lihat halaman ).
  - Langkah 2 (POWER STEERING) — KONFIRMASI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 3 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 4 (POWER STEERING) — SELESAI
  - Langkah 2 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.
  - Langkah 3 (POWER STEERING) — LAKUKAN KALIBRASI TITIK NOL (SENSOR TORSI): Lakukan kalibrasi titik nol sensor torsi lagi (Lihat halaman ).
  - Langkah 4 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.
  - Langkah 5 (POWER STEERING) — LAKUKAN KALIBRASI TITIK NOL (SENSOR TORSI): Lakukan kalibrasi titik nol sensor torsi lagi (Lihat halaman ).

### DTC `C1516` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 16] Penyetelan Titik Nol Sensor Torsi Tidak Tidak Berhasil (Dokumen: RM000001WCT001X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 16] Penyetelan Titik Nol Sensor Torsi Tidak Tidak Berhasil (Dokumen: RM000001WCT003X) | [POWER STEERING — SISTEM POW
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Kegagalan kalibrasi titik nol sensor torsi Steering column assembly; Kondisi Deteksi: Kalibrasi titik nol sensor torsi tidak diselesaikan dengan baik.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — HAPUS DTC
  - Langkah 2 (POWER STEERING) — LAKUKAN INISIALISASI (TITIK NOL SENSOR TORSI): Lakukan inisialisasi (Lihat halaman ).
  - Langkah 3 (POWER STEERING) — LAKUKAN KALIBRASI TITIK NOL (SENSOR TORSI): Lakukan kalibrasi titik nol sensor torsi (Lihat halaman ).
  - Langkah 4 (POWER STEERING) — KONFIRMASI DTC: Periksa DTC (Lihat halaman ).
  - Langkah 5 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 6 (POWER STEERING) — SELESAI
  - Langkah 1 (POWER STEERING) — HAPUS DTC: Hapus DTC (Lihat halaman ).
  - Langkah 4 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.

### DTC `C1517` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 17] Malfungsi Penahan (Hold) Sensor Torsi (Dokumen: RM000001AKH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 17] Malfungsi Penahan (Hold) Sensor Torsi (Dokumen: RM000001AKH007X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 17] Malfu
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor torsi (dibuat menyatu dalam steering column assembly) ECU power steering; Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ1); Kondisi Deteksi: Error atau terhentinya sinyal sensor torsi (TRQ2); Kondisi Deteksi: Deviasi antara sensor torsi TRQ1 dan TRQ2 melebihi nilai spesifikasi; Kondisi Deteksi: Error voltase power source sensor torsi; Kondisi Deteksi: Kontrol sementara yang disebabkan oleh 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN DATA LIST (TORQUE SENSOR OUTPUT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item [Torque Sensor 1 Output] and [Torque Sensor 2 Output] dalam DATA LIST. -> Ukur voltase. -> Periksa perbedaan nilai antara [Output 
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (OUTPUT): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 3 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (SENSOR TORSI): Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 4 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 5 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 6 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 1 (POWER STEERING) — BACA NILAINYA MENGGUNAKAN INTEELLIGENT TESTER (OUTPUT SENSOR TORSI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / EMPS / Data List. -> Pilih item Torque Sensor 1 Output dalam Torque Sensor 2 Output dalam Da
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING (VOLTASE TRQV): Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase standar: TRQV (c1-6) - TRQG (c1-8) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Posisi center)` : **2.3 sampai 2.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kanan)` : **2.5 sampai 4.7 V**
  - `[POWER STEERING] Voltase standar: TRQ1 (c1-5) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: TRQ2 (c1-7) - TRQG (c1-8) (Diputar ke kiri)` : **0.3 sampai 2.5 V**
  - `[POWER STEERING] Voltase standar: V1-6 (TRQV) - V1-8 (TRQG) (Switch pengapian on (IG))` : **7.5 sampai 8.5 V**

### DTC `C1524` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 24] Malfungsi Sirkuit Motor (Dokumen: RM000001AKN003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 24] Malfungsi Sirkuit Motor (Dokumen: RM000001AKN007X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 24] Malfungsi Sirkuit Motor (Dokumen:
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Steering column assembly ECU power steering; Kondisi Deteksi: Short (atau open) dalam sirkuit motor atau voltase abnormal atau arus dalam sirkuit motor.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAI MENGGUNAKAN DATA LIST (MOTOR ACTUAL CURRENT): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item [Motor Actual Current] dan [Command Value Current] dalam DATA LIST dan baca nilai tampilannya pada intelligent tester.
  - Langkah 2 (POWER STEERING) — PERIKSA ECU POWER STEERING: Putar switch pengapian ke on (IG). -> Ukur voltase.
  - Langkah 3 (POWER STEERING) — PERIKSA HARNESS DAN KONEKTOR (ECU POWER STEERING - MASA BODI): Lepas hubungan konektor dari ECU power steering. -> Ukur tahanan dan voltase.
  - Langkah 4 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (MOTOR POWER STEERING): Lepas hubungan konektor dari ECU power steering. -> Ukur tahanan.
  - Langkah 5 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 6 (POWER STEERING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (POWER STEERING) — GANTI STEERING COLUMN ASSEMBLY
  - Langkah 8 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Arus standar: Motor Actual Current (10 A sampai 55 A)` : **-55 A sampai -10 A**
  - `[POWER STEERING] Arus standar: Command Value Current (55 A)` : **-55 A**
  - `[POWER STEERING] Voltase standar: M1 (b1-1) - PGND (A19-2) (Diputar ke kanan)` : **11 sampai 14 V (RHD) Di bawah 1 V (LHD)**
  - `[POWER STEERING] Voltase standar: M1 (b1-1) - PGND (A19-2) (Diputar ke kiri)` : **Di bawah 1 V (RHD) 11 sampai 14 V (LHD)**
  - `[POWER STEERING] Voltase standar: M2 (b1-2) - PGND (A19-2) (Diputar ke kanan)` : **Di bawah 1 V (RHD) 11 sampai 14 V (LHD)**
  - `[POWER STEERING] Voltase standar: M2 (b1-2) - PGND (A19-2) (Diputar ke kiri)` : **11 sampai 14 V (RHD) Di bawah 1 V (LHD)**
  - `[POWER STEERING] Standar: PGND (A19-2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Standar: PIG (A19-1) - Masa bodi (Switch pengapian on (IG))` : **11 sampai 14 V**

### DTC `C1531` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 31] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 31] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: ECU power steering; Kondisi Deteksi: Malfungsi internal ECU (Malfungsi CPU); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sirkuit sekitarnya); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sensor temperature substrate); Kondisi Deteksi: Malfungsi internal ECU (error EEPROM); Kondisi Deteksi: Lokasi error data steering wheel (LHD atau RHD)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.
  - Langkah 2 (POWER STEERING) — PERBAIKI SIRKUIT YANG DITUNJUKKAN OLEH OUTPUT DTC
  - Langkah 3 (POWER STEERING) — GANTI ECU POWER STEERING

### DTC `C1532` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 32] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 32] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: ECU power steering; Kondisi Deteksi: Malfungsi internal ECU (Malfungsi CPU); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sirkuit sekitarnya); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sensor temperature substrate); Kondisi Deteksi: Malfungsi internal ECU (error EEPROM); Kondisi Deteksi: Lokasi error data steering wheel (LHD atau RHD)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.
  - Langkah 2 (POWER STEERING) — PERBAIKI SIRKUIT YANG DITUNJUKKAN OLEH OUTPUT DTC
  - Langkah 3 (POWER STEERING) — GANTI ECU POWER STEERING

### DTC `C1533` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 33] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 33] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: ECU power steering; Kondisi Deteksi: Malfungsi internal ECU (Malfungsi CPU); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sirkuit sekitarnya); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sensor temperature substrate); Kondisi Deteksi: Malfungsi internal ECU (error EEPROM); Kondisi Deteksi: Lokasi error data steering wheel (LHD atau RHD)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.
  - Langkah 2 (POWER STEERING) — PERBAIKI SIRKUIT YANG DITUNJUKKAN OLEH OUTPUT DTC
  - Langkah 3 (POWER STEERING) — GANTI ECU POWER STEERING

### DTC `C1534` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 34] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 34] Malfungsi Sirkuit ECU EPS (Dokumen: RM000001CHX009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: ECU power steering; Kondisi Deteksi: Malfungsi internal ECU (Malfungsi CPU); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sirkuit sekitarnya); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sensor temperature substrate); Kondisi Deteksi: Malfungsi internal ECU (error EEPROM); Kondisi Deteksi: Lokasi error data steering wheel (LHD atau RHD)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.
  - Langkah 2 (POWER STEERING) — PERBAIKI SIRKUIT YANG DITUNJUKKAN OLEH OUTPUT DTC
  - Langkah 3 (POWER STEERING) — GANTI ECU POWER STEERING

### DTC `C1535` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 35] Lokasi Error Data Steering Wheel (Dokumen: RM000001CHX003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 35] Lokasi Error Data Steering Wheel (Dokumen: RM000001CHX009X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: ECU power steering; Kondisi Deteksi: Malfungsi internal ECU (Malfungsi CPU); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sirkuit sekitarnya); Kondisi Deteksi: Malfungsi internal ECU (Malfungsi sensor temperature substrate); Kondisi Deteksi: Malfungsi internal ECU (error EEPROM); Kondisi Deteksi: Lokasi error data steering wheel (LHD atau RHD)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Periksa dari DTC.
  - Langkah 2 (POWER STEERING) — PERBAIKI SIRKUIT YANG DITUNJUKKAN OLEH OUTPUT DTC
  - Langkah 3 (POWER STEERING) — GANTI ECU POWER STEERING

### DTC `C1541` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 41] Speed Sensor Malfunction (Dokumen: RM0000034UL006X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 41] Speed Sensor Malfunction (Dokumen: RM0000034UL00AX) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 41] Speed Sensor Malfunction (Dokum
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor speedometer Sirkuit speed sensor Meter kombinasi ECU power steering; Kondisi Deteksi: Sinyal kecepatan kendaraan error; Kondisi Deteksi: Speed sensor malfungsi (Test Mode DTC)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — PERIKSA CARA KERJA SPEEDOMETER: Jalankan kendaraan dan periksa apakah speedometer dalam meter kombinasi bekerja secara bormal.
  - Langkah 2 (POWER STEERING) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (METER VEHICLE VELOCITY): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke on. -> Masuk ke menu berikut ini: Chassis / EMPS/ Data List / Meter Vehicle Velocity. -> Jalankan kendaraan. -> Baca nilai yang ditampilkan pada 
  - Langkah 3 (POWER STEERING) — LAKUKAN TEST MODE: Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (POWER STEERING) — PERIKSA METER KOMBINASI (+S VOLTASE): Lepas hubungan konektor meter kombinasi. -> Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor meter kombinasi.
  - Langkah 5 (POWER STEERING) — PERIKSA METER KOMBINASI (BENTUK GELOMBANG SINYAL SPD): Lepas meter kombinasi assembly dengan konektornya selama dihubungkan. -> Hubungkan oscilloscope ke konektor meter kombinasi. -> Hidupkan mesin. -> Jalankan kendaraan secara perlahan. -> Periksa bentuk gelombang sesuai dengan kondisi pada ta
  - Langkah 6 (POWER STEERING) — PERIKSA HARNESS DAN KONEKTOR (METER KOMBINASI - ECU POWER STEERING): Lepas hubungan konektor dari meter kombinasi dan ECU power steering. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor meter kombinasi dan ECU power steering.
  - Langkah 7 (POWER STEERING) — LANJUT KE MALFUNGSI SPEEDOMETER
  - Langkah 8 (POWER STEERING) — PERIKSA TERHADAP PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase Standar: D1-16 (+S) - Masa bodi (Switch pengapian on (IG))` : **4.5 sampai 5.5 V***
  - `[POWER STEERING] Tahanan Standar: D31-5 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan Standar: D31-5 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[POWER STEERING] Tahanan Standar: D29-5 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan Standar: D29-5 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1542` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 42] Speed Sensor Malfunction (Dokumen: RM0000034UL006X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 42] Speed Sensor Malfunction (Dokumen: RM0000034UL00AX) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 42] Speed Sensor Malfunction (Dokum
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor speedometer Sirkuit speed sensor Meter kombinasi ECU power steering; Kondisi Deteksi: Sinyal kecepatan kendaraan error; Kondisi Deteksi: Speed sensor malfungsi (Test Mode DTC)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — PERIKSA CARA KERJA SPEEDOMETER: Jalankan kendaraan dan periksa apakah speedometer dalam meter kombinasi bekerja secara bormal.
  - Langkah 2 (POWER STEERING) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (METER VEHICLE VELOCITY): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke on. -> Masuk ke menu berikut ini: Chassis / EMPS/ Data List / Meter Vehicle Velocity. -> Jalankan kendaraan. -> Baca nilai yang ditampilkan pada 
  - Langkah 3 (POWER STEERING) — LAKUKAN TEST MODE: Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (POWER STEERING) — PERIKSA METER KOMBINASI (+S VOLTASE): Lepas hubungan konektor meter kombinasi. -> Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor meter kombinasi.
  - Langkah 5 (POWER STEERING) — PERIKSA METER KOMBINASI (BENTUK GELOMBANG SINYAL SPD): Lepas meter kombinasi assembly dengan konektornya selama dihubungkan. -> Hubungkan oscilloscope ke konektor meter kombinasi. -> Hidupkan mesin. -> Jalankan kendaraan secara perlahan. -> Periksa bentuk gelombang sesuai dengan kondisi pada ta
  - Langkah 6 (POWER STEERING) — PERIKSA HARNESS DAN KONEKTOR (METER KOMBINASI - ECU POWER STEERING): Lepas hubungan konektor dari meter kombinasi dan ECU power steering. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor meter kombinasi dan ECU power steering.
  - Langkah 7 (POWER STEERING) — LANJUT KE MALFUNGSI SPEEDOMETER
  - Langkah 8 (POWER STEERING) — PERIKSA TERHADAP PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase Standar: D1-16 (+S) - Masa bodi (Switch pengapian on (IG))` : **4.5 sampai 5.5 V***
  - `[POWER STEERING] Tahanan Standar: D31-5 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan Standar: D31-5 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[POWER STEERING] Tahanan Standar: D29-5 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan Standar: D29-5 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1551` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 51] Voltase Power Supply IG Malfungsi (Dokumen: RM000001CJG003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 51] Voltase Power Supply IG Malfungsi (Dokumen: RM000001CJG008X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Fuse ECU-IG Sirkuit power source IG ECU power steering; Kondisi Deteksi: Open atau short pada sirkuit power source IG ketika switch pengapian on (IG).
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAI MENGGUNAKAN DATA LIST (IG POWER SUPPLY): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item [IG Power Supply] pada DATA LIST dan baca nilai yang ditampilkan pada intelligent tester.
  - Langkah 2 (POWER STEERING) — PEMERIKSAAN FUSE (ECU-IG): Cabut fuse ECU-IG dari main body ECU. -> Cek tahanan dari fuse.
  - Langkah 3 (POWER STEERING) — PERIKSA HARNESS DAN KONEKTOR (ECU POWER STEERING - MASA BODI): Lepaskan konektor dari ECU power steering. -> Ukur voltase dan tahanan.
  - Langkah 4 (POWER STEERING) — PERIKSA DARI HUBUNG PENDEK DALAM KOMPONEN DAN KABEL YANG DIHUBUNGKAN KE FUSE
  - Langkah 5 (POWER STEERING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 7 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 1 (POWER STEERING) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POWER SUPPLY IG): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan intelligent tester. -> Masuk ke menu berikut ini: Chassis / EMPS / Data List. -> Pilih item Power Supply IG pada DATA LIST dan baca nilai tampilan pada 
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Standar: IG (D31-6) - Masa bodi (Switch pengapian on (IG))` : **11 sampai 14 V**
  - `[POWER STEERING] Standar: PGND (A19-2) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: Fuse ECU-IG (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Voltase standar: D29-6 (IG) - Masa bodi (Switch pengapian on (IG))` : **11 sampai 14 V**
  - `[POWER STEERING] Tahanan standar: A18-2 (PGND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**

### DTC `C1552` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 52] Sirkuit Power Source PIG (Dokumen: RM000001CJH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 52] Sirkuit Power Source PIG (Dokumen: RM000001CJH009X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 52] Sirkuit Power Source PIG (Dokum
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Fuse EPS Sirkuit power source PIG ECU power steering; Kondisi Deteksi: Malfungsi sirkuit catu daya PIG; [POWER STEERING] Area Gangguan: Sirkuit power source PIG dan IG ECU power steering; Kondisi Deteksi: Overvoltase Abnormal; Kondisi Deteksi: Malfungsi sirkuit relay power source; [POWER STEERING] Area Gangguan: Steering column assembly (Motor power steering) ECU power steering
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAI MENGGUNAKAN DATA LIST (PIG POWER SUPPLY): Hubungkan intelligent tester ke DLC3. -> Pilih item [PIG Power Supply] pada DATA LIST dan baca nilai yang ditampilkan pada intelligent tester.
  - Langkah 2 (POWER STEERING) — PERIKSA FUSE (FUSE EPS): Lepas relay EPS dari ruang mesin R/B. -> Ukur tahanan fuse.
  - Langkah 3 (POWER STEERING) — PERIKSA HARNESS DAN KONNEKTOR (BATERAI - ECU POWER STEERING - MASA BODI): Lepas hubungan konektor dari ECU power steering. -> Ukur voltase dan tahanan.
  - Langkah 4 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (MOTOR POWER STEERING): Lepas hubungan konektor dari ECU power steering. -> Ukur tahanan.
  - Langkah 5 (POWER STEERING) — PERIKSA DARI HUBUNG PENDEK DALAM KOMPONEN DAN KABEL YANG DIHUBUNGKAN KE FUSE
  - Langkah 6 (POWER STEERING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 8 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Standar: PIG (A19-1) - Masa bodi` : **11 sampai 14 V**
  - `[POWER STEERING] Standar: PGND (A19-2) - Masa bodi` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: Fuse EPS (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Voltase standar: A18-1 (PIG) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[POWER STEERING] Tahanan standar: A18-2 (PGND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - U1-2 (M2) (Selalu)` : **0.08 sampai 0.15 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[POWER STEERING] Tahanan standar: U1-2 (M2) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `C1553` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 53] Saat Resetting Voltase, Kendaraan Sedang Dijalankan (Dokumen: RM000001CJH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 53] Saat Resetting Voltase, Kendaraan Sedang Dijalankan (Dokumen: RM000001CJH009X) | [POWER STEERING — SISTEM POWER STE
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Fuse EPS Sirkuit power source PIG ECU power steering; Kondisi Deteksi: Malfungsi sirkuit catu daya PIG; [POWER STEERING] Area Gangguan: Sirkuit power source PIG dan IG ECU power steering; Kondisi Deteksi: Overvoltase Abnormal; Kondisi Deteksi: Malfungsi sirkuit relay power source; [POWER STEERING] Area Gangguan: Steering column assembly (Motor power steering) ECU power steering
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAI MENGGUNAKAN DATA LIST (PIG POWER SUPPLY): Hubungkan intelligent tester ke DLC3. -> Pilih item [PIG Power Supply] pada DATA LIST dan baca nilai yang ditampilkan pada intelligent tester.
  - Langkah 2 (POWER STEERING) — PERIKSA FUSE (FUSE EPS): Lepas relay EPS dari ruang mesin R/B. -> Ukur tahanan fuse.
  - Langkah 3 (POWER STEERING) — PERIKSA HARNESS DAN KONNEKTOR (BATERAI - ECU POWER STEERING - MASA BODI): Lepas hubungan konektor dari ECU power steering. -> Ukur voltase dan tahanan.
  - Langkah 4 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (MOTOR POWER STEERING): Lepas hubungan konektor dari ECU power steering. -> Ukur tahanan.
  - Langkah 5 (POWER STEERING) — PERIKSA DARI HUBUNG PENDEK DALAM KOMPONEN DAN KABEL YANG DIHUBUNGKAN KE FUSE
  - Langkah 6 (POWER STEERING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 8 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Standar: PIG (A19-1) - Masa bodi` : **11 sampai 14 V**
  - `[POWER STEERING] Standar: PGND (A19-2) - Masa bodi` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: Fuse EPS (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Voltase standar: A18-1 (PIG) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[POWER STEERING] Tahanan standar: A18-2 (PGND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - U1-2 (M2) (Selalu)` : **0.08 sampai 0.15 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[POWER STEERING] Tahanan standar: U1-2 (M2) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `C1554` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 54] Sirkuit Relay EPS (Dokumen: RM000001CJH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 54] Sirkuit Relay EPS (Dokumen: RM000001CJH009X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 54] Sirkuit Relay EPS (Dokumen: RM000001CJH01LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Fuse EPS Sirkuit power source PIG ECU power steering; Kondisi Deteksi: Malfungsi sirkuit catu daya PIG; [POWER STEERING] Area Gangguan: Sirkuit power source PIG dan IG ECU power steering; Kondisi Deteksi: Overvoltase Abnormal; Kondisi Deteksi: Malfungsi sirkuit relay power source; [POWER STEERING] Area Gangguan: Steering column assembly (Motor power steering) ECU power steering
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAI MENGGUNAKAN DATA LIST (PIG POWER SUPPLY): Hubungkan intelligent tester ke DLC3. -> Pilih item [PIG Power Supply] pada DATA LIST dan baca nilai yang ditampilkan pada intelligent tester.
  - Langkah 2 (POWER STEERING) — PERIKSA FUSE (FUSE EPS): Lepas relay EPS dari ruang mesin R/B. -> Ukur tahanan fuse.
  - Langkah 3 (POWER STEERING) — PERIKSA HARNESS DAN KONNEKTOR (BATERAI - ECU POWER STEERING - MASA BODI): Lepas hubungan konektor dari ECU power steering. -> Ukur voltase dan tahanan.
  - Langkah 4 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (MOTOR POWER STEERING): Lepas hubungan konektor dari ECU power steering. -> Ukur tahanan.
  - Langkah 5 (POWER STEERING) — PERIKSA DARI HUBUNG PENDEK DALAM KOMPONEN DAN KABEL YANG DIHUBUNGKAN KE FUSE
  - Langkah 6 (POWER STEERING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 8 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Standar: PIG (A19-1) - Masa bodi` : **11 sampai 14 V**
  - `[POWER STEERING] Standar: PGND (A19-2) - Masa bodi` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: Fuse EPS (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Voltase standar: A18-1 (PIG) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[POWER STEERING] Tahanan standar: A18-2 (PGND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - U1-2 (M2) (Selalu)` : **0.08 sampai 0.15 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[POWER STEERING] Tahanan standar: U1-2 (M2) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `C1555` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 55] Sirkuit Relay Motor EPS (Dokumen: RM000001CJH003X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 55] Sirkuit Relay Motor EPS (Dokumen: RM000001CJH009X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 55] Sirkuit Relay Motor EPS (Dokumen:
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Fuse EPS Sirkuit power source PIG ECU power steering; Kondisi Deteksi: Malfungsi sirkuit catu daya PIG; [POWER STEERING] Area Gangguan: Sirkuit power source PIG dan IG ECU power steering; Kondisi Deteksi: Overvoltase Abnormal; Kondisi Deteksi: Malfungsi sirkuit relay power source; [POWER STEERING] Area Gangguan: Steering column assembly (Motor power steering) ECU power steering
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — BACA NILAI MENGGUNAKAN DATA LIST (PIG POWER SUPPLY): Hubungkan intelligent tester ke DLC3. -> Pilih item [PIG Power Supply] pada DATA LIST dan baca nilai yang ditampilkan pada intelligent tester.
  - Langkah 2 (POWER STEERING) — PERIKSA FUSE (FUSE EPS): Lepas relay EPS dari ruang mesin R/B. -> Ukur tahanan fuse.
  - Langkah 3 (POWER STEERING) — PERIKSA HARNESS DAN KONNEKTOR (BATERAI - ECU POWER STEERING - MASA BODI): Lepas hubungan konektor dari ECU power steering. -> Ukur voltase dan tahanan.
  - Langkah 4 (POWER STEERING) — PERIKSA STEERING COLUMN ASSEMBLY (MOTOR POWER STEERING): Lepas hubungan konektor dari ECU power steering. -> Ukur tahanan.
  - Langkah 5 (POWER STEERING) — PERIKSA DARI HUBUNG PENDEK DALAM KOMPONEN DAN KABEL YANG DIHUBUNGKAN KE FUSE
  - Langkah 6 (POWER STEERING) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 8 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Standar: PIG (A19-1) - Masa bodi` : **11 sampai 14 V**
  - `[POWER STEERING] Standar: PGND (A19-2) - Masa bodi` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: Fuse EPS (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Voltase standar: A18-1 (PIG) - Masa bodi (Selalu)` : **11 sampai 14 V**
  - `[POWER STEERING] Tahanan standar: A18-2 (PGND) - Masa bodi (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - U1-2 (M2) (Selalu)` : **0.08 sampai 0.15 Ω**
  - `[POWER STEERING] Tahanan standar: U1-1 (M1) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**
  - `[POWER STEERING] Tahanan standar: U1-2 (M2) - Masa bodi (Selalu)` : **1 MΩ atau lebih tinggi**

### DTC `C1571` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 71] Speed Sensor Malfungsi (Test Mode DTC) (Dokumen: RM0000034UL006X) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 71] Speed Sensor Malfungsi (Test Mode DTC) (Dokumen: RM0000034UL00AX) | [POWER STEERING — SISTEM POWER STEERING / Flash Code 71] Spe
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sensor speedometer Sirkuit speed sensor Meter kombinasi ECU power steering; Kondisi Deteksi: Sinyal kecepatan kendaraan error; Kondisi Deteksi: Speed sensor malfungsi (Test Mode DTC)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — PERIKSA CARA KERJA SPEEDOMETER: Jalankan kendaraan dan periksa apakah speedometer dalam meter kombinasi bekerja secara bormal.
  - Langkah 2 (POWER STEERING) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (METER VEHICLE VELOCITY): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan putar tester ke on. -> Masuk ke menu berikut ini: Chassis / EMPS/ Data List / Meter Vehicle Velocity. -> Jalankan kendaraan. -> Baca nilai yang ditampilkan pada 
  - Langkah 3 (POWER STEERING) — LAKUKAN TEST MODE: Lakukan pemeriksaan sensor dalam prosedur Test Mode (Lihat halaman ).
  - Langkah 4 (POWER STEERING) — PERIKSA METER KOMBINASI (+S VOLTASE): Lepas hubungan konektor meter kombinasi. -> Putar switch pengapian ke on (IG). -> Ukur voltase sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor meter kombinasi.
  - Langkah 5 (POWER STEERING) — PERIKSA METER KOMBINASI (BENTUK GELOMBANG SINYAL SPD): Lepas meter kombinasi assembly dengan konektornya selama dihubungkan. -> Hubungkan oscilloscope ke konektor meter kombinasi. -> Hidupkan mesin. -> Jalankan kendaraan secara perlahan. -> Periksa bentuk gelombang sesuai dengan kondisi pada ta
  - Langkah 6 (POWER STEERING) — PERIKSA HARNESS DAN KONEKTOR (METER KOMBINASI - ECU POWER STEERING): Lepas hubungan konektor dari meter kombinasi dan ECU power steering. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini. -> Hubungkan kembali konektor meter kombinasi dan ECU power steering.
  - Langkah 7 (POWER STEERING) — LANJUT KE MALFUNGSI SPEEDOMETER
  - Langkah 8 (POWER STEERING) — PERIKSA TERHADAP PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[POWER STEERING] Voltase Standar: D1-16 (+S) - Masa bodi (Switch pengapian on (IG))` : **4.5 sampai 5.5 V***
  - `[POWER STEERING] Tahanan Standar: D31-5 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan Standar: D31-5 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[POWER STEERING] Tahanan Standar: D29-5 (SPD) - D1-16 (+S) (Selalu)` : **Di bawah 1 Ω**
  - `[POWER STEERING] Tahanan Standar: D29-5 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `C1581` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 81] Assist Map Un-Writing (Dokumen: RM000001AL000LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECM ECU power steering; Kondisi Deteksi: Assist map tidak ditulis pada ECU power steering
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — LAKUKAN ASSIST MAP WRITING: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Set intelligent tester ke Test Mode (pilih "Signal Check"). -> Tunggu selama 7 detik atau lebih. -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (POWER STEERING) — PERIKSA SISTEM KOMUNIKASI CAN: Periksa DTC sistem komunikasi CAN (Lihat halaman ).
  - Langkah 3 (POWER STEERING) — PERIKSA ECM: Periksa bahwa ECM yang mematuhi spesifikasi kendaraan telah dipasang.
  - Langkah 4 (POWER STEERING) — GANTI ECU POWER STEERING
  - Langkah 5 (POWER STEERING) — SELESAI
  - Langkah 6 (POWER STEERING) — PERBAIKI SIRKUIT YANG DITUNJUKKAN OLEH OUTPUT DTC
  - Langkah 7 (POWER STEERING) — GANTI ECM

### DTC `P0010` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Aktuator Posisi Camshaft "A" (Bank 1) (Dokumen: RM000000PDW010X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Aktuator Posisi Camshaft "A" (Bank 1) (Dokumen: RM000000PDW02ZX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit OCV OCV ECM; Kondisi Deteksi: Open atau short dalam sirkuit OCV (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit camshaft timing oil control valve Camshaft timing oil control valve ECM; Kondisi Deteksi: Open atau short dalam sirkuit camshaft timing oil control valve (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DARI DTC: Hapus DTC setelah mencatat freeze frame data dan DTC. -> Biarkan mesin idle dan periksa DTC. -> Periksa apakah P0010 tidak ditampilkan.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY: Lepas hubungan konektor C24 OCV. -> Ukur tahanan antara terminal-terminal OCV. -> Hubungkan kembali konektor OCV.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (OCV - ECM): Lepas hubungan konektor C24 OCV. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor OCV. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG ATAU TIDAK (DTC P0010): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan panaskan mesin. -> Biarkan mesin idle dalam waktu 1 menit atau lebih. -> Pilih item menu be
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): OC1+ (C24-1) - OC1+ (C20-100)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): OC1- (C24-2) - OC1- (C20-123)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): OC1+ (C24-1) atau OC1+ (C20-100) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): OC1- (C24-2) atau OC1- (C20-123) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (20°C (68°F))` : **6.9 sampai 7.9 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): C25-1 (OC1+) - C23-100 (OC1+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): C25-2 (OC1-) - C23-123 (OC1-) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): C25-1 (OC1+) or C23-100 (OC1+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0011` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Posisi Camshaft "A" - Timing Over-Advanced atau System Performance (Bank 1) (Dokumen: RM000000PDU010X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Posisi Camshaft "A" - Timing Over-Advanced atau System Performance (Bank 1) (Dokumen: RM000000PDU034X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Timing katup OCV Filter OCV Camshaft timing gear assembly ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Timing katup Camshaft timing oil control valve Filter camshaft timing oil control valve Camshaft timing gear assembly ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ADANYA OUTPUT DTC YANG LAIN (SEBAGAI TAMBAHAN UNTUK DTC P011 atau POO12): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (OPERATE OCV): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Panaskan mesin. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Active Test / Control the VVT System (Bank 1). -> Periksa putaran mesin sewaktu me
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P0011 ATAU P0012): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan panaskan mesin. -> Ubah ECM dari normal mode ke check mode menggunakan tester (Lihat halama
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TIMING KATUP (PERIKSA DARI KEKENDORAN DAN GIGI LONCAT PADA RANTAI TIMING): Lepas cover cylinder head. -> Putar puli crankshaft , dan luruskan alurnya dengan tanda timing "0" pada cover rantai timing. -> Periksa tanda timing pada timing sproket camshaft dan camshaft timing gear menghadap ke atas seperti ditunjukkan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY (OCV): Lepas OCV. -> Ukur tahanan antara terminal-terminal OCV. -> Hubungkan voltase baterai positif ke terminal 1 dan voltase baterai negatif ke terminal 2. Periksa kerja katup. -> Pasang kembali OCV.
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA FILTER OIL CONTROL VALVE: Lepas generator. -> Lepas filter OCV. -> Periksa bahwa filter tidak tersumbat. -> Pasang kembali filter OCV. -> Pasang kembali generator.
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI CAMSHAFT TIMING GEAR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] OK: OCV OFF` : **Putaran mesin normal**
  - `[SISTEM KONTROL MESIN 1NZ-FE] OK: OCV ON` : **Idle mesin kasar atau mati mendadak (segera setelah OCV diubah dari OFF ke ON)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (20°C (68°F))` : **6.9 sampai 7.9 Ω**

### DTC `P0012` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Posisi Camshaft "A" - Timing Over-Retarded (Bank 1) (Dokumen: RM000000PDU010X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Posisi Camshaft "A" - Timing Over-Retarded (Bank 1) (Dokumen: RM000000PDU034X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Timing katup OCV Filter OCV Camshaft timing gear assembly ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Timing katup Camshaft timing oil control valve Filter camshaft timing oil control valve Camshaft timing gear assembly ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ADANYA OUTPUT DTC YANG LAIN (SEBAGAI TAMBAHAN UNTUK DTC P011 atau POO12): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (OPERATE OCV): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Panaskan mesin. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Active Test / Control the VVT System (Bank 1). -> Periksa putaran mesin sewaktu me
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P0011 ATAU P0012): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin dan panaskan mesin. -> Ubah ECM dari normal mode ke check mode menggunakan tester (Lihat halama
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TIMING KATUP (PERIKSA DARI KEKENDORAN DAN GIGI LONCAT PADA RANTAI TIMING): Lepas cover cylinder head. -> Putar puli crankshaft , dan luruskan alurnya dengan tanda timing "0" pada cover rantai timing. -> Periksa tanda timing pada timing sproket camshaft dan camshaft timing gear menghadap ke atas seperti ditunjukkan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY (OCV): Lepas OCV. -> Ukur tahanan antara terminal-terminal OCV. -> Hubungkan voltase baterai positif ke terminal 1 dan voltase baterai negatif ke terminal 2. Periksa kerja katup. -> Pasang kembali OCV.
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA FILTER OIL CONTROL VALVE: Lepas generator. -> Lepas filter OCV. -> Periksa bahwa filter tidak tersumbat. -> Pasang kembali filter OCV. -> Pasang kembali generator.
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI CAMSHAFT TIMING GEAR ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] OK: OCV OFF` : **Putaran mesin normal**
  - `[SISTEM KONTROL MESIN 1NZ-FE] OK: OCV ON` : **Idle mesin kasar atau mati mendadak (segera setelah OCV diubah dari OFF ke ON)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (20°C (68°F))` : **6.9 sampai 7.9 Ω**

### DTC `P0016` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Posisi Crankshaft - Korelasi Posisi Camshaft (Bank 1 Sensor A) (Dokumen: RM000000PDV00XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Posisi Crankshaft - Korelasi Posisi Camshaft (Bank 1 Sensor A) (Dokumen: RM000000PDV031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem mekanikal (Rantai timing lompat gigi atau rantai memanjang) ECM; Kondisi Deteksi: Penyimpangan pada sinyal crankshaft position sensor dan sinyal sensor VVT (2 trip pendeteksian logis); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem mekanikal (Rantai timing lompat gigi atau rantai memanjang) Camshaft timing oil control valve Filter camshaft timing oil control valve Camshaft timing gear assem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TIMING KATUP (PERIKSA DARI KEKENDORAN DAN RANTAI TIMING LONCAT GIGI: Lepas cover cylinder head. -> Putar puli crankshaft , dan luruskan alurnya dengan tanda timing "0" pada cover rantai timing. -> Periksa tanda timing pada timing sproket camshaft dan camshaft timing gear menghadap ke atas seperti ditunjukkan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — SETEL VALVE TIMING
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG ATAU TIDAK (DTC P0016): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Ubah ECM dari normal mode ke check mode menggunakan tester (Lihat halaman ). -> Hidupkan mesin dan panaskan me
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTCS LAIN (SEBAGAI TAMBAHAN UNTUK DTC P0016): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (OPERATE OCV): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Hidupkan tester. -> Panaskan mesin. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Active Test / Control the VVT System (Bank 1). -> Pilih item monitor berikut ini: 
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TIMING KATUP: Lepas cover cylinder head. -> Putar puli crankshaft, dan luruskan alurnya dengan tanda timing "0" pada tutup rantai timing. -> Periksa bahwa tanda-tanda tersebut lurus pada camshaft sproket camshaft timing gear menghadap ke atas seperti dit
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (20°C (68°F))` : **6.9 sampai 7.9 Ω**

### DTC `P0031` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 1) (Dokumen: RM000000YDF00HX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 1) (Dokumen: RM000000YDF00VX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heater Heated Oxygen (HO2) di bawah0.25 A bila heater bekerja dengan +B lebih besar dari10.5 V (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heat
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER): Lepas hubungan konektor C36 atau D28 sensor heated oxygen. -> Ukur tahanan antara terminal konektor sensor heated oxygen . -> Hubungkan kembali konektor sensor H02.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TEGANGAN TERMINAL (+B DARI SENSOR HO2 ): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal C36 ataukonektor sensor D28 H02dan masa bodi. -> Hubungkan kembali konektor sensor H02.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA RELAY INTEGRATION (RELAY EFI ): Lepas relay integrasi dari relay block ruang mesin. -> Periksa fuse EFI . -> Periksa relay EFI. -> Pasang kembali relay integrasi.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR HO2 - RELAY EFI): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas relay integrasi dari relay block ruang mesin. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Pasang kembali relay integrasi.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR H2O- ECM): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0031,P0032,P0037 ATAU P0038): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle dalam waktu 1 menit atau lebih. -> Pilih item menu berikut ini: Powertra
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR HEATED OXYGEN
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI RELAY INTEGRASI NO. 1
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - +B (2)` : **5.3 sampai 7.5 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - +B (2)` : **11 sampai 16 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C36-2) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (D28-2) - Masa Bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **Di bawah 1 Ω (Masukkan voltase baterai antara terminal 1A-2 dan 1A-3)**

### DTC `P0032` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 1) (Dokumen: RM000000YDF00HX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 1) (Dokumen: RM000000YDF00VX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heater Heated Oxygen (HO2) di bawah0.25 A bila heater bekerja dengan +B lebih besar dari10.5 V (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heat
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER): Lepas hubungan konektor C36 atau D28 sensor heated oxygen. -> Ukur tahanan antara terminal konektor sensor heated oxygen . -> Hubungkan kembali konektor sensor H02.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TEGANGAN TERMINAL (+B DARI SENSOR HO2 ): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal C36 ataukonektor sensor D28 H02dan masa bodi. -> Hubungkan kembali konektor sensor H02.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA RELAY INTEGRATION (RELAY EFI ): Lepas relay integrasi dari relay block ruang mesin. -> Periksa fuse EFI . -> Periksa relay EFI. -> Pasang kembali relay integrasi.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR HO2 - RELAY EFI): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas relay integrasi dari relay block ruang mesin. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Pasang kembali relay integrasi.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR H2O- ECM): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0031,P0032,P0037 ATAU P0038): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle dalam waktu 1 menit atau lebih. -> Pilih item menu berikut ini: Powertra
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR HEATED OXYGEN
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI RELAY INTEGRASI NO. 1
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - +B (2)` : **5.3 sampai 7.5 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - +B (2)` : **11 sampai 16 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C36-2) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (D28-2) - Masa Bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **Di bawah 1 Ω (Masukkan voltase baterai antara terminal 1A-2 dan 1A-3)**

### DTC `P0037` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 2) (Dokumen: RM000000YDF00HX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 2) (Dokumen: RM000000YDF00VX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heater Heated Oxygen (HO2) di bawah0.25 A bila heater bekerja dengan +B lebih besar dari10.5 V (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heat
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER): Lepas hubungan konektor C36 atau D28 sensor heated oxygen. -> Ukur tahanan antara terminal konektor sensor heated oxygen . -> Hubungkan kembali konektor sensor H02.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TEGANGAN TERMINAL (+B DARI SENSOR HO2 ): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal C36 ataukonektor sensor D28 H02dan masa bodi. -> Hubungkan kembali konektor sensor H02.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA RELAY INTEGRATION (RELAY EFI ): Lepas relay integrasi dari relay block ruang mesin. -> Periksa fuse EFI . -> Periksa relay EFI. -> Pasang kembali relay integrasi.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR HO2 - RELAY EFI): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas relay integrasi dari relay block ruang mesin. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Pasang kembali relay integrasi.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR H2O- ECM): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0031,P0032,P0037 ATAU P0038): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle dalam waktu 1 menit atau lebih. -> Pilih item menu berikut ini: Powertra
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR HEATED OXYGEN
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI RELAY INTEGRASI NO. 1
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - +B (2)` : **5.3 sampai 7.5 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - +B (2)` : **11 sampai 16 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C36-2) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (D28-2) - Masa Bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **Di bawah 1 Ω (Masukkan voltase baterai antara terminal 1A-2 dan 1A-3)**

### DTC `P0038` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 2) (Dokumen: RM000000YDF00HX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Sirkuit Kontrol Heater Sensor Oksigen (Bank 1 Sensor 2) (Dokumen: RM000000YDF00VX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heater Heated Oxygen (HO2) di bawah0.25 A bila heater bekerja dengan +B lebih besar dari10.5 V (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit heater sensor H2O Heater sensor HO2 Relay Integrasi (relay EFI) ECM; Kondisi Deteksi: Arus sensor heat
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER): Lepas hubungan konektor C36 atau D28 sensor heated oxygen. -> Ukur tahanan antara terminal konektor sensor heated oxygen . -> Hubungkan kembali konektor sensor H02.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TEGANGAN TERMINAL (+B DARI SENSOR HO2 ): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal C36 ataukonektor sensor D28 H02dan masa bodi. -> Hubungkan kembali konektor sensor H02.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA RELAY INTEGRATION (RELAY EFI ): Lepas relay integrasi dari relay block ruang mesin. -> Periksa fuse EFI . -> Periksa relay EFI. -> Pasang kembali relay integrasi.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR HO2 - RELAY EFI): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas relay integrasi dari relay block ruang mesin. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Pasang kembali relay integrasi.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR H2O- ECM): Lepas hubungan konektor C36 atau D28 sensor HO2. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0031,P0032,P0037 ATAU P0038): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle dalam waktu 1 menit atau lebih. -> Pilih item menu berikut ini: Powertra
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR HEATED OXYGEN
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI RELAY INTEGRASI NO. 1
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - +B (2)` : **5.3 sampai 7.5 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 1): HT1A (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - +B (2)` : **11 sampai 16 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar tahanan (Sensor 2): HT1B (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C36-2) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (D28-2) - Masa Bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **Di bawah 1 Ω (Masukkan voltase baterai antara terminal 1A-2 dan 1A-3)**

### DTC `P0100` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Massa atau Volume Aliran Udara (Dokumen: RM000000U5B011X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Massa atau Volume Aliran Udara (Dokumen: RM000000U5B036X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit MAF meter MAF meter ECM; Kondisi Deteksi: Voltase MAF meter kurang dari 0.2 V, atau lebih dari 4.9 V selama 3 detik (1 trip detection logic); Kondisi Deteksi: Tehangan MAF meter kurang dari 0.2 V selama 3 detik (1 trip detection logic); Kondisi Deteksi: Voltase MAF meter lebih dari 4.9 V selama 3 detik (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (TINGKAT MASS AIR FLOW ): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / MAF. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MASS AIR FLOW METER (TEGANGAN POWER SOURCE ): Lepas hubungan konektor C26 Mass Air flow (MAF) meter. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor dan Masa bodi. -> Hubungkan kembali konektor MAF meter .
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MASS AIR FLOW METER (VOLTASE VG): Pemeriksaan voltase output.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor MAF meter C26. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor MAF meter . -> Hubungkan kembali konektor ECM.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI MASS AIR FLOW METER
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C26-1) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VG (3) - E2G (2)` : **0.2 sampai 4.9 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VG (C26-3) - VG (C20-118)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2G (C26-2) - E2G (C20-116)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VG (C26-3) atau VG (C20-118) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): +B (C26-1) - 1A-4` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): +B (C26-1) atau 1A-4 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2G (C26-2) - Masa Bodi` : **Di bawah 1 Ω**

### DTC `P0102` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit Massa atau Volume Aliran Udara (Dokumen: RM000000U5B011X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit Massa atau Volume Aliran Udara (Dokumen: RM000000U5B036X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit MAF meter MAF meter ECM; Kondisi Deteksi: Voltase MAF meter kurang dari 0.2 V, atau lebih dari 4.9 V selama 3 detik (1 trip detection logic); Kondisi Deteksi: Tehangan MAF meter kurang dari 0.2 V selama 3 detik (1 trip detection logic); Kondisi Deteksi: Voltase MAF meter lebih dari 4.9 V selama 3 detik (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (TINGKAT MASS AIR FLOW ): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / MAF. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MASS AIR FLOW METER (TEGANGAN POWER SOURCE ): Lepas hubungan konektor C26 Mass Air flow (MAF) meter. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor dan Masa bodi. -> Hubungkan kembali konektor MAF meter .
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MASS AIR FLOW METER (VOLTASE VG): Pemeriksaan voltase output.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor MAF meter C26. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor MAF meter . -> Hubungkan kembali konektor ECM.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI MASS AIR FLOW METER
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C26-1) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VG (3) - E2G (2)` : **0.2 sampai 4.9 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VG (C26-3) - VG (C20-118)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2G (C26-2) - E2G (C20-116)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VG (C26-3) atau VG (C20-118) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): +B (C26-1) - 1A-4` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): +B (C26-1) atau 1A-4 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2G (C26-2) - Masa Bodi` : **Di bawah 1 Ω**

### DTC `P0103` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Massa atau Volume Aliran Udara (Dokumen: RM000000U5B011X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Massa atau Volume Aliran Udara (Dokumen: RM000000U5B036X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit MAF meter MAF meter ECM; Kondisi Deteksi: Voltase MAF meter kurang dari 0.2 V, atau lebih dari 4.9 V selama 3 detik (1 trip detection logic); Kondisi Deteksi: Tehangan MAF meter kurang dari 0.2 V selama 3 detik (1 trip detection logic); Kondisi Deteksi: Voltase MAF meter lebih dari 4.9 V selama 3 detik (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (TINGKAT MASS AIR FLOW ): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / MAF. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MASS AIR FLOW METER (TEGANGAN POWER SOURCE ): Lepas hubungan konektor C26 Mass Air flow (MAF) meter. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor dan Masa bodi. -> Hubungkan kembali konektor MAF meter .
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MASS AIR FLOW METER (VOLTASE VG): Pemeriksaan voltase output.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor MAF meter C26. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor MAF meter . -> Hubungkan kembali konektor ECM.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI MASS AIR FLOW METER
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C26-1) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VG (3) - E2G (2)` : **0.2 sampai 4.9 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VG (C26-3) - VG (C20-118)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2G (C26-2) - E2G (C20-116)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VG (C26-3) atau VG (C20-118) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): +B (C26-1) - 1A-4` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): +B (C26-1) atau 1A-4 - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2G (C26-2) - Masa Bodi` : **Di bawah 1 Ω**

### DTC `P0110` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit Temperatur Udara Intake (Dokumen: RM000000PF3012X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit Temperatur Udara Intake (Dokumen: RM000000PF3037X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short di sirkuit sensor IAT selama 0.5 detik (1 trip detection logic); Kondisi Deteksi: Langkah 1; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short di sirkuit sensor IAT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 4; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open di sirkuit sensor IAT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 2
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR OPEN IN WIRE HARNESS): Lepas hubungan konektor C26 Mass Air flow (MAF) meter. -> Hubungkan terminal THA dan E2 dari wire harness mass air flow sensor dari sisi konektor. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan te
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor MAF meter C26. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor MAF meter . -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR BILA OK, GANTI MASS AIR FLOW METER
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM BILA OK, GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor MAF meter C26. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilai ya
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THA (C26-4) - THA (C20-65)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2 (C26-5) - ETHA (C20-88)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THA (C26-4) atau THA (C20-65) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-4 (THA) - C23-65 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-5 (E2) - C23-88 (ETHA) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-4 (THA) atau C23-65 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0112` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit Temperatur Udara Intake (Dokumen: RM000000PF3012X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit Temperatur Udara Intake (Dokumen: RM000000PF3037X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short di sirkuit sensor IAT selama 0.5 detik (1 trip detection logic); Kondisi Deteksi: Langkah 1; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short di sirkuit sensor IAT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 4; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open di sirkuit sensor IAT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 2
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR OPEN IN WIRE HARNESS): Lepas hubungan konektor C26 Mass Air flow (MAF) meter. -> Hubungkan terminal THA dan E2 dari wire harness mass air flow sensor dari sisi konektor. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan te
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor MAF meter C26. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor MAF meter . -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR BILA OK, GANTI MASS AIR FLOW METER
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM BILA OK, GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor MAF meter C26. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilai ya
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THA (C26-4) - THA (C20-65)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2 (C26-5) - ETHA (C20-88)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THA (C26-4) atau THA (C20-65) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-4 (THA) - C23-65 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-5 (E2) - C23-88 (ETHA) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-4 (THA) atau C23-65 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0113` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Temperatur Udara Intake (Dokumen: RM000000PF3012X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Temperatur Udara Intake (Dokumen: RM000000PF3037X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short di sirkuit sensor IAT selama 0.5 detik (1 trip detection logic); Kondisi Deteksi: Langkah 1; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short di sirkuit sensor IAT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 4; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open di sirkuit sensor IAT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 2
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (INTAKE AIR TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR OPEN IN WIRE HARNESS): Lepas hubungan konektor C26 Mass Air flow (MAF) meter. -> Hubungkan terminal THA dan E2 dari wire harness mass air flow sensor dari sisi konektor. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan te
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (MASS AIR FLOW METER - ECM): Lepas hubungan konektor MAF meter C26. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor MAF meter . -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR BILA OK, GANTI MASS AIR FLOW METER
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM BILA OK, GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor MAF meter C26. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Intake Air. -> Baca nilai ya
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THA (C26-4) - THA (C20-65)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2 (C26-5) - ETHA (C20-88)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THA (C26-4) atau THA (C20-65) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-4 (THA) - C23-65 (THA) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-5 (E2) - C23-88 (ETHA) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C27-4 (THA) atau C23-65 (THA) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0115` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PF5011X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PF5038X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short di sirkuit sensor ECT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 1; Kondisi Deteksi: Langkah 4; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open di sirkuit sensor ECT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 2; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor temperatur cairan pendingin mesin selama 0.5 de
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE COOLANT TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR OPEN IN WIRE HARNESS): Lepas hubungan konektor C19 sensor Engine Coolant Temperature (ECT). -> Hubungkan terminal 1 dan 2 dari konektor sensor pada sisi wire harness. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan teste
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN - ECM): Lepas hubungan konektor C19 sensor ECT. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor ECT. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR JIKA OK, GANTI SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM BILA OK, GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor C19 sensor ECT. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilai
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THW (C19-2) - THW (C20-97)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2 (C19-1) - ETHW (C20-96)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THW (C19-2) atau THW (C20-97) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-2 - C23-97 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-1 - C23-96 (ETHW) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-2 atau C23-97 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0116` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Problem Range / Performance Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PFB010X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Problem Range / Performance Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PFB03DX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Thermostat Sensor ECT; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Thermostat Sensor temperatur cairan pendingin mesin
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DTC LAIN di-OUTPUT (SEBAGAI TAMBAHAN KE DTC P0116): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA THERMOSTAT: Lepas thermostat (Lihat halaman ). -> Periksa temperatur pembukaan katup dari thermostat. -> Pasang kembali thermostat (Lihat halaman ).
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THERMOSTAT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DTC LAIN di-OUTPUT (SEBAGAI TAMBAHAN KE DTC P0116): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA THERMOSTAT: Lepas thermostat (Lihat halaman ). -> Ukur temperatur bukaan pada katup thermostat. -> Pasang kembali thermostat (Lihat halaman ).

### DTC `P0117` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PF5011X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PF5038X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short di sirkuit sensor ECT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 1; Kondisi Deteksi: Langkah 4; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open di sirkuit sensor ECT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 2; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor temperatur cairan pendingin mesin selama 0.5 de
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE COOLANT TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR OPEN IN WIRE HARNESS): Lepas hubungan konektor C19 sensor Engine Coolant Temperature (ECT). -> Hubungkan terminal 1 dan 2 dari konektor sensor pada sisi wire harness. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan teste
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN - ECM): Lepas hubungan konektor C19 sensor ECT. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor ECT. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR JIKA OK, GANTI SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM BILA OK, GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor C19 sensor ECT. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilai
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THW (C19-2) - THW (C20-97)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2 (C19-1) - ETHW (C20-96)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THW (C19-2) atau THW (C20-97) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-2 - C23-97 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-1 - C23-96 (ETHW) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-2 atau C23-97 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0118` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PF5011X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000000PF5038X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short di sirkuit sensor ECT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 1; Kondisi Deteksi: Langkah 4; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open di sirkuit sensor ECT selama 0.5 detik (1 trip pendeteksian logis); Kondisi Deteksi: Langkah 2; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor temperatur cairan pendingin mesin selama 0.5 de
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE COOLANT TEMPERATURE ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (CHECK FOR OPEN IN WIRE HARNESS): Lepas hubungan konektor C19 sensor Engine Coolant Temperature (ECT). -> Hubungkan terminal 1 dan 2 dari konektor sensor pada sisi wire harness. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan teste
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN - ECM): Lepas hubungan konektor C19 sensor ECT. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor ECT. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE SENSOR JIKA OK, GANTI SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PASTIKAN SAMBUNGAN YANG BAIK KE ECM BILA OK, GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI INTELLIGENT TESTER (CHECK FOR SHORT IN WIRE HARNESS): Lepas hubungan konektor C19 sensor ECT. -> Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Coolant Temp. -> Baca nilai
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THW (C19-2) - THW (C20-97)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: E2 (C19-1) - ETHW (C20-96)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: THW (C19-2) atau THW (C20-97) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-2 - C23-97 (THW) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-1 - C23-96 (ETHW) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: C19-2 atau C23-97 (THW) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0120` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P0121` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Problem Range / Performance Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Problem Range / Performance Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P0122` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "A" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P0123` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "A" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "A" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P0134` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Sensor Oxygen Tidak ada aktivitas terdeteksi (Bank 1 Sensor 1) (Dokumen: RM000001NZZ003X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Sensor Oxygen Tidak ada aktivitas terdeteksi (Bank 1 Sensor 1) (Dokumen: RM000001NZZ00BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor HO2 (sensor 1) Heater sensor HO2 (sensor 1) Sensor HO2 (sensor 1) Tekanan bahan bakar Sistem induksi udara Sambungan selang PCV Katup dan selang PCV Injektor Kebocoran Gas Buang Relay Integrasi (relay EFI) ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor heated oxygen (sensor 1) Heater sensor heated oxygen (sensor 1) Sensor heat
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTCS LAIN (SEBAGAI TAMBAHAN KE DTC P0134): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI INTELLIGENT TESTER (OUTPUT VOLTAGE OF HEATED OXYGEN SENSOR): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hidupkan mesin. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / O2S B1S1 and Engine Speed. -> Hidupkan mesin sampai
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SAMBUNGAN SELANG PCV
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER): Lepas hubungan konektor C36 sensor HO2 (sensor 1). -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA RELAY INTEGRASI (EFI RELAY): Lepas relay integrasi dari relay block ruang mesin. -> Periksa fuse EFI . -> Periksa relay EFI. -> Pasang kembali relay integrasi.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR HEATED OXYGEN - ECM): Lepas hubungan konektor C36 sensor HO2 (sensor 1). -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor H02. -> Hubungkan kembali konektor ECM.
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DI MANA TERJADINYA MISFIRE DENGAN MEMONITOR DTC DAN DATA LIST
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SISTEM INDUKSI UDARA: Periksa sistem induksi udara untuk kebocoran vakum.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: HT1A (1) - +B (2)` : **5.3 sampai 7.5 Ω pada 20 °C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: HT1A (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **Di bawah 1 Ω (Masukkan voltase baterai antara terminal 1A-2 dan 1A-3)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): OX1A (C36-3) - OX1A (C20-112)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): HT1A (C36-1) - HT1A (C20-109)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): OX1A (C36-3) atau OX1A (C20-112) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): HT1A (C36-1) atau HT1A (C20-109) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0136` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit Sensor Oksigen (Bank 1 Sensor 2) (Dokumen: RM000000TEO00NX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Malfungsi Sirkuit Sensor Oksigen (Bank 1 Sensor 2) (Dokumen: RM000000TEO02CX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor HO2 (sensor 2) Sensor HO2 (sensor 2) Sensor HO2 (sensor 2) Relay Integrasi (relay EFI); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor Heated Oxygen (sensor 2) Sensor Heated Oxygen (sensor 2) Heater sensor Heated Oxygen (sensor 2) Relay Integrasi (relay EFI)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTCS LAIN (SEBAGAI TAMBAHAN KE DTC P0136): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI PADA INTELLIGENT TESTER (TEGANGAN OUTPUT SENSOR HEATED OXYGEN BANK SENSOR 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / O2S B1 S2. -> Biarkan mesin idle selama 3 menit pada 2.500 rpm. -> Tek
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER): Lepas hubungan konektor D28 sensor H2O (sensor 2). -> Ukur tahanan. -> Hubungkan kembali konektor sensor H02.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA RELAY INTEGRASI (EFI RELAY): Lepas relay integrasi dari relay block ruang mesin. -> Periksa fuse EFI . -> Periksa relay EFI. -> Pasang kembali relay integrasi.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (HEATED OXYGEN SENSOR (SENSOR2)- ECM): Lepas hubungan konektor D28 sensor H2O (sensor 2). -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor sensor H02.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN KONFIRMASI POLA PENGENDARAAN
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P0136): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: HT1B (1) - +B (2)` : **11 sampai 16 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: HT1B (1) - E2 (4)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1C-1 - 1A-4` : **Di bawah 1 Ω (Masukkan voltase baterai antara terminal 1A-2 dan 1A-3)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): OX1B (D28-3) - OX1B (C20-64)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): HT1B (D28-1) - HT1B (C20-47)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): OX1B (D28-3) atau OX1B (C20-64) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): HT1B (D28-1) atau HT1B (C20-47) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0220` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P0222` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "B" Sensor /Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "B" Sensor /Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P0223` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "B" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "B" Sensor/Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P0327` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit Sensor Knock 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT00TX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit Sensor Knock 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT033X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit knock sensor Sensor knock ECM; Kondisi Deteksi: Voltase output dari knock sensor 0.5 V atau kurang (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit sensor knock Sensor knock ECM; Kondisi Deteksi: Voltase output dari sensor knock 4.5 V atau lebih (1 trip detection logic); Kondisi Deteksi: Output voltase sensor knock adalah 0.5 V atau kurang se
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (KNOCK FEEDBACK VALUE): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Panaskan mesin. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Knock Feedback Value. -> Baca nilai yang dtampilkan pada tester selagi
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ECM - SENSOR KNOCK): Lepas hubungan konektor C20 ECM. -> Ukur tahanan antar terminal-terminalnya. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE KNK1): Lepas hubungan konektor P1 knock sensor. -> Putar switch pengapian ke on (IG). -> Ukur tahanan antara terminal knock sensor -> Hubungkan kembali konektor sensor knock.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA KNOCK SENSOR: Lepas knock sensor (Lihat halaman ). -> Ukur tahanan antar terminal-terminalnya. -> Pasang kembali knock sensor (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR KNOCK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: KNK1 (C20-110) - EKNK (C20-111)` : **120 sampai 280 kΩ pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: KNK1 (P1-2) - EKNK (P1-1)` : **4.5 sampai 5.5 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: KNK1 (2) - EKNK (1)` : **120 sampai 280 kΩ pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: N1-2 (KNK1) - N1-1 (EKNK) (Switch pengapian on (IG))` : **4.5 sampai 5.5 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (20°C (68°F))` : **120 sampai 280 kΩ**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): N1-2 (KNK1) - C23-110 (KNK1) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): N1-1 (EKNK) - C23-111 (EKNK) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): N1-2 (KNK1) atau C23-110 (KNK1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0328` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Sensor Knock 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT00TX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input pada Sirkuit Sensor Knock 1 (Bank 1 atau Single Sensor) (Dokumen: RM000000SVT033X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit knock sensor Sensor knock ECM; Kondisi Deteksi: Voltase output dari knock sensor 0.5 V atau kurang (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit sensor knock Sensor knock ECM; Kondisi Deteksi: Voltase output dari sensor knock 4.5 V atau lebih (1 trip detection logic); Kondisi Deteksi: Output voltase sensor knock adalah 0.5 V atau kurang se
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (KNOCK FEEDBACK VALUE): Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin dan hidupkan tester. -> Panaskan mesin. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Knock Feedback Value. -> Baca nilai yang dtampilkan pada tester selagi
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ECM - SENSOR KNOCK): Lepas hubungan konektor C20 ECM. -> Ukur tahanan antar terminal-terminalnya. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE KNK1): Lepas hubungan konektor P1 knock sensor. -> Putar switch pengapian ke on (IG). -> Ukur tahanan antara terminal knock sensor -> Hubungkan kembali konektor sensor knock.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA KNOCK SENSOR: Lepas knock sensor (Lihat halaman ). -> Ukur tahanan antar terminal-terminalnya. -> Pasang kembali knock sensor (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR KNOCK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: KNK1 (C20-110) - EKNK (C20-111)` : **120 sampai 280 kΩ pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: KNK1 (P1-2) - EKNK (P1-1)` : **4.5 sampai 5.5 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: KNK1 (2) - EKNK (1)` : **120 sampai 280 kΩ pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: N1-2 (KNK1) - N1-1 (EKNK) (Switch pengapian on (IG))` : **4.5 sampai 5.5 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (20°C (68°F))` : **120 sampai 280 kΩ**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): N1-2 (KNK1) - C23-110 (KNK1) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): N1-1 (EKNK) - C23-111 (EKNK) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): N1-2 (KNK1) atau C23-110 (KNK1) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0335` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Sensor Posisi Crankshaft "A" (Dokumen: RM000000TCW01IX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Sensor Posisi Crankshaft "A" (Dokumen: RM000000TCW04HX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor CKP Sensor CKP Plat sensor CKP ECM; Kondisi Deteksi: Tidak ada sinyal sensor CKP ke ECM saat berputar (1 trip detection logic) Tidak ada sinyal sensor CKP ke ECM saat mesin berputar 600 rpm atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor posisi crankshaft Sensor posisi crankshaft Sensor posisi cr
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE SPEED): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Engine Speed. -> Hidupkan mesin. -> Baca nilai yang ditampilkan pada t
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR POSISI CRANKSHAFT (TAHANAN): Lepas hubungan konektor C2 sensor posisi crankshaft (CKP). -> Ukur tahanan antara terminal 1 dan 2. -> Hubungkan kembali konektor sensor (CKP).
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI CRANKSHAFT - ECM): Lepas hubungan konektor sensor C2 CKP. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor sensor (CKP).
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA PEMASANGAN SENSOR (CRANKSHAFT POSITION SENSOR): Periksa pemasangan sensor CKP.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA PLAT SENSOR POSISI CRANKSHAFT (GIGI SENSOR PLATE): Periksa gigi plat sensor.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR POSISI CRANKSHAFT
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0335 ATAU P0339): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Dingin)` : **985 sampai 1,600 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Panas)` : **1,265 sampai 1,890 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): NE+ (C2-1) - NE+ (C20-122)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): NE- (C2-2) - NE- (C20-121)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): NE+ (C2-1) atau NE+ (C20-122) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): NE- (C2-2) atau NE- (C20-121) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Dingin)` : **985 sampai 1600 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Panas)` : **1265 sampai 1890 Ω**

### DTC `P0339` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Intermittent pada Sirkuit "A" Sensor Posisi Crankshaft (Dokumen: RM000000TCW01IX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Intermittent pada Sirkuit "A" Sensor Posisi Crankshaft (Dokumen: RM000000TCW04HX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor CKP Sensor CKP Plat sensor CKP ECM; Kondisi Deteksi: Tidak ada sinyal sensor CKP ke ECM saat berputar (1 trip detection logic) Tidak ada sinyal sensor CKP ke ECM saat mesin berputar 600 rpm atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sensor posisi crankshaft Sensor posisi crankshaft Sensor posisi cr
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (ENGINE SPEED): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Engine Speed. -> Hidupkan mesin. -> Baca nilai yang ditampilkan pada t
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR POSISI CRANKSHAFT (TAHANAN): Lepas hubungan konektor C2 sensor posisi crankshaft (CKP). -> Ukur tahanan antara terminal 1 dan 2. -> Hubungkan kembali konektor sensor (CKP).
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI CRANKSHAFT - ECM): Lepas hubungan konektor sensor C2 CKP. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor sensor (CKP).
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA PEMASANGAN SENSOR (CRANKSHAFT POSITION SENSOR): Periksa pemasangan sensor CKP.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA PLAT SENSOR POSISI CRANKSHAFT (GIGI SENSOR PLATE): Periksa gigi plat sensor.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR POSISI CRANKSHAFT
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0335 ATAU P0339): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Dingin)` : **985 sampai 1,600 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Panas)` : **1,265 sampai 1,890 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): NE+ (C2-1) - NE+ (C20-122)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): NE- (C2-2) - NE- (C20-121)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): NE+ (C2-1) atau NE+ (C20-122) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): NE- (C2-2) atau NE- (C20-121) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Dingin)` : **985 sampai 1600 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Panas)` : **1265 sampai 1890 Ω**

### DTC `P0340` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit "A" Sensor Posisi Camshaft (Bank 1 atau Single Sensor) (Dokumen: RM0000012JE007X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit "A" Sensor Posisi Camshaft (Bank 1 atau Single Sensor) (Dokumen: RM0000012JE019X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short di sirkuit sensor CMP Sensor CMP Camshaft Rantai timing lompat gigi ECM; Kondisi Deteksi: Kasus 1 Tidak ada sinyal sensor Posisi Camshaft (CMP) ke ECM selama cranking (2 trip detection logic) Kasus 2 Ketidaklurusan Camshaft/Crankshaft terdeteksi pada kecepatan mesin 600 rpm atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit se
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SENSOR POSISI CAMSHAFT (TAHANAN): Lepas hubungan konektor sensor C18 Posisi Camshaft (CMP) . -> Ukur tahanan antara terminal 1 dan 2. -> Hubungkan kembali konektor sensor CMP.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI CAMSHAFT - ECM): Lepas hubungan konektor sensor C18 CMP. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor sensor CMP.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA PEMASANGAN SENSOR (SENSOR POSISI CAMSHAFT): Periksa pemasangan sensor CKP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA VALVE TIMING: Lepas cover cylinder head. -> Putar puli crankshaft , dan luruskan alurnya dengan tanda timing "0" pada cover rantai timing. -> Periksa tanda timing pada timing sproket camshaft dan camshaft timing gear menghadap ke atas seperti ditunjukkan
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA CAMSHAFT: Periksa gigi camshaft.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR POSISI CAMSHAFT
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0340): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SENSOR POSISI CAMSHAFT
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Dingin)` : **1,630 sampai 2,740 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Panas)` : **2,065 sampai 3,225 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): G2+ (C18-1) - G2+ (C20-99)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): NE- (C18-2) - NE- (C20-121)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): G2+ (C18-1) atau G2+ (C20-99) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): NE- (C18-2) atau NE- (C20-121) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Dingin)` : **1630 sampai 2740 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Panas)` : **2065 sampai 3225 Ω**

### DTC `P0351` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "A" (Dokumen: RM000000XH4012X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "A" (Dokumen: RM000000XH4039X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short di IGF1 atau sirkuit IGT (1 hingga 4) antara koil pengapian dengan igniter dan ECM No. 1 hingga No. 4 koil pengapian dengan igniter ECM; Kondisi Deteksi: Tidak ada sinyal IGF ke ECM selama mesin sedang hidup (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short dalam sirkuit IGF1 atau IGT (1 sampai 4) Koil pengapian No. 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA KOIL PENGAPIAN ASSEMBLY (POWER SOURCE): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Periksa tahanan. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor. -> Hubungkan kembali ignition coil 
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (KOIL PENGAPIAN ASSEMBLY - ECM): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali ignition coil dan konektor igniter .
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG KEMBALI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Pindah-pindahkan pengaturan koil pengapian dengan igniter (di antara silinder No. 1 ke No. 4 ). -> Lakukan tes
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI KOIL PENGAPIAN ASSEMBLY
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN TES SIMULASI (SALING PERTUKARKAN SUSUNAN KOIL PENGAPIAN): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan koil pengapian (antara silinder No. 1 sampai silinder No. 4 ). -> Lakukan tes simul
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C11-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C12-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C13-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C14-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C11-1) - GND (C11-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C12-1) - GND (C12-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C13-1) - GND (C13-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C14-1) - GND (C14-4)` : **11 sampai 14 V**

### DTC `P0352` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "B" (Dokumen: RM000000XH4012X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "B" (Dokumen: RM000000XH4039X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short di IGF1 atau sirkuit IGT (1 hingga 4) antara koil pengapian dengan igniter dan ECM No. 1 hingga No. 4 koil pengapian dengan igniter ECM; Kondisi Deteksi: Tidak ada sinyal IGF ke ECM selama mesin sedang hidup (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short dalam sirkuit IGF1 atau IGT (1 sampai 4) Koil pengapian No. 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA KOIL PENGAPIAN ASSEMBLY (POWER SOURCE): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Periksa tahanan. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor. -> Hubungkan kembali ignition coil 
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (KOIL PENGAPIAN ASSEMBLY - ECM): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali ignition coil dan konektor igniter .
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG KEMBALI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Pindah-pindahkan pengaturan koil pengapian dengan igniter (di antara silinder No. 1 ke No. 4 ). -> Lakukan tes
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI KOIL PENGAPIAN ASSEMBLY
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN TES SIMULASI (SALING PERTUKARKAN SUSUNAN KOIL PENGAPIAN): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan koil pengapian (antara silinder No. 1 sampai silinder No. 4 ). -> Lakukan tes simul
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C11-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C12-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C13-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C14-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C11-1) - GND (C11-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C12-1) - GND (C12-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C13-1) - GND (C13-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C14-1) - GND (C14-4)` : **11 sampai 14 V**

### DTC `P0353` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "C" (Dokumen: RM000000XH4012X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "C" (Dokumen: RM000000XH4039X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short di IGF1 atau sirkuit IGT (1 hingga 4) antara koil pengapian dengan igniter dan ECM No. 1 hingga No. 4 koil pengapian dengan igniter ECM; Kondisi Deteksi: Tidak ada sinyal IGF ke ECM selama mesin sedang hidup (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short dalam sirkuit IGF1 atau IGT (1 sampai 4) Koil pengapian No. 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA KOIL PENGAPIAN ASSEMBLY (POWER SOURCE): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Periksa tahanan. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor. -> Hubungkan kembali ignition coil 
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (KOIL PENGAPIAN ASSEMBLY - ECM): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali ignition coil dan konektor igniter .
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG KEMBALI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Pindah-pindahkan pengaturan koil pengapian dengan igniter (di antara silinder No. 1 ke No. 4 ). -> Lakukan tes
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI KOIL PENGAPIAN ASSEMBLY
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN TES SIMULASI (SALING PERTUKARKAN SUSUNAN KOIL PENGAPIAN): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan koil pengapian (antara silinder No. 1 sampai silinder No. 4 ). -> Lakukan tes simul
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C11-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C12-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C13-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C14-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C11-1) - GND (C11-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C12-1) - GND (C12-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C13-1) - GND (C13-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C14-1) - GND (C14-4)` : **11 sampai 14 V**

### DTC `P0354` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "D" (Dokumen: RM000000XH4012X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Primer/ Sekunder Koil Pengapian "D" (Dokumen: RM000000XH4039X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short di IGF1 atau sirkuit IGT (1 hingga 4) antara koil pengapian dengan igniter dan ECM No. 1 hingga No. 4 koil pengapian dengan igniter ECM; Kondisi Deteksi: Tidak ada sinyal IGF ke ECM selama mesin sedang hidup (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sistem pengapian Open atau short dalam sirkuit IGF1 atau IGT (1 sampai 4) Koil pengapian No. 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA KOIL PENGAPIAN ASSEMBLY (POWER SOURCE): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Periksa tahanan. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor. -> Hubungkan kembali ignition coil 
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (KOIL PENGAPIAN ASSEMBLY - ECM): Lepas hubungan konektor C11, C12, C13 atau C14 koil pengapian dengan konektor igniter. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali ignition coil dan konektor igniter .
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH OUTPUT DTC BERULANG KEMBALI ATAU TIDAK (DTC P0351, P0352, P0353 ATAU P0354): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Pindah-pindahkan pengaturan koil pengapian dengan igniter (di antara silinder No. 1 ke No. 4 ). -> Lakukan tes
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI KOIL PENGAPIAN ASSEMBLY
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN TES SIMULASI (SALING PERTUKARKAN SUSUNAN KOIL PENGAPIAN): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Saling pertukarkan susunan koil pengapian (antara silinder No. 1 sampai silinder No. 4 ). -> Lakukan tes simul
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C11-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C12-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C13-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): GND (C14-4) - Masa bodi` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C11-1) - GND (C11-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C12-1) - GND (C12-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C13-1) - GND (C13-4)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +B (C14-1) - GND (C14-4)` : **11 sampai 14 V**

### DTC `P0443` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Purge Control Valve Sistem Evaporative Emission Control (Dokumen: RM000000VSO005X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Purge Control Valve Sistem Evaporative Emission Control (Dokumen: RM000000VSO014X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam VSV untuk sirkuit EVAP VSV untuk EVAP ECM; Kondisi Deteksi: Voltase terminal dari sirkuit output ECM tidak berhubungan dengan gerak sinyal dari ECM ke EVAP VSV (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit purge VSV Purge VSV ECM; Kondisi Deteksi: Voltase terminal dari sirkuit output ECM tidak berhubungan dengan gerak sinyal d
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER ( AKTIFKAN VSV UNTUK KONTROL EVEP): Hubungkan intelligent tester ke DLC3. -> Lepas selang vakum dari VSV for EVAP dari charcoal canister. -> Hidupkan mesin dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Active Test / Activate the VSV for Ev
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DUTY VACUUM SWITCHING VALVE (VSV FOR EVAP): Lepas hubungan konektor C3 duty vacuum switching valve. -> Ukur tahanan antara terminal-terminal duty vacuum switching valve. -> Hubungkan kembali konektor duty vacuum switching valve
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DUTY VACUUM SWITCHING VALVE (VSV FOR EVAP): Lepas hubungan konektor C3 duty vacuum switching valve. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal wire harness sisi konektor dan masa bodi. -> Hubungkan kembali konektor duty vacuum switching valve
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (VSV forEVAP- RELAY INTEGRATION): Lepas relay integrasi dari relay block ruang mesin. -> Lepas hubungan konektor C3 duty vacuum switching valve. -> Periksa tahanan. -> Pasang kembali relay integrasi. -> Hubungkan kembali konektor duty vacuum switching valve
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (VSV forEVAP- ECM): Lepas hubungan konektor C20 ECM. -> Lepas hubungan konektor C3 duty vacuum switching valve. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor duty vacuum switching valve
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI DUTY VACUUM SWITCHING VALVE
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar: VSV ON` : **Lepas hubungan selang yang digunakan sebagai penghisap dari jari Anda**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar: VSV OFF` : **Lepas hubungan selang yang tidak digunakan sebagai penghisap dari jari Anda**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VSV untuk EVAP (C3-2) - Masa bodi` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VSV untuk EVAP (C3-2) - Relay block ruang mesin (1A-4)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VSV untuk EVAP (C3-2) atau Relay block ruang mesin (1A-4) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VSV untuk EVAP (C3-1) - PRG (C20-49)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VSV untuk EVAP (C3-1) atau PRG (C20-49) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Standar: VSV ON` : **Saluran purge VSV menghisap ke jari**

### DTC `P0500` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Speed Sensor Kendaraan "A" (Dokumen: RM0000012ME007X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Speed Sensor Kendaraan "A" (Dokumen: RM0000012ME01GX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Speed Sensor Kendaraan "A" (Dokumen: RM0000012ME06EX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sinyal kecepatan Meter kombinasi Sirkuit speedometer ECM Speed sensor kendaraan; Kondisi Deteksi: Selama kendaraan sedang dikendarai, tidak ada sinyal speed sensor ke ECM. (1 trip detection logic: Transaxle Otomatis) (2 trip detection logic: Transaxle manual); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open atau short dalam sirkuit sinyal kecepatan Meter kombinasi ECM EC
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA CARA KERJA SPEEDOMETER: Jalankan kendaraan dan periksa apakah speedometer dalam meter kombinasi bekerja secara bormal.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (KECEPATAN MESIN ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT/ Data List / Vehicle Speed. -> Jalankan kendaraan. -> Baca nilai yang ditampilkan pa
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA METER KOMBINASI (+S VOLTASE): Lepas hubungan konektor D1 meter kombinasi. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal meter kombinasi dan masa bodi. -> Hubungkan kembali konektor meter kombinasi.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA METER KOMBINASI (SPD BENTUK GELOMBANG SINYAL): Geser tuas gear selector ke posisi netral -> Dongkrak kendaraan. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal meter kombinasi dan masa bodi sembari roda diputar pelan.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (METER KOMBINASI ASSEMBLY - ECM): Lepas hubungan konektor D1 meter kombinasi. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor meter kombinasi. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUT KE MALFUNGSI DALAM SPEEDOMETER
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI METER KOMBINASI ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +S (D1-16) - Masa bodi` : **4.5 sampai 5.5 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +S (D1-16) - Masa bodi` : **Voltase dibangkitkan secara terputus-putus**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): +S (D1-16) - SPD (A21-8)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): +S (D1-16) atau SPD (A21-8) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase Standar: D1-16 (+S) - Masa bodi (Switch pengapian on (IG))` : **4.5 sampai 5.5 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan Standar (Periksa dari Open): D1-16 (+S) - A20-8 (SPD) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan Standar (Periksa dari Short): D1-16 (+S) atau A20-8 (SPD) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0504` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Switch Rem "A" / "B" Berhubungan (Dokumen: RM000000XCT00OX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Switch Rem "A" / "B" Berhubungan (Dokumen: RM000000XCT02OX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ON; Kondisi Deteksi: OFF; Kondisi Deteksi: ON; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit sinyal switch lampu rem Switch lampu rem Fuse STOP Fuse IGN ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SWITCH LAMPU STOP ASSEMBLY (VOLTASE TERMINAL): Lepas hubungan konektor A13 switch lampu rem. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal ST1-dan STP dari konektor switch lampu rem A13 dan masa bodi. -> Hubungkan kembali konektor switch lampu rem.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SWITCH LAMPU REM ASSEMBLY: Lepas switch lampu rem assembly. -> Periksa tahanan. -> Pasang kembali switch lampu rem assembly.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (STP DAN ST1 - VOLTASE): Lepas hubungan konektor A21 ECM. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal ST1-dan STP dari konektor ECM A13 dan masa bodi. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SEKRING (STOP DAN SEKRING IGN): Lepas fuse STOP dan IGN dari main body ECU. -> Periksa tahanan. -> Pasang kembali fuse STOP dan fuse IGN.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SWITCH LAMPU REM ASSEMBLY
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DARI SHORT PADA SEMUA HARNESS DAN KONEKTOR YANG DIHUBUNGKAN KE FUSE DAN GANTI FUSE
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Pin switch dibebaskan)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Pin switch ditekan ke dalam)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 3 - 4 (Pin switch dibebaskan)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 3 - 4 (Pin switch ditekan ke dalam)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: ST1- (A21-35) - Masa bodi (Dibebaskan)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: ST1- (A21-35) - Masa bodi (Ditekan)` : **0 sampai 3 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: STP (A21-36) - Masa bodi (Dibebaskan)` : **0 sampai 3 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: STP (A21-36) - Masa bodi (Ditekan)` : **11 sampai 14 V**

### DTC `P0560` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Voltase Sistem (Dokumen: RM000000T8P01JX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Voltase Sistem (Dokumen: RM000000T8P04RX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit back-up power source Baterai Terminal baterai Fuse EFI ECM; Kondisi Deteksi: Open dalam sirkuit back-up power source ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA FUSE (FUSE EFI): Cabut fuse EFI dari relay block ruang mesin . -> Periksa tahanan fuse EFI. -> Pasang kembali fuse EFI.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA RANGKAIAN DAN KONEKTOR (ECM - EFI FUSE, EFI FUSE - BATTERY): Periksa harness dan konektor antara fuse EFI dan ECM. -> Periksa harness dan konektor antara fuse EFI dan baterai.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BATERAI: Periksa bahwa filter tidak tersumbat.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERMINAL BATERAI: Periksa bahwa terminal baterai tidak kendur atau berkarat.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA MANA OUTPUT DTC YANG LAGI-LAGI TIMBUL (DTC P0560): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar switch pengapian ke off dan putar tester ke off. -> Hidupkan mesin dan hidupkan tester. -> Pilih item me
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DARI SHORT PADA SEMUA HARNESS DAN KONEKTOR YANG DIHUBUNGKAN KE FUSE DAN GANTI FUSE
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI BATERAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): Fuse EFI (2) - BATT (A21-20)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): Fuse EFI (2) atau BATT (A21-20) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): Terminal baterai positif - EFI fuse (1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): Terminal baterai positif atau EFI fuse (1) Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: Fuse EFI (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): 2 (Fuse EFI) - A20-20 (BATT) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): 2 (Fuse EFI) atau A20-20 (BATT) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): 1 (Fuse EFI) - Terminal positif baterai (Selalu)` : **Di bawah 1 Ω**

### DTC `P0604` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Error pada Modul Kontrol Internal dalam Random Access Memory (RAM) (Dokumen: RM000000W9500WX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Error pada Modul Kontrol Internal dalam Random Access Memory (RAM) (Dokumen: RM000000W9503BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan internal ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTCS LAIN (SEBAGAI TAMBAHAN KE DTC P0604, P0606, P0607 ATAU P0657): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTC LAINNYA (SEBAGAI TAMBAHAN UNTUK INTERNAL ERROR DTC dari ECM): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `P0606` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] ECM / PCM Processor (Dokumen: RM000000W9500WX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] ECM / PCM Processor (Dokumen: RM000000W9503BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan internal ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTCS LAIN (SEBAGAI TAMBAHAN KE DTC P0604, P0606, P0607 ATAU P0657): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTC LAINNYA (SEBAGAI TAMBAHAN UNTUK INTERNAL ERROR DTC dari ECM): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `P0607` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Kinerja Control Module (Dokumen: RM000000W9500WX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan internal ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTCS LAIN (SEBAGAI TAMBAHAN KE DTC P0604, P0606, P0607 ATAU P0657): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM

### DTC `P060A` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Internal Control Module Monitoring Processor Performance (Dokumen: RM000000W9503BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan internal ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTC LAINNYA (SEBAGAI TAMBAHAN UNTUK INTERNAL ERROR DTC dari ECM): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM

### DTC `P060D` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Internal Control Module Accelerator Pedal Position Performance (Dokumen: RM000000W9503BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan internal ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTC LAINNYA (SEBAGAI TAMBAHAN UNTUK INTERNAL ERROR DTC dari ECM): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM

### DTC `P060E` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Internal Control Module Throttle Position Performance (Dokumen: RM000000W9503BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan internal ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTC LAINNYA (SEBAGAI TAMBAHAN UNTUK INTERNAL ERROR DTC dari ECM): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM

### DTC `P0617` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Starter Relay Circuit High (Dokumen: RM000000TA001OX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Starter Relay Circuit High (Dokumen: RM000000TA004YX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Switch Park/Neutral Position (PNP) (A/T * ) Clutch start switch (M/T * ) Sirkuit relay starter Switch pengapian ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Clutch start switch Sirkuit relay starter Switch pengapian *1 Main body ECU *2 ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (RELAY STARTER): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Active test / Activate the Starter Relay. -> Baca nilai yang didisplay pada tester
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (SINYAL STARTER ): Periksa sirkuit clutch start switch (untuk model transaxle manual). -> Periksa sirkuit switch Park/Neutral Position (PNP) (untuk model transaxle otomatis ).
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (STA VOLTASE TERMINAL): Lepas hubungan konektor A21 ECM. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor ECM dan Masa bodi. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA POSISI PARK/NEUTRAL ATAU SWITCH CLUTCH START: Periksa sirkuit clutch start switch (untuk model manual transaxle ). -> Periksa switch PNP (untuk model transaxle otomatis ).
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SWITCH POSISI PARK/NEUTRAL ATAU SWITCH CLUTCH START
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SWITCH PENGAPIAN ATAU STARTER ASSEMBLY: Lepas hubungan konektor D8 switch pengapian -> Periksa tahanan. -> Hubungkan kembali konektor switch pengapian.
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (SINYAL STARTER ): Periksa sirkuit clutch start switch (untuk model transaxle manual). -> Periksa sirkuit switch Park/Neutral Position (PNP) (untuk model transaxle otomatis ).
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (STA VOLTASE TERMINAL): Lepas hubungan konektor A21 ECM. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor ECM dan Masa bodi. -> Hubungkan kembali konektor ECM.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] OK: Switch pengapian on (IG)` : **OFF**
  - `[SISTEM KONTROL MESIN 1NZ-FE] OK: Hidupkan mesin` : **ON**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: Didorong ke dalam` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: Dibebaskan` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: P (2 - 6, 4 - 5)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: R (1 - 2)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: N (2 - 9, 4 - 5)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: D (2 - 7)` : **Di bawah 1 Ω**

### DTC `P0657` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Voltase Suplai Aktuator / Open (Dokumen: RM000000W9500WX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sirkuit Voltase Suplai Aktuator / Open (Dokumen: RM000000W9503BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ECM; Kondisi Deteksi: Kesalahan internal ECM (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTCS LAIN (SEBAGAI TAMBAHAN KE DTC P0604, P0606, P0607 ATAU P0657): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BEBERAPA OUTPUT DTC LAINNYA (SEBAGAI TAMBAHAN UNTUK INTERNAL ERROR DTC dari ECM): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `P0705` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Malfungsi Sirkuit Sensor Range Transmisi (Input PRNDL) (Dokumen: RM000000W8401MX) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Malfungsi Sirkuit Sensor Range Transmisi (Input PRNDL) (Dokumen: RM000000W84068X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open atau short dalam sirkuit switch posisi parkir/netral Switch posisi parkir/netral ECU kontrol pengunci pemindah gigi ECM; Kondisi Deteksi: (a) Terdapat 2 atau lebih sinyal berikut ON secara simultan. (2-trip detection logic) Sinyal input P Sinyal input R Sinyal input N Sinyal input D Sinyal input 2 Sinyal input L (b) Semua switch OFF secara simultan dari po; Kondisi Deteksi: (a) Terdapat 2 atau lebih 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — BACA NILAI MENGGUNAKAN DATA LIST (PARK/NEUTRAL POSITION SWITCH): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan intelligent tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List. -> Sesuai dengan yang ditampilkan dalam tester, baca Data L
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (POWER SOURCE DARI SWITCH POSISI PARKIR/NETRAL): Lepas hubungan konektor switch posisi parkir/netral. -> Putar switch pengapian ke on (IG), dan ukur voltasenya.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA POSISI SWITCH PARKIR/NETRAL ASSEMBLY: Lepas hubungan konektor switch posisi parkir/netral. -> Ukur tahanan ketika shift lever digerakkan ke setiap posisi.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (SWITCH POSISI PARKIR/NETRAL - ECM): Hubungkan konektor switch posisi parkir/netral. -> Lepas hubungan konektor shift lock control ECU. -> Lepas hubungan konektor ECM. -> Putar switch pengapian ke on )IG), dan ukur voltase ketika shift lever digerakkan ke setiap posisi.
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (SWITCH POSISI PARKIR/NETRAL - SHIFT LOCK CONTROL ECU - ECM): Lepas hubungan konektor shift lock control ECU. -> Putar switch pengapian ke on )IG), dan ukur voltase ketika shift lever digerakkan ke setiap posisi.
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT LOCK CONTROL ECU SUB-ASSEMBLY: Hubungkan konektor shift lock control ECU. -> Putar switch pengapian ke on )IG), dan ukur voltase ketika shift lever digerakkan ke setiap posisi.
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (SHIFT LOCK CONTROL ECU - ECM): Lepas hubungan konektor ECM. -> Putar switch pengapian ke on (IG), dan ukur voltasenya.
  - Langkah 8 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Voltase standar: 2 (RB) - Masa bodi` : **10 sampai 14 V**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: P (2 (RB) - 6 (PL))` : **Di bawah 1 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Kecuali P (2 (RB) - 6 (PL))` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: R (2 (RB) - 1 (RL))` : **Di bawah 1 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Kecuali R (2 (RB) - 1 (RL))` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: N (2 (RB) - 9 (NL))` : **Di bawah 1 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Kecuali N (2 (RB) - 9 (NL))` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: D atau 3 (2 (RB) - 7 (DL))` : **Di bawah 1 Ω**

### DTC `P0710` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Sirkuit Sensor Temperatur Fluida transmisi "A" (Dokumen: RM000000W8501MX) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Sirkuit Sensor Temperatur Fluida transmisi "A" (Dokumen: RM000000W85057X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open atau short dalam sirkuit sensor temperatur ATF Kabel transmisi (Sensor temperatur ATF) ECM; Kondisi Deteksi: Keduanya (a) dan (b) segera terdeteksi dalam waktu 0.5 detik ketika P0712 ataupun P0713 tak terdeteksi. (1-trip detection logic) (a) Tahanan sensor temperatur ATF kurang dari 79 Ω. (b) Tahanan sensor temperatur ATF lebih; [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short sirkuit dalam sensor tem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SENSOR TEMPERATUR ATF): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor kabel transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SENSOR TEMPERATUR ATF): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor kabel transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 (THO) - 6 (E2)` : **79 Ω sampai 156 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 (THO) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 6 (E2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 20°C (68°F)` : **3 sampai 4 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 110°C (230°F)` : **0.22 sampai 0.28 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 72 (THO1) - 95 (ETHO)` : **79 Ω sampai 156 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 72 (THO1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 95 (ETHO) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0712` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Low Input pada Surkuit Sensor Temperatur Fluida transmisi "A" (Dokumen: RM000000W8501MX) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Low Input pada Surkuit Sensor Temperatur Fluida transmisi "A" (Dokumen: RM000000W85057X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open atau short dalam sirkuit sensor temperatur ATF Kabel transmisi (Sensor temperatur ATF) ECM; Kondisi Deteksi: Keduanya (a) dan (b) segera terdeteksi dalam waktu 0.5 detik ketika P0712 ataupun P0713 tak terdeteksi. (1-trip detection logic) (a) Tahanan sensor temperatur ATF kurang dari 79 Ω. (b) Tahanan sensor temperatur ATF lebih; [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short sirkuit dalam sensor tem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SENSOR TEMPERATUR ATF): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor kabel transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SENSOR TEMPERATUR ATF): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor kabel transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 (THO) - 6 (E2)` : **79 Ω sampai 156 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 (THO) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 6 (E2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 20°C (68°F)` : **3 sampai 4 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 110°C (230°F)` : **0.22 sampai 0.28 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 72 (THO1) - 95 (ETHO)` : **79 Ω sampai 156 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 72 (THO1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 95 (ETHO) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0713` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] High Input pada Sirkuit Sensor Temperatur Fluida transmisi "A" (Dokumen: RM000000W8501MX) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] High Input pada Sirkuit Sensor Temperatur Fluida transmisi "A" (Dokumen: RM000000W85057X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open atau short dalam sirkuit sensor temperatur ATF Kabel transmisi (Sensor temperatur ATF) ECM; Kondisi Deteksi: Keduanya (a) dan (b) segera terdeteksi dalam waktu 0.5 detik ketika P0712 ataupun P0713 tak terdeteksi. (1-trip detection logic) (a) Tahanan sensor temperatur ATF kurang dari 79 Ω. (b) Tahanan sensor temperatur ATF lebih; [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short sirkuit dalam sensor tem
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SENSOR TEMPERATUR ATF): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor kabel transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SENSOR TEMPERATUR ATF): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor kabel transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 (THO) - 6 (E2)` : **79 Ω sampai 156 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 (THO) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 6 (E2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 20°C (68°F)` : **3 sampai 4 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 110°C (230°F)` : **0.22 sampai 0.28 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 72 (THO1) - 95 (ETHO)` : **79 Ω sampai 156 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 72 (THO1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 95 (ETHO) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0717` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Tidak ada Sinyal pada Turbine Speed Sensor (Dokumen: RM0000015VR00IX) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Tidak ada Sinyal pada Turbine Speed Sensor (Dokumen: RM0000015VR01OX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open atau short dalam sirkuit transmission revolution sensor (speed sensor (NT)) Transmission revolution sensor (speed sensor (NT)) Transaxle otomatis (clutch, brake atau gear dll.) ECM; [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open atau short dalam sirkuit sensor NT kecepatan Sensor kecepatan NT Transaxle otomatis (clutch, brake atau gear dll.) ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA PEMASANGAN TRANSMISSION REVOLUTION SENSOR (NT): Periksa pemasangan transmission revolution sensor.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA TRANSMISSION REVOLUTION SENSOR: Lepas hubungan konektor transmission revolution sensor dari transaxle. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (TRANSMISSION REVOLUTION SENSOR - ECM): Hubungkan konektor transmission revolution sensor. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PASANG DENGAN SEMPURNA ATAU GANTI TRANSMISSION REVOLUTION SENSOR
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — GANTI TRANSMISSION REVOLUTION SENSOR
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA PEMASANGAN SENSOR KECEPATAN NT: Periksa pemasangan sensor kecepatan NT.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 - 2` : **560 Ω sampai 680 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 125 (NT+) - 124 (NT-)` : **560 sampai 680 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 125 (NT+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 124 (NT-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 - 2 (20°C (68°F))` : **560 sampai 680 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 125 (NT+) - 124 (NT-) (20°C (68°F))` : **560 sampai 680 kΩ**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 125 (NT+) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 124 (NT-) - Masa bodi (Selalu)` : **10 kΩ atau lebih tinggi**

### DTC `P0724` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Brake Switch "B" Circuit High (Dokumen: RM000001DN9007X) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Brake Switch "B" Circuit High (Dokumen: RM000000W8804BX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit sinyal switch lampu rem Switch lampu rem ECM; Kondisi Deteksi: Lampu stop tetap ON meski pada saat kendaraan mengulang 5 putaran STOP (kurang dari 3 km/jam (1.86 mph)) and GO (30 km/jam (18.65 mph) atau lebih) (2 trip detection logic); Kondisi Deteksi: Switch lampu rem tetap ON meski pada saat kendaraan dikendarai dalam pola GO (30 km/h (18.63 mph) atau lebih) dan pola STOP (kurang 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (STOP LIGHT SWITCH): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Stop Light Switch. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA SWITCH LAMPU REM ASSEMBLY: Lepas switch lampu rem assembly. -> Periksa tahanan. -> Pasang kembali switch lampu rem assembly.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SWITCH LAMPU REM - ECM): Lepas hubungan konektor A21 ECM. -> Lepas hubungan konektor A13 switch lampu rem. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor switch lampu rem.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI SWITCH LAMPU REM ASSEMBLY
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTEELLIGENT TESTER (STOP LIGHT SWITCH): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Stop Light Switch. -> Baca nilai yang ditampilkan pada tester ketika m
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] OK: Stop Light Switch (Status switch lampu rem ON atau OFF)` : **ON: Pedal Rem ditekan OFF: Pedal Rem dibebaskan**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Pin switch dibebaskan)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 1 - 2 (Pin switch ditekan ke dalam)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 3 - 4 (Pin switch dibebaskan)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 3 - 4 (Pin switch ditekan ke dalam)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): STP (A21-36) - Switch kampu stop (A13-1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): ST1- (A21-35) - Switch lampu rem (A13-4)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): STP (A21-36) atau Switch lampu rem (A13-1) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0787` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Shift / Timing Solenoid Low (Shift Solenoid Valve ST) (Dokumen: RM000000GLW006X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Shift / Timing Solenoid Low (Shift Solenoid Valve ST) (Dokumen: RM000000GLW00CX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short dalam sirkuit shift solenoid valve ST Shift solenoid valve ST ECM; Kondisi Deteksi: ECM mendeteksi short dalam sirkuit solenoid valve ST empat kali ketika solenoid valve ST dioperasikan. (1-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open sirkuit dalam shift solenoid valve ST Shift solenoid valve ST ECM; Kondisi Deteksi: ECM mendeteksi open dalam sirkuit solenoid valve ST 4 kali
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE ST): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE ST: Lepas shift solenoid valve ST. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE ST
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE ST): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 2 (ST) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 80 (ST) - Masa bodi` : **11 Ω sampai 15 Ω pada 20 °C (68 °F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (ST) - Solenoid Body (ST)` : **11 sampai 15 Ω pada 20 °C (68 °F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 2 (ST) - Masa bodi (20 °C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 80 (ST) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (ST) - Solenoid Body (ST) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `P0788` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Shift / Timing Solenoid High (Shift Solenoid Valve ST) (Dokumen: RM000000GLW006X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Shift / Timing Solenoid High (Shift Solenoid Valve ST) (Dokumen: RM000000GLW00CX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short dalam sirkuit shift solenoid valve ST Shift solenoid valve ST ECM; Kondisi Deteksi: ECM mendeteksi short dalam sirkuit solenoid valve ST empat kali ketika solenoid valve ST dioperasikan. (1-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open sirkuit dalam shift solenoid valve ST Shift solenoid valve ST ECM; Kondisi Deteksi: ECM mendeteksi open dalam sirkuit solenoid valve ST 4 kali
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE ST): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE ST: Lepas shift solenoid valve ST. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE ST
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE ST): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 2 (ST) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 80 (ST) - Masa bodi` : **11 Ω sampai 15 Ω pada 20 °C (68 °F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (ST) - Solenoid Body (ST)` : **11 sampai 15 Ω pada 20 °C (68 °F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 2 (ST) - Masa bodi (20 °C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 80 (ST) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (ST) - Solenoid Body (ST) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `P0973` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Low sirkuit pada Kontrol Shift Solenoid "A" (Shift Solenoid Valve S1) (Dokumen: RM000000W86013X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Low sirkuit pada Kontrol Shift Solenoid "A" (Shift Solenoid Valve S1) (Dokumen: RM000000W8602SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 ECM; Kondisi Deteksi: ECM mendeteksi short dalam sirkuit solenoid valve S1 4 kali ketika solenoid valve S1 dioperasikan. (1-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 ECM; Kondisi Deteksi: ECM mendeteksi open dalam sirkuit solenoid valve S1 4 kali ket
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE S1: Lepas shift solenoid valve S1. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE S1
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 5 (S1) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 79 (S1) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S1) - Solenoid Body (S1)` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 5 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 79 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S1) - Solenoid Body (S1) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `P0974` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] High sirkuit pada Kontrol Shift Solenoid "A" (Shift Solenoid Valve S1) (Dokumen: RM000000W86013X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] High sirkuit pada Kontrol Shift Solenoid "A" (Shift Solenoid Valve S1) (Dokumen: RM000000W8602SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 ECM; Kondisi Deteksi: ECM mendeteksi short dalam sirkuit solenoid valve S1 4 kali ketika solenoid valve S1 dioperasikan. (1-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open sirkuit dalam shift solenoid valve S1 Shift solenoid valve S1 ECM; Kondisi Deteksi: ECM mendeteksi open dalam sirkuit solenoid valve S1 4 kali ket
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE S1: Lepas shift solenoid valve S1. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE S1
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S1): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 5 (S1) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 79 (S1) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S1) - Solenoid Body (S1)` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 5 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 79 (S1) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S1) - Solenoid Body (S1) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `P0976` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Low sirkuit pada Kontrol Shift Solenoid "B" (Shift Solenoid Valve S2) (Dokumen: RM000000W87012X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Low sirkuit pada Kontrol Shift Solenoid "B" (Shift Solenoid Valve S2) (Dokumen: RM000000W8702QX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 ECM; Kondisi Deteksi: ECM mendeteksi short dalam sirkuit solenoid valve S2 4 kali ketika solenoid valve S2 dioperasikan. (1-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 ECM; Kondisi Deteksi: ECM mendeteksi open dalam sirkuit solenoid valve S2 4 kali ket
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE S2: Lepas shift solenoid valve S2. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE S2
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 10 (S2) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 78 (S2) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S2) - Solenoid Body (S2)` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 10 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 78 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S2) - Solenoid Body (S2) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `P0977` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] High sirkuit pada Kontrol Shift Solenoid "B" (Shift Solenoid Valve S2) (Dokumen: RM000000W87012X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] High sirkuit pada Kontrol Shift Solenoid "B" (Shift Solenoid Valve S2) (Dokumen: RM000000W8702QX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 ECM; Kondisi Deteksi: ECM mendeteksi short dalam sirkuit solenoid valve S2 4 kali ketika solenoid valve S2 dioperasikan. (1-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open dalam sirkuit shift solenoid valve S2 Shift solenoid valve S2 ECM; Kondisi Deteksi: ECM mendeteksi open dalam sirkuit solenoid valve S2 4 kali ket
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE S2: Lepas shift solenoid valve S2. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE S2
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE S2): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 10 (S2) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 78 (S2) - Masa bodi` : **11 Ω sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S2) - Solenoid Body (S2)` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 10 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 78 (S2) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor solenoid (S2) - Solenoid Body (S2) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `P2102` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM000000PFU01FX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM000000PFU03ZX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit aktuator throttle Aktuator throttle ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit aktuator throttle Aktuator throttle Throttle valve Throttle body assembly ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit aktuator throttle Throttle body assembly ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit aktuator throttle Throttle
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA THROTTLE BODY ASSEMBLY (TAHANAN AKTUATOR THROTTLE): Lepas hubungan konektor C17 throttle body. -> Ukur tahanan antara terminal aktuator throtle. -> Hubungkan kembali konektor throttle body.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (AKTUATOR THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA THROTTLE BODY ASSEMBLY: Periksa adanya benda asing antara katup throtle dan rumahnya.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PEMERIKSA THROTTLE VALVE: Periksa apakah throttle valve membuka dan menutup dengan lembut.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — SINGKIRKAN BENDA ASING DAN BERSIHKAN THROTTLE BODY ASSEMBLY
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: M+ (2) - M- (1)` : **0.3 sampai 100 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): M+ (C20-42) - M+ (C17-2)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): M- (C20-41) - M- (C17-1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): M+ (C20-42) atau M+ (C17-2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): M- (C20-41) or M- (C17-1) - Body ground` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 2 (M+) - 1 (M-) (20°C (68°F))` : **0.3 sampai 100 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): C17-2 (M+) - C23-42 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): C17-1 (M-) - C23-41 (M-) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2103` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM000000PFU01FX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Sirkuit Motor Kontrol Aktuator Throttle (Dokumen: RM000000PFU03ZX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit aktuator throttle Aktuator throttle ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit aktuator throttle Aktuator throttle Throttle valve Throttle body assembly ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit aktuator throttle Throttle body assembly ECM; [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Short dalam sirkuit aktuator throttle Throttle
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA THROTTLE BODY ASSEMBLY (TAHANAN AKTUATOR THROTTLE): Lepas hubungan konektor C17 throttle body. -> Ukur tahanan antara terminal aktuator throtle. -> Hubungkan kembali konektor throttle body.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (AKTUATOR THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA THROTTLE BODY ASSEMBLY: Periksa adanya benda asing antara katup throtle dan rumahnya.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PEMERIKSA THROTTLE VALVE: Periksa apakah throttle valve membuka dan menutup dengan lembut.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — SINGKIRKAN BENDA ASING DAN BERSIHKAN THROTTLE BODY ASSEMBLY
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: M+ (2) - M- (1)` : **0.3 sampai 100 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): M+ (C20-42) - M+ (C17-2)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): M- (C20-41) - M- (C17-1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): M+ (C20-42) atau M+ (C17-2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): M- (C20-41) or M- (C17-1) - Body ground` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: 2 (M+) - 1 (M-) (20°C (68°F))` : **0.3 sampai 100 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): C17-2 (M+) - C23-42 (M+) (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): C17-1 (M-) - C23-41 (M-) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2111` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sistem Kontrol Aktuator Throttle - Macet pada posisi Terbuka (Dokumen: RM000000PFV01GX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sistem Kontrol Aktuator Throttle - Macet pada posisi Terbuka (Dokumen: RM000000PFV03ZX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Aktuator throttle Throttle body assembly Throttle valve; Kondisi Deteksi: Aktuator throttle tidak menutup bila diberi sinyal oleh ECM (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Aktuator throttle Throttle body assembly Throttle valve ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTC LAIN (SEBAGAI TAMBAHAN KE DTC P2111 atau P2112): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BODY THROTTLE ASSEMBLY (PEMERIKSAAN VISUAL THROTTLE VALVE): Periksa kontaminasi antara throttle valve dan housing. Bila perlu, bersihkan throttle body assembly. Dan periksa bahwa throttle valve bergerak dengan lembut.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P2111 ATAU P2112): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin, tekan penuh dan bebaskan pedal akselerator dengan cepat (agar throttle valve membuka dan menut
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTC LAIN (SEBAGAI TAMBAHAN KE DTC P2111 atau P2112): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.

### DTC `P2112` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sistem Kontrol Aktuator Throttle - Macet pada posisi Tertutup (Dokumen: RM000000PFV01GX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Sistem Kontrol Aktuator Throttle - Macet pada posisi Tertutup (Dokumen: RM000000PFV03ZX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Aktuator throttle Throttle body assembly Throttle valve; Kondisi Deteksi: Aktuator throttle tidak menutup bila diberi sinyal oleh ECM (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Aktuator throttle Throttle body assembly Throttle valve ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTC LAIN (SEBAGAI TAMBAHAN KE DTC P2111 atau P2112): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BODY THROTTLE ASSEMBLY (PEMERIKSAAN VISUAL THROTTLE VALVE): Periksa kontaminasi antara throttle valve dan housing. Bila perlu, bersihkan throttle body assembly. Dan periksa bahwa throttle valve bergerak dengan lembut.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P2111 ATAU P2112): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin, tekan penuh dan bebaskan pedal akselerator dengan cepat (agar throttle valve membuka dan menut
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTC LAIN (SEBAGAI TAMBAHAN KE DTC P2111 atau P2112): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.

### DTC `P2118` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle Actuator Control Motor Current Range / Performance (Dokumen: RM000000PFW01HX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle Actuator Control Motor Current Range / Performance (Dokumen: RM000000PFW040X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Open dalam sirkuit power source ETCS Baterai Terminal baterai Fuse ETCS ECM; Kondisi Deteksi: Open dalam sirkuit power source ETCS (+BM) (1 trip detection logic); Kondisi Deteksi: Open dalam sirkuit power source (+BM) ETCS (Electronic Throttle Control System) (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (+B VOLTASE ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / +BM voltage. -> Baca nilai yang ditampilkan pada tester.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA FUSE (FUSE ETCS): Cabut fuse ETCS dari relay block ruang mesin . -> Periksa tahanan fuse ETCS. -> Pasang kembali fuse ETCS.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ECM - FUSE ETCS , BATERAI): Periksa harness dan konektor antara fuse ETCS dan ECM. -> Periksa harness dan konektor antara fuse ETCS dan kabel baterai positif.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (+ VOLTASE BM): Lepas hubungan konektor A21 dan C20 ECM . -> Ukur voltase antara terminal A21 dan C20 konektor ECM . -> Hubungkan kembali konektor ECM.
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA BATERAI: Periksa bahwa filter tidak tersumbat.
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERMINAL BATERAI: Periksa bahwa terminal baterai dan ECM tidak kendur atau berkarat.
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA DARI SHORT PADA SEMUA HARNESS DAN KONEKTOR YANG DIHUBUNGKAN KE FUSE DAN GANTI FUSE
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): Sekring ETCS (2) - +BM (A21-3)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): Sekring ETCS (2) atau +BM (A21-3) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): Kabel baterai positif -Fuse ETCS (1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): Kabel baterai positif atau fuse ETCS (1)- Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: +BM (A21-3) - ME01 (C20-43)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar: Fuse ETCS (Selalu)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: A20-3 (+BM) - C23-104 (E1) (Selalu)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): 2 (Fuse ETCS) - A20-3 (+BM) (Selalu)` : **Di bawah 1 Ω**

### DTC `P2119` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle Actuator Control Throttle Body Range / Performance (Dokumen: RM000000PFX01GX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle Actuator Control Throttle Body Range / Performance (Dokumen: RM000000PFX03ZX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ETCS ECM; Kondisi Deteksi: Sudut buka throtle valve berubah-ubah secara terus menerus dari sudut buka target (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: ETCS (Electronic Throttle Control System) ECM; Kondisi Deteksi: Sudut buka throttle valve terus berubah dengan cepat dari sudut buka target (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTC LAIN (SEBAGAI TAMBAHAN KE DTC P0420): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P2119)
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTC LAIN (SEBAGAI TAMBAHAN KE DTC P0420): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P2119): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG). -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Biarkan mesin idle selama 15 detik atau lebih. -> Tekan penuh dan bebaskan pedal pedal akselerator dengan cepa
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT

### DTC `P2120` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle / Pedal Position Sensor / Switch "D" Circuit (Dokumen: RM000000PFY01BX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle / Pedal Position Sensor / Switch "D" Circuit (Dokumen: RM000000PFY03SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP ECM; Kondisi Deteksi: VPA berfluktuasi dengan cepat di luar batas minimal malfungsi selama 0.5 detik atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP Open dalam sirkuit VCP1 Masa open atau short dalam sirkuit VPA ECM; Kondisi Deteksi: VPA 0.4 V atau kurang selama 0.5 detik atau lebih bila pedal akselerator ditekan (1 trip detection logic); [SISTEM 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor A20 Accelerator Pedal Position (APP) sensor. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor APP. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VCPA DAN VOLTASE VCP2): Lepas hubungan konektor A20 APP. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal-terminal konektor A20 sensor APP. -> Hubungkan kembali konektor sensor APP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (SENSOR POSISI PEDAL AKSELERATOR DTC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas (0.5 sampai 4.5 V)` : **1.2 sampai 5.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas` : **Perbedaan antara Accelerator Position No. 1 dan Accelerator Position No. 2 lebih besar dari 0.02 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA (A20-6) - VPA (A21-55)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA (A20-5) - EPA (A21-59)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCPA (A20-4) - VCPA (A21-57)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA2 (A20-3) - VPA2 (A21-56)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA2 (A20-2) - EPA2 (A21-60)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCP2 (A20-1) - VCP2 (A21-58)` : **Di bawah 1 Ω**

### DTC `P2121` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle / Pedal Position Sensor / Switch "D" Circuit Range / Performance (Dokumen: RM000000PFZ01DX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle / Pedal Position Sensor / Switch "D" Circuit Range / Performance (Dokumen: RM000000PFZ03XX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Accelerator Pedal Position (APP) sensor ECM; Kondisi Deteksi: Perbedaan voltase antara VPA dan VPA2 kurang dari 0.4 V, atau lebih dari 1.2 V selama 0.5 detik (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor posisi pedal akselerator (pedal akselerator assembly) ECM; Kondisi Deteksi: Perbedaan antara VPA dan VPA2 kurang dari 0.4 V, atau lebih dari 1.2 V selama 0.5 detik (1 tr
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA OUTPUT DTC LAIN (SEBAGAI TAMBAHAN KE DTC P02121: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC P2121): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — LANJUTKAN KE BAGAN DTC
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA TERHADAP PROBLEM INTERMITTENT
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Dibebaskan (0.5 sampai 1.1 V)` : **1.2 sampai 2.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Ditekan (2.6 sampai 4.5 V)` : **3.4 sampai 5.0 V**

### DTC `P2122` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY01BX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY03SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP ECM; Kondisi Deteksi: VPA berfluktuasi dengan cepat di luar batas minimal malfungsi selama 0.5 detik atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP Open dalam sirkuit VCP1 Masa open atau short dalam sirkuit VPA ECM; Kondisi Deteksi: VPA 0.4 V atau kurang selama 0.5 detik atau lebih bila pedal akselerator ditekan (1 trip detection logic); [SISTEM 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor A20 Accelerator Pedal Position (APP) sensor. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor APP. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VCPA DAN VOLTASE VCP2): Lepas hubungan konektor A20 APP. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal-terminal konektor A20 sensor APP. -> Hubungkan kembali konektor sensor APP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (SENSOR POSISI PEDAL AKSELERATOR DTC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas (0.5 sampai 4.5 V)` : **1.2 sampai 5.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas` : **Perbedaan antara Accelerator Position No. 1 dan Accelerator Position No. 2 lebih besar dari 0.02 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA (A20-6) - VPA (A21-55)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA (A20-5) - EPA (A21-59)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCPA (A20-4) - VCPA (A21-57)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA2 (A20-3) - VPA2 (A21-56)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA2 (A20-2) - EPA2 (A21-60)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCP2 (A20-1) - VCP2 (A21-58)` : **Di bawah 1 Ω**

### DTC `P2123` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY01BX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "D" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY03SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP ECM; Kondisi Deteksi: VPA berfluktuasi dengan cepat di luar batas minimal malfungsi selama 0.5 detik atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP Open dalam sirkuit VCP1 Masa open atau short dalam sirkuit VPA ECM; Kondisi Deteksi: VPA 0.4 V atau kurang selama 0.5 detik atau lebih bila pedal akselerator ditekan (1 trip detection logic); [SISTEM 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor A20 Accelerator Pedal Position (APP) sensor. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor APP. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VCPA DAN VOLTASE VCP2): Lepas hubungan konektor A20 APP. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal-terminal konektor A20 sensor APP. -> Hubungkan kembali konektor sensor APP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (SENSOR POSISI PEDAL AKSELERATOR DTC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas (0.5 sampai 4.5 V)` : **1.2 sampai 5.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas` : **Perbedaan antara Accelerator Position No. 1 dan Accelerator Position No. 2 lebih besar dari 0.02 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA (A20-6) - VPA (A21-55)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA (A20-5) - EPA (A21-59)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCPA (A20-4) - VCPA (A21-57)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA2 (A20-3) - VPA2 (A21-56)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA2 (A20-2) - EPA2 (A21-60)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCP2 (A20-1) - VCP2 (A21-58)` : **Di bawah 1 Ω**

### DTC `P2125` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle / Sensor Pedal Posisi / Switch Sirkuit"B" (Dokumen: RM000000PFY01BX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Throttle / Sensor Pedal Posisi / Switch Sirkuit"B" (Dokumen: RM000000PFY03SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP ECM; Kondisi Deteksi: VPA berfluktuasi dengan cepat di luar batas minimal malfungsi selama 0.5 detik atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP Open dalam sirkuit VCP1 Masa open atau short dalam sirkuit VPA ECM; Kondisi Deteksi: VPA 0.4 V atau kurang selama 0.5 detik atau lebih bila pedal akselerator ditekan (1 trip detection logic); [SISTEM 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor A20 Accelerator Pedal Position (APP) sensor. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor APP. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VCPA DAN VOLTASE VCP2): Lepas hubungan konektor A20 APP. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal-terminal konektor A20 sensor APP. -> Hubungkan kembali konektor sensor APP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (SENSOR POSISI PEDAL AKSELERATOR DTC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas (0.5 sampai 4.5 V)` : **1.2 sampai 5.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas` : **Perbedaan antara Accelerator Position No. 1 dan Accelerator Position No. 2 lebih besar dari 0.02 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA (A20-6) - VPA (A21-55)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA (A20-5) - EPA (A21-59)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCPA (A20-4) - VCPA (A21-57)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA2 (A20-3) - VPA2 (A21-56)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA2 (A20-2) - EPA2 (A21-60)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCP2 (A20-1) - VCP2 (A21-58)` : **Di bawah 1 Ω**

### DTC `P2127` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY01BX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Low Input Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY03SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP ECM; Kondisi Deteksi: VPA berfluktuasi dengan cepat di luar batas minimal malfungsi selama 0.5 detik atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP Open dalam sirkuit VCP1 Masa open atau short dalam sirkuit VPA ECM; Kondisi Deteksi: VPA 0.4 V atau kurang selama 0.5 detik atau lebih bila pedal akselerator ditekan (1 trip detection logic); [SISTEM 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor A20 Accelerator Pedal Position (APP) sensor. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor APP. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VCPA DAN VOLTASE VCP2): Lepas hubungan konektor A20 APP. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal-terminal konektor A20 sensor APP. -> Hubungkan kembali konektor sensor APP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (SENSOR POSISI PEDAL AKSELERATOR DTC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas (0.5 sampai 4.5 V)` : **1.2 sampai 5.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas` : **Perbedaan antara Accelerator Position No. 1 dan Accelerator Position No. 2 lebih besar dari 0.02 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA (A20-6) - VPA (A21-55)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA (A20-5) - EPA (A21-59)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCPA (A20-4) - VCPA (A21-57)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA2 (A20-3) - VPA2 (A21-56)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA2 (A20-2) - EPA2 (A21-60)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCP2 (A20-1) - VCP2 (A21-58)` : **Di bawah 1 Ω**

### DTC `P2128` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY01BX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] High Input Sirkuit "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY03SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP ECM; Kondisi Deteksi: VPA berfluktuasi dengan cepat di luar batas minimal malfungsi selama 0.5 detik atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP Open dalam sirkuit VCP1 Masa open atau short dalam sirkuit VPA ECM; Kondisi Deteksi: VPA 0.4 V atau kurang selama 0.5 detik atau lebih bila pedal akselerator ditekan (1 trip detection logic); [SISTEM 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor A20 Accelerator Pedal Position (APP) sensor. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor APP. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VCPA DAN VOLTASE VCP2): Lepas hubungan konektor A20 APP. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal-terminal konektor A20 sensor APP. -> Hubungkan kembali konektor sensor APP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (SENSOR POSISI PEDAL AKSELERATOR DTC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas (0.5 sampai 4.5 V)` : **1.2 sampai 5.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas` : **Perbedaan antara Accelerator Position No. 1 dan Accelerator Position No. 2 lebih besar dari 0.02 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA (A20-6) - VPA (A21-55)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA (A20-5) - EPA (A21-59)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCPA (A20-4) - VCPA (A21-57)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA2 (A20-3) - VPA2 (A21-56)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA2 (A20-2) - EPA2 (A21-60)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCP2 (A20-1) - VCP2 (A21-58)` : **Di bawah 1 Ω**

### DTC `P2135` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Korelasi Voltase "A" / "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF600XX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Korelasi Voltase "A" / "B" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PF6031X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor Posisi Throttle (TP) (dibuat menyatu dalam throttle body assembly) ECM; Kondisi Deteksi: Voltase output VTA1 berfluktuasi secara cepat diluar titik rendah dan titik tinggi batas minimal malfungsi selama 2 detik saat pedal akselerator ditekan. (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor TP (dibuat menyatu dalam throttle body assembly) Sirkuit TP sensor ECM; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (THROTTLE POSITION No 1 dan THROTTLE POSITION No.2 ): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine and ECT / Data List / Throttle Position No. 1 and Throttle Position No. 2. -> Baca nilai yan
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR POSISI THROTTLE - ECM): Lepas hubungan konektor C17 throttle body. -> Lepas hubungan konektor C20 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor throttle body. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VOLTASE VC): Lepas hubungan konektor C17 throttle body. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal konektor bodi throtle . -> Hubungkan kembali konektor throttle body.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI THROTTLE BODY ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (DTC SENSOR POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik atau lebih. -> Pilih item menu berikut ini: Powertrain /
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VC (C17-5) - VCTA (C20-67)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA (C17-6) - VTA1 (C20-115)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VTA2 (C17-4) - VTA2 (C20-114)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): E2 (C17-3) - ETA (C20-91)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VC (C17-5) atau VCTA (C20-67) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA (C17-6) atau VTA1 (C20-115) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari short): VTA2 (C17-4) atau VTA2 (C20-114) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: VC (C17-5) - E2 (C17-3)` : **4.5 sampai 5.5 V**

### DTC `P2138` — [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Korelasi Voltase "D" / "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY01BX) | [SISTEM KONTROL MESIN 1NZ-FE — SISTEM SFI] Korelasi Voltase "D" / "E" Sensor / Switch Posisi Throttle / Pedal (Dokumen: RM000000PFY03SX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP ECM; Kondisi Deteksi: VPA berfluktuasi dengan cepat di luar batas minimal malfungsi selama 0.5 detik atau lebih (1 trip detection logic); [SISTEM KONTROL MESIN 1NZ-FE] Area Gangguan: Sensor APP Open dalam sirkuit VCP1 Masa open atau short dalam sirkuit VPA ECM; Kondisi Deteksi: VPA 0.4 V atau kurang selama 0.5 detik atau lebih bila pedal akselerator ditekan (1 trip detection logic); [SISTEM 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 1NZ-FE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI AKSELERATOR NO. 1 DAN POSISI AKSELERATOR NO. 2): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine dan ECT / Data List / Accelerator Position No. 1 dan Accelerator Position No. 2. -> Baca nil
  - Langkah 2 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA HARNESS DAN KONEKTOR (ACCELERATOR PEDAL POSITION SENSOR - ECM): Lepas hubungan konektor A20 Accelerator Pedal Position (APP) sensor. -> Lepas hubungan konektor A21 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor sensor APP. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA ECM (VCPA DAN VOLTASE VCP2): Lepas hubungan konektor A20 APP. -> Putar switch pengapian ke on (IG). -> Ukur voltase antara terminal-terminal konektor A20 sensor APP. -> Hubungkan kembali konektor sensor APP.
  - Langkah 4 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI PEDAL AKSELERATOR ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 1NZ-FE) — PERIKSA APAKAH DTC DI-OUTPUT LAGI ATAU TIDAK (SENSOR POSISI PEDAL AKSELERATOR DTC): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke on (IG) dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Hidupkan mesin. -> Biarkan mesin idle selama 15 detik. -> Pilih item menu berikut ini: Powertrain / Engine dan
  - Langkah 6 (SISTEM KONTROL MESIN 1NZ-FE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 1NZ-FE) — GANTI ECM
  - Langkah 8 (SISTEM KONTROL MESIN 1NZ-FE) — SISTEM OK
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas (0.5 sampai 4.5 V)` : **1.2 sampai 5.0 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Voltase standar: Bebas → Ditekan → Bebas` : **Perbedaan antara Accelerator Position No. 1 dan Accelerator Position No. 2 lebih besar dari 0.02 V**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA (A20-6) - VPA (A21-55)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA (A20-5) - EPA (A21-59)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCPA (A20-4) - VCPA (A21-57)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VPA2 (A20-3) - VPA2 (A21-56)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): EPA2 (A20-2) - EPA2 (A21-60)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 1NZ-FE] Tahanan standar (Periksa dari open): VCP2 (A20-1) - VCP2 (A21-58)` : **Di bawah 1 Ω**

### DTC `P2716` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Kelistrikan Pressure Control Solenoid "D" (Shift Solenoid Valve SLT) (Dokumen: RM0000015W100JX) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Kelistrikan Pressure Control Solenoid "D" (Shift Solenoid Valve SLT) (Dokumen: RM0000015W101TX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SLT Shift solenoid valve SLT ECM; Kondisi Deteksi: Open atau short telah dideteksi dalam sirkuit shift solenoid valve SLT selama 1 detik atau lebih selama pengendaraan. (1-trip detecting logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SLT): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE SLT: Lepas shift solenoid valve SLT. -> Ukur tahanan. -> Hubungkan kabel utama positif (+) dengan bola lampu 21 W ke terminal 2 dan kabel utama negatif (-) ke terminal 1 konektor solenoid valve, kemudian periksa gerakan valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE SLT
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SLT): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 3 (SLT+) - 8 (SLT-)` : **5.0 Ω sampai 5.6 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 3 (SLT+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 8 (SLT-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 76 (SLT+) - 75 (SLT-)` : **5.0 Ω sampai 5.6 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 76 (SLT+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 75 (SLT-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 1 - 2` : **5.0 Ω sampai 5.6 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 3 (SLT+) - 8 (SLT-) (20°C (68°F))` : **5.0 sampai 5.6 Ω**

### DTC `P2769` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Short dalam Sirkuit Torque Converter Clutch Solenoid (Shift Solenoid Valve SL) (Dokumen: RM000001IMZ004X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Short dalam Sirkuit Torque Converter Clutch Solenoid (Shift Solenoid Valve SL) (Dokumen: RM000001IMZ00
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short sirkuit dalam shift solenoid valve SL Shift solenoid valve SL ECM; Kondisi Deteksi: ECM mendeteksi short pada sirkuit solenoid valve SL ketika solenoid valve SL bekerja. (Tahanan solenoid: 8 Ω atau kurang) (2-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open sirkuit dalam shift solenoid valve SL Shift solenoid valve SL ECM; Kondisi Deteksi: ECM mendeteksi open pada sirkuit soleno
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE SL: Lepas shift solenoid valve SL. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE SL
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 4 (SL) - Masa bodi` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 57 (SL) - Masa bodi` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (SL) - Bodi Solenoid (SL)` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 4 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 57 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (SL) - Bodi Solenoid (SL) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `P2770` — [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Open dalam Sirkuit Torque Converter Clutch Solenoid (Shift Solenoid Valve SL) (Dokumen: RM000001IMZ004X) | [TRANSAXLE OTOMATIS U340E — SISTEM TRANSAXLE OTOMATIS] Open dalam Sirkuit Torque Converter Clutch Solenoid (Shift Solenoid Valve SL) (Dokumen: RM000001IMZ007X
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSAXLE OTOMATIS U340E] Area Gangguan: Short sirkuit dalam shift solenoid valve SL Shift solenoid valve SL ECM; Kondisi Deteksi: ECM mendeteksi short pada sirkuit solenoid valve SL ketika solenoid valve SL bekerja. (Tahanan solenoid: 8 Ω atau kurang) (2-trip detection logic); [TRANSAXLE OTOMATIS U340E] Area Gangguan: Open sirkuit dalam shift solenoid valve SL Shift solenoid valve SL ECM; Kondisi Deteksi: ECM mendeteksi open pada sirkuit soleno
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan.
  - Langkah 2 (TRANSAXLE OTOMATIS U340E) — PERIKSA HARNESS DAN KONEKTOR (KABEL TRANSMISI - ECM): Hubungkan konektor transmisi ke transaxle. -> Lepas hubungan konektor ECM. -> Ukur tahanan.
  - Langkah 3 (TRANSAXLE OTOMATIS U340E) — PERIKSA SHIFT SOLENOID VALVE SL: Lepas shift solenoid valve SL. -> Ukur tahanan. -> Hubungkan baterai positif (+) ke terminal konektor solenoid, dan baterai negatif (-) ke bodi solenoid untuk memeriksa kerja solenoid valve.
  - Langkah 4 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI KABEL TRANSMISI
  - Langkah 5 (TRANSAXLE OTOMATIS U340E) — GANTI ECM
  - Langkah 6 (TRANSAXLE OTOMATIS U340E) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSAXLE OTOMATIS U340E) — GANTI SHIFT SOLENOID VALVE SL
  - Langkah 1 (TRANSAXLE OTOMATIS U340E) — PERIKSA KABEL TRANSMISI (SHIFT SOLENOID VALVE SL): Lepas hubungan konektor kabel transmisi dari transaxle. -> Ukur tahanan sesuaikan dengan nilai dalam tabel di bawah ini.
- **Spesifikasi Standar Multimeter**:
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 4 (SL) - Masa bodi` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 57 (SL) - Masa bodi` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (SL) - Bodi Solenoid (SL)` : **11 sampai 15 Ω pada 20°C (68°F)**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 4 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: 57 (SL) - Masa bodi (20°C (68°F))` : **11 sampai 15 Ω**
  - `[TRANSAXLE OTOMATIS U340E] Tahanan standar: Konektor Solenoid (SL) - Bodi Solenoid (SL) (20°C (68°F))` : **11 sampai 15 Ω**

### DTC `U0073` — [KONTROL REM — ANTI-LOCK BRAKE SYSTEM] Control Module Communication Bus OFF (Dokumen: RM0000024PB01YX) | [KONTROL REM — ANTI-LOCK BRAKE SYSTEM / Flash Code 94] Control Module Communication Bus OFF (Dokumen: RM000001EFD007X) | [POWER STEERING — SISTEM POWER STEERING ELEKRONIK] Control Module Communication Bus OFF (Dokum
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [KONTROL REM] Area Gangguan: Sistem komunikasi CAN; [POWER STEERING] Area Gangguan: Sistem komunikasi CAN; Kondisi Deteksi: Error komunikasi CAN (bus CAN off); [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECM; Kondisi Deteksi: Error komunikasi ECM; [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECU skid control
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (KONTROL REM) — Periksa soket, kabel harness, dan komponen Control Module Communication Bus OFF sesuai dokumen Toyota GSIC RM0000024PB01YX.
  - Langkah 1 (KONTROL REM) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Periksa apakah DTC yang sama di-output (Lihat halaman ).
  - Langkah 2 (KONTROL REM) — PERBAIKI SISTEM KOMUNIKASI CAN
  - Langkah 3 (KONTROL REM) — SELESAI
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 3 (POWER STEERING) — LANJUTKAN KE SISTEM KOMUNIKASI CAN
  - Langkah 2 (KONTROL REM) — PERIKSA SISTEM KOMUNIKASI CAN

### DTC `U0100` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK] Kehilangan Komunikasi dengan ECM/PCM "A" (Dokumen: RM000001ALB003X) | [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 92] Kehilangan Komunikasi dengan ECM/PCM "A" (Dokumen: RM000001ALB00OX) | [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sistem komunikasi CAN; Kondisi Deteksi: Error komunikasi CAN (bus CAN off); [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECM; Kondisi Deteksi: Error komunikasi ECM; [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECU skid control; Kondisi Deteksi: Kesalahan komunikasi ECU skid control
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 3 (POWER STEERING) — LANJUTKAN KE SISTEM KOMUNIKASI CAN
  - Langkah 1 (METER) — MENGKONFIRMASI OUTPUT DTC: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-on (IG) (jangan men-start mesin) kemudian putar intellligent tester ke-ON. -> Hapus DTC yang disimpan dengan memilih item menu berikut pada tester: Body / Combination Meter 
  - Langkah 2 (METER) — SISTEM OK
  - Langkah 3 (METER) — LANJUTKAN KE SISTEM KOMUNIKASI CAN
  - Langkah 1 (POWER STEERING) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Periksa dari DTC.
  - Langkah 2 (METER) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA

### DTC `U0105` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK] Kehilangan Komunikasi dengan ECM (Dokumen: RM000001ALB003X)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sistem komunikasi CAN; Kondisi Deteksi: Error komunikasi CAN (bus CAN off); [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECM; Kondisi Deteksi: Error komunikasi ECM; [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECU skid control; Kondisi Deteksi: Kesalahan komunikasi ECU skid control
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 3 (POWER STEERING) — LANJUTKAN KE SISTEM KOMUNIKASI CAN

### DTC `U0121` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK] Kehilangan Komunikasi dengan Modul Kontrol Anti-lock Brake System (ABS) (Dokumen: RM000001ALB003X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sistem komunikasi CAN; Kondisi Deteksi: Error komunikasi CAN (bus CAN off); [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECM; Kondisi Deteksi: Error komunikasi ECM; [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECU skid control; Kondisi Deteksi: Kesalahan komunikasi ECU skid control
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 3 (POWER STEERING) — LANJUTKAN KE SISTEM KOMUNIKASI CAN

### DTC `U0129` — [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 93] Kehilangan Komunikasi dengan Control Module Sistem Rem (Dokumen: RM000001ALB00OX) | [POWER STEERING — SISTEM POWER STEERING ELEKRONIK / Flash Code 93] Kehilangan Komunikasi dengan Control Module Sistem Rem (Dokumen: RM000001ALB00TX) | [METER — SISTEM ME
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECM; Kondisi Deteksi: Error komunikasi ECM; [POWER STEERING] Area Gangguan: Sistem komunikasi CAN Aktuator rem assembly (ECU Skid control); Kondisi Deteksi: Kesalahan komunikasi ECU skid control; [METER] Area Gangguan: Sistem komunikasi CAN Aktuator rem; [POWER STEERING] Area Gangguan: Sistem komunikasi CAN ECU skid control
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (POWER STEERING) — KONFIRMASI DTC: Hapus DTC (Lihat halaman ). -> Periksa DTC (Lihat halaman ).
  - Langkah 2 (POWER STEERING) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 3 (POWER STEERING) — LANJUTKAN KE SISTEM KOMUNIKASI CAN
  - Langkah 1 (METER) — MENGKONFIRMASI OUTPUT DTC: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-on (IG) (jangan menghidupkan mesin) dan hidupkan tester. -> Hapus DTC yang disimpan dengan memilih item menu berikut pada tester: Body / Combination Meter / DTC / Clear. -> 
  - Langkah 2 (METER) — SISTEM OK
  - Langkah 3 (METER) — LANJUTKAN KE SISTEM KOMUNIKASI CAN
  - Langkah 1 (POWER STEERING) — KONFIRMASI ULANG DTC: Hapus DTC (Lihat halaman ). -> Periksa dari DTC.
  - Langkah 2 (METER) — GUNAKAN METODE SIMULASI UNTUK MEMERIKSA
