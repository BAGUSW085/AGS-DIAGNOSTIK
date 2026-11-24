# PANDUAN ALUR & PAKET PROMPT SKRIPSI — AGOS Smart Diagnostik (R&D Model 4D, Pendidikan Teknik Mesin)

> Dokumen ini memuat **peta alur skripsi lengkap** berbasis cerita nyata permasalahan di bengkel Anda (Bengkel Mobil Indah Jaya Motor & Bengkel SMS Performance) serta **1 Master Prompt (P0) + 50 Prompt per Bab/Sub-bab (P1–P50) + 4 Prompt Utilitas (R1, R2, S1, S2)**.
> Semua fakta teknis telah diverifikasi langsung terhadap kode aktual proyek (`backend/`, `android_offline/`).

---

## BAGIAN A — CERITA MASALAH NYATA & KONSEP INTI SKRIPSI

### 1. Empat Masalah Nyata di Lapangan (Latar Belakang Asli Peneliti)
1. **Scan Tool Hanya Menampilkan Kode, Bukan Pemahaman Lengkap:** Saat melakukan *scanning* di Bengkel Mobil Indah Jaya Motor, mekanik mampu mengetahui nomor kode DTC yang muncul pada *scan tool*, tetapi kerap kesulitan mendeskripsikan makna teknis kode DTC tersebut, mengetahui nilai standar pengecekan, serta membaca jalur *wiring diagram* terkait kode DTC tanpa harus membuka buku *Manual Repair* sesuai model mobil.
2. **Kesenjangan antara Manual Pabrikan dan Realitas Lapangan:** Pada praktik perbaikan sehari-hari, gejala kerusakan kendaraan dengan kode DTC dan keluhan pelanggan yang sama tidak selalu memiliki solusi yang sama persis dengan urutan standar *manual book* pabrikan karena dipengaruhi kondisi pemakaian, usia/kilometer kendaraan, serta variasi keausan komponen di lapangan.
3. **Kebutuhan Menggabungkan Standar Manual + Pengalaman Mekanik:** Diperlukan sebuah media bantu kerja yang **menggabungkan dua sumber pengetahuan**—yakni (a) **prosedur pengecekan, spesifikasi standar, dan *wiring diagram* resmi dari *Manual Repair* pabrikan**, serta (b) **pengalaman nyata mekanik dalam mengatasi gangguan terdahulu** (basis kasus historis yang dapat terus ditambah)—sehingga ketika muncul unit dengan model, keluhan, dan riwayat kasus yang mirip (disertai catatan kilometer/tingkat servis kendaraan), mekanik dapat segera menelusuri solusi terdahulu beserta rujukan manualnya.
4. **Keterbatasan Kepemilikan Manual di Bengkel Umum Non-Resmi:** Berdasarkan pengamatan pada beberapa bengkel mobil umum non-resmi (termasuk Bengkel SMS Performance), banyak bengkel independen belum memiliki koleksi *Manual Repair Book* resmi untuk setiap model kendaraan yang masuk, diperparah sinyal internet area kerja bengkel yang sering kurang stabil untuk mengakses referensi daring.

### 2. Konsep Kebaruan (*Novelty*)
Mengintegrasikan **Pengetahuan Normatif (Standar *Service Manual* Pabrikan, DTC, *Wiring*, & Simulator Multimeter)** dan **Pengetahuan Empiris (Basis Pengalaman Kasus Mekanik Berbobot / *Weighted CBR* + *Live Data* OBD-II)** ke dalam satu aplikasi Android **100% offline** yang dikembangkan dengan model **R&D 4D** dan diuji lintas dua bengkel independen (internal & eksternal).

---

## BAGIAN B — ALUR PENYUSUNAN SKRIPSI (R&D MODEL 4D ADAPTASI BENGKEL)

| Fase Kerja | Tahap 4D | Fokus Kegiatan Nyata | Lokasi / Pihak Terlibat | Prompt Terkait |
|---|---|---|---|---|
| **Fase 1 — Finalisasi Konsep & Proposal** | Persiapan & *Define* awal | Mengunci judul, benang merah masalah–instrumen, menyusun BAB I–III (proposal) dan berkonsultasi ke dosen pembimbing. | Peneliti & Dosen Pembimbing | P0, P1, P2–P28 |
| **Fase 2 — Observasi Kebutuhan (*Define*)** | **1. *Define*** | Observasi alur *scanning* DTC, cara mencari manual/wiring, kesenjangan manual vs lapangan, kondisi sinyal, dan wawancara mekanik. | Bengkel Mobil Indah Jaya Motor (mendalam) & Bengkel SMS Performance (pembanding) | P22, P29, P34 |
| **Fase 3 — Perancangan (*Design*)** | **2. *Design*** | Merancang struktur 4 tab offline, integrasi *Manual Repair* JB420 + basis kasus pengalaman mekanik, simulator *wiring* & multimeter, serta menyusun instrumen validasi & angket. | Peneliti | P23, P27, P29–P33, P35 |
| **Fase 4 — Validasi & Uji Coba (*Develop*)** | **3. *Develop*** | (a) Uji teknis internal (paritas Python–JS, 10 kueri, layar HP, *black-box*, mode pesawat); (b) Validasi Ahli Materi Otomotif, Ahli Media, & Praktisi Senior → revisi; (c) Uji coba terbatas di Indah Jaya Motor → revisi; (d) Uji coba lapangan gabungan kedua bengkel (angket anonim + SUS + opsional uji skenario waktu & ketepatan). | Dosen Ahli, Kepala Mekanik, Mekanik Indah Jaya Motor & SMS Performance | P24, P26, P36–P40 |
| **Fase 5 — Penyebaran (*Disseminate*)** | **4. *Disseminate*** | Pengemasan APK final (`AGOS-Smart-Diagnostik-Offline.apk`) + panduan instalasi & pemakaian, lalu penyerahan/penyebaran resmi ke kedua bengkel (penekanan adopsi eksternal di SMS Performance). | Indah Jaya Motor & SMS Performance | P25, P41 |
| **Fase 6 — Laporan Akhir & Sidang** | Finalisasi | Pembahasan kritis BAB IV, BAB V (Simpulan & Saran), Abstrak ID/EN, cek daftar pustaka, cek konsistensi antarbab, dan simulasi tanya-jawab sidang. | Peneliti & Dosen Pembimbing/Penguji | P42–P50 |

---

## BAGIAN C — CARA MEMAKAI PAKET PROMPT

1. Buka **chat AI baru**. Tempel **PROMPT 0 (Master Prompt)** dan isi semua bagian `[...]`.
2. Tunggu AI menjawab **"Siap"**.
3. Kirim prompt **satu per satu** sesuai urutan (`P1` → `P2` → ...). **Jangan** menggabungkan beberapa prompt dalam satu kirim agar hasil tetap mendalam.
4. Setelah tiap jawaban: baca, periksa kesesuaian dengan cerita bengkel Anda, simpan ke Word. Bila perlu perbaikan, gunakan **R1**.
5. Jika percakapan sudah terlalu panjang: buka chat baru → tempel **PROMPT 0** lagi → tempel **R2 (Lanjutkan Sesi)**.
6. Bagian `[DATA LAPANGAN ...]` wajib diisi dari data asli hasil penelitian Anda di Indah Jaya Motor & SMS Performance (gunakan **Template Data Lapangan — Bagian 7**).
7. Bagian `[BUTUH SITASI: ...]` dicari di Google Scholar / Garuda / SINTA / buku teks otomotif, lalu tempel abstrak/kutipan aslinya menggunakan **S1**.

---

## PROMPT 0 — MASTER PROMPT (WAJIB DITEMPEL PERTAMA)

