# Buku Pedoman Reparasi Resmi Toyota Avanza, Rush & Daihatsu Xenia (RM02X1ED_ID · Mesin K3-VE 1.3L, 3SZ-VE 1.5L, EJ-VE 1.0L & A/T A4Q)

- **Pack ID AGOS**: `toyota_avanza_xenia_2004_2015`
- **Merek & Model**: Toyota Avanza (Toyota Avanza / Rush & Daihatsu Xenia / Terios (K3-VE 1.3L · 3SZ-VE 1.5L · EJ-VE 1.0L))
- **Rentang Tahun**: 2004–2015
- **Kode Mesin Tercakup**: `K3-VE, 3SZ-VE, EJ-VE`
- **Total Kode DTC Terindeks**: **73 Kode DTC**
- **Total Pinout Terminal ECM/ECU**: **274 Terminal**
- **Total Spesifikasi Sensor & Data List**: **211 Parameter**

---

## 1. Ringkasan Bab & Sistem (`toc_rpr.xml`)

| Kategori Servis | Nama Sistem / Mesin | Jumlah Sub-Bab Prosedur |
| :--- | :--- | :---: |
| PENDAHULUAN | PENDAHULUAN | 9 |
| PENDAHULUAN | KATA PENGANTAR / PERINGATAN / TOC BAB | 2 |
| PENDAHULUAN | TOC2 | 2 |
| PERSIAPAN | PERSIAPAN | 117 |
| SPESIFIKASI SERVIS | SPESIFIKASI SERVIS | 84 |
| MESIN | SISTEM KONTROL MESIN 3SZ-VE | 77 |
| MESIN | SISTEM KONTROL MESIN EJ-VE | 75 |
| MESIN | SISTEM KONTROL MESIN K3-VE | 56 |
| MESIN | MEKANISME MESIN 3SZ-VE | 19 |
| MESIN | MEKANISME MESIN EJ-VE | 29 |
| MESIN | MEKANISME MESIN K3-VE | 3 |
| MESIN | BAHAN BAKAR 3SZ-VE | 17 |
| MESIN | BAHAN BAKAR EJ-VE | 17 |
| MESIN | BAHAN BAKAR K3-VE | 9 |
| MESIN | KONTROL EMISI 3SZ-VE | 17 |
| MESIN | KONTROL EMISI EJ-VE | 16 |
| MESIN | KONTROL EMISI K3-VE | 3 |
| MESIN | EXHAUST 3SZ-VE | 3 |
| MESIN | EXHAUST EJ-VE | 3 |
| MESIN | EXHAUST K3-VE | 3 |
| MESIN | PENDINGIN 3SZ-VE | 19 |
| MESIN | PENDINGINAN EJ-VE | 20 |
| MESIN | PENDINGIN K3-VE | 1 |
| MESIN | PELUMASAN 3SZ-VE | 9 |
| MESIN | PELUMASAN EJ-VE | 9 |
| MESIN | PELUMASAN K3-VE | 3 |
| MESIN | PENGAPIAN 3SZ-VE | 6 |
| MESIN | PENGAPIAN EJ-VE | 6 |
| MESIN | PENGAPIAN K3-VE IGNITION | 1 |
| MESIN | STARTING 3SZ-VE | 12 |
| MESIN | STARTING EJ-VE | 12 |
| MESIN | PENGISIAN 3SZ-VE | 10 |
| MESIN | PENGISIAN EJ-VE | 10 |
| MESIN | PENGISIAN K3-VE | 6 |
| TRANSMISI | TRANSMISI OTOMATIS A4Q | 36 |
| TRANSMISI | KOPLING | 19 |
| TRANSMISI | TRANSMISI MANUAL M5S | 7 |
| DRIVE LINE | DIFFERENSIAL | 12 |
| SUSPENSI & AXLE | SUSPENSI | 4 |
| SUSPENSI & AXLE | BAN DAN RODA | 1 |
| REM | KONTROL REM | 4 |
| REM | REM | 14 |
| KEMUDI | STEERING COLUMN | 9 |
| KEMUDI | POWER STEERING | 18 |
| SISTEM HEATER & AIR CONDITIONING | AIR CONDITIONING | 42 |
| RESTRAINT | SUPPLEMENTAL RESTRAINT SYSTEM | 49 |
| RESTRAINT | SEAT BELT | 11 |
| KEAMANAN | ENGINE IMMOBILISER | 18 |
| KELISTRIKAN BODI | LAMPU | 11 |
| KELISTRIKAN BODI | WIPER DAN WASHER | 2 |
| KELISTRIKAN BODI | DOOR LOCK | 7 |
| KELISTRIKAN BODI | METER | 9 |
| KELISTRIKAN BODI | AUDIO / VISUAL | 25 |
| KELISTRIKAN BODI | SISTEM LAINNYA | 4 |
| BODI | KACA DEPAN / KACA JENDELA | 9 |
| BODI | PANEL INSTRUMEN | 4 |
| BODI | TEMPAT DUDUK | 10 |
| BODI | EKSTERIOR | 35 |

---

## 2. Tabel Pinout & Tegangan Standar Terminal ECM / ECU

