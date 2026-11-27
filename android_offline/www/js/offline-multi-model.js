/**
 * AGOS Smart Diagnostik — Offline Multi-Model, Engine Catalog (Asia/Eropa/China),
 * Modern DTC (Diesel/Turbo/VVT/Hybrid/EV), Adaptive Live Data & Admin PIN Module
 * ==============================================================================
 * Menyamakan 100% logika backend FastAPI ke dalam APK Android Offline.
 */
(function (global) {
  'use strict';

  const KEY_CUSTOM_PACKS = 'agos_offline_custom_manual_packs_v1';
  const KEY_ADMIN_PIN = 'agos_offline_workshop_pin_v1';
  const DEFAULT_PIN = '1234';
  const _packLoadPromises = {};

  function normCode(raw) {
    return String(raw || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
  }

  function getGenerations() {
    return (global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.vehicle_generations) || [];
  }

  function getEngineDirectory() {
    return (global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.engine_directory) || [];
  }

  function getModernDtcCatalog() {
    return (global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.modern_dtc_catalog) || {};
  }

  function getLocalStoragePacks() {
    try {
      const raw = global.localStorage.getItem(KEY_CUSTOM_PACKS);
      const parsed = raw ? JSON.parse(raw) : [];
      return Array.isArray(parsed) ? parsed : [];
    } catch (_) {
      return [];
    }
  }

  function getBundledPackSummaries() {
    if (global.AGOS_OFFLINE_DATA && Array.isArray(global.AGOS_OFFLINE_DATA.custom_manual_pack_summaries)) {
      return global.AGOS_OFFLINE_DATA.custom_manual_pack_summaries;
    }
    const legacy = (global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.custom_manual_packs) || [];
    return Array.isArray(legacy) ? legacy.map((p) => ({
      pack_id: String(p.pack_id || ''),
      brand: String(p.brand || ''),
      brand_aliases: Array.isArray(p.brand_aliases) ? p.brand_aliases : [],
      model: String(p.model || ''),
      model_aliases: Array.isArray(p.model_aliases) ? p.model_aliases : [],
      generation_id: p.generation_id || null,
      generation_label: String(p.generation_label || p.model || ''),
      year_start: Number(p.year_start || 2010),
      year_end: Number(p.year_end || 2026),
      engine_codes: Array.isArray(p.engine_codes) ? p.engine_codes : [],
      title: String(p.title || 'Manual Tambahan Bengkel'),
      dtc_count: Array.isArray(p.dtc_catalog) ? p.dtc_catalog.length : 0,
      pinout_count: Array.isArray(p.wiring_pinouts) ? p.wiring_pinouts.length : 0,
      sensor_spec_count: Array.isArray(p.sensor_specs) ? p.sensor_specs.length : 0,
      is_builtin: false
    })) : [];
  }

  function getLoadedPackSync(packId) {
    const pid = String(packId || '').trim();
    if (!pid) return null;
    const localMatch = getLocalStoragePacks().find((p) => String(p.pack_id || '') === pid);
    if (localMatch) return localMatch;
    if (global.AGOS_PACK_STORE && global.AGOS_PACK_STORE[pid]) {
      return global.AGOS_PACK_STORE[pid];
    }
    const legacy = (global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.custom_manual_packs) || [];
    if (Array.isArray(legacy)) {
      const hit = legacy.find((p) => String(p.pack_id || '') === pid);
      if (hit) return hit;
    }
    return null;
  }

  function ensureOfflinePackLoaded(packId) {
    const pid = String(packId || '').trim();
    if (!pid || pid === 'suzuki_jb420_builtin' || pid === 'universal') {
      return Promise.resolve(null);
    }
    const existing = getLoadedPackSync(pid);
    if (existing) return Promise.resolve(existing);
    if (_packLoadPromises[pid]) return _packLoadPromises[pid];

    const summaryExists = getBundledPackSummaries().some((s) => String(s.pack_id || '') === pid);
    if (!summaryExists || typeof document === 'undefined') {
      return Promise.resolve(null);
    }

    _packLoadPromises[pid] = new Promise((resolve) => {
      const script = document.createElement('script');
      script.src = `data/packs/${encodeURIComponent(pid)}.js`;
      script.async = true;
      script.onload = () => {
        resolve((global.AGOS_PACK_STORE && global.AGOS_PACK_STORE[pid]) || null);
      };
      script.onerror = () => {
        delete _packLoadPromises[pid];
        resolve(null);
      };
      (document.head || document.documentElement).appendChild(script);
    });
    return _packLoadPromises[pid];
  }

  function loadCustomPacks() {
    const merged = new Map();
    if (global.AGOS_PACK_STORE) {
      Object.values(global.AGOS_PACK_STORE).forEach((p) => {
        if (p && p.pack_id) merged.set(p.pack_id, p);
      });
    }
    const legacy = (global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.custom_manual_packs) || [];
    if (Array.isArray(legacy)) {
      legacy.forEach((p) => { if (p && p.pack_id) merged.set(p.pack_id, p); });
    }
    getLocalStoragePacks().forEach((p) => {
      if (p && p.pack_id) merged.set(p.pack_id, p);
    });
    return Array.from(merged.values());
  }

  function buildCuratedPackComponents(pack, engineFilter) {
    const pinouts = Array.isArray(pack.wiring_pinouts) ? pack.wiring_pinouts : [];
    const specs = Array.isArray(pack.sensor_specs) ? pack.sensor_specs : [];
    const dtcs = Array.isArray(pack.dtc_catalog) ? pack.dtc_catalog : [];
    const engNorm = normCode(engineFilter || '');

    const matchesEng = (txt) => {
      if (!engNorm || engNorm.length < 3) return true;
      return normCode(txt).includes(engNorm);
    };

    let fPins = engNorm ? pinouts.filter((p) => matchesEng(`${p.pin || ''} ${p.signal || ''} ${p.function || ''}`)) : pinouts;
    let fSpecs = engNorm ? specs.filter((s) => matchesEng(`${s.sensor_name || ''} ${s.pin_configuration || ''}`)) : specs;
    if (engNorm && !fPins.length) fPins = pinouts;
    if (engNorm && !fSpecs.length) fSpecs = specs;

    const isDieselEng = engNorm && /(1kd|2kd|1gd|2gd|d13a|2l|3l)/i.test(engNorm);
    const engLabel = (engineFilter && String(engineFilter).trim()) || (pack.engine_codes || []).join(' / ') || pack.model;

    const slotDefs = [
      {
        id: 'coil', anatomy: 'coil',
        label: isDieselEng ? 'Common-Rail & SCV' : 'Koil Pengapian',
        pinPat: isDieselEng ? /\b(pcr\d?|scv|inj|edu|i-?jt|fuel\s*press|common\s*rail)\b/i : /\b(igt\d|igf\d?|coil|koil|ignit|pengapian)\b/i,
        specPat: isDieselEng ? /\b(pcr|scv|rail|injektor|injector|edu)\b/i : /\b(igt|igf|coil|koil|ignit)\b/i,
        dtcPat: isDieselEng ? /^(P008[78]|P0093|P020[1-6]|P1229|P0627)$/ : /^(P030[0-8]|P035[1-8])$/
      },
      {
        id: 'map', anatomy: 'map',
        label: isDieselEng ? 'Sensor Turbo / MAP' : 'Sensor MAP / Vakum',
        pinPat: /\b(pim|vcpm|e2pm|map|manifold|turbo|boost)\b/i,
        specPat: /\b(pim|map|manifold|turbo|boost)\b/i,
        dtcPat: /^(P010[5-9]|P023[4-8]|P0299)$/
      },
      {
        id: 'maf', anatomy: 'maf', label: 'Sensor MAF / Udara',
        pinPat: /\b(vg\b|evg|e2g|maf|mass\s*air|air\s*flow)\b/i,
        specPat: /\b(vg\b|maf|air\s*flow)\b/i,
        dtcPat: /^(P010[0-4]|P017[12])$/
      },
      {
        id: 'throttle', anatomy: 'throttle', label: 'Throttle Body & TPS',
        pinPat: /\b(vta\d?|m\+|m-|me01|etcs|throttle|tps|isc|idle)\b/i,
        specPat: /\b(vta|throttle|tps|etcs|isc)\b/i,
        dtcPat: /^(P012[0-4]|P022[0-3]|P050[57]|P21[013][0-9])$/
      },
      {
        id: 'app', anatomy: 'app', label: 'Sensor Pedal Gas APP',
        pinPat: /\b(vpa\d?|epa\d?|vcp[a2]|pedal|accel|app)\b/i,
        specPat: /\b(vpa|pedal|accel|app)\b/i,
        dtcPat: /^(P212[0-8]|P2138)$/
      },
      {
        id: 'ect', anatomy: 'ect', label: 'Sensor Suhu ECT & IAT',
        pinPat: /\b(thw|tha|ect|iat|coolant|water\s*temp)\b/i,
        specPat: /\b(thw|tha|ect|iat|coolant)\b/i,
        dtcPat: /^(P011[0-9]|P012[58])$/
      },
      {
        id: 'ckp', anatomy: 'ckp', label: 'Sensor CKP, CMP & VVT',
        pinPat: /\b(ne[+-]|g2[+-]|ckp|cmp|crank|cam|oc[v1][+-]?|vvt)\b/i,
        specPat: /\b(ne[+-]|g2|ckp|cmp|crank|cam|ocv|vvt)\b/i,
        dtcPat: /^(P033[5-9]|P034[0-5]|P001[0-6])$/
      },
      {
        id: 'o2', anatomy: 'o2', label: 'Sensor Oksigen O2 / A-F',
        pinPat: /\b(ox\d|ht\d|a1a|ha1a|o2|ho2s|oxygen|a\/f)\b/i,
        specPat: /\b(ox\d|ht\d|a1a|o2|ho2s|oxygen|a\/f)\b/i,
        dtcPat: /^(P003[0-8]|P013[0-9]|P014[01]|P219[56]|P223[78])$/
      },
      {
        id: 'injector', anatomy: 'coil', label: 'Injektor Bahan Bakar',
        pinPat: /#\d0\b|\b(inj\d|injektor|injector)\b/i,
        specPat: /#\d0\b|\b(inj|injektor|injector)\b/i,
        dtcPat: /^(P020[1-6]|P017[12])$/
      },
      {
        id: 'fan', anatomy: 'fan', label: 'Kipas Radiator & AC',
        pinPat: /\b(fan\d?|rfc|ac1|act|mrel|kipas|radiator|cooling\s*fan)\b/i,
        specPat: /\b(fan|kipas|radiator|ac)\b/i,
        dtcPat: /^(P048[0-5]|P053[0-3])$/
      }
    ];

    const curated = [];
    let mapReference = null;

    slotDefs.forEach((slot) => {
      const mPins = [];
      const seenPin = new Set();
      for (const p of fPins) {
        const hay = `${p.pin || ''} ${p.signal || ''} ${p.function || ''}`;
        if (slot.pinPat.test(hay)) {
          const pk = String(p.pin || '').trim();
          if (pk && !seenPin.has(pk)) {
            seenPin.add(pk);
            mPins.push(p);
            if (mPins.length >= 6) break;
          }
        }
      }
      const mSpecs = [];
      const seenSp = new Set();
      for (const s of fSpecs) {
        const hay = `${s.sensor_name || ''} ${s.pin_configuration || ''}`;
        if (slot.specPat.test(hay)) {
          const sk = String(s.sensor_name || '').trim();
          if (sk && !seenSp.has(sk)) {
            seenSp.add(sk);
            mSpecs.push(s);
            if (mSpecs.length >= 4) break;
          }
        }
      }
      if (!mPins.length && !mSpecs.length) return;

      const relDtcs = [];
      for (const d of dtcs) {
        const c = String(d.code || '').toUpperCase();
        if (c && slot.dtcPat.test(c) && !relDtcs.includes(c)) {
          relDtcs.push(c);
          if (relDtcs.length >= 5) break;
        }
      }

      if (slot.id === 'map') {
        const sp0 = mSpecs[0] || {};
        const p0 = mPins[0] || {};
        mapReference = {
          engine: engLabel,
          pin_hint: sp0.pin_configuration || (p0.pin ? `${p0.pin} (${p0.signal || ''})` : ''),
          voltage_idle: sp0.voltage_idle || p0.function || 'Idle ~0.9–1.5V | KOEO ~3.8–4.3V',
          voltage_wot: sp0.voltage_wot || '-'
        };
      }

      curated.push({
        id: slot.id,
        anatomy_type: slot.anatomy,
        short_label: slot.label,
        engine_label: engLabel,
        dtcs: relDtcs.length ? relDtcs.join(', ') : 'Lihat Pencarian Manual',
        pins: mPins,
        specs: mSpecs
      });
    });

    return { curated, mapReference };
  }

  function getPackDetailById(packId, engineFilter) {
    const pid = String(packId || '').trim();
    if (pid === 'suzuki_jb420_builtin') {
      return {
        pack_id: 'suzuki_jb420_builtin',
        brand: 'Suzuki',
        model: 'Grand Vitara',
        generation_id: 'suzuki_jb420',
        generation_label: 'Grand Vitara Gen 2 (JB420)',
        year_start: 2006,
        year_end: 2015,
        engine_codes: ['J20A'],
        title: 'Buku Pedoman Resmi Suzuki Grand Vitara JB420 (Vol 1 & Vol 2)',
        is_builtin: true,
        dtc_count: 207,
        pinout_count: 251,
        sensor_spec_count: 9,
        popular_dtcs: ['P0480', 'C1021', 'P0756', 'B1502', 'B1017', 'B1133', 'P1614', 'KLS-11'],
        curated_components: [],
        map_reference: null,
        wiring_pinouts: [],
        sensor_specs: []
      };
    }
    const pack = getLoadedPackSync(pid);
    if (!pack) return null;
    const dtcs = Array.isArray(pack.dtc_catalog) ? pack.dtc_catalog : [];
    const codeSet = new Set(dtcs.map((d) => String(d.code || '').toUpperCase()));
    const pref = ['P0300', 'P0171', 'P0087', 'P0107', 'P0117', 'P0122', 'P0130', 'P0335', 'P0340', 'P0480', 'P2135', 'P0105', 'P2122'];
    const popular = pref.filter((c) => codeSet.has(c)).slice(0, 8);
    for (const d of dtcs) {
      if (popular.length >= 8) break;
      const c = String(d.code || '').toUpperCase();
      if (c && !popular.includes(c)) popular.push(c);
    }
    const { curated, mapReference } = buildCuratedPackComponents(pack, engineFilter || '');
    return {
      pack_id: String(pack.pack_id || pid),
      brand: String(pack.brand || ''),
      brand_aliases: Array.isArray(pack.brand_aliases) ? pack.brand_aliases : [],
      model: String(pack.model || ''),
      generation_id: pack.generation_id || null,
      generation_label: String(pack.generation_label || pack.model || ''),
      year_start: Number(pack.year_start || 2010),
      year_end: Number(pack.year_end || 2026),
      engine_codes: Array.isArray(pack.engine_codes) ? pack.engine_codes : [],
      selected_engine: String(engineFilter || '').trim() || null,
      title: String(pack.title || 'Manual Tambahan Bengkel'),
      is_builtin: false,
      dtc_count: dtcs.length,
      pinout_count: Array.isArray(pack.wiring_pinouts) ? pack.wiring_pinouts.length : 0,
      sensor_spec_count: Array.isArray(pack.sensor_specs) ? pack.sensor_specs.length : 0,
      popular_dtcs: popular,
      curated_components: curated,
      map_reference: mapReference,
      wiring_pinouts: Array.isArray(pack.wiring_pinouts) ? pack.wiring_pinouts.slice(0, 60) : [],
      sensor_specs: Array.isArray(pack.sensor_specs) ? pack.sensor_specs.slice(0, 25) : []
    };
  }

  function cleanCustomPdfStr(raw) {
    return String(raw || '')
      .replace(/\)\s*\(Page\s+[^)]+\)/gi, '')
      .replace(/an d /g, 'and ')
      .replace(/O FF/g, 'OFF')
      .replace(/di sconnect/g, 'disconnect')
      .replace(/re lay/g, 'relay')
      .replace(/\s{2,}/g, ' ')
      .trim();
  }

  function askCustomPackRag(packId, queryText, engineCode) {
    const pack = getLoadedPackSync(packId);
    if (!pack) return null;
    const q = String(queryText || '').trim();
    const qLow = q.toLowerCase();
    const obdCodes = (q.toUpperCase().match(/\b[PCBU][0-9A-F]{4}\b/g) || []);
    const toyotaTwoPart = (q.toUpperCase().match(/\b[0-9]{2}-[0-9A-F]{2}\b/g) || []);
    const detected = [...new Set([...obdCodes, ...toyotaTwoPart])];
    const dtcs = Array.isArray(pack.dtc_catalog) ? pack.dtc_catalog : [];
    let specs = Array.isArray(pack.sensor_specs) ? pack.sensor_specs : [];
    let pinouts = Array.isArray(pack.wiring_pinouts) ? pack.wiring_pinouts : [];
    const engNorm = normCode(engineCode || '');
    if (engNorm && engNorm.length >= 3) {
      const fSpecs = specs.filter((sp) => normCode(sp.sensor_name || '').includes(engNorm));
      if (fSpecs.length) specs = fSpecs;
      const fPins = pinouts.filter((pw) => normCode(`${pw.pin || ''} ${pw.signal || ''}`).includes(engNorm));
      if (fPins.length) pinouts = fPins;
    }
    const title = String(pack.title || `${pack.brand} ${pack.model}`);
    const parts = [];

    if (/\bmaf\b|mass air flow/i.test(qLow) && (pack.engine_codes || []).some((e) => String(e).toUpperCase() === 'K14B')) {
      parts.push(`[CATATAN ARSITEKTUR MESIN — ${title}]\n• Mesin Suzuki K14B TIDAK memakai MAF Sensor.\n• K14B menggunakan Speed-Density berbasis MAP Sensor (C01-29 / C01-2 / C01-20) & IAT Sensor (C01-34 / C01-20).`);
    }

    const byCode = new Map(dtcs.map((d) => [String(d.code || '').toUpperCase(), d]));
    const matched = [];
    detected.forEach((c) => { if (byCode.has(c)) matched.push(byCode.get(c)); });
    const toks = qLow.replace(/[^a-z0-9\s-]/g, ' ').split(/\s+/).filter((t) => t.length >= 2);
    if (!matched.length && toks.length) {
      dtcs.forEach((d) => {
        const hay = `${d.code} ${d.description_id} ${d.common_causes}`.toLowerCase();
        if (toks.some((t) => hay.includes(t)) && matched.length < 3) matched.push(d);
      });
    }

    matched.slice(0, 4).forEach((cd) => {
      const steps = (cd.repair_steps || []).slice(0, 5).map((s) => `  ${cleanCustomPdfStr(s)}`).join('\n');
      parts.push(
        `[BUKU MANUAL RESMI: ${title} — DTC ${cd.code} (${cd.severity_level || 'HIGH'})]\n` +
        `• Deskripsi: ${cleanCustomPdfStr(cd.description_id)}\n` +
        `• Penyebab: ${cleanCustomPdfStr(cd.common_causes)}\n` +
        `• Langkah Pemeriksaan:\n${steps || '  Ikuti prosedur manual resmi.'}`
      );
      if (Array.isArray(cd.standard_specs) && cd.standard_specs.length) {
        parts.push(`[SPESIFIKASI STANDAR — DTC ${cd.code}]\n` + cd.standard_specs.slice(0, 5).map((s) => `• ${s.parameter}: ${s.normal_range}`).join('\n'));
      }
      if (Array.isArray(cd.wiring_pinout) && cd.wiring_pinout.length) {
        parts.push(`[JALUR WIRING & PINOUT RESMI — DTC ${cd.code}]\n` + cd.wiring_pinout.slice(0, 8).map((p) => `• ${p.pin}: ${p.signal} — ${p.function}`).join('\n'));
      }
    });

    const expToks = new Set(toks);
    if (/\bmaf\b/i.test(qLow)) { expToks.add('map'); expToks.add('iat'); }
    if (/koil|coil/i.test(qLow)) { expToks.add('coil'); expToks.add('koil'); expToks.add('igt'); }
    if (/kipas|fan/i.test(qLow)) { expToks.add('kipas'); expToks.add('fan'); }
    if (/throttle|tps/i.test(qLow)) { expToks.add('tps'); expToks.add('throttle'); expToks.add('vta'); }
    if (/pedal|app/i.test(qLow)) { expToks.add('app'); expToks.add('vpa'); }

    const mSpecs = specs.filter((sp) => {
      const h = `${sp.sensor_name} ${sp.pin_configuration} ${sp.voltage_idle}`.toLowerCase();
      return Array.from(expToks).some((t) => h.includes(t));
    });
    mSpecs.slice(0, 2).forEach((sp) => {
      parts.push(
        `[SPESIFIKASI SENSOR RESMI — ${sp.sensor_name}]\n` +
        `• Pinout: ${sp.pin_configuration}\n` +
        `• Idle/KOEO: ${sp.voltage_idle}\n` +
        `• Kerja/WOT: ${sp.voltage_wot}\n` +
        `• Tahanan/Suplai: ${sp.resistance_ohm}`
      );
    });

    if (!matched.length && pinouts.length && expToks.size) {
      const rPins = pinouts.filter((p) => {
        const h = `${p.pin} ${p.signal} ${p.function}`.toLowerCase();
        return Array.from(expToks).some((t) => h.includes(t));
      });
      if (rPins.length) {
        parts.push(`[PINOUT KONEKTOR ECM RESMI — ${pack.brand} ${pack.model}${engineCode ? ' (' + engineCode + ')' : ''}]\n` + rPins.slice(0, 10).map((p) => `• ${p.pin}: ${p.signal} — ${p.function}`).join('\n'));
      }
    }

    return {
      query: q,
      detected_dtc_codes: detected,
      synthesized_guidance: parts.length
        ? parts.join('\n\n')
        : `Kata kunci '${q}' belum ditemukan pada buku manual ${title}. Coba cari kode P0300, P0171, P0107, P0117, P0122, P0130, P0335, P0480, P2135 atau koil, map, tps, app, ect, ckp, o2, kipas.`,
      matched_dtc_details: [],
      matched_sensor_specs: [],
      matched_wiring_diagrams: [],
      matched_manual_sections: []
    };
  }

  function saveCustomPack(packData) {
    const localPacks = getLocalStoragePacks();
    const copy = { ...packData };
    if (!copy.pack_id) {
      const sb = String(copy.brand || 'custom').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
      const sm = String(copy.model || 'model').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
      copy.pack_id = `${sb}_${sm}_${copy.year_start || 2015}_${copy.year_end || 2026}`;
    }
    const updated = localPacks.filter((p) => p.pack_id !== copy.pack_id);
    updated.push(copy);
    try {
      global.localStorage.setItem(KEY_CUSTOM_PACKS, JSON.stringify(updated));
    } catch (_) {}
    global.AGOS_PACK_STORE = global.AGOS_PACK_STORE || {};
    global.AGOS_PACK_STORE[copy.pack_id] = copy;
    return copy;
  }

  function deleteCustomPack(packId) {
    if (packId === 'suzuki_jb420_builtin') return false;
    const localPacks = getLocalStoragePacks();
    const filtered = localPacks.filter((p) => p.pack_id !== packId);
    if (filtered.length === localPacks.length) return false;
    try {
      global.localStorage.setItem(KEY_CUSTOM_PACKS, JSON.stringify(filtered));
    } catch (_) {}
    if (global.AGOS_PACK_STORE && global.AGOS_PACK_STORE[packId]) {
      delete global.AGOS_PACK_STORE[packId];
    }
    return true;
  }

  function listAllPackSummaries() {
    const builtin = {
      pack_id: 'suzuki_jb420_builtin',
      brand: 'Suzuki',
      brand_aliases: ['Suzuki'],
      model: 'Grand Vitara',
      model_aliases: ['Grand Vitara', 'Vitara', 'JB420'],
      generation_id: 'suzuki_jb420',
      generation_label: 'Grand Vitara Gen 2 (JB420)',
      year_start: 2006,
      year_end: 2015,
      engine_codes: ['J20A'],
      title: 'Buku Pedoman Resmi Suzuki Grand Vitara JB420 (Vol 1 & Vol 2)',
      dtc_count: 207,
      pinout_count: 251,
      sensor_spec_count: 9,
      is_builtin: true
    };
    const merged = new Map();
    getBundledPackSummaries().forEach((s) => {
      if (s && s.pack_id) merged.set(s.pack_id, s);
    });
    getLocalStoragePacks().forEach((p) => {
      if (p && p.pack_id) {
        merged.set(p.pack_id, {
          pack_id: String(p.pack_id || ''),
          brand: String(p.brand || ''),
          brand_aliases: Array.isArray(p.brand_aliases) ? p.brand_aliases : [],
          model: String(p.model || ''),
          model_aliases: Array.isArray(p.model_aliases) ? p.model_aliases : [],
          generation_id: p.generation_id || null,
          generation_label: String(p.generation_label || p.model || ''),
          year_start: Number(p.year_start || 2010),
          year_end: Number(p.year_end || 2026),
          engine_codes: Array.isArray(p.engine_codes) ? p.engine_codes : [],
          title: String(p.title || 'Manual Tambahan Bengkel'),
          dtc_count: Array.isArray(p.dtc_catalog) ? p.dtc_catalog.length : 0,
          pinout_count: Array.isArray(p.wiring_pinouts) ? p.wiring_pinouts.length : 0,
          sensor_spec_count: Array.isArray(p.sensor_specs) ? p.sensor_specs.length : 0,
          is_builtin: false
        });
      }
    });
    return [builtin].concat(Array.from(merged.values()));
  }

  // --- ADMIN PIN GUARD (OFFLINE LOCALSTORAGE) ---
  function getStoredPin() {
    try {
      return global.localStorage.getItem(KEY_ADMIN_PIN) || DEFAULT_PIN;
    } catch (_) {
      return DEFAULT_PIN;
    }
  }

  function verifyPin(pin) {
    return Boolean(pin) && String(pin).trim() === getStoredPin();
  }

  function changePin(currentPin, newPin) {
    if (!verifyPin(currentPin)) return { ok: false, status: 401, detail: 'PIN lama salah.' };
    if (!/^\d{4,8}$/.test(String(newPin || '').trim())) {
      return { ok: false, status: 400, detail: 'PIN baru harus berupa 4 sampai 8 digit angka.' };
    }
    try {
      global.localStorage.setItem(KEY_ADMIN_PIN, String(newPin).trim());
    } catch (_) {}
    return { ok: true, message: 'PIN Kepala Bengkel offline berhasil diperbarui.' };
  }

  function getSecurityStatus() {
    const cur = getStoredPin();
    const isDef = cur === DEFAULT_PIN;
    return {
      pin_enabled: true,
      is_default_pin: isDef,
      default_hint: isDef ? 'PIN standar awal: 1234 (segera ubah melalui Mode Admin)' : null
    };
  }

  // --- RESOLUSI KENDARAAN, GENERASI, ALIAS MESIN & GUARDRAIL ---
  function matchesBrandModel(bq, mq, eb, em, aliases, brandAliases) {
    const bLow = String(bq || '').trim().toLowerCase();
    const mLow = String(mq || '').trim().toLowerCase();
    const ebLow = String(eb || '').trim().toLowerCase();
    const emLow = String(em || '').trim().toLowerCase();
    if (!mLow) return false;
    if (bLow) {
      const bPool = [ebLow].concat((brandAliases || []).map((ba) => String(ba || '').trim().toLowerCase())).filter(Boolean);
      const bHit = bPool.some((cand) => cand.includes(bLow) || bLow.includes(cand));
      if (bPool.length && !bHit) return false;
    }
    if (emLow && (emLow.includes(mLow) || mLow.includes(emLow))) return true;
    return (aliases || []).some((al) => {
      const a = String(al || '').toLowerCase();
      return a && (a.includes(mLow) || mLow.includes(a));
    });
  }

  function genMatchesEngine(gen, engineQ) {
    const nq = normCode(engineQ);
    if (!nq || nq.length < 2) return null;
    for (const v of (gen.engine_variants || [])) {
      const cands = [v.code].concat(v.aliases || []);
      for (const c of cands) {
        const nc = normCode(c);
        if (nc && (nq === nc || nq.includes(nc) || nc.includes(nq))) return v;
      }
    }
    return null;
  }

  function findCustomPack(brand, model, year, eng) {
    const summaries = listAllPackSummaries().filter((p) => !p.is_builtin);
    const engNorm = normCode(eng);
    const hasExplicitEng = Boolean(engNorm && (/[a-z]\d{2}[a-z]?|\d[a-z]{2}/.test(engNorm)));
    const scored = [];
    summaries.forEach((p) => {
      const bAliases = Array.isArray(p.brand_aliases) && p.brand_aliases.length ? p.brand_aliases : [p.brand];
      if (!matchesBrandModel(brand, model, p.brand, p.model, p.model_aliases || [p.model], bAliases)) return;
      const pCodes = (p.engine_codes || []).map((ec) => normCode(ec)).filter(Boolean);
      const engMatch = Boolean(engNorm && pCodes.length && pCodes.some((ec) => ec.includes(engNorm) || engNorm.includes(ec)));
      if (hasExplicitEng && pCodes.length && !engMatch) return;
      let yp = 0;
      if (year !== null && year !== undefined && !isNaN(year)) {
        const yrN = Number(year);
        const ys = Number(p.year_start || 1980);
        const ye = Number(p.year_end || 2030);
        if (yrN >= ys && yrN <= ye) yp = 2;
        else if (yrN === ye + 1 && engMatch) yp = 1;
        else return;
      } else {
        yp = engMatch ? 2 : 1;
      }
      const loaded = getLoadedPackSync(p.pack_id);
      scored.push({ score: yp + (engMatch ? 2 : 0), pack: loaded || p });
    });
    if (!scored.length) return null;
    scored.sort((a, b) => b.score - a.score);
    return scored[0].pack;
  }

  function resolveVehicleApplicability(brand, model, year, engineCode) {
    const bClean = String(brand || '').trim();
    const mClean = String(model || '').trim();
    const engClean = String(engineCode || '').trim();
    const yr = (year !== null && year !== undefined && year !== '' && !isNaN(Number(year))) ? Number(year) : null;
    const catalog = getGenerations();

    let modelMatches = catalog.filter((g) => matchesBrandModel(bClean, mClean, g.brand, g.model, g.model_aliases));
    let isReverse = false;
    if (!modelMatches.length && engClean) {
      const bLow = bClean.toLowerCase();
      modelMatches = catalog.filter((g) => genMatchesEngine(g, engClean) && (!bLow || g.brand.toLowerCase().includes(bLow) || bLow.includes(g.brand.toLowerCase())));
      if (modelMatches.length) isReverse = true;
    }

    const yearMatches = (yr !== null && modelMatches.length)
      ? modelMatches.filter((g) => g.year_start <= yr && yr <= g.year_end)
      : [];

    let transitionCandidates = [];
    let matchedModelOptions = [];
    let isTransition = false;
    let chosenGen = null;

    if (isReverse) {
      const pool = yearMatches.length ? yearMatches : modelMatches;
      const seen = new Set();
      pool.forEach((g) => {
        const k = `${g.brand}|${g.model}`.toLowerCase();
        if (seen.has(k)) return;
        seen.add(k);
        matchedModelOptions.push({
          brand: g.brand,
          model: String(g.model).split('/')[0].trim(),
          generation_label: g.generation_label,
          year_range: `${g.year_start}–${g.year_end}`,
          suggested_year: (yr && g.year_start <= yr && yr <= g.year_end) ? yr : Math.min(Math.max(2018, g.year_start), g.year_end)
        });
      });
      chosenGen = pool[0];
    } else if (yearMatches.length) {
      if (yearMatches.length > 1) {
        const ef = yearMatches.filter((g) => engClean && genMatchesEngine(g, engClean));
        if (ef.length === 1) {
          chosenGen = ef[0];
        } else {
          isTransition = true;
          transitionCandidates = yearMatches.map((g) => ({
            generation_id: g.generation_id,
            generation_label: g.generation_label,
            engine_codes: g.engine_codes || [],
            year_range: `${g.year_start}–${g.year_end}`,
            notes: g.notes || ''
          }));
          chosenGen = ef.length ? ef[ef.length - 1] : yearMatches[yearMatches.length - 1];
        }
      } else {
        chosenGen = yearMatches[0];
      }
    } else if (modelMatches.length) {
      let pool = modelMatches;
      if (engClean) {
        const ef = pool.filter((g) => genMatchesEngine(g, engClean));
        if (ef.length) pool = ef;
      }
      if (yr !== null) {
        pool = [...pool].sort((a, b) => Math.min(Math.abs(yr - a.year_start), Math.abs(yr - a.year_end)) - Math.min(Math.abs(yr - b.year_start), Math.abs(yr - b.year_end)));
        chosenGen = pool[0];
      } else {
        chosenGen = pool[pool.length - 1];
      }
    }

    const matchedVar = (chosenGen && engClean) ? genMatchesEngine(chosenGen, engClean) : null;
    const engineChips = chosenGen
      ? (chosenGen.engine_variants || []).map((v) => ({
          code: v.code, cc: v.cc || '', fuel: v.fuel || 'Bensin', desc: v.desc || '', aliases: v.aliases || []
        }))
      : [];
    const region = (chosenGen && chosenGen.region) || 'Asia';

    const hintLow = `${mClean} ${engClean}`.toLowerCase();
    let fuel = 'Bensin';
    if (matchedVar && matchedVar.fuel) fuel = matchedVar.fuel;
    else if (/air ev|binguo|cloud ev|atto 3|dolphin|seal|byd m6|mg4 ev|ioniq|kona electric|leaf|bz4x|ev6|ev9|neta|electric|listrik|\b(?:ev|bev)\b/.test(hintLow)) fuel = 'EV';
    else if (/hybrid|hev|phev|zenix hybrid|e:hev|shvs|eq boost/.test(hintLow)) fuel = 'Hybrid';
    else if (/diesel|solar|2gd|2kd|1gd|1kd|4n15|4d56|d4hb|4ja1|rz4e|crdi|vnt|vrz/.test(hintLow)) fuel = 'Diesel';
    else if (chosenGen && chosenGen.fuel_types && chosenGen.fuel_types.length) fuel = chosenGen.fuel_types[0];

    const isHv = fuel === 'EV' || fuel === 'Hybrid';
    const hvWarn = fuel === 'EV'
      ? 'BAHAYA TEGANGAN TINGGI EV (300V–400V DC): Wajib pakai sarung tangan isolasi 1000V (Class 0), cabut Service Plug, & tunggu 10 menit sebelum menyentuh kabel oranye, inverter, atau kompresor AC (oli wajib POE isolasi, DILARANG oli PAG!).'
      : (fuel === 'Hybrid'
        ? 'PERINGATAN SISTEM HYBRID / MILD-HYBRID (48V–350V DC): Patuhi prosedur keselamatan HV — jangan menyentuh kabel oranye tanpa APD isolasi 1000V & pastikan oli kompresor AC khusus POE/ND-11.'
        : null);

    const effBrand = bClean || (chosenGen ? chosenGen.brand : '');
    const effModel = mClean || (chosenGen ? chosenGen.model : '');
    const customPack = findCustomPack(effBrand, effModel, yr, engClean);

    if (customPack) {
      const genLbl = chosenGen ? chosenGen.generation_label : `${effBrand} ${effModel} (${customPack.year_start}–${customPack.year_end})`;
      const engLbl = matchedVar ? `${matchedVar.code} (${matchedVar.cc} ${matchedVar.fuel})` : ((customPack.engine_codes || []).join(', ') || engClean || '-');
      return {
        appInfo: {
          brand: effBrand || customPack.brand || '',
          model: effModel || customPack.model || '',
          year: yr,
          engine_code: matchedVar ? matchedVar.code : (engClean || engLbl),
          region,
          resolved_fuel_type: fuel,
          is_high_voltage: isHv,
          hv_safety_warning: hvWarn,
          resolved_generation_id: customPack.generation_id || (chosenGen ? chosenGen.generation_id : null),
          resolved_generation_label: genLbl,
          resolved_engine_label: engLbl,
          coverage_level: 'EXACT_OEM_MANUAL',
          is_pinout_verified: true,
          is_transition_year: isTransition,
          transition_candidates: transitionCandidates,
          available_engine_choices: engineChips,
          matched_model_options: matchedModelOptions,
          active_pack_id: String(customPack.pack_id || 'custom'),
          active_manual_source: customPack.title || 'Buku Manual Kustom Bengkel',
          safety_warning_title: isTransition ? `⚠️ Tahun Peralihan ${yr}: Konfirmasi Kode Mesin` : null,
          safety_warning_desc: isTransition ? `Tahun ${yr} adalah masa transisi generasi pada ${effModel}.` : null
        },
        customPack
      };
    }

    const isJb420 = chosenGen && chosenGen.generation_id === 'suzuki_jb420' && (!matchedVar || matchedVar.code === 'J20A') && (yr === null || yr <= 2015);
    if (isJb420) {
      return {
        appInfo: {
          brand: 'Suzuki',
          model: mClean || 'Grand Vitara',
          year: yr,
          engine_code: 'J20A',
          region: 'Asia',
          resolved_fuel_type: 'Bensin',
          is_high_voltage: false,
          hv_safety_warning: null,
          resolved_generation_id: 'suzuki_jb420',
          resolved_generation_label: 'Grand Vitara Gen 2 (JB420)',
          resolved_engine_label: 'J20A (2.0L Bensin)',
          coverage_level: 'EXACT_OEM_MANUAL',
          is_pinout_verified: true,
          is_transition_year: false,
          transition_candidates: [],
          available_engine_choices: engineChips,
          matched_model_options: matchedModelOptions,
          active_pack_id: 'suzuki_jb420_builtin',
          active_manual_source: 'Buku Pedoman Resmi Suzuki Grand Vitara JB420 (Vol 1 & Vol 2)',
          safety_warning_title: null,
          safety_warning_desc: null
        },
        customPack: null
      };
    }

    const dispVehicle = `${effBrand} ${effModel}`.trim() + (yr ? ` (${yr})` : '') || 'Kendaraan Umum';
    const isSuzuki = effBrand.toLowerCase().includes('suzuki') || (chosenGen && chosenGen.brand.toLowerCase() === 'suzuki');
    const genLbl = chosenGen ? chosenGen.generation_label : `${dispVehicle} (Klasifikasi Standar)`;
    const engLbl = matchedVar
      ? `${matchedVar.code} (${matchedVar.cc} ${matchedVar.fuel})`
      : (chosenGen ? (chosenGen.engine_codes || []).join(', ') : (engClean || '-'));

    return {
      appInfo: {
        brand: effBrand,
        model: effModel,
        year: yr,
        engine_code: matchedVar ? matchedVar.code : (engClean || engLbl),
        region,
        resolved_fuel_type: fuel,
        is_high_voltage: isHv,
        hv_safety_warning: hvWarn,
        resolved_generation_id: chosenGen ? chosenGen.generation_id : null,
        resolved_generation_label: genLbl,
        resolved_engine_label: engLbl,
        coverage_level: isSuzuki ? 'SAME_BRAND_REFERENCE' : 'UNIVERSAL_OBD_ONLY',
        is_pinout_verified: false,
        is_transition_year: isTransition,
        transition_candidates: transitionCandidates,
        available_engine_choices: engineChips,
        matched_model_options: matchedModelOptions,
        active_pack_id: 'universal',
        active_manual_source: `Standar Universal OBD-II ${fuel} & Kasus Bengkel (Manual ${dispVehicle} Belum Tersedia)`,
        safety_warning_title: `⚠️ MODE STANDAR UNIVERSAL OBD-II (${dispVehicle.toUpperCase()} · ${region.toUpperCase()} · ${fuel.toUpperCase()})`,
        safety_warning_desc: `Terdeteksi sebagai ${genLbl} (Mesin ${engLbl}). Diagnosa & kode DTC memakai Katalog Universal ${fuel} & kasus bengkel. Manual OEM khusus model ini belum diunggah — cek soket fisik dengan multitester sebelum jumper kabel.`
      },
      customPack: null
    };
  }

  // --- MODERN DTC, FUEL FILTER, ADAPTIVE LIVE DATA & CUTOFF ---
  const EV_FORBIDDEN = ['sensor o2', 'o2 sensor', 'ho2s', 'oksigen', 'a/f sensor', 'sensor a/f', 'busi', 'spark plug', 'koil', 'ignition coil', 'pengapian', 'injektor', 'injector', 'fuel pump', 'pompa bensin', 'bahan bakar', 'bbm', 'katalis', 'catalytic', 'egr', 'evap', 'throttle body', 'trotel', 'pcv', 'selang vakum', 'turbo', 'knalpot', 'exhaust', 'misfire', 'sensor maf', 'sensor map', 'sensor ckp', 'sensor cmp'];
  const DIESEL_FORBIDDEN = ['busi', 'spark plug', 'koil pengapian', 'ignition coil', 'kabel busi', 'pertalite', 'pertamax'];

  function isFuelCompatible(text, fuel) {
    const fl = String(fuel || 'Bensin').toLowerCase();
    const tl = String(text || '').toLowerCase();
    if (fl === 'ev') return !EV_FORBIDDEN.some((k) => tl.includes(k));
    if (fl === 'diesel') return !DIESEL_FORBIDDEN.some((k) => tl.includes(k));
    return true;
  }

  function stripJb420Pins(txt) {
    if (!txt) return txt;
    return String(txt)
      .replace(/\s*\((?:[ECGB]\d{2}-\d{1,2}(?:\s*,\s*[ECGB]\d{2}-\d{1,2})*)\)/g, '')
      .replace(/\b[EC]\d{2}-\d{1,2}\b/g, 'Pin Soket Terkait')
      .replace(/\s{2,}/g, ' ')
      .trim();
  }

  function lookupModernDtc(code, fuelType) {
    const cat = getModernDtcCatalog();
    const c = String(code || '').trim().toUpperCase();
    const entry = cat[c];
    if (!entry) return null;
    if (c === 'P0087' && fuelType !== 'Diesel') return null;
    return entry;
  }

  function evaluateAdaptiveLiveData(req) {
    const out = [];
    const n = (v) => (v !== null && v !== undefined && v !== '' && !isNaN(Number(v))) ? Number(v) : null;
    const rp = n(req.rail_pressure_mpa), bp = n(req.boost_kpa), inj = n(req.inj_feedback_mm3), egr = n(req.egr_pct);
    const soc = n(req.hv_soc_pct), del = n(req.hv_cell_delta_mv), iso = n(req.hv_insulation_mohm), tmp = n(req.hv_temp_c);

    if (rp !== null) {
      if (rp < 22) out.push({ parameter: 'Fuel Rail Pressure', value: `${rp.toFixed(1)} MPa`, status: 'CRITICAL', note: 'Tekanan Common-Rail TERLALU RENDAH (< 22 MPa) — Cek Filter Solar, Masuk Angin, SCV, atau Backleak Injektor.' });
      else if (rp > 195) out.push({ parameter: 'Fuel Rail Pressure', value: `${rp.toFixed(1)} MPa`, status: 'HIGH', note: 'Tekanan Common-Rail TERLALU TINGGI (> 195 MPa) — Cek SCV / Return / Sensor FRP.' });
      else out.push({ parameter: 'Fuel Rail Pressure', value: `${rp.toFixed(1)} MPa`, status: 'NORMAL', note: 'Tekanan Fuel Rail Common-Rail normal (25–190 MPa).' });
    }
    if (bp !== null) {
      if (bp < 95) out.push({ parameter: 'Boost Turbo', value: `${bp.toFixed(0)} kPa`, status: 'HIGH', note: 'Boost di bawah atmosfer — cek filter udara/sensor MAP.' });
      else if (bp > 260) out.push({ parameter: 'Boost Turbo', value: `${bp.toFixed(0)} kPa`, status: 'HIGH', note: 'OVERBOOST (> 260 kPa) — VNT/Wastegate macet (risiko P0234).' });
      else out.push({ parameter: 'Boost Turbo', value: `${bp.toFixed(0)} kPa`, status: 'NORMAL', note: 'Tekanan Boost Turbo normal.' });
    }
    if (inj !== null) {
      if (Math.abs(inj) >= 3.0) out.push({ parameter: 'Koreksi Injektor', value: `${inj >= 0 ? '+' : ''}${inj.toFixed(2)} mm³/st`, status: 'CRITICAL', note: 'Melebihi ±3.0 mm³/st — Injektor aus/mampet/bocor atau kompresi silinder lemah!' });
      else if (Math.abs(inj) >= 2.0) out.push({ parameter: 'Koreksi Injektor', value: `${inj >= 0 ? '+' : ''}${inj.toFixed(2)} mm³/st`, status: 'MEDIUM', note: 'Koreksi mulai melebar — disarankan purging/cek filter solar.' });
      else out.push({ parameter: 'Koreksi Injektor', value: `${inj >= 0 ? '+' : ''}${inj.toFixed(2)} mm³/st`, status: 'NORMAL', note: 'Keseimbangan injektor sehat.' });
    }
    if (egr !== null) {
      out.push({ parameter: 'Posisi EGR', value: `${egr.toFixed(0)}%`, status: egr > 85 ? 'MEDIUM' : 'NORMAL', note: egr > 85 ? 'Bukaan EGR tinggi (> 85%) — waspada katup macet terbuka saat beban penuh.' : 'Bukaan EGR normal.' });
    }
    if (iso !== null) {
      if (iso < 1.0) out.push({ parameter: 'Tahanan Isolasi HV', value: `${iso.toFixed(2)} MOhm`, status: 'CRITICAL', note: 'BAHAYA KEBOCORAN HV (< 1 MOhm)! Wajib APD 1000V — cek kompresor AC (wajib oli POE) & konektor oranye!' });
      else if (iso < 10.0) out.push({ parameter: 'Tahanan Isolasi HV', value: `${iso.toFixed(2)} MOhm`, status: 'HIGH', note: 'Isolasi HV menurun (< 10 MOhm) — cek kelembaban konektor & kompresor AC HV.' });
      else out.push({ parameter: 'Tahanan Isolasi HV', value: `${iso.toFixed(1)} MOhm`, status: 'NORMAL', note: 'Isolasi tegangan tinggi aman (> 10 MOhm).' });
    }
    if (del !== null) {
      if (del >= 150) out.push({ parameter: 'Delta Tegangan Sel HV', value: `${del.toFixed(0)} mV`, status: 'CRITICAL', note: 'CELL IMBALANCE BERAT (≥ 150 mV) — Ada modul/sel baterai HV drop (pemicu P0A80).' });
      else if (del >= 60) out.push({ parameter: 'Delta Tegangan Sel HV', value: `${del.toFixed(0)} mV`, status: 'MEDIUM', note: 'Selisih sel mulai melebar (60–150 mV).' });
      else out.push({ parameter: 'Delta Tegangan Sel HV', value: `${del.toFixed(0)} mV`, status: 'NORMAL', note: 'Keseimbangan sel baterai HV sehat.' });
    }
    if (soc !== null) {
      out.push({ parameter: 'SoC Baterai HV', value: `${soc.toFixed(0)}%`, status: soc < 15 ? 'HIGH' : 'NORMAL', note: soc < 15 ? 'SoC sangat rendah (< 15%) — risiko gagal READY.' : 'Muatan baterai HV memadai.' });
    }
    if (tmp !== null) {
      out.push({ parameter: 'Suhu HV / Inverter', value: `${tmp.toFixed(0)} °C`, status: tmp >= 50 ? 'CRITICAL' : 'NORMAL', note: tmp >= 50 ? 'OVERHEAT SISTEM HV (≥ 50°C) — Cek pompa coolant inverter & kipas baterai!' : 'Suhu sistem HV normal.' });
    }
    return out;
  }

  function extractReqDtcs(raw) {
    const tokens = String(raw || '').toUpperCase().split(/[,;\s/]+/).map((s) => s.trim()).filter(Boolean);
    const out = [];
    tokens.forEach((t) => {
      const m = t.match(/^([PCBU][0-9A-F]{4})(?:[-]?[0-9A-F]{2})?$/);
      const m2 = t.match(/^([0-9]{2}-[0-9A-F]{2})$/);
      const norm = m ? m[1] : (m2 ? m2[1] : null);
      if (norm && !out.includes(norm)) out.push(norm);
    });
    return out;
  }

  function cleanAndDedupePackPins(rawPins, packId) {
    const cleaned = [];
    for (const p of (rawPins || [])) {
      const pinS = String(p && p.pin || '').trim();
      if (!pinS) continue;
      const body = pinS.replace(/^\[[^\]]+\]\s*/, '').trim();
      if (/^\d\s*[-–]\s*\d$/.test(body)) continue;
      if (/\batau\b.*(masa\s*bodi|body\s*ground)/i.test(body)) continue;
      if ((body.match(/\bIGT\d\b/g) || []).length >= 2) continue;
      cleaned.push(p);
    }
    let out = cleaned.length ? cleaned : (rawPins || []);
    const pid = String(packId || '').toLowerCase();
    if (pid.includes('fortuner')) {
      const hasC75 = out.some(x => /\bC7[0-6]-/.test(String(x.pin || '')));
      const hasE10 = out.some(x => /\bE1[01]-/.test(String(x.pin || '')));
      if (hasC75 && hasE10) out = out.filter(x => !/\bE1[01]-/.test(String(x.pin || '')));
    }
    if (pid.includes('yaris_vios')) {
      const hasC20 = out.some(x => /\b(C20|A21)-/.test(String(x.pin || '')));
      const hasC23 = out.some(x => /\b(C23|A20)-/.test(String(x.pin || '')));
      if (hasC20 && hasC23) out = out.filter(x => !/\b(C23|A20)-/.test(String(x.pin || '')));
    }
    return out;
  }

  function selectCustomPackPins(pack, dtcCodes, textHint, engineCode, fuelType) {
    const allPins = Array.isArray(pack && pack.wiring_pinouts) ? pack.wiring_pinouts : [];
    if (!allPins.length) return [];

    const packId = String(pack.pack_id || '').toLowerCase();
    const engNorm = normCode(engineCode || '');
    const isDiesel = String(fuelType || '').toLowerCase() === 'diesel';
    const codeSet = new Set((dtcCodes || []).map((c) => String(c || '').toUpperCase()));
    const hint = String(textHint || '').toLowerCase();

    // Guardrail Diesel: Ertiga D13A tidak memiliki pinout di paket K14B
    if (isDiesel && packId === 'suzuki_ertiga_gen1_2012_2017') return [];

    // Ertiga K14B tidak pakai MAF (Speed-Density MAP + IAT)
    if (packId === 'suzuki_ertiga_gen1_2012_2017' && [...codeSet].some(c => /^P010[0-4]$/.test(c))) {
      return [
        { pin: 'C01-2', signal: 'GRY/RED — Suplai +5V Sensor MAP (K14B tanpa MAF)', function: 'Suplai +4.5–5.5 V IG ON' },
        { pin: 'C01-29', signal: 'RED/BLK — Sinyal Sensor MAP', function: 'Sinyal vakum intake manifold (1.0–1.6 V Idle)' },
        { pin: 'C01-34', signal: 'BLK/YEL — Sinyal Sensor IAT', function: 'Sinyal suhu udara masuk' },
        { pin: 'C01-20', signal: 'GRY/BLU — Massa Sensor MAP & IAT', function: 'Massa referensi sensor (< 0.3 V)' }
      ];
    }

    const isFan = [...codeSet].some((c) => /^P048[0-5]$/.test(c)) || /\b(kipas|cooling\s*fan|radiator\s*fan)\b/i.test(hint);
    let pool = allPins.filter(p => {
      const ps = String(p.pin || '');
      if (/^\[(AUDIO|PARK\s*ASSIST|STARTING|METER|ENGINE\s*IMMOBILIS|A\/T|AIR\s*BAG|SRS|ABS|VSC|CRUISE)/i.test(ps)) return false;
      if (!isFan && /^\[AIR\s*CONDITIONING/i.test(ps)) return false;
      return true;
    });
    if (!pool.length) pool = allPins;

    const hasEngTags = pool.some(p => /\[(1|2|3|4|k3|ej|d13)[a-z0-9\-]{2,}/i.test(String(p.pin || '')));
    if (engNorm && engNorm.length >= 3 && hasEngTags) {
      const engFiltered = pool.filter((p) => normCode(String(p.pin || '')).includes(engNorm));
      if (engFiltered.length) {
        pool = engFiltered;
      } else {
        return []; // Isolasi ketat multi-mesin: jangan bocorkan 3ZR-FE ke mesin lain!
      }
    } else if (isDiesel) {
      const dieselOnly = pool.filter((p) => /\[(1kd|2kd|1gd|2gd|d13a|4d56|4n15)/i.test(String(p.pin || '')));
      if (dieselOnly.length) pool = dieselOnly;
      else if (hasEngTags) return [];
    }

    const pats = [];
    if ([...codeSet].some((c) => /^P030[0-8]$|^P035[1-8]$/.test(c)) || /\b(koil|coil|misfire|pengapian|ignition|busi)\b/i.test(hint)) {
      pats.push(isDiesel ? /\b(pcr\d?|scv|inj|edu|rail|diesel)\b/i : /\b(igt[1-8]|igf\d?|ig[1-4](?!d)|koil\s*pengapian|ignition\s*coil)\b/i);
    } else if ([...codeSet].some((c) => /^P008[78]$|^P0093$/.test(c)) || /\b(common.?rail|scv|pcr|fuel\s*rail)\b/i.test(hint)) {
      pats.push(/\b(pcr\d?|scv|edu|inj|rail|fuel\s*press)\b/i);
    } else if ([...codeSet].some((c) => /^P033[5-9]$/.test(c)) || (/\b(ckp|crankshaft|poros\s*engkol)\b/i.test(hint) && !/\b(cmp|camshaft)\b/i.test(hint))) {
      pats.push(/\b(ne[+-]?|n1[+-]?|ckp|crankshaft|poros\s*engkol)\b/i);
    } else if ([...codeSet].some((c) => /^P034[0-9]$/.test(c)) || /\b(cmp|camshaft|poros\s*nok)\b/i.test(hint)) {
      pats.push(/\b(g2[+-]?(?!-\d)|n2[+-]?|vv1[+-]?|cmp|camshaft|poros\s*nok)\b/i);
    } else if (isFan) {
      pats.push(/\b(fan\d?|fanl|fanh|rfc|kipas\s*radiator|fan\s*radiator|cooling\s*fan)\b/i);
    } else if ([...codeSet].some((c) => /^P011[5-9]$|^P012[58]$/.test(c)) || /\b(ect|coolant|suhu\s*air|water\s*temp|thermostat)\b/i.test(hint)) {
      pats.push(/\b(thw|ethw|ect|coolant|water\s*temp|suhu\s*air)\b/i);
    } else if ([...codeSet].some((c) => /^P010[0-4]$/.test(c)) || /\b(maf|mass\s*air\s*flow)\b/i.test(hint)) {
      pats.push(/\b(vg\b|evg|e2g|maf|mass\s*air\s*flow)\b/i, /\b(vcpm|pim|e2pm|map|tekanan\s*absolut)\b/i);
    } else if ([...codeSet].some((c) => /^P010[5-9]$|^P017[12]$/.test(c)) || /\b(map|vakum|manifold|pim)\b/i.test(hint)) {
      const hasMaf = pool.some(p => /\b(vg\b|evg|e2g|maf)\b/i.test(`${p.pin} ${p.signal}`));
      if (hasMaf && [...codeSet].some(c => /^P017[12]$/.test(c))) pats.push(/\b(vg\b|evg|e2g|maf)\b/i);
      else pats.push(/\b(vcpm|pim|e2pm|map|tekanan\s*absolut)\b/i, /\b(vg\b|evg|e2g|maf)\b/i);
    } else if ([...codeSet].some((c) => /^P003[0-2]$|^P013[0-5]$/.test(c))) {
      if (isDiesel) return [];
      pats.push(/\b(ha1a|a1a[+-]?|ht1a|ox1a|ox1|oxh1|ho2s-1|bank\s*1\s*sensor\s*1|o2\s*depan)\b/i);
    } else if ([...codeSet].some((c) => /^P003[6-8]$|^P013[6-9]$|^P014[01]$/.test(c))) {
      if (isDiesel) return [];
      pats.push(/\b(ht1b|ox1b|ox2|ho2s-2|bank\s*1\s*sensor\s*2|o2\s*belakang)\b/i);
    } else if ([...codeSet].some((c) => /^P012[0-4]$|^P022[0-3]$|^P0507$|^P21[013][0-9]$/.test(c))) {
      pats.push(isDiesel ? /\b(vlu|lusl|diesel\s*throttle)\b/i : /\b(vta\d?|vcta|eta|vth|vc\b|tps|m\+|m-|throttle)\b/i);
    } else if ([...codeSet].some((c) => /^P212[2-9]$|^P2138$/.test(c)) || /\b(pedal|app|vpa)\b/i.test(hint)) {
      pats.push(/\b(vpa\d?|vcpa|vcp2|epa\d?|app|pedal)\b/i);
    }

    if (!pats.length) return [];

    const matched = [];
    const seen = new Set();
    for (const pat of pats) {
      const patSrc = pat.source;
      for (const p of pool) {
        const hay = `${p.pin || ''} ${p.signal || ''} ${p.function || ''}`;
        if (isDiesel && /\b(igt\d|igf|spark|busi|koil|k14b)\b/i.test(hay)) continue;
        if (patSrc.includes('g2') && /\b(ocv|oc1|oil\s*control)\b/i.test(hay)) continue;
        if (patSrc.includes('ne[') && /\b(g2\b|n2[+-]|camshaft|poros\s*nok)\b/i.test(hay)) continue;
        if (patSrc.includes('vta') && /\b(vpa\d?|vcpa|vcp2|epa\d?|pedal\s*akselerator|accelerator\s*pedal|oxygen|oksigen|\bo2\b|e8-2\b)\b/i.test(hay)) continue;
        if (pat.test(hay)) {
          const pk = String(p.pin || '').trim();
          if (pk && !seen.has(pk)) {
            seen.add(pk);
            matched.push(p);
            if (matched.length >= 10) break;
          }
        }
      }
      if (matched.length) break;
    }
    return cleanAndDedupePackPins(matched, packId).slice(0, 6);
  }

  async function enhanceOfflineSearchResultAsync(req, rawRes) {
    const resolved = resolveVehicleApplicability(req.brand, req.model, req.year, req.engine_code);
    let customPack = resolved.customPack;
    if (customPack && customPack.pack_id && !Array.isArray(customPack.dtc_catalog)) {
      const full = await ensureOfflinePackLoaded(customPack.pack_id);
      if (full) customPack = full;
    }
    return enhanceOfflineSearchResult(req, rawRes, resolved.appInfo, customPack);
  }

  function enhanceOfflineSearchResult(req, rawRes, preAppInfo, preCustomPack) {
    let appInfo = preAppInfo;
    let customPack = preCustomPack;
    if (!appInfo) {
      const resv = resolveVehicleApplicability(req.brand, req.model, req.year, req.engine_code);
      appInfo = resv.appInfo;
      customPack = resv.customPack;
    }
    if (customPack && customPack.pack_id && !Array.isArray(customPack.dtc_catalog)) {
      const loaded = getLoadedPackSync(customPack.pack_id);
      if (loaded) customPack = loaded;
    }
    const fuel = appInfo.resolved_fuel_type || 'Bensin';
    const isDiesel = String(fuel).toLowerCase() === 'diesel';
    const adaptiveLive = evaluateAdaptiveLiveData(req);
    const reqCodes = extractReqDtcs(req.dtc);

    // Filter ranked_matches untuk kesesuaian bahan bakar
    const compatMatches = (rawRes.ranked_matches || []).filter((m) =>
      isFuelCompatible(`${m.final_diagnosis} ${m.repair_action} ${m.complaint} ${m.symptom}`, fuel)
    );

    const out = {
      ...rawRes,
      ranked_matches: compatMatches,
      vehicle_applicability: appInfo
    };

    // 1. Cek apakah ada DTC di Custom Pack atau Katalog Modern (Diesel/Turbo/VVT/Hybrid/EV/CAN)
    let matchedModern = null;
    let matchedCustomDtc = null;
    if (reqCodes.length) {
      const firstCode = reqCodes[0];
      if (customPack && Array.isArray(customPack.dtc_catalog)) {
        const cand = customPack.dtc_catalog.find((d) => String(d.code || '').toUpperCase() === firstCode) || null;
        if (cand) {
          const candTxt = `${cand.description_id || ''} ${cand.common_causes || ''} ${(cand.repair_steps || []).join(' ')} ${(cand.wiring_pinout || []).map((w) => w.pin).join(' ')}`;
          const isErtigaK14bOnly = isDiesel && String(customPack.pack_id || '') === 'suzuki_ertiga_gen1_2012_2017' && /\b(k14b|c01-|koil|busi|ignition\s*coil)\b/i.test(candTxt);
          if (!isErtigaK14bOnly && isFuelCompatible(candTxt, fuel)) {
            matchedCustomDtc = cand;
          }
        }
      }
      if (!matchedCustomDtc) {
        const mh = lookupModernDtc(firstCode, fuel);
        const jbExists = global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.dtc_codes &&
          global.AGOS_OFFLINE_DATA.dtc_codes.some((d) => String(d.code || '').toUpperCase() === firstCode);
        if (mh && (fuel === 'Diesel' || fuel === 'EV' || fuel === 'Hybrid' || !jbExists)) {
          matchedModern = mh;
        }
      }
    }

    if (matchedCustomDtc) {
      const c = matchedCustomDtc.code.toUpperCase();
      const effEng = appInfo.engine_code || req.engine_code || '';
      const engNorm = normCode(effEng);
      let dtcPins = Array.isArray(matchedCustomDtc.wiring_pinout) ? [...matchedCustomDtc.wiring_pinout] : [];
      if (engNorm && engNorm.length >= 3 && dtcPins.length) {
        const engFiltered = dtcPins.filter((p) => normCode(p.pin || '').includes(engNorm));
        if (engFiltered.length) {
          dtcPins = engFiltered;
        } else if (dtcPins.some((p) => String(p.pin || '').includes('['))) {
          const smartEngPins = selectCustomPackPins(customPack, [c], `${matchedCustomDtc.description_id || ''} ${matchedCustomDtc.common_causes || ''}`, effEng, fuel);
          if (smartEngPins.length) dtcPins = smartEngPins;
        }
      }
      if (!dtcPins.length) {
        dtcPins = selectCustomPackPins(customPack, [c], `${matchedCustomDtc.description_id || ''} ${matchedCustomDtc.common_causes || ''}`, effEng, fuel);
      }
      if (isDiesel) {
        dtcPins = dtcPins.filter((p) => !/\b(igt\d|igf|koil|busi|k14b|c01-)\b/i.test(`${p.pin} ${p.signal} ${p.function}`));
      }
      dtcPins = cleanAndDedupePackPins(dtcPins, customPack.pack_id);
      const hasVerifiedPins = dtcPins.length > 0;
      out.top_case_code = `MANUAL-${c}`;
      out.top_diagnosis = `${cleanCustomPdfStr(matchedCustomDtc.description_id || c)} (DTC ${c})`;
      out.top_score_percent = 94.0;
      out.top_category_label = 'SANGAT MIRIP';
      out.top_headline = `${out.top_diagnosis} — 94.0% (Paket Manual Kustom Terverifikasi)`;
      out.direct_manual_advice = {
        diagnosis_title: cleanCustomPdfStr(matchedCustomDtc.description_id || c),
        system_category: 'Manual Kustom',
        group_category: customPack.title || 'Manual Kustom',
        manual_book_section: `${customPack.title || 'Manual Kustom'} — Kode ${c}`,
        cause_summary: cleanCustomPdfStr(Array.isArray(matchedCustomDtc.common_causes) ? matchedCustomDtc.common_causes.join('; ') : String(matchedCustomDtc.common_causes || '-')),
        cause_items: [{ category: 'Manual Kustom', detail: cleanCustomPdfStr(String(matchedCustomDtc.common_causes || matchedCustomDtc.description_id || '-')) }],
        repair_options: matchedCustomDtc.repair_options || [{ title: cleanCustomPdfStr((matchedCustomDtc.repair_steps && matchedCustomDtc.repair_steps[0]) || 'Ikuti langkah SOP manual kustom'), tag: 'Manual Kustom', priority: 'UTAMA', why: 'Sesuai paket manual terverifikasi.', verify: 'DTC hilang setelah uji jalan.' }],
        step_by_step_repair: (matchedCustomDtc.repair_steps || []).map(cleanCustomPdfStr),
        sensor_standards: matchedCustomDtc.standard_specs || [],
        wiring_pinout: hasVerifiedPins ? dtcPins : [{ pin: `Soket Komponen ${c}`, signal: `${customPack.brand} ${customPack.model}`, function: 'Pinout rinci kode ini belum terpetakan otomatis — verifikasi soket fisik memakai multitester.' }],
        relearn_reset_steps: [`1. Hapus DTC ${c} via scanner & lakukan test drive.`],
        is_pinout_verified: hasVerifiedPins,
        active_pack_id: appInfo.active_pack_id,
        safety_warning: appInfo.safety_warning_desc,
        hv_safety_warning: appInfo.hv_safety_warning,
        is_low_confidence_fallback: false,
        adaptive_live_findings: adaptiveLive
      };
      return out;
    }

    if (matchedModern) {
      const c = matchedModern.code;
      const causes = String(matchedModern.root_causes || '').split(';').map((s) => s.trim()).filter(Boolean);
      const customPins = customPack
        ? selectCustomPackPins(customPack, [c], `${matchedModern.title_id || ''} ${matchedModern.system_category || ''}`, appInfo.engine_code || req.engine_code, fuel)
        : [];
      const hasVerifiedCustomPins = customPins.length > 0;
      out.top_case_code = `MANUAL-${c}`;
      out.top_diagnosis = `${matchedModern.title_id} (DTC ${c})`;
      out.top_score_percent = 94.0;
      out.top_category_label = 'SANGAT MIRIP';
      out.top_headline = `${out.top_diagnosis} — 94.0% (Katalog Universal ${fuel} / Modern OBD-II)`;
      out.direct_manual_advice = {
        diagnosis_title: matchedModern.title_id,
        system_category: matchedModern.system_category || 'Kelistrikan',
        group_category: `Universal ${fuel}`,
        manual_book_section: hasVerifiedCustomPins
          ? `${customPack.title} + Katalog Modern ${fuel} — Kode ${c}`
          : `Katalog Universal ${fuel} / Modern OBD-II — Kode ${c}`,
        cause_summary: matchedModern.root_causes || '-',
        cause_items: causes.slice(0, 6).map((d, i) => ({ category: i === 0 ? 'Prioritas Utama' : (i === 1 ? 'Kemungkinan Tinggi' : 'Cek Pendukung'), detail: d })),
        repair_options: matchedModern.repair_options || [],
        step_by_step_repair: matchedModern.repair_steps || [],
        sensor_standards: matchedModern.standard_specs || [],
        wiring_pinout: hasVerifiedCustomPins
          ? customPins
          : ((matchedModern.requires_hv_safety || fuel === 'EV')
            ? [{ pin: 'Konektor HV / BMS (Wajib APD 1000V)', signal: 'Baterai HV / Inverter / CAN', function: 'Cek via Scanner BMS & Insulation Tester 500V (Jangan tusuk kabel oranye!)' }]
            : [{ pin: `Soket Komponen ${c}`, signal: `Sirkuit ${matchedModern.system_category} (${fuel})`, function: 'Manual pinout OEM untuk varian mesin ini belum tersedia — ukur fisik dengan multitester.' }]),
        relearn_reset_steps: [`1. Hapus DTC ${c} dengan scanner.`, '2. Lakukan learning/kalibrasi sistem terkait lalu uji jalan.'],
        is_pinout_verified: hasVerifiedCustomPins,
        active_pack_id: hasVerifiedCustomPins ? appInfo.active_pack_id : 'universal',
        safety_warning: hasVerifiedCustomPins ? appInfo.safety_warning_desc : (appInfo.safety_warning_desc || `Catatan: Pinout OEM khusus varian mesin ${appInfo.engine_code || fuel} belum tersedia di paket manual ini — verifikasi soket fisik dengan multitester.`),
        hv_safety_warning: (matchedModern.requires_hv_safety || appInfo.is_high_voltage) ? appInfo.hv_safety_warning : null,
        is_low_confidence_fallback: false,
        adaptive_live_findings: adaptiveLive
      };
      return out;
    }

    // 2. Confidence Cutoff (< 25%) jika tidak ada kecocokan kuat / kompatibel
    const topCompat = compatMatches[0] || null;
    const isManualFromRaw = String(out.top_case_code || '').startsWith('MANUAL-') && isFuelCompatible(out.top_diagnosis, fuel);
    if (!isManualFromRaw && (!topCompat || Number(topCompat.total_score || 0) < 25.0)) {
      const dtcTxt = reqCodes.length ? ` (${reqCodes.join(', ')})` : '';
      const safeTitle = fuel === 'EV'
        ? `Kasus Baru EV / Kode Belum Terpetakan${dtcTxt} — Panduan Pemeriksaan Awal Aman`
        : (fuel === 'Diesel'
          ? `Kasus Baru Diesel / Kode Belum Terpetakan${dtcTxt} — Panduan Pemeriksaan Awal Common-Rail`
          : `Kasus Baru / Kode Belum Terpetakan${dtcTxt} — Panduan Pemeriksaan Awal Sistematis`);
      const safeOpts = fuel === 'EV'
        ? [
            { title: 'Cek Tegangan Aki 12V Aux, Sekering Utama & Scan Modul BMS/VCU', tag: 'Langkah Aman #1', priority: 'UTAMA', why: 'Mayoritas gangguan gagal READY EV berasal dari aki 12V atau komunikasi BMS.', verify: 'Aki 12V ≥ 12.4V & BMS merespons.' },
            { title: 'Periksa Live Data BMS: SoC (%), Delta Sel (mV) & Tahanan Isolasi HV (MOhm)', tag: 'Wajib APD HV 1000V', priority: 'UTAMA', why: 'Mendeteksi cell imbalance atau kebocoran isolasi tegangan tinggi.', verify: 'Delta sel < 50 mV & Isolasi > 10 MOhm.' }
          ]
        : (fuel === 'Diesel'
          ? [
              { title: 'Cek Filter Solar, Masuk Angin & Live Data Fuel Rail Pressure', tag: 'Langkah Utama Diesel', priority: 'UTAMA', why: 'Suplai solar & tekanan common-rail adalah penyebab utama drop tenaga diesel.', verify: 'Tekanan rail idle 30–45 MPa stabil.' },
              { title: 'Periksa Selang Intercooler/Turbo, Kerja VNT & Katup EGR', tag: 'Udara & Turbo', priority: 'SEKUNDER', why: 'Kebocoran boost atau EGR macet memicu asap hitam & ngempos.', verify: 'Jalur boost kedap & EGR responsif.' }
            ]
          : [
              { title: 'Periksa Live Data Sensor Utama (STFT/LTFT, MAP/MAF, ECT, O2) & Aki/Ground', tag: 'Langkah Pertama', priority: 'UTAMA', why: 'Memastikan arah diagnosa berbasis data sebelum mengganti komponen.', verify: 'Pengisian 13.8–14.4V & data sensor wajar.' },
              { title: 'Cek Fisik Konektor, Kebocoran Vakum, Busi/Koil & Tekanan BBM', tag: 'Verifikasi Fisik', priority: 'SEKUNDER', why: 'Menangkap penyebab paling umum di lapangan secara cepat.', verify: 'Mesin normal lalu simpan kasus ke database.' }
            ]);
      out.top_case_code = 'BELUM-TERPETAKAN';
      out.top_diagnosis = safeTitle;
      out.top_score_percent = topCompat ? topCompat.total_score : 0;
      out.top_category_label = 'PERLU PEMERIKSAAN AWAL';
      out.top_headline = `${safeTitle} — Kecocokan historis rendah (${out.top_score_percent}%), gunakan panduan cek awal aman.`;
      out.direct_manual_advice = {
        diagnosis_title: safeTitle,
        system_category: fuel === 'EV' ? 'Kelistrikan' : (fuel === 'Diesel' ? 'Bahan Bakar' : 'Umum'),
        group_category: `Pemeriksaan Awal (${fuel})`,
        manual_book_section: `Mode Pemeriksaan Awal Aman — ${appInfo.resolved_generation_label}`,
        cause_summary: `Belum ada kecocokan kuat (< 25%) pada database lokal untuk ${appInfo.resolved_generation_label}. Lakukan pemeriksaan sistematis sesuai jenis mesin ${fuel}.`,
        cause_items: [{ category: 'Status Database', detail: `Kasus baru / DTC belum terdaftar untuk ${appInfo.resolved_generation_label} (${fuel}).` }],
        repair_options: safeOpts,
        step_by_step_repair: ['1. Baca seluruh DTC & Freeze Frame dari scanner.', `2. Lakukan pemeriksaan dasar aman khusus ${fuel}.`, '3. Setelah sembuh, klik Simpan Kasus agar AI offline mempelajarinya.'],
        sensor_standards: [],
        wiring_pinout: [{ pin: 'Soket Fisik Terkait', signal: `Pengukuran Aman (${fuel})`, function: 'Ukur langsung menggunakan multitester.' }],
        relearn_reset_steps: ['1. Reset DTC setelah perbaikan dan simpan kasus baru.'],
        is_pinout_verified: false,
        active_pack_id: 'universal',
        safety_warning: appInfo.safety_warning_desc,
        hv_safety_warning: appInfo.hv_safety_warning,
        is_low_confidence_fallback: true,
        adaptive_live_findings: adaptiveLive
      };
      return out;
    }

    // 3. Terapkan guardrail wiring & isolasi pinout asli paket kustom (ZERO false verified=True pada fallback JB420!)
    const adv = { ...(out.direct_manual_advice || {}) };
    adv.active_pack_id = appInfo.active_pack_id || 'universal';
    adv.adaptive_live_findings = adaptiveLive;
    adv.hv_safety_warning = appInfo.hv_safety_warning || adv.hv_safety_warning || null;

    if (customPack && appInfo.active_pack_id !== 'suzuki_jb420_builtin') {
      const diagContext = `${adv.diagnosis_title || ''} ${out.top_diagnosis || ''} ${req.complaint || ''} ${req.symptom || ''}`;
      const matchedPackPins = selectCustomPackPins(customPack, reqCodes, diagContext, appInfo.engine_code || req.engine_code, fuel);
      if (matchedPackPins.length) {
        adv.wiring_pinout = matchedPackPins;
        adv.manual_book_section = `${customPack.title || `${customPack.brand} ${customPack.model}`} (Pinout OEM Terverifikasi)`;
        adv.is_pinout_verified = true;
        adv.safety_warning = appInfo.safety_warning_desc;
        adv.repair_options = (adv.repair_options || []).map((o) => ({
          ...o,
          title: stripJb420Pins(o.title),
          why: stripJb420Pins(o.why),
          verify: stripJb420Pins(o.verify)
        }));
        adv.step_by_step_repair = (adv.step_by_step_repair || []).map(stripJb420Pins);
      } else {
        // ZERO kebocoran false verified=True! Jika tidak ada pinout asli utk mesin/BBM ini (mis. Ertiga D13A Diesel), tandai unverified!
        adv.is_pinout_verified = false;
        adv.active_pack_id = 'universal';
        adv.safety_warning = `⚠️ Pinout OEM spesifik untuk ${appInfo.brand} ${appInfo.model} (${appInfo.engine_code || fuel}) pada kasus ini belum tersedia dalam paket manual — diagram di bawah hanya ILUSTRASI UMUM (Ref. JB420), JANGAN jumper sebelum ukur fisik!`;
        adv.repair_options = (adv.repair_options || []).map((o) => ({
          ...o,
          title: stripJb420Pins(o.title),
          why: stripJb420Pins(o.why),
          verify: stripJb420Pins(o.verify)
        }));
        adv.step_by_step_repair = (adv.step_by_step_repair || []).map(stripJb420Pins);
        adv.wiring_pinout = (adv.wiring_pinout || []).map((w) => ({
          ...w,
          function: String(w.function || '').includes('[Contoh Ref') ? w.function : `[Contoh Ref. JB420 — Cek Soket Fisik] ${w.function || ''}`
        }));
      }
    } else if (!appInfo.is_pinout_verified) {
      adv.is_pinout_verified = false;
      adv.safety_warning = appInfo.safety_warning_desc;
      adv.repair_options = (adv.repair_options || []).map((o) => ({
        ...o,
        title: stripJb420Pins(o.title),
        why: stripJb420Pins(o.why),
        verify: stripJb420Pins(o.verify)
      }));
      adv.step_by_step_repair = (adv.step_by_step_repair || []).map(stripJb420Pins);
      adv.wiring_pinout = (adv.wiring_pinout || []).map((w) => ({
        ...w,
        function: String(w.function || '').includes('[Contoh Ref') ? w.function : `[Contoh Ref. JB420 — Cek Soket Fisik] ${w.function || ''}`
      }));
    } else {
      adv.is_pinout_verified = true;
      adv.safety_warning = appInfo.safety_warning_desc;
    }

    // Pastikan 3-tier standards (Statis + Idle + Scanner) selalu terisi di mode offline
    if ((!Array.isArray(adv.idle_standards) || adv.idle_standards.length === 0) && reqCodes.length && global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA.jb420_catalog) {
      const catArr = global.AGOS_OFFLINE_DATA.jb420_catalog.dtc_catalog || global.AGOS_OFFLINE_DATA.jb420_catalog || [];
      const foundCat = Array.isArray(catArr) ? catArr.find((d) => reqCodes.includes(String(d.code || '').toUpperCase())) : null;
      if (foundCat) {
        if (Array.isArray(foundCat.idle_standards) && foundCat.idle_standards.length) adv.idle_standards = foundCat.idle_standards.map((x) => ({ ...x }));
        if (Array.isArray(foundCat.scanner_standards) && foundCat.scanner_standards.length) adv.scanner_standards = foundCat.scanner_standards.map((x) => ({ ...x }));
        if (!adv.sim_circuit_key && foundCat.sim_circuit_key) adv.sim_circuit_key = String(foundCat.sim_circuit_key);
        if (!adv.atlas_module_id && foundCat.atlas_module_id) adv.atlas_module_id = String(foundCat.atlas_module_id);
      }
    }
    if (!Array.isArray(adv.idle_standards) || adv.idle_standards.length === 0) {
      adv.idle_standards = fuel === 'EV'
        ? [
            { parameter: 'Tegangan Aki 12V Aux Saat Mode READY (DC-DC Aktif)', normal_range: '13.6 – 14.5 V', unit: 'V DC' },
            { parameter: 'Tahanan Isolasi Sistem HV (Insulation Tester 500V)', normal_range: '> 10 MΩ (Wajib APD 1000V)', unit: 'MΩ' }
          ]
        : (fuel === 'Diesel'
          ? [
              { parameter: 'Tekanan Common-Rail Bahan Bakar Saat Idle Panas', normal_range: '30 – 45 MPa (300 – 450 bar)', unit: 'MPa' },
              { parameter: 'Putaran Mesin Idle Panas & Pengisian Alternator', normal_range: '700 – 800 RPM · 13.5 – 14.5 V', unit: 'RPM / V' }
            ]
          : [
              { parameter: 'Putaran Mesin Idle Tanpa Beban (Panas Kerja 80–90°C)', normal_range: '650 – 750 ± 50 RPM', unit: 'RPM' },
              { parameter: 'Tegangan Pengisian Alternator Saat Idle', normal_range: '13.5 – 14.5 V (Stabil)', unit: 'V DC' },
              { parameter: 'Vakum Intake Manifold / Tegangan Sensor MAP Saat Idle', normal_range: '24 – 38 kPa (~1.1 – 1.5 V)', unit: 'kPa / V' }
            ]);
    }
    if (!Array.isArray(adv.scanner_standards) || adv.scanner_standards.length === 0) {
      adv.scanner_standards = fuel === 'EV'
        ? [
            { parameter: 'HV BATTERY CELL VOLTAGE DELTA (Live Data BMS)', normal_range: '< 50 mV antar sel', unit: 'mV' },
            { parameter: 'HV BATTERY SOC / SOH & SUHU PACK', normal_range: '20 – 100% · 20 – 45 °C', unit: '% / °C' }
          ]
        : (fuel === 'Diesel'
          ? [
              { parameter: 'FUEL RAIL PRESSURE ACTUAL vs TARGET (Idle)', normal_range: '30 – 45 MPa (Selisih < ±3 MPa)', unit: 'MPa' },
              { parameter: 'INJECTOR FEEDBACK / CORRECTION VOLUME', normal_range: '–2.5 s/d +2.5 mm³/st', unit: 'mm³/st' }
            ]
          : [
              { parameter: 'COOLANT TEMP (ECT · Bab 1A-34 Idle Panas)', normal_range: '80 – 100 °C', unit: '°C' },
              { parameter: 'SHORT FT B1 (STFT) & LONG FT B1 (LTFT · Bab 1A-35)', normal_range: '–10% s/d +10% (Ambang ±20%)', unit: '%' },
              { parameter: 'MAF & MAP Saat Idle Panas (Bab 1A-34/35)', normal_range: '1.0 – 4.0 g/s · 24 – 38 kPa', unit: 'g/s · kPa' }
            ]);
    }

    out.direct_manual_advice = adv;
    return out;
  }

  global.AgosOfflineMultiModel = {
    getGenerations,
    getEngineDirectory,
    getModernDtcCatalog,
    ensureOfflinePackLoaded,
    loadCustomPacks,
    saveCustomPack,
    deleteCustomPack,
    listAllPackSummaries,
    getPackDetailById,
    askCustomPackRag,
    verifyPin,
    changePin,
    getSecurityStatus,
    resolveVehicleApplicability,
    lookupModernDtc,
    enhanceOfflineSearchResult,
    enhanceOfflineSearchResultAsync
  };
})(typeof window !== 'undefined' ? window : globalThis);