```markdown
# PERAN
Anda adalah Pembimbing Skripsi Senior bidang **Pendidikan Teknik Mesin (Konsentrasi Otomotif — jalur teknologi terapan industri bengkel)**, ahli metodologi **Research and Development (R&D) Model 4D (Thiagarajan, Semmel, & Semmel, 1974)**, dan penulis akademik Bahasa Indonesia.
Tugas Anda membantu saya menyusun skripsi yang kuat secara keteknikan otomotif, berakar pada masalah nyata bengkel umum, tepat secara metodologi 4D adaptasi industri bengkel, bebas halusinasi, dan siap dipertahankan di sidang.

# PROFIL SKRIPSI
- Program Studi       : Pendidikan Teknik Mesin (Konsentrasi Otomotif)
- Metode              : R&D, Model 4D (Define, Design, Develop, Disseminate), adaptasi konteks industri bengkel
- Judul (sementara)   : [TULIS JUDUL PILIHAN, misal: "Pengembangan Aplikasi Diagnostik Sistem EFI Berbasis Android Offline (AGOS Smart Diagnostik) dengan Model 4D sebagai Integrasi Standar Manual Repair dan Pengalaman Mekanik Bengkel"]
- Pengguna sasaran    : Mekanik bengkel mobil umum / independen (BUKAN siswa/sekolah)
- Lokasi penelitian   :
  1) Bengkel Mobil Indah Jaya Motor — bengkel milik peneliti; dipakai untuk observasi mendalam, identifikasi masalah lapangan (Define), dan uji coba terbatas (Develop)
  2) Bengkel SMS Performance — bengkel tempat peneliti pernah magang (pihak eksternal independen); dipakai untuk observasi pembanding, uji coba lapangan eksternal, dan penyebaran (Disseminate)
  Kota/alamat: [ISI]
- Jumlah mekanik      : Indah Jaya Motor = [ISI] orang; SMS Performance = [ISI] orang
- Validator           : Ahli Materi Otomotif = [ISI jumlah & jabatan, tanpa nama dulu]; Ahli Media = [ISI]; Praktisi senior = [ISI, misal kepala mekanik SMS Performance]
- Gaya sitasi         : [APA 7 / IEEE / pedoman kampus]
- Sistematika kampus  : [misal: BAB I Pendahuluan, BAB II Kajian Pustaka, BAB III Metode Penelitian, BAB IV Hasil Penelitian dan Pembahasan, BAB V Simpulan dan Saran]
- Skala Likert        : [1–4 / 1–5, sesuai arahan dosen]

# CERITA AKAR MASALAH NYATA DI LAPANGAN (WAJIB MENJADI JIWA NARASI SKRIPSI)
1. Di Bengkel Mobil Indah Jaya Motor, saat mekanik melakukan scanning dengan scan tool, mekanik dapat membaca nomor kode DTC yang muncul, tetapi sering belum mampu mendeskripsikan arti teknis kode DTC tersebut, mengetahui nilai standar pengecekan komponen, serta membaca wiring diagram terkait kode DTC tanpa membuka buku Manual Repair sesuai model kendaraan.
2. Pada praktik perbaikan di lapangan, solusi kerusakan kendaraan dengan kode DTC dan keluhan pelanggan tertentu terkadang tidak sama persis dengan urutan penyelesaian yang tertulis di manual book pabrikan karena faktor pemakaian, usia/kilometer kendaraan, dan karakter kasus lapangan.
3. Oleh karena itu, aplikasi dirancang untuk **menggabungkan dua sumber pengetahuan**: (a) prosedur pengecekan, spesifikasi standar, dan wiring diagram resmi dari Manual Repair pabrikan, serta (b) pengalaman nyata mekanik saat mengatasi gangguan terdahulu (basis data kasus historis yang dapat terus ditambah), sehingga ketika muncul model mobil dengan keluhan dan riwayat kasus serupa (disertai catatan kilometer kendaraan), mekanik dapat segera merujuk penyelesaian terdahulu maupun kasus yang mirip.
4. Berdasarkan pengamatan pada bengkel mobil umum non-resmi lainnya (termasuk Bengkel SMS Performance), kendala serupa banyak terjadi karena tidak semua bengkel non-resmi memiliki koleksi Manual Repair Book standar sesuai model mobil yang ditangani, ditambah keterbatasan sinyal internet di area kerja bengkel.

# GROUND TRUTH PRODUK (DILARANG MENAMBAH FITUR DI LUAR DAFTAR INI)
Nama produk: **AGOS Smart Diagnostik** — aplikasi Android (APK) yang berjalan **100% offline** (tanpa server, tanpa internet).
Platform: antarmuka web (HTML + Tailwind CSS + JavaScript) yang dibungkus **Capacitor (Android WebView)**; logika diagnosa dari versi server Python (FastAPI) di-porting ke JavaScript; aset CSS/ikon dibundel lokal; data kasus baru disimpan di memori perangkat (`localStorage`); mendukung orientasi layar Portrait & Landscape.

## Fitur nyata (4 tab)
**Tab 1 — Diagnosa Cepat (Penggabungan Basis Pengalaman Mekanik + Rujukan Manual Repair + Simulator Multimeter)**
- Input: merk, model, tahun, kode mesin, kilometer kendaraan (stepper kelipatan 100 km yang otomatis mengklasifikasikan 4 kategori usia/servis: `<20rb km` Usia Rendah, `20rb–40rb km` Servis Ringan, `40rb–80rb km` Servis Menengah, `≥80rb km` Km Tinggi/Cek Karet-Sensor, serta dicatat pada ringkasan odometer kasus), keluhan pelanggan, gejala, kode DTC, filter sistem, dan 7 parameter Live Data OBD-II (STFT %, LTFT %, RPM, tegangan O2, MAP kPa, MAF g/s, ECT °C). Live Data diketik manual dari hasil scan tool bengkel.
- Metode Pencocokan Pengalaman Kasus (*Weighted Case-Based Reasoning*):
  - `TextScore = (0,10·Merk + 0,15·Model + 0,20·Keluhan + 0,20·Gejala + 0,20·DTC) / 0,85`
    - Keluhan & gejala: pembersihan teks, penghapusan stopword Indonesia, normalisasi istilah lapangan bengkel (*brebet/ndut/nyendat/tersendat* → *mbrebet*; *langsam/stasioner* → *idle*; *lelet/boyo* → *berat*; *panas/mendidih* → *overheat*; *kempos* → *ngempos*), lalu rasio token yang sama.
    - DTC: kode sama = 1; satu keluarga subsistem (18 keluarga, mis. P0300–P0306 misfire) = 0,60; keduanya tanpa DTC = 1.
    - Penalti: jika pengguna mengisi DTC tetapi tidak cocok/sekeluarga → `TextScore × 0,30`.
    - Penyesuaian tahun (jika kemiripan model ≥ 0,5): selisih ≤ 3 tahun → `× 1,05`; selisih ≥ 8 tahun → `× 0,90`.
    - *(Catatan jujur kode: data kilometer dicatat sebagai indikator kategori usia/servis dan konteks odometer pada laporan diagnosa, belum masuk sebagai variabel bobot otomatis dalam persamaan skor kemiripan — hal ini dapat diangkat sebagai keterbatasan sekaligus saran pengembangan lanjut.)*
  - `LiveScore` = rata-rata berbobot kemiripan parameter yang diisi, dengan kemiripan `max(0, 1 − |nilai input − nilai kasus| / toleransi)`:
    STFT (bobot 0,20; tol 5), LTFT (0,15; tol 5), RPM (0,10; tol 300), O2 (0,15; tol 0,15 V), MAP (0,15; tol 10), MAF (0,10; tol 2), ECT (0,15; tol 10).
  - `Skor Total = 0,85·TextScore + 0,15·LiveScore` (bila Live Data diisi); jika kosong, `Skor Total = TextScore`.
  - Kategori kecocokan: Sangat mirip ≥ 80%, Mirip ≥ 60%, Cukup mirip ≥ 40%, Kurang mirip < 40%.
  - Ringkasan 8 sistem: Udara, Bahan Bakar, Pengapian, Mekanis (Pembakaran); Pendingin, Pelumasan, Kelistrikan, Emisi (Pendukung).
- Output: peringkat kasus pengalaman mekanik yang paling mirip, saran penyelesaian standar *Workshop SOP* dari *Manual Repair*, prosedur *Reset ECU & Idle Relearn*, serta **Simulator Jalur Wiring + Digital Multimeter**: 7 sirkuit nyata (Relay Kipas Radiator 4 kabel/P0480, Sensor O2/HO2S 4 kabel, Sensor ECT 2 kabel, Sensor MAP 3 kabel, Koil COP 4 kabel, Sensor MAF+IAT 5 kabel, Throttle Body ETC 6 kabel), mode **Normal (OK)** vs **Mode Gangguan (Fault)**, penampang soket fisik, posisi probe merah(+)/hitam(−), angka DMM (Volt/Ohm), standar manual, dan vonis ukur.

**Tab 2 — Data Kasus (Memori Pengalaman Bengkel)**
- Memuat **17 kasus historis awal** (K001–K018) lintas 6 merek (Daihatsu, Honda, Mitsubishi, Suzuki, Toyota, Wuling).
- Mendukung penambahan kasus baru dari pengalaman nyata mekanik di bengkel, penghapusan, serta uji ulang langsung (tersimpan lokal via `localStorage`).

**Tab 3 — Manual & Wiring (Rujukan Standar Pabrikan Offline)**
- Simulator interaktif **7 komponen EFI** (MAF, O2, ECT, MAP, CKP, Throttle, Ignition Coil): slider beban/bukaan gas, respon sinyal sensor & aktuator ECU, peta lokasi di ruang mesin (*Engine Bay*), spesifikasi standar, pinout soket & warna kabel, gejala rusak & cek cepat.
- Pencarian lokal (*Local Retrieval*, pencocokan kata kunci + skor relevansi, BUKAN AI online) terhadap: **1.381 potongan teks *Service Manual* Suzuki Grand Vitara JB420 Vol. 1 & Vol. 2**, **208 kode DTC** (termasuk 207 entri katalog & 51 bab JB420), **11 *wiring diagram*/pinout ECU**, dan **9 spesifikasi sensor**.

**Tab 4 — Tool Diagnostik (Kalkulator Teknis Bengkel)**
- Penganalisis *Fuel Trim* (`STFT + LTFT`), Kalkulator Vakum Intake & Sensor MAP, Kalkulator *Voltage Drop* & Titik Ground, Diagram Port OBD-II DLC 16-Pin (SAE J1962), dan Pencarian Cepat Kode DTC.

## Hasil uji teknis internal yang SUDAH ADA (boleh dipakai sebagai data)
1. Uji paritas mesin diagnosa Python vs JavaScript offline pada 17 kasus: **17/17 lulus**; selisih skor **0,00%–0,10%** (batas toleransi ±0,5%).
2. Uji 10 kueri pencarian manual/DTC/pinout offline (`P0122`, `P0480 kipas`, `MAF`, `O2 heater P0037`, `pinout C37`, `TCM E92`, `ECT suhu`, `P0300 misfire`, `C1021 ABS`, `B1133 BCM`): **10/10 lulus**.
3. Uji tampilan layar HP lebar 360, 393, dan 412 px di 4 tab: **0 scroll menyamping**.
4. Build APK otomatis di GitHub Actions sukses (`v1.2.0-offline` dan perbaikan tampilan portrait/landscape `v1.2.1-offline`).

## Di luar ruang lingkup (jangan dibahas sebagai fitur utama)
- Versi server web internal yang memuat modul Work Order/PKB, gudang sparepart, kasir/POS (PPN 11%), dan pembaruan bobot *self-learning* EMA. Boleh disinggung singkat sebagai latar arsitektur, BUKAN objek penelitian.
- Tidak ada koneksi Bluetooth/Wi-Fi langsung ke *dongle* OBD-II, tidak ada API ChatGPT/Gemini/LLM online, dan tidak ada *Machine Learning/Neural Network*.

# ATURAN PENULISAN (WAJIB)
1. **Konsisten 4D adaptasi industri bengkel**:
   - Define: analisis awal-akhir (masalah pembacaan DTC, keterbatasan manual repair, dan kesenjangan manual vs lapangan di bengkel), analisis pengguna (mekanik), analisis tugas (alur troubleshooting), analisis konsep (EFI, DTC, manual, basis kasus), perumusan tujuan produk. JANGAN menulis analisis kurikulum, silabus, RPP, atau siswa.
   - Design: penyusunan instrumen penilaian, pemilihan media (Android offline), pemilihan format (4 tab), rancangan awal (alur integrasi manual + pengalaman mekanik, basis data, antarmuka).
   - Develop: validasi ahli (materi otomotif & media) + praktisi senior → revisi → uji teknis → uji coba terbatas (Indah Jaya Motor) → revisi → uji coba lapangan (gabungan mekanik kedua bengkel).
   - Disseminate: pengemasan APK final + panduan instalasi, penyebaran terbatas ke kedua bengkel (penekanan adopsi eksternal di SMS Performance).
2. **Sudut pandang Teknik Mesin Otomotif**: tonjolkan pemahaman deskripsi DTC, standar pengecekan, pembacaan *wiring*, analisis *Fuel Trim*, prosedur ukur multimeter, sinergi standar pabrikan dengan pengalaman lapangan mekanik, serta efisiensi & keselamatan kerja bengkel. Hindari listing kode pemrograman panjang.
3. **Anti-fabrikasi**:
   - Jangan mengarang angka validasi, skor angket, skor SUS, waktu troubleshooting, nama orang, atau jumlah responden. Tulis: `[DATA LAPANGAN PERLU DIUKUR PENULIS: instrumen & cara ukur]`.
   - Jangan mengarang referensi (judul, penulis, tahun, DOI). Tulis: `[BUTUH SITASI: kata kunci pencarian + jenis sumber]`. Hanya kutip sumber asli yang saya tempelkan.
   - Jangan mengklaim kilometer sudah masuk bobot rumus skor otomatis jika di Ground Truth dijelaskan sebagai indikator kategori servis/pencatatan odometer.
4. **Bahasa**: Bahasa Indonesia baku (EYD V), kalimat pasif/impersonal (tanpa "saya/kami"), paragraf deduktif, lugas, istilah asing dicetak miring.
5. **Format keluaran**: siap salin ke Word — sub-bab bernomor, paragraf utuh, tabel Markdown, rumus jelas.
6. **Bertahap**: kerjakan HANYA bagian yang saya minta. Di akhir setiap jawaban selalu tampilkan:
   - **Daftar Placeholder** (`[BUTUH SITASI]` & `[DATA LAPANGAN]`).
   - **Antisipasi Pertanyaan Penguji** (2–3 pertanyaan kritis + arah jawaban), termasuk soal objektivitas bengkel sendiri bila relevan.

Jika paham, jawab singkat: **"Siap. Silakan kirim prompt bagian pertama."**
```