| Terminal (Simbol & Pin) | Warna Kabel & Deskripsi | Kondisi & Standar Tegangan / Tahanan |
| :--- | :--- | :--- |
| `[3SZ-VE] BAT (E10-7) - E1 (E8-29)` | Warna Kabel: B - BR-W — Baterai (untuk mengukur voltase baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[3SZ-VE] +B1 (E8-7) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sumber daya ECM | Switch pengapian ON: 11 sampai 14 V |
| `[3SZ-VE] VCPM (E8-22) - E2PM (E8-12)` | Warna Kabel: G-R - W-B — Sumber daya sensor tekanan absolut manifold | Switch pengapian ON: 4,5 sampai 5,5 V |
| `[3SZ-VE] PIM (E8-23) - E2PM (E8-12)` | Warna Kabel: R-W - W-B — Sensor tekanan absolut manifold | Sensor pembebasan udara: 3,1 sampai 4,1 V / Idle: 1,2 sampai 2,0 V |
| `[3SZ-VE] VC (E8-10) - E2 (E8-30)` | Warna Kabel: L-R - BR — Sumber daya sensor posisi throttle | Switch pengapian ON: 4,5 sampai 5,5 V |
| `[3SZ-VE] VTH (E8-20) - E2 (E8-30)` | Warna Kabel: O - BR — Sensor posisi throttle (untuk kontrol mesin) | Switch pengapian ON, pedal aselerator dibebaskan: 0,4 sampai 0,9 V / Switch pengapian ON, pedal aselerator ditekan: 3,2 sampai 5,0 V |
| `[3SZ-VE] THA (E8-13) - E2 (E8-30)` | Warna Kabel: G-W - BR — Sensor temperatur udara intake | Idling, temperatur udara masuk 20°C (20,00°C): 0,5 sampai 3,4 V / Idling, temperatur udara masuk 60°C (140°F): 0,2 sampai 1,0 V |
| `[3SZ-VE] THW (E8-19) - E2 (E8-30)` | Warna Kabel: B-W - BR — Sensor temperatur cairan pendingin mesin | Setelah pemanasan mesin, temperatur cairan pendingin mesin 60°C sampai 120°C (140°F sampai 248°F): 0,3 sampai 1,3 V |
| `[3SZ-VE] KNK (E8-31) - E1 (E8-29)` | Warna Kabel: L - BR-W — Sensor knock | Putaran mesin dipertahankan pada 4.000 rpm setelah mesin dipanaskan: Terbangkit pulsa (Lihat halaman ) |
| `[3SZ-VE] SPD (E10-18) - E1 (E8-29)` | Warna Kabel: LG-R - BR-W — Sinyal kecepatan dari meter kombinasi | Switch pengapian on, Roda penggerak diputar: Terbangkit pulsa (Lihat halaman ) |
| `[3SZ-VE] STA (E9-15) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sinyal starter | Mengengkol: 6 V atau lebih / Idle: Di bawah 0,5 V |
| `[3SZ-VE] Antara N1+ (E8-11) dan N1- (E8-21)` | Warna Kabel: W - B — Sensor posisi crankshaft | Idle: Terbangkit pulsa (Lihat halaman ) |
| `[3SZ-VE] N2+ (E8-18) - N2- (E8-28)` | Warna Kabel: G - R — Sensor Posisi Camshaft | Idle: Terbangkit pulsa (Lihat halaman ) |
| `[3SZ-VE] OCV+ (E9-7) - OCV- (E9-6)` | Warna Kabel: G-B - LG — Camshaft Timing Oil Control Valve (OCV) | Idle: Terbangkit pulsa (Lihat model gelombang 1) |
| `[3SZ-VE] VTH (E8-2) - E2 (E8-30)` | Warna Kabel: GR - BR — Sensor heated oxygen (Sensor 1) | Putaran mesin dipertahankan pada 2.500 rpm selama 2 menit setelah mesin dipanaskan: Terbangkit pulsa (Lihat model gelombang 2) |
| `[3SZ-VE] VTH (E8-1) - E2 (E8-30)` | Warna Kabel: W - BR — Sensor oksigen (Sensor 2) | Putaran mesin dipertahankan pada 2.500 rpm selama 2 menit setelah mesin dipanaskan: Terbangkit pulsa (Lihat model gelombang 3) |
| `[3SZ-VE] OXH1 (E8-8) - E2 (E8-30)` | Warna Kabel: L-Y - BR — Pemanas sensor heated oxygen (Sensor 1) | Idle: Di bawah 3,0 V / Switch pengapian ON: 8 sampai 14 V |
| `[3SZ-VE] #10 (E8-6) - E01 (E8-3)` | Warna Kabel: W-G - BR — Injector | Switch pengapian ON: 11 sampai 14 V |
| `[3SZ-VE] #20 (E8-5) - E01 (E8-3)` | Warna Kabel: W-L - BR — Injector | Switch pengapian ON: 11 sampai 14 V |
| `[3SZ-VE] #30 (E8-4) - E01 (E8-3)` | Warna Kabel: W-R - BR — Injector | Idle: Terbangkit pulsa (Lihat model gelombang 4) |
| `[3SZ-VE] #40 (E9-5) - E01 (E8-3)` | Warna Kabel: W - BR — Injector | Idle: Terbangkit pulsa (Lihat model gelombang 4) |
| `[3SZ-VE] IG1 (E8-17) - E1 (E8-29)` | Warna Kabel: L-B - BR-W — Koil pengapian (Sinyal pengapian) | Switch pengapian ON: Di bawah 0,5 V |
| `[3SZ-VE] IG2 (E8-27) - E1 (E8-29)` | Warna Kabel: LG-B - BR-W — Koil pengapian (Sinyal pengapian) | Switch pengapian ON: Di bawah 0,5 V |
| `[3SZ-VE] IG3 (E8-34) - E1 (E8-29)` | Warna Kabel: W-G - BR-W — Koil pengapian (Sinyal pengapian) | Idle: Terbangkit pulsa (Lihat halaman ) |
| `[3SZ-VE] IG4 (E8-16) - E1 (E8-29)` | Warna Kabel: W-R - BR-W — Koil pengapian (Sinyal pengapian) | Idle: Terbangkit pulsa (Lihat halaman ) |
| `[3SZ-VE] PRG (E8-9) - E01 (E8-3)` | Warna Kabel: P-L - BR — Vacuum switching valve (EVAP) | Switch pengapian ON: 11 sampai 14 V / Idle: Terbangkit pulsa (Lihat model gelombang 5) |
| `[3SZ-VE] IACAHI (E8-15) - IACALO (E8-14)` | Warna Kabel: G-O - G-B — Katup kontrol putaran idle | Idle: Terbangkit pulsa (0 sampai 12 V) |
| `[3SZ-VE] IACBHI (E8-25) - IACBLO (E8-24)` | Warna Kabel: R-B - R-L — Katup kontrol putaran idle | Idle: Terbangkit pulsa (0 sampai 12 V) |
| `[3SZ-VE] DEF (E10-4) - E1 (E8-29)` | Warna Kabel: W-G - BR-W — Switch defogger | Switch defogger OFF: 0 sampai 1,5 V / Switch defogger ON: 7,5 sampai 14 V |
| `[3SZ-VE] PST (E8-32) - E1 (E8-29)` | Warna Kabel: L-W - BR-W — Switch tekanan oli power steering | Switch tekanan oli ON: Di bawah 0,5 V / Switch tekanan oli OFF: 11 sampai 14 V |
| `[3SZ-VE] Tanpa sensor oksigen belakang (sensor 2), tanpa sistem engine immobiliser: FC1 (E` | Warna Kabel: B-W - BR — Pompa bahan bakar | Switch pengapian ON (Mesin tidak hidup): 11 sampai 14 V / Idle: Di bawah 2,0 V |
| `[3SZ-VE] VF (E10-17) - E1 (E8-29)` | Warna Kabel: LG-B - BR-W — Air-fuel ratio learned control value output | Mesin idling, terminal EFIT open: Tetap 5 V: Jumlah bertambah Pembangkitan pulsa 0 sampai 5 V: Normal Tetap 0 V: Jumlah berkurang / Putaran mesin 1.200 rpm atau lebih, terminal EFIT short: 5 V: Gemuk 0 V: Kurus / Putaran |
| `[3SZ-VE] ACEV (E10-14) - E21 (E10-31)` | Warna Kabel: BR-W - BR-Y — Cooler thermistor No.1 (Sensor temperatur evaporator A/C) | Air conditioner ON: 0,15 sampai 4,8 V |
| `[3SZ-VE] ACSW (E9-24) - E1 (E8-29)` | Warna Kabel: L-O - BR-W — Tanpa heater: Switch tekanan A/C | Switch pengapian ON: 11 sampai 14 V / Mesin idling Switch blower ON dan switch kontrol cooler ON: 11 sampai 14 V |
| `[3SZ-VE] ACVR (E10-30) - E21 (E10-31)` | Warna Kabel: B-O - BR-Y — Switch kontrol temperatur A/C (Switch kontrol heater) | Switch pengapian ON: Variasi dengan volume |
| `[3SZ-VE] MGC (E9-25) - E01 (E8-3)` | Warna Kabel: G-W - BR — Magnet clutch A/C | Magnetic clutch A/C ON: Di bawah 1,0 V / Magnetic clutch A/C OFF: 11 sampai 14 V |
| `[3SZ-VE] H/L (E10-10) - E1 (E8-29)` | Warna Kabel: R-L - BR-W — Switch lampu tail | Lampu tail ON: 11 sampai 14 V / Lampu tail OFF: Di bawah 0,5 V |
| `[3SZ-VE] BLW (E10-11) - E1 (E8-29)` | Warna Kabel: L-R - BR-W — Motor blower | Switch blower ON: Di bawah 0,5 V / Switch blower OFF: 11 sampai 14 V |
| `[3SZ-VE] FAN1 (E9-14) - E01 (E8-3)` | Warna Kabel: R-W - BR — Fan radiator | Fan radiator ON: Di bawah 1,0 V / Fan radiator OFF: 11 sampai 14 V |
| `[3SZ-VE] W (E10-6) - E01 (E8-3)` | Warna Kabel: V-W - BR — Lampu Indikator Malfungsi (MIL) | MIL menyala: Di bawah 1,0 V / MIL padam: 11 sampai 14 V |
| `[3SZ-VE] EFIT (E10-28) - E1 (E8-29)` | Warna Kabel: LG - BR-W — Terminal EFIT dari DLC3 | Switch pengapian ON: 11 sampai 14 V |
| `[3SZ-VE] REV (E10-24) - E1 (E8-29)` | Warna Kabel: R-B *1 - BR-W R-G *2 - BR-W — Sinyal putaran mesin | Idle: Terbangkit pulsa (Lihat model gelombang 6) |
| `[3SZ-VE] FPOF (E10-13) - E1 (E8-29)` | Warna Kabel: L - BR-W — Sensor airbag tengah assembly | Idle dengan mesin dalam kondisi panas: Terbangkit pulsa (Lihat model gelombang 7) |
| `[3SZ-VE] ATTX *1 (E9-2) - E1 (E8-29)` | Warna Kabel: R - BR-W — Komunikasi serial A/T | Switch pengapian ON: Terbangkit pulsa (0 sampai 12 V) |
| `[3SZ-VE] ATRX *1 (E9-1) - E1 (E8-29)` | Warna Kabel: G - BR-W — Komunikasi serial A/T | Switch pengapian ON: Terbangkit pulsa (0 sampai 12 V) |
| `[3SZ-VE] ATNE *1 (E9-3) - E1 (E8-29)` | Warna Kabel: L-W - BR-W — Komunikasi serial A/T | Idle: Terbangkit pulsa (0 sampai 12 V) |
| `[3SZ-VE] A/T *1 (E10-9 atau E10-20) - E1 (E8-29)` | Warna Kabel: W-L or W-R - BR-W — Relay starter | Switch pengapian ke ST Posisi shift lever kecuali P dan N: 8 sampai 14 V / Switch pengapian ke ST Posisi shift lever P dan N: Di bawah 3 V |
| `[3SZ-VE] STP (E10-12) - E1 (E8-29)` | Warna Kabel: G-Y - BR-W — Switch lampu rem | Pedal rem ditekan: 11 sampai 14 V / Pedal Rem Dibebaskan: Di bawah 1,5 V |
| `[3SZ-VE] SIO1 (E10-27) - E1 (E8-29)` | Warna Kabel: P - BR-W — Komunikasi tester diagnostik | Switch pengapian OFF ke ON: Terbangkit pulsa |
| `[3SZ-VE] SIO2 (E10-32) - E1 (E8-29)` | Warna Kabel: GR - BR-W — Komunikasi ECU kunci transponder | Switch pengapian ON ke ST: Terbangkit pulsa |
| `[3SZ-VE] E01 (E8-3) - Masa bodi)` | Warna Kabel: BR - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[3SZ-VE] E1 (E8-29) - Masa bodi` | Warna Kabel: BR-W - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[3SZ-VE] E2 (E8-30) - E1 (E8-29)` | Warna Kabel: BR- BR-W — Massa | Selalu: Di bawah 1 Ω |
| `[EJ-VE] BAT (E10-7) - E1 (E8-29)` | Warna Kabel: B - BR-W — Baterai (untuk mengukur voltase baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[EJ-VE] +B1 (E8-7) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sumber daya ECM | Switch pengapian ON: 11 sampai 14 V |
| `[EJ-VE] VCPM (E8-22) - E2PM (E8-12)` | Warna Kabel: G-R - W-B — Sumber daya sensor vakum | Switch pengapian ON: 4,5 sampai 5,5 V |
| `[EJ-VE] PIM (E8-23) - E2PM (E8-12)` | Warna Kabel: R-W - W-B — Sensor tekanan absolut manifold | Sensor pembebasan udara: 2,2 sampai 3,1 V / Idling: 1,2 sampai 2,0 V |
| `[EJ-VE] VC (E8-10) - E2 (E8-30)` | Warna Kabel: L-R - BR — Sumber daya sensor posisi throttle | Switch pengapian ON: 4,5 sampai 5,5 V |
| `[EJ-VE] VTH (E8-20) - E2 (E8-30)` | Warna Kabel: O - BR — Sensor posisi throttle (untuk kontrol mesin) | Switch pengapian ON, pedal aselerator dibebaskan: 0,4 sampai 0,9 V / Switch pengapian ON, pedal aselerator ditekan: 3,2 sampai 5,0 V |
| `[EJ-VE] THA (E8-13) - E2 (E8-30)` | Warna Kabel: G-W - BR — Sensor temperatur udara masuk | Idling, temperatur udara masuk 20°C (68°F): 0,5 sampai 3,4 V / Idling, temperatur udara masuk 60°C (140°F): 0,2 sampai 1,0 V |
| `[EJ-VE] THW (E8-19) - E2 (E8-30)` | Warna Kabel: B-W - BR — Sensor temperatur cairan pendingin mesin | Setelah pemanasan mesin, temperatur cairan pendingin mesin 60°C sampai 120°C (140°F sampai 248°F): 0,2 sampai 1,0 V |
| `[EJ-VE] KNK (E8-31) - E1 (E8-29)` | Warna Kabel: L - BR-W — Sensor knock | Putaran mesin dipertahankan pada 4.000 rpm setelah mesin dipanaskan: Timbul pulsa (Lihat halaman ) |
| `[EJ-VE] SPD (E10-18) - E1 (E8-29)` | Warna Kabel: LG-R - BR-W — Sinyal kecepatan dari meter kombinasi | Switch pengapian on, Roda penggerak diputar: Timbul pulsa (Lihat halaman ) |
| `[EJ-VE] STA (E9-15) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sinyal starter | Cranking: 11 sampai 14 V / Idling: Di bawah 0,5 V |
| `[EJ-VE] N1+ (E8-11) - N1- (E8-21)` | Warna Kabel: W - B — Sensor posisi crankshaft | Idling: Timbul pulsa (Lihat halaman ) |
| `[EJ-VE] N2+ (E8-18) - N2- (E8-28)` | Warna Kabel: G - R — Sensor posisi camshaft | Idling: Timbul pulsa (Lihat halaman ) |
| `[EJ-VE] OCV+ (E9-7) - OCV- (E9-6)` | Warna Kabel: G-B - LG — Camshaft Timing Oil Control Valve (OCV) | Idling: Timbul pulsa (Lihat bentuk gelombang 1) |
| `[EJ-VE] OX1 (E8-2) - E2 (E8-30)` | Warna Kabel: GR - BR — Sensor heated oxygen (Sensor 1) | Putaran mesin dipertahankan pada 2.500 rpm selama 2 menit setelah mesin dipanaskan: Timbul pulsa (Lihat bentuk gelombang 2) |
| `[EJ-VE] OXH1 (E8-8) - E2 (E8-30)` | Warna Kabel: L-Y - BR — Pemanas sensor heated oxygen (Sensor 1) | Idling: Di bawah 3,0 V / Switch pengapian ON: 11 sampai 14 V |
| `[EJ-VE] #10 (E8-6) - E01 (E8-3)` | Warna Kabel: W-G - BR — Injector | Switch pengapian ON: 11 sampai 14 V |
| `[EJ-VE] #20 (E8-5) - E01 (E8-3)` | Warna Kabel: W-L - BR — Injector | Switch pengapian ON: 11 sampai 14 V |
| `[EJ-VE] #30 (E8-4) - E01 (E8-3)` | Warna Kabel: W-R - BR — Injector | Idling: Timbul pulsa (Lihat bentuk gelombang 3) |
| `[EJ-VE] IG1 (E8-17) - E1 (E8-29)` | Warna Kabel: L-B - BR-W — Koil pengapian (Sinyal pengapian) | Switch pengapian ON: Di bawah 0,5 V |
| `[EJ-VE] IG2 (E8-27) - E1 (E8-29)` | Warna Kabel: LG-B - BR-W — Koil pengapian (Sinyal pengapian) | Switch pengapian ON: Di bawah 0,5 V |
| `[EJ-VE] IG3 (E8-34) - E1 (E8-29)` | Warna Kabel: W-G - BR-W — Koil pengapian (Sinyal pengapian) | Idling: Timbul pulsa (Lihat halaman ) |
| `[EJ-VE] PRG (E8-9) - E01 (E8-3)` | Warna Kabel: P-L - BR — Vacuum switching valve (EVAP) | Switch pengapian ON: 11 sampai 14 V / Idling: Timbul pulsa (Lihat bentuk gelombang 4) |
| `[EJ-VE] IACAHI (E8-15) - IACALO (E8-14)` | Warna Kabel: G-O - G-B — Katup kontrol putaran idle | Idling: Timbul pulsa (0 sampai 12 V) |
| `[EJ-VE] IACBHI (E8-25) - IACBLO (E8-24)` | Warna Kabel: R-B - R-L — Katup kontrol putaran idle | Idling: Timbul pulsa (0 sampai 12 V) |
| `[EJ-VE] PST (E8-32) - E1 (E8-29)` | Warna Kabel: L-W - BR-W — Switch tekanan oli power steering | Switch tekanan oli ON: Di bawah 0,5 V / Switch tekanan oli OFF: 11 sampai 14 V |
| `[EJ-VE] FC1 (E10-22) - E01 (E8-3)` | Warna Kabel: B-W - BR — Pompa bahan bakar | Switch pengapian ON (Mesin tidak hidup): 11 sampai 14 V / Idling: Di bawah 2.0 V |
| `[EJ-VE] VF (E10-17) - E1 (E8-29)` | Warna Kabel: LG-B - BR-W — Air-fuel ratio learned control value output | Mesin idling, terminal T open: Tetap 5 V : Menambah jumlah 0 sampai 5 V pulse generation: Normal Tetap 0 V: Pengurangan jumlah / Putaran mesin 1.200 rpm atau lebih, terminal T short: 5 V: Gemuk 0 V: Kurus / Putaran mesin |
| `[EJ-VE] ACEV (E10-14) - E21 (E10-31)` | Warna Kabel: BR-W - BR-Y — Cooler thermistor No.1 (Sensor temperatur evaporator A/C) | Switch kontrol cooler ON: 0,15 sampai 4,8 V |
| `[EJ-VE] ACSW (E9-24) - E1 (E8-29)` | Warna Kabel: L-O - BR-W — Switch tekanan A/C | Switch pengapian ON (Switch tekanan): 11 sampai 14 V |
| `[EJ-VE] ACVR (E10-30) - E21 (E10-31)` | Warna Kabel: B-O - BR-Y — Kontrol temperatur A/C (Switch kontrol heater) | Switch pengapian ON: Variasi dengan volume |
| `[EJ-VE] MGC (E9-25) - E01 (E8-3)` | Warna Kabel: G-W - BR — Magnet clutch A/C | Magnetic clutch A/C ON: Di bawah 1,0 V / Magnetic clutch A/C OFF: 11 sampai 14 V |
| `[EJ-VE] H/L (E10-10) - E1 (E8-29)` | Warna Kabel: R-L - BR-W — Switch lampu tail | Lampu tail ON: 11 sampai 14 V / Lampu tail OFF: Di bawah 0,5 V |
| `[EJ-VE] BLW (E10-11) - E1 (E8-29)` | Warna Kabel: L-R - BR-W — Motor blower | Switch blower ON: Di bawah 0,5 V / Switch blower OFF: 11 sampai 14 V |
| `[EJ-VE] FAN1 (E9-14) - E01 (E8-3)` | Warna Kabel: R-W - BR — Fan radiator | Fan radiator ON: Di bawah 1,0 V / Fan radiator OFF: 11 sampai 14 V |
| `[EJ-VE] W (E10-6) - E01 (E8-3)` | Warna Kabel: V-W - BR — Malfunction Indicator Lamp (MIL) | MIL menyala: Di bawah 1,0 V / MIL padam: 11 sampai 14 V |
| `[EJ-VE] EFIT (E10-28) - E1 (E8-29)` | Warna Kabel: LG - BR-W — Terminal EFIT dari DLC3 | Switch pengapian ON: 11 sampai 14 V |
| `[EJ-VE] REV (E10-24) - E1 (E8-29)` | Warna Kabel: R-G - BR-W — Sinyal putaran mesin | Idling: Timbul pulsa (Lihat bentuk gelombang 5) |
| `[EJ-VE] STP (E10-12) - E1 (E8-29)` | Warna Kabel: G-Y - BR-W — Switch lampu rem | Pedal rem diinjak: 11 - 14 V / Pedal rem dibebaskan: Di bawah 1,5 V |
| `[EJ-VE] SIO1 (E10-27) - E1 (E8-29)` | Warna Kabel: P - BR-W — Komunikasi tester diagnostik | Switch pengapian OFF ke ON: Timbul pulsa |
| `[EJ-VE] E01 (E8-3) - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[EJ-VE] E1 (E8-29) - Masa bodi` | Warna Kabel: BR-W - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[EJ-VE] E2 (E8-30) - E1 (E8-29)` | Warna Kabel: BR- BR-W — Masa | Selalu: Di bawah 1 Ω |
| `[K3-VE] BAT (E10-7) - E1 (E8-29)` | Warna Kabel: B - BR-W — Baterai (untuk mengukur voltase baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[K3-VE] +B1 (E8-7) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sumber daya ECM | Switch pengapian ON: 11 sampai 14 V |
| `[K3-VE] VCPM (E8-22) - E2PM (E8-12)` | Warna Kabel: G-R - W-B — Sumber daya sensor tekanan absolut manifold | Switch pengapian ON: 4,5 sampai 5,5 V |
| `[K3-VE] PIM (E8-23) - E2PM (E8-12)` | Warna Kabel: R-W - W-B — Sensor tekanan absolut manifold | Sensor pembebasan udara: 3,1 sampai 4,1 V / Idling: 1,2 sampai 2,0 V |
| `[K3-VE] VC (E8-10) - E2 (E8-30)` | Warna Kabel: L-R - BR — Sumber daya sensor posisi throttle | Switch pengapian ON: 4,5 sampai 5,5 V |
| `[K3-VE] VTH (E8-20) - E2 (E8-30)` | Warna Kabel: O - BR — Sensor posisi throttle (untuk kontrol mesin) | Switch pengapian ON, pedal aselerator dibebaskan: 0,4 sampai 0,9 V / Switch pengapian ON, pedal aselerator ditekan: 3,2 sampai 5,0 V |
| `[K3-VE] THA (E8-13) - E2 (E8-30)` | Warna Kabel: G-W - BR — Sensor temperatur udara intake | Idling, temperatur udara masuk 20°C (20,00°C): 0,5 sampai 3,4 V / Idling, temperatur udara masuk 60°C (140°F): 0,2 sampai 1,0 V |
| `[K3-VE] THW (E8-19) - E2 (E8-30)` | Warna Kabel: B-W - BR — Sensor temperatur cairan pendingin mesin | Setelah pemanasan mesin, temperatur cairan pendingin mesin 60°C sampai 120°C (140°F sampai 248°F): 0,3 sampai 1,3 V |
| `[K3-VE] KNK (E8-31) - E1 (E8-29)` | Warna Kabel: L - BR-W — Sensor knock | Putaran mesin dipertahankan pada 4.000 rpm setelah mesin dipanaskan: Terbangkit pulsa (Lihat halaman ) |
| `[K3-VE] SPD (E10-18) - E1 (E8-29)` | Warna Kabel: LG-R - BR-W — Sinyal kecepatan dari meter kombinasi | Switch pengapian on, Roda penggerak diputar: Terbangkit pulsa (Lihat halaman ) |
| `[K3-VE] STA (E9-15) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sinyal starter | Mengengkol: 6 V atau lebih / Idling: Di bawah 0,5 V |
| `[K3-VE] Antara N1+ (E8-11) dan N1- (E8-21)` | Warna Kabel: W - B — Sensor posisi crankshaft | Idling: Terbangkit pulsa (Lihat halaman ) |
| `[K3-VE] N2+ (E8-18) - N2- (E8-28)` | Warna Kabel: G - R — Sensor posisi crankshaft | Idling: Terbangkit pulsa (Lihat halaman ) |
| `[K3-VE] OCV+ (E9-7) - OCV- (E9-6)` | Warna Kabel: G-B - LG — Camshaft Timing Oil Control Valve (OCV) | Idling: Terbangkit pulsa (Lihat model gelombang 1) |
| `[K3-VE] VTH (E8-2) - E2 (E8-30)` | Warna Kabel: GR - BR — Sensor heated oxygen (Sensor 1) | Putaran mesin dipertahankan pada 2.500 rpm selama 2 menit setelah mesin dipanaskan: Terbangkit pulsa (Lihat model gelombang 2) |
| `[K3-VE] OXH1 (E8-8) - E2 (E8-30)` | Warna Kabel: L-Y - BR — Pemanas sensor heated oxygen (Sensor 1) | Idling: Di bawah 3,0 V / Switch pengapian ON: 8 sampai 14 V |
| `[K3-VE] #10 (E8-6) - E01 (E8-3)` | Warna Kabel: W-G - BR — Injector | Switch pengapian ON: 11 sampai 14 V |
| `[K3-VE] #20 (E8-5) - E01 (E8-3)` | Warna Kabel: W-L - BR — Injector | Switch pengapian ON: 11 sampai 14 V |
| `[K3-VE] #30 (E8-4) - E01 (E8-3)` | Warna Kabel: W-R - BR — Injector | Idling: Terbangkit pulsa (Lihat model gelombang 3) |
| `[K3-VE] #40 (E9-5) - E01 (E8-3)` | Warna Kabel: W - BR — Injector | Idling: Terbangkit pulsa (Lihat model gelombang 3) |
| `[K3-VE] IG1 (E8-17) - E1 (E8-29)` | Warna Kabel: L-B - BR-W — Koil pengapian (Sinyal pengapian) | Switch pengapian ON: Di bawah 0,5 V |
| `[K3-VE] IG2 (E8-27) - E1 (E8-29)` | Warna Kabel: LG-B - BR-W — Koil pengapian (Sinyal pengapian) | Switch pengapian ON: Di bawah 0,5 V |
| `[K3-VE] IG3 (E8-34) - E1 (E8-29)` | Warna Kabel: W-G - BR-W — Koil pengapian (Sinyal pengapian) | Idling: Terbangkit pulsa (Lihat halaman ) |
| `[K3-VE] IG4 (E8-16) - E1 (E8-29)` | Warna Kabel: W-R - BR-W — Koil pengapian (Sinyal pengapian) | Idling: Terbangkit pulsa (Lihat halaman ) |
| `[K3-VE] PRG (E8-9) - E01 (E8-3)` | Warna Kabel: P-L - BR — Vacuum switching valve (EVAP) | Switch pengapian ON: 11 sampai 14 V / Idling: Terbangkit pulsa (Lihat model gelombang 4) |
| `[K3-VE] IACAHI (E8-15) - IACALO (E8-14)` | Warna Kabel: G-O - G-B — Katup kontrol putaran idle | Idling: Terbangkit pulsa (0 sampai 12 V) |
| `[K3-VE] IACBHI (E8-25) - IACBLO (E8-24)` | Warna Kabel: R-B - R-L — Katup kontrol putaran idle | Idling: Terbangkit pulsa (0 sampai 12 V) |
| `[K3-VE] DEF (E10-4) - E1 (E8-29)` | Warna Kabel: W-G - BR-W — Switch defogger | Switch defogger OFF: 0 sampai 1,5 V / Switch defogger ON: 7,5 sampai 14 V |
| `[K3-VE] PST (E8-32) - E1 (E8-29)` | Warna Kabel: L-W - BR-W — Switch tekanan oli power steering | Switch tekanan oli ON: Di bawah 0,5 V / Switch tekanan oli OFF: 11 sampai 14 V |
| `[K3-VE] Tanpa sistem engine immobilizer: FC1 (E10-22) - E01 (E8-3) Dengan sistem engine im` | Warna Kabel: B-W - BR — Pompa bahan bakar | Switch pengapian ON (Mesin tidak hidup): 11 sampai 14 V / Idling: Di bawah 2,0 V |
| `[K3-VE] VF (E10-17) - E1 (E8-29)` | Warna Kabel: LG-B - BR-W — Air-fuel ratio learned control value output | Mesin idling, terminal EFIT open: Tetap 5 V: Jumlah bertambah Pembangkitan pulsa 0 sampai 5 V: Normal Tetap 0 V: Jumlah berkurang / Putaran mesin 1.200 rpm atau lebih, terminal EFIT short: 5 V: Gemuk 0 V: Kurus / Putaran |
| `[K3-VE] ACEV (E10-14) - E21 (E10-31)` | Warna Kabel: BR-W - BR-Y — Cooler thermistor No.1 (Sensor temperatur evaporator A/C) | Air conditioner ON: 0,15 sampai 4,8 V |
| `[K3-VE] ACSW (E9-24) - E1 (E8-29)` | Warna Kabel: L-O - BR-W — Tanpa heater: Switch tekanan A/C | Switch pengapian ON (Switch tekanan): 11 sampai 14 V / Mesin idling Switch blower ON dan switch kontrol cooler ON: 11 sampai 14 V |
| `[K3-VE] ACVR (E10-30) - E21 (E10-31)` | Warna Kabel: B-O - BR-Y — Switch kontrol temperatur A/C (Switch kontrol heater) | Switch pengapian ON: Variasi dengan volume |
| `[K3-VE] MGC (E9-25) - E01 (E8-3)` | Warna Kabel: G-W - BR — Magnet clutch A/C | Magnetic clutch A/C ON: Di bawah 1,0 V / Magnetic clutch A/C OFF: 11 sampai 14 V |
| `[K3-VE] H/L (E10-10) - E1 (E8-29)` | Warna Kabel: R-L - BR-W — Switch lampu tail | Lampu tail ON: 11 sampai 14 V / Lampu tail OFF: Di bawah 0,5 V |
| `[K3-VE] BLW (E10-11) - E1 (E8-29)` | Warna Kabel: L-R - BR-W — Motor blower | Switch blower ON: Di bawah 0,5 V / Switch blower OFF: 11 sampai 14 V |
| `[K3-VE] FAN1 (E9-14) - E01 (E8-3)` | Warna Kabel: R-W - BR — Fan radiator | Fan radiator ON: Di bawah 1,0 V / Fan radiator OFF: 11 sampai 14 V |
| `[K3-VE] W (E10-6) - E01 (E8-3)` | Warna Kabel: V-W - BR — Lampu Indikator Malfungsi (MIL) | MIL menyala: Di bawah 1,0 V / MIL padam: 11 sampai 14 V |
| `[K3-VE] EFIT (E10-28) - E1 (E8-29)` | Warna Kabel: LG - BR-W — Terminal EFIT dari DLC3 | Switch pengapian ON: 11 sampai 14 V |
| `[K3-VE] REV (E10-24) - E1 (E8-29)` | Warna Kabel: R-G - BR-W — Sinyal putaran mesin | Idling: Terbangkit pulsa (Lihat model gelombang 5) |
| `[K3-VE] FPOF (E10-13) - E1 (E8-29)` | Warna Kabel: L - BR-W — Sensor airbag tengah assembly | Idle dengan mesin dalam kondisi panas: Terbangkit pulsa (Lihat model gelombang 6) |
| `[K3-VE] STP (E10-12) - E1 (E8-29)` | Warna Kabel: G-Y - BR-W — Switch lampu rem | Pedal rem ditekan: 11 - 14 V / Pedal Rem Dibebaskan: Di bawah 1,5 V |
| `[K3-VE] SIO1 (E10-27) - E1 (E8-29)` | Warna Kabel: P - BR-W — Komunikasi tester diagnostik | Switch pengapian OFF → ON: Terbangkit pulsa |
| `[K3-VE] SIO2 (E10-32) - E1 (E8-29)` | Warna Kabel: GR - BR-W — Komunikasi ECU kunci transponder | Switch pengapian ON ke ST: Terbangkit pulsa |
| `[K3-VE] E01 (E8-3) - Masa bodi)` | Warna Kabel: BR - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[K3-VE] E1 (E8-29) - Masa bodi` | Warna Kabel: BR-W - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[K3-VE] E2 (E8-30) - E1 (E8-29)` | Warna Kabel: BR- BR-W — Massa | Selalu: Di bawah 1 Ω |
| `[A/T A4Q] P (T8-15) - E1 (T9-24)` | Warna Kabel: G-B - B — Sinyal switch posisi pemindahan P | Switch pengapian ON dan shift lever posisi P: Di bawah 1 V / Switch pengapian ON dan shift lever selain posisi P: 11 sampai 14 V |
| `[A/T A4Q] R (T9-7) - E1 (T9-24)` | Warna Kabel: G-W - B — Sinyal switch posisi pemindahan R | Switch pengapian ON dan shift lever posisi R: 11 sampai 14 V / Switch pengapian ON dan shift lever selain posisi posisi R: Di bawah 1 V |
| `[A/T A4Q] N (T8-24) - E1 (T9-24)` | Warna Kabel: G-R - B — Sinyal switch posisi pemindahan N | Switch pengapian ON dan shift lever posisi N: Di bawah 1 V / Switch pengapian ON dan shift lever selain posisi posisi N: 11 sampai 14 V |
| `[A/T A4Q] D (T8-17) - E1 (T9-24)` | Warna Kabel: B-L - B — Sinyal switch posisi pemindahan D | Switch pengapian ON dan shift lever posisi D: Di bawah 1 V / Switch pengapian ON dan shift lever selain posisi posisi D: 11 sampai 14 V |
| `[A/T A4Q] 2 (T8-16) - E1 (T9-24)` | Warna Kabel: G-O - B — 2 sinyal switch posisi pemindahan | Switch pengapian ON dan shift lever posisi 2: Di bawah 1 V / Switch pengapian ON dan shift lever selain posisi posisi 2: 11 sampai 14 V |
| `[A/T A4Q] L (T8-25) - E1 (T9-24)` | Warna Kabel: V - B — Sinyal switch posisi pemindahan L | Switch pengapian ON dan shift lever posisi L: Di bawah 1 V / Switch pengapian ON dan shift lever selain posisi posisi L: 11 sampai 14 V |
| `[A/T A4Q] VBTB (T8-9) - ETBN (T8-20)` | Warna Kabel: L-B - P-B — Sumber daya sensor kecepatan input | Switch pengapian ON: 11 sampai 14 V |
| `[A/T A4Q] RTBN (T8-10) - ETBN (T8-20)` | Warna Kabel: W - P-B — Sinyal sensor input speed | Mesin putaran idle dan posisi shift lever P atau N: Terbangkit pulsa (Lihat model gelombang 1) |
| `[A/T A4Q] ETBN (T8-20) - E1 (T9-24)` | Warna Kabel: P-B - B — Masa sensor kecepatan input | Selalu: Di bawah 1 Ω |
| `[A/T A4Q] VBOP (T8-7) - EOPT (T8-18)` | Warna Kabel: L-Y - W-L — Sumber daya sensor output speed | Switch pengapian ON: 11 sampai 14 V |
| `[A/T A4Q] ROPT (T8-8) - EOPT (T8-18)` | Warna Kabel: L - W-L — Sinyal sensor output speed | Kecepatan kendaraan 20 km/jam (12 mph): Terbangkit pulsa (Lihat model gelombang 2) |
| `[A/T A4Q] EOPT (T8-18) - E1 (T9-24)` | Warna Kabel: W-L - B — Masa sensor output speed | Selalu: Di bawah 1 Ω |
| `[A/T A4Q] OTMP (T8-14) - ETMP (T8-13)` | Warna Kabel: Y-B - BR-W — Sinyal sensor temperatur ATF | Temperatur ATF: 80 °C (176°F) atau lebih: Di bawah 1,1 V / Temperatur ATF: 20 °C (20,00°C): Sekitar 3,4 V |
| `[A/T A4Q] SPDO (T9-15) - E1 (T9-24)` | Warna Kabel: P - B — Sinyal Kecepatan Kendaraan | Kecepatan kendaraan 40 km/jam (25 mph): Terbangkit pulsa (Lihat model gelombang 3) |
| `[A/T A4Q] REG1 (T9-8) - E1 (T9-24)` | Warna Kabel: L-W - B — Sinyal Putaran Mesin | Putaran idle mesin: Terbangkit pulsa (Lihat model gelombang 4) |
| `[A/T A4Q] B1+ (T8-6) - B1-(T8-5)` | Warna Kabel: R-W - G-W — Sinyal solenoid SL1 | Ketika kelistrikan diputar ke on: Terbangkit pulsa (Lihat model gelombang 5) / Ketika kelistrikan tidak diputar ke on: Di bawah 1 V |
| `[A/T A4Q] C2+ (T8-4) - C2-(T8-3)` | Warna Kabel: B-W - G-Y — Sinyal solenoid SL2 | Ketika kelistrikan diputar ke on: Terbangkit pulsa (Lihat model gelombang 6) / Ketika kelistrikan tidak diputar ke on: Di bawah 1 V |
| `[A/T A4Q] C3B2+ (T8-2) - C3B2-(T8-1)` | Warna Kabel: W-G - W-R — Sinyal solenoid SL3 | Ketika kelistrikan diputar ke on: Terbangkit pulsa (Lihat model gelombang 7) / Ketika kelistrikan tidak diputar ke on: Di bawah 1 V |
| `[A/T A4Q] LUCC (T8-23) - E01 (T9-6)` | Warna Kabel: B-Y - B — Sinyal solenoid DSU | Lock-up OFF: Di bawah 1 V / Slip lock-up (ON ←→ OFF): Terbangkit pulsa (Lihat model gelombang 8) |
| `[A/T A4Q] LUCR (T8-11) - E01 (T9-6)` | Warna Kabel: L-R - B — Sinyal solenoid SL | Ketika kelistrikan diputar ke on: 11 sampai 14 V / Ketika kelistrikan tidak diputar ke on: Di bawah 1 V |
| `[A/T A4Q] SOLR (T8-12) - E01 (T9-6)` | Warna Kabel: GR - B — Sinyal solenoid SR | Ketika kelistrikan diputar ke on: 11 sampai 14 V / Ketika kelistrikan tidak diputar ke on: Di bawah 1 V |
| `[A/T A4Q] O/D1 (T9-22) - E1 (T9-24)` | Warna Kabel: LG-R - B — Switch utama O/D | Switch pengapian ON: 11 sampai 14 V / Switch pengapian ON dan tekan switch utama O/D secara kontinu: Di bawah 1 V |
| `[A/T A4Q] ODL (T10-22) - E1 (T9-24)` | Warna Kabel: L-O - B — Sinyal indikator O/D OFF | Switch utama O/D ON (O/D OFF): Di bawah 3 V / Switch utama O/D OFF (O/D ON): 7,5 sampai 14 V |
| `[A/T A4Q] BRK (T9-18) - E1 (T9-24)` | Warna Kabel: G-Y - B — Sinyal switch lampu rem | Pedal rem diinjak: 7,5 sampai 14 V / Pedal rem dibebaskan: Di bawah 1,5 V |
| `[A/T A4Q] CTX (T9-12) - E1 (T9-24)` | Warna Kabel: G - B — Sinyal serial komunikasi dengan ECM | Switch pengapian ON: Terbangkit pulsa (0 sampai 12 V) |
| `[A/T A4Q] CRX (T9-4) - E1 (T9-24)` | Warna Kabel: R - B — Sinyal serial komunikasi dengan ECM | Switch pengapian ON: Terbangkit pulsa (0 sampai 12 V) |
| `[A/T A4Q] SIO1 (T9-17) - E1 (T9-24)` | Warna Kabel: P-G - B — Komunikasi tester diagnostik | Selama komunikasi dengan intelligent tester: Terbangkit pulsa |
| `[A/T A4Q] T (T10-11) - E1 (T9-24)` | Warna Kabel: V - B — Terminal ECUT dari DLC3 | Switch pengapian ON: 11 sampai 14 V |
| `[A/T A4Q] +B1 (T9-3) - E01 (T9-6)` | Warna Kabel: LG - B — Switch pengapian | Switch pengapian ON: 11 sampai 14 V |
| `[A/T A4Q] BAT1 (T9-2) - E01 (T9-6)` | Warna Kabel: L-B - B — Baterai (untuk memory ECU) | Selalu: 11 sampai 14 V |
| `[A/T A4Q] BAT2 (T9-1) - E01 (T9-6)` | Warna Kabel: L-B - B — Baterai (untuk memory ECU) | Selalu: 11 sampai 14 V |
| `[A/T A4Q] E1 (T9-24) -Masa bodi` | Warna Kabel: B - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[A/T A4Q] E01 (T9-6) -Masa bodi` | Warna Kabel: B - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[A/T A4Q] E02 (T9-5) -Masa bodi` | Warna Kabel: B - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[A/T A4Q] ATNE (E9-3) - E1 (E8-29)` | Warna Kabel: L-W - BR-W — Sinyal Putaran Mesin | Putaran idle mesin: Terbangkit pulsa |
| `[A/T A4Q] ATTX (E9-2) - E1 (E8-29)` | Warna Kabel: R - BR-W — Sinyal serial komunikasi dengan ECU kontrol transmisi | Switch pengapian ON: Terbangkit pulsa (0 sampai 12 V) |
| `[A/T A4Q] ATRX (E9-1) - E1 (E8-29)` | Warna Kabel: G - BR-W — Sinyal serial komunikasi dengan ECU kontrol transmisi | Switch pengapian ON: Terbangkit pulsa (0 sampai 12 V) |
| `[AIR CONDITIONING] BAT (E10-7) - E1 (E8-29)` | Warna Kabel: B - BR-W — Baterai (untuk mengukur voltase baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[AIR CONDITIONING] +B1 (E8-7) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sumber daya ECM | Switch pengapian ON: 11 sampai 14 V |
| `[AIR CONDITIONING] ACEV (E10-14) - E21 (E10-31)` | Warna Kabel: BR-W - BR-Y — Thermistor cooler No.1 (Sensor temperatur evaporator A/C) | Air conditioner: OFF ke ON: Di bawah 1,0 V → 0,15 sampai 4,8 V |
| `[AIR CONDITIONING] ACSW (E9-24) - E1 (E8-29)` | Warna Kabel: L-O - BR-W — Tanpa heater: Switch tekanan A/C | Switch pengapian ON: 11 sampai 14 V / Mesin idling Switch blower ON dan switch kontrol cooler ON: 11 sampai 14 V |
| `[AIR CONDITIONING] ACVR (E10-30) - E21 (E10-31)` | Warna Kabel: B-O - BR-Y — Switch kontrol temperatur A/C (Switch kontrol heater) | Switch pengapian ON: Variasi dengan volume |
| `[AIR CONDITIONING] MGC (E9-25) - E01 (E8-3)` | Warna Kabel: G-W - BR — Magnetic clutch A/C | Magnetic clutch A/C ON ke OFF: Di bawah 1,0 V → 11 sampai 14 V |
| `[AIR CONDITIONING] BLW (E10-11) - E1 (E8-29)` | Warna Kabel: L-R - BR-W — Motor blower | Switch blower heather ON ke OFF: 0 sampai 0,5 V →11 sampai 14 V |
| `[AIR CONDITIONING] FAN1 (E9-14) - E01 (E8-3)` | Warna Kabel: R-W - BR — Fan radiator | Fan radiator ON ke OFF: Di bawah 1,0 V → 11 sampai 14 V |
| `[AIR CONDITIONING] E01 (E8-3) - Masa bodi` | Warna Kabel: BR - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[AIR CONDITIONING] E1 (E8-29) - Masa bodi` | Warna Kabel: BR-W - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[AIR CONDITIONING] E2 (E8-30) - E1 (E8-29)` | Warna Kabel: BR- BR-W — Massa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] ANT1 (T13-1) - ANT2 (T13-7)` | Warna Kabel: B-W - B — (Koil kunci transponder) | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] GND (T14-7) - Masa bodi` | Warna Kabel: W-B - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] +B (T14-1) - GND (T14-7)` | Warna Kabel: B-R - W-B — Baterai | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] IG (T14-2) - GND (T14-7)` | Warna Kabel: LG - W-B — Switch pengapian | Switch pengapian 1: OFF ke 2: ON: 1: 0 V → 2: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] KSW ( T14-3) - GND (T14-7)` | Warna Kabel: R-W - W-B — Switch peringatan unlock | Tidak terdapat kunci dalam silinder kunci pengapian.: 10 kΩ atau lebih tinggi / Kunci di dalam silinder kunci pengapian.: Di bawah 1 Ω / Tidak terdapat kunci dalam silinder kunci pengapian.: 11 sampai 14 V / Kunci di dal |
| `[ENGINE IMMOBILISER] SIO1 (T14-9) - GND (T14-7)` | Warna Kabel: P-B - W-B — Komunikasi diagnosis tester | Switch pengapian OFF → ON: Terbangkit pulsa |
| `[ENGINE IMMOBILISER] SIO2 (T14-8) - GND (T14-7)` | Warna Kabel: GR - W-B — Koumunikasi Immobiliser | Switch pengapian OFF → ON: Terbangkit pulsa |
| `[ENGINE IMMOBILISER] IND (T14-14) - GND (T14-7)` | Warna Kabel: L-W - W-B — Sinyal indikator keamanan | Sistem engine immobiliser SET → UNSET: 3 sampai 5 V → Di bawah 1 V |
| `[ENGINE IMMOBILISER] COIL(+) (T14-6) - COIL(-) (T14-13)` | Warna Kabel: B-W - B — Koil kunci transponder | Selalu: Di bawah 1 Ω |
| `[ENGINE IMMOBILISER] BAT (E10-7) - E1 (E8-29)` | Warna Kabel: B - BR-W — Baterai (untuk mengukur voltase baterai dan untuk memory ECM) | Selalu: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] +B1 (E8-7) - E1 (E8-29)` | Warna Kabel: B-R - BR-W — Sumber daya ECM | Switch pengapian ON: 11 sampai 14 V |
| `[ENGINE IMMOBILISER] SIO1 (E10-26) - E1 (E8-29)` | Warna Kabel: P-B - BR-W — Komunikasi diagnosis tester | Switch pengapian ON: Terbangkit pulsa |
| `[ENGINE IMMOBILISER] SIO2 (E10-32) - E1 (E8-29)` | Warna Kabel: GR - BR-W — Koumunikasi Immobiliser | Switch pengapian ON: Terbangkit pulsa |
| `[ENGINE IMMOBILISER] E1 (E8-29) - Masa bodi` | Warna Kabel: BR-W - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[DOOR LOCK] D2-3 - Masa bodi` | Warna Kabel: B - Masa bodi — +B sumber daya | Selalu: 11 sampai 14V |
| `[DOOR LOCK] D2-4 - Masa bodi` | Warna Kabel: P * 1 - Masa bodi G * 2 -Masa bodi — Kontrol input kunci pintu sisi pengemudi | Switch kontrol kunci pintu (tombol kunci pintu sisi pengemudi atau silinder kunci) LOCK: 10 KΩ atau lebih tinggi / Switch kontrol kunci pintu (tombol kunci pintu sisi pengemudi atau silinder kunci)UNLOCK: Di bawah 1Ω |
| `[DOOR LOCK] D2-6 - Masa bodi` | Warna Kabel: W-B - Masa bodi — Massa | Selalu: Di bawah 1Ω |
| `[DOOR LOCK] D2-1 - Masa bodi` | Warna Kabel: L - Masa bodi — Semua door lock motor mengeluarkan gerakan UNLOCK | Switch kontrol kunci pintu (tombol kunci pintu sisi pengemudi atau silinder kunci) LOCK: Di bawah 1 V / Switch kontrol kunci pintu (tombol kunci pintu sisi pengemudi atau silinder kunci)UNLOCK: 11 sampai 14V |
| `[DOOR LOCK] D2-2 - Masa bodi` | Warna Kabel: L-W - Masa bodi — Semua door lock motor mengeluarkan gerakan LOCK | Switch kontrol kunci pintu (tombol kunci pintu sisi pengemudi atau silinder kunci) LOCK: 11 sampai 14V / Switch kontrol kunci pintu (tombol kunci pintu sisi pengemudi atau silinder kunci)UNLOCK: Di bawah 1 V |
| `[METER] C4-2 - Masa bodi` | Warna Kabel: G-B - Masa bodi — Tanda belok kiri | Lampu indikator belok kiri OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C4-3 (*3) - Masa bodi` | Warna Kabel: V-R - Masa bodi — Sinyal ABS | Lampu peringatan ABS OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C4-5 (*1) - Masa bodi` | Warna Kabel: L-O - Masa bodi — Sinyal permukaan bahan bakar | Switch pengapian ON: 11 sampai 14 V |
| `[METER] C4-6 - Masa bodi` | Warna Kabel: W-B - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[METER] C4-7 - Masa bodi` | Warna Kabel: R-L - Masa bodi — Sinyal penerangan | Switch dimmer head light OFF → TAIL: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C4-8 - Masa bodi` | Warna Kabel: V - Masa bodi — Sinyal temperatur cairan pendingin mesin | Switch pengapian ON: 18,0 sampai 198,5 Ω |
| `[METER] C4-10 - Masa bodi` | Warna Kabel: LG-R - Masa bodi — Sinyal Kecepatan Kendaraan | Roda penggerak berputar perlahan dan switch pengapian ON: Terbangkit pulsa (Lihat model gelombang 1) |
| `[METER] C4-11 - Masa bodi` | Warna Kabel: BR - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[METER] C4-12 - Masa bodi` | Warna Kabel: V-W - Masa bodi — Sinyal MIL | Lampu indikator check engine ON → OFF: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C5-1 - Masa bodi` | Warna Kabel: G - Masa bodi — Tanda belok kanan | Lampu indikator belok kanan OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C5-2 - Masa bodi` | Warna Kabel: R-Y - Bodi masa — Sinyal Hi-beam | Lampu indikator Hi beam OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C5-3 (*5) - Masa bodi` | Warna Kabel: R-G - Masa bodi — Sinyal tacho | Mesin hidup: Terbangkit pulsa (Lihat model gelombang 2) |
| `[METER] C5-4 (*5) - Masa bodi C5-5 (*6) - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal sender bahan bakar | Switch pengapian ON: 7,0 sampai 119,0 Ω |
| `[METER] C5-6 (*1) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal switch courtesy pintu | Lampu peringatan pintu OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C5-7 (*1) - Masa bodi` | Warna Kabel: W-L - Masa bodi — Sinyal switch courtesy pintu | Lampu peringatan pintu OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C5-8 (*1) - Masa bodi` | Warna Kabel: B-R - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[METER] C5-10 - Masa bodi` | Warna Kabel: R-W (*3) - Masa bodi R (*4) - Masa bodi — Sinyal EBD (*3) Switch rem parkir dan sinyal switch peringatan level minyak rem (*4) | Lampu peringatan rem OFF → ON: Di bawah 1 V → 11 sampai 14 V (*3) 11 sampai 14 V → Di bawah 1 V (*4) |
| `[METER] C5-11 (*2) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal Airbag | Lampu peringatan airbag OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C5-13 (*1) - Masa bodi` | Warna Kabel: P-L - Masa bodi — Sinyal seat belt pengemudi | Switch pengapian ON dan switch buckle seat belt pengemudi ON (Belt tidak dikenakan): Di bawah 1 V / Switch pengapian ON dan switch buckle seat belt pengemudi OFF (Belt dikenakan): 11 sampai 14 V |
| `[METER] C5-14 - Masa bodi` | Warna Kabel: W-R - Masa bodi — Sinyal pengisian arus | Switch pengapian ON (mesin mati) → mesin idle: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C5-15 - Masa bodi` | Warna Kabel: L-W - Masa bodi — Sinyal tekanan oli | Lampu peringatan tekanan oli ON → OFF: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C5-16 - Masa bodi` | Warna Kabel: LG - Masa bodi — Sinyal switch pengapian | Switch pengapian OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-1 - Masa bodi` | Warna Kabel: G - Masa bodi — Tanda belok kanan | Lampu indikator belok kanan OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-2 - Masa bodi` | Warna Kabel: R-Y - Masa bodi — Sinyal Hi-beam | Lampu indikator Hi beam OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-3 (*1) - Masa bodi` | Warna Kabel: W-L - Masa bodi — Sinyal switch courtesy pintu | Lampu peringatan pintu OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-4 (*1) - Masa bodi` | Warna Kabel: W - Masa bodi — Sinyal switch courtesy pintu | Lampu peringatan pintu OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-5 - Masa bodi` | Warna Kabel: G-B - Masa bodi — Tanda belok kiri | Lampu indikator belok kiri OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-7 - Masa bodi` | Warna Kabel: G-W - Masa bodi — Switch posisi parkir/Netral (R) | Switch pengapian ON A/T shift lever dalam posisi R: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-8 - Masa bodi` | Warna Kabel: R-W - Masa bodi — Sinyal EBD | Lampu peringatan rem OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-9 (*1) - Masa bodi` | Warna Kabel: P-L - Masa bodi — Sinyal seat belt pengemudi | Switch pengapian ON dan switch buckle seat belt pengemudi ON (Belt tidak dikenakan): Di bawah 1 V / Switch pengapian ON dan switch buckle seat belt pengemudi OFF (Belt dikenakan): 11 sampai 14 V |
| `[METER] C8-10 - Masa bodi` | Warna Kabel: R-B - Masa bodi — Sinyal tacho | Mesin hidup: Terbangkit pulsa (Lihat model gelombang 2) |
| `[METER] C8-11 - Masa bodi` | Warna Kabel: R-G - Masa bodi — Sinyal tacho | Mesin hidup: Terbangkit pulsa (Lihat model gelombang 2) |
| `[METER] C8-12 - Masa bodi` | Warna Kabel: P - Bodi masa — Sinyal Kecepatan Kendaraan | Roda penggerak berputar perlahan dan switch pengapian ON: Terbangkit pulsa (Lihat model gelombang 1) |
| `[METER] C8-13 - Masa bodi` | Warna Kabel: LG-R - Masa bodi — Sinyal Kecepatan Kendaraan | Roda penggerak berputar perlahan dan switch pengapian ON: Terbangkit pulsa (Lihat model gelombang 1) |
| `[METER] C8-14 - Masa bodi` | Warna Kabel: R-L - Masa bodi — Sinyal penerangan | Switch dimmer head light OFF → TAIL: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-16 - Masa bodi` | Warna Kabel: BR - Masa bodi — Masa | Selalu: Di bawah 1 Ω |
| `[METER] C8-17 (*2) - Masa bodi` | Warna Kabel: G-Y - Masa bodi — Sinyal Airbag | Lampu peringatan airbag OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-18 - Masa bodi` | Warna Kabel: V-R - Masa bodi — Sinyal ABS | Lampu peringatan ABS OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-19 - Masa bodi` | Warna Kabel: L-Y - Masa bodi — Sinyal sender bahan bakar | Switch pengapian ON: 11 sampai 14 V |
| `[METER] C8-20 - Masa bodi` | Warna Kabel: V - Masa bodi — Sinyal temperatur cairan pendingin mesin | Switch pengapian ON: 22,1 sampai 217,8 Ω |
| `[METER] C8-21 - Masa bodi` | Warna Kabel: W-R - Masa bodi — Sinyal relay starter | Switch pengapian OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-22 - Masa bodi` | Warna Kabel: G-B - Masa bodi — Switch posisi parkir/netral (P) | Switch pengapian ON A/T shift lever dalam posisi P: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-23 - Masa bodi` | Warna Kabel: G-R - Masa bodi — Switch posisi parkir/netral (N) | Switch pengapian ON A/T shift lever dalam posisi N: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-24 - Masa bodi` | Warna Kabel: B-L - Masa bodi — Switch posisi parkir/netral (D) | Switch pengapian ON A/T shift lever dalam posisi D: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-25 - Masa bodi` | Warna Kabel: G-O - Masa bodi — Switch posisi parkir/netral (2) | Switch pengapian ON A/T shift lever dalam posisi 2: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-26 - Masa bodi` | Warna Kabel: V - Masa bodi — Switch posisi parkir/netral (L) | Switch pengapian ON A/T shift lever dalam posisi L: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-35 - Masa bodi` | Warna Kabel: L-O - Masa bodi — Sinyal O/D OFF | Lampu indikator O/D OFF dari OFF → ON: 11 sampai 14 V → Di bawah 1 V |
| `[METER] C8-36 - Masa bodi` | Warna Kabel: W-R - Masa bodi — Sinyal pengisian arus | Switch pengapian ON (mesin mati) → mesin idle: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-37 - Masa bodi` | Warna Kabel: V-W - Masa bodi — Sinyal MIL | Lampu indikator check engine ON → OFF: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-38 - Masa bodi` | Warna Kabel: L-W - Masa bodi — Sinyal tekanan oli | Lampu peringatan tekanan oli ON → OFF: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-39 - Masa bodi` | Warna Kabel: LG - Masa bodi — Sinyal switch pengapian | Switch pengapian OFF → ON: Di bawah 1 V → 11 sampai 14 V |
| `[METER] C8-40 - Masa bodi` | Warna Kabel: B-R - Masa bodi — Baterai | Selalu: 11 sampai 14 V |
| `[AUDIO / VISUAL] R3-1 (FR+) - R3-7 (GND)` | Warna Kabel: L * 3 - BR R * 4 - BR — Sinyal suara (Kanan Depan) | Mainkan sistem audio: - |
| `[AUDIO / VISUAL] R3-2 (FL+) - R3-7 (GND)` | Warna Kabel: G * 3 - BR LG * 4 - BR — Sinyal suara (Kiri Depan) | Mainkan sistem audio: - |
| `[AUDIO / VISUAL] R3-3 (ACC * 1) - R3-7 (GND) R3-3 (ACC+B * 2) - R3-7 (GND)` | Warna Kabel: L - BR — Aksessoris (ON) | Putar switch pengapian ke ACC: 11 sampai 14 V |
| `[AUDIO / VISUAL] R3-4 (BU+B * 1) - R3-7 (GND) R3-4 (BACK-UP * 5) - R3-7 (GND) R3-4 (+B * 6` | Warna Kabel: B-R - BR — Baterai | Selalu: 11 sampai 14 V |
| `[AUDIO / VISUAL] R3-5 (FR-) - R3-7 (GND)` | Warna Kabel: L-B * 3 - BR R-B * 4 - BR — Sinyal suara (Kanan Depan) | Mainkan sistem audio: - |
| `[AUDIO / VISUAL] R3-6 (FL-) - R3-7 (GND)` | Warna Kabel: G-W * 3 - BR LG-B * 4 - BR — Sinyal suara (Kiri Depan) | Mainkan sistem audio: - |
| `[AUDIO / VISUAL] R3-7 (GND) - Masa bodi` | Warna Kabel: BR - Masa bodi — Massa | Selalu: Di bawah 1 Ω |
| `[AUDIO / VISUAL] R4-1 (RR+) - R3-7 (GND)` | Warna Kabel: LG - BR — Sinyal suara (Kanan Belakang) | Mainkan sistem audio: - |
| `[AUDIO / VISUAL] R4-2 (RL+) - R3-7 (GND)` | Warna Kabel: P - BR — Sinyal suara (Kiri Belakang) | Mainkan sistem audio: - |
| `[AUDIO / VISUAL] R4-3 (RR-) - R3-7 (GND)` | Warna Kabel: LG-B - BR — Sinyal suara (Kanan Belakang) | Mainkan sistem audio: - |
| `[AUDIO / VISUAL] R4-6 (RL-) - R3-7 (GND)` | Warna Kabel: P-B - BR — Sinyal suara (Kiri Belakang) | Mainkan sistem audio: - |

---

## 3. Katalog Lengkap Prosedur Pemeriksaan Kode DTC (OBD-II & Flash Code)

### DTC `B0100` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 13] Hubung Pendek pada Sirkut Squib Sisi Pengemudi (Dokumen: RM0000017PL004X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkui
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B0101` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 14] Open Circuit pada Sirkut Squib Sisi Pengemudi (Dokumen: RM0000017PL004X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkui
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B0102` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 11] Hubung Pendek pada GND dalam Sirkut Squib Sisi Pengemudi (Dokumen: RM0000017PL004X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkui
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B0103` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 12] Hubung Pendek ke B+ dalam Sirkut Squib Sisi Pengemudi (Dokumen: RM0000017PL004X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan konektor kabel panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkui
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B1000` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 31] Malfungsi Sensor Airbag Tengah Assembly (Dokumen: RM000000YTI00SX)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag tengah assembly; Kondisi Deteksi: Malfungsi sensor airbag tengah assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> Bersihkan berbagai DTC yang tersimpan dalam memori (lihat halaman ). -> Putar switch pengapian ke OFF. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODA SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY

### DTC `B1100` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 31] Malfungsi Sensor Airbag Tengah Assembly (Dokumen: RM0000017Q9008X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag tengah assembly; Kondisi Deteksi: Malfungsi sensor airbag tengah assembly
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> Bersihkan berbagai DTC yang tersimpan dalam memori (Lihat halaman ). -> Putar switch pengapian ke OFF. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODA SIMULASI UNTUK MEMERIKSA
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY

### DTC `B1156` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 15] Malfungsi Sensor Airbag Depan RH (Dokumen: RM000002H74000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag depan RH Sensor airbag tengah assembly Kabel panel instrumen Kabel utama ruang mesin; Kondisi Deteksi: Sensor airbag tengah assembly menerima sinyal open atau short ke sinyal masa dalam sirkuit sensor airbag depan RH Malfungsi sensor airbag depan RH. Malfungsi sensor airbag tengah assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (SHORT KE MASA): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari sensor airbag tengah assembly dan sensor airbag depan RH. -> Ukur tahanan.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (OPEN ): Gunakan kabel servis, hubungkan terminal FSSR+ (A9-2) dan FSSR- (A9-1) dari konektor E. -> Ukur tahanan.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — 3. PERIKSA SENSOR AIRBAG DEPAN RH: Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Lepaskan konektor dari sensor airbag tengah assembly dan sensor airbag depan RH. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL UTAMA RUANG MESIN (SHORT KE MASA): Lepaskan konektor kabel utama ruang mesin dari kabel panel instrumen. -> Ukur tahanan.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL UTAMA RUANG MESIN (DARI OPEN CIRCUIT): Lepaskan konektor kabel utama ruang mesin dari kabel panel instrumen. -> Ukur tahanan.
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG DEPAN RH
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A10-9) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR- (A10-10) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A10-9) - FSSR- (A10-20) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A9-2) - FSSR-(A9-1) (Selalu)` : **738 sampai 902 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-2 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-1 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-1 - II1-2 (Selalu)` : **Di bawah 1 Ω**

### DTC `B1157` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 15] Malfungsi Sensor Airbag Depan RH (Dokumen: RM000002H74000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag depan RH Sensor airbag tengah assembly Kabel panel instrumen Kabel utama ruang mesin; Kondisi Deteksi: Sensor airbag tengah assembly menerima sinyal open atau short ke sinyal masa dalam sirkuit sensor airbag depan RH Malfungsi sensor airbag depan RH. Malfungsi sensor airbag tengah assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (SHORT KE MASA): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari sensor airbag tengah assembly dan sensor airbag depan RH. -> Ukur tahanan.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (OPEN ): Gunakan kabel servis, hubungkan terminal FSSR+ (A9-2) dan FSSR- (A9-1) dari konektor E. -> Ukur tahanan.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — 3. PERIKSA SENSOR AIRBAG DEPAN RH: Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Lepaskan konektor dari sensor airbag tengah assembly dan sensor airbag depan RH. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL UTAMA RUANG MESIN (SHORT KE MASA): Lepaskan konektor kabel utama ruang mesin dari kabel panel instrumen. -> Ukur tahanan.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL UTAMA RUANG MESIN (DARI OPEN CIRCUIT): Lepaskan konektor kabel utama ruang mesin dari kabel panel instrumen. -> Ukur tahanan.
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG DEPAN RH
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A10-9) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR- (A10-10) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A10-9) - FSSR- (A10-20) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A9-2) - FSSR-(A9-1) (Selalu)` : **738 sampai 902 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-2 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-1 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-1 - II1-2 (Selalu)` : **Di bawah 1 Ω**

### DTC `B1158` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 16] Front Airbag Sensor LH Malfunction (Dokumen: RM000002H75000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag depan LH Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Pada saat sensor airbag tegah asembly menerima sinyal open atau short ke sinyal masa dalam sirkuit sensor airbag depan LH. Malfungsi sensor airbag depan LH. Malfungsi sensor airbag tengah assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMENT PANEL (SHORT KE GROUND): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari sensor airbag depan LH. -> Ukur tahanan.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN (OPEN): Gunakan kabel servis, hubungkan terminal FSSL+ (A8-2) dan FSSL- (A8-1) dari konektor C. -> Ukur tahanan.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SENSOR AIRBAG DEPAN LH: Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Connect the connectors to the center airbag sensor assembly and the front airbag sensor LH. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG DEPAN LH
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODA SIMULASI UNTUK MEMERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A10-15) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL- (A10-26) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A10-15) - FSSL- (A10-26) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A8-2) - FSSL- (A8-1) (Selalu)` : **738 sampai 902 Ω**

### DTC `B1159` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (Tanpa Airbag Penumpang Depan) / Flash Code 16] Front Airbag Sensor LH Malfunction (Dokumen: RM000002H75000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag depan LH Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Pada saat sensor airbag tegah asembly menerima sinyal open atau short ke sinyal masa dalam sirkuit sensor airbag depan LH. Malfungsi sensor airbag depan LH. Malfungsi sensor airbag tengah assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMENT PANEL (SHORT KE GROUND): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari sensor airbag depan LH. -> Ukur tahanan.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN (OPEN): Gunakan kabel servis, hubungkan terminal FSSL+ (A8-2) dan FSSL- (A8-1) dari konektor C. -> Ukur tahanan.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SENSOR AIRBAG DEPAN LH: Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Connect the connectors to the center airbag sensor assembly and the front airbag sensor LH. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG DEPAN LH
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODA SIMULASI UNTUK MEMERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A10-15) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL- (A10-26) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A10-15) - FSSL- (A10-26) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A8-2) - FSSL- (A8-1) (Selalu)` : **738 sampai 902 Ω**

### DTC `B1600` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 15] Sisi R sensor mekanikal FR terjadi malfungsi (Dokumen: RM000002H7D000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag depan RH Sensor airbag tengah assembly Kabel panel instrumen Kabel utama ruang mesin; Kondisi Deteksi: Sensor airbag tengah assembly menerima sinyal open atau short ke sinyal masa dalam sirkuit sensor airbag depan RH Malfungsi sensor airbag depan RH. Malfungsi sensor airbag tengah assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (SHORT KE MASA): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari sensor airbag tengah assembly dan sensor airbag depan RH. -> Ukur tahanan.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SIRKUIT SENSOR AIRBAG DEPAN RH (OPEN ): Gunakan kabel servis, hubungkan terminal FSSR+ (A9-2) dan FSSR- (A9-1) dari konektor E. -> Ukur tahanan.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — 3. PERIKSA SENSOR AIRBAG DEPAN RH: Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Lepaskan konektor dari sensor airbag tengah assembly dan sensor airbag depan RH. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL UTAMA RUANG MESIN (SHORT KE MASA): Lepaskan konektor kabel utama ruang mesin dari kabel panel instrumen. -> Ukur tahanan.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL UTAMA RUANG MESIN (DARI OPEN CIRCUIT): Lepaskan konektor kabel utama ruang mesin dari kabel panel instrumen. -> Ukur tahanan.
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODA SIMULASI UNTUK MEMERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A10-12) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR- (A10-13) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A10-12) - FSSR- (A10-13) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSR+ (A9-2) - FSSR- (A9-1) (Selalu)` : **738 sampai 902 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-2 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-1 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: II1-1 - II1-2 (Selalu)` : **Di bawah 1 Ω**

### DTC `B1605` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 15] Sisi L sensor mekanikal FR malfungsi (Dokumen: RM000002H7F000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Sensor airbag depan LH Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Pada saat sensor airbag tegah asembly menerima sinyal open atau short ke sinyal masa dalam sirkuit sensor airbag depan LH. Malfungsi sensor airbag depan LH. Malfungsi sensor airbag tengah assembly.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN (SHORT KE MASA): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari sensor airbag depan LH. -> Ukur tahanan.
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL PANEL INSTRUMEN (OPEN): Gunakan kabel servis, hubungkan terminal FSSL+ (A8-2) dan FSSL- (A8-1) dari konektor C. -> Ukur tahanan.
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA SENSOR AIRBAG DEPAN LH: Ukur tahanan.
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Connect the connectors to the center airbag sensor assembly and the front airbag sensor LH. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG DEPAN LH
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GUNAKAN METODA SIMULASI UNTUK MEMERIKSA
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A10-14) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL- (A10-20) - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A10-14) - FSSL- (A10-20) (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: FSSL+ (A8-2) - FSSL- (A8-1) (Selalu)` : **738 sampai 902 Ω**

