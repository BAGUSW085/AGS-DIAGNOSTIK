# PROGRES — APK Android Offline AGOS Smart Diagnostik

> Aturan: kerjakan tugas pertama yang belum dicentang `[ ]`. Setelah selesai, ubah jadi `[x]`,
> isi kolom catatan, lalu commit. Spesifikasi lengkap ada di `PROMPT_APK_OFFLINE.md`.

**Status terakhir:** Belum dimulai (prompt master baru dibuat).
**Model AI terakhir yang bekerja:** —
**Tanggal update terakhir:** 2026-11-16

---

## Fase 1 — Persiapan
- [ ] 1.1 Commit perubahan yang masih tertunda di `main` (`backend/app/db/seed_historical_cases.py` sudah ditambah K013–K018, plus `PROMPT_APK_OFFLINE.md` dan file ini).
- [ ] 1.2 Buat branch `git checkout -b apk-offline`.
- [ ] 1.3 Buat folder `android_offline/` sesuai struktur di Bagian 4 prompt master.
- [ ] 1.4 Salin `backend/app/static/index.html` → `android_offline/www/index.html` (salin, bukan pindah). Salin juga `icon-192.png` dan `icon-512.png`.

## Fase 2 — Ekspor Data
- [ ] 2.1 Tulis `android_offline/tools/export_data.py` (koneksi SQLite mode baca saja: `file:...?mode=ro`).
- [ ] 2.2 Hasilkan `www/data/historical_cases.json`, `dtc_codes.json`, `wiring_diagrams.json`, `sensor_specs.json`, `repair_manuals.json`, `jb420_catalog.json`.
- [ ] 2.3 Catat ukuran tiap file JSON. Jika `repair_manuals.json` > 5 MB, buang kolom yang tidak dipakai UI.

## Fase 3 — Port Mesin Diagnosa
- [ ] 3.1 `www/js/engine.js`: tokenizer, stopword, sinonim, parsing DTC, keluarga DTC.
- [ ] 3.2 Skor teks, skor live, skor total, kategori, ranking, `system_summaries`.
- [ ] 3.3 Pembuatan `direct_manual_advice` (port logika `ManualRepairAdvice` dari Python).
- [ ] 3.4 `tools/verify_engine.py` + hasil verifikasi semua kasus lolos ±0.5%.

## Fase 4 — Port Pencarian Manual / DTC
- [ ] 4.1 `www/js/manual-search.js` meniru respons `/manuals/ask-assistant` (`synthesized_guidance`, `detected_dtc_codes`, `matched_wiring_diagrams`).
  Sumber yang di-port: `backend/app/services/manual_wiring_service.py` → `ask_rag_assistant()` (baris ±357–710),
  `retrieve_repair_manuals()` (±298), `search_sensor_specs()`, `search_wiring_diagrams()`, `lookup_dtc_codes()`, `_extract_tokens()`, `_extract_dtc_from_text()`.
  Ini pencarian berbasis kata kunci + skor (bukan LLM/internet), jadi wajib berfungsi penuh offline.
- [ ] 4.2 Uji 10 kueri (mis. "P0122", "P0480 kipas", "MAF", "O2 heater P0037", "pinout C37", "TCM E92") — hasil JS sama dengan respons endpoint web.

## Fase 5 — Lapisan Offline API
- [ ] 5.1 `www/js/data-store.js`: muat JSON bawaan + simpan kasus tambahan/terhapus di `localStorage` (bawaan tidak diubah).
- [ ] 5.2 `www/js/offline-api.js`: fungsi `offlineFetch()` untuk 6 endpoint (lihat tabel Bagian 3).
- [ ] 5.3 Ganti semua `fetch(\`${API_BASE}...\`)` dan `fetch('/health')` di `www/index.html`.

## Fase 6 — Hilangkan Ketergantungan Internet
- [ ] 6.1 Tailwind CDN → build lokal `www/css/app.css`.
- [ ] 6.2 Font Awesome lokal (css + webfonts).
- [ ] 6.3 Font Plus Jakarta Sans lokal atau fallback font sistem.
- [ ] 6.4 Hapus/sembunyikan QR `api.qrserver.com`, link `bore.pub`, tombol Pasang App, service worker.
- [ ] 6.5 Ganti `window.print()` dengan bagikan/simpan hasil.

## Fase 7 — Rapikan Tampilan HP (Bagian 6 prompt master)
- [ ] 7.1 Viewport, safe-area, anti scroll samping.
- [ ] 7.2 Tabel → kartu di layar < 640px (5 tabel).
- [ ] 7.3 Bottom nav, target sentuh 44px, ukuran font.
- [ ] 7.4 SVG simulator dan modal layar penuh.
- [ ] 7.5 Tombol Back Android.
- [ ] 7.6 Uji lebar 360/393/412px di semua tab, catat hasilnya.

## Fase 8 — Capacitor & Build
- [ ] 8.1 `package.json`, `capacitor.config.json`, `tailwind.config.js`, `src/input.css`.
- [ ] 8.2 `.github/workflows/build_apk_offline.yml`.
- [ ] 8.3 Build sukses di GitHub Actions (perlu izin pengguna untuk push branch `apk-offline`).

## Fase 9 — Uji Akhir & Serah Terima
- [ ] 9.1 Semua poin Definition of Done (Bagian 9 prompt master) lolos.
- [ ] 9.2 Tulis `android_offline/CARA_INSTAL_APK.md` (bahasa sederhana untuk pengguna).

---

## Catatan Kerja
| Tanggal | Model AI | Tugas | Catatan |
|---|---|---|---|
| 2026-11-16 | Claude Opus 5.5 | Prompt master | Membuat `PROMPT_APK_OFFLINE.md` dan file progres ini. Belum ada kode APK. |

## Catatan Masalah
- (kosong)