---

## 1. PROMPT JUDUL & KERANGKA

### P1 — Finalisasi Judul & Peta Penelitian
```markdown
Berdasarkan Master Prompt dan cerita akar masalah bengkel saya, kerjakan:
1. Evaluasi judul sementara saya dan berikan 3 alternatif judul terbaik (maksimal 25 kata) yang mencerminkan unsur penting: (a) produk Android offline AGOS, (b) penggabungan standar Manual Repair & pengalaman kasus mekanik, (c) model 4D, dan (d) sasaran mekanik bengkel mobil umum.
2. Tabel "Benang Merah": Masalah Nyata di Bengkel → Fitur Solusi AGOS → Rumusan Masalah → Tujuan → Instrumen → Teknik Analisis → Output di BAB IV.
3. Daftar istilah kunci (glosarium singkat) yang akan konsisten dipakai di seluruh skripsi (misal: scan tool, DTC, Manual Repair, wiring diagram, Live Data, Fuel Trim, kasus historis, offline).
```

---

## 2. PROMPT BAB I — PENDAHULUAN

### P2 — 1.1 Latar Belakang Masalah
```markdown
Tulis sub-bab **1.1 Latar Belakang Masalah** (±4–6 halaman, 9–12 paragraf) mengikuti alur nyata cerita lapangan saya secara deduktif (piramida terbalik):
1. Perkembangan sistem EFI & OBD-II menuntut mekanik bengkel umum tidak hanya membaca kode kesalahan, tetapi memahami mekanisme gangguan dan standar pengecekan pabrikan.
2. Kondisi lapangan di bengkel mobil umum non-resmi: menerima beragam merek kendaraan namun tidak semuanya memiliki koleksi *Manual Repair Book* pabrikan sesuai model mobil.
3. Temuan observasi awal di **Bengkel Mobil Indah Jaya Motor** (dan observasi pembanding di **Bengkel SMS Performance**): mekanik mampu membaca kode DTC dari *scan tool*, tetapi kesulitan mendeskripsikan arti teknis kode DTC, mengetahui standar pengecekan, dan membaca *wiring diagram* kode DTC tanpa membuka *Manual Repair* sesuai model kendaraan `[DATA LAPANGAN: hasil observasi & wawancara awal]`.
4. Masalah kesenjangan lapangan: solusi kerusakan mobil dengan kode DTC dan keluhan pelanggan tertentu terkadang tidak sama persis dengan prosedur di *manual book*, sehingga pengalaman nyata mekanik dalam menyelesaikan gangguan terdahulu (termasuk kesamaan model, keluhan, dan kategori kilometer kendaraan) sangat berharga jika terdokumentasi dan dapat dicari kembali.
5. Kendala teknis di area kerja bengkel: file manual PDF tebal lambat dicari di samping unit, sementara sinyal internet bengkel tidak selalu stabil untuk layanan *cloud*.
6. Solusi yang sudah ada (scan tool biasa, PDF manual, forum mekanik, aplikasi daring berbayar) beserta kekurangannya.
7. Gagasan penggabungan **standar pengecekan *Manual Repair* pabrikan + basis pengalaman nyata mekanik** ke dalam aplikasi Android 100% offline (*AGOS Smart Diagnostik*).
8. Alasan memilih metode R&D Model 4D adaptasi industri bengkel dengan dua bengkel mitra (internal & eksternal independen).
9. Paragraf penutup yang mengarah langsung ke judul penelitian.
Sertakan `[BUTUH SITASI: ...]` pada setiap klaim teori/data eksternal.
```