### DTC `B1800` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 13] Frontal collision squib tempat duduk depan short (Dokumen: RM000002H7C000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit -> Kembalikan
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B1801` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 14] Frontal collision squib tempat duduk depan open (Dokumen: RM000002H7C000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit -> Kembalikan
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B1802` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 11] Frontal collision squib tempat duduk depan short GND (Dokumen: RM000002H7C000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit -> Kembalikan
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B1803` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 12] Frontal collision squib tempat duduk depan short BATT (Dokumen: RM000002H7C000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Steering pad (squib sisi pengemudi) Kabel spiral Sensor airbag tengah assembly Kabel panel instrumen; Kondisi Deteksi: Short circuit pada squib sisi pengemudi. Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open circuit pada squib sisi pengemudi Malfungsi squib sisi pengemudi Malfungsi kabel spiral Malfungsi sensor airbag tengah assembl
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SQUIB SISI PENGEMUDI - KABEL SPIRAL): Putar switch pengapian ke LOCK. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan konektor dari steering pad -> Periksa konektor kabel spiral dan terminalnya (pada sisi steering pad
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA STEERING PAD (SQUIB SISI PENGEMUDI): Lepaskan konektor dari steering pad -> Hubungkan sisi kabel warna putih dari SST (tahanan 2,1Ω) ke konektor E. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tungg
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (KABEL SPIRAL - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor E. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi kabel spiral)
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL SPIRAL.: Lepaskan panel instrumen dari kabel spiral. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pendek dalam sirkuit -> Kembalikan
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag tengah assembly) dan periksa bahwa konektor telah dihubungkan dengan sempurna pada sensor airbag tengah assembly.
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor kabel panel instrumen dari sensor airbag tengah assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa dari hubung pe
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke steering pad, kabel spiral dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. 
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL SPIRAL
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D+ - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: D- - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D- - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: D+ - D- (Selalu)` : **1 MΩ atau lebih**

### DTC `B1805` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 53] Frontal collision squib tempat duduk penumpang short (Dokumen: RM000002H7E000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Airbag assembly penumpang depan (Sisi squib penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Short dalam Sirkut Squib Sisi Penumpang Depan Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open dalam sirkut squib sisi penumpang depan. Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (AIRBAG PENUMPANG DEPAN - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi airbag penumpang depan) dan periksa bahwa kone
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Lepaskan konektor dari airbag penumpang depan assembly. -> Hubungkan sisi kabel warna hitam dari SST (Tahanan 2,1Ω) ke konektor C. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengap
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor C. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor dari sensor airbag tengah assembly dan airbag penumpang depan assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> H
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-2 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-1 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-1 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **1 MΩ atau lebih**

### DTC `B1806` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 54] Frontal collision squib tempat duduk penumpang open (Dokumen: RM000002H7E000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Airbag assembly penumpang depan (Sisi squib penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Short dalam Sirkut Squib Sisi Penumpang Depan Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open dalam sirkut squib sisi penumpang depan. Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (AIRBAG PENUMPANG DEPAN - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi airbag penumpang depan) dan periksa bahwa kone
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Lepaskan konektor dari airbag penumpang depan assembly. -> Hubungkan sisi kabel warna hitam dari SST (Tahanan 2,1Ω) ke konektor C. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengap
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor C. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor dari sensor airbag tengah assembly dan airbag penumpang depan assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> H
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-2 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-1 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-1 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **1 MΩ atau lebih**

### DTC `B1807` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 51] Frontal collision squib tempat duduk penumpang GND short (Dokumen: RM000002H7E000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Airbag assembly penumpang depan (Sisi squib penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Short dalam Sirkut Squib Sisi Penumpang Depan Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open dalam sirkut squib sisi penumpang depan. Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (AIRBAG PENUMPANG DEPAN - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi airbag penumpang depan) dan periksa bahwa kone
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Lepaskan konektor dari airbag penumpang depan assembly. -> Hubungkan sisi kabel warna hitam dari SST (Tahanan 2,1Ω) ke konektor C. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengap
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor C. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor dari sensor airbag tengah assembly dan airbag penumpang depan assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> H
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-2 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-1 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-1 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **1 MΩ atau lebih**

### DTC `B1808` — [SUPPLEMENTAL RESTRAINT SYSTEM — SISTEM AIRBAG (dengan Airbag Penumpang Depan) / Flash Code 52] Frontal collision squib tempat duduk penumpang BATT short (Dokumen: RM000002H7E000X)
- **Tingkat Keparahan**: `CRITICAL`
- **Area Gangguan & Kondisi Deteksi**: [SUPPLEMENTAL RESTRAINT SYSTEM] Area Gangguan: Kabel panel instrumen Airbag assembly penumpang depan (Sisi squib penumpang depan) Sensor airbag tengah assembly; Kondisi Deteksi: Short dalam Sirkut Squib Sisi Penumpang Depan Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondisi Deteksi: Open dalam sirkut squib sisi penumpang depan. Malfungsi squib sisi penumpang depan. Malfungsi sensor airbag tengah assembly; Kondi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (AIRBAG PENUMPANG DEPAN - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi airbag penumpang depan) dan periksa bahwa kone
  - Langkah 2 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA AIRBAG PENUMPANG DEPAN (SQUIB SISI PENUMPANG DEPAN): Lepaskan konektor dari airbag penumpang depan assembly. -> Hubungkan sisi kabel warna hitam dari SST (Tahanan 2,1Ω) ke konektor C. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengap
  - Langkah 3 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KONEKTOR (SENSOR AIRBAG TENGAH ASSEMBLY - KABEL PANEL INSTRUMEN): Putar switch pengapian ke OFF. -> Lepaskan kabel terminal negatif (-) baterai dari baterai, dan tunggu minimal selama 90 detik. -> Lepaskan SST dari konektor C. -> Periksa konektor dan terminal kabel panel instrumen (pada sisi sensor airbag
  - Langkah 4 (SUPPLEMENTAL RESTRAINT SYSTEM) — PERIKSA KABEL INSTRUMEN PANEL: Lepaskan konektor dari sensor airbag tengah assembly dan airbag penumpang depan assembly. -> Periksa dari short circuit ke B+ -> Periksa dari open circuit dalam sirkuit -> Periksa dari adanya hubung pendek ke masa dalam sirkuit. -> Periksa 
  - Langkah 5 (SUPPLEMENTAL RESTRAINT SYSTEM) — PEMERIKSAAN SENSOR AIRBAG TENGAH ASSEMBLY: Hubungkan konektor ke airbag penumpang depan dan sensor airbag tengah assembly. -> Hubungkan kabel terminal negatif (-) ke baterai, dan tunggu minimal selama 2 detik. -> Putar switch pengapian ke ON, dan tunggu minimal selama 60 detik. -> H
  - Langkah 6 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI AIRBAG ASSEMBLY PENUMPANG DEPAN
  - Langkah 7 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI KABEL PANEL INSTRUMEN
  - Langkah 8 (SUPPLEMENTAL RESTRAINT SYSTEM) — GANTI SENSOR AIRBAG TENGAH ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-2 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Voltase standar: A13-1 - Masa bodi (Switch pengapian ON)` : **Di bawah 1 V**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **Di bawah 1 Ω**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-1 - Masa bodi (Selalu)` : **1 MΩ atau lebih**
  - `[SUPPLEMENTAL RESTRAINT SYSTEM] Tahanan standar: A13-2 - A13-1 (Selalu)` : **1 MΩ atau lebih**

### DTC `B2780` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 15] Switch Kunci OFF Malfungsi (Dokumen: RM000002L5P000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Sirkuit switch peringatan unlock open atau short Steering column upper bracket dengan/switch assembly (switch peringatan unlock) ECU kunci transponder assembly; Kondisi Deteksi: Dengan switch pengapian diset ke posisi ON, switch kunci OFF telah dideteksi selama 500 ms lebih
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA FUSE (HAZARD): Cabut fuse HAZARD dari kotak fuse. -> Ukur tahanan fuse HAZARD. -> Pasang kembali fuse HAZARD.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA STEERING COLUMN UPPER DENGAN/SWITCH BRACKET ASSEMBLY (SWITCH PERINGATAN UNLOCK): Lepaskan konektor switch peringatan unlock U1. -> Ukur tahanan dari konektor sisi switch. -> Hubungkan kembali konektor switch peringatan unlock.
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (SWITCH PERINGATAN UNLOCK - BATERAI): Lepaskan konektor switch peringatan unlock U1. -> Ukur voltase wire harness sisi konektor. -> Hubungkan kembali konektor switch peringatan unlock.
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ECU KUNCI TRANSPONDER ASSEMBLY - SWITCH PERINGATAN UNLOCK): Lepaskan konektor T14 ECU kunci transponder -> Lepaskan konektor switch peringatan unlock U1. -> Ukur tahanan pada wire harness sisi konektor. -> Hubungkan kembali switch peringatan unlock dan konektor ECU kunci transponder.
  - Langkah 5 (ENGINE IMMOBILISER) — GANTI ECU KUNCI TRANSPONDER ASSEMBLY
  - Langkah 6 (ENGINE IMMOBILISER) — GANTI FUSE
  - Langkah 7 (ENGINE IMMOBILISER) — GANTI STEERING COLUMN UPPER DENGAN/SWITCH BRACKET ASSEMBLY (SWITCH PERINGATAN UNLOCK)
  - Langkah 8 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: 1 - 2 (Didorong)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: 1 - 2 (Bebas)` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Voltage standar: U1-2 - Masa bodi` : **11 sampai 14 V**
  - `[ENGINE IMMOBILISER] Tahanan standar: KSW (T14-3) - U1-1` : **Di bawah 1 Ω**

### DTC `B2788` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 41] Kesalahan komunikasi (Code not coincident) (Dokumen: RM000002L5V000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: ECU kunci transponder assembly ECM Wire harness; Kondisi Deteksi: Pada saat kode tidak sesuai selama komunikasi dengan ECM; Kondisi Deteksi: Pada saat tidak ada respon yang diterima selama komunikasi dengan ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Pilih menu item berikut ini: Diagnosis / Body / Immobiliser / DTC -> Baca DTC.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ECU KUNCI TRANSPONDER -ECM): Lepaskan konektor E10 ECM. -> Lepaskan konektor T14 ECU kunci transponder -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor ECU kunci transponder.
  - Langkah 3 (ENGINE IMMOBILISER) — LAKUKAN PENDAFTARAN KUNCI: Hapus DTC. -> Reregister kunci (kode ID kunci)
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hidupkan mesin. -> Pilih menu item berikut ini: Diagnosis / Body / Immobiliser / DTC -> Baca DTC.
  - Langkah 5 (ENGINE IMMOBILISER) — GANTI ECU KUNCI TRANSPONDER ASSEMBLY
  - Langkah 6 (ENGINE IMMOBILISER) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hidupkan mesin. -> Pilih menu item berikut ini: Diagnosis / Body / Immobiliser / DTC -> Baca DTC.
  - Langkah 7 (ENGINE IMMOBILISER) — GANTI ECM
  - Langkah 8 (ENGINE IMMOBILISER) — PERIKSA PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Standar tahanan (Periksa keadaan open): SIO2 (T14-8) - SIO2 (E10-32)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Standar tahanan (Periksa keadaan short): SIO2 (T14-8) atau SIO2 (E10-32) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B2789` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 42] Kesalahan komunikasi (No reply) (Dokumen: RM000002L5V000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: ECU kunci transponder assembly ECM Wire harness; Kondisi Deteksi: Pada saat kode tidak sesuai selama komunikasi dengan ECM; Kondisi Deteksi: Pada saat tidak ada respon yang diterima selama komunikasi dengan ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Pilih menu item berikut ini: Diagnosis / Body / Immobiliser / DTC -> Baca DTC.
  - Langkah 2 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN KONEKTOR (ECU KUNCI TRANSPONDER -ECM): Lepaskan konektor E10 ECM. -> Lepaskan konektor T14 ECU kunci transponder -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor ECU kunci transponder.
  - Langkah 3 (ENGINE IMMOBILISER) — LAKUKAN PENDAFTARAN KUNCI: Hapus DTC. -> Reregister kunci (kode ID kunci)
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hidupkan mesin. -> Pilih menu item berikut ini: Diagnosis / Body / Immobiliser / DTC -> Baca DTC.
  - Langkah 5 (ENGINE IMMOBILISER) — GANTI ECU KUNCI TRANSPONDER ASSEMBLY
  - Langkah 6 (ENGINE IMMOBILISER) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hidupkan mesin. -> Pilih menu item berikut ini: Diagnosis / Body / Immobiliser / DTC -> Baca DTC.
  - Langkah 7 (ENGINE IMMOBILISER) — GANTI ECM
  - Langkah 8 (ENGINE IMMOBILISER) — PERIKSA PROBLEM INTERMITTENT
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Standar tahanan (Periksa keadaan open): SIO2 (T14-8) - SIO2 (E10-32)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Standar tahanan (Periksa keadaan short): SIO2 (T14-8) atau SIO2 (E10-32) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B2793` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 23] Kode ID Kunci tidak Terdaftar (Dokumen: RM000002L5S000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci ECU kunci transponder assembly (Koil kunci transponder) Wire harness; Kondisi Deteksi: Chip transponder malfungsi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Masukkan kunci kendaraan lain pada silinder kunci pengapian. -> Periksa apakah mesin dapat di-start dengan kunci tersebut.
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN CONNECTOR (ECU KUNCI TRANSPONDER ASSEMBLY - KOIL KUNCI TRANSPONDER): Lepaskan konektor T14 ECU kunci transponder -> Lepaskan konektor T13 koil kunci transponder -> Ukur tahanan pada wire harness sisi konektor. -> Hubungkan kembali ECU kunci transponder dan konektor amplifier kunci transponder.
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA KUNCI: Periksa apakah pengoperasian dapat dibuat dengan kunci yang normal.
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA START MESIN: Setelah penggantian koil kunci transponder dengan normal yang memfungsikan koil kunci transponder, periksa apakah mesin hidup.
  - Langkah 6 (ENGINE IMMOBILISER) — NORMAL (KOIL KUNCI TRANSPONDER RUSAK)
  - Langkah 7 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (ENGINE IMMOBILISER) — KUNCI PENGGANTI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(+) (T14-6) - ANT1 (T13-1)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(-) (T14-13) - ANT2 (T13-7)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (+) (T14-6) atau ANT1 (T13-1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (-) (T14-13) atau ANT2 (T13-7) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B2794` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 22] Unmatched Encryption Code (Dokumen: RM000002L5R000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci; Kondisi Deteksi: Pada saat kode ID kunci tidak bersesuaian selama komunikasi transponder
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — LAKUKAN PENDAFTARAN KUNCI: Hapus DTC (Lihat halaman ). -> Register ulang kunci dan masukkan kunci ke dalam silinder kunci pengapian. Periksa apakah mesin dapat di-start dengan kunci tersebut.
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 3 (ENGINE IMMOBILISER) — KUNCI PENGGANTI

### DTC `B2795` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 21] Unmatched Key Code (Dokumen: RM000002L5Q000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci; Kondisi Deteksi: Pada saat sistem dicoba untuk distart menggunakan kunci tak diregistrasi.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — LAKUKAN PENDAFTARAN KUNCI: Hapus DTC (Lihat halaman ). -> Register ulang kunci dan masukkan kunci ke dalam silinder kunci pengapian. Periksa apakah mesin dapat di-start dengan kunci tersebut.
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 3 (ENGINE IMMOBILISER) — KUNCI PENGGANTI

### DTC `B2796` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 12] Transponder / Koil Antena Malfungsi (Dokumen: RM000002L5O000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: (Koil kunci transponder) ECU kunci transponder assembly Wire harness; Kondisi Deteksi: Setelah koil immobiliser telah ditambah energi, tidak ada respon yang diterima dari kunci.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA KOIL KUNCI TRANSPONDER: Setelah penggantian koil kunci transponder dengan normal yang memfungsikan koil kunci transponder, periksa apakah mesin hidup.
  - Langkah 2 (ENGINE IMMOBILISER) — NORMAL (KOIL KUNCI TRANSPONDER RUSAK)
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN CONNECTOR (ECU KUNCI TRANSPONDER ASSEMBLY - KOIL KUNCI TRANSPONDER): Lepaskan konektor T14 ECU kunci transponder -> Lepaskan konektor T13 koil kunci transponder -> Ukur tahanan pada wire harness sisi konektor. -> Hubungkan kembali ECU kunci transponder dan konektor koil kunci transponder.
  - Langkah 4 (ENGINE IMMOBILISER) — GANTI ECU KUNCI TRANSPONDER ASSEMBLY
  - Langkah 5 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(+) (T14-6) - ANT1 (T13-1)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(-) (T14-13) - ANT2 (T13-7)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (+) (T14-6) atau ANT1 (T13-1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (-) (T14-13) atau ANT2 (T13-7) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B2797` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 24] Malfungsi Komunikasi No .1, Malfungsi Komunikasi Transponder (Dokumen: RM000002L5T000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci (Koil kunci transponder) ECU kunci transponder assembly Wire harness; Kondisi Deteksi: Komunikasi transponder rusak; [ENGINE IMMOBILISER] Area Gangguan: Key (Koil kunci transponder) ECU kunci transponder assembly Wire harness; Kondisi Deteksi: Pada saat semua data tidak dapat diterima dalam waktu yang telah ditentukan selama transponder
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Masukkan kunci kendaraan lain pada silinder kunci pengapian. -> Periksa apakah mesin dapat di-start dengan kunci tersebut.
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN CONNECTOR (ECU KUNCI TRANSPONDER ASSEMBLY - KOIL KUNCI TRANSPONDER): Lepaskan konektor T14 ECU kunci transponder -> Lepaskan konektor T13 koil kunci transponder -> Ukur tahanan pada wire harness sisi konektor. -> Hubungkan kembali ECU kunci transponder dan konektor amplifier kunci transponder.
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA KUNCI: Periksa apakah pengoperasian dapat dibuat dengan kunci yang normal.
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA START MESIN: Setelah penggantian koil kunci transponder dengan normal yang memfungsikan koil kunci transponder, periksa apakah mesin hidup.
  - Langkah 6 (ENGINE IMMOBILISER) — NORMAL (KOIL KUNCI TRANSPONDER RUSAK)
  - Langkah 7 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (ENGINE IMMOBILISER) — KUNCI PENGGANTI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(+) (T14-6) - ANT1 (T13-1)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(-) (T14-13) - ANT2 (T13-7)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (+) (T14-6) atau ANT1 (T13-1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (-) (T14-13) atau ANT2 (T13-7) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `B2798` — [ENGINE IMMOBILISER — SISTEM ENGINE IMMOBILISER / Flash Code 25] Malfungsi Komunikasi No .2, Komunikasi tidak Sempurna dengan Transponder (Dokumen: RM000002L5T000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [ENGINE IMMOBILISER] Area Gangguan: Kunci (Koil kunci transponder) ECU kunci transponder assembly Wire harness; Kondisi Deteksi: Komunikasi transponder rusak; [ENGINE IMMOBILISER] Area Gangguan: Key (Koil kunci transponder) ECU kunci transponder assembly Wire harness; Kondisi Deteksi: Pada saat semua data tidak dapat diterima dalam waktu yang telah ditentukan selama transponder
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (ENGINE IMMOBILISER) — PERIKSA SELAGI MESIN DI-START DENGAN KUNCI LAIN: Masukkan kunci kendaraan lain pada silinder kunci pengapian. -> Periksa apakah mesin dapat di-start dengan kunci tersebut.
  - Langkah 2 (ENGINE IMMOBILISER) — SELESAI
  - Langkah 3 (ENGINE IMMOBILISER) — PERIKSA HARNESS DAN CONNECTOR (ECU KUNCI TRANSPONDER ASSEMBLY - KOIL KUNCI TRANSPONDER): Lepaskan konektor T14 ECU kunci transponder -> Lepaskan konektor T13 koil kunci transponder -> Ukur tahanan pada wire harness sisi konektor. -> Hubungkan kembali ECU kunci transponder dan konektor amplifier kunci transponder.
  - Langkah 4 (ENGINE IMMOBILISER) — PERIKSA KUNCI: Periksa apakah pengoperasian dapat dibuat dengan kunci yang normal.
  - Langkah 5 (ENGINE IMMOBILISER) — PERIKSA START MESIN: Setelah penggantian koil kunci transponder dengan normal yang memfungsikan koil kunci transponder, periksa apakah mesin hidup.
  - Langkah 6 (ENGINE IMMOBILISER) — NORMAL (KOIL KUNCI TRANSPONDER RUSAK)
  - Langkah 7 (ENGINE IMMOBILISER) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (ENGINE IMMOBILISER) — KUNCI PENGGANTI
- **Spesifikasi Standar Multimeter**:
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(+) (T14-6) - ANT1 (T13-1)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL(-) (T14-13) - ANT2 (T13-7)` : **Di bawah 1 Ω**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (+) (T14-6) atau ANT1 (T13-1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[ENGINE IMMOBILISER] Tahanan standar: COIL (-) (T14-13) atau ANT2 (T13-7) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0105` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 31] Sirkuit Tekanan Absolute Manifold / Tekanan Barometric (Dokumen: RM000002ILL000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 31] Sirkuit Tekanan Absolute Manifold / Tekanan Barometric (Dokumen: RM000002ILL001X) | [SISTEM KONTROL MESIN K3-VE — SISTE
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Sensor tekanan absolut manifold ECM; [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Sensor tekanan absolut manifold ECM; [SISTEM KONTROL MESIN K3-VE] Area Gangguan: Open atau short circuit dalam sensor tekanan absolute manifold Sensor tekanan absolut manifold ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTAGE VCPM): Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTASE PIM): Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA WIRE HARNESS DAN KONEKTOR (SENSOR TEKANAN ABSOLUT MANIFOLD - ECM): Lepaskan konektor sensor tekanan absolut manifold V1. -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor tekanan absolut manifold. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR TEKANAN ABSOLUT MANIFOLD: Putar switch pengapian ke ON. -> Lepaskan selang vakum dari sensor tekanan absolut manifold. -> Hubungkan voltmeter antara terminal dari E8-23 (PIM) dan E8-12 (E2PM) pada sisi ECM, kemudian ukur output voltase dalam tekanan atmosfir. -> Gun
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI SENSOR TEKANAN ABSOLUT MANIFOLD
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA ECM (VOLTAGE VCPM): Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: VCPM (E8-22) - E2PM (E8-12)` : **4,5 sampai 5,5 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: PIM (E8-23) - E2PM (E8-12)` : **2,2 sampai 3,1 V (dibebaskan)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): VC (V1-3) - VCPM (E8-22)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): PIM (V1-2 ) - PIM (E8-23)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): E2 (V1-1) - E2PM (E8-12)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): VC (V1-3) atau VCPM (E8-22) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): PIM (V1-2) atau PIM (E8-23) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): E2 (V1-1) atau E2PM (E8-12) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0110` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 43] Sirkuit Intake Air Temperature Malfungsi (Dokumen: RM000002ILN000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 43] Malfungsi Sirkuit Temperatur Udara Intake (Dokumen: RM000002ILN001X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 43] Sirk
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short di sirkuit sensor temperatur udara intake Sensor temperatur udara intake ECM; [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short di sirkuit sensor temperatur udara intake Sensor temperatur udara masuk ECM; [SISTEM KONTROL MESIN K3-VE] Area Gangguan: Open atau short di sirkuit sensor temperatur udara intake Sensor temperatur udara intake ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTAGE THA): Putar switch pengapian ke ON. -> Ukur voltase antara terminal THA dan E2 dari konektor E8 ECM.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR TEMPERATUR UDARA MASUK: Lepas sensor temperatur udara masuk. -> Ukur tahanan sensor temperatur udara intake
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - SENSOR TEMPERATUR UDARA INTAKE): Lepaskan konektor ECM E8. -> Lepaskan konektor I7 sensor temperatur udara intake. -> Periksa tahanan. -> Hubungkan kembali konektor sensor temperatur udara intake -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI SENSOR TEMPERATUR UDARA INTAKE
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA ECM (VOLTAGE THA): Putar switch pengapian ke ON. -> Ukur voltase antara terminal THA dan E2 dari konektor E8 ECM.
  - Langkah 2 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA SENSOR TEMPERATUR UDARA MASUK: Lepas sensor temperatur udara masuk. -> Ukur tahanan sensor temperatur udara intake
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: 20°C (20,00°C)` : **0,5 sampai 3,4 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: 60°C (60,00°C)` : **0,2 sampai 1,0 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **2,21 sampai 2,69 kΩ pada 20 °C ( 68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **0,29 sampai 0,354 kΩ pada 80 °C ( 80,00°C)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): THA (E8-13) - THA (I7-1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): E2 (E8-30) - E2 (I7-2)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): THA (E8-13) atau THA (I7-1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Voltase standar: 20°C (68°F)` : **0,5 sampai 3,4 V**

