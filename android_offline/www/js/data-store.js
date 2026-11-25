/**
 * AGOS Smart Diagnostik — Offline Data Store (data-store.js)
 * ==========================================================
 * Memuat data bawaan (historical_cases, dtc_codes, wiring_diagrams,
 * sensor_specs, repair_manuals, jb420_catalog) dari bundle offline
 * serta mengelola penambahan/penghapusan kasus di localStorage HP
 * tanpa merusak data bawaan.
 */
(function (global) {
  'use strict';

  const STORAGE_KEY_ADDED = 'agos_offline_added_cases_v1';
  const STORAGE_KEY_DELETED = 'agos_offline_deleted_case_ids_v1';
  const STORAGE_KEY_VERIFIED = 'agos_offline_verified_case_ids_v1';

  let _cache = null;

  async function loadJsonAsset(filename, fallbackKey) {
    if (global.AGOS_OFFLINE_DATA && global.AGOS_OFFLINE_DATA[fallbackKey]) {
      return global.AGOS_OFFLINE_DATA[fallbackKey];
    }
    const resp = await fetch('data/' + filename);
    if (!resp.ok) {
      throw new Error('Gagal memuat ' + filename);
    }
    return await resp.json();
  }

  async function ensureLoaded() {
    if (_cache) return _cache;
    const [
      historical_cases,
      dtc_codes,
      wiring_diagrams,
      sensor_specs,
      repair_manuals,
      jb420_catalog
    ] = await Promise.all([
      loadJsonAsset('historical_cases.json', 'historical_cases'),
      loadJsonAsset('dtc_codes.json', 'dtc_codes'),
      loadJsonAsset('wiring_diagrams.json', 'wiring_diagrams'),
      loadJsonAsset('sensor_specs.json', 'sensor_specs'),
      loadJsonAsset('repair_manuals.json', 'repair_manuals'),
      loadJsonAsset('jb420_catalog.json', 'jb420_catalog')
    ]);

    const dtcCatalogMap = {};
    if (jb420_catalog && Array.isArray(jb420_catalog.dtc_catalog)) {
      jb420_catalog.dtc_catalog.forEach((item) => {
        const c = String(item.code || '').trim().toUpperCase();
        if (c) dtcCatalogMap[c] = item;
      });
    }

    const dtcCodeMap = {};
    (dtc_codes || []).forEach((row) => {
      const c = String(row.code || '').trim().toUpperCase();
      if (c) dtcCodeMap[c] = row;
    });

    _cache = {
      baseCases: Array.isArray(historical_cases) ? historical_cases : [],
      dtcCodes: Array.isArray(dtc_codes) ? dtc_codes : [],
      dtcCodeMap,
      wiringDiagrams: Array.isArray(wiring_diagrams) ? wiring_diagrams : [],
      sensorSpecs: Array.isArray(sensor_specs) ? sensor_specs : [],
      repairManuals: Array.isArray(repair_manuals) ? repair_manuals : [],
      jb420Catalog: jb420_catalog || {},
      dtcCatalogMap
    };
    return _cache;
  }

  function getAddedCases() {
    try {
      const raw = global.localStorage.getItem(STORAGE_KEY_ADDED);
      return raw ? JSON.parse(raw) : [];
    } catch (_) {
      return [];
    }
  }

  function saveAddedCases(list) {
    try {
      global.localStorage.setItem(STORAGE_KEY_ADDED, JSON.stringify(list));
    } catch (_) {}
  }

  function getDeletedIds() {
    try {
      const raw = global.localStorage.getItem(STORAGE_KEY_DELETED);
      return new Set(raw ? JSON.parse(raw) : []);
    } catch (_) {
      return new Set();
    }
  }

  function saveDeletedIds(setObj) {
    try {
      global.localStorage.setItem(STORAGE_KEY_DELETED, JSON.stringify(Array.from(setObj)));
    } catch (_) {}
  }

  function getVerifiedIds() {
    try {
      const raw = global.localStorage.getItem(STORAGE_KEY_VERIFIED);
      return new Set(raw ? JSON.parse(raw) : []);
    } catch (_) {
      return new Set();
    }
  }

  function saveVerifiedIds(setObj) {
    try {
      global.localStorage.setItem(STORAGE_KEY_VERIFIED, JSON.stringify(Array.from(setObj)));
    } catch (_) {}
  }

  async function getAllCases() {
    const data = await ensureLoaded();
    const deleted = getDeletedIds();
    const verifiedOverrides = getVerifiedIds();
    const added = getAddedCases();
    const byCode = new Map();
    data.baseCases.forEach((c) => {
      if (!deleted.has(Number(c.id)) && !deleted.has(String(c.case_code))) {
        const copy = { ...c };
        if (verifiedOverrides.has(Number(copy.id)) || verifiedOverrides.has(String(copy.case_code))) {
          copy.verification_status = 'TERVERIFIKASI';
        } else if (!copy.verification_status) {
          copy.verification_status = 'TERVERIFIKASI';
        }
        byCode.set(String(copy.case_code || copy.id), copy);
      }
    });
    added.forEach((c) => {
      if (!deleted.has(Number(c.id)) && !deleted.has(String(c.case_code))) {
        const copy = { ...c };
        if (verifiedOverrides.has(Number(copy.id)) || verifiedOverrides.has(String(copy.case_code))) {
          copy.verification_status = 'TERVERIFIKASI';
        }
        byCode.set(String(copy.case_code || copy.id), copy);
      }
    });
    const merged = Array.from(byCode.values());
    merged.sort((a, b) => String(a.case_code || '').localeCompare(String(b.case_code || '')));
    return merged;
  }

  async function addCase(payload) {
    const data = await ensureLoaded();
    const added = getAddedCases();

    let caseCode = String(payload.case_code || '').trim().toUpperCase();
    if (!caseCode) {
      let maxNum = 18;
      [...data.baseCases, ...added].forEach((c) => {
        const m = String(c.case_code || '').match(/^K0*(\d+)$/i);
        if (m) {
          const n = parseInt(m[1], 10);
          if (n > maxNum) maxNum = n;
        }
      });
      caseCode = 'K' + String(maxNum + 1).padStart(3, '0');
    }

    const existingIdx = added.findIndex((c) => String(c.case_code || '').toUpperCase() === caseCode);
    const nextId = existingIdx >= 0 ? added[existingIdx].id : (Date.now() + Math.floor(Math.random() * 1000));

    const sysCategory = payload.system_category || 'Udara';
    const pembakaranSet = new Set(['Udara', 'Bahan Bakar', 'Pengapian', 'Mekanis']);
    const groupCategory = pembakaranSet.has(sysCategory) ? 'Pembakaran' : 'Pendukung';
    const verStatus = String(payload.verification_status || 'DRAFT').trim().toUpperCase();

    const newCase = {
      id: nextId,
      case_code: caseCode,
      brand: (payload.brand || 'Umum').trim(),
      model: (payload.model || '-').trim(),
      year: payload.year || null,
      engine_capacity: payload.engine_capacity || '-',
      engine_code: String(payload.engine_code || '').trim().toUpperCase(),
      odometer_km: payload.odometer_km != null && payload.odometer_km !== '' ? Number(payload.odometer_km) : null,
      license_plate: String(payload.license_plate || '').trim().toUpperCase(),
      mechanic_name: String(payload.mechanic_name || '').trim(),
      verification_status: verStatus === 'TERVERIFIKASI' ? 'TERVERIFIKASI' : 'DRAFT',
      complaint: (payload.complaint || '').trim(),
      symptom: (payload.symptom || '').trim(),
      dtc: (payload.dtc || 'Tidak ada').trim() || 'Tidak ada',
      stft: payload.stft ?? null,
      ltft: payload.ltft ?? null,
      rpm: payload.rpm ?? null,
      o2_voltage: payload.o2_voltage || null,
      map_kpa: payload.map_kpa ?? null,
      maf_gps: payload.maf_gps ?? null,
      ect_c: payload.ect_c ?? null,
      inspection_findings: (payload.inspection_findings || '').trim(),
      final_diagnosis: (payload.final_diagnosis || '').trim(),
      repair_action: (payload.repair_action || '').trim(),
      system_category: sysCategory,
      affected_system: payload.affected_system || null,
      group_category: groupCategory,
      manual_book_ref:
        'Buku Pedoman Perbaikan Workshop Manual - Prosedur Servis Standar. Tindakan: ' +
        (payload.repair_action || '-'),
      created_at: new Date().toISOString().slice(0, 10)
    };

    if (existingIdx >= 0) added[existingIdx] = newCase;
    else added.push(newCase);
    saveAddedCases(added);
    return {
      status: 'success',
      id: newCase.id,
      case_code: caseCode,
      verification_status: newCase.verification_status,
      message: `Kasus ${caseCode} (${newCase.brand} ${newCase.model} · Status: ${newCase.verification_status}) tersimpan di perangkat!`,
      case: newCase
    };
  }

  async function verifyCaseById(id) {
    const numId = Number(id);
    const added = getAddedCases();
    const idx = added.findIndex((c) => Number(c.id) === numId);
    let code = String(id);
    if (idx !== -1) {
      added[idx].verification_status = 'TERVERIFIKASI';
      code = added[idx].case_code || code;
      saveAddedCases(added);
    }
    const verSet = getVerifiedIds();
    verSet.add(numId);
    if (code) verSet.add(String(code));
    saveVerifiedIds(verSet);
    return {
      status: 'verified',
      id: numId,
      case_code: code,
      verification_status: 'TERVERIFIKASI',
      message: `Kasus ${code} resmi TERVERIFIKASI Standar Bengkel!`
    };
  }

  async function deleteCaseById(id) {
    const numId = Number(id);
    const added = getAddedCases();
    const idx = added.findIndex((c) => Number(c.id) === numId);
    if (idx !== -1) {
      added.splice(idx, 1);
      saveAddedCases(added);
    } else {
      const deleted = getDeletedIds();
      deleted.add(numId);
      saveDeletedIds(deleted);
    }
    return { message: 'Kasus berhasil dihapus.' };
  }

  global.AgosDataStore = {
    ensureLoaded,
    getAllCases,
    addCase,
    verifyCaseById,
    deleteCaseById
  };
})(typeof window !== 'undefined' ? window : globalThis);