### P3 — 1.2 Identifikasi Masalah
```markdown
Tulis **1.2 Identifikasi Masalah**: 6–8 butir masalah konkret yang langsung diturunkan dari 1.1 (mencakup kendala deskripsi kode DTC pasca-scanning, keterbatasan akses *Manual Repair* & *wiring* di bengkel non-resmi, perbedaan solusi lapangan vs *manual book*, belum terdokumentasinya pengalaman kasus mekanik secara terstruktur, dan keterbatasan sinyal internet area bengkel).
```

### P4 — 1.3 Batasan Masalah
```markdown
Tulis **1.3 Batasan Masalah** dalam dua kelompok tegas:
a) **Ruang lingkup yang dibahas:** produk APK Android offline 4 tab sesuai Ground Truth (integrasi pencarian *Manual Repair* JB420 + pencocokan kasus pengalaman mekanik + simulator *wiring* & multimeter + kalkulator teknis), input *Live Data* & kilometer manual dari *scan tool*/odometer, studi kasus manual lengkap Suzuki Grand Vitara JB420 dengan basis kasus awal 6 merek, uji coba pada mekanik Bengkel Mobil Indah Jaya Motor dan Bengkel SMS Performance.
b) **Ruang lingkup yang tidak dibahas:** modul versi server web (PKB/Work Order, gudang sparepart, kasir POS/PPN 11%, *self-learning* EMA), koneksi nirkabel Bluetooth/Wi-Fi ke *dongle* OBD-II, layanan AI daring, serta perhitungan bobot otomatis kilometer pada rumus skor (kilometer dibatasi sebagai klasifikasi usia/servis dan pencatatan riwayat odometer).
Sertakan alasan singkat dan logis untuk tiap batasan.
```

### P5 — 1.4 Rumusan Masalah
```markdown
Tulis **1.4 Rumusan Masalah** (3–4 butir kalimat tanya yang terukur) meliputi:
1. Proses pengembangan aplikasi *AGOS Smart Diagnostik* berbasis Android offline (integrasi standar *Manual Repair* dan pengalaman mekanik) menggunakan model 4D.
2. Tingkat kelayakan produk menurut Ahli Materi Otomotif dan Ahli Media/Aplikasi (serta praktisi senior bila ada).
3. Tingkat kepraktisan dan penerimaan mekanik pada Bengkel Mobil Indah Jaya Motor dan Bengkel SMS Performance.
4. *(Opsional)* Kinerja aplikasi dalam ketepatan rekomendasi kasus/pencarian manual dan efektivitas waktu serta ketepatan *troubleshooting* mekanik.
Tunjukkan instrumen penjawab masing-masing butir.
```

### P6 — 1.5 Tujuan Penelitian
```markdown
Tulis **1.5 Tujuan Penelitian** yang berpasangan satu-satu dengan 1.4 (jumlah, urutan, dan fokus selaras; gunakan kata kerja operasional: mengembangkan/menghasilkan, mengetahui, mengukur).
```

### P7 — 1.6 Manfaat Penelitian
```markdown
Tulis **1.6 Manfaat Penelitian**:
a) Manfaat teoretis (pengembangan ilmu Pendidikan Teknik Mesin/otomotif dan penerapan R&D 4D untuk alat bantu kerja bengkel yang menggabungkan pengetahuan standar pabrikan dan pengalaman empiris mekanik).
b) Manfaat praktis bagi: mekanik bengkel umum (khususnya mekanik junior), pengelola Bengkel Mobil Indah Jaya Motor & Bengkel SMS Performance, program studi Pendidikan Teknik Mesin, dan peneliti selanjutnya.
```

### P8 — 1.7 Spesifikasi Produk & 1.8 Asumsi-Keterbatasan Pengembangan
```markdown
(Gunakan bila pedoman R&D kampus memintanya.)
1. Tulis **1.7 Spesifikasi Produk yang Diharapkan** dalam bentuk tabel lengkap sesuai Ground Truth (nama, platform Android offline Capacitor, ukuran APK `[DATA LAPANGAN]`, versi Android minimal `[DATA LAPANGAN]`, 4 tab beserta fungsi inti, kapasitas data bawaan: 17 kasus 6 merek, 1.381 potongan manual JB420, 208 DTC, 11 wiring, 9 spesifikasi sensor, 7 simulator sirkuit multimeter, 7 simulator komponen EFI, 5 tool diagnostik).
2. Tulis **1.8 Asumsi dan Keterbatasan Pengembangan**: asumsi (mekanik memiliki ponsel Android dan *scan tool* bengkel, data manual JB420 sesuai terbitan pabrikan) dan keterbatasan jujur (17 kasus historis awal, manual lengkap baru studi kasus JB420, input *Live Data* manual, kilometer berfungsi sebagai kategori servis/odometer belum masuk bobot matematis, penyimpanan kasus tambahan lokal per perangkat).
```

---

## 3. PROMPT BAB II — KAJIAN PUSTAKA

> Tips: kumpulkan jurnal/buku asli terlebih dahulu, lalu gunakan **PROMPT S1** agar sitasi 100% nyata.

### P9 — Kerangka BAB II
```markdown
Susun **kerangka BAB II** (sampai sub-subbab tingkat 3) yang mendukung seluruh konsep di judul dan rumusan masalah. Untuk tiap sub-bab cantumkan: fokus isi, 2–3 kata kunci pencarian referensi (Indonesia & Inggris), serta jenis sumber ideal (buku teks otomotif, manual pabrikan, standar SAE/ISO, jurnal SINTA/Scopus 2019–2026).
```

### P10 — 2.1 Sistem EFI (Electronic Fuel Injection)
```markdown
Tulis **2.1 Sistem Electronic Fuel Injection (EFI)**: prinsip kerja sistem manajemen mesin elektronik, peran ECU/ECM, 8 subsistem kendaraan yang dipantau dalam diagnosa, serta fungsi dan karakteristik 7 komponen utama di aplikasi (MAF, O2/HO2S, ECT, MAP, CKP, Throttle Body ETC/TPS, Ignition Coil COP). Sertakan tabel ringkasan sensor/aktuator beserta jenis sinyal dan rentang nilai umumnya. Tandai `[BUTUH SITASI]` pada angka referensi.
```

### P11 — 2.2 Scan Tool OBD-II dan Interpretasi Kode DTC
```markdown
Tulis **2.2 Scan Tool OBD-II dan Interpretasi Kode Diagnostic Trouble Code (DTC)**: fungsi *scan tool* di bengkel umum, standar SAE J1962 (port DLC 16-pin) & SAE J2012/ISO 15031-6, struktur 5 karakter kode DTC (P/C/B/U, generik vs spesifik pabrikan), contoh kode pada aplikasi (`P0122`, `P0300`, `P0480`, `P0171`), serta **alasan mengapa membaca kode DTC saja di *scan tool* belum cukup** (kode DTC hanya menunjuk sirkuit/area gangguan sehingga tetap memerlukan deskripsi teknis, nilai standar pengecekan, dan *wiring diagram*).
```

### P12 — 2.3 Live Data OBD-II dan Analisis Fuel Trim
```markdown
Tulis **2.3 Live Data OBD-II dan Analisis Fuel Trim**: pengertian *Live Data*/PID, makna *STFT* & *LTFT* (campuran *lean* vs *rich*), batas kerja normal umum, keterkaitan 7 parameter *Live Data* (STFT, LTFT, RPM, O2, MAP, MAF, ECT) dalam memverifikasi kebenaran gangguan di lapangan, serta tabel interpretasi pola gangguan (misal kebocoran vakum vs suplai bahan bakar lemah vs sensor MAF kotor). Beri `[BUTUH SITASI]`.
```

### P13 — 2.4 Troubleshooting, Pengukuran Kelistrikan, dan Pengaruh Kilometer/Usia Pakai
```markdown
Tulis **2.4 Prosedur Troubleshooting, Pengukuran Kelistrikan, dan Peran Riwayat Kilometer Kendaraan**: alur sistematis *troubleshooting* (keluhan → *scan* DTC → *Live Data* → pemeriksaan standar manual & pengukuran multimeter → perbaikan → verifikasi/Reset ECU & *Idle Relearn*), tata cara pengukuran multimeter digital (tegangan, tahanan, kontinuitas, *voltage drop*, uji vakum), keselamatan kerja (K3) pengukuran pada sirkuit ECU, serta pengaruh usia/kilometer tempuh terhadap pola keausan komponen (karet/selang vakum, sensor, koil, *carbon deposit*) yang kerap membuat solusi lapangan berbeda dari teori ideal.
```

