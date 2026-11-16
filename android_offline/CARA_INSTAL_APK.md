# Cara Mengambil & Memasang APK Offline AGOS Smart Diagnostik di HP Android

Aplikasi **AGOS Smart Diagnostik (Mode Offline)** sudah dikonversi agar berjalan **100% tanpa internet dan tanpa server**, sementara seluruh data web lama Anda tetap tersimpan utuh di branch `main`.

---

## Langkah 1 — Mengunggah Branch `apk-offline` ke GitHub (1 Klik)
Buka terminal (CMD / PowerShell) di folder proyek Anda, lalu jalankan:
```bash
git push -u origin apk-offline
```

## Langkah 2 — Mengunduh File `.apk` dari GitHub Actions
1. Buka repositori GitHub Anda di browser:
   👉 **[https://github.com/BAGUSW085/agos-smart-diagnostik/actions](https://github.com/BAGUSW085/agos-smart-diagnostik/actions)**
2. Klik workflow **"Build Android APK Offline - AGOS Smart Diagnostik"** yang paling atas (tunggu ±2–3 menit hingga ikon berubah menjadi centang hijau ✅).
3. Gulir ke bagian paling bawah (**Artifacts**), lalu klik **`agos-diagnostik-offline-apk`** untuk mengunduh file `.zip`.
4. Ekstrak file `.zip` tersebut, di dalamnya terdapat file **`app-debug.apk`**.

## Langkah 3 — Memasang APK di HP Android
1. Kirim file **`app-debug.apk`** ke HP Android Anda (bisa lewat WhatsApp, kabel data USB, atau Google Drive).
2. Ketuk file **`app-debug.apk`** di HP Anda.
3. Jika muncul peringatan keamanan *"Instal aplikasi yang tidak dikenal"*, ketuk **Setelan (Settings)** $\rightarrow$ aktifkan **"Izinkan dari sumber ini"**.
4. Ketuk **Instal (Install)** $\rightarrow$ **Buka (Open)**.

---

## Cara Kembali ke Versi Web / Cloud (Cadangan Opsi A)
Jika suatu saat Anda berubah pikiran dan ingin memakai versi Web / Cloud kembali, cukup jalankan:
```bash
git checkout main
```
Seluruh file `backend/`, database `bengkel_masa_depan.db`, dan data 17 kasus Anda (`K001` s/d `K018`) **100% utuh dan tidak berubah sedikit pun**.
