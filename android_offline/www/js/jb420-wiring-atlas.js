/**
 * AGOS Dark Cockpit — Atlas Wiring Diagram & Alur Sinyal Resmi Suzuki Grand Vitara JB420 (2.0L J20A)
 * ===================================================================================================
 * Mencakup Kategori 1 (20 Modul Mesin & EFI + Kasus Non-Wiring P0171/P0420),
 * Kategori 2 (7 Modul Kontrol Ber-DTC: TCM A/T, ABS/EBD, SRS Air Bag, Auto A/C HVAC, BCM, ICM, KSCM),
 * dan Kategori 4 (4 Peta Dasar: Kode Warna Kabel, Box Sekring, Titik Ground, Layout & Bentuk Konektor).
 * Seluruh gambar foto wiring asli diambil langsung dari Service Manual resmi Vol 1 (661 hal) & Vol 2 (827 hal).
 */

(function () {
  const WIRE_COLOR_HEX = {
    BLK: '#18181b', B: '#18181b',
    WHT: '#f8fafc', W: '#f8fafc',
    RED: '#dc2626', R: '#dc2626',
    BLU: '#2563eb', L: '#2563eb',
    GRN: '#16a34a', G: '#16a34a',
    YEL: '#eab308', Y: '#eab308',
    BRN: '#92400e', BR: '#92400e',
    ORN: '#f97316', O: '#f97316',
    PNK: '#ec4899', P: '#ec4899',
    GRY: '#64748b', GR: '#64748b',
    PPL: '#9333ea', V: '#9333ea',
    'LT GRN': '#4ade80', LG: '#4ade80',
    'LT BLU': '#38bdf8', LB: '#38bdf8',
    BEI: '#d6c29f',
    SLV: '#cbd5e1'
  };

  function resolveSingleColor(tok) {
    const clean = String(tok || '').trim().toUpperCase();
    return WIRE_COLOR_HEX[clean] || '#475569';
  }

  function getWirePalette(colorCode) {
    const raw = String(colorCode || 'GRY').trim().toUpperCase();
    const parts = raw.split('/').map(s => s.trim()).filter(Boolean);
    const base = resolveSingleColor(parts[0] || 'GRY');
    const stripe = parts[1] ? resolveSingleColor(parts[1]) : null;
    return { base, stripe, label: raw };
  }

  function renderWireSwatchHtml(colorCode) {
    const { base, stripe, label } = getWirePalette(colorCode);
    const bgStyle = stripe
      ? `background: linear-gradient(180deg, ${base} 0%, ${base} 34%, ${stripe} 35%, ${stripe} 65%, ${base} 66%, ${base} 100%);`
      : `background: ${base};`;
    return `<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-slate-950/90 border border-slate-700 font-mono text-[10px] font-bold text-slate-100 shrink-0" title="Kode Warna Kabel OEM: ${label}">
      <span class="inline-block w-7 h-3 rounded-sm border border-slate-400/70 shadow-inner" style="${bgStyle}"></span>
      <span>${label}</span>
    </span>`;
  }

  const JB420_WIRING_ATLAS = [
    // =========================================================================
    // KATEGORI 1: MESIN & EFI (ECM C37 / E23 — BAB 1A, 1H & BAB 9A A-1..A-5)
    // =========================================================================
    {
      id: 'gv_ign_coil',
      category: 'efi',
      badge: 'A-3 · PENGAPIAN',
      title: 'Sistem Pengapian 4× Koil COP (Silinder #1–#4)',
      subtitle: 'ECM C37-21/20/19/18 → Koil C40, C41, C42, C43 + Noise Filter C47',
      dtcs: ['P0300', 'P0301', 'P0302', 'P0303', 'P0304'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a3_pengapian_9a41.webp', label: 'Diagram A-3 Pengapian (9A-41)', source: 'Vol 2 Bab 9A-41 (A-3 Diagram Sirkuit Sistim Pengapian · S5JB0A910E040)' },
        { img: 'img/jb420_wiring/v1_ign_1h2.webp', label: 'Skema Pengapian (1H-2)', source: 'Vol 1 Bab 1H-2 (Diagram Sirkuit Sistim Pengapian)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +12V Sekring 20A IG COIL', from: 'Box J/B Sekring #39 (20A IG COIL)', via: 'E82-23 → E62 → E55/C35-10 → C55', to: 'Pin 1 Koil C40–C43 & C47 Pin 2', wire: 'BLK/WHT', desc: 'Kunci kontak ON mengalirkan +12V serentak ke Pin 1 keempat koil COP dan Noise Filter.' },
        { step: 2, tag: 'OUTPUT', title: 'Sinyal Pemicu Pengapian (IGT) dari ECM', from: 'ECM C37-21 / 20 / 19 / 18', via: '4 Jalur Terpisah (Silinder #1–#4)', to: 'Pin 3 Koil C40 (#1), C41 (#2), C42 (#3), C43 (#4)', wire: 'BRN/BLK', desc: 'ECM mengirim pulsa trigger ke ignitor internal tiap koil sesuai urutan pengapian 1-3-4-2.' },
        { step: 3, tag: 'GROUND', title: 'Jalur Massa Koil & Noise Filter', from: 'Pin 2 Koil C40–C43 & C47 Pin 1', via: 'Splice Massa Pengapian', to: 'Titik Ground Blok #5', wire: 'BLK/ORN', desc: 'Arus primer koil kembali ke massa mesin melalui kabel BLK/ORN ke Ground #5.' }
      ],
      wires: [
        { colorCode: 'BLK/WHT', from: 'Sekring #39 (20A IG COIL)', to: 'Pin 1 Koil C40–C43 (+B)', dir: 'power', role: 'Suplai daya positif +12V utama koil COP', func: 'Memberi arus kerja ke kumparan primer & ignitor keempat koil saat kunci kontak ON.', keyState: 'IG ON (Mesin Mati)', probe: 'Merah (+) Pin 1 Koil · Hitam (−) Massa Aki', spec: '10 – 14 V DC', faultHint: 'Jika 0V → periksa sekring #39 (20A IG COIL) di J/B & sambungan E55/C35-10.' },
        { colorCode: 'BRN', from: 'ECM Pin C37-21', to: 'Koil #1 (C40 Pin 3)', dir: 'out', role: 'Trigger pengapian Silinder #1 (P0301)', func: 'Mengirim sinyal pulsa pemantik dari ECM ke transistor ignitor koil silinder #1.', keyState: 'IG ON / Idle', probe: 'Merah (+) C37-21 · Hitam (−) Massa', spec: '0 – 0,6 V (IG ON) / Pulsa saat Idle', faultHint: 'Jika pulsa ECM normal tapi pincang → tukar fisik koil #1 untuk konfirmasi.' },
        { colorCode: 'BRN/BLK', from: 'ECM Pin C37-20', to: 'Koil #2 (C41 Pin 3)', dir: 'out', role: 'Trigger pengapian Silinder #2 (P0302)', func: 'Mengirim sinyal pulsa pemantik dari ECM ke ignitor koil silinder #2.', keyState: 'IG ON / Idle', probe: 'Merah (+) C37-20 · Hitam (−) Massa', spec: '0 – 0,6 V (IG ON) / Pulsa saat Idle', faultHint: 'Cek kontinuitas C37-20 ↔ C41 Pin 3 (< 1 Ω) bila tidak ada pulsa di soket koil.' },
        { colorCode: 'BRN/WHT', from: 'ECM Pin C37-19', to: 'Koil #3 (C42 Pin 3)', dir: 'out', role: 'Trigger pengapian Silinder #3 (P0303)', func: 'Mengirim sinyal pulsa pemantik dari ECM ke ignitor koil silinder #3.', keyState: 'IG ON / Idle', probe: 'Merah (+) C37-19 · Hitam (−) Massa', spec: '0 – 0,6 V (IG ON) / Pulsa saat Idle', faultHint: 'Pastikan pin soket C42 tidak kendur/korosi akibat panas ruang mesin.' },
        { colorCode: 'BRN/YEL', from: 'ECM Pin C37-18', to: 'Koil #4 (C43 Pin 3)', dir: 'out', role: 'Trigger pengapian Silinder #4 (P0304)', func: 'Mengirim sinyal pulsa pemantik dari ECM ke ignitor koil silinder #4.', keyState: 'IG ON / Idle', probe: 'Merah (+) C37-18 · Hitam (−) Massa', spec: '0 – 0,6 V (IG ON) / Pulsa saat Idle', faultHint: 'Ukur kebocoran isolasi selongsong karet koil jika misfire muncul saat beban tinggi.' },
        { colorCode: 'BLK/ORN', from: 'Pin 2 Koil C40–C43', to: 'Titik Ground Blok #5', dir: 'ground', role: 'Massa bersama 4 koil & Noise Filter C47', func: 'Menjadi jalur balik arus primer dan peredam interferensi listrik ke blok mesin.', keyState: 'IG OFF (Mode Ohm)', probe: 'Merah (+) Pin 2 Koil · Hitam (−) Aki (−)', spec: '< 1 Ω (Kontinyu)', faultHint: 'Jika tahanan > 2 Ω → bersihkan baut Ground #5 (bisa bikin semua silinder misfire P0300).' }
      ]
    },
    {
      id: 'gv_ecm_power',
      category: 'efi',
      badge: '1A-217 · POWER ECM',
      title: 'Power Supply Utama, Main Relay & Ground ECM',
      subtitle: 'Aki → Box Sikring No.2 (FI) → Main Relay → E23-1/16/29/60 & C37-15/29/48',
      dtcs: ['P1510', 'P0601', 'P0602', 'P0607', 'Non-DTC'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_ecm_power_1a217.webp', label: 'Sirkuit Power & Ground ECM (1A-217)', source: 'Vol 1 Bab 1A-217 (Memeriksa Sirkuit Power ECM dan Ground · S5JB0A1104064)' },
        { img: 'img/jb420_wiring/v1_ecm_io_1a15.webp', label: 'Diagram I/O ECM (1A-15)', source: 'Vol 1 Bab 1A-15 (Diagram Sirkuit Input/Output ECM)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p1_9a43.webp', label: 'A-5 Kontrol Mesin Lembar 1 (9A-43)', source: 'Vol 2 Bab 9A-43 (A-5 Diagram Sirkuit Sistim Kontrol Mesin & A/C)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai Stand-by & Kunci Kontak ke ECM', from: 'Aki +12V & Sekring FI / IGN', via: 'Box Sikring No.2', to: 'ECM E23-29 (IG) & Back-Up (+BB)', wire: 'BLK/RED', desc: 'Kunci kontak ON mengaktifkan pin E23-29 agar ECM bangun dan segera menarik Main Relay.' },
        { step: 2, tag: 'OUTPUT', title: 'ECM Menarik Main Relay → Daya Utama +B', from: 'ECM C37-22 (Kontrol Relay) → Main Relay', via: 'Kabel BLU/BLK', to: 'ECM E23-1, E23-16 & E23-60 (+12V)', wire: 'BLU/BLK', desc: 'ECM memberi ground di C37-22 sehingga Main Relay ON dan menyuplai +12V penuh ke ECM & sensor.' },
        { step: 3, tag: 'GROUND', title: 'Massa Utama Blok Mesin ECM', from: 'ECM C37-15, C37-29, C37-48, C37-58', via: 'Harness Mesin', to: 'Ground Blok Mesin', wire: 'BLK/YEL', desc: 'Seluruh logika & driver aktuator ECM membutuhkan jalur massa rendah tahanan (< 1 Ω).' }
      ],
      wires: [
        { colorCode: 'BLK/WHT', from: 'Kunci Kontak IG ON', to: 'ECM Pin E23-29', dir: 'power', role: 'Sinyal bangun (Ignition Sense) ECM', func: 'Memberitahu ECM bahwa kunci kontak diputar ke posisi ON.', keyState: 'IG ON', probe: 'Merah (+) E23-29 · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika 0V saat IG ON → cek sekring IGN & kunci kontak (lampu Check Engine tidak menyala).' },
        { colorCode: 'BLK/YEL', from: 'ECM Pin C37-22', to: 'Kumparan Main Relay', dir: 'out', role: 'Kontrol aktivasi Main Relay (Active Low)', func: 'ECM menarik pin C37-22 ke massa (< 1V) untuk menyalakan Main Relay.', keyState: 'IG ON', probe: 'Merah (+) C37-22 · Hitam (−) Massa', spec: '< 1,0 V saat IG ON (10–14 V saat OFF)', faultHint: 'Jika tetap 12V saat IG ON → periksa power E23-29 & massa ECM.' },
        { colorCode: 'BLU/BLK', from: 'Kontak Main Relay', to: 'ECM E23-1 & E23-16 (+B)', dir: 'power', role: 'Power utama operasional ECM & sensor', func: 'Menyuplai arus kerja utama untuk mikroprosesor ECM, MAF, koil, dan injektor.', keyState: 'IG ON', probe: 'Merah (+) E23-1 / E23-16 · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika 0V padahal relay bunyi → kontak internal Main Relay hangus atau sekring FI putus.' },
        { colorCode: 'BLK/ORN', from: 'ECM C37-15, C37-29, C37-48', to: 'Massa Blok Mesin', dir: 'ground', role: 'Ground daya & logika ECM', func: 'Menjaga referensi 0V stabil bagi seluruh rangkaian sensor & driver aktuator.', keyState: 'IG OFF (Mode Ohm)', probe: 'Merah (+) Pin Ground C37 · Hitam (−) Aki (−)', spec: '< 1 Ω (Tegangan jatuh < 0,2 V saat ON)', faultHint: 'Ground kendor menyebabkan scanner gagal konek atau banyak DTC acak muncul bersamaan.' }
      ]
    },
    {
      id: 'gv_ckp',
      category: 'efi',
      badge: '1A-115 · CKP',
      title: 'Sensor CKP (Crankshaft Position Sensor — 3-Pin C20)',
      subtitle: 'Konektor C20 3-Pin J20A: Pin 1 Shield (BLK), Pin 2 CKP− (PNK C37-36), Pin 3 CKP+ (BLU C37-51)',
      dtcs: ['P0335', 'P0336'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_ckp_p0335_1a115.webp', label: 'Wiring Diagram P0335 & Pinout E23/C37 (1A-115)', source: 'Vol 1 Bab 1A-115 (DTC P0335 Sirkuit CKP Sensor · Fig I5JB0A110047-02)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p2_9a44.webp', label: 'A-5 Lembar 2 (9A-44)', source: 'Vol 2 Bab 9A-44 (Diagram A-5 Kontrol Mesin)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Prasyarat Power ECM & Sinyal Starter', from: 'Kunci Kontak START → Starter Relay', via: 'BLK/YEL & BLU', to: 'ECM E23-60 (Sinyal Cranking)', wire: 'BLK/YEL', desc: 'P0335 terdeteksi saat ECM melihat sinyal cranking masuk 2 detik namun pulsa CKP kosong.' },
        { step: 2, tag: 'INPUT', title: 'Sinyal AC Induktif Sensor CKP (Pin 2 & 3)', from: 'Sensor CKP C20 (3-Pin)', via: 'Pin 2 PNK & Pin 3 BLU', to: 'ECM C37-36 (PNK) & C37-51 (BLU)', wire: 'PNK', desc: 'Putaran gigi sensor plate kruk as membangkitkan tegangan pulsa AC antara Pin 2 & Pin 3 untuk menentukan RPM & TMA.' },
        { step: 3, tag: 'GROUND', title: 'Pin 1 Pelindung Shield & Massa Blok #3', from: 'C20 Pin 1 (Shield CKP)', via: 'Kabel BLK', to: 'Massa Blok Mesin #3', wire: 'BLK', desc: 'Pin 1 kabel pelindung mencegah gangguan noise pengapian mengacaukan pembacaan RPM.' }
      ],
      wires: [
        { colorCode: 'BLK', from: 'Sensor CKP C20 Pin 1 (Shield)', to: 'Massa Blok Mesin #3', dir: 'ground', role: 'Perisai anti-noise elektromagnetik (Pin 1 C20)', func: 'Menyaring gangguan medan magnet dari koil pengapian dan alternator.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin 1 C20 ↔ Massa Bodi', spec: '< 1 Ω (Tidak boleh short ke Pin 2/3)', faultHint: 'Shield putus bisa menimbulkan RPM melompat-lompat saat digas.' },
        { colorCode: 'PNK', from: 'Sensor CKP C20 Pin 2 (−)', to: 'ECM Pin C37-36', dir: 'in', role: 'Sinyal pulsa posisi kruk as (−)', func: 'Pasangan diferensial jalur sinyal CKP yang terhubung langsung ke input ECM.', keyState: 'IG OFF (Mode Ohm)', probe: 'Tahanan Sensor Pin 2 ↔ Pin 3', spec: '1,68 – 2,52 kΩ @ 20°C · Kontinuitas kabel < 1 Ω', faultHint: 'Bila tahanan OL (putus) saat mesin panas → ganti Sensor CKP.' },
        { colorCode: 'BLU', from: 'Sensor CKP C20 Pin 3 (+)', to: 'ECM Pin C37-51', dir: 'in', role: 'Sinyal pulsa posisi kruk as (+)', func: 'Mengirimkan gelombang pulsa induktif saat kruk as berputar untuk hitung RPM & timing.', keyState: 'Cranking / Idle (AC Volt)', probe: 'Merah (+) C37-51 · Hitam (−) C37-36', spec: '> 0,5 V AC saat cranking (simetris)', faultHint: 'Pastikan kabel tidak terjepit dekat knalpot/blok mesin.' }
      ]
    },
    {
      id: 'gv_cmp',
      category: 'efi',
      badge: '1A-117 · CMP',
      title: 'Sensor CMP (Camshaft Position Sensor)',
      subtitle: 'Sensor Hall-Effect 3-Pin (+12V Main Relay, Sinyal C37-52, Ground)',
      dtcs: ['P0340', 'P0341'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_cmp_p0340_1a117.webp', label: 'Wiring Diagram P0340 CMP (1A-117)', source: 'Vol 1 Bab 1A-117 (DTC P0340 Sirkuit CMP Sensor · S5JB0A1104041)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p2_9a44.webp', label: 'A-5 Lembar 2 (9A-44)', source: 'Vol 2 Bab 9A-44 (Diagram A-5 Kontrol Mesin)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +12V dari Main Relay', from: 'Main Relay (Sekring FI)', via: 'Kabel BLU/BLK', to: 'Pin Power Sensor CMP', wire: 'BLU/BLK', desc: 'Berbeda dengan CKP induktif, CMP tipe Hall-Effect membutuhkan suplai +12V aktif saat IG ON.' },
        { step: 2, tag: 'INPUT', title: 'Pulsa Digital Posisi Noken As', from: 'Pin Sinyal Sensor CMP', via: 'Harness Mesin', to: 'ECM Pin C37-52', wire: 'RED/YEL', desc: 'Menentukan langkah kompresi silinder #1 untuk sinkronisasi semprotan injektor sekuensial.' },
        { step: 3, tag: 'GROUND', title: 'Massa Sensor CMP', from: 'Pin Ground Sensor CMP', via: 'Massa Mesin', to: 'Ground Blok / ECM', wire: 'BLK/ORN', desc: 'Jalur balik tegangan referensi Hall-Effect.' }
      ],
      wires: [
        { colorCode: 'BLU/BLK', from: 'Main Relay', to: 'Sensor CMP (+B)', dir: 'power', role: 'Suplai tegangan aktif sensor Hall-Effect', func: 'Menyalakan rangkaian elektronik internal sensor CMP.', keyState: 'IG ON', probe: 'Merah (+) Pin Power CMP · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika 0V → periksa cabang suplai dari Main Relay.' },
        { colorCode: 'RED/YEL', from: 'Sensor CMP (Sinyal)', to: 'ECM Pin C37-52', dir: 'in', role: 'Pulsa posisi camshaft (0V ↔ 5V)', func: 'Menginformasikan posisi top silinder #1 ke ECM.', keyState: 'Cranking / Idle', probe: 'Merah (+) C37-52 · Hitam (−) Massa', spec: 'Berubah-ubah 0–1 V ↔ 4–5 V saat mesin diputar', faultHint: 'Jika diam konstan 0V atau 5V saat diputar → sensor CMP rusak atau rantai keteng melompat.' },
        { colorCode: 'BLK/ORN', from: 'Sensor CMP (GND)', to: 'Massa Blok Mesin', dir: 'ground', role: 'Ground sensor CMP', func: 'Referensi 0V rangkaian Hall-Effect.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin GND CMP ↔ Aki (−)', spec: '< 1 Ω', faultHint: 'Ground buruk menyebabkan starter panjang susah hidup.' }
      ]
    },
    {
      id: 'gv_maf_iat',
      category: 'efi',
      badge: '1A-62 · MAF & IAT',
      title: 'Sensor MAF (Mass Air Flow) & IAT (Suhu Udara)',
      subtitle: 'Soket 5-Pin Terpadu C13 · MAF C37-26/27 & IAT C37-25/57',
      dtcs: ['P0101', 'P0102', 'P0103', 'P0111', 'P0112', 'P0113'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_maf_p0101_1a62.webp', label: 'Wiring Diagram MAF Induk P0101–P0103 (1A-62)', source: 'Vol 1 Bab 1A-62 (Fig I5JB0A110033-01 · DTC P0101/P0102/P0103 MAF Sensor)' },
        { img: 'img/jb420_wiring/v1_iat_p0111_1a74.webp', label: 'Wiring Diagram IAT Induk P0111–P0113 (1A-74)', source: 'Vol 1 Bab 1A-74 (Fig I5JB0A110036-01 · DTC P0111/P0112/P0113 IAT Sensor)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +12V Pemanas Hot-Wire MAF', from: 'Main Relay', via: 'Kabel BLU/BLK', to: 'Pin Power Soket MAF', wire: 'BLU/BLK', desc: 'Menyuplai +12V untuk memanaskan elemen pengukur massa aliran udara masuk.' },
        { step: 2, tag: 'INPUT', title: 'Sinyal MAF (C37-26) & Sinyal IAT (C37-25)', from: 'Sensor MAF/IAT', via: 'RED (MAF) & LT GRN (IAT)', to: 'ECM C37-26 & C37-25', wire: 'RED', desc: 'MAF naik tegangannya seiring aliran udara; IAT turun tegangannya saat suhu udara makin panas.' },
        { step: 3, tag: 'GROUND', title: 'Massa MAF (C37-27) & Massa Sensor (C37-57)', from: 'Pin Ground MAF & IAT', via: 'BLU & GRY/GRN', to: 'ECM C37-27 & C37-57', wire: 'GRY/GRN', desc: 'Ground khusus sensor yang kembali langsung ke ECM agar pembacaan bebas gangguan.' }
      ],
      wires: [
        { colorCode: 'BLU/BLK', from: 'Main Relay', to: 'MAF Pin Power (+B)', dir: 'power', role: 'Power supply 12V sensor MAF', func: 'Mengaktifkan rangkaian pengukur aliran udara hot-wire.', keyState: 'IG ON', probe: 'Merah (+) Pin Power MAF · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika 0V → muncul P0102 dan mesin langsung pincang/mati.' },
        { colorCode: 'RED', from: 'MAF Signal', to: 'ECM Pin C37-26', dir: 'in', role: 'Sinyal laju massa udara masuk (g/s)', func: 'Dasar utama ECM menghitung durasi bukaan injektor bahan bakar.', keyState: 'IG ON / Idle Hangat', probe: 'Merah (+) C37-26 · Hitam (−) C37-27', spec: '0,5–1,0 V (IG ON mati) · 1,3–1,8 V (Idle hangat)', faultHint: 'Bila terlalu rendah → elemen MAF kotor oli/debu atau selang intake robek.' },
        { colorCode: 'BLU', from: 'MAF Ground', to: 'ECM Pin C37-27', dir: 'ground', role: 'Massa khusus sinyal MAF', func: 'Menjaga referensi tegangan sinyal MAF tetap presisi.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin MAF GND ↔ Massa Bodi', spec: '< 3 Ω', faultHint: 'Tahanan tinggi membuat pembacaan MAF melenceng tinggi (campuran kaya).' },
        { colorCode: 'LT GRN', from: 'IAT Signal (NTC)', to: 'ECM Pin C37-25', dir: 'in', role: 'Sinyal suhu udara masuk', func: 'Koreksi kepadatan udara terhadap suhu ruang mesin.', keyState: 'IG ON', probe: 'Merah (+) C37-25 · Hitam (−) C37-57', spec: '3,18–3,67V @0°C · 1,32–1,65V @40°C · 0,46–0,60V @80°C', faultHint: 'Jika ~5V terus → kabel putus (P0113); jika 0V → short ground (P0112).' },
        { colorCode: 'GRY/GRN', from: 'Sensor Ground (E2)', to: 'ECM Pin C37-57', dir: 'ground', role: 'Massa bersama sensor IAT/MAP/ECT', func: 'Jalur balik ground stabil dari ECM untuk sensor analog.', keyState: 'IG OFF (Mode Ohm)', probe: 'C37-57 ↔ Massa Bodi', spec: '< 3 Ω', faultHint: 'Putus jalur C37-57 akan memicu P0113, P0108, & P0118 bersamaan!' }
      ]
    },
    {
      id: 'gv_map',
      category: 'efi',
      badge: '1A-68 · MAP',
      title: 'Sensor MAP (Manifold Absolute Pressure)',
      subtitle: 'Sensor 3-Pin C12: Vref +5V (C37-14), Sinyal Vakum (C37-55), Ground (C37-57)',
      dtcs: ['P0106', 'P0107', 'P0108', 'P2227', 'P2228', 'P2229'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_map_p0106_1a68.webp', label: 'Wiring Diagram MAP Induk P0106–P0108 (1A-68)', source: 'Vol 1 Bab 1A-68 (Fig I5JB0A110034-01 · DTC P0106/P0107/P0108 MAP Sensor)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Tegangan Referensi +5V (Vref)', from: 'ECM Pin C37-14', via: 'Jalur +5V Sensor', to: 'Sensor MAP Pin VCC', wire: 'GRY/RED', desc: 'ECM menyediakan tegangan stabil +5V presisi untuk sensor MAP.' },
        { step: 2, tag: 'INPUT', title: 'Sinyal Tekanan/Vakum Intake', from: 'Sensor MAP Pin OUT', via: 'Harness Mesin', to: 'ECM Pin C37-55', wire: 'GRN/WHT', desc: 'Saat KOEO ~4V (tekanan atmosfer), turun ke 1,0–1,6V saat mesin idle bervakum.' },
        { step: 3, tag: 'GROUND', title: 'Massa Sensor Bersama', from: 'Sensor MAP Pin GND', via: 'Kabel GRY/GRN', to: 'ECM Pin C37-57', wire: 'GRY/GRN', desc: 'Kembali langsung ke massa analog ECM.' }
      ],
      wires: [
        { colorCode: 'GRY/RED', from: 'ECM Pin C37-14', to: 'Sensor MAP (+5V)', dir: 'power', role: 'Tegangan referensi +5V', func: 'Suplai daya presisi dari regulator internal ECM.', keyState: 'IG ON', probe: 'Merah (+) Pin VCC · Hitam (−) Massa', spec: '4,5 – 5,5 V DC', faultHint: 'Jika 0V → cek apakah ada sensor lain yang short menarik jalur 5V turun.' },
        { colorCode: 'GRN/WHT', from: 'Sensor MAP (Signal)', to: 'ECM Pin C37-55', dir: 'in', role: 'Tegangan sinyal vakum intake manifold', func: 'Mengukur beban mesin untuk koreksi pengapian & EGR.', keyState: 'IG ON / Idle', probe: 'Merah (+) C37-55 · Hitam (−) C37-57', spec: '3,8–4,3 V (KOEO) · 1,0–1,6 V (Idle hangat)', faultHint: '< 0,2V memicu P0107 (short ground); > 4,7V memicu P0108 (putus/short 5V).' },
        { colorCode: 'GRY/GRN', from: 'Sensor MAP (GND)', to: 'ECM Pin C37-57', dir: 'ground', role: 'Ground analog ECM', func: 'Referensi 0V presisi untuk sensor tekanan.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin GND MAP ↔ Massa', spec: '< 3 Ω', faultHint: 'Ground putus membuat tegangan sinyal naik mendekati 5V (P0108).' }
      ]
    },
    {
      id: 'gv_ect',
      category: 'efi',
      badge: '1A-81 · ECT',
      title: 'Sensor ECT (Engine Coolant Temperature)',
      subtitle: 'Thermistor NTC 2-Pin C09 · Sinyal C37-24 (PPL/YEL) & Massa Bersama C37-57 (GRY/GRN)',
      dtcs: ['P0116', 'P0117', 'P0118', 'B1561'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_ect_p0116_1a81.webp', label: 'Wiring Diagram ECT Induk P0116–P0118 (1A-81)', source: 'Vol 1 Bab 1A-81 (Fig I5JB0A110038-01 · DTC P0116/P0117/P0118 ECT Sensor)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Tegangan Pull-Up +5V dari ECM', from: 'ECM Pin C37-24 (Internal Resistor)', via: 'Kabel Sinyal ECT (PPL/YEL)', to: 'Sensor ECT C09 Pin 2', wire: 'PPL/YEL', desc: 'ECM mengalirkan +5V melalui resistor internal untuk membaca perubahan tahanan NTC.' },
        { step: 2, tag: 'INPUT', title: 'Perubahan Tegangan Sesuai Suhu Coolant', from: 'Thermistor ECT C09', via: 'Pembagi Tegangan', to: 'ECM Pin C37-24', wire: 'PPL/YEL', desc: 'Mesin dingin = tahanan besar (~2,5V); mesin panas 80°C = tahanan kecil (~0,5–0,7V).' },
        { step: 3, tag: 'GROUND', title: 'Massa Sensor C37-57', from: 'Sensor ECT C09 Pin 1', via: 'Kabel GRY/GRN', to: 'ECM Pin C37-57', wire: 'GRY/GRN', desc: 'Menutup rangkaian pembagi tegangan thermistor kembali ke ECM.' }
      ],
      wires: [
        { colorCode: 'PPL/YEL', from: 'Sensor ECT C09 Pin 2', to: 'ECM Pin C37-24', dir: 'in', role: 'Sinyal suhu air radiator', func: 'Mengatur kekayaan BBM saat start dingin dan titik nyala kipas radiator.', keyState: 'IG ON', probe: 'Merah (+) C37-24 · Hitam (−) C37-57', spec: '~2,5 V @20°C · 0,5–0,7 V @80°C (Tahanan 2,0–3,0 kΩ @20°C / 0,29–0,35 kΩ @80°C)', faultHint: 'Jika ~5V terus (scanner -40°C) → soket lepas/putus (P0118), kipas langsung nyala fail-safe.' },
        { colorCode: 'GRY/GRN', from: 'Sensor ECT C09 Pin 1', to: 'ECM Pin C37-57', dir: 'ground', role: 'Massa analog sensor', func: 'Jalur balik sensor suhu ke ECM.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin 1 ECT ↔ C37-57', spec: '< 1 Ω', faultHint: 'Periksa korosi pada soket dekat rumah thermostat.' }
      ]
    },
    {
      id: 'gv_af_ho2s',
      category: 'efi',
      badge: '1A-54 · A/F & O2',
      title: 'Sensor A/F Depan (4-Pin Upstream) & HO2S-2 Belakang (4-Pin C15)',
      subtitle: 'Sensor-1 (4-Pin 2x2: O2 HTR RLY PNK, C37-32/38/37) & Sensor-2 Belakang C15 (C37-47/11/57)',
      dtcs: ['P0030', 'P0031', 'P0032', 'P0037', 'P0038', 'P0131', 'P0132', 'P0133', 'P0134', 'P0137', 'P0138', 'P0140'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_af_heater_p0030_1a54.webp', label: 'Wiring Heater A/F Sensor-1 P0030 (1A-54)', source: 'Vol 1 Bab 1A-54 (Fig I5JB0A110027-02 · DTC P0030/P0031/P0032 Heater A/F Sensor-1)' },
        { img: 'img/jb420_wiring/v1_af_p0131_1a94.webp', label: 'Wiring Sinyal A/F Sensor-1 P0131 (1A-94)', source: 'Vol 1 Bab 1A-94 (Fig I5JB0A110044-02 · DTC P0131/P0132/P0133/P0134 A/F Sensor-1)' },
        { img: 'img/jb420_wiring/v1_ho2s_p0037_1a59.webp', label: 'Wiring Heater HO2S-2 P0037 (1A-59)', source: 'Vol 1 Bab 1A-59 (Fig I5JB0A110032-01 · DTC P0037/P0038 Heater HO2S-2)' },
        { img: 'img/jb420_wiring/v1_ho2s2_p0137_1a97.webp', label: 'Wiring Sinyal HO2S-2 P0137 (1A-97)', source: 'Vol 1 Bab 1A-97 (Fig I5JB0A110045-01 · DTC P0137/P0138/P0140 Sinyal HO2S-2)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p3_9a45.webp', label: 'A-5 Lembar 3 (9A-45)', source: 'Vol 2 Bab 9A-45 (Diagram A-5 Kontrol Mesin)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +12V HO2S Heater Relay & Kontrol PWM Heater', from: 'HO2S Heater Relay (#10 20A O2 HTR) & ECM C37-32 / C37-47', via: 'Kabel PNK (+12V) & PNK/BLU (PWM)', to: 'Heater A/F Sensor-1 (4-Pin) & HO2S-2 (C15)', wire: 'PNK', desc: 'HO2S Heater Relay menyuplai +12V ke Pin 1 Heater, sementara ECM memodulasi ground PWM (C37-32/47) agar elemen keramik mencapai > 350°C dengan cepat.' },
        { step: 2, tag: 'INPUT', title: 'Sinyal Rasio Udara-BBM (4-Pin A/F Sensor-1)', from: 'A/F Sensor-1 (Pin 3 WHT & Pin 4 BLK)', via: 'C37-38 & C37-37', to: 'ECM Input Rasio Lambda', wire: 'WHT', desc: 'Membaca perbandingan udara-bahan bakar secara presisi (3,0–3,2V & 2,6–2,8V) untuk koreksi STFT/LTFT.' },
        { step: 3, tag: 'INPUT', title: 'Monitor Katalis HO2S Sensor-2 (4-Pin C15)', from: 'HO2S-2 Belakang C15 (Pin 2 RED & Pin 1 GRN)', via: 'ECM C37-11 & C37-57', to: 'Monitor Efisiensi Katalis', wire: 'RED', desc: 'Tegangan 0,1–0,9V stabil menandakan katalis sehat; berosilasi cepat menandakan katalis bocor/lemah.' }
      ],
      wires: [
        { colorCode: 'PNK', from: 'HO2S Heater Relay (Sekring #10 20A O2 HTR)', to: 'Pin 1 Heater A/F Sensor-1 & Pin 4 HO2S-2 (+12V)', dir: 'power', role: 'Suplai +12V elemen pemanas (Heater) Sensor-1 & Sensor-2', func: 'Menyuplai tegangan kerja +12V ke kumparan pemanas keramik saat IG ON.', keyState: 'IG ON', probe: 'Merah (+) Pin 1 PNK · Hitam (−) Massa Bodi', spec: '10,0 – 14,0 V DC', faultHint: 'Jika 0V → periksa Sekring #10 (20A O2 HTR) dan HO2S Heater Relay di kotak relay.' },
        { colorCode: 'PNK/BLU', from: 'ECM Pin C37-32 (S1) / C37-47 (S2 BLK/RED)', to: 'Pin 2 Heater (−) A/F Sensor-1 / Pin 3 HO2S-2', dir: 'out', role: 'Kontrol Heater PWM Low-Side dari ECM (P0030–P0032)', func: 'ECM memodulasi ground heater agar suhu elemen stabil > 350°C.', keyState: 'IG OFF (Mode Ohm, Soket Lepas)', probe: 'Ukur Pin 1 ↔ Pin 2 pada soket 4-pin sensor', spec: 'Sensor-1: 2,3–4,3 Ω · Sensor-2: 5–7 Ω @20°C', faultHint: 'Jika tahanan OL (putus) → muncul P0030/P0031 (depan) atau P0037 (belakang).' },
        { colorCode: 'WHT', from: 'A/F Sensor-1 Pin 3 (+)', to: 'ECM Pin C37-38', dir: 'in', role: 'Sinyal utama A/F Sensor (+)', func: 'Mengukur arus pemompaan oksigen pada gas buang sebelum katalis.', keyState: 'IG ON / Idle Hangat', probe: 'Merah (+) C37-38 · Hitam (−) Massa', spec: '3,0 – 3,2 V DC', faultHint: 'Jika jatuh < 1V atau > 4,5V → cek korsleting harness/sensor rusak (P0131/P0132).' },
        { colorCode: 'BLK', from: 'A/F Sensor-1 Pin 4 (−)', to: 'ECM Pin C37-37', dir: 'in', role: 'Sinyal referensi A/F Sensor (−)', func: 'Pasangan tegangan diferensial A/F Sensor-1 (4-Pin 2x2).', keyState: 'IG ON / Idle Hangat', probe: 'Merah (+) C37-37 · Hitam (−) Massa', spec: '2,6 – 2,8 V DC', faultHint: 'Selisih antara C37-38 dan C37-37 sekitar ~0,4 V pada campuran stoikiometri.' }
      ]
    },
    {
      id: 'gv_etc_app',
      category: 'efi',
      badge: '1A-88 · ETC & APP',
      title: 'Throttle Body Elektronik (ETC/TPS) & Pedal Gas (APP)',
      subtitle: 'TPS Main/Sub (C37-44/53) + Motor Actuator (C37-40/41) + Pedal APP (E23)',
      dtcs: ['P0122', 'P0123', 'P0222', 'P0223', 'P2101', 'P2102', 'P2103', 'P2119', 'P2122', 'P2123', 'P2127', 'P2128', 'P2135', 'P2138'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_etc_p0122_1a88.webp', label: 'Wiring Diagram TPS/ETC P0122 (1A-88)', source: 'Vol 1 Bab 1A-88 (DTC P0122 Sirkuit TPS Main · S5JB0A1104073)' },
        { img: 'img/jb420_wiring/v1_app_p2122_1a181.webp', label: 'Wiring Diagram Pedal APP P2122 (1A-181)', source: 'Vol 1 Bab 1A-181 (DTC P2122 Sirkuit Pedal Position Sensor)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p5_9a47.webp', label: 'A-5 Lembar 5 ETC & APP (9A-47)', source: 'Vol 2 Bab 9A-47 (Sensor Pedal Gas & Throttle Body)' }
      ],
      stages: [
        { step: 1, tag: 'INPUT', title: 'Dual Sensor Pedal Gas (APP Main & Sub)', from: 'Pedal Gas Elektronik (6-Pin)', via: 'Jalur Ganda Independen', to: 'ECM Konektor E23', wire: 'YEL', desc: 'Pedal gas memiliki 2 sensor (Main & Sub) yang selalu dibandingkan ECM demi keamanan anti-macet.' },
        { step: 2, tag: 'OUTPUT', title: 'Penggerak Motor DC Throttle Body', from: 'ECM C37-40 (+) & C37-41 (−)', via: 'Sinyal PWM H-Bridge', to: 'Motor Actuator ETC (Pin 1 & 2)', wire: 'RED/BLK', desc: 'ECM membuka/menutup kupu-kupu throttle secara presisi termasuk pengaturan putaran idle.' },
        { step: 3, tag: 'INPUT', title: 'Umpan Balik Dual TPS (Main & Sub)', from: 'TPS Main (C37-44) & Sub (C37-53)', via: 'Vref C37-45 (+5V) & GND C37-54', to: 'ECM Konfirmasi Sudut Bukaan', wire: 'GRN/YEL', desc: 'Bila sudut TPS tidak cocok dengan perintah motor atau beda Main/Sub, ECM masuk Limp Mode.' }
      ],
      wires: [
        { colorCode: 'RED/BLK', from: 'ECM C37-40 & C37-41', to: 'Motor ETC Pin 1 & Pin 2', dir: 'out', role: 'Penggerak motor DC kupu-kupu throttle', func: 'Memutar katup throttle secara elektronik mengikuti injakan pedal gas.', keyState: 'IG OFF (Mode Ohm)', probe: 'Ukur Pin 1 ↔ Pin 2 pada soket Throttle Body', spec: '0,3 – 100 Ω pada 20°C', faultHint: 'Jika kupu-kupu berkerak berat / macet → muncul P2101 / P2119.' },
        { colorCode: 'GRN/YEL', from: 'TPS Main (ETC)', to: 'ECM Pin C37-44', dir: 'in', role: 'Sinyal sudut throttle utama', func: 'Melaporkan sudut aktual bukaan katup throttle ke ECM.', keyState: 'IG ON', probe: 'Merah (+) C37-44 · Hitam (−) C37-54', spec: '0,5–1,1 V (tutup) → 3,6–4,7 V (buka penuh)', faultHint: 'Sinyal putus/drop memicu P0122 & RPM tertahan (limp mode).' },
        { colorCode: 'YEL', from: 'TPS Sub (ETC)', to: 'ECM Pin C37-53', dir: 'in', role: 'Sinyal pembanding throttle (redundansi)', func: 'Memverifikasi keakuratan TPS Main secara real-time.', keyState: 'IG ON', probe: 'Merah (+) C37-53 · Hitam (−) C37-54', spec: '1,4–2,2 V (tutup) → 4,4–4,9 V (buka penuh)', faultHint: 'Selisih tidak wajar antara Main & Sub memicu P2135.' },
        { colorCode: 'GRY/RED', from: 'ECM Pin C37-45 & C37-54', to: 'Suplai +5V & Ground TPS', dir: 'power', role: 'Power referensi +5V & massa TPS', func: 'Menyuplai tegangan kerja untuk sensor posisi throttle.', keyState: 'IG ON', probe: 'Merah (+) C37-45 · Hitam (−) C37-54', spec: '4,5 – 5,5 V DC', faultHint: 'Lakukan prosedur idle relearn setelah membersihkan throttle body.' }
      ]
    },
    {
      id: 'gv_injector',
      category: 'efi',
      badge: '1A-220 · NON-DTC',
      title: 'Sirkuit 4× Injektor Bahan Bakar (Prosedur Non-DTC)',
      subtitle: 'Main Relay (+12V) → 4× Injektor → Driver ECM C37 (Urutan 1-3-4-2)',
      dtcs: ['Non-DTC', 'P0300', 'P0301', 'P0302', 'P0303', 'P0304'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_injector_1a220.webp', label: 'Prosedur Sirkuit Fuel Injector (1A-220)', source: 'Vol 1 Bab 1A-220 (Memeriksa Sirkuit Fuel Injector · S5JB0A1104065)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p2_9a44.webp', label: 'A-5 Lembar 2 Injektor (9A-44)', source: 'Vol 2 Bab 9A-44 (Diagram A-5 Kontrol Mesin)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +12V Bersama dari Main Relay', from: 'Main Relay (Sekring FI)', via: 'Harness Injektor (D)', to: 'Pin 1 Keempat Injektor (#1–#4)', wire: 'BLU/BLK', desc: 'Saat kunci kontak ON, keempat injektor langsung standby menerima +12V.' },
        { step: 2, tag: 'OUTPUT', title: 'Pulsa Ground Sekuensial dari ECM', from: 'Driver Injektor ECM (C37)', via: '4 Kabel Terpisah', to: 'Pin 2 Injektor #1, #2, #3, #4', wire: 'YEL/BLK', desc: 'ECM menarik masing-masing injektor ke massa selama 2–3 milidetik saat idle untuk menyemprotkan BBM.' },
        { step: 3, tag: 'GROUND', title: 'Uji Tahanan Kumparan Injektor', from: 'Soket Injektor Lepas (IG OFF)', via: 'Pin 1 ↔ Pin 2 Injektor', to: 'Multimeter Mode Ohm', wire: 'BLK', desc: 'Tahanan standar injektor J20A berkisar 10–14 Ω pada 20°C (pastikan seragam antar 4 silinder).' }
      ],
      wires: [
        { colorCode: 'BLU/BLK', from: 'Main Relay', to: 'Pin 1 Injektor #1–#4 (+B)', dir: 'power', role: 'Suplai +12V keempat injektor', func: 'Memberikan tegangan kerja bagi kumparan solenoid injektor.', keyState: 'IG ON', probe: 'Merah (+) Pin 1 Injektor · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika semua injektor 0V → periksa Main Relay dan sekring FI.' },
        { colorCode: 'YEL/BLK', from: 'ECM Driver Injektor #1–#4', to: 'Pin 2 Masing-masing Injektor', dir: 'out', role: 'Kontrol semprotan BBM sekuensial (Active Low)', func: 'Mengatur durasi bukaan injektor (ms) berdasarkan sinyal MAF, RPM, dan A/F Sensor.', keyState: 'IG OFF (Ohm) / Cranking (Test Lamp LED)', probe: 'Pin 1 ↔ Pin 2 Injektor (Ohm)', spec: '10 – 14 Ω @20°C · LED test lamp berkedip saat cranking', faultHint: 'Di manual JB420 tidak ada DTC P0201–P0204; gunakan prosedur Bab 1A-220 saat terjadi misfire.' }
      ]
    },
    {
      id: 'gv_fuel_pump',
      category: 'efi',
      badge: '1A-222 · FUEL PUMP',
      title: 'Pompa Bensin (Fuel Pump), Relay & Fuel Level Sensor',
      subtitle: 'ECM Kontrol Relay Fuel Pump → Motor Pompa Tangki (Harness L/R)',
      dtcs: ['Non-DTC', 'P0462', 'P0463'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_fuelpump_1a222.webp', label: 'Sirkuit Fuel Pump & Relay (1A-222)', source: 'Vol 1 Bab 1A-222 (Memeriksa Fuel Pump dan Sirkuitnya · S5JB0A1104066)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p1_9a43.webp', label: 'A-5 Lembar 1 Fuel Pump Relay (9A-43)', source: 'Vol 2 Bab 9A-43 (Diagram A-5 Kontrol Mesin)' },
        { img: 'img/jb420_wiring/v1_fuellevel_p0462_1a129.webp', label: 'Wiring Fuel Level Sensor P0462/P0463 (1A-129)', source: 'Vol 1 Bab 1A-129 (Fig I5JB0A110055-02 · DTC P0462/P0463 Fuel Level Sensor)' }
      ],
      stages: [
        { step: 1, tag: 'OUTPUT', title: 'ECM Mengaktifkan Relay Pompa (Priming 2 Detik)', from: 'ECM Kontrol Fuel Pump Relay', via: 'Relay Pompa Bensin', to: 'Kontak Relay +12V', wire: 'PNK/BLK', desc: 'Saat kunci kontak ON, ECM mengaktifkan relay selama 2 detik (priming) lalu aktif kontinu saat CKP berputar.' },
        { step: 2, tag: 'POWER', title: 'Arus Daya ke Motor Pompa Tangki', from: 'Output Relay Pompa Bensin', via: 'Harness Lantai (L) → Kabel Pompa (R)', to: 'Motor Fuel Pump Tangki', wire: 'PNK', desc: 'Memutar motor pompa untuk menghasilkan tekanan bahan bakar 2,7 – 3,1 kg/cm² di fuel rail.' },
        { step: 3, tag: 'GROUND', title: 'Massa Pompa & Sinyal Pelampung BBM', from: 'Tangki BBM (Pompa & Fuel Level)', via: 'Massa Bodi Belakang', to: 'Ground & Meter / ECM (P0462/P0463)', wire: 'BLK', desc: 'Massa tangki yang berkarat menyebabkan pompa melemah atau jarum bensin tidak akurat.' }
      ],
      wires: [
        { colorCode: 'PNK/BLK', from: 'ECM Pin Kontrol FP', to: 'Kumparan Relay Pompa Bensin', dir: 'out', role: 'Aktivasi Relay Fuel Pump (Active Low)', func: 'Menghidupkan pompa 2 detik saat IG ON & selama mesin berputar.', keyState: 'IG ON (2 detik pertama) / Cranking', probe: 'Merah (+) Pin Kontrol · Hitam (−) Massa', spec: '< 1 V saat priming 2 detik / mesin hidup', faultHint: 'Jika relay tidak berbunyi saat IG ON → cek sekring FI, Main Relay, & sinyal ECM.' },
        { colorCode: 'PNK', from: 'Output Relay Pompa', to: 'Motor Fuel Pump (+)', dir: 'power', role: 'Suplai daya +12V motor pompa tangki', func: 'Menggerakkan pompa bensin tekanan tinggi.', keyState: 'Priming / Cranking', probe: 'Merah (+) Soket Tangki · Hitam (−) Massa', spec: '10 – 14 V DC · Tekanan BBM 2,7–3,1 kg/cm²', faultHint: 'Jika 12V ada di tangki tapi tidak berdengung & tekanan 0 bar → motor pompa bensin macet/mati.' }
      ]
    },
    {
      id: 'gv_cooling_fan',
      category: 'efi',
      badge: 'A-4 · COOLING FAN',
      title: 'Sistem Kipas Radiator (Putaran Rendah & Tinggi)',
      subtitle: 'ECM E23-46/47/48 → Relay Fan #1, #2, #3 (Sekring 30A RAD FAN)',
      dtcs: ['P0480'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a4_pendingin_9a42.webp', label: 'Diagram A-4 Sistim Pendingin (9A-42)', source: 'Vol 2 Bab 9A-42 (A-4 Diagram Sirkuit Sistim Pendingin · S5JB0A910E004)' },
        { img: 'img/jb420_wiring/v1_fan_p0480_1a133.webp', label: 'Wiring Diagram P0480 (1A-133)', source: 'Vol 1 Bab 1A-133 (DTC P0480 Sirkuit Kontrol Kipas Radiator 1)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Daya Utama Sekring 30A RAD FAN', from: 'Aki +12V → Box Sikring No.2', via: 'Sekring 30A RAD FAN & Relay #1/#2/#3', to: 'Motor Kipas Radiator & Kondensor', wire: 'WHT/RED', desc: 'Jalur arus besar terpisah melalui Box Sikring No.2 ruang mesin.' },
        { step: 2, tag: 'OUTPUT', title: 'Kontrol 2 Kecepatan dari ECM', from: 'ECM E23-46 (Low) & E23-47/48 (High)', via: 'Kumparan Relay Fan', to: 'Aktivasi Seri (Low) / Paralel (High)', wire: 'LT GRN', desc: 'ECM menyalakan putaran rendah saat ECT ~98°C atau AC ON, dan putaran tinggi saat suhu/tekanan AC naik.' },
        { step: 3, tag: 'GROUND', title: 'Massa Motor Kipas', from: 'Terminal Negatif Motor Fan', via: 'Harness Depan', to: 'Titik Ground Ruang Mesin', wire: 'BLK', desc: 'Pastikan tahanan massa motor < 1 Ω agar putaran kipas tidak loyo.' }
      ],
      wires: [
        { colorCode: 'WHT/RED', from: 'Sekring 30A RAD FAN', to: 'Kontak Relay Fan #1/#2', dir: 'power', role: 'Suplai arus tinggi motor kipas', func: 'Menyuplai arus besar 12V untuk memutar motor kipas radiator.', keyState: 'IG ON / Selalu Ada (+B)', probe: 'Merah (+) Input Relay · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika putus berulang → cek motor kipas macet atau korsleting.' },
        { colorCode: 'LT GRN', from: 'ECM Pin E23-46', to: 'Relay Kipas Radiator #1', dir: 'out', role: 'Kontrol Kipas Putaran Rendah (P0480)', func: 'ECM menarik ke ground untuk mengaktifkan Relay Fan #1.', keyState: 'AC ON / Suhu > 98°C', probe: 'Merah (+) E23-46 · Hitam (−) Massa', spec: '< 1 V saat kipas diperintah ON · 10–14 V saat OFF', faultHint: 'Gunakan Active Test di scanner untuk memaksa kipas ON tanpa menunggu panas.' },
        { colorCode: 'BLU/WHT', from: 'ECM Pin E23-47 & E23-48', to: 'Relay Kipas #2 & #3 (High Speed)', dir: 'out', role: 'Kontrol Kipas Putaran Tinggi', func: 'Mengubah rangkaian 2 kipas dari seri (Low) menjadi paralel (High).', keyState: 'Suhu > 103°C / Tekanan AC Tinggi', probe: 'Merah (+) E23-47/48 · Hitam (−) Massa', spec: '< 1 V saat High Speed aktif', faultHint: 'Jika Low jalan tapi High mati → cek Relay #2 & #3.' }
      ]
    },
    {
      id: 'gv_cranking',
      category: 'efi',
      badge: 'A-1 · STARTER',
      title: 'Sistem Starter & Relay Cranking (A/T & M/T)',
      subtitle: 'Kunci Kontak ST → Sekring ST → Starter Relay → Range Switch A/T → Starter',
      dtcs: ['P0616', 'P0617'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a1_cranking_9a39.webp', label: 'Diagram A-1 Cranking / Starter (9A-39)', source: 'Vol 2 Bab 9A-39 (A-1 Diagram Sirkuit Sistim Cranking · S5JB0A910E001)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Sinyal Kunci Kontak Posisi START', from: 'Kunci Kontak ST → Sekring ST SIG', via: 'Kabel BLK/YEL', to: 'Relay Starting Motor Control & ECM', wire: 'BLK/YEL', desc: 'Mengirim sinyal permintaan starter dari kunci kontak ke relay & ECM.' },
        { step: 2, tag: 'GROUND', title: 'Pengaman Posisi P/N (Model A/T)', from: 'Kumparan Starter Relay', via: 'Transmission Range Switch (P/N)', to: 'Massa Bodi (BLK)', wire: 'BLK/RED', desc: 'Pada mobil A/T, starter hanya bisa aktif jika tuas di P atau N; pada M/T langsung ke massa.' },
        { step: 3, tag: 'OUTPUT', title: 'Arus Utama Solenoid & Motor Starter', from: 'Aki +12V & Output Relay Starter', via: 'Kabel Tebal & Terminal 50', to: 'Starting Motor Magnet Clutch', wire: 'BLK/YEL', desc: 'Menarik bendik starter dan memutar flywheel mesin.' }
      ],
      wires: [
        { colorCode: 'BLK/YEL', from: 'Kunci Kontak ST / Sekring ST', to: 'Relay Starter & Terminal 50 Starter', dir: 'power', role: 'Arus pemicu solenoid starter', func: 'Mengaktifkan magnet clutch starter saat kunci diputar ke START.', keyState: 'Posisi START (Cranking)', probe: 'Merah (+) Terminal 50 · Hitam (−) Massa', spec: '≥ 9,5 V saat distarter', faultHint: 'Jika 0V saat di-start pada mobil A/T → coba geser tuas ke N (uji Range Switch).' },
        { colorCode: 'BLK/RED', from: 'Relay Starter', to: 'Transmission Range Switch (A/T)', dir: 'ground', role: 'Interlock pengaman posisi P/N (A/T)', func: 'Mencegah mesin distarter saat transmisi masuk gigi D/R.', keyState: 'Tuas P atau N (IG OFF Ohm)', probe: 'Ukur kontinuitas ke massa pada P & N', spec: '< 1 Ω di P/N · OL (terbuka) di R/D', faultHint: 'Range switch kotor/bergeser sering bikin mobil mati total tidak bisa distarter.' }
      ]
    },
    {
      id: 'gv_charging',
      category: 'efi',
      badge: 'A-2 · PENGISIAN',
      title: 'Sistem Pengisian (Alternator) & Electric Load Sensor',
      subtitle: 'Generator Control (P0620/P0625/P0626) & ELD Sensor (P1501/P1502)',
      dtcs: ['P0620', 'P0625', 'P0626', 'P1501', 'P1502'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a2_pengisian_9a40.webp', label: 'Diagram A-2 Pengisian / Alternator (9A-40)', source: 'Vol 2 Bab 9A-40 (A-2 Diagram Sirkuit Sistim Pengisian · S5JB0A910E002)' },
        { img: 'img/jb420_wiring/v1_eld_p1501_1a154.webp', label: 'Wiring Diagram ELD P1501 (1A-154)', source: 'Vol 1 Bab 1A-154 (DTC P1501/P1502 Electric Load Current Sensor)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Output Utama Alternator Terminal B+', from: 'Alternator (B+) → Sekring Utama 100A', via: 'Kabel Daya Tebal', to: 'Terminal Positif Aki (+)', wire: 'WHT', desc: 'Mengisi aki dan menyuplai seluruh kelistrikan mobil saat mesin hidup (13,8–14,6 V).' },
        { step: 2, tag: 'OUTPUT', title: 'Kontrol Regulasi ECM & Lampu Indikator', from: 'ECM Kontrol Generator & Meter', via: 'Soket 4-Pin Alternator (IG, L, C, FR)', to: 'IC Regulator Alternator', wire: 'BLK/WHT', desc: 'ECM mengatur beban pengisian alternator agar efisiensi BBM optimal dan aki tidak overcharge.' },
        { step: 3, tag: 'INPUT', title: 'Sensor Beban Listrik (ELD)', from: 'Electric Load Current Sensor (Box Sekring)', via: 'Sinyal Beban Arus', to: 'ECM (P1501/P1502)', wire: 'GRN/RED', desc: 'Memberitahu ECM saat lampu/AC/defogger menyala agar RPM idle & pengisian dinaikkan.' }
      ],
      wires: [
        { colorCode: 'WHT', from: 'Alternator Terminal B+', to: 'Main Fuse 100A → Aki (+)', dir: 'power', role: 'Output utama arus pengisian aki', func: 'Mengalirkan arus pengisian DC dari alternator ke baterai.', keyState: 'Mesin Hidup (2000 rpm)', probe: 'Merah (+) Aki (+) · Hitam (−) Aki (−)', spec: '13,8 – 14,6 V (beban lampu/AC ON tetap > 13,2 V)', faultHint: 'Jika < 12,5V saat mesin hidup → cek main fuse, carbon brush, atau IC regulator.' },
        { colorCode: 'BLK/WHT', from: 'Sekring IG', to: 'Alternator Terminal IG', dir: 'power', role: 'Excitation +12V IC Regulator', func: 'Mengaktifkan regulator alternator saat kunci kontak ON.', keyState: 'IG ON', probe: 'Merah (+) Pin IG Alternator · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Putus sekring IG membuat alternator tidak mau mengisi sama sekali.' }
      ]
    },
    {
      id: 'gv_knock',
      category: 'efi',
      badge: '1A-113 · KNOCK',
      title: 'Knock Sensor (Sensor Detonasi / Ngelitik — 1-Pin C26)',
      subtitle: 'Sensor Piezoelektrik 1-Pin C26 (WHT C37-56) + Massa Langsung Bodi Baut Blok Mesin',
      dtcs: ['P0327', 'P0328'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_knock_p0327_1a113.webp', label: 'Wiring Diagram Knock Sensor P0327 (1A-113)', source: 'Vol 1 Bab 1A-113 (Fig I5JB0A110046-01 · DTC P0327/P0328 Knock Sensor)' }
      ],
      stages: [
        { step: 1, tag: 'INPUT', title: 'Deteksi Getaran Detonasi Blok Mesin (1-Pin C26)', from: 'Elemen Piezoelektrik Knock Sensor C26 Pin 1', via: 'Kabel WHT Berpelindung Shield', to: 'ECM Input Knock C37-56', wire: 'WHT', desc: 'Menghasilkan tegangan AC kecil bila terjadi pembakaran ngelitik (knocking) agar ECM memundurkan timing.' },
        { step: 2, tag: 'GROUND', title: 'Massa Langsung Bodi Baut (23 N·m) & Shield', from: 'Bodi Sensor (Baut Blok) & Shield Kabel', via: 'Blok Mesin & Ground ECM', to: 'Massa Blok Mesin', wire: 'BLK', desc: 'Soket C26 hanya memiliki 1 pin sinyal; jalur massa sensor langsung melalui baut pengikat ke blok silinder.' },
        { step: 3, tag: 'INPUT', title: 'Cek Tahanan Internal Resistor 500–620 kΩ', from: 'Soket 1-Pin C26 (IG OFF)', via: 'Ukur Tahanan Pin 1 ↔ Bodi Sensor', to: 'Multimeter Skala MΩ', wire: 'WHT', desc: 'Resistor internal digunakan ECM untuk mendeteksi sirkuit putus (P0327) atau short (P0328).' }
      ],
      wires: [
        { colorCode: 'WHT', from: 'Knock Sensor C26 Pin 1', to: 'ECM Pin C37-56', dir: 'in', role: 'Sinyal getaran detonasi mesin 1-Pin (P0327/P0328)', func: 'Mencegah kerusakan piston akibat pembakaran terlalu cepat/BBM oktan rendah.', keyState: 'IG OFF (Mode Ohm) / IG ON (Bias 2–3V)', probe: 'Pin 1 C26 ↔ Bodi Logam Sensor Knock', spec: '500 – 620 kΩ (nominal ~560 kΩ @20°C) · Bias 2,0–3,0 V', faultHint: 'Kencangkan baut pengikat tepat 23 N·m karena bodi baut sekaligus menjadi massa sensor.' }
      ]
    },
    {
      id: 'gv_egr_evap_imtv',
      category: 'efi',
      badge: '1A-120 · EMISI & IMTV',
      title: 'Katup EGR, EVAP Purge Valve & IMTV (Intake Tuning)',
      subtitle: 'Kontrol Emisi Gas Buang (P0401–P0403), Uap Tangki (P0443) & IMTV (P0660)',
      dtcs: ['P0401', 'P0402', 'P0403', 'P0443', 'P0660'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_egr_p0401_1a120.webp', label: 'Wiring EGR Induk P0401–P0403 (1A-120)', source: 'Vol 1 Bab 1A-120 (Fig I5JB0A110051-01 · DTC P0401/P0402/P0403 Katup EGR C10)' },
        { img: 'img/jb420_wiring/v1_evap_p0443_1a127.webp', label: 'Wiring EVAP Purge P0443 (1A-127)', source: 'Vol 1 Bab 1A-127 (Fig I5JB0A110054-02 · DTC P0443 EVAP Purge Control Valve)' },
        { img: 'img/jb420_wiring/v1_imtv_p0660_1a152.webp', label: 'Wiring IMTV P0660 (1A-152)', source: 'Vol 1 Bab 1A-152 (Fig I5JB0A110064-02 · DTC P0660 Intake Manifold Tuning Valve)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +12V Aktuator Emisi dari Main Relay', from: 'Main Relay (+12V)', via: 'Kabel BLU/BLK', to: 'Stepper EGR, EVAP Solenoid & IMTV', wire: 'BLU/BLK', desc: 'Ketiga aktuator emisi menerima suplai +12V bersama dari Main Relay saat IG ON.' },
        { step: 2, tag: 'OUTPUT', title: 'Kontrol Stepper 4-Fasa (EGR) & PWM (EVAP/IMTV)', from: 'ECM Driver Emisi (C37)', via: '4 Kabel Stepper EGR / 1 Kabel Solenoid', to: 'EGR Valve · EVAP Purge · IMTV', wire: 'GRN/ORN', desc: 'ECM mengatur aliran EGR untuk menekan NOx, membakar uap tangki EVAP, dan mengubah panjang intake (IMTV).' },
        { step: 3, tag: 'GROUND', title: 'Uji Tahanan Kumparan & Kebersihan Saluran', from: 'Soket Aktuator (IG OFF)', via: 'Mode Ohm', to: 'Verifikasi Kumparan & Jelaga Karbon', wire: 'BLK', desc: 'Pada P0401/P0402 sering kali katup & saluran EGR tersumbat kerak karbon mekanis.' }
      ],
      wires: [
        { colorCode: 'BLU/BLK', from: 'Main Relay', to: 'EGR / EVAP / IMTV (+B)', dir: 'power', role: 'Suplai +12V aktuator kontrol emisi', func: 'Menyuplai daya kerja bagi motor stepper EGR dan solenoid EVAP/IMTV.', keyState: 'IG ON', probe: 'Merah (+) Pin Power · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika P0403, P0443, P0660 muncul serentak → cek jalur power bersama Main Relay!' },
        { colorCode: 'GRN/ORN', from: 'ECM Driver Stepper/Solenoid', to: 'Pin Kontrol EGR / EVAP / IMTV', dir: 'out', role: 'Perintah buka-tutup katup emisi', func: 'Menggerakkan katup sesuai putaran & beban mesin.', keyState: 'IG OFF (Mode Ohm)', probe: 'Ukur kumparan pada soket katup', spec: 'EGR Stepper: ~20–24 Ω tiap kumparan · EVAP/IMTV: ~30–38 Ω @20°C', faultHint: 'Untuk P0401/P0402 bersihkan kerak karbon katup EGR dan pipa salurannya.' }
      ]
    },
    {
      id: 'gv_vss_brake_ac',
      category: 'efi',
      badge: '1A-137 · VSS / REM / AC',
      title: 'Sensor Kecepatan (VSS), Switch Rem & Tekanan A/C',
      subtitle: 'Sinyal Pendukung Idle & Cut-Off ECM (P0500, P0504, P0532/P0533)',
      dtcs: ['P0500', 'P0504', 'P0532', 'P0533'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_vss_p0500_1a137.webp', label: 'Wiring VSS P0500 (1A-137)', source: 'Vol 1 Bab 1A-137 (DTC P0500 Vehicle Speed Sensor)' },
        { img: 'img/jb420_wiring/v1_brake_p0504_1a139.webp', label: 'Wiring Switch Rem P0504 (1A-139)', source: 'Vol 1 Bab 1A-139 (DTC P0504 Korelasi Switch Rem A/B)' },
        { img: 'img/jb420_wiring/v1_acpress_p0532_1a141.webp', label: 'Wiring Tekanan A/C P0532 (1A-141)', source: 'Vol 1 Bab 1A-141 (DTC P0532 A/C Refrigerant Pressure Sensor)' }
      ],
      stages: [
        { step: 1, tag: 'INPUT', title: 'Sinyal Kecepatan Kendaraan (VSS)', from: 'ABS / Transmisi → Speedometer', via: 'Jalur Sinyal Kecepatan', to: 'ECM (P0500)', wire: 'PPL', desc: 'Digunakan ECM untuk kontrol deselerasi fuel-cut & penyesuaian idle berjalan.' },
        { step: 2, tag: 'INPUT', title: 'Korelasi 2 Kontak Switch Pedal Rem', from: 'Stop Lamp Switch (Kontak A & B)', via: 'Dual Signal +12V/0V', to: 'ECM (P0504)', wire: 'GRN/WHT', desc: 'Dua kontak harus berubah saling berlawanan saat pedal rem diinjak; jika sama → P0504.' },
        { step: 3, tag: 'INPUT', title: 'Sensor Tekanan Freon A/C (3-Pin)', from: 'A/C Pressure Sensor (+5V, SIG, GND)', via: 'Harness Depan', to: 'ECM (P0532/P0533)', wire: 'RED/BLU', desc: 'Melindungi kompresor AC jika freon kosong (< 0,2V) atau tekanan berlebih (> 4,8V) dan memicu fan High.' }
      ],
      wires: [
        { colorCode: 'GRN/WHT', from: 'Switch Pedal Rem (A/B)', to: 'ECM Pin Brake Sense', dir: 'in', role: 'Status injakan pedal rem (P0504)', func: 'Mengamankan sistem Electronic Throttle & transmisi A/T saat pengereman.', keyState: 'IG ON (Lepas vs Injak Rem)', probe: 'Ukur 2 jalur output switch pedal rem', spec: 'Kontak A & B saling terbalik (0V ↔ 12V)', faultHint: 'Bohlam lampu rem putus / LED aftermarket tanpa resistor kadang memicu P0504.' },
        { colorCode: 'RED/BLU', from: 'A/C Pressure Sensor', to: 'ECM Input Tekanan A/C', dir: 'in', role: 'Sinyal tekanan refrigeran A/C (P0532/P0533)', func: 'Mengizinkan kopling kompresor AC aktif & mengatur kecepatan kipas kondensor.', keyState: 'IG ON / AC ON', probe: 'Merah (+) Pin Sinyal · Hitam (−) Massa Sensor', spec: '0,5 – 4,5 V proporsional tekanan freon (Vref = 5V)', faultHint: 'Jika 0V → cek freon habis atau kabel sensor di pipa kondensor putus.' }
      ]
    },
    {
      id: 'gv_can_bus',
      category: 'efi',
      badge: '1A-159 · CAN BUS',
      title: 'Jaringan Komunikasi CAN Bus (ECM ↔ TCM ↔ ABS ↔ BCM)',
      subtitle: 'Kabel Pilin CAN-High (RED/WHT) & CAN-Low (WHT/BLU) · Terminasi 60 Ω',
      dtcs: ['P1674', 'P1676', 'P1678', 'P1685', 'U1073', 'U1100'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v1_can_p1674_1a159.webp', label: 'Wiring Diagram CAN Bus P1674 (1A-159)', source: 'Vol 1 Bab 1A-159 (DTC P1674 Komunikasi CAN Putus/Error · S5JB0A1104058)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p4_9a46.webp', label: 'A-5 Lembar 4 Jalur DLC & CAN (9A-46)', source: 'Vol 2 Bab 9A-46 (Jalur CAN & DLC 16-Pin)' }
      ],
      stages: [
        { step: 1, tag: 'INPUT', title: 'Tulang Punggung Data CAN-H & CAN-L', from: 'ECM (Resistor Terminasi 120 Ω)', via: 'Joint Connector (J/C) Kabel Pilin', to: 'TCM, ABS, BCM, Speedometer & DLC Pin 6/14', wire: 'RED', desc: 'Seluruh modul bertukar data RPM, kecepatan roda, & status rem secara digital kecepatan tinggi.' },
        { step: 2, tag: 'GROUND', title: 'Uji Tahanan Terminasi 60 Ω (Wajib IG OFF!)', from: 'Soket OBD-II DLC Pin 6 (CAN-H)', via: '2 Resistor 120 Ω Paralel (ECM & BCM)', to: 'Soket OBD-II DLC Pin 14 (CAN-L)', wire: 'WHT', desc: 'Aki dilepas → ukur tahanan Pin 6 ↔ Pin 14: normal 54–66 Ω (~60 Ω). Jika 120 Ω = 1 cabang putus!' },
        { step: 3, tag: 'OUTPUT', title: 'Uji Tegangan Komunikasi Aktif (IG ON)', from: 'DLC Pin 6 (CAN-H) & Pin 14 (CAN-L)', via: 'Tegangan Diferensial', to: 'Multimeter DC Volt', wire: 'WHT/RED', desc: 'CAN-H normal ~2,5–3,5V dan CAN-L ~1,5–2,5V (jumlah keduanya selalu ~5,0V).' }
      ],
      wires: [
        { colorCode: 'RED', from: 'DLC Pin 6 · J/C G74/G75', to: 'ECM · TCM · ABS · BCM (CAN-H)', dir: 'in', role: 'Saluran Data Tinggi CAN-High', func: 'Mengirim bit data digital kecepatan tinggi antar komputer mobil.', keyState: 'IG OFF (Aki Lepas) / IG ON', probe: 'Ohm: Pin 6 ↔ 14 · Volt: Pin 6 ↔ Massa', spec: 'Tahanan: 54 – 66 Ω · Tegangan IG ON: ~2,6 – 3,5 V', faultHint: 'Jika tahanan < 10 Ω → salah satu modul/kabel CAN short, lepas soket modul satu per satu.' },
        { colorCode: 'WHT', from: 'DLC Pin 14 · J/C G74/G75', to: 'ECM · TCM · ABS · BCM (CAN-L)', dir: 'in', role: 'Saluran Data Rendah CAN-Low', func: 'Pasangan diferensial anti-gangguan dari saluran CAN-High.', keyState: 'IG ON', probe: 'Merah (+) DLC Pin 14 · Hitam (−) Massa', spec: 'Tegangan IG ON: ~1,5 – 2,4 V (CAN-H + CAN-L ≈ 5,0 V)', faultHint: 'Jika 120 Ω → jalur menuju salah satu modul ujung (ECM atau BCM/Meter) terputus.' }
      ]
    },
    {
      id: 'gv_nonwiring_p0171',
      category: 'efi',
      badge: '⚠️ NON-WIRING · P0171',
      title: 'Sistem Bahan Bakar Terlalu Kurus / Kaya (P0171 / P0172)',
      subtitle: 'Gangguan Mekanis / Vakum / Tekanan BBM — Bukan Sekadar 1 Kabel Putus!',
      dtcs: ['P0171', 'P0172', 'P2195', 'P2196'],
      isNonWiring: true,
      nonWiringSummary: 'DTC P0171 (Terlalu Kurus) & P0172 (Terlalu Kaya) adalah gangguan kinerja sistem campuran udara-bahan bakar (Functional/System Fault), BUKAN kerusakan sirkuit kabel tunggal. Mengganti sensor O2/A-F tanpa memeriksa kebocoran vakum atau tekanan BBM adalah kesalahan paling umum di bengkel!',
      mechChecks: [
        { step: 1, title: 'Cek Kebocoran Vakum Intake & Selang PCV', detail: 'Periksa selang intake setelah MAF, selang vakum PCV, selang booster rem, dan gasket intake manifold dari retak/sobek (udara liar masuk tidak terukur MAF → LTFT naik > +15%).' },
        { step: 2, title: 'Ukur Tekanan Bahan Bakar (Fuel Pressure Gauge)', detail: 'Standar JB420 (1G): 2,7 – 3,1 kg/cm² (270–310 kPa) saat idle. Jika < 2,5 kg/cm² → saringan pompa tangki mampet, regulator bocor, atau pompa bensin lemah.' },
        { step: 3, title: 'Periksa Kebocoran Pipa Knalpot Sebelum Sensor-1', detail: 'Kebocoran paking exhaust manifold menyedot oksigen luar ke dekat A/F Sensor-1 sehingga ECM tertipu mengira campuran kurus.' },
        { step: 4, title: 'Verifikasi Sensor MAF, A/F Sensor & Injektor (Buka Pintasan Wiring di Bawah)', detail: 'Bila 3 cek mekanis di atas 100% normal, lanjut uji tegangan MAF (1,3–1,8V idle hangat), A/F Sensor, dan pola semprotan injektor.' }
      ],
      relatedIds: ['gv_maf_iat', 'gv_af_ho2s', 'gv_injector', 'gv_fuel_pump'],
      safetyGuard: 'none',
      photos: [
        { img: 'img/jb420_wiring/v1_p0171_ref_1a101.webp', label: 'Tabel Diagnosa Resmi P0171 (1A-101)', source: 'Vol 1 Bab 1A-101 (DTC P0171/P0172 Sistim Bahan Bakar Terlalu Kurus/Kaya · S5JB0A1104037)' }
      ],
      stages: [],
      wires: []
    },
    {
      id: 'gv_nonwiring_p0420',
      category: 'efi',
      badge: '⚠️ NON-WIRING · P0420',
      title: 'Efisiensi Catalytic Converter Rendah (P0420)',
      subtitle: 'Gangguan Fisik Katalis / Kebocoran Exhaust — Cek Mekanis Sebelum Ganti Part',
      dtcs: ['P0420'],
      isNonWiring: true,
      nonWiringSummary: 'DTC P0420 muncul saat ECM melihat gelombang tegangan HO2S Sensor-2 (belakang katalis) ikut naik-turun cepat meniru Sensor-1 (depan). Ini bukan kabel putus, melainkan penurunan kapasitas penyimpan oksigen pada Catalytic Converter atau kebocoran knalpot.',
      mechChecks: [
        { step: 1, title: 'Pastikan Tidak Ada DTC Misfire (P030x) atau Fuel Trim (P0171/P0172)', detail: 'Pembakaran tidak sempurna (busi/koil rusak) akan membanjiri katalis dengan bensin mentah dan memicu P0420 palsu — selesaikan misfire lebih dulu.' },
        { step: 2, title: 'Periksa Kebocoran Paking Exhaust & Leher Knalpot', detail: 'Retakan pipa di antara Sensor-1 dan Sensor-2 membuat gas buang tercampur udara luar sehingga pembacaan efisiensi katalis gagal.' },
        { step: 3, title: 'Bandingkan Grafik Live Data A/F Sensor-1 vs HO2S Sensor-2', detail: 'Pada 2.000 rpm mesin hangat, katalis sehat menjaga tegangan HO2S-2 relatif stabil (~0,6–0,8V). Bila berosilasi cepat 0,1↔0,8V → katalis jenuh/rusak.' }
      ],
      relatedIds: ['gv_af_ho2s', 'gv_ign_coil', 'gv_nonwiring_p0171'],
      safetyGuard: 'none',
      photos: [
        { img: 'img/jb420_wiring/v1_cat_p0420_1a125.webp', label: 'Diagram Sistem Katalis P0420 (1A-125)', source: 'Vol 1 Bab 1A-125 (Fig I5JB0A110053-02 · DTC P0420 Efisiensi Catalyst & Sensor O2)' },
        { img: 'img/jb420_wiring/v1_ho2s2_p0137_1a97.webp', label: 'Wiring Sinyal HO2S-2 Belakang (1A-97)', source: 'Vol 1 Bab 1A-97 (Fig I5JB0A110045-01 · Monitor HO2S-2)' }
      ],
      stages: [],
      wires: []
    },
    {
      id: 'gv_ecm_full_a5',
      category: 'efi',
      badge: 'A-5 · FULL ECM (5 LEMBAR)',
      title: 'Diagram Utuh A-5: Seluruh Sistem Kontrol Mesin & A/C',
      subtitle: 'Peta Induk 5 Halaman Penuh Konektor ECM C37 & E23 (Vol 2 Hal. 9A-43 s/d 9A-47)',
      dtcs: ['A-5', 'C37', 'E23'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a5_ecm_p1_9a43.webp', label: 'A-5 Hal. 1 (9A-43 · Power & FP)', source: 'Vol 2 Bab 9A-43 (A-5 Lembar 1/5 — Power ECM, Main Relay, Fuel Pump)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p2_9a44.webp', label: 'A-5 Hal. 2 (9A-44 · Injektor/CKP/CMP)', source: 'Vol 2 Bab 9A-44 (A-5 Lembar 2/5 — Injektor, CKP, CMP, Knock)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p3_9a45.webp', label: 'A-5 Hal. 3 (9A-45 · MAF/MAP/ECT/O2/EGR)', source: 'Vol 2 Bab 9A-45 (A-5 Lembar 3/5 — MAF/IAT, MAP, ECT, O2/A-F, EGR)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p4_9a46.webp', label: 'A-5 Hal. 4 (9A-46 · CAN/DLC/AC/VSS)', source: 'Vol 2 Bab 9A-46 (A-5 Lembar 4/5 — CAN Bus, DLC, A/C, Brake, VSS)' },
        { img: 'img/jb420_wiring/v2_a5_ecm_p5_9a47.webp', label: 'A-5 Hal. 5 (9A-47 · ETC & Pedal APP)', source: 'Vol 2 Bab 9A-47 (A-5 Lembar 5/5 — Throttle Body ETC & Sensor Pedal Gas)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Lembar 1–2: Daya ECM, Pengapian, Injektor & CKP/CMP', from: 'Sekring & Main Relay', via: '9A-43 & 9A-44', to: 'ECM C37/E23 + Aktuator Pembakaran', wire: 'BLU/BLK', desc: 'Gunakan Lembar 1–2 untuk kasus mesin mati total, tidak ada api, atau tidak ada semprotan bensin.' },
        { step: 2, tag: 'INPUT', title: 'Lembar 3–4: Seluruh Sensor Mesin, Emisi & CAN Bus', from: 'MAF, MAP, ECT, O2, EGR, CAN', via: '9A-45 & 9A-46', to: 'ECM & Soket DLC 16-Pin', wire: 'RED/YEL', desc: 'Gunakan Lembar 3–4 untuk kasus boros BBM, brebet, emisi, dan gagal konek scanner.' },
        { step: 3, tag: 'OUTPUT', title: 'Lembar 5: Kontrol Gas Elektronik (ETC & APP)', from: 'Pedal Gas APP ↔ Throttle Body ETC', via: '9A-47', to: 'ECM C37-40..54', wire: 'GRN/YEL', desc: 'Gunakan Lembar 5 untuk kasus gas tidak merespons (Limp Mode).' }
      ],
      wires: [
        { colorCode: 'BLU/BLK', from: 'Main Relay', to: 'Seluruh Jalur +12V Mesin (9A-43)', dir: 'power', role: 'Tulang punggung suplai +12V EFI', func: 'Menyuplai ECM, MAF, CMP, Injektor, Heater O2, EGR, dan EVAP secara paralel.', keyState: 'IG ON', probe: 'Cek di E23-1 / E23-16', spec: '10 – 14 V DC', faultHint: 'Gunakan tombol "Foto Asli OEM" di atas untuk menggeser 5 lembar penuh peta A-5!' },
        { colorCode: 'GRY/GRN', from: 'ECM Pin C37-57 (Sensor Ground)', to: 'IAT, MAP, ECT & Sensor Analog (9A-45)', dir: 'ground', role: 'Massa analog presisi seluruh sensor mesin', func: 'Menjadi titik referensi 0V stabil bagi sensor suhu dan tekanan intake.', keyState: 'IG OFF (Mode Ohm)', probe: 'C37-57 ↔ Massa Bodi', spec: '< 3 Ω', faultHint: 'Jika putus → muncul DTC tinggi bersamaan (P0108, P0113, P0118).' },
        { colorCode: 'BLK/ORN', from: 'ECM C37-15/29/48 & Koil', to: 'Titik Ground Blok Mesin #5 (9A-43)', dir: 'ground', role: 'Massa daya utama komputer ECM', func: 'Jalur balik arus kerja seluruh driver aktuator mesin.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin Ground C37 ↔ Aki (−)', spec: '< 1 Ω (Volt Drop < 0,2 V)', faultHint: 'Cek selalu kekencangan baut massa blok pasca servis besar mesin.' }
      ]
    },

    // =========================================================================
    // KATEGORI 2: 7 MODUL KONTROL ELEKTRONIK BER-DTC (VOL 1 4E & VOL 2 BAB 9A)
    // =========================================================================
    {
      id: 'gv_mod_tcm',
      category: 'modules',
      badge: 'A-6 · TCM A/T (27 DTC)',
      title: 'Modul Transmisi Otomatis A/T (TCM — E92 & E93)',
      subtitle: 'Shift Solenoid A/B, TCC Lock-Up, Range Switch, Input/Output Speed & ATF Temp',
      dtcs: ['P0705', 'P0707', 'P0712', 'P0713', 'P0751', 'P0756', 'P1603'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a6_tcm_p1_9a48.webp', label: 'A-6 TCM Lembar 1 (9A-48)', source: 'Vol 2 Bab 9A-48 (A-6 Diagram Sirkuit Sistim Kontrol A/T · S5JB0A910E006)' },
        { img: 'img/jb420_wiring/v2_a6_tcm_p2_9a49.webp', label: 'A-6 TCM Lembar 2 (9A-49)', source: 'Vol 2 Bab 9A-49 (A-6 Lembar 2/2 — Solenoid & Sensor Transmisi A/T)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Power Supply & Ground TCM (E92/E93)', from: 'Sekring Back-Up & IG', via: 'Harness Instrumen (E)', to: 'TCM E92 (24-Pin) & E93 (26-Pin)', wire: 'BLK/WHT', desc: 'TCM membutuhkan +12V konstan, +12V IG ON, serta komunikasi CAN dengan ECM.' },
        { step: 2, tag: 'INPUT', title: 'Sensor Posisi Tuas, Kecepatan & Suhu ATF', from: 'Range Switch (P0705), Speed Sensor & ATF Temp (P0712)', via: 'Harness Transmisi', to: 'Input TCM E92/E93', wire: 'BLU/YEL', desc: 'Menentukan waktu perpindahan gigi yang halus sesuai kecepatan roda & beban gas.' },
        { step: 3, tag: 'OUTPUT', title: 'Shift Solenoid A/B & Lock-Up Solenoid', from: 'Driver Output TCM', via: 'Soket Transmisi A/T', to: 'Solenoid Valve Body (P0751)', wire: 'YEL/GRN', desc: 'Mengatur tekanan hidrolik perpindahan gigi 1–4 dan penguncian Torque Converter.' }
      ],
      wires: [
        { colorCode: 'BLK/WHT', from: 'Sekring IG / J/B', to: 'TCM Power IG (+12V)', dir: 'power', role: 'Suplai daya operasional TCM', func: 'Menghidupkan komputer transmisi otomatis saat kunci kontak ON.', keyState: 'IG ON', probe: 'Konektor E92/E93 Pin Power ↔ Massa', spec: '10 – 14 V DC', faultHint: 'Power TCM hilang membuat transmisi masuk fail-safe tertahan di gigi 3.' },
        { colorCode: 'BLU/YEL', from: 'Shift Solenoid A/B & TCC', to: 'TCM Konektor E92/E93', dir: 'out', role: 'Kontrol solenoid perpindahan gigi (P0751)', func: 'Membuka/menutup jalur oli ATF ke kopling gigi transmisi.', keyState: 'IG OFF (Mode Ohm)', probe: 'Ukur tahanan pin solenoid ↔ massa bodi transmisi', spec: '11 – 15 Ω pada 20°C', faultHint: 'Tahanan di luar 11–15 Ω atau oli ATF terbakar memicu nyentak & P0751.' }
      ]
    },
    {
      id: 'gv_mod_abs',
      category: 'modules',
      badge: 'F-2 · ABS/EBD (23 DTC)',
      title: 'Sistem Rem ABS / EBD (Modul E03 — 26-Pin)',
      subtitle: 'Sekring 50A/30A/10A, 4× Wheel Speed Sensor, CAN Bus & Motor Pompa ABS',
      dtcs: ['C1021', 'C1022', 'C1025', 'C1031', 'C1035', 'C1041', 'C1057', 'C1061', 'C1071', 'U1073', 'U1100'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_f2_abs_p1_9a86.webp', label: 'F-2 ABS Lembar 1 — Power & CAN (9A-86)', source: 'Vol 2 Bab 9A-86 (F-2 Diagram Sirkuit ABS · S5JB0A910E029)' },
        { img: 'img/jb420_wiring/v2_f2_abs_p2_9a87.webp', label: 'F-2 ABS Lembar 2 — 4× Sensor Roda (9A-87)', source: 'Vol 2 Bab 9A-87 (F-2 Lembar 2/2 — 4 Wheel Speed Sensor ABS)' },
        { img: 'img/jb420_wiring/v1_abs_4e4.webp', label: 'Diagram Sirkuit ABS (Vol 1 · 4E-4)', source: 'Vol 1 Bab 4E-4 (Diagram Sirkuit ABS · S5JB0A4502002)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: '3 Jalur Sekring ABS (50A, 30A, 10A)', from: 'Sekring 50A ABS1, 30A ABS2 & 10A ABS', via: 'WHT/BLU, WHT/RED & GRN/ORN', to: 'ABS E03-1, E03-14 & E03-7', wire: 'WHT/BLU', desc: 'Motor pompa, solenoid katup, dan logika komputer ABS masing-masing dilindungi sekring terpisah.' },
        { step: 2, tag: 'INPUT', title: '4× Wheel Speed Sensor & Saluran CAN', from: '4 Sensor Roda (FR, FL, RR, RL) & CAN', via: 'Konektor E03 (Pin 8/10 & 12/6 CAN)', to: 'ABS Control Module E03', wire: 'RED', desc: 'Membaca kecepatan putaran keempat roda untuk mencegah roda terkunci saat rem mendadak.' },
        { step: 3, tag: 'GROUND', title: '2 Jalur Massa Utama ABS', from: 'ABS E03-13 & E03-26', via: '2 Kabel BLK Tebal', to: 'Titik Ground #10', wire: 'BLK', desc: 'Jalur balik arus besar motor pompa hidrolik ABS.' }
      ],
      wires: [
        { colorCode: 'WHT/BLU', from: 'Sekring #21 (50A ABS1)', to: 'ABS E03 Pin 1', dir: 'power', role: 'Daya utama motor pompa ABS (C1061)', func: 'Menyuplai arus besar ke motor pompa hidrolik ABS.', keyState: 'Selalu Ada (+B)', probe: 'Merah (+) E03-1 · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika 0V → periksa sekring #21 (50A) pada Kotak Sikring No.2.' },
        { colorCode: 'WHT/RED', from: 'Sekring #20 (30A ABS2)', to: 'ABS E03 Pin 14', dir: 'power', role: 'Daya solenoid katup ABS (C1063)', func: 'Menyuplai daya untuk 8 katup inlet/outlet hidrolik ABS.', keyState: 'Selalu Ada (+B)', probe: 'Merah (+) E03-14 · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Putus sekring 30A memicu C1057 / C1063.' },
        { colorCode: 'GRN/ORN', from: 'Sekring #30 (10A ABS · E82-24)', to: 'ABS E03 Pin 7', dir: 'power', role: 'Suplai IG ON logika modul ABS', func: 'Menghidupkan mikroprosesor ABS saat kunci kontak ON.', keyState: 'IG ON', probe: 'Merah (+) E03-7 · Hitam (−) Massa', spec: '10 – 14 V DC', faultHint: 'Jika 0V → lampu ABS menyala terus & scanner gagal masuk modul ABS.' },
        { colorCode: 'BLK', from: 'ABS E03 Pin 13 & Pin 26', to: 'Titik Ground #10', dir: 'ground', role: 'Ground daya pompa & logika ABS', func: 'Menjaga arus kerja pompa ABS stabil.', keyState: 'IG OFF (Mode Ohm)', probe: 'E03-13 & E03-26 ↔ Ground #10', spec: '< 1 Ω', faultHint: 'Cek juga tahanan 4 sensor roda di Lembar 2 (9A-87) bila muncul C1021–C1036.' }
      ]
    },
    {
      id: 'gv_mod_srs',
      category: 'modules',
      badge: '⛔ F-1 · SRS AIR BAG (24 DTC)',
      title: 'Sistem SRS Air Bag (Modul SDM — G47 23-Pin)',
      subtitle: 'WAJIB PATUHI PROSEDUR KESELAMATAN! Konektor Kuning · Inflator & Pretensioner',
      dtcs: ['B1013', 'B1016', 'B1021', 'B1031', 'B1032', 'B1033', 'B1034', 'B1051'],
      isNonWiring: false,
      safetyGuard: 'srs',
      photos: [
        { img: 'img/jb420_wiring/v2_f1_srs_9a85.webp', label: 'F-1 Diagram SRS Air Bag (9A-85)', source: 'Vol 2 Bab 9A-85 (F-1 Diagram Sirkuit Sistim Air-Bag · S5JB0A910E028)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Power IG Sekring AIR BAG & Ground SDM', from: 'Sekring AIR BAG → G47-16', via: 'Kabel BLK/WHT & Ground G47-20', to: 'Modul SDM Air Bag (G47)', wire: 'BLK/WHT', desc: 'SDM selalu melakukan self-check 6 detik saat kunci kontak ON (lampu AIR BAG berkedip lalu padam).' },
        { step: 2, tag: 'OUTPUT', title: 'Sirkuit Inflator Pengemudi (Clock Spring) & Penumpang', from: 'SDM G47-05/06 & Penumpang', via: 'Harness Kuning (Q) & Contact Coil', to: 'Inflator Setir & Dashboard + Pretensioner', wire: 'YEL', desc: 'Jalur kuning khusus — B1031/B1032 paling sering disebabkan pita Contact Coil (Clock Spring) setir putus.' },
        { step: 3, tag: 'OUTPUT', title: 'Sinyal Status Air Bag ke BCM & Meter', from: 'SDM G47-22 (YEL)', via: 'ADS Signal', to: 'BCM G30-19 & Indikator SRS', wire: 'YEL/GRN', desc: 'Menyalakan lampu peringatan AIR BAG bila ada sirkuit terbuka/short atau pasca benturan.' }
      ],
      wires: [
        { colorCode: 'BLK/WHT', from: 'Sekring AIR BAG', to: 'SDM Pin G47-16', dir: 'power', role: 'Suplai daya IG ON modul SDM', func: 'Menyuplai daya kerja komputer SRS Air Bag.', keyState: 'IG ON', probe: 'Merah (+) G47-16 · Hitam (−) Massa', spec: '10 – 14 V DC (≥ 8 V)', faultHint: 'Pastikan kabel aki dilepas ≥ 90 detik sebelum mencabut soket kuning!' },
        { colorCode: 'BLK', from: 'SDM Pin G47-20', to: 'Massa Bodi', dir: 'ground', role: 'Ground utama modul SDM', func: 'Referensi 0V rangkaian SRS.', keyState: 'IG OFF (Aki Lepas 90 dtk)', probe: 'G47-20 ↔ Massa Bodi', spec: '< 1 Ω', faultHint: 'Baut pengikat modul SDM ke lantai juga harus kencang sempurna.' },
        { colorCode: 'YEL', from: 'SDM G47-06 / G47-05 (YEL/GRN)', to: 'Contact Coil → Inflator Pengemudi', dir: 'out', role: 'Sirkuit pemicu Air Bag (DILARANG UKUR OHM!)', func: 'Menyalakan inflator saat tabrakan depan keras terdeteksi sensor benturan.', keyState: '⛔ HANYA BACA LEWAT SCAN TOOL!', probe: 'JANGAN colok probe Ohmmeter ke inflator!', spec: 'Baca nilai resistansi loop di Live Data Scanner (~2,0–2,6 Ω)', faultHint: 'Jika B1031 muncul bersamaan dengan klakson/tombol setir mati → ganti Contact Coil (Clock Spring).' }
      ]
    },
    {
      id: 'gv_mod_hvac',
      category: 'modules',
      badge: 'E-2 · AUTO A/C (20 DTC)',
      title: 'Sistem Auto A/C / HVAC (Modul G52 — 32-Pin)',
      subtitle: 'Sensor Suhu Kabin (B1502), Evaporator (B1503), Sunload (B1504), Mix & Blower',
      dtcs: ['B1502', 'B1503', 'B1504', 'B1511', 'B1512', 'B1513'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_e2_hvac_p1_9a83.webp', label: 'E-2 Auto A/C Lembar 1 (9A-83)', source: 'Vol 2 Bab 9A-83 (E-2 Diagram Sirkuit Sistim A/C Otomatis · S5JB0A910E047)' },
        { img: 'img/jb420_wiring/v2_e2_hvac_p2_9a84.webp', label: 'E-2 Auto A/C Lembar 2 (9A-84)', source: 'Vol 2 Bab 9A-84 (E-2 Lembar 2/2 — Actuator, Blower & Sensor HVAC)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Power Modul HVAC & Blower Relay', from: 'Sekring A/C & Blower 40A', via: 'Harness B (A/C) & G (Dashboard)', to: 'HVAC Control Module G52 & Blower Motor', wire: 'BLU/WHT', desc: 'Menyuplai daya panel kontrol otomatis dan motor blower kabin.' },
        { step: 2, tag: 'INPUT', title: '3 Sensor Utama Auto A/C', from: 'Inside Temp (B1502), Evap Temp (B1503), Sunload (B1504)', via: 'Konektor G52 (32-Pin)', to: 'Perhitungan Otomatis Suhu Kabin', wire: 'GRN/BLK', desc: 'HVAC membandingkan suhu kabin, suhu evaporator, dan intensitas matahari.' },
        { step: 3, tag: 'OUTPUT', title: 'Actuator Air-Mix, Mode & Sinyal A/C ke ECM', from: 'HVAC G52', via: 'Motor Servo & Sinyal Permintaan A/C', to: 'Damper Udara & ECM (Kompresor)', wire: 'YEL/RED', desc: 'Mengatur posisi damper panas/dingin dan mengirim permintaan hidupkan kompresor ke ECM.' }
      ],
      wires: [
        { colorCode: 'BLU/WHT', from: 'Sekring A/C & Blower 40A', to: 'HVAC Modul G52 & Blower Relay', dir: 'power', role: 'Suplai daya panel Auto A/C & motor blower', func: 'Memberi arus kerja kontrol panel AC dan hembusan blower kabin.', keyState: 'IG ON', probe: 'Pin Power G52 ↔ Massa Bodi', spec: '10 – 14 V DC', faultHint: 'Jika panel AC mati total → cek sekring A/C & Heater Blower 40A.' },
        { colorCode: 'GRN/BLK', from: 'Inside Air & Evap Temp Sensor', to: 'HVAC Konektor G52', dir: 'in', role: 'Sinyal thermistor suhu kabin (B1502) & evaporator (B1503)', func: 'Mencegah evaporator membeku dan menjaga suhu kabin sesuai setelan tombol Auto.', keyState: 'IG OFF (Ohm) / IG ON (Volt)', probe: 'Ukur tahanan sensor di soket lepas', spec: '~1,5–2,5 kΩ @25°C (NTC: makin dingin tahanan makin besar)', faultHint: 'Sensor suhu kabin (B1502) di balik kisi kecil dashboard sering tertutup gumpalan debu!' },
        { colorCode: 'YEL/RED', from: 'HVAC G52', to: 'ECM (Permintaan Kompresor A/C)', dir: 'out', role: 'Sinyal permintaan aktivasi magnet clutch A/C', func: 'Meminta ECM menaikkan idle dan menyalakan relay kompresor + kipas kondensor.', keyState: 'Mesin Hidup · A/C ON', probe: 'Ukur jalur A/C Request ke ECM', spec: 'Berubah status saat tombol A/C ditekan ON/OFF', faultHint: 'Jika kompresor tak nyala padahal tombol A/C hidup → cek juga Sensor Tekanan Freon (P0532).' }
      ]
    },
    {
      id: 'gv_mod_bcm',
      category: 'modules',
      badge: 'A-8 · BCM (9 DTC)',
      title: 'Body Control Module (BCM — G30, G31 & G32)',
      subtitle: 'Pusat Kelistrikan Bodi, Door Lock, Interior, Peringatan & Gerbang CAN Bus',
      dtcs: ['B1133', 'B1141', 'B1150', 'P1678'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a8_bcm_p1_9a51.webp', label: 'A-8 BCM Lembar 1 (9A-51)', source: 'Vol 2 Bab 9A-51 (A-8 Diagram Sirkuit Sistim Kontrol Bodi · S5JB0A910E008)' },
        { img: 'img/jb420_wiring/v2_a8_bcm_p2_9a52.webp', label: 'A-8 BCM Lembar 2 (9A-52)', source: 'Vol 2 Bab 9A-52 (A-8 Lembar 2/5 — Koneksi BCM G30/G31/G32)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +B & IG Junction Block ke BCM', from: 'Junction Block (Box Sikring No.3)', via: 'Konektor G30, G31, G32', to: 'BCM (59 Pinout Terdata)', wire: 'WHT/RED', desc: 'BCM menyatu erat dengan sistem kelistrikan kabin di bawah dashboard.' },
        { step: 2, tag: 'INPUT', title: 'Switch Pintu, Kunci & Jaringan CAN', from: 'Door Switch, Keyless & CAN Bus', via: 'J/C G74/G75 (RED & WHT)', to: 'Logika BCM', wire: 'RED', desc: 'BCM juga menjadi ujung resistor terminasi CAN Bus (120 Ω) berpasangan dengan ECM.' },
        { step: 3, tag: 'OUTPUT', title: 'Kontrol Door Lock, Lampu Kabin & Alarm', from: 'Driver Output BCM', via: 'Harness Pintu (J) & Kabin', to: 'Actuator Pintu, Dome & Buzzer', wire: 'BLU/BLK', desc: 'Mengatur kenyamanan otomatis dan keamanan pintu.' }
      ],
      wires: [
        { colorCode: 'WHT/RED', from: 'Junction Block (Box No.3)', to: 'BCM Konektor G30 / G31 (+B & IG)', dir: 'power', role: 'Suplai daya utama & IG ON BCM', func: 'Menghidupkan mikroprosesor BCM yang mengatur kunci pintu, lampu kabin, dan alarm.', keyState: 'Selalu Ada (+B) & IG ON', probe: 'Pin Power G30/G31 ↔ Massa', spec: '10 – 14 V DC', faultHint: 'Periksa soket J/B di bawah dashboard jika banyak fitur bodi mati serentak.' },
        { colorCode: 'RED', from: 'BCM CAN-H / CAN-L (WHT)', to: 'J/C G74/G75 → ECM & ABS', dir: 'in', role: 'Komunikasi CAN Bus BCM (P1678)', func: 'Sinkronisasi status kunci, immobilizer, dan lampu peringatan.', keyState: 'IG OFF (Aki Lepas)', probe: 'Ukur DLC Pin 6 ↔ 14', spec: '54 – 66 Ω (Terminasi 120 Ω di dalam BCM)', faultHint: 'Jika modul BCM terendam air / korsleting, jaringan CAN seluruh mobil bisa lumpuh.' },
        { colorCode: 'BLK', from: 'BCM Ground (G30/G31)', to: 'Titik Ground Dashboard', dir: 'ground', role: 'Ground logika & driver BCM', func: 'Referensi 0V rangkaian kontrol bodi.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin Ground BCM ↔ Massa Sasis', spec: '< 1 Ω', faultHint: 'Pastikan baut ground pilar A kiri/kanan bebas karat.' }
      ]
    },
    {
      id: 'gv_mod_icm',
      category: 'modules',
      badge: 'A-7 · IMMOBILIZER (10 DTC)',
      title: 'Sistem Immobilizer (Modul ICM — G24 6-Pin)',
      subtitle: 'Antena Transponder Kunci → ICM G24 ↔ ECM (P1614, P1615, P1616, P1618)',
      dtcs: ['P1614', 'P1615', 'P1616', 'P1618', 'P1636'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_a7_icm_9a50.webp', label: 'A-7 Diagram Immobilizer (9A-50)', source: 'Vol 2 Bab 9A-50 (A-7 Diagram Sirkuit Sistim Immobilizer · S5JB0A910E007)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Suplai +B, IG ON & Ground ICM G24', from: 'Box Sekring J/B', via: 'Konektor G24 (6-Pin)', to: 'Immobilizer Control Module', wire: 'BLK/WHT', desc: 'ICM membaca chip transponder di anak kunci saat kunci dimasukkan dan diputar ke ON.' },
        { step: 2, tag: 'INPUT', title: 'Verifikasi Kode Transponder Kunci', from: 'Coil Antena Rumah Kunci', via: 'ICM G24', to: 'Validasi ID Kunci Terdaftar', wire: 'GRN/WHT', desc: 'Bila chip kunci tidak terbaca atau bukan kunci asli → lampu gembok berkedip & P1614.' },
        { step: 3, tag: 'OUTPUT', title: 'Otorisasi Komunikasi ICM ↔ ECM', from: 'ICM G24 (Jalur Serial / CAN)', via: 'Harness Dashboard', to: 'ECM (Izin Hidupkan Injektor & Koil)', wire: 'LT GRN', desc: 'Tanpa izin sah dari ICM, ECM akan memutus semprotan bahan bakar sehingga mesin gagal hidup.' }
      ],
      wires: [
        { colorCode: 'BLK/WHT', from: 'Sekring IG', to: 'ICM Pin G24 Power', dir: 'power', role: 'Suplai daya modul Immobilizer', func: 'Menghidupkan modul pembaca transponder saat IG ON.', keyState: 'IG ON', probe: 'Pin Power G24 ↔ Massa', spec: '10 – 14 V DC', faultHint: 'Uji selalu dengan anak kunci cadangan dulu untuk membedakan rusak chip kunci vs rusak modul ICM.' },
        { colorCode: 'LT GRN', from: 'ICM Konektor G24 (Serial/Data)', to: 'ECM Pin Komunikasi Immobilizer', dir: 'out', role: 'Sinyal otorisasi start mesin (P1614/P1618)', func: 'Mengirim kode verifikasi sah ke ECM agar injektor & pengapian diizinkan aktif.', keyState: 'IG ON (Saat Kunci Dimasukkan)', probe: 'Cek kontinuitas kabel G24 ↔ ECM (IG OFF)', spec: '< 1 Ω (Tidak boleh putus / short ke ground)', faultHint: 'Jika mengganti ECM atau ICM copotan, wajib registrasi ulang kode kunci dengan scan tool.' },
        { colorCode: 'BLK', from: 'ICM Pin G24 Ground', to: 'Massa Dashboard', dir: 'ground', role: 'Ground modul pembaca kunci', func: 'Referensi 0V agar pembacaan sinyal RF antena kunci stabil.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin GND G24 ↔ Massa Bodi', spec: '< 1 Ω', faultHint: 'Gantungan kunci logam tebal/alarm aftermarket di sekitar lubang kunci bisa mengganggu sinyal antena.' }
      ]
    },
    {
      id: 'gv_mod_kscm',
      category: 'modules',
      badge: 'B-9 · SMART KEY (10 DTC)',
      title: 'Sistem Keyless Start / Smart Key (KSCM — G44 40-Pin)',
      subtitle: 'Antena Remote, Steering Lock Unit, Request Switch & Otorisasi Start (KLS-11..21)',
      dtcs: ['KLS-11', 'KLS-13', 'KLS-14', 'KLS-21'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_b9_kscm_9a66.webp', label: 'B-9 Diagram Smart Key / KSCM (9A-66)', source: 'Vol 2 Bab 9A-66 (B-9 Diagram Sirkuit Sistim Smart Key · S5JB0A910E036)' }
      ],
      stages: [
        { step: 1, tag: 'INPUT', title: 'Deteksi Remote Smart Key di Dalam Kabin', from: 'Antena Interior & Request Switch', via: 'Konektor G44 (40-Pin)', to: 'Keyless Start Control Module (KSCM)', wire: 'PNK/BLU', desc: 'Memverifikasi remote resmi ada di dalam kabin saat tombol/knob starter ditekan.' },
        { step: 2, tag: 'OUTPUT', title: 'Pembukaan Kunci Setir (Steering Lock Unit)', from: 'KSCM G44', via: 'Jalur Komunikasi Steering Lock', to: 'Electric Steering Lock (KLS-11/13)', wire: 'YEL/BLK', desc: 'Jika motor steering lock macet/gagal komunikasi → knob starter tidak bisa diputar (KLS-11).' },
        { step: 3, tag: 'OUTPUT', title: 'Otorisasi Starter ke ECM & ICM', from: 'KSCM G44', via: 'CAN / Serial Immobilizer', to: 'ECM & Starter Relay', wire: 'LT GRN', desc: 'Mengizinkan mesin distarter setelah remote & steering lock terverifikasi.' }
      ],
      wires: [
        { colorCode: 'PNK/BLU', from: 'Antena Kabin & Request Switch', to: 'KSCM Konektor G44 (40-Pin)', dir: 'in', role: 'Sinyal deteksi remote Smart Key', func: 'Mengonfirmasi keberadaan remote resmi di dalam kabin saat tombol/knob ditekan.', keyState: 'Tekan Knob / Remote di Kabin', probe: 'Ukur baterai remote CR2032 & suplai +B G44', spec: 'Baterai Remote ≥ 2,9 V · Suplai KSCM 10–14 V', faultHint: 'Indikator kunci merah di meter menandakan baterai remote lemah atau interferensi RF.' },
        { colorCode: 'YEL/BLK', from: 'KSCM G44', to: 'Electric Steering Lock Unit', dir: 'out', role: 'Komunikasi & rilis kunci setir (KLS-11/13)', func: 'Melepas kunci mekanis batang setir sebelum knob kunci kontak diputar.', keyState: 'IG ON / Tekan Knob', probe: 'Cek kontinuitas jalur G44 ↔ Steering Lock (IG OFF)', spec: '< 1 Ω (Tegangan suplai motor lock 10–14 V)', faultHint: 'Goyangkan setir sedikit saat memutar knob jika kunci setir terjepit beban roda miring.' },
        { colorCode: 'BLK', from: 'KSCM G44 Ground', to: 'Massa Dashboard', dir: 'ground', role: 'Ground utama modul Keyless Start', func: 'Referensi 0V rangkaian penerima sinyal Smart Key.', keyState: 'IG OFF (Mode Ohm)', probe: 'Pin GND G44 ↔ Massa Bodi', spec: '< 1 Ω', faultHint: 'Jika KSCM mati total, mobil tetap bisa dinyalakan darurat memakai anak kunci mekanis di dalam remote.' }
      ]
    },

    // =========================================================================
    // KATEGORI 4: PETA DASAR KELISTRIKAN JB420 (WARNA, SEKRING, GROUND, KONEKTOR)
    // =========================================================================
    {
      id: 'gv_base_colors',
      category: 'base',
      badge: '9A-2 · KODE WARNA & SIMBOL',
      title: 'Kode Warna Kabel, Singkatan & Simbol Kelistrikan Suzuki',
      subtitle: 'Panduan Resmi Membaca Kode Warna 2-Warna (BLK/WHT, BRN/BLK) & Simbol OEM',
      dtcs: ['9A-2', '9A-3', 'WARNA'],
      isNonWiring: false,
      safetyGuard: 'none',
      photos: [
        { img: 'img/jb420_wiring/v2_base_colors_9a2.webp', label: '9A-2 Singkatan & Warna Kabel', source: 'Vol 2 Bab 9A-2 (Singkatan-Singkatan & Simbol Warna Kabel · S5JB0A9101002)' },
        { img: 'img/jb420_wiring/v2_base_symbols_9a3.webp', label: '9A-3 Simbol & Tanda Listrik', source: 'Vol 2 Bab 9A-3 (Simbol dan Tanda Kelistrikan · S5JB0A9101004)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Aturan Baca 2 Warna: [WARNA DASAR / GARIS STRIP]', from: 'Huruf Pertama = Warna Isolasi Utama', via: 'Garis Miring (/)', to: 'Huruf Kedua = Warna Garis Strip Tipis', wire: 'BLK/WHT', desc: 'Contoh: BLK/WHT berarti kabel berwarna HITAM dengan garis strip PUTIH; BRN/BLK = Cokelat bergaris Hitam.' },
        { step: 2, tag: 'INPUT', title: 'Kode Huruf Harness Lokasi JB420', from: 'A=Aki · B=A/C · C=Mesin · D=Injektor', via: 'E=Main · G=Dashboard', to: 'J=Pintu · L=Lantai · Q=Air Bag', wire: 'BLU', desc: 'Kode awal konektor langsung menunjukkan lokasi fisiknya! Misal C37 = Harness Mesin, E23 = Main Harness, G47 = Dashboard.' },
        { step: 3, tag: 'GROUND', title: 'Membaca Simbol Komponen & Sambungan', from: 'Titik Bulat Hitam = Tersambung (Splice)', via: 'Garis Melompat = Tidak Terhubung', to: 'Segitiga/Garis Bertingkat = Ground', wire: 'BLK', desc: 'Buka tab "Foto Asli OEM" untuk melihat tabel simbol lengkap resmi Suzuki (Hal. 9A-2 & 9A-3).' }
      ],
      wires: [
        { colorCode: 'BLK/WHT', from: 'Hitam / Garis Putih', to: 'Umumnya Jalur +12V IG ON / Koil', dir: 'power', role: 'Contoh kode 2-warna Suzuki', func: 'Isolasi dominan Hitam (BLK) dengan garis memanjang Putih (WHT).', keyState: 'Referensi 9A-2', probe: 'Cocokkan warna di soket fisik', spec: 'Standar Warna OEM Suzuki', faultHint: 'Jangan tertukar dengan WHT/BLK (Putih bergaris Hitam — kebalikannya!).' },
        { colorCode: 'BLU/BLK', from: 'Biru / Garis Hitam', to: 'Umumnya Output +12V Main Relay EFI', dir: 'power', role: 'Jalur suplai bersama sensor & aktuator mesin', func: 'Warna dasar Biru (BLU) bergaris Hitam (BLK).', keyState: 'Referensi 9A-2', probe: 'Terukur 10–14 V saat IG ON', spec: 'Main Relay Output', faultHint: 'Warna LT GRN = Hijau Muda · PPL = Ungu · GRY = Abu-abu · ORN = Oranye.' }
      ]
    },
    {
      id: 'gv_base_fuse',
      category: 'base',
      badge: '9A-25..30 · BOX SEKRING',
      title: 'Peta Box Sikring No.1, No.2 (Relay), No.3 (J/B) & Power Supply',
      subtitle: 'Lokasi & Nilai Ampere Seluruh Sekring Ruang Mesin & Kabin (FI, IG COIL, ABS, FAN)',
      dtcs: ['9A-25', '9A-28', '9A-29', '9A-30', 'SEKRING'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_base_power_9a25.webp', label: '9A-25 Diagram Power Supply', source: 'Vol 2 Bab 9A-25 (Diagram Power Supply Utama)' },
        { img: 'img/jb420_wiring/v2_base_fuse1_9a28.webp', label: '9A-28 Box Sikring No.1', source: 'Vol 2 Bab 9A-28 (Box Sikring No.1 — Dekat Aki)' },
        { img: 'img/jb420_wiring/v2_base_fuse2_9a29.webp', label: '9A-29 Box Sikring No.2 & Relay', source: 'Vol 2 Bab 9A-29 (Box Sikring No.2 & Kotak Relay Ruang Mesin)' },
        { img: 'img/jb420_wiring/v2_base_fuse3_9a30.webp', label: '9A-30 Box Sikring No.3 (J/B Kabin)', source: 'Vol 2 Bab 9A-30 (Box Sikring No.3 Dalam Junction Block)' }
      ],
      stages: [
        { step: 1, tag: 'POWER', title: 'Box Sikring No.1 (Terminal Positif Aki)', from: 'Aki +12V', via: 'Main Fuse 100A / 80A / 60A', to: 'Distribusi ke Box No.2 & Box No.3', wire: 'WHT/RED', desc: 'Cek pertama bila mobil mati total tanpa lampu dashboard sama sekali.' },
        { step: 2, tag: 'POWER', title: 'Box Sikring No.2 & Kotak Relay (Ruang Mesin)', from: 'Ruang Mesin Sisi Aki', via: 'Sekring FI, ST, RAD FAN 30A, ABS 50A/30A', to: 'Main Relay, Fuel Pump Relay, Fan Relay #1–#3', wire: 'BLK/RED', desc: 'Pusat sekring & relay sistem injeksi mesin, starter, kipas radiator, dan ABS.' },
        { step: 3, tag: 'POWER', title: 'Box Sikring No.3 — Junction Block (Bawah Dashboard)', from: 'Kabin Pengemudi', via: 'Sekring #39 (20A IG COIL), #30 (10A ABS), AIR BAG, METER', to: 'Koil, Modul Kabin & Instrument', wire: 'BLK/WHT', desc: 'Sekring #39 (20A IG COIL) terletak di J/B kabin, bukan di ruang mesin!' }
      ],
      wires: [
        { colorCode: 'WHT/RED', from: 'Box No.1 (Terminal Aki) — 100A/80A', to: 'Main Fuse & Distribusi Box No.2/No.3', dir: 'power', role: 'Sekring induk (Main Fuse) seluruh kendaraan', func: 'Melindungi jalur utama dari aki ke alternator, kotak relay mesin, dan J/B kabin.', keyState: 'Selalu Ada (+B)', probe: 'Ukur input & output Main Fuse ↔ Massa', spec: '12,0 – 12,8 V (Mesin Mati) · 13,8–14,6 V (Hidup)', faultHint: 'Jika putus (umumnya akibat salah pasang kutub aki/jumper terbalik) → seluruh mobil mati total.' },
        { colorCode: 'BLK/RED', from: 'Box No.2 (Ruang Mesin) — FI / RAD FAN / ABS', to: 'Main Relay, Kipas 30A & ABS 50A/30A', dir: 'power', role: 'Sekring utama injeksi mesin, kipas & ABS', func: 'Melindungi jalur kerja ECM, pompa bensin, motor kipas radiator, dan modul ABS.', keyState: 'Selalu Ada (+B) / IG ON', probe: 'Uji kedua kaki tes di punggung sekring', spec: '10–14 V pada KEDUA sisi kaki sekring', faultHint: 'Buka tab "Foto Asli OEM" → 9A-29 untuk melihat posisi pasti tiap relay & sekring ruang mesin.' },
        { colorCode: 'BLK/WHT', from: 'Box No.3 (J/B Kabin) Sekring #39 & #30', to: '20A IG COIL (#39) & 10A ABS (#30)', dir: 'power', role: 'Sekring koil pengapian COP & logika ABS', func: 'Memutus suplai 4 koil sekaligus jika ada korsleting koil/noise filter.', keyState: 'IG ON', probe: 'Uji kedua kaki tes di punggung sekring', spec: '10–14 V pada KEDUA sisi kaki sekring', faultHint: 'Sekring #39 (20A IG COIL) ada di bawah dashboard (J/B No.3), bukan di ruang mesin!' }
      ]
    },
    {
      id: 'gv_base_ground',
      category: 'base',
      badge: '9A-24 · TITIK GROUND',
      title: 'Peta Lokasi Titik Ground (Massa) Bodi & Blok Mesin',
      subtitle: 'Lokasi Fisik Baut Ground #1 s/d #12 (Ground #5 Pengapian, #10 ABS, Ground ECM)',
      dtcs: ['9A-24', 'GROUND', 'MASSA'],
      isNonWiring: false,
      safetyGuard: 'ohm',
      photos: [
        { img: 'img/jb420_wiring/v2_base_ground_9a24.webp', label: '9A-24 Peta Titik Ground Lengkap', source: 'Vol 2 Bab 9A-24 (Peta Lokasi Titik Ground / Massa JB420)' }
      ],
      stages: [
        { step: 1, tag: 'GROUND', title: 'Ground Ruang Mesin & Blok Silinder (#1–#5)', from: 'Terminal (−) Aki → Bodi & Blok Mesin', via: 'Titik Ground #5 (Koil & ECM)', to: 'Sistem Pengapian & Sensor Mesin', wire: 'BLK/ORN', desc: 'Baut massa ruang mesin yang berkarat/kendor pasca turun mesin sering memicu misfire & DTC palsu.' },
        { step: 2, tag: 'GROUND', title: 'Ground Sasis Depan (#10 — ABS)', from: 'Modul ABS E03-13 & E03-26', via: 'Kabel BLK Tebal', to: 'Titik Ground #10', wire: 'BLK', desc: 'Harus bersih dari cat/karat agar motor pompa ABS menarik arus penuh tanpa voltage drop.' },
        { step: 3, tag: 'GROUND', title: 'Ground Kabin & Belakang', from: 'Dashboard (BCM/SDM/HVAC) & Tangki BBM', via: 'Baut Massa Pilar & Lantai', to: 'Sasis Bodi', wire: 'BLK', desc: 'Uji tegangan jatuh (Voltage Drop) saat beban aktif wajib < 0,2 V.' }
      ],
      wires: [
        { colorCode: 'BLK/ORN', from: 'Titik Ground #5 (Blok Mesin / Kepala Silinder)', to: 'Koil Pengapian C40–C43, Noise Filter & ECM', dir: 'ground', role: 'Massa utama sistem pengapian & ECM', func: 'Menjadi jalur balik arus primer koil dan referensi ground daya ECM.', keyState: 'IG OFF (Ohm) / IG ON (Volt Drop)', probe: 'Baut Ground #5 ↔ Aki (−)', spec: 'Tahanan < 1 Ω · Voltage Drop < 0,2 V', faultHint: 'Baut Ground #5 lupa dikencangkan pasca servis mesin langsung memicu misfire P0300!' },
        { colorCode: 'BLK', from: 'Titik Ground #10 (Sasis Depan) & Kabin', to: 'Modul ABS E03-13/26, BCM, SDM & Tangki', dir: 'ground', role: 'Massa daya pompa ABS & modul kabin', func: 'Menutup jalur arus besar motor pompa ABS dan modul elektronik bodi.', keyState: 'IG OFF (Ohm) / Beban ON (Volt Drop)', probe: 'Baut Ground #10 ↔ Aki (−)', spec: 'Tahanan < 1 Ω · Voltage Drop < 0,2 V saat beban ON', faultHint: 'Bersihkan permukaan baut dan lug kabel dari cat/karat dengan amplas halus + contact cleaner.' }
      ]
    },
    {
      id: 'gv_base_connectors',
      category: 'base',
      badge: '9A-13 & 9A-91 · KONEKTOR',
      title: 'Layout Konektor Ruang Mesin & Bentuk Fisik Soket (C & E)',
      subtitle: 'Peta Posisi Konektor Ruang Mesin (9A-13) & Bentuk Pinout Soket C/E (9A-91/93)',
      dtcs: ['9A-13', '9A-91', '9A-93', 'KONEKTOR', 'SOKET'],
      isNonWiring: false,
      safetyGuard: 'none',
      photos: [
        { img: 'img/jb420_wiring/v2_base_conn_eng_9a13.webp', label: '9A-13 Layout Konektor Ruang Mesin', source: 'Vol 2 Bab 9A-13 (Diagram Layout Konektor Ruang Mesin)' },
        { img: 'img/jb420_wiring/v2_base_conn_c_9a91.webp', label: '9A-91 Bentuk Fisik Konektor C (Mesin)', source: 'Vol 2 Bab 9A-91 (Data Bentuk Konektor C — Harness Mesin)' },
        { img: 'img/jb420_wiring/v2_base_conn_e_9a93.webp', label: '9A-93 Bentuk Fisik Konektor E (Main)', source: 'Vol 2 Bab 9A-93 (Data Bentuk Konektor E — Main Harness)' }
      ],
      stages: [
        { step: 1, tag: 'INPUT', title: 'Mencari Lokasi Fisik Soket di Ruang Mesin', from: 'Kode Konektor (mis. C37, C40–43, E03)', via: 'Peta 9A-13 Ruang Mesin', to: 'Posisi Komponen di Mobil', wire: 'BLU', desc: 'Cocokkan kode soket dari diagram sirkuit ke peta tata letak ruang mesin Hal. 9A-13.' },
        { step: 2, tag: 'INPUT', title: 'Membaca Urutan Nomor Pin (Arah Penglihatan)', from: 'Sisi Terminal vs Sisi Kabel', via: 'Gambar Bentuk Soket 9A-91 / 9A-93', to: 'Pin Target yang Tepat (Anti Salah Colok!)', wire: 'YEL', desc: 'Perhatikan posisi kancing pengunci (lock tab) di bagian atas sebelum menghitung nomor pin 1, 2, 3.' },
        { step: 3, tag: 'POWER', title: 'Tips Aman Menusuk Probe Multimeter', from: 'Back-Probing dari Sisi Belakang Kabel', via: 'Jarum Back-Probe Halus', to: 'Jangan Melebarkan Terminal Depan!', wire: 'RED', desc: 'Menusuk paksa sisi depan pin betina akan melonggarkan jepitan terminal dan menciptakan penyakit baru!' }
      ],
      wires: [
        { colorCode: 'GRY', from: 'Konektor C (Harness Mesin · 9A-91)', to: 'C37 (ECM), C40–43 (Koil), CKP, CMP, MAF', dir: 'in', role: 'Panduan identifikasi pin konektor ruang mesin', func: 'Memastikan probe multimeter masuk ke nomor terminal soket C yang tepat (posisi tab pengunci di atas).', keyState: 'Panduan Fisik (9A-13 & 9A-91)', probe: 'Gunakan teknik Back-Probe dari belakang seal kabel', spec: 'Jangan melebarkan celah pin betina depan!', faultHint: 'Buka tab "Foto Asli OEM" → 9A-91 untuk melihat gambar fisik bentuk soket C.' },
        { colorCode: 'BLU', from: 'Konektor E (Main Harness · 9A-93)', to: 'E23 (ECM), E03 (ABS), E82 (J/B), E92/93 (TCM)', dir: 'in', role: 'Panduan identifikasi pin konektor Main Harness', func: 'Menentukan arah penomoran pin konektor utama yang menghubungkan ruang mesin ke kabin.', keyState: 'Panduan Fisik (9A-13 & 9A-93)', probe: 'Cocokkan nomor terminal & warna kabel sebelum mengukur', spec: 'Verifikasi fisik selalu memakai warna kabel + posisi pin', faultHint: 'Jika konektor E55/C35 (sambungan mesin-bodi) korosi/lembab, banyak sensor bisa error bersamaan.' }
      ]
    }
  ];

  window.JB420_WIRING_ATLAS = JB420_WIRING_ATLAS;
  window.jb420WirePalette = getWirePalette;
  window.jb420RenderWireSwatch = renderWireSwatchHtml;
})();