### DTC `P0115` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 42] Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000002ILM000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 42] Sirkuit Temperatur Cairan Pendingin Mesin (Dokumen: RM000002ILM001X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 42] Sir
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short circuit dalam sensor temperatur cairan pendingin mesin Sensor temperatur cairan pendingin mesin ECM; Kondisi Deteksi: Open atau short dalam sirkuit sensor temperatur cairan pendingin mesin selama 0,5 detik atau lebih (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short circuit dalam sensor temperatur cairan pendingin mesin Sensor temperatur cairan pen
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTAGE THW): Panaskan mesin sampai pada temperatur kerja normal. -> Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN: Ukur tahanan sensor temperatur cairan pendingin mesin.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN): Lepaskan konektor sensor temperatur cairan pendingin mesin W1 -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor temperatur cairan pendingin mesin. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA ECM (VOLTAGE THW): Panaskan mesin sampai pada temperatur kerja normal. -> Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
  - Langkah 2 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN: Ukur tahanan sensor temperatur cairan pendingin mesin.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: THW (E8-19) - E2 (E8-30)` : **0,2 sampai 1,0 V (Temperatur cairan pendingin mesin 60° sampai 120°C (140° sampai 248 °F))**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **2,29 sampai 2,6 kΩ pada 20°C ( 68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **0,3017 sampai 0,3269 kΩ pada 80°C ( 80,00°C)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar (Periksa dari open):: THW (W1-1) atau THW (E8-19)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar (Periksa dari open):: E2 (W1-2) - E2 (E8-30)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar (Periksa dari short):: THW (W1-1) atau THW (E8-19) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Voltase standar: THW (E8-19) - E2 (E8-30)` : **0,2 sampai 1,0 V (Temperatur cairan pendingin mesin 60° sampai 120°C (140° sampai 248 °F))**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar: 1 - 2]` : **2,29 sampai 2,59 kΩ pada 20°C (68°F)**

### DTC `P0120` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 41] Malfungsi Sirkuit Sensor Posisi Pedal Throttle / Switch "A" (Dokumen: RM000002ILJ000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 41] Malfungsi Sirkuit Sensor Posisi Pedal Throttle / Switch "A" (Dokumen: RM000002ILJ001X) | [SISTEM KONTROL MESIN K3-
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sensor posisi throttle Sensor posisi throttle ECM; Kondisi Deteksi: Setelah mesin dihidupkan, output voltase dari sensor posisi throttle di bawah 0,2 V atau di atas 4,8 V selama lebih dari 0,5 detik. (1 trip pendeteksian logis); Kondisi Deteksi: Area Gangguan; [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Terbuka Penuh; [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open di s
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (POSISI THROTTLE): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan intelligent tester ON. -> Pilih menu item berikut ini: Powertrain / Engine / Data List / Throttle POS. -> Baca nilai yang ditampilkan pada intelligent tester
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR POSISI THROTTLE: Lepaskan konektor sensor posisi throttle T1 -> Ukur tahanan antara terminal-terminal dari sensor posisi throttle. -> Hubungkan kembali konektor sensor posisi throttle.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - SENSOR POSISI THROTTLE): Lepaskan konektor sensor posisi throttle T1 -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor posisi throttle. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR POSISI THROTTLE: Lepaskan konektor sensor posisi throttle T1 -> Ukur tahanan antara terminal-terminal dari sensor posisi throttle. -> Hubungkan kembali konektor sensor posisi throttle.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - SENSOR POSISI THROTTLE): Lepaskan konektor sensor posisi throttle T1 -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor posisi throttle. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI SENSOR POSISI THROTTLE
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: VC (T1-1) - E2 (T1-2) (-)` : **2,5 sampai 6,0 kΩ**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: VTA (T1-3) - E2 (T1-2) (Tertutup penuh)` : **0,3 sampai 5,8 kΩ**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: VTA (T1-3) - E2 (T1-2) (Terbuka penuh)` : **1,98 sampai 9,16 kΩ**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): VC (E8-10) - VC (T1-1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): VTH (E8-20) - VTA (T1-3)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): E2 (E8-30) - E2 (T1-2)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): VC (E8-10) atau VC (T1-1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): VTH (E8-20) atau VTA (T1-3) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0130` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 21] Sirkuit Sensor Oksisgen (Bank 1 Sensor 1) (Dokumen: RM000002ILK000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 21] Sirkuit Sensor Oksisgen (Bank 1 Sensor 1) (Dokumen: RM000002ILK001X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 21] Sir
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short di sirkuit sensor heated oxygen ( sensor 1) Sensor heated oxygen ( sensor 1) Pemanas sensor heated oxygen ( sensor 1) ECM; Kondisi Deteksi: Output voltase dari sensor heated oxygen tetap sekitar 0,08 V saat kendaraan dikendarai pada 40 km/jam (25 mph) atau lebih setelah mesin dipanaskan (2 trip detection logic); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit s
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR HEATED OXYGEN (OUTPUT VOLTASE SENSOR 1 ): Menggunakan intelligent tester: -> Tidak menggunakan intelligent tester:
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SELANG VENTILASI
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER ): Lepaskan konektor sensor heated oxygen H11. -> Ukur tahanan antara terminal-terminal dari konektor sensor heated oxygen. -> Hubungkan kembali konektor sensor heated oxygen.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (HEATED OXYGEN SENSOR - ECM): Lepaskan konektor sensor heated oxygen H11. -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor heated oxygen. -> Hubungkan kembali konektor ECM.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SISTEM INDUKSI UDARA: Periksa kebocoran vakum dalam sistem induksi udara.
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA TEKANAN BAHAN BAKAR: Pasang tekanan bahan bakar.
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA PERCIKAN/SPARK DAN PENGAPIAN: Periksa sistem pengapian.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (HT) - 2 (+B)` : **Dengan sensor oksigen (Sensor 2): 5,0 sampai 7 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (HT) - 2 (+B)` : **Tanpa sensor oksigen (sensor 2): 11,7 sampai 15,5 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 2 (+B) - 4 (E1)` : **1 MΩ atau lebih**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): OX (H11-3) - OX1 (E8-2)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): HT (H11-1) - OXH1 (E8-8)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): E1 (H11-4) - E2 (E8-30)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): OX (H11-3) atau OX1 (E8-2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): HT (H11-1) atau OXH1 (E8-8) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0135` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 23] Sirkuit Heater Sensor O2 (Bank 1 Sensor 1) (Dokumen: RM000002ILO000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 23] Sirkuit Heater Sensor O2 (Bank 1 Sensor 1) (Dokumen: RM000002ILO001X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 23] S
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit heater dari sensor heated oxygen (sensor 1) Sensor heated oxygen ( sensor 1) ECM; Kondisi Deteksi: Open atau short dalam sirkuit heater pada sensor oksigen dari 1,280 detik atau lebih (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit heater dari sensor oksigen Sensor heated oxygen (sensor 1) ECM; Kondisi Deteksi: Open at
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER ): Lepaskan konektor sensor heated oxygen H11. -> Ukur tahanan antara terminal-terminal dari konektor sensor heated oxygen. -> Hubungkan kembali konektor sensor heated oxygen.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTASE OXH1): Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (HEATED OXYGEN SENSOR - ECM): Periksa harness dan konektor antara ECM dan konektor sensor heated oxygen.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI HEATED OXYGEN SENSOR
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA SENSOR HEATED OXYGEN (TAHANAN HEATER ): Lepaskan konektor sensor heated oxygen H11. -> Ukur tahanan antara terminal-terminal dari konektor sensor heated oxygen. -> Hubungkan kembali konektor sensor heated oxygen.
  - Langkah 2 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA ECM (VOLTASE OXH1): Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (HT) - 2 (+B)` : **Dengan sensor oksigen (Sensor 2): 5,0 sampai 7 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (HT) - 2 (+B)` : **Tanpa sensor oksisgen (sensor 2): 11,7 sampai 15,5 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 2 (+B) - 4 (E1)` : **1 MΩ atau lebih**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: OXH1 (E8-8) - E2 (E8-30)` : **8 sampai 14 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): HT (H11-1) - OXH1 (E8-8)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): HT (H11-1) atau OXH1 (E8-8) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar: 1 (HT) - 2 (+B)` : **11,7 sampai 15,5 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar: 2 (+B) - 4 (E1)` : **1 MΩ atau lebih**

### DTC `P0136` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 22] Sirkuit Sensor O2 (Bank 1 Sensor 2) (Dokumen: RM000002ILP000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sensor oksigen (sensor 2) Sensor oksigen (sensor 2) ECM; Kondisi Deteksi: Setelah mesin dipanaskan, output voltase dari sensor oksigen tetap pada 0,6 V, atau kurang dari 0,1 V. (2 trip pendeteksian logis)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan intelligent tester ON. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — BACA NILAI MENGGUNAKAN INTELLIGENT TESTER (OUTPUT VOLTASE SENSOR OKSIGEN): Hubungkan intelligent tester ke DLC3. -> Start mesin dan hidupkan intelligent tester. -> Pilih menu item berikut ini: Powertrain / Engine / Data List / O2S B1 S2. -> Setelah memanaskan mesin, hidupkan mesin dengan kecepatan 2,500 rpm selama
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR OKSIGEN - ECM): Lepaskan konektor sensor oksigen 07. -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor oksigen. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — LAKUKAN KONFIRMASI POLA PENGENDARAAN
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan intelligent tester ON. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI SENSOR OKSIGEN
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar (Periksa dari open):: OX (O7-1) - OX2 (E8-1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar (Periksa dari open):: E1 (O7-2) - E2 (E8-30)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar (Periksa dari short):: OX (O7-1) atau OX2 (E8-1) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0171` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 25] Sistem Terlalu Kurus (Malfungsi A/F Kurus, Bank 1) (Dokumen: RM000002IL1001X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 25] Sistem Terlalu Kurus (Malfungsi A/F Kurus, Bank 1) (Dokumen: RM000002IL1002X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Sistem induksi udara Injektor tersumbat Sensor tekanan absolut manifold Sensor temperatur cairan pendingin mesin Tekanan bahan bakar Kebocoran gas pada sistem exhaust Open atau short di sirkuit sensor heated oxygen ( sensor 1) Sensor heated oxygen ( sensor 1) Selang ventilasi ECM; Kondisi Deteksi: Bila feedback rasio udara-bahan bakar stabil setelah pemanasan mesin, fuel trim mempertimbangkan adanya ke
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester ke-ON. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SELANG VENTILASI
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SISTEM INDUKSI UDARA: Periksa kebocoran vakum dalam sistem induksi udara.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR TEKANAN ABSOLUT MANIFOLD: Putar switch pengapian ke ON. -> Lepaskan selang vakum dari sensor tekanan absolut manifold. -> Hubungkan voltmeter antara terminal dari ECM, kemudian ukur output voltase dalam tekanan atmosfir. -> Gunakan pompa vakum, ukur penurunan voltas
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN: Lepas sensor temperatur pendingin mesin. -> Ukur tahanan sensor. -> Pasang kembali sensor temperatur pendingin mesin.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA PERCIKAN/SPARK DAN PENGAPIAN: Periksa sistem pengapian.
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA TEKANAN BAHAN BAKAR: Pasang tekanan bahan bakar.
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA FUEL INJECTOR ASSY (INJECTION DAN VOLUME): Periksa semprotan injektor dan volume injeksi.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: PIM (E8-23) - E2PM (E8-12)` : **2,2 sampai 3,1 V Dalam tekanan atmosfir (*1)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Penurunan voltase): 13,3 (100, 3,94) kPa (mmHg, in.Hg)` : **0,25 sampai 0,55 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Penurunan voltase): 26,7 (200, 7,87) kPa (mmHg, in.Hg)` : **0,65 sampai 0,95 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Penurunan voltase): 40,0 (300, 11,81) kPa (mmHg, in.Hg)` : **1,05 sampai 1,35 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Kenaikan voltase): 19,6 (0,20, 2,84) kPa (kgf/cm 2 , psi)` : **0,45 sampai 0,75 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **2,29 sampai 2,6 kΩ pada 20°C ( 68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **0,3017 sampai 0,3269 kΩ pada 80°C ( 80,00°C)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (HT) - 2 (+B)` : **Dengan sensor oksigen (Sensor 2): 5,0 sampai 7 Ω pada 20°C (68°F)**

