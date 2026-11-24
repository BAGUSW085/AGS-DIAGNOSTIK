"""
Konverter Resmi Database XML Toyota GSIC (tmc-service-db / tmc-service-inc)
ke Markdown Buku Manual Gabungan (.md) & Paket JSON AGOS Smart Diagnostik (.json)
=================================================================================
Mendukung ekstraksi otomatis dari struktur folder `xmlweb/<pub_id>/repair/`:
1. `pub.xml`          -> Identitas publikasi, model, kode sasis, dan tahun
2. `troubleshoot.xml` -> Peta lengkap kode DTC OBD-II & Flash Code ke dokumen `RM000...xml`
3. `toc_rpr.xml`      -> Daftar isi lengkap bab servis, `TERMINAL ECM/ECU`, `DATA LIST`, `TABEL GEJALA`
4. `contents/rm*.xml` -> Isi lengkap penjelasan DTC, area gangguan, langkah pemeriksaan (<testgrp>),
                         spesifikasi tegangan/tahanan (<spec>), tabel pinout & warna kabel ECM,
                         serta parameter Data List scanner.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
from typing import Any
import xml.etree.ElementTree as ET


def clean_ws(text: str | None) -> str:
    """Membersihkan spasi berlebih dan baris kosong dari teks XML."""
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def elem_text(elem: ET.Element | None) -> str:
    """Mengambil seluruh teks di dalam elemen XML beserta child-nya."""
    if elem is None:
        return ""
    return clean_ws(" ".join(elem.itertext()))


def parse_cals_table(table_elem: ET.Element) -> list[list[str]]:
    """
    Mem-parsing tabel XML Toyota GSIC (format CALS <tgroup>/<thead>/<tbody>/<row>/<entry>)
    lengkap dengan dukungan atribut `morerows` (rowspan) agar kolom simbol terminal,
    warna kabel, dan deskripsi tidak bergeser pada baris multi-kondisi.
    """
    rows_out: list[list[str]] = []
    tgroup = table_elem.find("tgroup")
    if tgroup is None:
        return rows_out

    num_cols = int(tgroup.attrib.get("cols", "5") or "5")
    tbody = tgroup.find("tbody")
    if tbody is None:
        return rows_out

    # Menyimpan sisa rowspan per kolom: col_idx -> [remaining_rows, text_value]
    active_spans: dict[int, list[Any]] = {}

    for row_elem in tbody.findall("row"):
        current_row: list[str] = []
        entries = row_elem.findall("entry")
        entry_idx = 0

        for col_idx in range(num_cols):
            if col_idx in active_spans and active_spans[col_idx][0] > 0:
                current_row.append(active_spans[col_idx][1])
                active_spans[col_idx][0] -= 1
                if active_spans[col_idx][0] <= 0:
                    del active_spans[col_idx]
            elif entry_idx < len(entries):
                ent = entries[entry_idx]
                entry_idx += 1
                val = elem_text(ent)
                current_row.append(val)
                morerows = int(ent.attrib.get("morerows", "0") or "0")
                if morerows > 0:
                    active_spans[col_idx] = [morerows, val]
            else:
                current_row.append("")

        if any(c.strip() for c in current_row):
            rows_out.append(current_row)

    return rows_out


def find_contents_file(contents_dir: Path, rm_id: str) -> Path | None:
    """Mencari file `rm000...xml` di folder `repair/contents` (case-insensitive)."""
    if not rm_id:
        return None
    cand_lower = contents_dir / f"{rm_id.lower()}.xml"
    if cand_lower.exists():
        return cand_lower
    cand_upper = contents_dir / f"{rm_id.upper()}.xml"
    if cand_upper.exists():
        return cand_upper
    return None


def parse_terminal_ecu_doc(
    xml_path: Path, section_name: str
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """
    Mengekstrak tabel `TERMINAL ECM` / `TERMINAL ECU` menjadi:
    1. `wiring_pinouts`: list dict {pin, signal, function}
    2. `sensor_specs`: list dict {sensor_name, pin_configuration, voltage_idle, voltage_wot, resistance_ohm}
    """
    pinouts: list[dict[str, str]] = []
    sensor_specs: list[dict[str, str]] = []
    if not xml_path or not xml_path.exists():
        return pinouts, sensor_specs

    try:
        tree = ET.parse(xml_path)
    except Exception:
        return pinouts, sensor_specs

    engine_tag = (
        section_name.replace("SISTEM KONTROL MESIN", "")
        .replace("KONTROL MESIN", "")
        .replace("ENGINE CONTROL", "")
        .replace("TRANSMISI OTOMATIS", "A/T")
        .replace("TRANSAXLE OTOMATIS", "A/T")
        .replace("AUTOMATIC TRANSMISSION / TRANSAXLE", "A/T")
        .replace("AUTOMATIC TRANSMISSION", "A/T")
        .strip()
    )
    prefix_tag = f"[{engine_tag}] " if engine_tag else ""

    # Kelompokkan baris berdasarkan pasangan terminal (kolom 0)
    grouped_terms: dict[str, dict[str, Any]] = {}
    for table in tree.findall(".//table"):
        rows = parse_cals_table(table)
        for r in rows:
            if len(r) < 5:
                continue
            term_sym, wire_col, desc, cond, std_val = r[0], r[1], r[2], r[3], r[4]
            if not term_sym or term_sym.lower().startswith("simbol"):
                continue
            key = f"{term_sym}|{wire_col}"
            if key not in grouped_terms:
                grouped_terms[key] = {
                    "term": term_sym,
                    "wire": wire_col,
                    "desc": desc,
                    "conditions": [],
                }
            cond_pair = f"{cond}: {std_val}" if cond else std_val
            if cond_pair and cond_pair not in grouped_terms[key]["conditions"]:
                grouped_terms[key]["conditions"].append(cond_pair)

    for info in grouped_terms.values():
        term = info["term"]
        wire = info["wire"] or "-"
        desc = info["desc"] or "-"
        conds = info["conditions"]
        cond_str = " | ".join(conds)

        pin_label = f"{prefix_tag}{term}".strip()
        pinouts.append(
            {
                "pin": pin_label[:90],
                "signal": f"Warna Kabel: {wire} — {desc}"[:140],
                "function": cond_str[:220] or "Sesuai standar manual resmi Toyota",
            }
        )

        # Buat entri sensor_specs untuk sensor/aktuator utama
        desc_low = f"{term} {desc}".lower()
        if any(
            k in desc_low
            for k in (
                "tekanan",
                "manifold",
                "pim",
                "maf",
                "vg",
                "throttle",
                "vta",
                "vth",
                "pedal",
                "vpa",
                "temperatur",
                "thw",
                "tha",
                "crankshaft",
                "camshaft",
                "knock",
                "knk",
                "ocv",
                "oxygen",
                "ox",
                "a/f",
                "a1a",
                "injector",
                "#10",
                "pengapian",
                "igt",
                "ig1",
                "pompa",
                "fc",
                "fpr",
                "starter",
                "sta",
                "baterai",
                "+b",
                "solenoid",
                "canh",
                "canl",
                "rail",
                "scv",
            )
        ):
            v_idle = conds[0] if conds else "-"
            v_wot = conds[1] if len(conds) > 1 else v_idle
            sensor_specs.append(
                {
                    "sensor_name": f"{prefix_tag}{desc} ({term})"[:140],
                    "pin_configuration": f"Terminal: {term} | Warna Kabel: {wire}",
                    "voltage_idle": v_idle[:180],
                    "voltage_wot": v_wot[:180],
                    "resistance_ohm": f"Referensi Manual Resmi Toyota ({section_name})",
                }
            )

    return pinouts, sensor_specs


def parse_data_list_doc(xml_path: Path, section_name: str) -> list[dict[str, str]]:
    """Mengekstrak tabel `DATA LIST / ACTIVE TEST` menjadi tambahan `sensor_specs`."""
    specs: list[dict[str, str]] = []
    if not xml_path or not xml_path.exists():
        return specs
    try:
        tree = ET.parse(xml_path)
    except Exception:
        return specs

    engine_tag = (
        section_name.replace("SISTEM KONTROL MESIN", "")
        .replace("KONTROL MESIN", "")
        .replace("ENGINE CONTROL", "")
        .strip()
    )
    prefix = f"[{engine_tag} Data List] " if engine_tag else "[Data List] "

    for table in tree.findall(".//table"):
        rows = parse_cals_table(table)
        for r in rows:
            if len(r) < 3:
                continue
            item_name, measure_range, normal_cond = r[0], r[1], r[2]
            diag_note = r[3] if len(r) > 3 else "-"
            if not item_name or "display tester" in item_name.lower():
                continue
            specs.append(
                {
                    "sensor_name": f"{prefix}{item_name}"[:140],
                    "pin_configuration": f"Parameter Scanner DLC3: {measure_range}"[:160],
                    "voltage_idle": f"Standar Normal: {normal_cond}"[:180],
                    "voltage_wot": f"Catatan Diagnosa: {diag_note}"[:180],
                    "resistance_ohm": f"Data List Resmi Toyota ({section_name})",
                }
            )
    return specs


def parse_dtc_doc(xml_path: Path, section_name: str, ttl_name: str) -> dict[str, Any]:
    """
    Mem-parsing dokumen `RM000...xml` untuk satu atau beberapa kode DTC:
    - Penjelasan & kondisi deteksi
    - Area Gangguan (`causes`)
    - Langkah pemeriksaan (`repair_steps`) dari `<testgrp>`
    - Spesifikasi multimeter (`standard_specs`) dari `<spec>`
    - Pinout terkait (`wiring_pinout`) yang disebutkan pada langkah pengukuran
    """
    result: dict[str, Any] = {
        "description": "",
        "causes": [],
        "repair_steps": [],
        "standard_specs": [],
        "wiring_pinout": [],
    }
    if not xml_path or not xml_path.exists():
        return result

    try:
        tree = ET.parse(xml_path)
    except Exception:
        return result

    # 1. Ambil penjelasan & tabel kondisi deteksi / area gangguan
    for sub in tree.findall(".//subpara"):
        sname = clean_ws(sub.findtext("name", "")).upper()
        if "PENJELASAN" in sname or "DESCRIPTION" in sname:
            ptxts = [clean_ws(p.text) for p in sub.findall(".//content5/ptxt") if clean_ws(p.text)]
            if ptxts:
                result["description"] = " ".join(ptxts[:2])
            for tbl in sub.findall(".//table"):
                for row in parse_cals_table(tbl):
                    if len(row) >= 3:
                        dtc_no, detect_cond, trouble_area = row[0], row[1], row[2]
                        if trouble_area and "area gangguan" not in trouble_area.lower():
                            result["causes"].append(f"[{section_name}] Area Gangguan: {trouble_area}")
                        if detect_cond and "kondisi" not in detect_cond.lower():
                            result["causes"].append(f"Kondisi Deteksi: {detect_cond[:220]}")

    # 2. Ambil langkah pemeriksaan (<testgrp>) dan spesifikasi (<spec>)
    step_num = 1
    seen_specs: set[str] = set()
    seen_pins: set[str] = set()

    for tgrp in tree.findall(".//testgrp"):
        ttitle = clean_ws(tgrp.findtext("testtitle", ""))
        if not ttitle:
            continue
        t1_texts = [elem_text(t1.find("ptxt")) for t1 in tgrp.findall(".//test1") if elem_text(t1.find("ptxt"))]
        detail = " -> ".join(t for t in t1_texts if t)[:240]
        if detail:
            result["repair_steps"].append(
                f"Langkah {step_num} ({section_name}) — {ttitle}: {detail}"
            )
        else:
            result["repair_steps"].append(
                f"Langkah {step_num} ({section_name}) — {ttitle}"
            )
        step_num += 1

        # Ekstrak tabel <spec> di dalam testgrp
        for spec in tgrp.findall(".//spec"):
            stitle = clean_ws(spec.findtext("title", "")) or ttitle
            if stitle.lower() in {"hasil", "result", "prosedur"}:
                continue
            for tbl in spec.findall(".//table"):
                for row in parse_cals_table(tbl):
                    if len(row) >= 2:
                        conn_tester = row[0]
                        spec_val = row[-1]
                        cond_mid = row[1] if len(row) >= 3 else ""
                        if not conn_tester or any(
                            h in conn_tester.lower() for h in ("hubungan tester", "kondisi", "lanjutkan ke")
                        ):
                            continue
                        if spec_val.strip().upper() in {"A", "B", "C", "D", "E", "F", "OK", "NG", "-"}:
                            continue
                        param_lbl = f"[{section_name}] {stitle}: {conn_tester}"
                        if cond_mid and cond_mid != spec_val:
                            param_lbl += f" ({cond_mid})"
                        spec_key = f"{param_lbl}={spec_val}"
                        if spec_key not in seen_specs:
                            seen_specs.add(spec_key)
                            result["standard_specs"].append(
                                {
                                    "parameter": param_lbl[:140],
                                    "normal_range": spec_val[:140],
                                    "unit": "V / Ohm",
                                }
                            )
                        if conn_tester not in seen_pins and len(seen_pins) < 10:
                            seen_pins.add(conn_tester)
                            result["wiring_pinout"].append(
                                {
                                    "pin": f"[{section_name}] {conn_tester}"[:90],
                                    "signal": ttitle[:120],
                                    "function": f"Standar: {spec_val}"[:160],
                                }
                            )

    return result


def normalize_dtc_code(raw_code: str) -> tuple[str, str | None]:
    """
    Memisahkan kode DTC OBD-II utama dan Flash Code 2-digit (jika ada).
    Contoh:
      'P0105/31' -> ('P0105', '31')
      'C0200/31' -> ('C0200', '31')
      '11'       -> ('DTC-11', '11')
    """
    raw = clean_ws(raw_code).upper()
    if "/" in raw:
        main_part, flash_part = raw.split("/", 1)
        main_part = main_part.strip()
        flash_part = flash_part.strip()
        if re.match(r"^[PCBU][0-9A-F]{4}$", main_part):
            return main_part, flash_part
    if re.match(r"^[PCBU][0-9A-F]{4}$", raw):
        return raw, None
    if re.match(r"^[0-9]{2}$", raw):
        return f"DTC-{raw}", raw
    return raw, None


def infer_severity(code: str, section_name: str, item_desc: str) -> str:
    """Menentukan tingkat keparahan (CRITICAL / HIGH / MEDIUM) berdasarkan kode & sistem."""
    c_up = code.upper()
    s_up = f"{section_name} {item_desc}".upper()
    if any(k in s_up for k in ("AIRBAG", "SQUIB", "RESTRAINT", "PRETENSIONER", "HYBRID", "BATERAI HV")):
        return "CRITICAL"
    if any(k in s_up for k in ("REM", "BRAKE", "ABS", "CRANKSHAFT", "CAMSHAFT", "IMMOBILISER", "PROCESSOR", "RAM", "OVER", "INJECTOR", "FUEL")):
        return "HIGH"
    if c_up.startswith(("P0", "P1", "P2", "C0", "C1", "B1", "B2")):
        return "HIGH"
    return "MEDIUM"


def build_pack_and_markdown_from_gsic(
    xml_roots: list[Path],
    pack_meta: dict[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    """
    Menggabungkan satu atau beberapa folder `xmlweb/<pub_id>/repair` Toyota GSIC menjadi:
    1. File Paket JSON AGOS (`PAKET_MANUAL_TOYOTA_<...>.json`)
    2. File Buku Manual Gabungan Markdown (`MANUAL_REPAIR_TOYOTA_<...>.md`)
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    all_pinouts: list[dict[str, str]] = []
    seen_pin_keys: set[str] = set()
    all_sensor_specs: list[dict[str, str]] = []
    seen_spec_names: set[str] = set()
    dtc_map: dict[str, dict[str, Any]] = {}
    toc_sections_summary: list[tuple[str, str, int]] = []

    for xml_root in xml_roots:
        # Temukan folder repair/<term atau tanggal terakhir> dan repair/contents
        contents_dirs = list(xml_root.rglob("repair/contents"))
        if not contents_dirs:
            continue
        contents_dir = contents_dirs[0]
        repair_dir = contents_dir.parent

        # Pilih sub-folder indeks terbaik (prioritaskan `term`, jika tidak ada pilih tanggal terbesar)
        index_dir = repair_dir / "term"
        if not (index_dir / "troubleshoot.xml").exists():
            cand_dirs = sorted(
                [d for d in repair_dir.iterdir() if d.is_dir() and (d / "troubleshoot.xml").exists()],
                key=lambda x: x.name,
                reverse=True,
            )
            if not cand_dirs:
                continue
            index_dir = cand_dirs[0]

        toc_path = index_dir / "toc_rpr.xml"
        ts_path = index_dir / "troubleshoot.xml"

        # 1. Ekstrak TERMINAL ECM/ECU & DATA LIST dari toc_rpr.xml
        if toc_path.exists():
            try:
                toc_tree = ET.parse(toc_path)
                for servcat in toc_tree.findall(".//servcat"):
                    cat_name = clean_ws(servcat.findtext("name", ""))
                    for sec in servcat.findall("section"):
                        sec_name = clean_ws(sec.findtext("name", ""))
                        paras = sec.findall(".//para")
                        toc_sections_summary.append((cat_name, sec_name, len(paras)))
                        for para in paras:
                            pname = clean_ws(para.findtext("name", "")).upper()
                            pid = para.attrib.get("id", "")
                            cfile = find_contents_file(contents_dir, pid)
                            if not cfile:
                                continue
                            if "TERMINAL ECM" in pname or "TERMINAL ECU" in pname:
                                pins, s_specs = parse_terminal_ecu_doc(cfile, sec_name)
                                for p in pins:
                                    pk = f"{p['pin']}|{p['signal']}"
                                    if pk not in seen_pin_keys:
                                        seen_pin_keys.add(pk)
                                        all_pinouts.append(p)
                                for sp in s_specs:
                                    sk = sp["sensor_name"]
                                    if sk not in seen_spec_names:
                                        seen_spec_names.add(sk)
                                        all_sensor_specs.append(sp)
                            elif "DATA LIST" in pname:
                                dl_specs = parse_data_list_doc(cfile, sec_name)
                                for sp in dl_specs:
                                    sk = sp["sensor_name"]
                                    if sk not in seen_spec_names and len(all_sensor_specs) < 180:
                                        seen_spec_names.add(sk)
                                        all_sensor_specs.append(sp)
            except Exception as exc:
                print(f"[WARN] Gagal mem-parsing toc_rpr.xml ({toc_path}): {exc}")

        # 2. Ekstrak seluruh DTC dari troubleshoot.xml + dokumen RM000...xml terkait
        if ts_path.exists():
            try:
                ts_tree = ET.parse(ts_path)
                for servcat in ts_tree.findall(".//servcat"):
                    cat_name = clean_ws(servcat.findtext("name", ""))
                    for sec in servcat.findall("section"):
                        sec_name = clean_ws(sec.findtext("name", ""))
                        for ttl in sec.findall("ttl"):
                            ttl_name = clean_ws(ttl.findtext("name", ""))
                            for dtc_el in ttl.findall("dtc"):
                                rm_id = dtc_el.attrib.get("id", "")
                                cfile = find_contents_file(contents_dir, rm_id)
                                parsed_doc = parse_dtc_doc(cfile, sec_name, ttl_name) if cfile else {
                                    "description": "",
                                    "causes": [],
                                    "repair_steps": [],
                                    "standard_specs": [],
                                    "wiring_pinout": [],
                                }

                                codes_els = dtc_el.findall("dtccode")
                                items_els = dtc_el.findall("detection-item")
                                for idx_c, c_el in enumerate(codes_els):
                                    raw_c = clean_ws(c_el.text)
                                    if not raw_c:
                                        continue
                                    det_item = (
                                        clean_ws(items_els[idx_c].text)
                                        if idx_c < len(items_els)
                                        else (clean_ws(items_els[0].text) if items_els else "")
                                    )
                                    norm_c, flash_c = normalize_dtc_code(raw_c)
                                    flash_note = f" / Flash Code {flash_c}" if flash_c else ""
                                    desc_line = f"[{sec_name} — {ttl_name}{flash_note}] {det_item} (Dokumen: {rm_id})"

                                    if norm_c not in dtc_map:
                                        dtc_map[norm_c] = {
                                            "code": norm_c,
                                            "descriptions": [desc_line],
                                            "severity_level": infer_severity(norm_c, sec_name, det_item),
                                            "causes": [],
                                            "repair_steps": [],
                                            "wiring_pinout": [],
                                            "standard_specs": [],
                                            "doc_ids": [rm_id],
                                        }
                                    else:
                                        if desc_line not in dtc_map[norm_c]["descriptions"]:
                                            dtc_map[norm_c]["descriptions"].append(desc_line)
                                        if rm_id not in dtc_map[norm_c]["doc_ids"]:
                                            dtc_map[norm_c]["doc_ids"].append(rm_id)

                                    entry = dtc_map[norm_c]
                                    for c_str in parsed_doc["causes"]:
                                        if c_str not in entry["causes"] and len(entry["causes"]) < 10:
                                            entry["causes"].append(c_str)
                                    if not entry["causes"] and det_item:
                                        entry["causes"].append(
                                            f"[{sec_name}] Malfungsi pada sirkuit/komponen: {det_item}"
                                        )

                                    for st in parsed_doc["repair_steps"]:
                                        if st not in entry["repair_steps"] and len(entry["repair_steps"]) < 12:
                                            entry["repair_steps"].append(st)
                                    if not entry["repair_steps"]:
                                        entry["repair_steps"].append(
                                            f"Langkah 1 ({sec_name}) — Periksa soket, kabel harness, dan komponen {det_item} sesuai dokumen Toyota GSIC {rm_id}."
                                        )

                                    for sp in parsed_doc["standard_specs"]:
                                        if sp not in entry["standard_specs"] and len(entry["standard_specs"]) < 10:
                                            entry["standard_specs"].append(sp)

                                    for wp in parsed_doc["wiring_pinout"]:
                                        if wp not in entry["wiring_pinout"] and len(entry["wiring_pinout"]) < 10:
                                            entry["wiring_pinout"].append(wp)
            except Exception as exc:
                print(f"[WARN] Gagal mem-parsing troubleshoot.xml ({ts_path}): {exc}")

    # Susun list dtc_catalog final sesuai skema AGOS
    dtc_catalog_out: list[dict[str, Any]] = []
    for code_key in sorted(dtc_map.keys()):
        d = dtc_map[code_key]
        dtc_catalog_out.append(
            {
                "code": d["code"],
                "description_id": " | ".join(d["descriptions"][:3])[:320],
                "severity_level": d["severity_level"],
                "common_causes": "; ".join(d["causes"][:6])[:450] or "Periksa konektor, harness, sensor, dan ECM.",
                "repair_steps": d["repair_steps"][:8],
                "wiring_pinout": d["wiring_pinout"][:8],
                "standard_specs": d["standard_specs"][:8],
                "page": 1,
            }
        )

    pack_payload = {
        "pack_id": pack_meta["pack_id"],
        "brand": pack_meta.get("brand", "Toyota"),
        "model": pack_meta["model"],
        "model_aliases": pack_meta.get("model_aliases", [pack_meta["model"].lower()]),
        "generation_id": pack_meta.get("generation_id"),
        "generation_label": pack_meta["generation_label"],
        "year_start": pack_meta["year_start"],
        "year_end": pack_meta["year_end"],
        "engine_codes": pack_meta["engine_codes"],
        "title": pack_meta["title"],
        "dtc_catalog": dtc_catalog_out,
        "wiring_pinouts": all_pinouts,
        "sensor_specs": all_sensor_specs,
    }

    slug = pack_meta["pack_id"].upper()
    json_out_path = output_dir / f"PAKET_MANUAL_{slug}.json"
    md_out_path = output_dir / f"MANUAL_REPAIR_{slug}.md"

    json_out_path.write_text(
        json.dumps(pack_payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # Bangun file Markdown (.md) lengkap untuk dibaca manusia & dokumentasi
    md_lines: list[str] = [
        f"# {pack_meta['title']}",
        "",
        f"- **Pack ID AGOS**: `{pack_meta['pack_id']}`",
        f"- **Merek & Model**: {pack_meta.get('brand', 'Toyota')} {pack_meta['model']} ({pack_meta['generation_label']})",
        f"- **Rentang Tahun**: {pack_meta['year_start']}–{pack_meta['year_end']}",
        f"- **Kode Mesin Tercakup**: `{', '.join(pack_meta['engine_codes'])}`",
        f"- **Total Kode DTC Terindeks**: **{len(dtc_catalog_out)} Kode DTC**",
        f"- **Total Pinout Terminal ECM/ECU**: **{len(all_pinouts)} Terminal**",
        f"- **Total Spesifikasi Sensor & Data List**: **{len(all_sensor_specs)} Parameter**",
        "",
        "---",
        "",
        "## 1. Ringkasan Bab & Sistem (`toc_rpr.xml`)",
        "",
        "| Kategori Servis | Nama Sistem / Mesin | Jumlah Sub-Bab Prosedur |",
        "| :--- | :--- | :---: |",
    ]
    seen_sec_rows: set[str] = set()
    for cat_n, sec_n, p_cnt in toc_sections_summary:
        rk = f"{cat_n}|{sec_n}"
        if rk not in seen_sec_rows:
            seen_sec_rows.add(rk)
            md_lines.append(f"| {cat_n} | {sec_n} | {p_cnt} |")

    md_lines.extend(
        [
            "",
            "---",
            "",
            "## 2. Tabel Pinout & Tegangan Standar Terminal ECM / ECU",
            "",
            "| Terminal (Simbol & Pin) | Warna Kabel & Deskripsi | Kondisi & Standar Tegangan / Tahanan |",
            "| :--- | :--- | :--- |",
        ]
    )
    for wp in all_pinouts:
        p_clean = wp["pin"].replace("|", "/")
        s_clean = wp["signal"].replace("|", "/")
        f_clean = wp["function"].replace("|", "/")
        md_lines.append(f"| `{p_clean}` | {s_clean} | {f_clean} |")

    md_lines.extend(
        [
            "",
            "---",
            "",
            "## 3. Katalog Lengkap Prosedur Pemeriksaan Kode DTC (OBD-II & Flash Code)",
            "",
        ]
    )
    for dtc in dtc_catalog_out:
        md_lines.append(f"### DTC `{dtc['code']}` — {dtc['description_id']}")
        md_lines.append(f"- **Tingkat Keparahan**: `{dtc['severity_level']}`")
        md_lines.append(f"- **Area Gangguan & Kondisi Deteksi**: {dtc['common_causes']}")
        if dtc["repair_steps"]:
            md_lines.append("- **Langkah Pemeriksaan Resmi (Toyota GSIC)**:")
            for st in dtc["repair_steps"]:
                md_lines.append(f"  - {st}")
        if dtc["standard_specs"]:
            md_lines.append("- **Spesifikasi Standar Multimeter**:")
            for sp in dtc["standard_specs"]:
                md_lines.append(f"  - `{sp['parameter']}` : **{sp['normal_range']}**")
        md_lines.append("")

    md_out_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(
        f"[SUKSES] {pack_meta['pack_id']} -> DTC: {len(dtc_catalog_out)}, "
        f"Pinouts: {len(all_pinouts)}, Sensor Specs: {len(all_sensor_specs)} | "
        f"JSON: {json_out_path.name}, MD: {md_out_path.name}"
    )
    return pack_payload


def register_packs_into_agos(packs: list[dict[str, Any]], project_root: Path) -> None:
    """
    Menyimpan/memperbarui paket manual Toyota ke `backend/app/data/custom_manual_packs.json`
    tanpa menghapus paket yang sudah ada (seperti `suzuki_ertiga_gen1_2012_2017`).
    """
    custom_packs_path = project_root / "backend" / "app" / "data" / "custom_manual_packs.json"
    existing_packs: list[dict[str, Any]] = []
    if custom_packs_path.exists():
        try:
            raw = json.loads(custom_packs_path.read_text(encoding="utf-8"))
            if isinstance(raw, dict) and isinstance(raw.get("packs"), list):
                existing_packs = raw["packs"]
        except Exception:
            existing_packs = []

    by_id: dict[str, dict[str, Any]] = {
        str(p.get("pack_id")): p for p in existing_packs if p.get("pack_id")
    }
    for new_p in packs:
        by_id[str(new_p["pack_id"])] = new_p

    merged_list = list(by_id.values())
    custom_packs_path.write_text(
        json.dumps({"packs": merged_list}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[AGOS DB] Berhasil mendaftarkan {len(packs)} paket Toyota ke {custom_packs_path} (Total aktif: {len(merged_list)} paket).")


def run_batch_conversion(
    scratch_base: Path,
    avanza_root: Path,
    output_dir: Path,
    project_root: Path,
) -> list[dict[str, Any]]:
    """Menjalankan konversi batch seluruh paket manual Toyota yang sudah diekstrak XML-nya."""
    pubs = scratch_base / "pubs"

    pack_configs: list[tuple[list[Path], dict[str, Any]]] = [
        (
            [avanza_root],
            {
                "pack_id": "toyota_avanza_xenia_2004_2015",
                "brand": "Toyota",
                "model": "Avanza",
                "model_aliases": [
                    "avanza",
                    "veloz",
                    "avanza vvti",
                    "all new avanza",
                    "avanza lama",
                    "xenia",
                    "daihatsu xenia",
                    "rush",
                    "rush konde",
                    "terios",
                    "gran max",
                    "granmax",
                    "luxio",
                    "f600",
                    "f601",
                    "f602",
                ],
                "generation_id": "toyota_avanza_gen1_2_kv",
                "generation_label": "Toyota Avanza / Rush & Daihatsu Xenia / Terios (K3-VE 1.3L · 3SZ-VE 1.5L · EJ-VE 1.0L)",
                "year_start": 2004,
                "year_end": 2015,
                "engine_codes": ["K3-VE", "3SZ-VE", "EJ-VE"],
                "title": "Buku Pedoman Reparasi Resmi Toyota Avanza, Rush & Daihatsu Xenia (RM02X1ED_ID · Mesin K3-VE 1.3L, 3SZ-VE 1.5L, EJ-VE 1.0L & A/T A4Q)",
            },
        ),
        (
            [pubs / "FORTUNER 2012", pubs / "FORTUNER"],
            {
                "pack_id": "toyota_fortuner_gen1_2005_2015",
                "brand": "Toyota",
                "model": "Fortuner",
                "model_aliases": [
                    "fortuner",
                    "fortuner vnt",
                    "fortuner lama",
                    "fortuner trd",
                    "fortuner diesel",
                    "fortuner bensin",
                    "kun51",
                    "kun60",
                    "tgn51",
                    "tgn61",
                    "ggn50",
                ],
                "generation_id": "toyota_fortuner_gen1",
                "generation_label": "Toyota Fortuner Gen 1 (2KD-FTV 2.5L VNT/D-4D · 1KD-FTV 3.0L · 2TR-FE 2.7L VVT-i · 1GR-FE 4.0L V6)",
                "year_start": 2005,
                "year_end": 2015,
                "engine_codes": ["2KD-FTV", "1KD-FTV", "2TR-FE", "1GR-FE"],
                "title": "Buku Pedoman Reparasi Resmi Toyota Fortuner (RM1871EH-ID & RMOOM4E · Mesin 2KD-FTV, 1KD-FTV, 2TR-FE, 1GR-FE & A/T A340/A343/A750F)",
            },
        ),
        (
            [pubs / "HILUX 2012", pubs / "FORTUNER 2012"],
            {
                "pack_id": "toyota_innova_gen1_2004_2015",
                "brand": "Toyota",
                "model": "Innova",
                "model_aliases": [
                    "innova",
                    "kijang innova",
                    "innova lama",
                    "innova bensin",
                    "innova diesel",
                    "innova barong",
                    "tgn40",
                    "tgn41",
                    "kun40",
                ],
                "generation_id": "toyota_innova_gen1",
                "generation_label": "Toyota Kijang Innova Gen 1 (1TR-FE 2.0L Bensin · 2KD-FTV 2.5L D-4D Diesel · 2TR-FE 2.7L)",
                "year_start": 2004,
                "year_end": 2015,
                "engine_codes": ["1TR-FE", "2KD-FTV", "2TR-FE"],
                "title": "Buku Pedoman Reparasi Resmi Toyota Platform IMV Kijang Innova (RM1830EH-ID & RM1871EH-ID · Mesin 1TR-FE 2.0L Bensin, 2KD-FTV 2.5L Diesel & 2TR-FE 2.7L)",
            },
        ),
        (
            [pubs / "HILUX 2012"],
            {
                "pack_id": "toyota_hilux_hiace_2005_2015",
                "brand": "Toyota",
                "model": "Hilux / HiAce",
                "model_aliases": [
                    "hilux",
                    "hilux vigo",
                    "hilux single cab",
                    "hilux double cabin",
                    "hiace",
                    "hiace commuter",
                    "tgn10",
                    "kun15",
                    "kun25",
                    "kun26",
                ],
                "generation_id": "toyota_hilux_hiace",
                "generation_label": "Toyota Hilux Vigo & HiAce Commuter (1TR-FE 2.0L · 2KD-FTV 2.5L · 1KD-FTV 3.0L)",
                "year_start": 2005,
                "year_end": 2015,
                "engine_codes": ["2KD-FTV", "1KD-FTV", "1TR-FE"],
                "title": "Buku Pedoman Reparasi Resmi Toyota Hilux & HiAce IMV (RM1830EH-ID · Mesin 1KD-FTV 3.0L, 2KD-FTV 2.5L Diesel, 1TR-FE 2.0L Bensin & A/T A340F)",
            },
        ),
        (
            [pubs / "RM_YARIS", pubs / "RM_TOYOTA_VIOS"],
            {
                "pack_id": "toyota_yaris_vios_1nzfe_2003_2016",
                "brand": "Toyota",
                "model": "Yaris / Vios / Sienta",
                "model_aliases": [
                    "yaris",
                    "yaris bakpao",
                    "yaris lele",
                    "vios",
                    "limo",
                    "vios limo",
                    "ncp91",
                    "ncp93",
                ],
                "generation_id": "toyota_yaris_vios_sienta",
                "generation_label": "Toyota Yaris (NCP91) & Vios / Limo (NCP93) — Mesin 1NZ-FE 1.5L VVT-i",
                "year_start": 2003,
                "year_end": 2016,
                "engine_codes": ["1NZ-FE"],
                "title": "Buku Pedoman Reparasi Resmi Toyota Yaris & Vios / Limo (RMO2C4EL & RMO5K3EL · Mesin 1NZ-FE 1.5L VVT-i & Transaxle Otomatis U340E)",
            },
        ),
    ]

    # Tambahkan paket Corolla Altis / Camry / Alphard bila sudah diekstrak
    altis_camry_roots = [
        p
        for p in (
            pubs / "NEW COROLLA ALTIS",
            pubs / "RM_Alphard_2008 (E)",
            pubs / "CAMRY HYBRID",
            pubs / "CAMRY",
        )
        if p.exists() and list(p.rglob("repair/contents/*.xml"))
    ]
    if altis_camry_roots:
        pack_configs.append(
            (
                altis_camry_roots,
                {
                    "pack_id": "toyota_corolla_camry_alphard_2004_2015",
                    "brand": "Toyota",
                    "model": "Corolla / Camry / Alphard",
                    "model_aliases": [
                        "corolla",
                        "altis",
                        "corolla altis",
                        "camry",
                        "camry hybrid",
                        "alphard",
                        "vellfire",
                        "harrier",
                        "zze141",
                        "zze142",
                        "zre143",
                        "acv40",
                        "gsv40",
                        "avv50",
                        "ggh20",
                        "anh20",
                    ],
                    "generation_id": "toyota_corolla_camry_alphard",
                    "generation_label": "Toyota Corolla Altis, Camry / Hybrid & Alphard (1ZZ-FE · 3ZR-FE · 2AZ-FE · 2GR-FE · 2AR-FXE)",
                    "year_start": 2004,
                    "year_end": 2015,
                    "engine_codes": ["1ZZ-FE", "3ZZ-FE", "3ZR-FE", "2AZ-FE", "1AZ-FE", "2GR-FE", "2AR-FXE"],
                    "title": "Buku Pedoman Reparasi Resmi Toyota Corolla Altis, Camry & Alphard (RMO8V1EL, RM08Z0E_ID & RM213OEL · Mesin 1ZZ-FE, 3ZR-FE, 2AZ-FE, 2GR-FE & 2AR-FXE Hybrid)",
                },
            )
        )

    generated_packs: list[dict[str, Any]] = []
    for roots, meta in pack_configs:
        valid_roots = [r for r in roots if r.exists()]
        if not valid_roots:
            continue
        pack_data = build_pack_and_markdown_from_gsic(valid_roots, meta, output_dir)
        generated_packs.append(pack_data)

    if generated_packs:
        register_packs_into_agos(generated_packs, project_root)

    return generated_packs
