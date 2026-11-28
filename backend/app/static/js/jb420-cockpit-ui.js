/**
 * AGOS Dark Cockpit — Unified Live Circuit & Interactive Signal Flow Engine (Suzuki Grand Vitara JB420)
 * =====================================================================================================
 * Mengelola Pilar 3 (Skripsi R&D 4D):
 * - Filter Kategori 1 (Mesin & EFI) + Kategori 2 (7 Modul Kontrol) + Kategori 4 (Peta Dasar)
 * - Sakelar 2-Mode: [⚡ Simulasi Alur Terpadu] | [📷 Foto Wiring Asli OEM]
 * - BARU (Simulasi Alur Terpadu 1 Kanvas Hidup — BUKAN Terpisah Per-Tahap!):
 *   • Seluruh rangkaian (Sumber Daya/Sensor Input -> Hub Mikrokontroler ECM/Modul -> Aktuator Output -> Umpan Balik/Ground)
 *     tampil menyatu dalam 1 papan sirkuit PCB Dark Cockpit hidup dengan partikel elektron bergerak serentak!
 *   • 3 Mode Kondisi Nyata: [🔑 IG ON (Statis)] | [🔥 Mesin Hidup (Live)] | [💥 Uji Putus Kabel (Fault Injection)]
 *   • Slider Interaktif Kontekstual (Pedal Gas/RPM, Suhu Coolant °C, Beban Listrik %, Kecepatan Roda km/jam)
 *     yang menggerakkan animasi aktuator (kupu-kupu throttle, kipas radiator, percikan koil, katup EGR),
 *     gelombang Mini-Oscilloscope hidup, dan angka Live Telemetry secara real-time!
 *   • Klik langsung kabel mana saja di diagram untuk Sorot/Inspeksi (Mode Live) atau Putus Virtual (Mode Gangguan)
 *     yang otomatis menyalakan indikator MIL Check Engine + Kode DTC pemicunya!
 * - Mode Foto Asli OEM: Multi-Halaman, Zoom +/-/100%, Fullscreen Lightbox, [☀️ Kertas Asli | 🌙 Blueprint Gelap]
 * - Penanganan Cerdas Kasus Non-Wiring (P0171 / P0420) lengkap dengan Diagram Aliran Fluida/Gas Hidup
 */