### DTC `P0172` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 26] Sistem Terlalu Gemuk (Malfungsi A/F Gemuk, Bank 1) (Dokumen: RM000002IL1001X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 26] Sistem Terlalu Gemuk (Malfungsi A/F Gemuk, Bank 1) (Dokumen: RM000002IL1002X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Sistem induksi udara Injektor tersumbat Sensor tekanan absolut manifold Sensor temperatur cairan pendingin mesin Tekanan bahan bakar Kebocoran gas pada sistem exhaust Open atau short di sirkuit sensor heated oxygen ( sensor 1) Sensor heated oxygen ( sensor 1) Selang ventilasi ECM; Kondisi Deteksi: Bila feedback rasio udara-bahan bakar stabil setelah pemanasan mesin, fuel trim mempertimbangkan adanya ke
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester ke-ON. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SELANG VENTILASI
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SISTEM INDUKSI UDARA: Periksa kebocoran vakum dalam sistem induksi udara.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR TEKANAN ABSOLUT MANIFOLD: Putar switch pengapian ke ON. -> Lepaskan selang vakum dari sensor tekanan absolut manifold. -> Hubungkan voltmeter antara terminal dari ECM, kemudian ukur output voltase dalam tekanan atmosfir. -> Gunakan pompa vakum, ukur penurunan voltas
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR TEMPERATUR CAIRAN PENDINGIN MESIN: Lepas sensor temperatur pendingin mesin. -> Ukur tahanan sensor. -> Pasang kembali sensor temperatur pendingin mesin.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA PERCIKAN/SPARK DAN PENGAPIAN: Periksa sistem pengapian.
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA TEKANAN BAHAN BAKAR: Pasang tekanan bahan bakar.
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA FUEL INJECTOR ASSY (INJECTION DAN VOLUME): Periksa semprotan injektor dan volume injeksi.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: PIM (E8-23) - E2PM (E8-12)` : **2,2 sampai 3,1 V Dalam tekanan atmosfir (*1)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Penurunan voltase): 13,3 (100, 3,94) kPa (mmHg, in.Hg)` : **0,25 sampai 0,55 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Penurunan voltase): 26,7 (200, 7,87) kPa (mmHg, in.Hg)` : **0,65 sampai 0,95 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Penurunan voltase): 40,0 (300, 11,81) kPa (mmHg, in.Hg)` : **1,05 sampai 1,35 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Kenaikan voltase): 19,6 (0,20, 2,84) kPa (kgf/cm 2 , psi)` : **0,45 sampai 0,75 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **2,29 sampai 2,6 kΩ pada 20°C ( 68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **0,3017 sampai 0,3269 kΩ pada 80°C ( 80,00°C)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (HT) - 2 (+B)` : **Dengan sensor oksigen (Sensor 2): 5,0 sampai 7 Ω pada 20°C (68°F)**