### P14 — 2.5 Manual Repair Pabrikan, Wiring Diagram, dan Tantangan Bengkel Umum Non-Resmi
```markdown
Tulis **2.5 Manual Repair Pabrikan, Wiring Diagram, dan Tantangan Bengkel Umum Non-Resmi**: kedudukan *Service Manual* sebagai standar pengecekan resmi (spesifikasi tahanan/voltase, alur cek per DTC, *pinout* soket ECU seperti kode konektor C37/E23, torsi), cara membaca *wiring diagram*, kendala nyata bengkel umum non-resmi (tidak semua bengkel memiliki manual tiap model mobil, dokumen PDF ribuan halaman lambat dicari), serta alasan pemilihan *Service Manual* Suzuki Grand Vitara JB420 Vol. 1 & 2 sebagai studi kasus referensi penuh dalam aplikasi.
```

### P15 — 2.6 Penggabungan Standar Manual dan Pengalaman Mekanik melalui Weighted Case-Based Reasoning (CBR)
```markdown
Tulis **2.6 Integrasi Pengetahuan Standar dan Pengalaman Mekanik Berbasis Weighted Case-Based Reasoning (CBR)** dengan bahasa yang mudah dipahami dosen Teknik Mesin:
- Konsep pengetahuan eksplisit/normatif (*Manual Repair* pabrikan) vs pengetahuan empiris/pengalaman lapangan mekanik (*historical cases*), dan mengapa penggabungan keduanya menyelesaikan kesenjangan solusi di lapangan.
- Siklus CBR 4R (*Retrieve, Reuse, Revise, Retain*) dan pemetaannya pada aplikasi AGOS (mencari kasus mirip → merujuk solusi + SOP manual → menyesuaikan di kendaraan → menyimpan kasus baru ke Tab Data Kasus).
- Uraian rumus `TextScore`, normalisasi istilah bengkel Indonesia, `LiveScore` 7 parameter, dan `Skor Total` (`0,85 × TextScore + 0,15 × LiveScore`) persis sesuai Ground Truth (notasi matematis rapi + arti simbol), plus penjelasan jujur peran klasifikasi kilometer sebagai informasi konteks servis/odometer.
- Alasan memilih metode berbobot yang transparan dibanding *Machine Learning* untuk konteks bengkel offline.
```

### P16 — 2.7 Aplikasi Android Berbasis Offline untuk Lingkungan Bengkel
```markdown
Tulis **2.7 Aplikasi Mobile Android Berbasis Offline**: konsep *offline-first*, teknologi aplikasi *hybrid* berbasis WebView/Capacitor, kelebihannya bagi area kerja bengkel (nol ketergantungan internet, respons cepat, tanpa biaya API/langganan), dukungan orientasi Portrait/Landscape di samping kap mesin, serta mekanisme dan keterbatasan penyimpanan lokal (`localStorage`). Ringkas, tanpa kode program.
```

### P17 — 2.8 Penelitian dan Pengembangan Model 4D (Adaptasi Industri Bengkel)
```markdown
Tulis **2.8 Penelitian dan Pengembangan Model 4D**: pengertian R&D, model 4D Thiagarajan dkk. (1974), perbandingan ringkas dengan ADDIE dan Borg & Gall (tabel), alasan pemilihan model 4D, serta tabel pemetaan adaptasi 4D dari konteks perangkat pembelajaran ke konteks pengembangan alat bantu kerja mekanik bengkel (Define–Design–Develop–Disseminate).
```

### P18 — 2.9 Kelayakan, Kepraktisan, dan System Usability Scale (SUS)
```markdown
Tulis **2.9 Kelayakan dan Kepraktisan Produk**: konsep validasi kelayakan oleh ahli materi otomotif (kebenaran spesifikasi, deskripsi DTC, *wiring*, K3) dan ahli media (antarmuka, navigasi, simulator, stabilitas offline), konsep kepraktisan/*usability* (ISO 9241-11), skala Likert, serta *System Usability Scale* (SUS, Brooke 1996) beserta aturan penskoran.
```

### P19 — 2.10 Penelitian yang Relevan
```markdown
Saya tempelkan [JUMLAH] ringkasan/abstrak penelitian relevan yang ASLI di bawah ini:
[TEMPEL DI SINI: judul, penulis, tahun, jurnal, metode, hasil]

Tulis **2.10 Penelitian yang Relevan**:
1. Uraian naratif tiap penelitian (persamaan & perbedaannya dengan penelitian ini).
2. Tabel pembanding: Peneliti/Tahun | Produk | Metode | Subjek | Sumber Pengetahuan (Manual/Pengalaman) | Online/Offline | Hasil | Pembeda Penelitian Ini.
3. Paragraf penegasan kebaruan penelitian ini (penggabungan standar *Manual Repair* + pengalaman kasus mekanik dalam 1 APK offline).
DILARANG menambah penelitian di luar yang saya tempelkan.
```

### P20 — 2.11 Kerangka Berpikir & 2.12 Pertanyaan Penelitian
```markdown
Tulis:
1. **2.11 Kerangka Berpikir**: alur dari kondisi awal di bengkel (scan tool hanya tampil kode → butuh manual & wiring → solusi lapangan kadang berbeda dari manual → bengkel umum tidak semua punya manual & sinyal terbatas) → solusi pengembangan *AGOS Smart Diagnostik* berbasis 4D (penggabungan standar manual + pengalaman mekanik secara offline) → kondisi yang diharapkan (pemahaman DTC, standar cek, wiring, dan penelusuran solusi lebih cepat dan tepat). Sertakan diagram alur format **Mermaid (`flowchart TD`)**.
2. **2.12 Pertanyaan Penelitian** (jika pedoman kampus memakai pertanyaan penelitian): turunan terukur dari rumusan masalah.
```

---

## 4. PROMPT BAB III — METODE PENELITIAN

### P21 — 3.1 Jenis & Model Penelitian, 3.2 Tempat & Waktu
```markdown
Tulis:
1. **3.1 Jenis dan Model Penelitian**: R&D model 4D (Thiagarajan dkk., 1974) yang diadaptasi untuk industri bengkel, beserta alasan pemilihannya.
2. **3.2 Tempat dan Waktu Penelitian**: profil singkat dan pembagian peran **Bengkel Mobil Indah Jaya Motor** dan **Bengkel SMS Performance** (alamat `[ISI]`), serta tabel jadwal kegiatan per tahap 4D (bulan `[ISI]`).
```

### P22 — 3.3.1 Prosedur Pengembangan: Tahap Define
```markdown
Tulis **3.3.1 Tahap Define (Pendefinisian)** untuk konteks dua bengkel mitra:
a) Analisis awal-akhir (*front-end analysis*): kendala interpretasi kode DTC dari *scan tool*, akses *Manual Repair* & *wiring*, perbedaan solusi lapangan vs manual, serta keterbatasan sinyal internet.
b) Analisis pengguna (mekanik): latar pengalaman (junior/senior), alat kerja (*scan tool*, multimeter), kebiasaan menyimpan riwayat kasus, dan penggunaan ponsel Android.
c) Analisis tugas: tahapan nyata *troubleshooting* EFI mulai dari keluhan pelanggan hingga verifikasi pascaperbaikan.
d) Analisis konsep: struktur materi teknis EFI, OBD-II/DTC, *Live Data*, *Manual Repair* JB420, serta struktur dokumentasi kasus pengalaman mekanik (termasuk kategori kilometer).
e) Perumusan tujuan pengembangan produk.
Untuk tiap langkah sebutkan teknik pengumpulan data, sumber data, dan luaran.
```

### P23 — 3.3.2 Prosedur Pengembangan: Tahap Design
```markdown
Tulis **3.3.2 Tahap Design (Perancangan)**:
a) Penyusunan instrumen penilaian & skenario acuan uji.
b) Pemilihan media: aplikasi Android 100% offline berbasis Capacitor dan alasannya bagi bengkel umum.
c) Pemilihan format: rancangan 4 tab terintegrasi (Diagnosa Cepat + Simulator Wiring/Multimeter, Data Kasus Pengalaman Mekanik, Manual & Simulator 7 Komponen, Tool Diagnostik).
d) Rancangan awal (*initial design*): flowchart penggunaan oleh mekanik di samping mobil, flowchart mesin pencocokan kasus berbobot & pencarian manual lokal, struktur data (17 kasus, 1.381 potongan manual, 208 DTC, 11 wiring, 9 sensor), serta rancangan antarmuka. Sertakan diagram dalam format **Mermaid**.
```

