# ATURAN WAJIB PROYEK DIAGNOSA DTC & WIRING OEM (ZERO-HALLUCINATION)

Dokumen ini adalah aturan permanen proyek **AGOS Smart Diagnostik (Suzuki Grand Vitara JB420 / Multi-Model)** yang wajib dipatuhi oleh seluruh pengembang dan asisten AI pada setiap perubahan data DTC, pinout ECM, diagram wiring, maupun simulator soket.

---

## 1. SINGLE SOURCE OF TRUTH (REPAIR MANUAL OEM)

- **Dilarang keras menebak** jumlah pin soket, tata letak pin (`layout`), warna kabel, sumber relay/sekring, atau fungsi terminal dari pengetahuan umum/internet.
  - *Contoh pelanggaran yang dilarang:* Dilarang berasumsi A/F Sensor-1 selalu 6-pin Bosch LSU apabila manual/standar target proyek mengunci konfigurasi **4-pin (`2x2`: 2 Heater `PNK` & `PNK/BLU` + 2 Sinyal `WHT` & `BLK`)**.
- Semua data konektor (`connector.connector_code`, `connector.pin_count`, `connector.layout`, `connector.pins[]`) **wajib berasal dari Repair Manual OEM** kendaraan target yang tersimpan di direktori referensi proyek (`manual repair suzuki grand vitara 2012.pdf` Vol 1 & `grand vitara 2.pdf` Vol 2, atau manual OEM resmi model target lain).
- Tabel `wiring_pinout` wajib diturunkan langsung dari `connector.pins[]` sebagai satu sumber kebenaran (*Single Source of Truth*) agar tidak pernah terjadi ketidaksinkronan antara tabel pinout, gambar skematik, dan penampang fisik soket.

---

## 2. SHARED WIRING INHERITANCE (ANTI TEXT-ONLY CROSS-REFERENCE)

- Jika suatu kode DTC pada buku manual merujuk ke halaman kode DTC induk lain (misal: `P0102` → lihat `P0101` Hal. `1A-62`, `P0107` → lihat `P0106` Hal. `1A-68`, `P0112` → lihat `P0111` Hal. `1A-74`, `P0118` → lihat `P0116` Hal. `1A-81`, `P0403` → lihat `P0401` Hal. `1A-120`), sistem **WAJIB** menautkan dan menampilkan gambar diagram wiring OEM induk dari grup sensor terkait melalui `wiring_ref_id` pada Shared Wiring Asset Registry (`wiring_diagrams`).
- **Dilarang** me-render halaman manual yang hanya berisi teks instruksi rujukan (*"Lihat DTC P0xxx"*) sebagai gambar wiring diagram.
- UI wajib menyertakan keterangan keterkaitan lintas-kode (`wiring_cross_ref_note` & `manual_page_ref`) di bawah/atas pratinjau gambar wiring OEM agar mekanik memahami bahwa diagram tersebut dipakai bersama oleh grup sensor terkait.

---

## 3. STRICT DATA-DRIVEN SOCKET SIMULATION

- Komponen **Simulasi Jalur Wiring & Soket** (`backend/app/static/index.html` & `android_offline/www/index.html`) **WAJIB** me-render jumlah kabel, titik probe, dan rongga pin konektor secara 100% dinamis dari `advice.connector.pins` dan `advice.connector.layout` (`1x1`, `1x2`, `1x3`, `1x4`, `2x2`, `1x5`, `2x3`, `1x6`, `2x4`).
- **Dilarang** meng-hardcode override jumlah pin di layer UI (seperti memaksa semua A/F ke 6-pin atau memaksa 1-pin ditambah dummy pin kedua).
- Jumlah pin visual yang dirender di SVG **tidak boleh pernah berbeda** dari `connector.pin_count`.
- Apabila `connector.pin_count !== connector.pins.length` atau terdapat duplikasi / nomor pin di luar rentang `1..pin_count`, UI wajib memblokir gambar soket perkiraan dan menampilkan banner peringatan keselamatan (**FR-05 Fallback**).

---

## 4. MANDATORY QA CHECK (AUTOMATED GATE)

- Setiap penambahan, pembaruan, atau refactoring data DTC, wiring diagram, foto OEM, maupun simulator soket **WAJIB** menjalankan dan lulus 100% (exit code `0`) skrip validasi otomatis sebelum dianggap selesai:

```bash
python scripts/validate_dtc_data.py
```

- Skrip ini juga terdaftar sebagai gerbang otomatis di CI/CD build APK (`.github/workflows/build_apk_offline.yml`).
- Jika data manual OEM untuk suatu kode DTC baru belum tersedia atau belum terverifikasi secara fisik, **WAJIB** tandai `verification_status: "UNVERIFIED"` dan tampilkan peringatan di UI — **jangan pernah mengisi data tebakan**.