### DTC `P0325` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 18] Sirkuit Sensor Knock 1 (Dokumen: RM000002NSI000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 18] Sirkuit Sensor Knock 1 (Dokumen: RM000002NSI001X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 18] Sirkuit Sensor Knock 1 (Dokumen: RM000002
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sensor knock Knock sensor (kendor atau under-torqued) ECM; Kondisi Deteksi: Pada saat sensor knock terjadi open atau shorted selama 2 detik atau lebih selagi mesin berputar 2.000 rpm atau lebih dan tekanan intake manifold 350 mmHg atau lebih. (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit sensor knock Knock sensor (ke
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (OUTPUT VOLTASE SENSOR): Start mesin dan panaskan mesin. -> Hubungkan oscilloscope probes ke terminal KNK dan terminal E2 dari ECM. -> Periksa bentuk gelombang saat mesin idling atau dinaikkan putarannya.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (SENSOR KNOCK - ECM): Lepaskan konektor sensor knock K1 -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTAGE TERMINAL KNK): Lepaskan konektor sensor knock K1 -> Putar switch pengapian ke ON. -> Ukur voltase antar terminal ECM. -> Hubungkan kembali konektor sensor .
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA KNOCK SENSOR (INSTALASI SENSOR): Periksa pemasangan sensor knock.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA KNOCK SENSOR (TAHANAN SENSOR): Lepas sensor knock. -> Ukur tahanan antar terminal sensor. -> pasang kembali sensor knock.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI KNOCK SENSOR
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester ke-ON. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): + (K1-2) - KNK (E8-31)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): - (K1-1) - E2 (E8-30)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): + (K1-2) atau KNK (E8-31) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: KNK (E8-31) - E2 (E8-30)` : **4,5 sampai 5,5 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: +(2) - -(1)` : **120 sampai 280 kΩ pada 20°C ( 68°F)**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): Knock sensor (K1-1) - KNK (E8-31)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari short):: Knock sensor (K1-1) atau KNK (E8-31) - Masa bodi` : **10 kΩ atau lebih**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar: 1 - Bodi` : **10 kΩ atau lebih**

### DTC `P0335` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 13] Malfungsi Sirkuit "A" Sensor Posisi Crankshaft (Dokumen: RM000002IKX001X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 13] Malfungsi Sirkuit "A" Sensor Posisi Crankshaft (Dokumen: RM000002IKX002X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Co
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sensor posisi crankshaft Sensor posisi crankshaft Plat sensor posisi crankshaft No.1 ECM; Kondisi Deteksi: Selama cranking, sinyal N1 tidak di-input ke ECM selama 2 detik (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit sensor posisi crankshaft Sensor posisi crankshaft Plat sensor posisi crankshaft No.1 ECM; Kondisi Det
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (OUTPUT VOLTASE SENSOR): Hubungkan oscilloscope probes ke terminal N1+ dan terminal N1- dari konektor ECM. -> Periksa bentuk gelombang saat mesin idling atau cranking.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR POSISI CRANKSHAFT (TAHANAN SENSOR): Lepaskan konektor sensor posisi crankshaft C2. -> Ukur tahanan sensor posisi crankshaft. -> Hubungkan kembali konektor sensor posisi crankshaft.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (CRANKSHAFT POSITION SENSOR- ECM): Lepaskan konektor sensor posisi crankshaft C2. -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor posisi crankshaft. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR POSISI CRANKSHAFT (PEMASANGAN SENSOR): Periksa pemasangan sensor posisi crankshaft.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA PLAT SENSOR POSISI CRANKSHAFT NO.1: Periksa gigi sensor plate.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI PLAT SENSOR POSISI CRANKSHAFT NO.1
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI SENSOR POSISI CRANKSHAFT
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] PERIKSA SENSOR POSISI CRANKSHAFT (TAHANAN SENSOR): 1 (+) - 2 (-)` : **1.850 sampai 2.450 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): + (C2-1) - N1+ (E8-11)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): - (C2-2) - N1- (E8-21)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): + (C2-1) atau N1+ (E8-11) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): - (C2-2) atau N1- (E8-21) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar: 1 (+) - 2 (-)` : **1.850 sampai 2.450 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): + (C2-1) - N1+ (E8-11)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): - (C2-2) - N1- (E8-21)` : **Di bawah 1 Ω**

### DTC `P0340` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 14] Sirkuit Sensor Posisi Camshaft "A" (Bank 1 atau Single Sensor) (Dokumen: RM000002IKY001X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 14] Sirkuit "A" Sensor Posisi Camshaft (Bank 1 atau Single Sensor) (Dokumen: RM000002IKY002X) | [SISTEM KONTROL MES
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sensor posisi camshaft Sensor Posisi Camshaft Camshaft (timing rotor) ECM; Kondisi Deteksi: Setelah mesin dihidupkan, tidak terdapat input sinyal dari sensor posisi camshaft selama 2 detik atau lebih (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit sensor posisi camshaft Sensor posisi camshaft Camshaft (timing rotor) EC
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (OUTPUT VOLTASE SENSOR): Hubungkan oscilloscope probes ke terminal N1+ dan terminal N1- dari konektor ECM. -> Periksa bentuk gelombang saat mesin idling atau cranking.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR POSISI CAMSHAFT (TAHANAN SENSOR): Lepaskan konektor sensor posisi camshaft C1. -> Ukur tahanan sensor posisi camshaft. -> Hubungkan kembali konektor sensor posisi camshaft.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (CAMSHAFT POSITION SENSOR- ECM): Lepaskan konektor sensor posisi camshaft C1. -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor sensor posisi camshaft. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR POSISI CAMSHAFT (PEMASANGAN SENSOR): Periksa pemasangan sensor posisi camshaft.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA CAMSHAFT (TIMING ROTOR): Periksa gigi timing rotor.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI SENSOR POSISI CAMSHAFT
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (+) - 2 (-)` : **1.850 sampai 2.450 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): + (C1-1) - N2+ (E8-18)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): - (C1-2) - N2- (E8-28)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): + (C1-1) or N2+ (E8-18) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): - (C1-2) atau N2- (E8-28) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar: 1 (+) - 2 (-)` : **950 sampai 1,250 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): + (C1-1) - N2+ (E8-18)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): - (C1-2) - N2- (E8-28)` : **Di bawah 1 Ω**