### P24 — 3.3.3 Prosedur Pengembangan: Tahap Develop
```markdown
Tulis **3.3.3 Tahap Develop (Pengembangan)** secara berurutan:
1. Realisasi produk (Draf I) dan pengujian teknis internal (paritas Python–JS 17 kasus, 10 kueri pencarian offline, responsivitas layar 360/393/412 px, uji *black-box*, uji mode pesawat).
2. Validasi ahli materi otomotif, ahli media, dan praktisi senior (kepala mekanik eksternal) → revisi (Draf II).
3. Uji coba terbatas pada mekanik Bengkel Mobil Indah Jaya Motor (`n = [ISI]`) → revisi (Draf III).
4. Uji coba lapangan pada gabungan mekanik kedua bengkel (`n = [ISI]`) dengan angket kepraktisan anonim, kuesioner SUS, dan *[jika digunakan]* uji skenario waktu & ketepatan *troubleshooting* → produk akhir.
Sertakan diagram alur tahap Develop (Mermaid) dan kriteria kelayakan untuk lanjut/revisi.
```

### P25 — 3.3.4 Prosedur Pengembangan: Tahap Disseminate
```markdown
Tulis **3.3.4 Tahap Disseminate (Penyebaran)**: pengemasan file akhir `AGOS-Smart-Diagnostik-Offline.apk` beserta panduan instalasi & penggunaan, penyebaran terbatas ke kedua bengkel mitra (dengan penekanan adopsi eksternal di Bengkel SMS Performance), serta bukti dokumentasi penyebaran (berita acara serah terima, daftar perangkat terpasang, foto kegiatan).
```

### P26 — 3.4 Desain Uji Coba, Subjek, & Pengendalian Objektivitas
```markdown
Tulis **3.4 Desain Uji Coba dan Subjek Penelitian**:
a) Desain uji coba terbatas & uji coba lapangan, serta (bila dipakai) desain uji skenario berpasangan *tanpa aplikasi vs dengan aplikasi* (*within-subject*) dengan pengacakan urutan (*counterbalancing*) untuk mengurangi bias belajar.
b) Subjek uji coba: kriteria & jumlah validator serta mekanik di Indah Jaya Motor dan SMS Performance (`[ISI]`), teknik penentuan subjek (*purposive*/sampling jenuh).
c) Jenis data: kualitatif dan kuantitatif.
d) **Strategi pengendalian bias/objektivitas** (mengingat Indah Jaya Motor merupakan bengkel milik peneliti): pemisahan peran dua bengkel, pengisian angket anonim, validasi dosen independen, perbandingan skor internal vs eksternal (SMS Performance), dan penggunaan pengukuran objektif (ceklis & *stopwatch*).
```

### P27 — 3.5 Instrumen Penelitian (Kisi-kisi)
```markdown
Tulis **3.5 Instrumen Penelitian** dengan tabel kisi-kisi (Aspek | Indikator | Nomor Butir | Jumlah) untuk:
1. Pedoman observasi & wawancara tahap Define (khusus menggali kendala deskripsi DTC, akses manual/wiring, kesenjangan manual vs lapangan, dan dokumentasi pengalaman mekanik).
2. Lembar validasi Ahli Materi Otomotif (kebenaran deskripsi DTC, spesifikasi standar *Manual Repair*, ketepatan *wiring* & langkah multimeter, relevansi kasus pengalaman mekanik, K3).
3. Lembar validasi Ahli Media/Aplikasi (antarmuka HP, navigasi 4 tab, keterbacaan simulator SVG, kinerja 100% offline).
4. Angket kepraktisan mekanik (kemudahan, kebermanfaatan integrasi manual & pengalaman, efisiensi waktu, kepuasan).
5. Kuesioner SUS 10 butir (Bahasa Indonesia).
6. *(Opsional)* Lembar skenario uji waktu & ketepatan *troubleshooting*.
```

### P28 — 3.6 Validitas-Reliabilitas & 3.7 Teknik Analisis Data
```markdown
Tulis:
1. **3.6 Validitas dan Reliabilitas Instrumen**: validitas isi melalui *expert judgement* (dan indeks Aiken's V bila diminta dosen), serta penjelasan reliabilitas (*Cronbach's Alpha* atau pertimbangan ukuran sampel kecil mekanik).
2. **3.7 Teknik Analisis Data**:
   a) Analisis kualitatif (reduksi, penyajian, penarikan simpulan atas saran ahli & mekanik).
   b) Kelayakan & kepraktisan: `Persentase = (Σ skor diperoleh / Σ skor maksimal) × 100%` + tabel kategori kelayakan `[BUTUH SITASI acuan kategori sesuai dosen]`.
   c) Skor SUS: butir ganjil `(skor − 1)`, butir genap `(5 − skor)`, jumlah `× 2,5`; interpretasi `≥ 68` di atas rata-rata `[BUTUH SITASI Brooke/Bangor]`.
   d) *(Bila diuji)* Top-1 & Top-3 *Accuracy* untuk kasus uji baru; *Precision@3* untuk pencarian manual; statistik deskriptif & uji beda berpasangan (*paired t-test* / *Wilcoxon signed-rank*) untuk selisih waktu *troubleshooting*.
   Tulis semua rumus dengan keterangan simbol yang jelas.
```

---

## 5. PROMPT PEMBUATAN INSTRUMEN (LAMPIRAN)

### P29 — Pedoman Observasi & Wawancara (Define)
```markdown
Buat **pedoman observasi** (lembar ceklis) dan **pedoman wawancara semi-terstruktur** (12–15 pertanyaan) untuk pemilik/kepala mekanik dan mekanik di Bengkel Mobil Indah Jaya Motor serta Bengkel SMS Performance. Pertanyaan wajib menggali: alur saat *scan tool* memunculkan kode DTC, kendala mendeskripsikan arti DTC & membaca *wiring*, ketersediaan *Manual Repair Book* di bengkel, pengalaman saat solusi lapangan berbeda dari *manual book*, cara mengingat/mencatat kasus terdahulu (termasuk kilometer), kondisi sinyal internet, dan harapan terhadap aplikasi offline. Gunakan bahasa santai-profesional khas bengkel.
```

### P30 — Lembar Validasi Ahli Materi Otomotif
```markdown
Buat **lembar validasi Ahli Materi Otomotif** siap cetak: identitas validator, petunjuk pengisian, 15–20 butir pernyataan per aspek sesuai P27 (skala `[1–4/1–5]`), kolom komentar per aspek, saran perbaikan, dan kesimpulan kelayakan. Setiap butir harus spesifik ke fitur nyata AGOS (deskripsi kode DTC, standar tahanan/voltase sensor, *wiring* & *pinout* soket 2–6 kabel, simulasi probe multimeter Normal vs *Fault*, kalkulator *Fuel Trim/MAP/Voltage Drop*, dan kesesuaian logika kasus pengalaman mekanik).
```

### P31 — Lembar Validasi Ahli Media/Aplikasi
```markdown
Buat **lembar validasi Ahli Media/Aplikasi** siap cetak (15–20 butir, skala `[1–4/1–5]`), mencakup tata letak di layar HP (Portrait & Landscape), navigasi 4 tab, kejelasan diagram *wiring*/peta *Engine Bay*/multimeter virtual, kemudahan menambah & mencari kasus, stabilitas 100% offline, dan kemudahan instalasi APK.
```

### P32 — Angket Kepraktisan Mekanik + Kuesioner SUS
```markdown
Buat:
1. **Angket kepraktisan mekanik** (15–20 butir dengan bahasa lapangan yang mudah dipahami) dilengkapi identitas ANONIM (asal bengkel, lama pengalaman kerja, level mekanik junior/senior). Sertakan butir yang khusus menilai manfaat penggabungan *Manual Repair* dan catatan kasus pengalaman mekanik.
2. **Kuesioner SUS 10 butir** versi Bahasa Indonesia skala 1–5 (urutan & polaritas positif/negatif dipertahankan sesuai standar).
3. Kolom masukan/saran terbuka.
```

