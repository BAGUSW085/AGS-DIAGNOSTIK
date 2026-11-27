# Catatan Projek AGOS Smart Diagnostik — Daftar Belum Diterapkan (Pengingat)

**Tanggal Disimpan:** 26 November 2026  
**Status Rilis Terakhir:** **v2.2.0 (PRD `REQ-01` s/d `REQ-14` Selesai 100%)**  
**Alasan Jeda:** Pengguna sedang fokus menyusun **Proposal Skripsi** terlebih dahulu.

---

## 1. Status Terakhir yang Sudah Selesai & Aktif
- **Web Resmi (Vercel Production):** https://ags-diagnostik.vercel.app/ — commit `4616a02` (`main`), terverifikasi **10/10 PASS**.
- **APK Android Offline v2.2.0:** `AGOS-Smart-Diagnostik-Offline.apk` (`10,87 MB`, Release [`v2.2.0-offline`](https://github.com/BAGUSW085/AGS-DIAGNOSTIK/releases/tag/v2.2.0-offline)), terverifikasi **10/10 PASS** (8 Paket Manual OEM, Wiring Simulator v3, SheetJS lokal, Weighted CBR).
- **Basis Data & Excel:** `backend/bengkel_masa_depan.db` + `DATA_KASUS_AGOS.xlsx` memuat 17 kasus terverifikasi (`K001`–`K010`, `K012`–`K018`) + 1 kasus uji lokal `K019` (`DRAFT`).

---

## 2. Daftar Fitur & Pekerjaan yang Belum Diterapkan (Untuk Diingatkan Nanti)

### A. Prioritas Cepat (Peningkatan Langsung v2.2.x)
- [ ] **Express Search 1-Baris Multi-DTC (`backend/app/static/index.html` → `parseExpressQuery`)**
  - Saat ini *Form Diagnosa Cerdas* dan *Asisten Manual AI (Tab 3)* sudah mendukung Multi-DTC, tetapi **Express Search 1-Baris** masih baru menangkap 1 kode DTC pertama.
  - Rencana: upgrade `parseExpressQuery()` agar langsung mendeteksi, menampilkan, dan mengisi banyak kode DTC sekaligus (mis. `K14B P0107 P0113` atau `J20A P0302 P0171`), serta pilihan cepat kode DTC saat membuka `/wiring-viewer` dari kasus Multi-DTC.
- [ ] **Evaluasi & Penyesuaian Bobot Weighted CBR (Jika Diperlukan Setelah Uji Bengkel Nyata)**
  - Bobot aktif saat ini: Keluhan/Gejala `25%`, DTC `25%`, Model `15%`, Kilometer `15%`, Merek/Platform Kembar `10%`, Tahun `10%` (+ integrasi Live Data `15%`, tie-breaker verifikasi `+2%`).
  - Rencana: review ulang akurasi peringkat setelah mekanik menginput lebih banyak kasus riil bengkel.
- [ ] **Review Kasus Uji `K019` (`DRAFT`)**
  - Cek apakah kasus uji lokal `K019` (Suzuki Grand Vitara `P0300`, status `DRAFT`) ingin diverifikasi oleh Kepala Bengkel (`PIN 1234`) atau dihapus agar dataset kembali persis 17 kasus.

### B. Pengembangan Fitur Fase Berikutnya (v2.3+ / Roadmap Lanjutan & Komersialisasi)
- [ ] **Sistem Proteksi Distribusi APK Anti-Share (1 Device = 1 Akun / 1 Kode Aktivasi / Kode Referral)**
  - Distribusi APK dikendalikan penuh oleh pemilik (tombol Admin & Pasang/Bagikan APK di header sudah dihapus).
  - Rencana teknis: Android Device Fingerprinting (`ANDROID_ID` + Hardware Hash) + Aktivasi Online Sekali Pakai via Server Lisensi (Supabase/Firebase/FastAPI) dengan Kode Lisensi/Referral unik → menghasilkan token terenkripsi (HMAC/AES) di Android Keystore. Setelah aktif di 1 HP, aplikasi tetap bekerja **100% offline**, namun jika APK disalin/dikirim ke HP lain tidak dapat dibuka tanpa aktivasi kode baru.
- [ ] **Sinkronisasi Cloud Hybrid Google Sheets (Offline-First + Auto-Sync)**
  - Mekanik tetap input & cari kasus 100% offline di HP; saat HP tersambung internet/Wi-Fi, data kasus otomatis tersinkronisasi ke Google Sheets pemilik bengkel agar mudah dipantau real-time dari HP tanpa kirim file manual.
- [ ] **Pilar 3 — Web POS Bengkel Produksi Penuh (Koneksi Database Nyata)**
  - Saat ini di Tab `Web POS Bengkel (Demo)` masih berupa pratinjau interaktif (`REQ-09`).
  - Rencana: implementasi database nyata untuk PKB, manajemen stok sparepart gudang (auto-deduct persisten), cetak invoice kasir PPN 11%, riwayat pelanggan/nopol, dan laporan omzet.
- [ ] **Penambahan Paket Manual Repair OEM & Alur Sinyal `/wiring-viewer`**
  - Tambah buku manual repair model baru (di luar 8 paket aktif saat ini) serta *curated signal chains* tambahan di `/wiring-viewer` (mis. Honda, Mitsubishi, Daihatsu generasi terbaru, EV/Hybrid tambahan).
- [ ] **Mode Siang / Terang (*Light Mode*)**
  - Opsi tema terang agar layar tetap mudah dibaca mekanik di area bengkel yang terang/terkena sinar matahari langsung.
- [ ] **Lampiran Foto Bukti Diagnosa & Kirim Laporan ke WhatsApp Pelanggan**
  - Upload foto kerusakan komponen/soket/multimeter saat menyimpan kasus + tombol kirim ringkasan bahasa awam (`REQ-07`) langsung ke WhatsApp pemilik mobil.
- [ ] **Pembersihan / Perbaikan Workflow `.github/workflows/build_apk.yml` (Legacy)**
  - Workflow lama `build_apk.yml` di branch `main` sempat gagal saat push (sedangkan workflow utama `build_apk_offline.yml` di branch `apk-offline` sudah sukses 100%). Perlu dirapikan atau dinonaktifkan jika sudah tidak dipakai agar status commit GitHub selalu hijau.

---

## 3. Catatan Teknis Saat Kembali Melanjutkan Proyek
1. Untuk menyalakan ulang server lokal di PC:
   ```powershell
   cd "c:\project bengkel masa depan ai antigravity\backend"
   .\.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
2. Setiap perubahan pada `backend/app/static/index.html` atau `ewd_viewer.html` perlu disinkronkan ke offline APK dengan:
   ```powershell
   backend\.venv\Scripts\python.exe android_offline\tools\export_data.py
   backend\.venv\Scripts\python.exe android_offline\tools\sync_web_to_offline.py
   ```
3. Push ke `main` otomatis men-deploy ke `https://ags-diagnostik.vercel.app/`; push ke `apk-offline` otomatis memicu GitHub Actions membangun & merilis `AGOS-Smart-Diagnostik-Offline.apk`.