### DTC `P0350` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 16] Koil Pengapian "A" Utama / Sirkuit Sekunder (Dokumen: RM000002IKZ001X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 16] Sirkuit Primer/ Sekunder "A" Koil Pengapian (Dokumen: RM000002IKZ002X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 16]
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit IG (1 sampai 4) Koil pengapian assembly No. 1 sampai No. 4 ECM; Kondisi Deteksi: Open dalam sirkuit IG1 sampai 4 dari koil pengapian assembly ke ECM (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit IG (1 sampai 3) Koil pengapian assembly No. 1 sampai No. 3 ECM; Kondisi Deteksi: Open dalam sirkuit IG1 sampai 3 dari koil 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (COIL PENGAPIAN - ECM): Lepaskan ignition coil I2, I3, I4 dan/atau I6 dan konektor koil pengapian assembly. -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor koil pengapian assembly
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA KOIL PENGAPIAN (CATU DAYA): Lepaskan ignition coil I2, I3, I4 dan/atau I6 dan konektor koil pengapian assembly. -> Periksa tahanan. -> Putar switch pengapian ke ON. -> Ukur voltase antara terminal wire harness sisi konektor . -> Hubungkan kembali konektor koil pengapi
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (IG1 - SINYAL IG4 ): Hubungkan oscilloscope probes ke terminal IG1 (IG2, IG3 dan/atau IG4) dan terminal E1 dari konektor ECM. -> Periksa bentuk gelombang saat mesin idling atau cranking.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR (KOIL PENGAPIAN - SWITCH PENGAPIAN, KOIL PENGAPIAN - MASA BODI)
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI KOIL PENGAPIAN
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA HARNESS DAN KONEKTOR (COIL PENGAPIAN - ECM): Lepaskan ignition coil I2, I3, dan/atau I4 dan konektor koil pengapian assembly. -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor koil pengapian assembly
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Koil pengapian No. 1 (I2-3) - IG1 (E8-17)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Koil pengapian No. 2 (I3-3) - IG2 (E8-27)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Koil pengapian No. 3 (I4-3) - IG3 (E8-34)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Koil pengapian No. 4 (I6-3) - IG4 (E8-16)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Koil pengapian No. 1 (I2-3) atau IG1 (E8-17) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Koil pengapian No. 2 (I3-3) atau IG2 (E8-27) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Koil pengapian No.3 (I4-3) atau IG3 (E8-34) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Koil pengapian No. 4 (I6-3) atau IG4 (E8-16) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0443` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 76] Malfungsi pada Sirkuit Purge Control Valve Sistem Evaporative Emission Control (Dokumen: RM000002NGW000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 76] Malfungsi pada Sirkuit Purge Control Valve Sistem Evaporative Emission Control (Dokumen: RM0000
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short pada sirkuit vacuum switching valve (EVAP). Vacuum switching valve (EVAP) ECM; Kondisi Deteksi: Malfungsi dalam sirkuit vacuum switching valve (EVAP) secara kontinu selama 10 detik atau lebih dalam pengoperasian kontrol purge* (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short pada sirkuit vacuum switching valve (EVAP). Vacuum switching valve (EVAP)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — LAKUKAN ACTIVE TEST MENGGUNAKAN INTELLIGENT TESTER (EVAP VSV): Hubungkan selang vakum ke vacuum switching valve (sisi canister). -> Hubungkan intelligent tester ke DLC3. -> Start mesin dan hidupkan intelligent tester. -> Pilih menu item berikut ini: Powertrain / Engine / Active Test / EVAP VSV. -> Laku
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTAGE PRG): Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E8 ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA VACUUM SWITCHING VALVE (EVAP): Lepas vacuum switching valve. -> Periksa tahanan vacuum switching valve. -> Periksa kerja vacuum switching valve. -> Pasang kembali vacuum switching valve
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (VSV (EVAP) - ECM): Lepaskan konektor ECM E8. -> Lepas konektor vacuum switching valve V3. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor vacuum switching valve.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (RELAY EFI- VSV (EVAP)): Lepas relay EFI dari kotak fuse. -> Lepas konektor vacuum switching valve V3. -> Periksa tahanan. -> Pasang kembali relay EFI. -> Hubungkan kembali konektor vacuum switching valve.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SIRKUIT SUMBER DAYA ECM
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI VACUUM SWITCHING VALVE (EVAP)
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar: VSV ON` : **Memberikan hisapan pada jari Anda**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar: VSV OFF` : **Tidak memberikan hisapan pada jari Anda**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: PRG (E8-9) - E01 (E8-3)` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 - 2` : **30 sampai 34 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Vacuum switching valve (V3-1) - PRG (E8-9)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Vacuum switching valve (V3-1) atau PRG (E8-9) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Vacuum switching valve (V3-2) - relay EFI (5)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Vacuum switching valve (V3-2) atau relay EFI (5) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0500` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 52] Sensor Kecepatan Kendaraan (Dokumen: RM000002NP6000X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 52] Sensor Kecepatan Kendaraan (Dokumen: RM000002NP6001X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 52] Sensor Kecepatan Kendaraan (Dokum
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sensor kecepatan Sirkuit speedometer (Meter kombinasi, ECU kontrol transmisi) ECM; Kondisi Deteksi: Selama deselerasi, kecepatan kendaraan 0 km/jam (0 mph) selama lebih dari 3 detik walaupun putaran mesin 500 sampai 4.000 rpm di bawah kontrol pemutusan bahan bahan bakar (fuel cut) (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dala
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA COMBINATION METER ASSEMBLY (CARA KERJA SPEEDOMETER): Jalankan kendaraan dan periksa cara kerja speedometer normal di combination meter.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (SPD VOLTAGE): Pindahkan tuas pemindah gigi ke posisi netral. -> Dongkrak keatas roda belakang -> Putar switch pengapian ke ON. -> Putar perlahan roda belakang, dan ukur voltage dari konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR ( METER KOMBINASI ASSEMBLY - ECM): Lepas konektor C4 atau C8 meter kombinasi. -> Lepaskan konektor E10 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor meter kombinasi assembly. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — MENGGANTI METER KOMBINASI ASSEMBLY
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SIRKUIT SPEEDOMETER (METER DAN SISTEM GAUGE)
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA COMBINATION METER ASSEMBLY (CARA KERJA SPEEDOMETER): Jalankan kendaraan dan periksa cara kerja speedometer normal di combination meter.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: SPD (E10-18) - E1 (E8-29)` : **Voltase timbul sebentar-sebentar**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): M/T: SPSR (C4-10) - SPD (E10-18)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): A/T: SPSR (C8-13) - SPD (E10-18)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): M/T: SPSR (C4-10) atau SPD (E10-18) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): A/T: SPSR (C8-13) atau SPD (E10-18) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Voltase standar: SPD (E10-18) - E1 (E8-29)` : **Voltase dibangkitkan secara terputus-putus**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): SPSR (C4-10) - SPD (E10-18)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari short):: SPSR (C4-10) atau SPD (E10-18) - Masa bodi` : **10 kΩ atau lebih**

### DTC `P0505` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 71] Sistem kontrol Idle Malfungsi (Dokumen: RM000002IL9002X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 71] Malfungsi pada Sistem Kontrol Idle (Dokumen: RM000002IL9000X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 71] Sistem kontrol Idle Ma
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit katup Idle Speed Control (ISC) Katup ISC macet pada posisi terbuka atau tertutup ECM; Kondisi Deteksi: Terjadi ketidak normalan (open atau short) dalam sinyal aktuasi ISC. (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit katup Idle Speed Control (ISC) Katup Idle speed control (ISC) macet terbuka atau tertutup. ECM; Kond
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA PUTARAN IDLE MESIN: Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin. -> Ukur putaran mesin.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (KATUP ISC - ECM): Lepaskan konektor I1 katup Idle Speed Control (ISC). -> Lepaskan konektor ECM E8. -> Periksa tahanan. -> Hubungkan kembali konektor katup ISC. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA KATUP IDLE SPEED CONTROL ASSEMBLY: Lepaskan konektor I1 katup Idle Speed Control (ISC). -> Ukur tahanan antara terminal dari konektor katup ISC. -> Hubungkan kembali konektor katup ISC.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI KATUP IDLE SPEED CONTROL ASSEMBLY
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA PROBLEM INTERMITTENT
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA PUTARAN IDLE MESIN: Hubungkan intelligent tester ke DLC3. -> Hidupkan mesin -> Ukur putaran mesin.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): ISA1 (I1-3) - IACAHI (E8-15)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): ISA2 (I1-1) - IACALO (E8-14)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): ISB1 (I1-4) - IACBHI (E8-25)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): ISB2 (I1-2) - IACBLO (E8-24)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): ISA1 (I1-3) - IACAHI (E8-15) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): ISA2 (I1-1) - IACALO (E8-14) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): ISB1 (I1-4) - IACBHI (E8-25) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): ISB2 (I1-2) - IACBLO (E8-24) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0705` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 55] Malfungsi Sirkuit Sensor Range Transmisi (Input PRNDL) (Dokumen: RM000000W84042X) | [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 56] Malfungsi Sirkuit Sensor Range Transmisi (Input PRNDL) (Dokumen: RM000000W84042X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open dalam sirkuit switch posisi parkir/netral Posisi switch Park/neutral ECU kontrol transmisi; [TRANSMISI OTOMATIS A4Q] Area Gangguan: Short dalam sirkuit switch posisi parkir/netral Posisi switch Park/neutral ECU kontrol transmisi; Kondisi Deteksi: 2 atau lebih switch ON secara bersamaan selama lebih dari priode spesifikasi untuk posisi P, R, N, D, 2 dan L. (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (SWITCH POSISI PARK/NEUTRAL - MASA BODI): Lepaskan konektor N1 switch posisi parkir / neutral. -> Ukur tahanan.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (BATERAI - SWITCH POSISI PARKIR/NETRAL): Putar switch pengapian ke ON, dan ukur voltasenya.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA POSISI SWITCH PARKIR/NETRAL ASY: Ukur tahanan ketika shift lever digerakkan ke setiap posisi. -> Hubungkan kembali konektor N1 switch posisi parkir / netral.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (SWITCH POSISI PARK/NEUTRAL -ECU KONTROL TRANSMISI): Lepas konektor C8 meter kombinasi. -> Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan ketika shift lever digerakkan ke setiap posisi. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi. -> Lepaskan konektor ECU kont
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERIKSA METER KOMBINASI ASSEMBLY
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SWITCH POSISI PARKIR/NETRAL ASSEMBLY
  - Langkah 8 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 6 (E) - Masa bodi` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Voltage standar: ON (7 (RB) - Masa bodi)` : **11 sampai 14 V**
  - `[TRANSMISI OTOMATIS A4Q] Voltage standar: OFF (7 (RB) - Masa bodi)` : **Di bawah 1 V**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: P (4 (P) - 6 (E))` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: Kecuali P (4 (P) - 6 (E))` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: R (1 (R) - 7 (RB))` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: Kecuali R (1 (R) - 7 (RB))` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: N (5 (N) - 6 (E))` : **Di bawah 1 Ω**

### DTC `P0710` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 38] Sirkuit Sensor Temperatur Fluida transmisi "A" (Dokumen: RM000000W8503LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam sirkuit sensor temperatur ATF Kabel solenoid (Sensor temperatur ATF) ECU kontrol transmisi; Kondisi Deteksi: Sirkuit sensor temperatur ATF mengalami open atau short selama periode yang telah ditentukan. (1 trip detection logic); [TRANSMISI OTOMATIS A4Q] Area Gangguan: Kabel solenoid (Sensor temperatur ATF) ECU kontrol transmisi; Kondisi Deteksi: Sensor temperatur ATF tidak bekerja deng
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA KABEL SOLENOID (SENSOR TEMPERATUR ATF): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(KABEL SOLENOID - ECU KONTROL TRANSMISI): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 0°C (0,00°C) (8 (OTMP) - 12 (ETMP))` : **5,07 kΩ sampai 6,19 kΩ**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 140°C (284°F) (8 (OTMP) - 12 (ETMP))` : **69,8 Ω sampai 74,2 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: - (8 (OTMP) - Masa bodi)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: - (12 (ETMP) - Masa bodi)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 20°C (20,00°C)` : **2,4 kΩ**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 80°C (176°F)` : **313 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 0°C (0,00°C) (T8-14 (OTMP) - T11-13 (ETMP))` : **5,07 kΩ sampai 6,19 kΩ**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 140°C (284°F) (T8-14 (OTMP) - T11-13 (ETMP))` : **69,8 Ω sampai 74,2 Ω**

### DTC `P0711` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 38] Range / Performance Surkuit Sensor Temperatur Fluida Transmisi (Dokumen: RM000000W8503LX)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam sirkuit sensor temperatur ATF Kabel solenoid (Sensor temperatur ATF) ECU kontrol transmisi; Kondisi Deteksi: Sirkuit sensor temperatur ATF mengalami open atau short selama periode yang telah ditentukan. (1 trip detection logic); [TRANSMISI OTOMATIS A4Q] Area Gangguan: Kabel solenoid (Sensor temperatur ATF) ECU kontrol transmisi; Kondisi Deteksi: Sensor temperatur ATF tidak bekerja deng
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA KABEL SOLENOID (SENSOR TEMPERATUR ATF): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(KABEL SOLENOID - ECU KONTROL TRANSMISI): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 0°C (0,00°C) (8 (OTMP) - 12 (ETMP))` : **5,07 kΩ sampai 6,19 kΩ**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 140°C (284°F) (8 (OTMP) - 12 (ETMP))` : **69,8 Ω sampai 74,2 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: - (8 (OTMP) - Masa bodi)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: - (12 (ETMP) - Masa bodi)` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 20°C (20,00°C)` : **2,4 kΩ**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 80°C (176°F)` : **313 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 0°C (0,00°C) (T8-14 (OTMP) - T11-13 (ETMP))` : **5,07 kΩ sampai 6,19 kΩ**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 140°C (284°F) (T8-14 (OTMP) - T11-13 (ETMP))` : **69,8 Ω sampai 74,2 Ω**

### DTC `P0715` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 37] Sirkuit Sensor Kecepatan Input / Turbin (Dokumen: RM000002N8G001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam sirkuit sensor putaran transmisi (sensor kecepatan input) Sensor putaran transmisi (sensor kecepatan input) Open atau short dalam sirkuit switch posisi parkir/netral ECU kontrol transmisi; [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam sirkuit sensor putaran transmisi (sensor kecepatan output) Sensor putaran transmisi (sensor kecepatan output) Open atau short dalam sirku
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Pindahkan tuas pemindah gigi ke posisi P, N, dan D. -> Pilih item menu berikut ini: Powertrain / ECT / DTC / Current or Pending. -> Periksa jika d
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC: Lepas sensor putaran transmisi (sensor kecepatan input) dan sensor putaran transmisi (sensor kecepatan output) dari transmisi. -> Tukar sensor putaran transmisi (sensor kecepatan input) untuk sensor putaran transmisi (sensor kecepatan outpu
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(SENSOR KECEPATAN INPUT - ECU KONTROL TRANSMISI): Lepaskan konektor sensor putaran transmisi (sensor kecepatan input) -> Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T6 sensor putaran transmisi (sensor kecepatan input) -> Hubungkan kembali kone
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(SENSOR KECEPATAN OUTPUT - ECU KONTROL TRANSMISI): Lepaskan konektor T7 sensor putaran transmisi (sensor kecepatan input) -> Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T7 sensor putaran transmisi (sensor kecepatan input) -> Hubungkan kembali k
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — LANJUTKAN KE BAGAN DTC
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — GANTI SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN OUTPUT)
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN INPUT)
  - Langkah 8 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T6-1 (VCC) - T8-9 (VBTB)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T6-2 (VOUT) - T8-10 (RTBN)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T6-3 (GND) - T8-20 (ETBN)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-10 (RTBN) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T7-1 (VCC) - T8-7 (VBOP)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T7-2 (VOUT) - T8-8 (ROPT)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T7-3 (GND) - T8-18 (EOPT)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-8 (ROPT) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0720` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 42] Sirkuit Sensor Kecepatan Output (Dokumen: RM000002N8G001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam sirkuit sensor putaran transmisi (sensor kecepatan input) Sensor putaran transmisi (sensor kecepatan input) Open atau short dalam sirkuit switch posisi parkir/netral ECU kontrol transmisi; [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam sirkuit sensor putaran transmisi (sensor kecepatan output) Sensor putaran transmisi (sensor kecepatan output) Open atau short dalam sirku
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Pindahkan tuas pemindah gigi ke posisi P, N, dan D. -> Pilih item menu berikut ini: Powertrain / ECT / DTC / Current or Pending. -> Periksa jika d
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC: Lepas sensor putaran transmisi (sensor kecepatan input) dan sensor putaran transmisi (sensor kecepatan output) dari transmisi. -> Tukar sensor putaran transmisi (sensor kecepatan input) untuk sensor putaran transmisi (sensor kecepatan outpu
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(SENSOR KECEPATAN INPUT - ECU KONTROL TRANSMISI): Lepaskan konektor sensor putaran transmisi (sensor kecepatan input) -> Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T6 sensor putaran transmisi (sensor kecepatan input) -> Hubungkan kembali kone
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(SENSOR KECEPATAN OUTPUT - ECU KONTROL TRANSMISI): Lepaskan konektor T7 sensor putaran transmisi (sensor kecepatan input) -> Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T7 sensor putaran transmisi (sensor kecepatan input) -> Hubungkan kembali k
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — LANJUTKAN KE BAGAN DTC
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — GANTI SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN OUTPUT)
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN INPUT)
  - Langkah 8 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T6-1 (VCC) - T8-9 (VBTB)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T6-2 (VOUT) - T8-10 (RTBN)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T6-3 (GND) - T8-20 (ETBN)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-10 (RTBN) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T7-1 (VCC) - T8-7 (VBOP)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T7-2 (VOUT) - T8-8 (ROPT)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T7-3 (GND) - T8-18 (EOPT)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-8 (ROPT) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0725` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 86] Sirkuit Input Putaran Mesin (Dokumen: RM000002N8J001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam wire harness antara ECM dan ECU kontrol transmisi ECU kontrol transmisi Sistem SFI; Kondisi Deteksi: Pada saat sinyal REG1 (ATNE) tidak di-input dari ECM ke ECU kontrol transmisi selama periode spesifikasinya. (2 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC / Current or pending. -> Baca DTC menggunakan tester. -> Pilih item menu berikut ini: Power
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (ECU KONTROL TRANSMISI - ECM): Lepaskan konektor ECU kontrol transmisi T9. -> Lepaskan konektor ECM E9. -> Ukur tahanan. -> Hubungkan kembali konektor T9 ECU kontrol transmisi. -> Hubungkan kembali konektor ECM E9.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI: Ganti ECU kontrol transmisi.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC (DTC P0725/86): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar switch pengapian off dan hidupkan tester off. -> Start mesin dan hidupkan tester -> Pilih item menu berikut i
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — LANJUTKAN KE BAGAN DTC
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — PERIKSA SISTEM SFI
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-8 (REG1) - E9-3 (ATNE)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: E9-3 (ATNE) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P0753` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 61] Shift Solenoid A" Elektrik (Shift Solenoid Valve SL1) (Dokumen: RM000002N8K001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SL1 Shift solenoid valve SL1 ECU kontrol transmisi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA KABEL SOLENOID (SL1): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (KABEL SOLENOID - ECM): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA SHIFT SOLENOID VALVE SL1: Lepas shift solenoid valve SL1. -> Ukur tahanan. -> Hubungkan terminal baterai positif (+) dengan bohlam 21 W ke terminal 2 dan baterai negatif (-) ke terminal 1 konektor solenoid valve, kemudian periksa gerakan katup.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SHIFT SOLENOID VALVE SL1
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 7 (B1+) - 11 (B1-)` : **5,0 sampai 5,6 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 7 (B1+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 11 (B1-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-6 (B1+) - T8-5 (B1-)` : **5,0 sampai 5,6 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-6 (B1+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-5 (B1-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 1 - 2` : **5,0 sampai 5,6 Ω**

### DTC `P0758` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 62] Shift Solenoid B" Elektrik (Shift Solenoid Valve SL2) (Dokumen: RM000002N8L001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SL2 Shift solenoid valve SL2 ECU kontrol transmisi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA KABEL SOLENOID (SL2): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (KABEL SOLENOID - ECM): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA SHIFT SOLENOID VALVE SL2: Lepas shift solenoid valve SL2. -> Ukur tahanan. -> Hubungkan terminal baterai positif (+) dengan bohlam 21 W ke terminal 2 dan baterai negatif (-) ke terminal 1 konektor solenoid valve, kemudian periksa gerakan katup.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SHIFT SOLENOID VALVE SL2
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 5 (C2+) - 9 (C2-)` : **5,1 sampai 5,5 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 5 (C2+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 9 (C2-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-4 (C2+) - T8-3 (C2-)` : **5,1 sampai 5,5 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-4 (C2+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-3 (C2-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 1 - 2` : **5,1 sampai 5,5 Ω**

### DTC `P0763` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 63] Shift Solenoid "C" Elektrik (Shift Solenoid Valve SL3) (Dokumen: RM000002N8M001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SL3 Shift solenoid valve SL3 ECU kontrol transmisi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA KABEL SOLENOID (SL3): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (KABEL SOLENOID - ECM): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA SHIFT SOLENOID VALVE SL3: Lepas shift solenoid valve SL3. -> Ukur tahanan. -> Hubungkan terminal baterai positif (+) dengan bohlam 21 W ke terminal 2 dan baterai negatif (-) ke terminal 1 konektor solenoid valve, kemudian periksa gerakan katup.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SHIFT SOLENOID VALVE SL3
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 6 (C3B2+) - 10 (C3B2-)` : **5,1 sampai 5,5 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 6 (C3B2+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 10 (C3B2-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-2 (C3B2+) - T8-1 (C3B2-)` : **5,1 sampai 5,5 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-2 (C3B2+) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-1 (C3B2-) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 1 - 2` : **5,1 sampai 5,5 Ω**

### DTC `P0768` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 64] Shift Solenoid "D" Elektrik (Shift Solenoid Valve DSU) (Dokumen: RM000002N8N001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve DSU Shift solenoid valve DSU ECU kontrol transmisi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA SOLENOID WIRE (DSU): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (KABEL SOLENOID - ECM): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA SHIFT SOLENOID VALVE DSU: Lepas shift solenoid valve DSU. -> Ukur tahanan. -> Hubungkan terminal baterai positif (+) dari konektor solenoid valve, dan baterai negatif (-) ke bodi solenoid valve.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SHIFT SOLENOID VALVE DSU
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 2 (LUCC) - Masa bodi` : **11 sampai 13 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-23 (LUCC) - Masa bodi` : **11 sampai 13 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: Konektor Solenoid (DSU) - Bodi Solenoid (DSU)` : **11 sampai 13 Ω**

### DTC `P0773` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 65] Shift Solenoid "E" Elektrik (Shift Solenoid Valve SL) (Dokumen: RM000002N8H001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SL Shift solenoid valve SL ECU kontrol transmisi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA SOLENOID WIRE (SL): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (KABEL SOLENOID - ECM): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA SHIFT SOLENOID VALVE SL: Lepas shift solenoid valve SL -> Ukur tahanan. -> Hubungkan terminal baterai positif (+) dari konektor solenoid valve, dan baterai negatif (-) ke bodi solenoid valve.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SHIFT SOLENOID VALVE SL
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 3 (LUCR) - Masa bodi` : **14 sampai 18 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-11 (LUCR) - Masa bodi` : **14 sampai 18 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: Konektor Solenoid (SL) - Bodi Solenoid (SL)` : **14 sampai 18 Ω**

### DTC `P1346` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 75] Sensor VVT / Range Sirkuit sensor Posisi Camshaft / Problem Performance (Bank 1) (Dokumen: RM000002ILD002X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 75] Sensor VVT / Range Sirkuit sensor Posisi Camshaft / Problem Performance (Bank 1) (Dokumen: RM
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Sistem mekanikal (rantai timing loncat gigi, rantai telah memanjang) Timing katup ECM; Kondisi Deteksi: Timing crankshaft dan timing camshaft keduanya tidak bersesuaian dengan kontrol timing katup (2 trip detection logic); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Sistem mekanikal (rantai timing loncat gigi, rantai telah memanjang) Timing katup ECM; Kondisi Deteksi: Crankshaft timing dan camshaft No.
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA VALVE TIMING (PERIKSA DARI KEKENDORAN DAN GIGI LOMPAT PADA TIMING CHAIN): Putar crankshaft searah jarum jam, untuk meluruskan tanda timing dari puli crankshaft dengan penunjuk pada tutup rantai timing. -> Periksa bahwa tanda penyesuai pada camshaft timing sprocket menghadap ke atas. Jika tidak, putar crankshaft 1
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — SETEL VALVE TIMING
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA VALVE TIMING (PERIKSA DARI KEKENDORAN DAN GIGI LOMPAT PADA TIMING CHAIN): Putar crankshaft searah jarum jam, untuk meluruskan tanda timing dari puli crankshaft dengan penunjuk pada tutup rantai timing. -> Periksa bahwa tanda penyesuai pada camshaft timing sprocket menghadap ke atas. Jika tidak, putar crankshaft 1
  - Langkah 2 (SISTEM KONTROL MESIN EJ-VE) — TIMING KATUP PENYESUAI
  - Langkah 3 (SISTEM KONTROL MESIN EJ-VE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN K3-VE) — PERIKSA VALVE TIMING (PERIKSA DARI KEKENDORAN DAN GIGI LOMPAT PADA TIMING CHAIN): Putar crankshaft searah jarum jam, untuk meluruskan tanda timing dari puli crankshaft dengan penunjuk pada tutup rantai timing. -> Periksa bahwa tanda penyesuai pada camshaft timing sprocket menghadap ke atas. Jika tidak, putar crankshaft 1
  - Langkah 2 (SISTEM KONTROL MESIN K3-VE) — SETEL VALVE TIMING

### DTC `P1349` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 73] Malfungsi pada Sistem VVT (Bank 1) (Dokumen: RM000002ILF002X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 73] Malfungsi pada Sistem VVT (Bank 1) (Dokumen: RM000002ILF000X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 73] Malfungsi pada Si
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit camshaft timing oil control valve Timing katup Katup kontrol oli camshaft Filter camshaft timing oil control valve Camshaft timing sprocket assembly ECM; [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit camshaft timing oil control valve Timing katup Katup Kontrol Oli Timing Camshaft Filter camshaft timing oil control valve Camshaft timing sprocket 
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA TIMING KATUP: Putar crankshaft searah jarum jam, untuk meluruskan tanda timing dari puli crankshaft dengan penunjuk pada tutup rantai timing. -> Periksa bahwa tanda penyesuai pada camshaft timing sprocket menghadap ke atas. Jika tidak, putar crankshaft 1
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY (CARA KERJA OCV): Hidupkan mesin. -> Periksa putaran mesin pada periksa (1) dan (2). -> Hubungkan kembali konektor camshaft timing oil control valve.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (SINYAL OCV ): Periksa menggunakan oscilloscope. -> Selama idling, periksa bentuk gelombang antara terminal konektor E9 ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA FILTER OIL CONTROL VALVE (FILTER OCV): Lepas filter OCV (Camshaft Timing Oil Control Valve) -> Periksa filter tidak tersumbat. -> Pasang kembali OCV filter
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - CAMSHAFT TIMING OIL CONTROL VALVE (OCV)): Lepaskan konektor C7 OCV (Camshaft Timing Oil Control Valve) -> Lepaskan konektor ECM E9. -> Periksa tahanan. -> Hubungkan kembali konektor OCV. -> Hubungkan kembali konektor ECM .
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA KATUP KONTROL CAMSHAFT TIMING OIL ASSY (OCV): Periksa tahanan. -> Periksa cara kerja.
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI KATUP KONTROL CAMSHAFT TIMING OIL ASSY
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA CAMSHAFT TIMING SPROCKET ASSEMBLY
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): OCV (C7-1) - OCV+ (E9-7)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): OCV (C7-2) - OCV- (E9-6)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): OCV (C7-1) atau OCV+ (E9-7) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): OCV (C7-2) atau OCV- (E9-6) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: 1 (+) - 2 (-)` : **6,9 sampai 7,9 Ω pada 20°C (68°F)**
  - `[SISTEM KONTROL MESIN EJ-VE] Standar: OCV+ (E9-7) - OCV- (E9-6)` : **Betulkan bentuk gelombang seperti ditunjukkan berikut**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): OCV (C7-1) - OCV+ (E9-7)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): OCV (C7-2) - OCV- (E9-6)` : **Di bawah 1 Ω**

### DTC `P1510` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 54] Sirkuit Sinyal Starter (Dokumen: RM000002ILA002X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 54] Sirkuit Sinyal Starter (Dokumen: RM000002ILA000X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 54] Sirkuit Sinyal Starter (Dokumen: RM000002
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sinyal starter Open atau short dalam sirkuit speedometer ECM; [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit sinyal starter Open atau short dalam sirkuit sensor kecepatan ECM; [SISTEM KONTROL MESIN K3-VE] Area Gangguan: Open atau short dalam sirkuit sinyal starter Open atau short dalam sirkuit speedometer ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTAGE STA): Putar switch pengapian ke ON. -> Ukur voltase antara terminal-terminal konektor E8, E9 ECM
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA FUSE (FUSE ST-A): Cabut fuse ST-A dari kotak fuse. -> Periksa tahanan fuse ST-A. -> Pasang kembali fuse ST-A.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - ST-A FUSE): Periksa harness dan konektor antara konektor fuse ST-A dan ECM
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (FUSE ST-A - STARTER): Lepaskan konektor starter S1. -> Cabut fuse ST-A dari kotak fuse. -> Periksa tahanan. -> Hubungkan kembali konektor starter -> Pasang kembali fuse ST-A.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SWITCH PENGAPIAN ASSEMBLY: Lepaskan konektor 15 switch pengapian. -> Periksa tahanan antara terminal konektor seperti ditunjukkan di bawah. -> Hubungkan kembali konektor switch pengapian
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA FUSE (FUSE ST-B (HANYA A/T)): Cabut fuse ST-B dari kotak fuse. -> Periksa tahanan fuse ST-B. -> Pasang kembali fuse ST-B.
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA RELAY STARTER (RELAY STARTER (HANYA A/T)): Lepas relay starter. -> Periksa tahanan relay starter. -> Pasang kembali relay starter.
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - RELAY STARTER (HANYA A/T)): Periksa harness dan konektor antara relay starter dan konektor ECM.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: STA (E9-15) - E1 (E8-29) (Switch pengapian ON)` : **0 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: STA (E9-15) - E1 (E8-29) (Mesin berputar)` : **6 V atau lebih**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Kotak fuse (terminal 2 fuse ST-A ) - STA (E9-15)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Kotak fuse (terminal 2 fuse ST-A ) atau STA (E9-15) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): Starter (S1-1) - Kotak fuse (terminal 1 fuse ST-A)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): Starter (S1-1) atau Kotak fuse (terminal 1 fuse ST-A) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: LOCK (Semua terminal)` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Tahanan standar: ACC (1-3)` : **Di bawah 1 Ω**