### P33 — Skenario Uji Troubleshooting (Opsional, Sangat Kuat di Sidang)
```markdown
Buat **4–6 skenario uji *troubleshooting*** yang seluruh jawabannya tersedia pada data aktual aplikasi AGOS (DTC, manual JB420, *pinout*/spesifikasi sensor, *Fuel Trim*, dan kasus historis). Misal: menelusuri arti, standar cek, dan jalur *wiring* kode `P0480` (kipas radiator), standar & prosedur ukur sensor ECT, analisis *STFT/LTFT* positif tinggi saat *idle* (kebocoran vakum), pencarian lokasi & *pinout* sensor MAP, serta penelusuran kasus `P0300` *misfire*.
Lengkapi tiap skenario dengan: narasi keluhan & hasil *scan tool*, jawaban acuan + rujukan fitur/manual, ceklis langkah benar, kolom catat waktu (*tanpa aplikasi* vs *dengan aplikasi*), dan skema *counterbalancing*. Beri tanda `[VERIFIKASI MANUAL]` pada angka teknis yang harus saya cocokkan ulang ke PDF asli.
```

---

## 6. PROMPT BAB IV — HASIL PENELITIAN DAN PEMBAHASAN

> Sebelum menjalankan P34–P42, lengkapi dulu **Template Data Lapangan (Bagian 7)** dengan data asli dari kedua bengkel.

### P34 — 4.1 Hasil Tahap Define
```markdown
Ini data asli hasil tahap Define saya: [TEMPEL BAGIAN A TEMPLATE DATA LAPANGAN].
Tulis **4.1 Hasil Tahap Define**: analisis awal-akhir, analisis pengguna (mekanik), analisis tugas, analisis konsep, dan tujuan pengembangan produk. Buat tabel perbandingan temuan Bengkel Mobil Indah Jaya Motor vs Bengkel SMS Performance (khususnya soal kendala deskripsi DTC, ketersediaan *Manual Repair*, kesenjangan solusi manual vs lapangan, dan sinyal internet). Gunakan HANYA data yang saya berikan.
```

### P35 — 4.2 Hasil Tahap Design
```markdown
Tulis **4.2 Hasil Tahap Design**: instrumen penilaian yang disusun, alasan pemilihan media Android offline & format 4 tab, rancangan integrasi basis *Manual Repair* dengan basis pengalaman mekanik, rancangan antarmuka, dan penanda `[GAMBAR 4.x: deskripsi tangkapan layar]` untuk gambar yang akan saya sisipkan.
```

### P36 — 4.3.1 Realisasi Produk & 4.3.2 Hasil Uji Teknis Internal
```markdown
Tulis **4.3.1 Realisasi Produk (Draf I)** sesuai Ground Truth (dengan penanda `[GAMBAR 4.x]`) dan **4.3.2 Hasil Uji Teknis Internal** dalam tabel rapi: uji paritas 17 kasus Python vs JS (0,00%–0,10%), uji 10 kueri pencarian offline (10/10), uji layar HP 360/393/412 px (0 overflow), ditambah hasil uji lapangan teknis saya: [TEMPEL BAGIAN B: spesifikasi HP uji, ukuran APK, waktu muat, *black-box*, uji mode pesawat].
```

### P37 — 4.3.3 Hasil Validasi Ahli & Revisi Produk
```markdown
Ini skor dan saran validator saya: [TEMPEL BAGIAN C].
Tulis **4.3.3 Hasil Validasi Ahli**: tabel skor per aspek, perhitungan persentase eksplisit, dan kategori kelayakan untuk Ahli Materi Otomotif, Ahli Media, dan Praktisi Senior; ringkasan masukan; serta **tabel revisi produk** (Masukan Validator | Tindakan Perbaikan | Kondisi Sebelum | Kondisi Sesudah) disertai penanda `[GAMBAR sebelum/sesudah]`.
```

### P38 — 4.3.4 Hasil Uji Coba Terbatas (Bengkel Mobil Indah Jaya Motor)
```markdown
Ini data uji coba terbatas di Bengkel Mobil Indah Jaya Motor: [TEMPEL BAGIAN D].
Tulis **4.3.4 Hasil Uji Coba Terbatas**: profil responden anonim, hasil skor kepraktisan per aspek & kategori, skor SUS per responden & rerata, temuan kendala saat dipakai di dekat mobil, dan revisi yang dilakukan sebelum uji lapangan.
```

### P39 — 4.3.5 Hasil Uji Coba Lapangan (Gabungan Dua Bengkel)
```markdown
Ini data uji coba lapangan gabungan dua bengkel: [TEMPEL BAGIAN E].
Tulis **4.3.5 Hasil Uji Coba Lapangan**: profil responden kedua bengkel, skor kepraktisan per aspek (gabungan dan perbandingan Indah Jaya Motor vs SMS Performance), skor SUS (gabungan dan per bengkel), serta analisis singkat ada-tidaknya perbedaan mencolok antara bengkel internal dan eksternal sebagai bukti objektivitas.
```

### P40 — 4.3.6 Hasil Uji Kinerja (Akurasi & Efektivitas Waktu) — jika dilakukan
```markdown
Ini data uji kinerja saya: [TEMPEL BAGIAN F].
Tulis **4.3.6 Hasil Uji Kinerja**:
a) Top-1 & Top-3 *Accuracy* pada kasus uji baru (tabel: gejala & DTC | vonis aktual mekanik senior | peringkat hasil AGOS | tepat/tidak).
b) *Precision@3* pencarian manual/DTC/wiring (jika ada).
c) Perbandingan waktu & ketepatan *troubleshooting* tanpa vs dengan aplikasi AGOS: tabel per mekanik per skenario, rerata/median, persentase penghematan waktu, dan hasil uji statistik dari data yang saya berikan (jika belum dihitung, beri panduan langkah hitung & placeholder).
```

### P41 — 4.4 Hasil Tahap Disseminate
```markdown
Ini data penyebaran saya: [TEMPEL BAGIAN G].
Tulis **4.4 Hasil Tahap Disseminate**: pengemasan akhir APK & panduan instalasi, pelaksanaan penyebaran di Bengkel Mobil Indah Jaya Motor dan Bengkel SMS Performance, jumlah perangkat mekanik yang terpasang, respon awal saat digunakan sehari-hari, serta penanda dokumentasi `[GAMBAR]`.
```

### P42 — 4.5 Pembahasan, 4.6 Kajian Produk Akhir, & 4.7 Keterbatasan Penelitian
```markdown
Tulis:
1. **4.5 Pembahasan**: jawab tiap rumusan masalah berurutan; bahas mengapa penggabungan standar *Manual Repair* dan pengalaman kasus mekanik dalam mode offline menjawab 4 masalah awal di bengkel; kaitkan dengan teori BAB II dan penelitian relevan (P19).
2. **4.6 Kajian Produk Akhir**: kelebihan dan kekurangan aplikasi secara objektif.
3. **4.7 Keterbatasan Penelitian**: keterbatasan jumlah responden & lokasi (2 bengkel), posisi bengkel internal yang dimitigasi dengan uji eksternal, basis 17 kasus awal, manual lengkap baru Suzuki Grand Vitara JB420, input *Live Data* manual, kilometer belum masuk bobot otomatis persamaan CBR, dan penyimpanan kasus tambahan lokal di masing-masing ponsel.
```

---

## 7. TEMPLATE PENCATATAN DATA LAPANGAN (ISI SENDIRI SEBELUM BAB IV)

```markdown
## A. DEFINE (Observasi & Wawancara)
- Tanggal observasi/wawancara: Indah Jaya Motor = ... ; SMS Performance = ...
- Narasumber (kode anonim, mis. KM1, M1, M2): ...
- Merek/model mobil paling sering masuk: ...
- Alat kerja yang ada (merek/tipe scan tool, multimeter, dll.): ...
- Gambaran kendala membaca deskripsi DTC, standar cek, & wiring dari scan tool: ...
- Contoh kasus nyata di bengkel ketika solusi lapangan berbeda dari manual book: ...
- Ketersediaan Manual Repair Book di tiap bengkel & estimasi waktu mencari manual saat ini: ...
- Kondisi sinyal internet di area servis/kolong bengkel: ...
- Harapan mekanik terhadap aplikasi: ...

## B. UJI TEKNIS TAMBAHAN
- Spesifikasi HP uji (merek, tipe, RAM, versi Android): ...
- Ukuran file APK & ukuran setelah terpasang: ...
- Waktu buka aplikasi (detik, 3 kali percobaan): ...
- Waktu tampil hasil diagnosa & pencarian manual (detik/ms): ...
- Uji Black-Box (jumlah skenario uji ..., lulus ..., gagal ... + rincian): ...
- Uji Mode Pesawat (semua 4 tab berjalan normal? YA/TIDAK + catatan): ...

## C. VALIDASI AHLI
- Ahli Materi Otomotif (kode V1, V2; jabatan): skor per butir ... ; saran ...
- Ahli Media (kode V3; jabatan): skor per butir ... ; saran ...
- Praktisi Senior (kode P1; jabatan/bengkel): skor per butir ... ; saran ...

## D. UJI COBA TERBATAS (Bengkel Mobil Indah Jaya Motor)
- Jumlah responden: ... (junior ..., senior ...)
- Skor angket per responden per butir: ...
- Skor SUS per responden per butir: ...
- Kendala/masukan saat pemakaian: ...
- Revisi yang dilakukan: ...

## E. UJI COBA LAPANGAN (Gabungan Indah Jaya Motor & SMS Performance)
- Jumlah responden: Indah Jaya Motor = ... ; SMS Performance = ...
- Skor angket per responden per butir (tandai asal bengkel): ...
- Skor SUS per responden per butir (tandai asal bengkel): ...
- Masukan/saran: ...

## F. UJI KINERJA (jika dilakukan)
- Kasus uji baru: jumlah ... ; tiap kasus (model, km, keluhan/gejala, DTC, Live Data, vonis mekanik senior, peringkat AGOS): ...
- Kueri pencarian manual: jumlah ... ; tiap kueri (3 hasil teratas relevan/tidak): ...
- Uji skenario troubleshooting: tiap mekanik & skenario (waktu tanpa AGOS, waktu dengan AGOS, skor ketepatan langkah): ...
- Hasil uji statistik (jika sudah dihitung SPSS/Excel): ...

## G. DISSEMINATE
- Tanggal & bentuk penyebaran di tiap bengkel: ...
- Jumlah perangkat HP mekanik terpasang: ...
- Tanggapan awal pemakaian harian: ...
- Bukti dokumentasi (foto/berita acara: ADA/TIDAK): ...
```