(function () {
  let activeCategory = 'efi';
  let activeModuleId = 'gv_ign_coil';
  let activeVisualMode = 'flow'; // 'flow' | 'photo'
  let activePhotoIdx = 0;
  let activeStageIdx = -1; // -1 = Semua jalur aktif serentak (Unified); >=0 = Sorot jalur terpilih
  let simRunMode = 'live'; // 'igon' | 'live' | 'fault'
  let simSliderVal = 35; // 0..100 slider kontekstual (Gas/RPM, Suhu, Beban, Kecepatan)
  let faultStageIdx = 0; // Jalur yang diputus saat mode 'fault'
  let photoTheme = 'paper'; // 'paper' | 'blueprint'
  let photoZoom = 1.0;
  let fsZoom = 1.0;
  let unifiedZoom = 1.0;

  function _esc(v) {
    return String(v == null ? '' : v)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function resolveImgUrl(relPath) {
    if (!relPath) return '';
    if (window.location.protocol === 'file:' || typeof window.offlineFetch === 'function') {
      return relPath;
    }
    return `/static/${relPath}`;
  }

  function getAtlas() {
    return Array.isArray(window.JB420_WIRING_ATLAS) ? window.JB420_WIRING_ATLAS : [];
  }

  function getActiveModule() {
    const atlas = getAtlas();
    return atlas.find(m => m.id === activeModuleId) || atlas[0] || null;
  }

  function wrapLines(txt, maxLen, maxLines = 2) {
    const words = String(txt || '').split(/\s+/);
    const lines = [];
    let cur = '';
    for (const w of words) {
      if ((cur + ' ' + w).trim().length > maxLen && cur) {
        lines.push(cur);
        cur = w;
      } else {
        cur = (cur + ' ' + w).trim();
      }
    }
    if (cur) lines.push(cur);
    return lines.slice(0, maxLines);
  }

  function renderSvgTextLines(lines, cx, startY, color, size = 11, weight = '700') {
    return lines.map((ln, idx) =>
      `<text x="${cx}" y="${startY + idx * (size + 3.5)}" text-anchor="middle" fill="${color}" font-family="system-ui,Segoe UI,sans-serif" font-size="${size}" font-weight="${weight}">${_esc(ln)}</text>`
    ).join('');
  }

  // Profil simulasi kontekstual agar setiap modul punya slider, oscilloscope, ikon aktuator & angka live realistis!
  function getModuleSimProfile(mod) {
    const id = mod.id || '';
    const v = Math.max(0, Math.min(100, Number(simSliderVal) || 0));
    const isFault = simRunMode === 'fault';
    const isIgOn = simRunMode === 'igon';
    const p = isIgOn ? 0 : (v / 100);

    if (id === 'gv_etc_app') {
      const app1 = (0.72 + p * 3.25).toFixed(2);
      const tps1 = (0.85 + p * 3.15).toFixed(2);
      const angle = Math.round(5 + p * 82);
      return {
        hubTitle: 'ECM J20A',
        hubSub: 'E23 (APP) · C37 (ETC)',
        sliderLabel: '🎚️ Injak Pedal Gas (APP)',
        sliderValueText: isIgOn ? 'IG ON · Pedal 0%' : `Pedal ${v}% · Throttle ${angle}°`,
        waveType: 'pwm',
        actuatorType: 'throttle',
        actuatorParam: angle,
        metric1: { lbl: 'APP MAIN (E23-55)', val: isFault ? '0.00 V ⚠' : `${app1} V` },
        metric2: { lbl: 'TPS MAIN (C37-54)', val: isFault ? 'LIMP 7°' : `${tps1} V` },
        metric3: { lbl: 'BUKAAN THROTTLE', val: isFault ? 'FAIL-SAFE' : `${angle}°` }
      };
    }
    if (id === 'gv_ign_coil') {
      const rpm = isIgOn ? 0 : Math.round(680 + p * 3820);
      const adv = isIgOn ? 0 : Math.round(10 + p * 26);
      return {
        hubTitle: 'ECM J20A',
        hubSub: 'C37-21/20/19/18 (COP)',
        sliderLabel: '🎚️ Putaran Mesin (RPM)',
        sliderValueText: isIgOn ? 'IG ON · 0 RPM' : `${rpm.toLocaleString('id-ID')} RPM · ${adv}° BTDC`,
        waveType: 'pulse',
        actuatorType: 'spark',
        actuatorParam: rpm,
        metric1: { lbl: 'SUPLAI +B (#39)', val: isFault && faultStageIdx === 0 ? '0.00 V ⚠' : (isIgOn ? '12.40 V' : '14.15 V') },
        metric2: { lbl: 'TRIGGER C37-18..21', val: isFault ? 'HILANG PULSA' : (isIgOn ? '0.15 V' : `5V · ${Math.round(rpm / 30)} Hz`) },
        metric3: { lbl: 'TIMING API', val: isFault ? 'MISFIRE!' : `${adv}° BTDC` }
      };
    }
    if (id === 'gv_cooling_fan' || id === 'gv_ect') {
      const temp = Math.round(28 + (v / 100) * 78); // 28°C .. 106°C
      const ectV = Math.max(0.42, (3.25 - (temp - 25) * 0.035)).toFixed(2);
      const fanState = isFault ? 'MATI ⚠' : (temp >= 102.5 ? 'HIGH (RLY 1-3)' : (temp >= 97.5 ? 'LOW (RLY #1)' : 'STANDBY OFF'));
      return {
        hubTitle: 'ECM J20A',
        hubSub: id === 'gv_ect' ? 'C37-24 / C37-57 (ECT)' : 'E23-46/47/48 (FAN)',
        sliderLabel: '🌡️ Suhu Coolant (ECT)',
        sliderValueText: `${temp} °C · Kipas: ${fanState}`,
        waveType: temp >= 97.5 ? 'low_on' : 'dc',
        actuatorType: 'fan',
        actuatorParam: isFault ? 0 : (temp >= 102.5 ? 2 : (temp >= 97.5 ? 1 : 0)),
        metric1: { lbl: 'SUHU COOLANT', val: isFault && id === 'gv_ect' ? '−40 °C ⚠' : `${temp} °C` },
        metric2: { lbl: 'SINYAL C37-24', val: isFault && id === 'gv_ect' ? '4.98 V ⚠' : `${ectV} V` },
        metric3: { lbl: 'STATUS KIPAS', val: fanState }
      };
    }
    if (id === 'gv_egr_evap_imtv') {
      const egrPct = isIgOn ? 0 : Math.round(p * 48);
      const rpm = isIgOn ? 0 : Math.round(680 + p * 2820);
      return {
        hubTitle: 'ECM J20A',
        hubSub: 'C37-03..06 (EGR) · C37-13',
        sliderLabel: '🎚️ Beban / RPM Jalan',
        sliderValueText: isIgOn ? 'IG ON · EGR 0%' : `${rpm} RPM · EGR ${egrPct}%`,
        waveType: egrPct > 5 ? 'pwm' : 'dc',
        actuatorType: 'valve',
        actuatorParam: isFault ? 0 : egrPct,
        metric1: { lbl: 'EGR OPENING', val: isFault ? 'MACET / 0%' : `${egrPct} %` },
        metric2: { lbl: 'C37-03..06 STEPPER', val: isFault ? '0.00 V ⚠' : (egrPct > 5 ? 'Pulsa 0–14V' : '13.8 V Idle') },
        metric3: { lbl: 'TAHANAN COIL', val: isFault ? 'OL (PUTUS)' : '24.5 Ω OK' }
      };
    }
    if (id === 'gv_ckp' || id === 'gv_cmp') {
      const rpm = isIgOn ? 0 : Math.round(680 + p * 3820);
      const acv = isIgOn ? '0.00 V' : `${(1.2 + p * 4.4).toFixed(1)} Vp-p`;
      return {
        hubTitle: 'ECM J20A',
        hubSub: id === 'gv_ckp' ? 'C37-51 / C37-36 (CKP)' : 'C37-52 (CMP Hall-IC)',
        sliderLabel: '🎚️ Putaran Poros (RPM)',
        sliderValueText: isIgOn ? 'IG ON · 0 RPM' : `${rpm.toLocaleString('id-ID')} RPM`,
        waveType: id === 'gv_ckp' ? 'sine' : 'pulse',
        actuatorType: 'rotor',
        actuatorParam: isFault ? 0 : rpm,
        metric1: { lbl: 'BACAAN RPM', val: isFault ? '0 RPM ⚠' : `${rpm} RPM` },
        metric2: { lbl: id === 'gv_ckp' ? 'SINUS CKP' : 'PULSA CMP', val: isFault ? 'NO SIGNAL' : (id === 'gv_ckp' ? acv : '0↔5V · 6/rev') },
        metric3: { lbl: 'SINKRONISASI', val: isFault ? 'GAGAL START' : 'SYNC OK' }
      };
    }
    if (id === 'gv_maf_iat' || id === 'gv_map') {
      const mafGs = isIgOn ? '0.0' : (2.1 + p * 14.5).toFixed(1);
      const mafV = isIgOn ? '0.78' : (1.45 + p * 2.35).toFixed(2);
      const mapKpa = isIgOn ? 100 : Math.round(29 + p * 65);
      const mapV = isIgOn ? '3.95' : (1.18 + p * 2.55).toFixed(2);
      return {
        hubTitle: 'ECM J20A',
        hubSub: id === 'gv_maf_iat' ? 'C37-26 (MAF) · C37-25 (IAT)' : 'C37-14 (+5V) · C37-55 (MAP)',
        sliderLabel: '🎚️ Bukaan Gas / Hisapan Udara',
        sliderValueText: id === 'gv_maf_iat' ? `Aliran ${mafGs} g/s (${mafV} V)` : `Tekanan ${mapKpa} kPa (${mapV} V)`,
        waveType: 'analog',
        actuatorType: 'meter',
        actuatorParam: isFault ? 0 : Math.round(p * 100),
        metric1: { lbl: id === 'gv_maf_iat' ? 'MAF FLOW' : 'MAP PRESSURE', val: isFault ? 'ERR ⚠' : (id === 'gv_maf_iat' ? `${mafGs} g/s` : `${mapKpa} kPa`) },
        metric2: { lbl: 'SINYAL VOLT', val: isFault ? '0.00 V ⚠' : (id === 'gv_maf_iat' ? `${mafV} V` : `${mapV} V`) },
        metric3: { lbl: 'FUEL TRIM', val: isFault ? '+24% LEAN' : '±2.5% OK' }
      };
    }
    if (id === 'gv_af_ho2s') {
      const afMa = isIgOn ? '0.00' : ((p - 0.45) * 0.28).toFixed(2);
      const o2V = isIgOn ? '4.50' : (0.68 - (p - 0.5) * 0.25).toFixed(2);
      return {
        hubTitle: 'ECM J20A',
        hubSub: 'C37-32/37/38 (A/F) · C37-11 (O2)',
        sliderLabel: '🎚️ Rasio Udara-BBM (AFR)',
        sliderValueText: `A/F ${afMa} mA · HO2S-2 ${o2V} V`,
        waveType: 'sine',
        actuatorType: 'meter',
        actuatorParam: isFault ? 0 : Math.round(45 + (p - 0.5) * 40),
        metric1: { lbl: 'A/F CURRENT', val: isFault ? 'OPEN ⚠' : `${afMa} mA` },
        metric2: { lbl: 'HO2S-2 (C37-11)', val: isFault ? '0.00 V ⚠' : `${o2V} V` },
        metric3: { lbl: 'CLOSED LOOP', val: isFault ? 'OPEN LOOP' : 'CLSD AKTIF' }
      };
    }
    if (id === 'gv_injector' || id === 'gv_fuel_pump') {
      const pw = isIgOn ? '0.0' : (2.4 + p * 7.8).toFixed(1);
      const bar = isFault ? '0.0' : (isIgOn ? '3.2' : '3.3');
      return {
        hubTitle: 'ECM J20A',
        hubSub: id === 'gv_injector' ? 'C37-01/02/16/17 (INJ)' : 'E23-15 (FUEL PUMP RLY)',
        sliderLabel: '🎚️ Beban Semprotan BBM',
        sliderValueText: isIgOn ? 'IG ON · Priming 2 dtk' : `Pulse ${pw} ms · Rail ${bar} bar`,
        waveType: 'pulse',
        actuatorType: 'spray',
        actuatorParam: isFault ? 0 : (isIgOn ? 10 : Math.round(25 + p * 75)),
        metric1: { lbl: 'TEKANAN RAIL', val: `${bar} bar` },
        metric2: { lbl: 'DURASI PULSA', val: isFault ? '0.0 ms ⚠' : `${pw} ms` },
        metric3: { lbl: 'POMPA BENSIN', val: isFault ? 'MATI ⚠' : 'ON AKTIF' }
      };
    }
    if (id === 'gv_charging') {
      const amp = isIgOn ? 0 : Math.round(12 + p * 32);
      const duty = isIgOn ? 0 : Math.round(18 + p * 34);
      const volt = isFault ? '11.85' : (isIgOn ? '12.45' : (14.25 - p * 0.35).toFixed(2));
      return {
        hubTitle: 'ECM & ALTERNATOR',
        hubSub: 'C37-08/28 (GEN) · C37-09 (ELD)',
        sliderLabel: '💡 Beban Kelistrikan (Lampu+AC)',
        sliderValueText: `Beban ${v}% · ${amp} A · ${volt} V`,
        waveType: 'pwm',
        actuatorType: 'meter',
        actuatorParam: isFault ? 0 : Math.round(100 - p * 20),
        metric1: { lbl: 'TEGANGAN AKI', val: `${volt} V` },
        metric2: { lbl: 'ARUS ELD (J20A)', val: isFault ? 'ERR ⚠' : `${amp} A` },
        metric3: { lbl: 'FIELD DUTY', val: isFault ? '0% ⚠' : `${duty} %` }
      };
    }
    if (id === 'gv_can_bus') {
      return {
        hubTitle: 'JARINGAN CAN BUS',
        hubSub: 'E23-04 (CAN-H) · E23-19 (CAN-L)',
        sliderLabel: '📡 Trafik Paket Data CAN',
        sliderValueText: isFault ? 'BUS OFF · 120 Ω / SHORT!' : `500 kbps · Terminasi 60.2 Ω`,
        waveType: 'can',
        actuatorType: 'can',
        actuatorParam: isFault ? 0 : Math.round(35 + p * 65),
        metric1: { lbl: 'CAN-HIGH (E23-04)', val: isFault ? '0.00 V ⚠' : '2.74 V' },
        metric2: { lbl: 'CAN-LOW (E23-19)', val: isFault ? '0.00 V ⚠' : '2.26 V' },
        metric3: { lbl: 'TAHANAN DLC 6-14', val: isFault ? '120 Ω ⚠' : '60.2 Ω OK' }
      };
    }
    if (id === 'gv_mod_abs') {
      const kmh = isIgOn ? 0 : Math.round(p * 100);
      return {
        hubTitle: 'MODUL ABS / EBD',
        hubSub: 'Konektor E03 · 4 Sensor Roda',
        sliderLabel: '🚗 Kecepatan Putaran Roda',
        sliderValueText: `${kmh} km/jam · 4 Roda Sinkron`,
        waveType: 'pulse',
        actuatorType: 'rotor',
        actuatorParam: isFault ? 0 : kmh * 35,
        metric1: { lbl: 'RODA FL/FR/RL/RR', val: isFault ? 'FR 0 km/j ⚠' : `${kmh} km/j` },
        metric2: { lbl: 'SUPLAI E03-07', val: isIgOn ? '12.4 V' : '14.1 V' },
        metric3: { lbl: 'LAMPU ABS', val: isFault ? 'MENYALA ⚠' : 'PADAM OK' }
      };
    }
    if (id === 'gv_mod_tcm') {
      const gear = isIgOn ? 'P' : (p < 0.25 ? '1' : (p < 0.5 ? '2' : (p < 0.78 ? '3' : '4 (OD)')));
      return {
        hubTitle: 'MODUL TCM A/T',
        hubSub: 'Konektor E92 · Shift Solenoid',
        sliderLabel: '⚙️ Posisi Gigi & Beban A/T',
        sliderValueText: isIgOn ? 'Tuas P · IG ON' : `Gigi ${gear} · ATF 78°C`,
        waveType: 'pwm',
        actuatorType: 'valve',
        actuatorParam: isFault ? 0 : Math.round(25 + p * 70),
        metric1: { lbl: 'POSISI GIGI', val: isFault ? 'LIMP GIGI 3' : `GIGI ${gear}` },
        metric2: { lbl: 'SHIFT SOL A/B', val: isFault ? 'OPEN ⚠' : '13.2 Ω OK' },
        metric3: { lbl: 'SUPLAI E92-06', val: isIgOn ? '12.4 V' : '14.1 V' }
      };
    }
    if (id === 'gv_mod_srs') {
      return {
        hubTitle: 'MODUL SDM AIR BAG',
        hubSub: 'Konektor Kuning G47 (SAFETY!)',
        sliderLabel: '🛡️ Mode Uji Aman Scanner SDM',
        sliderValueText: '⛔ Dilarang Ukur Ohm di Inflator!',
        waveType: 'dc',
        actuatorType: 'shield',
        actuatorParam: isFault ? 0 : 100,
        metric1: { lbl: 'SUPLAI G47-16', val: isFault ? '< 7.5 V ⚠' : '12.4 V OK' },
        metric2: { lbl: 'INFLATOR (SCANNER)', val: isFault ? 'OPEN > 6 Ω' : '2.4 Ω OK' },
        metric3: { lbl: 'LAMPU AIR BAG', val: isFault ? 'MENYALA ⚠' : 'PADAM OK' }
      };
    }
    if (id === 'gv_mod_hvac') {
      const setC = Math.round(18 + p * 12);
      return {
        hubTitle: 'MODUL AUTO A/C',
        hubSub: 'Konektor G52 (HVAC Control)',
        sliderLabel: '❄️ Setelan Suhu Kabin AC',
        sliderValueText: `Target ${setC} °C · Ref +5V G52-14`,
        waveType: 'analog',
        actuatorType: 'fan',
        actuatorParam: isFault ? 0 : (setC <= 22 ? 2 : 1),
        metric1: { lbl: 'TARGET SUHU', val: `${setC} °C` },
        metric2: { lbl: 'REF +5V (G52-14)', val: isFault ? '0.00 V ⚠' : '5.01 V' },
        metric3: { lbl: 'KOMPRESOR', val: isFault ? 'OFF ⚠' : (setC <= 26 ? 'ON DINGIN' : 'STANDBY') }
      };
    }
    const defaultHub = mod.category === 'modules'
      ? (mod.badge.split('·')[1] || 'MODUL KONTROL').trim()
      : (mod.category === 'base' ? 'DISTRIBUSI DAYA JB420' : 'ECM J20A (C37/E23)');
    return {
      hubTitle: defaultHub.slice(0, 18),
      hubSub: (mod.dtcs || []).slice(0, 3).join(' · ') || 'JB420 OEM',
      sliderLabel: '🎚️ Intensitas Sinyal Simulasi',
      sliderValueText: isIgOn ? 'IG ON (Standby)' : `Aktif ${v}% · Normal`,
      waveType: mod.category === 'base' ? 'dc' : 'pulse',
      actuatorType: 'meter',
      actuatorParam: isFault ? 0 : Math.round(25 + p * 75),
      metric1: { lbl: 'TEGANGAN KERJA', val: isFault ? '0.00 V ⚠' : (isIgOn ? '12.4 V' : '14.1 V') },
      metric2: { lbl: 'STATUS SIRKUIT', val: isFault ? 'OPEN / PUTUS' : 'KONTINYU OK' },
      metric3: { lbl: 'DIAGNOSA ECM', val: isFault ? (mod.dtcs?.[0] || 'DTC ON') : 'NORMAL OK' }
    };
  }

  function buildOscilloscopePath(waveType, sliderVal, isIgOn, isFault) {
    // Returns SVG polyline path inside x: 344..516, y: 214..262 (center y=238)
    if (isFault) {
      return {
        path: 'M 346 254 L 514 254',
        color: '#f43f5e',
        label: '0.00V FLAT (OPEN!)'
      };
    }
    if (isIgOn || waveType === 'dc') {
      return {
        path: 'M 346 226 L 514 226',
        color: '#22d3ee',
        label: isIgOn ? 'DC STANDBY (IG ON)' : 'DC STABIL 12–14V'
      };
    }
    const p = sliderVal / 100;
    if (waveType === 'sine') {
      const cycles = Math.max(2, Math.round(3 + p * 5));
      const pts = [];
      for (let i = 0; i <= 48; i++) {
        const x = 346 + (i / 48) * 168;
        const rad = (i / 48) * cycles * Math.PI * 2;
        const amp = 14 + p * 6;
        const y = 238 - Math.sin(rad) * amp;
        pts.push(`${i === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${y.toFixed(1)}`);
      }
      return { path: pts.join(' '), color: '#38bdf8', label: `SINUS AC · ${cycles}×/DIV` };
    }
    if (waveType === 'pulse' || waveType === 'pwm') {
      const pulses = Math.max(2, Math.round(3 + p * 5));
      const step = 168 / pulses;
      const duty = waveType === 'pwm' ? (0.22 + p * 0.56) : 0.28;
      let d = 'M 346 254';
      for (let i = 0; i < pulses; i++) {
        const x0 = 346 + i * step;
        const x1 = x0 + step * duty;
        const x2 = x0 + step;
        d += ` L ${x0.toFixed(1)} 220 L ${x1.toFixed(1)} 220 L ${x1.toFixed(1)} 254 L ${x2.toFixed(1)} 254`;
      }
      return {
        path: d,
        color: waveType === 'pwm' ? '#fbbf24' : '#34d399',
        label: waveType === 'pwm' ? `PWM DUTY ${Math.round(duty * 100)}%` : `PULSA DIGITAL 5V`
      };
    }
    if (waveType === 'can') {
      let d = 'M 346 238';
      const bits = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1];
      const step = 168 / bits.length;
      bits.forEach((b, i) => {
        const x0 = 346 + i * step;
        const x1 = x0 + step;
        const y = b ? 222 : 252;
        d += ` L ${x0.toFixed(1)} ${y} L ${x1.toFixed(1)} ${y}`;
      });
      return { path: d, color: '#a78bfa', label: 'CAN-H / CAN-L 500kbps' };
    }
    if (waveType === 'low_on') {
      return { path: 'M 346 222 L 385 222 L 385 254 L 514 254', color: '#34d399', label: 'ACTIVE LOW (< 1V ON)' };
    }
    // Analog variable level
    const yLvl = Math.round(254 - p * 34);
    return {
      path: `M 346 ${yLvl} Q 388 ${yLvl - 3}, 430 ${yLvl} T 514 ${yLvl}`,
      color: '#22d3ee',
      label: `ANALOG LIVE (${Math.round(p * 100)}%)`
    };
  }

  function buildActuatorMiniVisual(profile, isIgOn, isFault) {
    const cx = 790;
    const cy = 128;
    if (isFault) {
      return `<g transform="translate(${cx},${cy})">
        <circle r="18" fill="#450a0a" stroke="#f43f5e" stroke-width="2"/>
        <path d="M-7 -7 L7 7 M7 -7 L-7 7" stroke="#fda4af" stroke-width="2.5" stroke-linecap="round"/>
      </g>`;
    }
    if (profile.actuatorType === 'throttle') {
      const ang = isIgOn ? 5 : profile.actuatorParam;
      return `<g transform="translate(${cx},${cy})">
        <circle r="19" fill="#09152b" stroke="#fbbf24" stroke-width="1.8"/>
        <line x1="-14" y1="0" x2="14" y2="0" stroke="#fbbf24" stroke-width="3.5" stroke-linecap="round" transform="rotate(${-ang})"/>
        <circle r="3.5" fill="#fef3c7"/>
      </g>`;
    }
    if (profile.actuatorType === 'fan') {
      const spd = profile.actuatorParam; // 0 off, 1 low, 2 high
      const dur = spd === 2 ? '0.35s' : (spd === 1 ? '0.9s' : '');
      const anim = dur ? `<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="${dur}" repeatCount="indefinite"/>` : '';
      return `<g transform="translate(${cx},${cy})">
        <circle r="19" fill="#09152b" stroke="${spd ? '#34d399' : '#475569'}" stroke-width="1.8"/>
        <g>
          ${anim}
          <path d="M0 0 C5 -14, 14 -10, 6 -2 Z M0 0 C14 5, 10 14, 2 6 Z M0 0 C-5 14, -14 10, -6 2 Z M0 0 C-14 -5, -10 -14, -2 -6 Z" fill="${spd ? '#34d399' : '#64748b'}"/>
        </g>
        <circle r="3" fill="#e2e8f0"/>
      </g>`;
    }
    if (profile.actuatorType === 'spark') {
      const active = !isIgOn && profile.actuatorParam > 0;
      return `<g transform="translate(${cx},${cy})">
        <circle r="19" fill="#09152b" stroke="${active ? '#f59e0b' : '#475569'}" stroke-width="1.8"/>
        <polygon points="2,-12 -7,2 0,2 -3,13 8,-2 1,-2" fill="${active ? '#fde047' : '#64748b'}">
          ${active ? '<animate attributeName="opacity" values="1;0.25;1" dur="0.35s" repeatCount="indefinite"/>' : ''}
        </polygon>
      </g>`;
    }
    if (profile.actuatorType === 'rotor') {
      const active = !isIgOn && profile.actuatorParam > 0;
      const dur = active ? `${Math.max(0.35, 1.8 - (profile.actuatorParam / 4500) * 1.3).toFixed(2)}s` : '';
      return `<g transform="translate(${cx},${cy})">
        <circle r="19" fill="#09152b" stroke="#38bdf8" stroke-width="1.8"/>
        <g>
          ${dur ? `<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="${dur}" repeatCount="indefinite"/>` : ''}
          <circle r="12" fill="none" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4 3"/>
        </g>
        <circle r="4" fill="#bae6fd"/>
      </g>`;
    }
    if (profile.actuatorType === 'valve' || profile.actuatorType === 'spray') {
      const pct = Math.min(100, Math.max(0, profile.actuatorParam));
      const hBar = Math.round((pct / 100) * 24);
      return `<g transform="translate(${cx},${cy})">
        <rect x="-15" y="-17" width="30" height="34" rx="6" fill="#09152b" stroke="#fbbf24" stroke-width="1.6"/>
        <rect x="-9" y="${12 - hBar}" width="18" height="${Math.max(3, hBar)}" rx="3" fill="${profile.actuatorType === 'spray' ? '#38bdf8' : '#fbbf24'}"/>
      </g>`;
    }
    if (profile.actuatorType === 'shield') {
      return `<g transform="translate(${cx},${cy})">
        <path d="M0 -17 L15 -10 V3 C15 11, 7 16, 0 19 C-7 16, -15 11, -15 3 V-10 Z" fill="#4c0519" stroke="#fb7185" stroke-width="1.8"/>
        <text x="0" y="5" text-anchor="middle" fill="#fecdd3" font-size="11" font-weight="800">SRS</text>
      </g>`;
    }
    // Live gauge arc
    const pct = Math.min(100, Math.max(0, profile.actuatorParam));
    const dash = Math.round((pct / 100) * 85);
    return `<g transform="translate(${cx},${cy})">
      <circle r="18" fill="#09152b" stroke="#1e293b" stroke-width="3"/>
      <circle r="14" fill="none" stroke="#22d3ee" stroke-width="3" stroke-dasharray="${dash} 100" transform="rotate(-90)"/>
      <text x="0" y="4" text-anchor="middle" fill="#e0f2fe" font-family="Consolas,monospace" font-size="9.5" font-weight="700">${pct}%</text>
    </g>`;
  }

  function buildUnifiedCircuitSvg(mod) {
    const stages = mod.stages || [];
    if (!stages.length) return '';

    const profile = getModuleSimProfile(mod);
    const isIgOn = simRunMode === 'igon';
    const isFault = simRunMode === 'fault';
    const speedDur = isIgOn
      ? 3.0
      : Math.max(0.55, 1.9 - (simSliderVal / 100) * 1.25);

    const tagMeta = {
      POWER: { glow: '#ef4444', stroke: '#f87171', badgeBg: '#450a0a', text: '#fecaca', short: 'POWER +B' },
      INPUT: { glow: '#06b6d4', stroke: '#22d3ee', badgeBg: '#083344', text: '#cffafe', short: 'INPUT' },
      OUTPUT: { glow: '#f59e0b', stroke: '#fbbf24', badgeBg: '#451a03', text: '#fef3c7', short: 'OUTPUT' },
      GROUND: { glow: '#10b981', stroke: '#34d399', badgeBg: '#022c22', text: '#a7f3d0', short: 'GROUND' }
    };

    // Kelompokkan seluruh tahap ke dalam 1 papan sirkuit terpadu:
    // Slot kiri-atas (POWER / Stage 0), Slot kiri-bawah (INPUT / Stage 1), Slot kanan-atas (OUTPUT), Slot kanan-bawah (FEEDBACK / GROUND)
    const s0 = stages[0];
    const s1 = stages[1] || null;
    const s2 = stages[2] || null;

    // Tentukan jalur yang masuk ke 4 zona secara cerdas dari urutan & tag stage!
    const mappedPaths = stages.map((st, idx) => {
      const pal = window.jb420WirePalette ? window.jb420WirePalette(st.wire) : { base: '#38bdf8', stripe: null, label: st.wire || 'SIG' };
      const tm = tagMeta[st.tag] || tagMeta.INPUT;
      const isCut = isFault && idx === faultStageIdx;
      const isFocused = activeStageIdx === -1 || activeStageIdx === idx;
      const opacity = isFocused ? 1 : 0.34;
      const wireCore = pal.base === '#18181b' ? '#64748b' : pal.base;
      return { st, idx, pal, tm, isCut, isFocused, opacity, wireCore };
    });

    // Tentukan geometri kabel & node untuk 1..3 jalur serentak di 1 kanvas 860×415!
    // Posisi tetap elegan:
    //  - Kiri Atas  (Node A: x=22..236, y=68..162)  --> terhubung ke Hub Tengah Kiri Atas (x=316, y=115)
    //  - Kiri Bawah (Node B: x=22..236, y=194..288) --> terhubung ke Hub Tengah Kiri Bawah (x=316, y=241)
    //  - Hub Tengah (ECM/Modul: x=316..544, y=64..294) -> berisi Chip IC + MIL LED + Mini Oscilloscope!
    //  - Kanan Atas (Node C: x=624..838, y=68..178) <-- terhubung dari Hub Tengah Kanan Atas (x=544, y=122)
    //  - Kanan Bawah(Node D: x=624..838, y=198..288)<-- terhubung dari Hub Tengah Kanan Bawah (x=544, y=242) + Loop Feedback/Massa!
    const slots = [];
    // Peta 3 stage ke jalur grafis terpadu yang mengalir logis kiri -> tengah -> kanan -> balik:
    if (mappedPaths.length >= 1) {
      const p0 = mappedPaths[0];
      slots.push({
        ...p0,
        nodeBox: { x: 20, y: 68, w: 214, h: 98, roleLbl: `JALUR #1 · ${p0.tm.short}`, title: p0.st.from, sub: p0.st.via },
        pathId: 'jb-path-0',
        d: 'M 234 117 C 266 117, 282 117, 316 117',
        midX: 275, midY: 98,
        arrowPts: '315,117 303,110 303,124',
        cutX: 275, cutY: 117
      });
    }
    if (mappedPaths.length >= 2) {
      const p1 = mappedPaths[1];
      const isOutputStage = p1.st.tag === 'OUTPUT';
      if (isOutputStage) {
        slots.push({
          ...p1,
          nodeBox: { x: 626, y: 68, w: 214, h: 108, roleLbl: `JALUR #2 · ${p1.tm.short}`, title: p1.st.to, sub: p1.st.via, hasActuator: true },
          pathId: 'jb-path-1',
          d: 'M 544 122 C 576 122, 594 122, 626 122',
          midX: 585, midY: 103,
          arrowPts: '625,122 613,115 613,129',
          cutX: 585, cutY: 122
        });
      } else {
        slots.push({
          ...p1,
          nodeBox: { x: 20, y: 192, w: 214, h: 98, roleLbl: `JALUR #2 · ${p1.tm.short}`, title: p1.st.from, sub: p1.st.via },
          pathId: 'jb-path-1',
          d: 'M 234 241 C 266 241, 282 241, 316 241',
          midX: 275, midY: 222,
          arrowPts: '315,241 303,234 303,248',
          cutX: 275, cutY: 241
        });
      }
    }
    if (mappedPaths.length >= 3) {
      const p2 = mappedPaths[2];
      const p1WasOutput = mappedPaths[1] && mappedPaths[1].st.tag === 'OUTPUT';
      if (p1WasOutput) {
        // p2 adalah Umpan Balik / Ground / Input sekunder: tampilkan di Kanan Bawah dengan jalur lengkung balik ke Hub Tengah!
        const isFeedbackToEcm = p2.st.tag === 'INPUT' || /ecm|umpan balik|feedback|sensor/i.test(p2.st.to);
        slots.push({
          ...p2,
          nodeBox: { x: 626, y: 196, w: 214, h: 96, roleLbl: `JALUR #3 · ${isFeedbackToEcm ? 'UMPAN BALIK' : p2.tm.short}`, title: isFeedbackToEcm ? p2.st.from : p2.st.to, sub: p2.st.via },
          pathId: 'jb-path-2',
          d: isFeedbackToEcm
            ? 'M 626 244 C 594 244, 576 244, 544 244'
            : 'M 544 244 C 576 244, 594 244, 626 244',
          midX: 585, midY: 225,
          arrowPts: isFeedbackToEcm ? '545,244 557,237 557,251' : '625,244 613,237 613,251',
          cutX: 585, cutY: 244
        });
      } else {
        // p0=Kiri Atas, p1=Kiri Bawah -> p2 di Kanan Atas (Target/Output/Ground Utama)
        slots.push({
          ...p2,
          nodeBox: { x: 626, y: 68, w: 214, h: 112, roleLbl: `JALUR #3 · ${p2.tm.short}`, title: p2.st.to, sub: p2.st.via, hasActuator: true },
          pathId: 'jb-path-2',
          d: 'M 544 124 C 576 124, 594 124, 626 124',
          midX: 585, midY: 105,
          arrowPts: '625,124 613,117 613,131',
          cutX: 585, cutY: 124
        });
      }
    }

    // Jika kotak Kiri Bawah kosong (karena p1=OUTPUT & p2=GROUND/FEEDBACK), tampilkan kotak Info Referensi Massa / Tegangan Sistem
    const hasLeftBottom = slots.some(sl => sl.nodeBox.x < 100 && sl.nodeBox.y > 170);
    const hasRightBottom = slots.some(sl => sl.nodeBox.x > 500 && sl.nodeBox.y > 170);
    const hasRightTop = slots.some(sl => sl.nodeBox.x > 500 && sl.nodeBox.y < 170);

    const fillerBoxes = [];
    if (!hasLeftBottom) {
      const refWire = (mod.wires || []).find(w => w.dir === 'ground' || w.dir === 'in') || (mod.wires || [])[0];
      const cleanSpec = refWire
        ? (refWire.spec.length > 26 ? `${refWire.spec.slice(0, 24).replace(/[\s,–\-(&]+$/, '')}…` : refWire.spec)
        : '0.0–0.2 V · < 1 Ω';
      fillerBoxes.push(`
        <g opacity="0.92">
          <rect x="20" y="192" width="214" height="98" rx="12" fill="#071326" stroke="#334155" stroke-width="1.4" stroke-dasharray="5 3"/>
          <rect x="30" y="201" width="118" height="16" rx="4" fill="#0f172a" stroke="#475569" stroke-width="0.8"/>
          <text x="89" y="212" text-anchor="middle" fill="#94a3b8" font-family="Consolas,monospace" font-size="8.5" font-weight="700">REFERENSI PIN &amp; GND</text>
          ${renderSvgTextLines(wrapLines(refWire ? refWire.to : 'Massa Blok Mesin (< 1 Ω)', 24, 2), 127, 236, '#cbd5e1', 10.5, '700')}
          <text x="127" y="274" text-anchor="middle" fill="#34d399" font-family="Consolas,monospace" font-size="9.5" font-weight="700">${_esc(cleanSpec)}</text>
          <path d="M 234 241 L 316 241" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
        </g>`);
    }
    if (!hasRightTop) {
      fillerBoxes.push(`
        <g>
          <rect x="626" y="68" width="214" height="110" rx="12" fill="#0a1930" stroke="#38bdf8" stroke-width="1.6"/>
          <rect x="636" y="77" width="118" height="16" rx="4" fill="#020617" stroke="#38bdf8" stroke-width="0.8"/>
          <text x="695" y="88" text-anchor="middle" fill="#7dd3fc" font-family="Consolas,monospace" font-size="8.5" font-weight="700">RESPON AKTUATOR</text>
          ${renderSvgTextLines(wrapLines(mod.title, 18, 2), 700, 114, '#ffffff', 10.5, '700')}
          <text x="700" y="158" text-anchor="middle" fill="#94a3b8" font-family="Consolas,monospace" font-size="9">${_esc(profile.metric3.val)}</text>
          ${buildActuatorMiniVisual(profile, isIgOn, isFault)}
          <path d="M 544 123 L 626 123" stroke="${isFault ? '#f43f5e' : '#38bdf8'}" stroke-width="3" stroke-dasharray="6 4"/>
        </g>`);
    }
    if (!hasRightBottom) {
      // Tutup loop feedback bawah dari Kanan Atas ke Hub Tengah agar tampak sebagai 1 sirkuit utuh!
      fillerBoxes.push(`
        <g opacity="0.92">
          <rect x="626" y="198" width="214" height="92" rx="12" fill="#041c1a" stroke="#10b981" stroke-width="1.4"/>
          <rect x="636" y="207" width="128" height="16" rx="4" fill="#022c22" stroke="#34d399" stroke-width="0.8"/>
          <text x="700" y="218" text-anchor="middle" fill="#6ee7b7" font-family="Consolas,monospace" font-size="8.5" font-weight="700">LOOP MASSA &amp; VERIFIKASI</text>
          <text x="733" y="244" text-anchor="middle" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700">Titik Ground / Loop Balik</text>
          <text x="733" y="264" text-anchor="middle" fill="#34d399" font-family="Consolas,monospace" font-size="10" font-weight="700">${isFault ? '⚠ LOOP TERPUTUS!' : '✓ RANGKAIAN TERTUTUP OK'}</text>
          <path id="jb-loop-close" d="M 733 180 L 733 198" stroke="${isFault ? '#f43f5e' : '#10b981'}" stroke-width="2.5" stroke-dasharray="4 3"/>
          <path id="jb-loop-ret" d="M 626 244 L 544 244" stroke="${isFault ? '#f43f5e' : '#10b981'}" stroke-width="2.5" stroke-dasharray="5 4"/>
          ${!isFault ? `<circle r="3.5" fill="#6ee7b7"><animateMotion dur="${(speedDur * 1.1).toFixed(2)}s" repeatCount="indefinite"><mpath href="#jb-loop-ret"/></animateMotion></circle>` : ''}
        </g>`);
    }

    // Render setiap jalur kabel & kotaknya secara interaktif (clickable!)
    const wiresAndNodesSvg = slots.map(sl => {
      const clickFn = isFault ? `setJb420FaultStage(${sl.idx})` : `setJb420Stage(${sl.idx})`;
      const nodeTitleLines = wrapLines(sl.nodeBox.title, sl.nodeBox.hasActuator ? 17 : 22, 2);
      const nodeSubLines = wrapLines(sl.nodeBox.sub, sl.nodeBox.hasActuator ? 18 : 24, 1);
      const textCenterX = sl.nodeBox.hasActuator ? (sl.nodeBox.x + 84) : (sl.nodeBox.x + sl.nodeBox.w / 2);

      // Animated traveling electrons (2 orbs staggered along path!)
      const particles = sl.isCut
        ? `<g transform="translate(${sl.cutX},${sl.cutY})">
             <circle r="13" fill="#450a0a" stroke="#f43f5e" stroke-width="2">
               <animate attributeName="r" values="11;15;11" dur="0.8s" repeatCount="indefinite"/>
             </circle>
             <text x="0" y="4" text-anchor="middle" fill="#fecdd3" font-family="Consolas,monospace" font-size="12" font-weight="900">✕</text>
           </g>`
        : `
          <circle r="4.5" fill="#ffffff" filter="url(#neonGlow)">
            <animateMotion dur="${speedDur.toFixed(2)}s" repeatCount="indefinite"><mpath href="#${sl.pathId}"/></animateMotion>
          </circle>
          <circle r="3.5" fill="${sl.tm.stroke}" opacity="0.9">
            <animateMotion dur="${speedDur.toFixed(2)}s" begin="${(speedDur / 2).toFixed(2)}s" repeatCount="indefinite"><mpath href="#${sl.pathId}"/></animateMotion>
          </circle>`;

      return `
        <g class="cursor-pointer" onclick="${clickFn}" opacity="${sl.opacity}">
          <!-- Neon Glow Trace -->
          <path d="${sl.d}" fill="none" stroke="${sl.isCut ? '#f43f5e' : sl.tm.glow}" stroke-width="11" stroke-opacity="${sl.isCut ? '0.35' : '0.24'}" filter="url(#neonGlow)"/>
          <!-- Real OEM Wire Core -->
          <path id="${sl.pathId}" d="${sl.d}" fill="none" stroke="${sl.isCut ? '#991b1b' : sl.wireCore}" stroke-width="6" stroke-linecap="round" ${sl.isCut ? 'stroke-dasharray="7 7"' : ''}/>
          ${sl.pal.stripe && !sl.isCut ? `<path d="${sl.d}" fill="none" stroke="${sl.pal.stripe}" stroke-width="2.5" stroke-dasharray="10 8"/>` : ''}
          <!-- Arrowhead -->
          <polygon points="${sl.arrowPts}" fill="${sl.isCut ? '#f43f5e' : sl.tm.stroke}"/>
          <!-- Traveling Electron Particles / Cut Icon -->
          ${particles}
          <!-- OEM Wire Color Pill -->
          <rect x="${sl.midX - 38}" y="${sl.midY - 11}" width="76" height="19" rx="9" fill="#020617" stroke="${sl.isCut ? '#f43f5e' : sl.tm.stroke}" stroke-width="1.2"/>
          <text x="${sl.midX}" y="${sl.midY + 2}" text-anchor="middle" fill="${sl.isCut ? '#fda4af' : '#ffffff'}" font-family="Consolas,monospace" font-size="9.5" font-weight="700">${sl.isCut ? 'OPEN ⚠' : _esc(sl.pal.label)}</text>

          <!-- Connected Component Node Card -->
          <rect x="${sl.nodeBox.x}" y="${sl.nodeBox.y}" width="${sl.nodeBox.w}" height="${sl.nodeBox.h}" rx="12"
                fill="${sl.isCut ? '#2a0812' : sl.tm.badgeBg}" stroke="${sl.isCut ? '#f43f5e' : sl.tm.stroke}"
                stroke-width="${activeStageIdx === sl.idx ? '2.6' : '1.7'}"/>
          <rect x="${sl.nodeBox.x + 10}" y="${sl.nodeBox.y + 9}" width="${Math.min(148, sl.nodeBox.w - 20)}" height="16" rx="4" fill="#020617" stroke="${sl.isCut ? '#f43f5e' : sl.tm.stroke}" stroke-width="0.8"/>
          <text x="${sl.nodeBox.x + 16}" y="${sl.nodeBox.y + 20}" fill="${sl.isCut ? '#fda4af' : sl.tm.text}" font-family="Consolas,monospace" font-size="8.5" font-weight="800">${_esc(sl.nodeBox.roleLbl)}</text>
          ${renderSvgTextLines(nodeTitleLines, textCenterX, sl.nodeBox.y + 44, '#ffffff', 11, '700')}
          ${renderSvgTextLines(nodeSubLines, textCenterX, sl.nodeBox.y + 78, '#94a3b8', 9.5, '600')}
          ${sl.nodeBox.hasActuator ? buildActuatorMiniVisual(profile, isIgOn, isFault) : ''}
        </g>`;
    }).join('');

    // Central Microprocessor Hub + Live Oscilloscope
    const osc = buildOscilloscopePath(profile.waveType, simSliderVal, isIgOn, isFault);
    const primaryDtc = (mod.dtcs && mod.dtcs[0]) ? mod.dtcs[0] : 'DTC';
    const milBg = isFault ? '#7f1d1d' : '#064e3b';
    const milStroke = isFault ? '#f43f5e' : '#10b981';
    const milText = isFault ? `⚠ MIL ON · ${primaryDtc}` : (isIgOn ? '🔑 IG ON · STANDBY' : '● SISTEM LIVE OK');

    // IC chip decorative pins along ECM left & right sides
    const icPins = [92, 117, 142, 167, 216, 241, 266].map(y =>
      `<rect x="309" y="${y - 3}" width="7" height="6" rx="1.5" fill="#38bdf8" opacity="0.65"/>
       <rect x="544" y="${y - 3}" width="7" height="6" rx="1.5" fill="#fbbf24" opacity="0.65"/>`
    ).join('');

    // Active explanation footer inside SVG (adapts to unified overview, focused wire, or fault injection!)
    let bottomTitle = '';
    let bottomDesc = '';
    if (isFault) {
      const cutSt = stages[Math.min(faultStageIdx, stages.length - 1)] || stages[0];
      const matchW = (mod.wires || [])[Math.min(faultStageIdx, Math.max(0, (mod.wires || []).length - 1))];
      bottomTitle = `💥 SIMULASI PUTUS JALUR #${cutSt.step} (${cutSt.wire}): ${cutSt.title}`;
      bottomDesc = matchW
        ? `Dampak & Cek Multimeter: ${matchW.faultHint} · Ukur ${matchW.probe} (Standar: ${matchW.spec})`
        : `Aliran terputus di ${cutSt.from} → ${cutSt.to}! ECM langsung menyalakan MIL (${primaryDtc}).`;
    } else if (activeStageIdx >= 0 && stages[activeStageIdx]) {
      const fs = stages[activeStageIdx];
      bottomTitle = `🔍 FOKUS JALUR #${fs.step} (${fs.tag} · ${fs.wire}): ${fs.title}`;
      bottomDesc = fs.desc;
    } else {
      bottomTitle = `⚡ ALUR SIRKUIT TERPADU (${stages.length} JALUR HIDUP SERENTAK) — Klik kabel mana saja untuk sorot detail!`;
      bottomDesc = stages.map(s => `[${s.step}] ${s.from} → ${s.to}`).join('  |  ');
    }

    return `
      <svg viewBox="0 0 860 408" class="w-full h-auto block rounded-xl border border-cyan-500/35 bg-[#040916] shadow-2xl select-none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="pcbGrid" width="22" height="22" patternUnits="userSpaceOnUse">
            <path d="M 22 0 L 0 0 0 22" fill="none" stroke="#0c182e" stroke-width="1"/>
          </pattern>
          <radialGradient id="hubGrad" cx="50%" cy="35%" r="70%">
            <stop offset="0%" stop-color="#0f294a"/>
            <stop offset="100%" stop-color="#050d1d"/>
          </radialGradient>
          <filter id="neonGlow" x="-25%" y="-25%" width="150%" height="150%">
            <feGaussianBlur stdDeviation="3.5" result="blur"/>
            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
        </defs>

        <!-- PCB Background -->
        <rect width="860" height="408" fill="url(#pcbGrid)"/>

        <!-- Top Telemetry HUD Bar -->
        <rect x="16" y="12" width="828" height="40" rx="10" fill="#091326" stroke="#1e3a5f" stroke-width="1.2"/>
        <text x="30" y="36" fill="#38bdf8" font-family="Consolas,monospace" font-size="11.5" font-weight="800">⚡ PAPAN SIRKUIT HIDUP TERPADU · ${_esc(mod.badge)}</text>
        <!-- 3 Live Readout Chips on Top Right -->
        <rect x="428" y="18" width="132" height="28" rx="6" fill="#040b18" stroke="#1e293b"/>
        <text x="494" y="28" text-anchor="middle" fill="#64748b" font-family="Consolas,monospace" font-size="7.5" font-weight="700">${_esc(profile.metric1.lbl)}</text>
        <text x="494" y="41" text-anchor="middle" fill="${isFault ? '#fb7185' : '#22d3ee'}" font-family="Consolas,monospace" font-size="10.5" font-weight="800">${_esc(profile.metric1.val)}</text>

        <rect x="568" y="18" width="132" height="28" rx="6" fill="#040b18" stroke="#1e293b"/>
        <text x="634" y="28" text-anchor="middle" fill="#64748b" font-family="Consolas,monospace" font-size="7.5" font-weight="700">${_esc(profile.metric2.lbl)}</text>
        <text x="634" y="41" text-anchor="middle" fill="${isFault ? '#fb7185' : '#34d399'}" font-family="Consolas,monospace" font-size="10.5" font-weight="800">${_esc(profile.metric2.val)}</text>

        <rect x="708" y="18" width="128" height="28" rx="6" fill="#040b18" stroke="#1e293b"/>
        <text x="772" y="28" text-anchor="middle" fill="#64748b" font-family="Consolas,monospace" font-size="7.5" font-weight="700">${_esc(profile.metric3.lbl)}</text>
        <text x="772" y="41" text-anchor="middle" fill="${isFault ? '#fb7185' : '#fbbf24'}" font-family="Consolas,monospace" font-size="10.5" font-weight="800">${_esc(profile.metric3.val)}</text>

        <!-- Filler Loops & Reference Cards -->
        ${fillerBoxes.join('')}

        <!-- ALL UNIFIED WIRES & COMPONENT NODES -->
        ${wiresAndNodesSvg}

        <!-- CENTRAL HUB: MICROPROCESSOR ECM / MODUL + LIVE OSCILLOSCOPE -->
        <g>
          ${icPins}
          <rect x="316" y="64" width="228" height="228" rx="16" fill="url(#hubGrad)" stroke="${isFault ? '#f43f5e' : '#22d3ee'}" stroke-width="2.2" filter="url(#neonGlow)"/>
          <!-- Pulse Ring Heartbeat -->
          <circle cx="337" cy="86" r="5" fill="${isFault ? '#f43f5e' : '#10b981'}">
            <animate attributeName="opacity" values="1;0.25;1" dur="${isFault ? '0.45s' : '1.3s'}" repeatCount="indefinite"/>
          </circle>
          <!-- MIL Status Pill -->
          <rect x="350" y="75" width="182" height="22" rx="11" fill="${milBg}" stroke="${milStroke}" stroke-width="1.2"/>
          <text x="441" y="90" text-anchor="middle" fill="#ffffff" font-family="Consolas,monospace" font-size="10" font-weight="800">${_esc(milText)}</text>

          <!-- Hub Title & Connector ID -->
          <text x="430" y="124" text-anchor="middle" fill="#ffffff" font-family="system-ui,Segoe UI,sans-serif" font-size="16" font-weight="900" letter-spacing="0.5">${_esc(profile.hubTitle)}</text>
          <text x="430" y="142" text-anchor="middle" fill="#7dd3fc" font-family="Consolas,monospace" font-size="10" font-weight="700">${_esc(profile.hubSub)}</text>

          <!-- Internal Logic Bus Indicator -->
          <rect x="334" y="154" width="192" height="24" rx="6" fill="#040b18" stroke="#1e3a5f"/>
          <text x="430" y="170" text-anchor="middle" fill="#cbd5e1" font-family="Consolas,monospace" font-size="9.5" font-weight="700">INPUT ➔ LOGIKA MCU ➔ DRIVER</text>

          <!-- MINI LIVE OSCILLOSCOPE SCREEN -->
          <rect x="334" y="188" width="192" height="90" rx="8" fill="#020814" stroke="#1e3a5f" stroke-width="1.2"/>
          <!-- Scope Grid Lines -->
          <line x1="334" y1="218" x2="526" y2="218" stroke="#0f2540" stroke-width="0.8" stroke-dasharray="3 3"/>
          <line x1="334" y1="238" x2="526" y2="238" stroke="#153254" stroke-width="0.9"/>
          <line x1="334" y1="258" x2="526" y2="258" stroke="#0f2540" stroke-width="0.8" stroke-dasharray="3 3"/>
          <line x1="382" y1="188" x2="382" y2="278" stroke="#0f2540" stroke-width="0.8" stroke-dasharray="3 3"/>
          <line x1="430" y1="188" x2="430" y2="278" stroke="#0f2540" stroke-width="0.8" stroke-dasharray="3 3"/>
          <line x1="478" y1="188" x2="478" y2="278" stroke="#0f2540" stroke-width="0.8" stroke-dasharray="3 3"/>
          <!-- Scope Header -->
          <text x="342" y="201" fill="#64748b" font-family="Consolas,monospace" font-size="8" font-weight="700">OSCILLOSCOPE</text>
          <text x="518" y="201" text-anchor="end" fill="${osc.color}" font-family="Consolas,monospace" font-size="8" font-weight="800">${_esc(osc.label)}</text>
          <!-- Animated Waveform Trace -->
          <path d="${osc.path}" fill="none" stroke="${osc.color}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" filter="url(#neonGlow)"/>
        </g>

        <!-- Bottom Interactive Analysis Strip -->
        <rect x="16" y="308" width="828" height="86" rx="10" fill="${isFault ? '#2a0812' : '#081326'}" stroke="${isFault ? '#f43f5e' : '#1e3a5f'}" stroke-width="1.3"/>
        <text x="32" y="332" fill="${isFault ? '#fda4af' : '#38bdf8'}" font-family="system-ui,Segoe UI,sans-serif" font-size="12" font-weight="800">${_esc(bottomTitle.slice(0, 96))}</text>
        ${renderSvgTextLines(wrapLines(bottomDesc, 110, 2), 430, 354, '#e2e8f0', 11, '500')}
      </svg>
    `;
  }

  function buildNonWiringFlowSvg(mod) {
    const isCat = mod.id === 'gv_nonwiring_p0420';
    return `
      <svg viewBox="0 0 860 190" class="w-full h-auto block rounded-xl border border-amber-500/40 bg-[#050b18] shadow-xl select-none" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="nwGrid" width="22" height="22" patternUnits="userSpaceOnUse">
            <path d="M 22 0 L 0 0 0 22" fill="none" stroke="#131c2e" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="860" height="190" fill="url(#nwGrid)"/>
        <text x="24" y="28" fill="#fbbf24" font-family="Consolas,monospace" font-size="11.5" font-weight="800">⚙️ ALUR FISIK MEKANIS / FLUIDA TERPADU (NON-WIRING · ${_esc(mod.dtcs.join(', '))})</text>
        <!-- Node 1 -->
        <rect x="24" y="48" width="175" height="92" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8"/>
        <text x="111" y="76" text-anchor="middle" fill="#7dd3fc" font-family="Consolas,monospace" font-size="9.5" font-weight="700">${isCat ? '1. GAS BUANG MESIN' : '1. INTAKE &amp; VAKUM'}</text>
        <text x="111" y="100" text-anchor="middle" fill="#ffffff" font-family="system-ui,sans-serif" font-size="11.5" font-weight="800">${isCat ? 'Campuran BBM &amp; Api' : 'Filter + MAF + Selang'}</text>
        <text x="111" y="122" text-anchor="middle" fill="#fbbf24" font-family="Consolas,monospace" font-size="9.5">${isCat ? 'Cek Misfire / Fuel Trim' : 'Cek Bocor Vakum!'}</text>

        <path id="nw1" d="M 199 94 L 245 94" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6 4"/>
        <circle r="4" fill="#fff"><animateMotion dur="1.1s" repeatCount="indefinite"><mpath href="#nw1"/></animateMotion></circle>

        <!-- Node 2 -->
        <rect x="245" y="48" width="175" height="92" rx="12" fill="#451a03" stroke="#f59e0b" stroke-width="2"/>
        <text x="332" y="76" text-anchor="middle" fill="#fde68a" font-family="Consolas,monospace" font-size="9.5" font-weight="700">${isCat ? '2. A/F SENSOR-1 (HULU)' : '2. TEKANAN BBM &amp; INJ'}</text>
        <text x="332" y="100" text-anchor="middle" fill="#ffffff" font-family="system-ui,sans-serif" font-size="11.5" font-weight="800">${isCat ? 'Cek Bocor Knalpot' : 'Pompa 3.0–3.5 bar'}</text>
        <text x="332" y="122" text-anchor="middle" fill="#fcd34d" font-family="Consolas,monospace" font-size="9.5">${isCat ? 'Arus −0.20..+0.10 mA' : 'Injektor Bersih?'}</text>

        <path id="nw2" d="M 420 94 L 466 94" stroke="#fbbf24" stroke-width="4" stroke-dasharray="6 4"/>
        <circle r="4" fill="#fff"><animateMotion dur="1.1s" repeatCount="indefinite"><mpath href="#nw2"/></animateMotion></circle>

        <!-- Node 3 -->
        <rect x="466" y="48" width="175" height="92" rx="12" fill="#083344" stroke="#22d3ee" stroke-width="1.8"/>
        <text x="553" y="76" text-anchor="middle" fill="#a5f3fc" font-family="Consolas,monospace" font-size="9.5" font-weight="700">${isCat ? '3. KATALIS KONVERTER' : '3. RUANG BAKAR &amp; A/F'}</text>
        <text x="553" y="100" text-anchor="middle" fill="#ffffff" font-family="system-ui,sans-serif" font-size="11.5" font-weight="800">${isCat ? 'Beda Suhu +30..60°C' : 'A/F Deteksi Kurus'}</text>
        <text x="553" y="122" text-anchor="middle" fill="#67e8f9" font-family="Consolas,monospace" font-size="9.5">${isCat ? 'Outlet > Inlet' : 'STFT + LTFT > +20%'}</text>

        <path id="nw3" d="M 641 94 L 687 94" stroke="#10b981" stroke-width="4" stroke-dasharray="6 4"/>
        <circle r="4" fill="#fff"><animateMotion dur="1.1s" repeatCount="indefinite"><mpath href="#nw3"/></animateMotion></circle>

        <!-- Node 4 -->
        <rect x="687" y="48" width="150" height="92" rx="12" fill="#022c22" stroke="#34d399" stroke-width="1.8"/>
        <text x="762" y="76" text-anchor="middle" fill="#a7f3d0" font-family="Consolas,monospace" font-size="9.5" font-weight="700">4. VERIFIKASI ECM</text>
        <text x="762" y="100" text-anchor="middle" fill="#ffffff" font-family="system-ui,sans-serif" font-size="11.5" font-weight="800">${isCat ? 'HO2S-2 Tenang' : 'Fuel Trim Normal'}</text>
        <text x="762" y="122" text-anchor="middle" fill="#6ee7b7" font-family="Consolas,monospace" font-size="9.5">${isCat ? '~0.6–0.7 V Stabil' : 'STFT/LTFT ±5%'}</text>

        <text x="430" y="170" text-anchor="middle" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="11">Kode ini dipicu penyimpangan aliran udara/BBM/gas buang mekanis—lakukan daftar cek fisik di bawah sebelum bongkar wiring.</text>
      </svg>`;
  }

  function updateCategoryButtons() {
    const atlas = getAtlas();
    const counts = {
      efi: atlas.filter(m => m.category === 'efi').length,
      modules: atlas.filter(m => m.category === 'modules').length,
      base: atlas.filter(m => m.category === 'base').length,
      all: atlas.length
    };
    document.querySelectorAll('.jb420-cat-btn').forEach(btn => {
      const cat = btn.dataset.cat;
      const cntEl = btn.querySelector('.jb420-cat-cnt');
      if (cntEl && counts[cat] != null) cntEl.textContent = counts[cat];
      if (cat === activeCategory) {
        btn.className = 'jb420-cat-btn shrink-0 px-3 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-600 to-brand-600 text-white border border-cyan-400/60 shadow-md shadow-cyan-900/40 flex items-center gap-1.5 transition active:scale-95';
      } else {
        btn.className = 'jb420-cat-btn shrink-0 px-3 py-2 rounded-xl text-xs font-semibold bg-slate-950/90 text-slate-300 hover:text-white border border-slate-700/90 hover:border-cyan-500/60 flex items-center gap-1.5 transition active:scale-95';
      }
    });
  }

  function getFilteredModules() {
    const atlas = getAtlas();
    const q = (document.getElementById('jb420-atlas-search')?.value || '').trim().toLowerCase();
    if (!q) {
      return atlas.filter(m => activeCategory === 'all' || m.category === activeCategory);
    }
    const tokens = q.split(/\s+/).filter(Boolean);
    const scored = [];
    for (const m of atlas) {
      const dtcsLow = (m.dtcs || []).map(d => String(d).toLowerCase());
      const badgeLow = String(m.badge || '').toLowerCase();
      const titleLow = String(m.title || '').toLowerCase();
      const subLow = String(m.subtitle || '').toLowerCase();
      const wireLow = (m.wires || []).map(w => `${w.colorCode} ${w.from} ${w.to} ${w.role} ${w.func}`).join(' ').toLowerCase();
      const fullHay = `${m.id} ${badgeLow} ${titleLow} ${subLow} ${dtcsLow.join(' ')} ${wireLow}`;
      if (!tokens.every(t => fullHay.includes(t))) continue;

      let score = 0;
      for (const t of tokens) {
        if (dtcsLow.some(d => d === t)) score += 120;
        else if (dtcsLow.some(d => d.includes(t))) score += 75;
        if (badgeLow.includes(t)) score += 65;
        if (titleLow.includes(t)) score += 55;
        if (subLow.includes(t)) score += 25;
        if (wireLow.includes(t)) score += 6;
      }
      scored.push({ m, score });
    }
    scored.sort((a, b) => b.score - a.score);
    return scored.map(x => x.m);
  }

  function renderModuleSelector() {
    const listEl = document.getElementById('jb420-module-pills');
    const selEl = document.getElementById('jb420-module-select');
    const items = getFilteredModules();

    if (items.length && !items.some(m => m.id === activeModuleId)) {
      activeModuleId = items[0].id;
      activePhotoIdx = 0;
      activeStageIdx = -1;
      faultStageIdx = 0;
    }

    if (selEl) {
      selEl.innerHTML = items.map(m =>
        `<option value="${_esc(m.id)}" ${m.id === activeModuleId ? 'selected' : ''}>[${_esc(m.badge)}] ${_esc(m.title)} (${_esc((m.dtcs || []).slice(0, 3).join(', '))})</option>`
      ).join('') || '<option value="">Tidak ditemukan modul cocok...</option>';
    }

    if (listEl) {
      if (!items.length) {
        listEl.innerHTML = '<div class="text-xs text-slate-400 py-2">Tidak ada sirkuit JB420 yang cocok dengan kata kunci pencarian.</div>';
        return;
      }
      listEl.innerHTML = items.map(m => {
        const isAct = m.id === activeModuleId;
        const dtcShort = (m.dtcs || []).slice(0, 2).join(', ');
        const nwDot = m.isNonWiring
          ? '<span class="w-2 h-2 rounded-full bg-amber-400 shrink-0" title="Kasus Non-Wiring / Mekanis"></span>'
          : (m.safetyGuard === 'srs'
            ? '<span class="w-2 h-2 rounded-full bg-rose-500 shrink-0" title="SRS Air Bag Safety"></span>'
            : '<span class="w-2 h-2 rounded-full bg-cyan-400 shrink-0"></span>');
        const cls = isAct
          ? 'bg-cyan-950/90 border-cyan-400 text-white ring-1 ring-cyan-400/50 shadow-lg shadow-cyan-950/50'
          : 'bg-slate-950/80 border-slate-800 text-slate-300 hover:border-cyan-500/50 hover:text-white';
        return `<button type="button" onclick="selectJb420Module('${_esc(m.id)}')" class="shrink-0 text-left px-3 py-2 rounded-xl border ${cls} transition active:scale-95 max-w-[245px]">
          <div class="flex items-center gap-1.5 text-[10px] font-mono font-bold ${isAct ? 'text-cyan-300' : 'text-slate-400'}">
            ${nwDot}
            <span class="truncate">${_esc(m.badge)}</span>
          </div>
          <div class="text-[11.5px] font-bold truncate mt-0.5">${_esc(m.title)}</div>
          <div class="text-[10px] font-mono text-amber-300/90 truncate mt-0.5">${_esc(dtcShort)}</div>
        </button>`;
      }).join('');
    }
  }

  function applyUnifiedInlineZoom() {
    const wrap = document.getElementById('jb420-unified-svg-wrap');
    const svg = wrap ? wrap.querySelector('svg') : null;
    const lbl = document.getElementById('jb420-unified-zoom-lbl');
    if (svg) {
      const baseW = (wrap && wrap.clientWidth > 60) ? wrap.clientWidth : 320;
      const targetPx = Math.round(baseW * unifiedZoom);
      svg.classList.remove('w-full');
      svg.style.width = unifiedZoom <= 1.01 ? '100%' : `${targetPx}px`;
      svg.style.minWidth = unifiedZoom <= 1.01 ? '0' : `${targetPx}px`;
      svg.style.maxWidth = 'none';
    }
    if (lbl) lbl.textContent = `${Math.round(unifiedZoom * 100)}%`;
  }

  function refreshUnifiedSvgOnly() {
    const mod = getActiveModule();
    const wrap = document.getElementById('jb420-unified-svg-wrap');
    const sliderValLbl = document.getElementById('jb420-sim-slider-val');
    if (!mod || !wrap) return;
    wrap.innerHTML = buildUnifiedCircuitSvg(mod);
    applyUnifiedInlineZoom();
    if (sliderValLbl) {
      sliderValLbl.textContent = getModuleSimProfile(mod).sliderValueText;
    }
  }

  function renderActiveModuleStage() {
    const mod = getActiveModule();
    const host = document.getElementById('jb420-stage-host');
    if (!mod || !host) return;

    const dtcBadges = (mod.dtcs || []).map(c =>
      `<span class="px-2 py-0.5 rounded-md bg-amber-500/15 text-amber-300 border border-amber-500/40 font-mono text-[10.5px] font-bold">${_esc(c)}</span>`
    ).join('');

    // Mode Toggle Buttons (Sakelar 2-Mode!)
    const flowBtnCls = activeVisualMode === 'flow'
      ? 'bg-gradient-to-r from-cyan-600 to-brand-600 text-white border-cyan-400 shadow-lg shadow-cyan-950/50'
      : 'bg-slate-950 text-slate-300 border-slate-700 hover:border-cyan-500/60 hover:text-white';
    const photoBtnCls = activeVisualMode === 'photo'
      ? 'bg-amber-500 bg-gradient-to-r from-amber-500 to-orange-500 text-slate-950 border-amber-300 shadow-lg shadow-amber-950/50'
      : 'bg-slate-950 text-slate-300 border-slate-700 hover:border-amber-400/60 hover:text-white';

    // Safety Guardrail Banner
    let safetyHtml = '';
    if (mod.safetyGuard === 'srs') {
      safetyHtml = `
        <div class="rounded-xl bg-rose-950/80 border-2 border-rose-500/80 p-3 flex items-start gap-2.5 text-xs text-rose-100 shadow-lg">
          <i class="fa-solid fa-skull-crossbones text-rose-400 text-base mt-0.5 shrink-0"></i>
          <div>
            <div class="font-extrabold text-rose-300 uppercase tracking-wide">⛔ PERINGATAN KESELAMATAN SRS AIR BAG (WAJIB!)</div>
            <p class="mt-0.5 leading-relaxed"><strong>DILARANG KERAS</strong> mengukur tahanan modul inflator Air Bag memakai ohmmeter/multimeter biasa (arus uji dapat memicu ledakan Air Bag!). Lepas kabel negatif (−) aki dan <strong>tunggu minimal 90 detik</strong> sebelum menyentuh konektor kuning.</p>
          </div>
        </div>`;
    } else if (mod.safetyGuard === 'ohm') {
      safetyHtml = `
        <div class="rounded-xl bg-amber-950/50 border border-amber-500/50 px-3.5 py-2.5 flex items-center gap-2 text-[11.5px] text-amber-200">
          <i class="fa-solid fa-triangle-exclamation text-amber-400 shrink-0"></i>
          <span><strong>Keselamatan Kerja Multimeter:</strong> Wajib <strong>Kunci Kontak OFF &amp; Lepas Soket</strong> sebelum mengukur tahanan (Mode Ohm Ω / Kontinuitas) agar sirkuit ECM tidak rusak.</span>
        </div>`;
    }

    // Visual Stage Content: UNIFIED LIVE FLOW MODE OR OEM PHOTO MODE
    let visualStageHtml = '';
    if (activeVisualMode === 'flow') {
      if (mod.isNonWiring) {
        const mechHtml = (mod.mechChecks || []).map(item => `
          <div class="rounded-xl bg-slate-950/90 border border-amber-500/35 p-3 flex items-start gap-3">
            <div class="w-7 h-7 rounded-lg bg-amber-500/20 border border-amber-400/50 text-amber-300 font-mono font-extrabold text-xs flex items-center justify-center shrink-0">${item.step}</div>
            <div>
              <div class="text-xs font-bold text-white">${_esc(item.title)}</div>
              <p class="text-[11.5px] text-slate-300 mt-0.5 leading-relaxed">${_esc(item.detail)}</p>
            </div>
          </div>
        `).join('');

        const atlas = getAtlas();
        const relBtns = (mod.relatedIds || []).map(rid => {
          const rm = atlas.find(x => x.id === rid);
          if (!rm) return '';
          return `<button type="button" onclick="selectJb420Module('${_esc(rm.id)}', 'photo')" class="px-3 py-2 rounded-xl bg-cyan-950/80 hover:bg-cyan-700 border border-cyan-500/50 text-cyan-200 hover:text-white text-xs font-bold flex items-center gap-1.5 transition active:scale-95">
            <i class="fa-solid fa-diagram-project text-cyan-400"></i>
            <span>Buka Foto Wiring: ${_esc(rm.title)}</span>
          </button>`;
        }).join('');

        visualStageHtml = `
          <div class="rounded-2xl bg-gradient-to-br from-amber-950/40 via-slate-950 to-slate-950 border-2 border-amber-500/50 p-4 space-y-3.5">
            <div class="flex items-start gap-3">
              <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-400/60 text-amber-300 flex items-center justify-center text-lg shrink-0">
                <i class="fa-solid fa-gears"></i>
              </div>
              <div>
                <span class="inline-block px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 text-[10px] font-extrabold uppercase">Klasifikasi: Gangguan Sistem Mekanis / Fluida (Non-Wiring)</span>
                <p class="text-xs text-slate-200 mt-1.5 leading-relaxed">${_esc(mod.nonWiringSummary)}</p>
              </div>
            </div>
            <div class="overflow-x-auto">${buildNonWiringFlowSvg(mod)}</div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5">${mechHtml}</div>
            <div class="pt-2 border-t border-slate-800 space-y-2">
              <div class="text-[11px] font-bold text-cyan-300 uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-bolt"></i> Pintasan Foto Wiring Sensor Terkait (Jika Cek Mekanis Normal):
              </div>
              <div class="flex flex-wrap gap-2">${relBtns}</div>
            </div>
          </div>`;
      } else {
        const stages = mod.stages || [];
        const profile = getModuleSimProfile(mod);
        const modeBtn = (key, label, activeCls) => {
          const isOn = simRunMode === key;
          const cls = isOn
            ? activeCls
            : 'bg-slate-900 text-slate-300 border-slate-700 hover:border-cyan-500/60 hover:text-white';
          return `<button type="button" onclick="setJb420SimMode('${key}')" class="px-2.5 sm:px-3 py-1.5 rounded-lg border text-[11px] font-extrabold transition active:scale-95 ${cls}">${label}</button>`;
        };

        // Unified Quick-Spotlight Chips (Semua jalur tetap tampil utuh, tombol ini hanya menyorot atau memilih jalur putus!)
        const allChipCls = (activeStageIdx === -1 && simRunMode !== 'fault')
          ? 'bg-cyan-600 text-white border-cyan-400 shadow'
          : 'bg-slate-950 text-slate-300 border-slate-700 hover:border-cyan-500/60 hover:text-white';
        const wireFilterChips = [
          `<button type="button" onclick="setJb420Stage(-1)" class="shrink-0 px-2.5 py-1 rounded-lg border text-[10.5px] font-bold transition ${allChipCls}">🌐 Semua Jalur (${stages.length})</button>`,
          ...stages.map((st, idx) => {
            const isSel = simRunMode === 'fault' ? (faultStageIdx === idx) : (activeStageIdx === idx);
            const cls = isSel
              ? (simRunMode === 'fault' ? 'bg-rose-600 text-white border-rose-400 shadow' : 'bg-amber-500 text-slate-950 border-amber-300 shadow')
              : 'bg-slate-950 text-slate-300 border-slate-700 hover:border-cyan-500/60 hover:text-white';
            const fn = simRunMode === 'fault' ? `setJb420FaultStage(${idx})` : `setJb420Stage(${idx})`;
            return `<button type="button" onclick="${fn}" class="shrink-0 px-2.5 py-1 rounded-lg border text-[10.5px] font-bold transition ${cls}">
              ${simRunMode === 'fault' ? '💥 Putus' : '🔍 Sorot'} #${st.step} ${_esc(st.tag)} (${_esc(st.wire)})
            </button>`;
          })
        ].join('');

        // Unified Ringkasan Seluruh Alur (1-2-3 sekaligus terlihat ringkas!)
        const summaryCards = stages.map((st, idx) => {
          const isCut = simRunMode === 'fault' && faultStageIdx === idx;
          const isFocus = activeStageIdx === idx;
          const borderCls = isCut
            ? 'border-rose-500/80 bg-rose-950/35'
            : (isFocus ? 'border-cyan-400 bg-cyan-950/40' : 'border-slate-800 bg-slate-950/85 hover:border-cyan-500/50');
          const clickFn = simRunMode === 'fault' ? `setJb420FaultStage(${idx})` : `setJb420Stage(${idx})`;
          return `
            <button type="button" onclick="${clickFn}" class="text-left rounded-xl border ${borderCls} p-2.5 transition space-y-1">
              <div class="flex items-center justify-between gap-1.5">
                <span class="text-[10px] font-mono font-extrabold ${isCut ? 'text-rose-300' : 'text-cyan-300'}">${isCut ? '💥 TERPUTUS' : `ALUR #${st.step} · ${_esc(st.tag)}`}</span>
                <span class="text-[9.5px] font-mono px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-amber-300">${_esc(st.wire)}</span>
              </div>
              <div class="text-[11.5px] font-bold text-white leading-snug">${_esc(st.title)}</div>
              <p class="text-[10.5px] text-slate-300 leading-relaxed">${_esc(st.desc)}</p>
            </button>`;
        }).join('');

        visualStageHtml = `
          <div class="space-y-3">
            <!-- LIVE COCKPIT CONTROL BAR (3 MODE + SLIDER INTERAKTIF) -->
            <div class="rounded-xl bg-[#040a17] border border-cyan-500/35 p-3 space-y-2.5 shadow-inner">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <div class="flex flex-wrap items-center gap-1.5">
                  ${modeBtn('igon', '🔑 IG ON (Statis)', 'bg-sky-700 text-white border-sky-400 shadow')}
                  ${modeBtn('live', '🔥 Mesin Hidup (Live)', 'bg-emerald-600 text-white border-emerald-400 shadow')}
                  ${modeBtn('fault', '💥 Uji Putus Kabel', 'bg-rose-600 text-white border-rose-400 shadow')}
                </div>
                <span class="text-[10.5px] text-slate-400 font-mono">
                  ${simRunMode === 'fault' ? 'Klik kabel di gambar untuk memutus jalur & lihat DTC!' : 'Seluruh alur menyatu dalam 1 papan sirkuit hidup'}
                </span>
              </div>

              <!-- Interactive Dynamic Slider -->
              <div class="flex flex-col sm:flex-row sm:items-center gap-2 pt-1.5 border-t border-slate-800/90">
                <label for="jb420-sim-slider" class="text-[11px] font-bold text-cyan-300 shrink-0">${_esc(profile.sliderLabel)}:</label>
                <input id="jb420-sim-slider" type="range" min="0" max="100" value="${simSliderVal}"
                       oninput="setJb420SimSlider(this.value)"
                       class="flex-1 accent-cyan-500 cursor-pointer h-2 rounded-lg bg-slate-800" />
                <span id="jb420-sim-slider-val" class="text-[11px] font-mono font-bold px-2.5 py-1 rounded-lg bg-slate-900 border border-cyan-500/40 text-amber-300 shrink-0 text-center">${_esc(profile.sliderValueText)}</span>
              </div>
            </div>

            <!-- ZOOM TOOLBAR PAPAN SIRKUIT (RAMAH MEKANIK SENIOR DI LAYAR HP!) -->
            <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-950/90 border border-slate-800 rounded-xl px-2.5 sm:px-3 py-1.5">
              <span class="text-[10.5px] text-cyan-300 font-semibold flex items-center gap-1.5">
                <i class="fa-solid fa-magnifying-glass-plus text-amber-400"></i>
                <span>Zoom Sirkuit &amp; Pin (Cubit 2 jari / tombol +):</span>
              </span>
              <div class="flex items-center gap-1.5 shrink-0">
                <button type="button" onclick="zoomJb420Unified(-0.35)" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-600 text-white font-bold text-sm" title="Perkecil Sirkuit">−</button>
                <button type="button" id="jb420-unified-zoom-lbl" onclick="resetJb420UnifiedZoom()" class="px-2 h-8 min-w-[46px] rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-600 font-mono text-[11px] text-cyan-300 font-bold" title="Reset ke 100%">${Math.round(unifiedZoom * 100)}%</button>
                <button type="button" onclick="zoomJb420Unified(0.35)" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-600 text-white font-bold text-sm" title="Perbesar Sirkuit">+</button>
                <button type="button" id="btn-jb420-unified-fs" onclick="openAgosSvgZoomModal && openAgosSvgZoomModal('pilar3-unified')" class="px-2.5 h-8 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white text-[11px] font-bold flex items-center gap-1 shadow active:scale-95" title="Buka Simulasi Sirkuit di Layar Penuh">
                  <i class="fa-solid fa-expand"></i>
                  <span>Layar Penuh</span>
                </button>
              </div>
            </div>

            <!-- UNIFIED ALL-IN-ONE INTERACTIVE CIRCUIT CANVAS (BISA DI-ZOOM & PINCH!) -->
            <div id="jb420-unified-svg-wrap" class="agos-zoom-stage rounded-xl" ondblclick="openAgosSvgZoomModal && openAgosSvgZoomModal('pilar3-unified')">${buildUnifiedCircuitSvg(mod)}</div>

            <!-- QUICK SPOTLIGHT / FAULT SELECTOR CHIPS -->
            <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-0.5">${wireFilterChips}</div>

            <!-- RINGKASAN TERPADU SELURUH JALUR (TAMPIL SEMUA SEKALIGUS) -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-2.5">${summaryCards}</div>
          </div>`;
      }
    } else {
      // MODE 2: FOTO WIRING ASLI OEM (HD WebP + Multi-Halaman + Kertas Asli / Blueprint Gelap + Zoom + Layar Penuh!)
      const photos = mod.photos || [];
      const pIdx = Math.min(activePhotoIdx, Math.max(0, photos.length - 1));
      const activePhoto = photos[pIdx];
      const imgUrl = activePhoto ? resolveImgUrl(activePhoto.img) : '';
      const filterStyle = photoTheme === 'blueprint'
        ? 'filter: invert(0.92) hue-rotate(180deg) contrast(1.12) brightness(1.04);'
        : '';
      const frameBg = photoTheme === 'blueprint' ? 'bg-[#071124]' : 'bg-white';

      const pageTabs = photos.length > 1
        ? `<div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1">
            ${photos.map((ph, i) => `
              <button type="button" onclick="setJb420PhotoPage(${i})" class="shrink-0 px-2.5 py-1.5 rounded-lg text-[11px] font-bold border transition ${i === pIdx ? 'bg-amber-500 text-slate-950 border-amber-300' : 'bg-slate-950 text-slate-300 border-slate-700 hover:border-amber-400'}">
                📄 ${_esc(ph.label)}
              </button>
            `).join('')}
          </div>`
        : '';

      visualStageHtml = `
        <div class="space-y-2.5">
          ${pageTabs}
          <!-- Photo Control Toolbar (Zero Overflow on 360px Mobile!) -->
          <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-950/90 border border-slate-800 rounded-xl px-2.5 sm:px-3 py-2">
            <div class="inline-flex rounded-lg border border-slate-700 overflow-hidden text-[11px] font-bold shrink-0">
              <button type="button" onclick="setJb420PhotoTheme('paper')" class="px-2.5 py-1.5 transition ${photoTheme === 'paper' ? 'bg-amber-500 text-slate-950' : 'bg-slate-900 text-slate-300 hover:text-white'}">☀️ Kertas Asli</button>
              <button type="button" onclick="setJb420PhotoTheme('blueprint')" class="px-2.5 py-1.5 transition ${photoTheme === 'blueprint' ? 'bg-cyan-600 text-white' : 'bg-slate-900 text-slate-300 hover:text-white'}">🌙 Blueprint Gelap</button>
            </div>
            <div class="flex flex-wrap items-center gap-1.5">
              <button type="button" onclick="zoomJb420Photo(-0.25)" class="w-8 h-8 sm:w-9 sm:h-9 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-600 text-white font-bold text-sm shrink-0" title="Perkecil">−</button>
              <button type="button" id="jb420-zoom-label" onclick="resetJb420PhotoZoom()" class="px-2 h-8 sm:h-9 min-w-[46px] rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-600 font-mono text-[11px] text-cyan-300 font-bold shrink-0" title="Reset Zoom ke 100%">${Math.round(photoZoom * 100)}%</button>
              <button type="button" onclick="zoomJb420Photo(0.25)" class="w-8 h-8 sm:w-9 sm:h-9 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-600 text-white font-bold text-sm shrink-0" title="Perbesar">+</button>
              <button type="button" onclick="openJb420PhotoFullscreen()" class="px-2.5 sm:px-3 h-8 sm:h-9 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white text-[11px] font-bold flex items-center gap-1.5 shadow shrink-0 active:scale-95">
                <i class="fa-solid fa-expand"></i>
                <span>Layar Penuh</span>
              </button>
            </div>
          </div>

          <!-- OEM Photo Viewport (Mendukung Cubit 2 Jari Pinch-to-Zoom!) -->
          <div id="jb420-oem-photo-viewport" class="rounded-2xl border-2 border-slate-700/90 ${frameBg} overflow-auto max-h-[540px] p-2 sm:p-3 shadow-inner transition-colors touch-pan-x touch-pan-y">
            <img id="jb420-oem-photo-img" src="${_esc(imgUrl)}" alt="${_esc(activePhoto ? activePhoto.label : mod.title)}"
                 onclick="openJb420PhotoFullscreen()"
                 class="mx-auto block rounded-lg cursor-zoom-in transition-transform duration-150 origin-top-left"
                 style="width: ${Math.round(photoZoom * 100)}%; max-width: none; ${filterStyle}" />
          </div>

          <!-- Academic Source Citation -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 text-[11px] text-slate-300 bg-slate-950/90 border border-slate-800 rounded-xl px-3.5 py-2">
            <span><i class="fa-solid fa-book-open text-amber-400 mr-1.5"></i><strong>Sumber Resmi:</strong> Buku Manual Suzuki Grand Vitara JB420 — ${_esc(activePhoto ? activePhoto.source : '')}</span>
            <span class="text-cyan-400 font-semibold shrink-0">Ketuk gambar untuk Layar Penuh</span>
          </div>
        </div>`;
    }

    // Wire-by-Wire Explanation Cards (With Real 2-Color Swatches!)
    const wires = mod.wires || [];
    const dirStyle = {
      power: { cls: 'border-red-500/40 bg-red-950/20', tag: 'POWER +B/+5V', tagCls: 'bg-red-500/20 text-red-300 border-red-500/40' },
      in: { cls: 'border-cyan-500/40 bg-cyan-950/20', tag: 'INPUT SENSOR', tagCls: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40' },
      out: { cls: 'border-amber-500/40 bg-amber-950/20', tag: 'OUTPUT / KONTROL', tagCls: 'bg-amber-500/20 text-amber-300 border-amber-500/40' },
      ground: { cls: 'border-slate-600/60 bg-slate-900/80', tag: 'GROUND / MASSA', tagCls: 'bg-slate-700/60 text-slate-200 border-slate-500/50' }
    };

    const wiresHtml = wires.length ? `
      <div class="space-y-2.5 pt-1">
        <div class="flex items-center justify-between gap-2">
          <h4 class="text-xs font-extrabold uppercase tracking-wider text-cyan-300 flex items-center gap-1.5">
            <i class="fa-solid fa-cable-car text-amber-400"></i>
            Penjelasan Alur Tiap Jalur Kabel &amp; Panduan Ukur Multimeter (${wires.length} Jalur)
          </h4>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-3">
          ${wires.map(w => {
            const ds = dirStyle[w.dir] || dirStyle.in;
            const swatch = window.jb420RenderWireSwatch ? window.jb420RenderWireSwatch(w.colorCode) : _esc(w.colorCode);
            return `
              <div class="rounded-xl border ${ds.cls} p-3.5 space-y-2 hover:border-cyan-400/70 transition">
                <div class="flex flex-wrap items-center justify-between gap-2">
                  ${swatch}
                  <span class="px-2 py-0.5 rounded-md border text-[9.5px] font-extrabold font-mono ${ds.tagCls}">${ds.tag}</span>
                </div>
                <div class="text-xs font-bold text-white flex flex-wrap items-center gap-1.5 font-mono">
                  <span class="text-amber-300">${_esc(w.from)}</span>
                  <i class="fa-solid fa-arrow-right text-cyan-400 text-[10px]"></i>
                  <span class="text-cyan-200">${_esc(w.to)}</span>
                </div>
                <div class="text-[11.5px] font-semibold text-slate-100">${_esc(w.role)}</div>
                <p class="text-[11px] text-slate-300 leading-relaxed">${_esc(w.func)}</p>
                <div class="rounded-lg bg-slate-950/90 border border-slate-800 p-2.5 space-y-1 text-[11px]">
                  <div class="flex justify-between gap-2"><span class="text-slate-400">🔑 Kunci / Kondisi:</span><span class="text-slate-100 font-semibold text-right">${_esc(w.keyState)}</span></div>
                  <div class="flex justify-between gap-2"><span class="text-slate-400">📍 Posisi Probe:</span><span class="text-cyan-200 font-mono text-right">${_esc(w.probe)}</span></div>
                  <div class="flex justify-between gap-2"><span class="text-slate-400">✅ Standar OEM:</span><span class="text-emerald-300 font-mono font-bold text-right">${_esc(w.spec)}</span></div>
                </div>
                <div class="text-[10.5px] text-amber-200/90 bg-amber-950/30 border border-amber-500/30 rounded-lg px-2.5 py-1.5">
                  <strong class="text-amber-300">Tips Lapangan:</strong> ${_esc(w.faultHint)}
                </div>
              </div>`;
          }).join('')}
        </div>
      </div>` : '';

    host.innerHTML = `
      <div class="rounded-2xl bg-[#070e1d] border border-cyan-500/35 p-4 sm:p-5 shadow-2xl space-y-4">
        <!-- Module Header -->
        <div class="flex flex-col lg:flex-row lg:items-start justify-between gap-3 border-b border-slate-800 pb-3.5">
          <div class="space-y-1">
            <div class="flex flex-wrap items-center gap-1.5">
              <span class="px-2 py-0.5 rounded-md bg-cyan-500/15 text-cyan-300 border border-cyan-500/40 font-mono text-[10.5px] font-extrabold">${_esc(mod.badge)}</span>
              ${dtcBadges}
            </div>
            <h3 class="text-base sm:text-lg font-extrabold text-white leading-snug">${_esc(mod.title)}</h3>
            <p class="text-xs text-slate-400">${_esc(mod.subtitle)}</p>
          </div>
          <!-- SAKELAR 2-MODE UTAMA -->
          <div class="grid grid-cols-2 gap-1.5 sm:flex sm:items-center shrink-0">
            <button type="button" id="btn-jb420-mode-flow" onclick="setJb420VisualMode('flow')" class="px-3.5 py-2.5 rounded-xl border text-xs font-extrabold flex items-center justify-center gap-1.5 transition active:scale-95 ${flowBtnCls}">
              <i class="fa-solid fa-bolt"></i>
              <span>${mod.isNonWiring ? 'Alur Cek Mekanis' : 'Simulasi Terpadu'}</span>
            </button>
            <button type="button" id="btn-jb420-mode-photo" onclick="setJb420VisualMode('photo')" class="px-3.5 py-2.5 rounded-xl border text-xs font-extrabold flex items-center justify-center gap-1.5 transition active:scale-95 ${photoBtnCls}">
              <i class="fa-solid fa-image"></i>
              <span>Foto Asli OEM</span>
            </button>
          </div>
        </div>

        ${safetyHtml}
        ${visualStageHtml}
        ${wiresHtml}
      </div>
    `;
    applyUnifiedInlineZoom();
    // Pasang dukungan cubit 2 jari (Pinch-to-Zoom) untuk Simulasi Sirkuit & Foto OEM
    if (typeof window.attachAgosPinchZoom === 'function') {
      const uniWrap = document.getElementById('jb420-unified-svg-wrap');
      if (uniWrap) {
        window.attachAgosPinchZoom(uniWrap, () => unifiedZoom, (s) => {
          unifiedZoom = s;
          applyUnifiedInlineZoom();
        }, 1.0, 3.2);
      }
      const photoVp = document.getElementById('jb420-oem-photo-viewport');
      if (photoVp) {
        window.attachAgosPinchZoom(photoVp, () => photoZoom, (s) => {
          photoZoom = s;
          window.zoomJb420Photo(0);
        }, 0.75, 3.5);
      }
    }
  }

  // Public Global Controls
  window.setJb420Category = function (cat) {
    activeCategory = cat;
    updateCategoryButtons();
    renderModuleSelector();
    renderActiveModuleStage();
  };

  window.filterJb420Atlas = function () {
    const items = getFilteredModules();
    const q = (document.getElementById('jb420-atlas-search')?.value || '').trim();
    if (q && items.length) {
      activeModuleId = items[0].id;
      activePhotoIdx = 0;
      activeStageIdx = -1;
      faultStageIdx = 0;
    }
    renderModuleSelector();
    renderActiveModuleStage();
  };

  window.selectJb420Module = function (modId, forceVisualMode = '', forcePhotoIdx = 0) {
    const atlas = getAtlas();
    const found = atlas.find(m => m.id === modId);
    if (!found) return;
    activeModuleId = found.id;
    activeCategory = found.category;
    const maxPIdx = Math.max(0, (found.photos ? found.photos.length : 1) - 1);
    activePhotoIdx = Math.min(maxPIdx, Math.max(0, Number(forcePhotoIdx) || 0));
    activeStageIdx = -1;
    faultStageIdx = 0;
    simRunMode = 'live';
    simSliderVal = found.id === 'gv_cooling_fan' ? 92 : 35;
    photoZoom = 1.0;
    unifiedZoom = 1.0;
    if (forceVisualMode === 'flow' || forceVisualMode === 'photo') {
      activeVisualMode = forceVisualMode;
    }
    updateCategoryButtons();
    renderModuleSelector();
    renderActiveModuleStage();
  };

  window.setJb420VisualMode = function (mode) {
    activeVisualMode = mode === 'photo' ? 'photo' : 'flow';
    photoZoom = 1.0;
    renderActiveModuleStage();
  };

  window.setJb420Stage = function (idx) {
    if (simRunMode === 'fault') simRunMode = 'live';
    activeStageIdx = (activeStageIdx === idx && idx >= 0) ? -1 : idx;
    renderActiveModuleStage();
  };

  window.setJb420SimMode = function (mode) {
    simRunMode = (mode === 'igon' || mode === 'fault') ? mode : 'live';
    if (simRunMode === 'fault') {
      activeStageIdx = -1;
    }
    renderActiveModuleStage();
  };

  window.setJb420FaultStage = function (idx) {
    simRunMode = 'fault';
    faultStageIdx = Math.max(0, Number(idx) || 0);
    renderActiveModuleStage();
  };

  window.setJb420SimSlider = function (val) {
    simSliderVal = Math.max(0, Math.min(100, Number(val) || 0));
    if (simRunMode === 'igon' && simSliderVal > 0) {
      simRunMode = 'live';
      renderActiveModuleStage();
      return;
    }
    refreshUnifiedSvgOnly();
  };

  window.setJb420PhotoPage = function (idx) {
    activePhotoIdx = idx;
    photoZoom = 1.0;
    renderActiveModuleStage();
  };

  window.setJb420PhotoTheme = function (theme) {
    photoTheme = theme === 'blueprint' ? 'blueprint' : 'paper';
    renderActiveModuleStage();
    syncFullscreenPhotoModal();
  };

  window.zoomJb420Photo = function (delta) {
    photoZoom = Math.max(0.75, Math.min(3.0, Math.round((photoZoom + delta) * 100) / 100));
    const img = document.getElementById('jb420-oem-photo-img');
    const lbl = document.getElementById('jb420-zoom-label');
    if (img) img.style.width = `${Math.round(photoZoom * 100)}%`;
    if (lbl) lbl.textContent = `${Math.round(photoZoom * 100)}%`;
  };

  window.resetJb420PhotoZoom = function () {
    photoZoom = 1.0;
    window.zoomJb420Photo(0);
  };

  function syncFullscreenPhotoModal() {
    const mod = getActiveModule();
    if (!mod || !mod.photos || !mod.photos.length) return;
    const ph = mod.photos[Math.min(activePhotoIdx, mod.photos.length - 1)];
    const img = document.getElementById('fs-jb420-photo-img');
    const title = document.getElementById('fs-jb420-photo-title');
    const src = document.getElementById('fs-jb420-photo-source');
    const wrap = document.getElementById('fs-jb420-photo-wrap');
    const lbl = document.getElementById('fs-jb420-zoom-label');
    if (img) {
      img.src = resolveImgUrl(ph.img);
      img.style.width = `${Math.round(fsZoom * 100)}%`;
      img.style.filter = photoTheme === 'blueprint'
        ? 'invert(0.92) hue-rotate(180deg) contrast(1.12) brightness(1.04)'
        : 'none';
    }
    if (wrap) {
      wrap.classList.toggle('bg-[#071124]', photoTheme === 'blueprint');
      wrap.classList.toggle('bg-white', photoTheme !== 'blueprint');
    }
    if (title) title.textContent = `${mod.title} — ${ph.label}`;
    if (src) src.textContent = `Sumber Resmi: Buku Manual Suzuki Grand Vitara JB420 — ${ph.source}`;
    if (lbl) lbl.textContent = `${Math.round(fsZoom * 100)}%`;
  }

  window.openJb420PhotoFullscreen = function () {
    fsZoom = 1.0;
    syncFullscreenPhotoModal();
    const modal = document.getElementById('modal-jb420-photo-fullscreen');
    if (modal) modal.classList.remove('hidden');
  };

  window.closeJb420PhotoFullscreen = function () {
    const modal = document.getElementById('modal-jb420-photo-fullscreen');
    if (modal) modal.classList.add('hidden');
  };

  window.zoomJb420Unified = function (delta) {
    unifiedZoom = Math.max(1.0, Math.min(3.2, Math.round((unifiedZoom + delta) * 100) / 100));
    applyUnifiedInlineZoom();
  };

  window.resetJb420UnifiedZoom = function () {
    unifiedZoom = 1.0;
    applyUnifiedInlineZoom();
  };

  window.zoomJb420Fullscreen = function (delta) {
    fsZoom = Math.max(0.75, Math.min(4.0, Math.round((fsZoom + delta) * 100) / 100));
    syncFullscreenPhotoModal();
  };

  window.getJb420FullscreenZoom = function () {
    return fsZoom;
  };

  window.setJb420FullscreenZoomAbs = function (val) {
    fsZoom = Math.max(0.75, Math.min(4.0, Number(val) || 1.0));
    syncFullscreenPhotoModal();
  };

  window.openJb420AtlasByDtc = function (dtcRaw, preferredMode = 'flow') {
    const code = String(dtcRaw || '').toUpperCase().split(/[,\s;]+/).map(s => s.trim()).find(Boolean) || '';
    const atlas = getAtlas();
    let hit = null;
    if (code) {
      hit = atlas.find(m => (m.dtcs || []).some(d => d.toUpperCase() === code));
      if (!hit) {
        if (/^P030[0-4]$/.test(code)) hit = atlas.find(m => m.id === 'gv_ign_coil');
        else if (/^P017[12]$|^P219[56]$/.test(code)) hit = atlas.find(m => m.id === 'gv_nonwiring_p0171');
        else if (/^P0420$/.test(code)) hit = atlas.find(m => m.id === 'gv_nonwiring_p0420');
        else if (/^P040[1-3]$|^P0443$|^P0660$/.test(code)) hit = atlas.find(m => m.id === 'gv_egr_evap_imtv');
        else if (/^P07|^P1603$/.test(code)) hit = atlas.find(m => m.id === 'gv_mod_tcm');
        else if (/^C10/.test(code)) hit = atlas.find(m => m.id === 'gv_mod_abs');
        else if (/^B10/.test(code)) hit = atlas.find(m => m.id === 'gv_mod_srs');
        else if (/^B15/.test(code)) hit = atlas.find(m => m.id === 'gv_mod_hvac');
        else if (/^B11/.test(code)) hit = atlas.find(m => m.id === 'gv_mod_bcm');
        else if (/^P16[1-3]/.test(code)) hit = atlas.find(m => m.id === 'gv_mod_icm');
        else if (/^U10|^U11|^P167|^P168/.test(code)) hit = atlas.find(m => m.id === 'gv_can_bus');
      }
    }
    if (typeof window.switchTab === 'function') {
      window.switchTab('manuals');
    }
    if (hit) {
      window.selectJb420Module(hit.id, preferredMode);
    } else {
      window.setJb420VisualMode(preferredMode);
    }
    const el = document.getElementById('jb420-cockpit-atlas');
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  function initJb420Cockpit() {
    if (!document.getElementById('jb420-cockpit-atlas')) return;
    updateCategoryButtons();
    renderModuleSelector();
    renderActiveModuleStage();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initJb420Cockpit);
  } else {
    initJb420Cockpit();
  }
})();