### DTC `P1520` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 51] Sirkuit Switch A/C Malfungsi (Dokumen: RM000002ILC002X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 51] Sirkuit Switch A/C Malfungsi (Dokumen: RM000002ILC000X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 51] Sirkuit Switch A/C Malfungsi 
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit sensor posisi throttle Sensor posisi throttle Short circuit dalam switch kontrol cooler (dengan heater) Switch kontrol cooler assembly (dengan heater) Short circuit dalam switch kontrol temperatur A/C (tanpa heater) Switch kontrol temperatur A/C (menyatu dengan switch kontrol heater assembly) (tanpa heater) Open atau short dalam sirkuit switch posisi parkir/netral Posisi s
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM: Putar switch pengapian ke ON. -> Bebaskan pedal akselerator. -> Putar switch kontrol temperatur A/C ke OFF (tanpa heater) -> Pindahkan gigi transmisi ke posisi P atau N (Kendaraan A/T) -> Ukur voltase antara terminal konektor E8, E9 dan E10
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (THROTTLE POSITION SENSOR- ECM): Lepaskan konektor sensor posisi throttle T1 -> Lepaskan konektor ECM E8. -> Periksa tahanan antara wire harness sisi konektor. -> Hubungkan kembali konektor sensor posisi throttle. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SENSOR POSISI THROTTLE: Lepaskan konektor sensor posisi throttle T1 -> Ukur tahanan antara terminal-terminal dari sensor posisi throttle. -> Hubungkan kembali konektor sensor posisi throttle.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (SWITCH KONTROL COOLER - ECM): Lepaskan konektor ECM E9. -> Putar switch pengapian ke ON. -> Ukur voltase antara terminal konektor ECM dan Masa bodi. -> Hubungkan kembali konektor ECM.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SWITCH KONTROL COOLER ASSEMBLY: Lepas switch kontrol cooler assembly. -> Periksa tahanan antara terminal-terminal dari switch kontrol cooler. -> Pasang kembali switch kontrol cooler.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (SWITCH KONTROL TEMPERATUR A/C - ECM): Lepaskan konektor A6 switch kontrol temperatur A/C (menyatu dengan switch kontrol heater assembly). -> Lepaskan konektor E10 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor switch kontrol temperatur A/C. -> Hubungkan kembali konektor
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA SWITCH KONTROL HEATER ASSEMBLY (SWITCH KONTROL TEMPERATUR A/C): Lepas switch kontrol heater assembly. -> Putar knob switch kontrol temperatur A/C ke posisi OFF. -> Periksa tahanan antara terminal switch kontrol temperatur A/C (menyatu dengan switch kontrol heater assembly). -> Pasang kembali switch kont
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR ( METER KOMBINASI ASSEMBLY - ECM): Lepas konektor C8 meter kombinasi. -> Lepaskan konektor E10 ECM. -> Periksa tahanan. -> Hubungkan kembali konektor meter kombinasi assembly. -> Hubungkan kembali konektor ECM.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Sensor posisi throttle): VTH (E8-20) - E2 (E8-30) (Tertutup penuh)` : **0,4 sampai 0,8 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Sensor posisi throttle): VTH (E8-20) - E2 (E8-30) (Terbuka penuh)` : **3,2 sampai 5,0 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Sensor posisi throttle): VC (E8-10) - E2 (E8-30) (-)` : **4,5 sampai 5,5 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Switch kontrol cooler) (dengan heater): ACSW (E9-24) - E1 (E8-29) (Switch kontrol cooler OFF)` : **Di bawah 1 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Switch kontrol cooler) (dengan heater): ACSW (E9-24) - E1 (E8-29) (Switch blower dan switch k` : **11 sampai 14 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Switch kontrol temperatur A/C) (tanpa heater): ACVR (E10-30) - E21 (E8-29)` : **4,5 sampai 5,5 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Switch posisi parkir/netral): A/T (E10-20) - E1 (E8-29) (Range P atau N)` : **0 sampai 0,5 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltase standar (Switch posisi parkir/netral): A/T (E10-20) - E1 (E8-29) (Selain dari range di atas)` : **Sekitar 10 V**

### DTC `P1530` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 44] Sistem Sinyal Sensor Temperatur Evaporator Air Conditioner (Dokumen: RM000002ILB002X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 44] Sistem Sinyal Sensor Temperatur Evaporator Air Conditioner (Dokumen: RM000002ILB000X) | [SISTEM KONTROL MESIN K3-VE
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit thermistor cooler No. 1 Thermistor cooler No.1 ECM; Kondisi Deteksi: Output voltase dari thermistor di bawah 0,1 V atau di atas 4,85 V selama lebih dari 0,5 detik dengan switch A/C bekerja (1 trip pendeteksian logis); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit thermistor cooler No. 1 Thermistor cooler No.1 ECM; Kondisi Deteksi: Output voltase
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (VOLTASE ACEV): Putar switch pengapian ke ON. -> Putar switch cooler control ke ON. -> Ukur voltase antara terminal pada konektor E10 ECM.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (COOLER THERMISTOR NO. 1 - ECM): Lepaskan konektor cooler thermistor A5 No.1. -> Lepaskan konektor E10 ECM. -> Periksa tahanan. -> Lepaskan konektor cooler thermistor No.1. -> Hubungkan kembali konektor ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA THERMISTOR PENDINGIN NO.1
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI COOLER THERMISTOR NO.1
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA ECM (VOLTASE ACEV): Putar switch pengapian ke ON. -> Putar switch air conditioner ke ON. -> Ukur voltase antara terminal pada konektor E10 ECM.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: ACEV (E10-14) - E21 (E10-31)` : **0,15 sampai 4,8 V**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): ACEV (A5-1) - ACEV (E10-14)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): E21 (A5-2) - E21 (E10-31)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): ACEV (A5-1) atau ACEV (E10-14) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Voltase standar: ACEV (E10-14) - E21 (E10-31)` : **0,15 sampai 4,8 V**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): ACEV (A5-1) - ACEV (E10-14)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): E21 (A5-2) - E21 (E10-31)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari short):: ACEV (A5-1) atau ACEV (E10-14) - Masa bodi` : **10 kΩ atau lebih**

### DTC `P1600` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 83] Malfungsi pada Sirkuit Sinyal Immobiliser (Dokumen: RM000002KAY000X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 83] Malfungsi pada Sirkuit Sinyal Immobiliser (Dokumen: RM000002KAY002X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: ECM; Kondisi Deteksi: Kode yang berganti-ganti tidak dapat selesai ditulis dalam ECM (1 trip detection logic); [SISTEM KONTROL MESIN K3-VE] Area Gangguan: ECM
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA OUTPUT DTC: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester ke-ON. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN K3-VE) — PERIKSA OUTPUT DTC: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN K3-VE) — GANTI ECM

### DTC `P1601` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 81] Malfungsi Sinyal Immobiliser (Dokumen: RM000002KAZ000X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 81] Malfungsi Sinyal Immobiliser (Dokumen: RM000002KAZ002X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Sistem engine immobiliser ECU kunci transponder assembly (ECU Immobiliser ) Open atau short dalam line komunikasi (wire harness atau konektor) ECM; Kondisi Deteksi: Problem komunikasi dengan ECU kunci transponder assembly (ECU Immobiliser) atau ketidak sesuaian kode. (1 trip detection logic); [SISTEM KONTROL MESIN K3-VE] Area Gangguan: Sistem engine immobiliser ECU kunci transponder assembly (ECU Immob
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA OUTPUT DTC LAINNYA: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar switch pengapian ke OFF, kemudian putar switch pengapian ke ON lagi. -> Hidupkan mesin. -> Pilih menu item be
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - ECU KUNCI TRANSPONDER): Lepaskan konektor E10 ECM. -> Lepaskan konektor T14 ECU kunci transponder -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor ECU kunci transponder.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — LAKUKAN PENDAFTARAN KUNCI: Hapus DTC (Lihat halaman ). -> Reregister kunci (kode ID kunci)
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hidupkan mesin. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM: Ganti dengan ECM baru atau yang telah diketahui baik.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hidupkan mesin. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECU KUNCI TRANSPONDER ASSEMBLY
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — SELESAI
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): SIO2 (T14-8) - SIO2 (E10-32)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): SIO2 (T14-8) atau SIO2 (E10-32) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN K3-VE] Standar tahanan (Periksa keadaan open): SIO2 (T14-8) - SIO2 (E10-32)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN K3-VE] Standar tahanan (Periksa keadaan short): SIO2 (T14-8) atau SIO2 (E10-32) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P1602` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 82] Problem Komunikasi Serial antara ECU EFI dan ECU A/T (Dokumen: RM000002KAX000X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit line komunikasi ECU kontrol transmisi ECM; Kondisi Deteksi: Malfungsi komunikasi dari ECM ke ECU kontrol transmisi atau dari ECU kontrol transmisi ke ECM dideteksi selama lebih dari periode spesifikasi. (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA OUTPUT DTC: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Lakukan uji jalan. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - ECU KONTROL TRANSMISI): Lepaskan konektor ECM E9. -> Lepaskan konektor ECU kontrol transmisi T9. -> Periksa tahanan. -> Hubungkan kembali konektor ECM. -> Hubungkan kembali konektor ECU kontrol transmisi.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECU KONTROL TRANSMISI (SUMBER DAYA DARI ECU KONTROL TRANSMISI): Putar switch pengapian ke ON. -> Ukur voltase antara terminal-terminal konektor ECU kontrol transmisi.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI KOMPUTER KONTROL TRANSMISI: Ganti dengan ECU kontrol transmisi baru atau yang telah diketahui baik. -> Hapus DTC (Lihat halaman ).
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA APAKAH OUTPUT DTC BERULANG: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke-ON dan hidupkan tester. -> Pilih menu item berikut ini: Powertrain / Engine / DTC. -> Baca DTC.
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — SELESAI
  - Langkah 8 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): CRX (T9-4) - ATTX (E9-2)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): CTX (T9-12) - ATRX (E9-1)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): CRX (T9-4) atau ATTX (E9-2) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): CTX (T9-12) atau ATRX (E9-1) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: +B1 (T9-3) - E1 (T9-24)` : **11 sampai 14 V**

### DTC `P1656` — [SISTEM KONTROL MESIN 3SZ-VE — SISTEM SFI / Flash Code 74] Malfungsi pada Sikuit OCV (Bank 1) (Dokumen: RM000002ILE002X) | [SISTEM KONTROL MESIN EJ-VE — SISTEM SFI / Flash Code 74] Malfungsi pada Sikuit OCV (Bank 1) (Dokumen: RM000002ILE000X) | [SISTEM KONTROL MESIN K3-VE — SISTEM SFI / Flash Code 74] Malfungsi pada Si
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [SISTEM KONTROL MESIN 3SZ-VE] Area Gangguan: Open atau short dalam sirkuit camshaft timing oil control valve Katup kontrol oli camshaft ECM; Kondisi Deteksi: Open atau short dalam sirkuit camshaft timing oil control valve (1 trip detection logic); [SISTEM KONTROL MESIN EJ-VE] Area Gangguan: Open atau short dalam sirkuit camshaft timing oil control valve Katup Kontrol Oli Timing Camshaft ECM; [SISTEM KONTROL MESIN K3-VE] Area Gangguan: Open atau s
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY (CARA KERJA OCV): Lepaskan konektor C7 OCV (Camshaft Timing Oil Control Valve) -> Gunakan voltase baterai positif pada terminal OCV. -> Periksa putaran mesin -> Hubungkan kembali konektor OCV.
  - Langkah 2 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA ECM (SINYAL OCV ): Putar switch pengapian ke ON. -> Ukur voltase antara terminal pada konektor E9 ECM.
  - Langkah 3 (SISTEM KONTROL MESIN 3SZ-VE) — PERIKSA HARNESS DAN KONEKTOR (ECM - OCV): Lepaskan konektor C7 OCV (Camshaft Timing Oil Control Valve) -> Lepaskan konektor ECM E9. -> Periksa tahanan. -> Hubungkan kembali konektor OCV. -> Hubungkan kembali konektor ECM.
  - Langkah 4 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI KATUP KONTROL CAMSHAFT TIMING OIL ASSY
  - Langkah 5 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 6 (SISTEM KONTROL MESIN 3SZ-VE) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (SISTEM KONTROL MESIN 3SZ-VE) — GANTI ECM
  - Langkah 1 (SISTEM KONTROL MESIN EJ-VE) — PERIKSA CAMSHAFT TIMING OIL CONTROL VALVE ASSEMBLY (CARA KERJA OCV): Lepaskan konektor C7 OCV (Camshaft Timing Oil Control Valve) -> Gunakan voltase baterai positif pada terminal OCV. -> Periksa putaran mesin -> Hubungkan kembali konektor OCV.
- **Spesifikasi Standar Multimeter**:
  - `[SISTEM KONTROL MESIN 3SZ-VE] Voltage standar: OCV+ (E9-7) - OCV- (E9-6)` : **0,4 V atau kurang**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): OCV (C7-1) - OCV+ (E9-7)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan open): OCV (C7-2) - OCV- (E9-6)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): OCV (C7-1) atau OCV+ (E9-7) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN 3SZ-VE] Standar tahanan (Periksa keadaan short): OCV (C7-2) atau OCV- (E9-6) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[SISTEM KONTROL MESIN EJ-VE] Voltase standar: OCV+ (E9-7) - OCV- (E9-6)` : **0,4 V atau kurang**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): OCV (C7-1) - OCV+ (E9-7)` : **Di bawah 1 Ω**
  - `[SISTEM KONTROL MESIN EJ-VE] Tahanan standar (Periksa dari open): OCV (C7-2) - OCV- (E9-6)` : **Di bawah 1 Ω**

### DTC `P1703` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 72] Kecepatan Lock-up tidak Bersesuaian (Dokumen: RM000002N8O001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Valve body assembly Torque converter clutch (Kopling torque converter) ECU kontrol transmisi Transmisi otomatis assembly; Kondisi Deteksi: Pada saat lock-up bekerja dan putaran mesin sangat berbeda dengan putaran lock-up. (2 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA HYDRAULIC TEST
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA TORQUE CONVERTER CLUTCH ASSEMBLY
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — GANTI TORQUE CONVERTER CLUTCH ASSEMBLY
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI TRANSMISSION VALVE BODY ASSEMBLY
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI TRANSMISI OTOMATIS ASSEMBLY

### DTC `P1706` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 31] Malfungsi Momen Mesin (Dokumen: RM000002N8P001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Sistem SFI; Kondisi Deteksi: Ketika sinyal malfungsi dikirim dari ECM. (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC (SISTEM SFI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC / Current or Pending. -> Baca DTC menggunakan tester.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — LANJUTKAN KE BAGAN DTC (SISTEM SFI)

### DTC `P1711` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 41] Malfungsi Sensor Posisi Throttle (Dokumen: RM000002N8Q001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Sistem SFI; Kondisi Deteksi: Ketika sinyal malfungsi dikirim dari ECM. (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC (SISTEM SFI): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / Engine / DTC / Current or Pending. -> Baca DTC menggunakan tester.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — LANJUTKAN KE BAGAN DTC (SISTEM SFI)

### DTC `P1730` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 21] Sumber Daya Baterai Abnormal (Dokumen: RM000002N8R001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam sirkuit sumber daya back-up ECU kontrol transmisi; Kondisi Deteksi: Back-up power source (BAT1, BAT2) is cut off for a specific period of time. (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA ECU KONTROL TRANSMISI (VOLTASE BAT1, BAT2 ): Lepaskan konektor ECU kontrol transmisi T9. -> Putar switch pengapian ke ON. -> Ukur voltase antara terminal konektor T9 ECU kontrol transmisi -> Hubungkan kembali konektor T9 ECU kontrol transmisi.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA FUSE (ECU-B): Cabut fuse ECU-B dari ruang mesin R/B. -> Periksa tahanan fuse ECU-B. -> Pasang kembali fuse ECU-B.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(FUSE ECU-B - ECU KONTROL TRANSMISI): Cabut fuse ECU-B dari ruang mesin R/B. -> Lepaskan konektor ECU kontrol transmisi T9. -> Ukur tahanan. -> Hubungkan kembali konektor T9. -> Pasang kembali fuse ECU-B.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(FUSE ECU-B - BATERAI): Cabut fuse ECU-B dari ruang mesin R/B. -> Lepaskan terminal negatif baterai. -> Lepaskan terminal baterai positif. -> Ukur tahanan. -> Pasang kembali fuse ECU-B. -> Lepaskan terminal baterai positif. -> Hubungkan kembali terminal negatif ba
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC: Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar switch pengapian off dan hidupkan tester off. -> Start mesin dan hidupkan tester -> Pilih item menu berikut i
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — PERIKSA DARI SHORT PADA SEMUA HARNESSES DAN KONEKTOR YANG DIHUBUNGKAN KE FUSE DAN GANTI FUSE
  - Langkah 8 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Voltage standar: T9-1 (BAT2) - T9 - 6 (E01)` : **11 sampai 14 V**
  - `[TRANSMISI OTOMATIS A4Q] Voltage standar: T9-2 (BAT2) - T9 - 6 (E01)` : **11 sampai 14 V**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 2 (Fuse ECU-B) - T9-1 (BAT2)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 2 (Fuse ECU-B) - T9-2 (BAT2)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 2 (fuse ECU-B) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Standar tahanan (Periksa keadaan open): Terminal positif baterai 1 (fuse ECU-B)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Standar tahanan (Periksa keadaan open): 1 (fuse ECU-B) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P1731` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 22] Sumber Daya Sistem Sensor Abnormal (Dokumen: RM000002N8S001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Short dalam sirkuit transmission revolution sensor (sensor kecepatan input) Short dalam sirkuit transmission revolution sensor (sensor kecepatan output) Sensor putaran transmisi (sensor kecepatan input) Sensor putaran transmisi (sensor kecepatan output) ECU kontrol transmisi; Kondisi Deteksi: Tidak terdapat sinyal dari sensor putaran transmisi (sensor kecepatan input) dan sensor putaran transmisi (sensor ke
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR(SENSOR PUTARAN TRANSMISI - ECU KONTROL TRANSMISI): Lepaskan konektor sensor putaran transmisi (sensor kecepatan input) -> Lepaskan konektor t 17 sensor putaran transmisi (sensor kecepatan output) -> Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN INPUT): Hubungkan intelligent tester ke DLC3. -> Lepaskan konektor sensor putaran transmisi (sensor kecepatan input) -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / ECT / DTC / Current. -> Baca DTC 
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN OUTPUT): Hubungkan intelligent tester ke DLC3. -> Lepaskan konektor T17 sensor putaran transmisi (sensor kecepatan output) -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Pilih item menu berikut ini: Powertrain / ECT / DTC / Current. -> Baca
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN OUTPUT)
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — GANTI SENSOR PUTARAN TRANSMISI (SENSOR KECEPATAN INPUT)
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-9 (VBTB) - Masa bodi` : **10 kΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-7 (VBOP) - Masa bodi` : **10 kΩ atau lebih tinggi**

### DTC `P1780` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 66] Shift Solenoid "F" Electrical (Shift Solenoid Valve SR) (Dokumen: RM000002N8T001X)
- **Tingkat Keparahan**: `HIGH`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short sirkuit dalam shift solenoid valve SR Shift solenoid valve SR ECU kontrol transmisi
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA SOLENOID WIRE (SR): Lepaskan konektor kabel solenoid E3. -> Ukur tahanan. -> Hubungkan kembali konektor kabel solenoid E3.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (KABEL SOLENOID - ECM): Lepaskan konektor kontrol ECU transmisi T8. -> Ukur tahanan. -> Hubungkan kembali konektor T8 konektor ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA SHIFT SOLENOID VALVE SR: Lepas shift solenoid valve SR. -> Ukur tahanan. -> Hubungkan terminal baterai positif (+) dari konektor solenoid valve, dan baterai negatif (-) ke bodi solenoid valve.
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI KABEL SOLENOID
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 7 (TRANSMISI OTOMATIS A4Q) — GANTI SHIFT SOLENOID VALVE SR
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: 4 (SOLR) - Masa bodi` : **14 sampai 18 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T8-12 (SOLR) - Masa bodi` : **14 sampai 18 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: Konektor Solenoid (SR) - Bodi Solenoid (SR)` : **14 sampai 18 Ω**

### DTC `U0100` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 82] Kehilangan Komunikasi dengan ECM/PCM "A" (Dokumen: RM000002N8I001X)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam ECU kontrol transmisi dan sirkuit ECM ECU kontrol transmisi ECM; Kondisi Deteksi: Bila kontrol transmisi ECU tidak menerima sinyal komunikasi dari ECM. (1 trip detection logic); Kondisi Deteksi: Pada saat ECU kontrol transmisi menerima pesan error (tidak terdapat sinyal dari ECU kontrol transmisi) dari ECM. (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (ECU KONTROL TRANSMISI - ECM): Lepaskan konektor ECU kontrol transmisi T9. -> Lepaskan konektor ECM E9. -> Ukur tahanan. -> Hubungkan kembali konektor T9 ECU kontrol transmisi. -> Hubungkan kembali konektor ECM E9.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI: Ganti ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC (DTC U0100/82 DAN/ATAU U1001/85): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar switch pengapian off dan hidupkan tester off. -> Start mesin dan hidupkan tester -> Pilih item menu berikut i
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-4 (CRX) - E9-2 (ATTX)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-12 (CTX) - E9-1 (ATRX)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-4 (CRX) - Masa bodi` : **10 KΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-12 (CTX) - Masa bodi` : **10 KΩ atau lebih tinggi**

### DTC `U1001` — [TRANSMISI OTOMATIS A4Q — SISTEM TRANSMISI OTOMATIS / Flash Code 85] Kehilangan Komunikasi dari TCM ke ECM (Dokumen: RM000002N8I001X)
- **Tingkat Keparahan**: `MEDIUM`
- **Area Gangguan & Kondisi Deteksi**: [TRANSMISI OTOMATIS A4Q] Area Gangguan: Open atau short dalam ECU kontrol transmisi dan sirkuit ECM ECU kontrol transmisi ECM; Kondisi Deteksi: Bila kontrol transmisi ECU tidak menerima sinyal komunikasi dari ECM. (1 trip detection logic); Kondisi Deteksi: Pada saat ECU kontrol transmisi menerima pesan error (tidak terdapat sinyal dari ECU kontrol transmisi) dari ECM. (1 trip detection logic)
- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:
  - Langkah 1 (TRANSMISI OTOMATIS A4Q) — PERIKSA HARNESS DAN KONEKTOR (ECU KONTROL TRANSMISI - ECM): Lepaskan konektor ECU kontrol transmisi T9. -> Lepaskan konektor ECM E9. -> Ukur tahanan. -> Hubungkan kembali konektor T9 ECU kontrol transmisi. -> Hubungkan kembali konektor ECM E9.
  - Langkah 2 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI: Ganti ECU kontrol transmisi.
  - Langkah 3 (TRANSMISI OTOMATIS A4Q) — PERIKSA OUTPUT DTC (DTC U0100/82 DAN/ATAU U1001/85): Hubungkan intelligent tester ke DLC3. -> Putar switch pengapian ke ON. -> Hidupkan tester. -> Hapus DTC (Lihat halaman ). -> Putar switch pengapian off dan hidupkan tester off. -> Start mesin dan hidupkan tester -> Pilih item menu berikut i
  - Langkah 4 (TRANSMISI OTOMATIS A4Q) — GANTI ECU KONTROL TRANSMISI
  - Langkah 5 (TRANSMISI OTOMATIS A4Q) — PERBAIKI ATAU GANTI HARNESS ATAU KONEKTOR
  - Langkah 6 (TRANSMISI OTOMATIS A4Q) — GANTI ECM
- **Spesifikasi Standar Multimeter**:
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-4 (CRX) - E9-2 (ATTX)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-12 (CTX) - E9-1 (ATRX)` : **Di bawah 1 Ω**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-4 (CRX) - Masa bodi` : **10 KΩ atau lebih tinggi**
  - `[TRANSMISI OTOMATIS A4Q] Tahanan standar: T9-12 (CTX) - Masa bodi` : **10 KΩ atau lebih tinggi**