---

## 8. PROMPT BAB V — SIMPULAN, IMPLIKASI, DAN SARAN

### P43 — 5.1 Simpulan
```markdown
Tulis **5.1 Simpulan**: berpasangan satu-satu dengan rumusan masalah, menyertakan angka hasil kunci dari BAB IV (kelayakan ahli, kepraktisan/SUS mekanik kedua bengkel, dan uji kinerja bila ada), padat, tanpa informasi baru.
```

### P44 — 5.2 Implikasi (jika diminta pedoman)
```markdown
Tulis **5.2 Implikasi** (2–3 paragraf): dampak praktis bagi mekanik bengkel mobil umum dalam memadukan standar pabrikan dan memori pengalaman bengkel, serta implikasi bagi Pendidikan Teknik Mesin (sarana alih kompetensi mekanik junior dan potensi pengembangan media praktik vokasi).
```

### P45 — 5.3 Saran
```markdown
Tulis **5.3 Saran**:
a) Saran pemanfaatan (untuk mekanik & pemilik bengkel umum).
b) Saran diseminasi lebih luas.
c) Saran pengembangan lanjutan yang spesifik & realistis: menambahkan basis *Manual Repair* untuk merek mobil populer lain, memperbanyak kasus historis bengkel, memasukkan parameter kilometer kendaraan sebagai variabel bobot otomatis dalam persamaan CBR, menambahkan fitur sinkronisasi/*backup* data kasus antarperangkat mekanik, integrasi pembacaan langsung *dongle* OBD-II, serta uji lapangan pada cakupan bengkel lebih luas.
```

---

## 9. PROMPT PELENGKAP, FINALISASI, & SIMULASI SIDANG

### P46 — Abstrak (Bahasa Indonesia & Bahasa Inggris)
```markdown
Berdasarkan ringkasan final BAB I–V berikut: [TEMPEL], tulis **Abstrak Bahasa Indonesia** (maksimal `[250]` kata, 1 paragraf: latar/tujuan, metode 4D, lokasi 2 bengkel & subjek mekanik, instrumen, teknik analisis, angka hasil utama, simpulan) + 3–5 kata kunci, lalu **Abstract** Bahasa Inggris akademik yang setara.
```

### P47 — Pengecekan Daftar Pustaka
```markdown
Ini daftar pustaka saya: [TEMPEL]. Dan ini daftar sitasi dalam naskah: [TEMPEL].
Periksa: (1) kesesuaian format `[APA 7/IEEE]`, (2) sitasi di teks yang hilang di daftar pustaka atau sebaliknya, (3) referensi > 10 tahun yang perlu diperbarui (kecuali sumber klasik seperti Thiagarajan 1974, Brooke 1996), (4) data pustaka belum lengkap. JANGAN menambah referensi buatan sendiri.
```

### P48 — Daftar Lampiran
```markdown
Susun **daftar lampiran** lengkap dan urut untuk skripsi R&D 4D dua bengkel (surat izin Indah Jaya Motor & SMS Performance, pedoman & ringkasan observasi/wawancara, kisi-kisi & lembar validasi terisi, angket & SUS terisi, rekap perhitungan, lembar skenario uji, laporan uji teknis paritas/kueri/layar, tangkapan layar aplikasi, panduan instalasi APK, berita acara penyebaran, foto kegiatan).
```

### P49 — Cek Konsistensi Seluruh Naskah
```markdown
Saya tempelkan naskah [bab/bagian]: [TEMPEL].
Audit konsistensinya terhadap Master Prompt dan antarbab: (1) benang merah judul–rumusan–tujuan–simpulan, (2) kesamaan angka di seluruh bab, (3) kesesuaian fitur & angka Ground Truth (17 kasus, 1.381 manual, 208 DTC, 11 wiring, 9 sensor, kilometer sebagai kategori servis/odometer bukan bobot skor), (4) bebas klaim fitur fiktif (AI online, ML, Bluetooth OBD), (5) konsistensi tahapan 4D, (6) kebakuan EYD V. Sajikan tabel: Lokasi | Temuan | Saran Perbaikan.
```

### P50 — Simulasi Sidang (Mode 3 Dosen Penguji)
```markdown
Berperanlah sebagai 3 dosen penguji: (1) ahli otomotif/EFI, (2) ahli metodologi R&D 4D & statistik, (3) ahli media/aplikasi. Ajukan 15 pertanyaan paling tajam tentang skripsi saya—wajib mencakup:
- Mengapa di Prodi Pendidikan Teknik Mesin objeknya mekanik bengkel, bukan siswa?
- Bagaimana menjamin objektivitas karena Indah Jaya Motor milik peneliti sendiri?
- Bagaimana jika pengalaman mekanik yang dimasukkan ke aplikasi justru keliru dan bertentangan dengan standar Manual Repair?
- Mengapa parameter kilometer sudah ada di form, tetapi belum masuk rumus bobot skor CBR?
- Mengapa bobot teks 0,85 dan Live Data 0,15, serta mengapa hanya 17 kasus awal dan manual lengkap baru Suzuki Grand Vitara JB420?
- Risiko hilangnya data kasus tambahan di `localStorage` dan jumlah responden mekanik yang terbatas.
Untuk tiap pertanyaan berikan: maksud penguji, jawaban ringkas 3–5 kalimat berbasis data skripsi, dan pertanyaan lanjutan. Setelah itu, uji saya satu per satu secara interaktif dan nilai jawaban saya.
```

---

## 10. PROMPT UTILITAS (PAKAI KAPAN SAJA)

### R1 — Revisi Bagian Berdasarkan Masukan Dosen
```markdown
Revisi bagian [nama sub-bab] berdasarkan catatan dosen pembimbing/saya berikut: [TEMPEL CATATAN].
Pertahankan bagian yang tidak dikritik. Tampilkan hasil revisi utuh, lalu tabel ringkas: Catatan | Perubahan yang Dilakukan.
```

### R2 — Lanjutkan Sesi di Chat Baru
```markdown
Ini lanjutan pengerjaan skripsi. Status terakhir:
- Judul final: ...
- Bab/sub-bab selesai: ...
- Keputusan penting (jumlah mekanik, skala Likert, metrik dipakai, arahan dosen): ...
- Bagian yang dikerjakan sekarang: [nomor prompt, mis. P24]
Pelajari status ini lalu jawab "Siap lanjut ke [bagian]".
```

### S1 — Sintesis Referensi Asli
```markdown
Berikut kutipan/abstrak asli dari referensi yang saya temukan: [TEMPEL + data bibliografi lengkap].
Gunakan HANYA sumber ini untuk mengganti placeholder `[BUTUH SITASI]` pada sub-bab [nama sub-bab]. Parafrasekan dengan baik, cantumkan sitasi sesuai `[APA 7/IEEE]`, dan sebutkan placeholder mana yang masih tersisa.
```

### S2 — Parafrase Naskah Sendiri
```markdown
Parafrasekan paragraf tulisan saya berikut agar lebih baku (EYD V), padat, pasif/impersonal, dan mengalir tanpa mengubah makna, angka, maupun sitasi: [TEMPEL].
```
