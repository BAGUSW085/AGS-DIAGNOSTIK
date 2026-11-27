"""
Render Potongan Foto Wiring Asli Resmi Suzuki Grand Vitara JB420 (Vol 1 & Vol 2)
================================================================================
Merender halaman diagram sirkuit vektor OEM (Kategori 1: Mesin & EFI,
Kategori 2: 7 Modul Kontrol Ber-DTC, Kategori 4: Peta Sekring, Ground, Warna Kabel & Konektor)
menjadi gambar WebP HD tajam dengan auto-crop margin putih.
"""

from __future__ import annotations

from pathlib import Path
import shutil
import pypdfium2 as pdfium
from PIL import Image, ImageChops

ROOT_DIR = Path(__file__).resolve().parents[2]
VOL1_PDF = ROOT_DIR / "manual repair suzuki vitara" / "manual repair suzuki grand vitara 2012.pdf"
VOL2_PDF = ROOT_DIR / "manual repair suzuki vitara" / "grand vitara 2.pdf"

WEB_IMG_DIR = ROOT_DIR / "backend" / "app" / "static" / "img" / "jb420_wiring"
OFF_IMG_DIR = ROOT_DIR / "android_offline" / "www" / "img" / "jb420_wiring"

# Daftar halaman resmi Vol 1 & Vol 2 (1-indexed) untuk Kategori 1 + 2 + 4
PAGES_TO_RENDER: list[tuple[str, str, int, float]] = [
    # --- KATEGORI 1: MESIN & EFI (VOL 1 BAB 1A / 1H & VOL 2 BAB 9A A-1..A-5) ---
    ("v1_ecm_io_1a15", "v1", 73, 2.2),          # Diagram Sirkuit Input/Output ECM (1A-15)
    ("v1_ecm_power_1a217", "v1", 275, 2.2),     # Power ECM & Ground (1A-217)
    ("v1_ign_1h2", "v1", 430, 2.3),             # Diagram Sirkuit Pengapian Koil COP (1H-2)
    ("v2_a3_pengapian_9a41", "v2", 501, 2.3),   # A-3 Diagram Sirkuit Pengapian (9A-41)
    ("v1_ckp_p0335_1a115", "v1", 173, 2.2),     # CKP P0335 (1A-115)
    ("v1_cmp_p0340_1a117", "v1", 175, 2.2),     # CMP P0340 (1A-117)
    ("v1_maf_p0102_1a65", "v1", 123, 2.2),      # MAF P0102 (1A-65)
    ("v1_iat_p0112_1a77", "v1", 135, 2.2),      # IAT P0112 (1A-77)
    ("v1_map_p0107_1a70", "v1", 128, 2.2),      # MAP P0107 (1A-70)
    ("v1_ect_p0118_1a85", "v1", 143, 2.2),      # ECT P0118 (1A-85)
    ("v1_af_p0131_1a94", "v1", 152, 2.2),       # O2/A-F Sensor-1 P0131 (1A-94)
    ("v1_ho2s_p0037_1a59", "v1", 117, 2.2),     # HO2S Heater Sensor-2 P0037 (1A-59)
    ("v1_etc_p0122_1a88", "v1", 146, 2.2),      # ETC / TPS Main P0122 (1A-88)
    ("v1_app_p2122_1a181", "v1", 239, 2.2),     # APP Pedal Gas P2122 (1A-181)
    ("v1_injector_1a220", "v1", 278, 2.2),      # Sirkuit 4x Fuel Injector Non-DTC (1A-220)
    ("v1_fuelpump_1a222", "v1", 280, 2.2),      # Fuel Pump & Relay Non-DTC (1A-222)
    ("v1_fan_p0480_1a133", "v1", 191, 2.2),     # Cooling Fan P0480 (1A-133)
    ("v2_a4_pendingin_9a42", "v2", 502, 2.3),   # A-4 Diagram Sirkuit Pendingin (9A-42)
    ("v2_a1_cranking_9a39", "v2", 499, 2.3),    # A-1 Diagram Sirkuit Cranking/Starter (9A-39)
    ("v2_a2_pengisian_9a40", "v2", 500, 2.3),   # A-2 Diagram Sirkuit Pengisian/Alternator (9A-40)
    ("v1_knock_p0327_1a113", "v1", 171, 2.2),   # Knock Sensor P0327/P0328 (1A-113)
    ("v1_egr_p0403_1a123", "v1", 181, 2.2),     # EGR Control P0403 (1A-123)
    ("v1_evap_p0443_1a127", "v1", 185, 2.2),    # EVAP Purge P0443 (1A-127)
    ("v1_imtv_p0660_1a152", "v1", 210, 2.2),    # IMTV Intake Manifold Tuning Valve P0660 (1A-152)
    ("v1_vss_p0500_1a137", "v1", 195, 2.2),     # VSS P0500 (1A-137)
    ("v1_brake_p0504_1a139", "v1", 197, 2.2),   # Brake Switch P0504 (1A-139)
    ("v1_acpress_p0532_1a141", "v1", 199, 2.2), # A/C Pressure Sensor P0532 (1A-141)
    ("v1_eld_p1501_1a154", "v1", 212, 2.2),     # Electric Load Sensor P1501 (1A-154)
    ("v1_can_p1674_1a159", "v1", 217, 2.2),     # CAN Bus Komunikasi P1674 (1A-159)
    ("v1_p0171_ref_1a101", "v1", 159, 2.0),     # Non-Wiring P0171 Tabel Diagnosa Manual (1A-101)
    ("v2_a5_ecm_p1_9a43", "v2", 503, 2.2),      # A-5 Kontrol Mesin & A/C Lembar 1 (9A-43)
    ("v2_a5_ecm_p2_9a44", "v2", 504, 2.2),      # A-5 Kontrol Mesin & A/C Lembar 2 (9A-44)
    ("v2_a5_ecm_p3_9a45", "v2", 505, 2.2),      # A-5 Kontrol Mesin & A/C Lembar 3 (9A-45)
    ("v2_a5_ecm_p4_9a46", "v2", 506, 2.2),      # A-5 Kontrol Mesin & A/C Lembar 4 (9A-46)
    ("v2_a5_ecm_p5_9a47", "v2", 507, 2.2),      # A-5 Kontrol Mesin & A/C Lembar 5 (9A-47)

    # --- KATEGORI 2: 7 MODUL KONTROL BER-DTC (VOL 1 4E & VOL 2 BAB 9A) ---
    ("v2_a6_tcm_p1_9a48", "v2", 508, 2.2),      # A-6 TCM Transmisi Otomatis Lembar 1 (9A-48)
    ("v2_a6_tcm_p2_9a49", "v2", 509, 2.2),      # A-6 TCM Transmisi Otomatis Lembar 2 (9A-49)
    ("v1_abs_4e4", "v1", 624, 2.2),             # Diagram Sirkuit ABS/EBD (4E-4)
    ("v2_f2_abs_p1_9a86", "v2", 546, 2.2),      # F-2 ABS Lembar 1 (9A-86)
    ("v2_f2_abs_p2_9a87", "v2", 547, 2.2),      # F-2 ABS Lembar 2 (9A-87)
    ("v2_f1_srs_9a85", "v2", 545, 2.2),         # F-1 SRS Air Bag SDM G47 (9A-85)
    ("v2_e2_hvac_p1_9a83", "v2", 543, 2.2),     # E-2 Auto A/C HVAC Lembar 1 (9A-83)
    ("v2_e2_hvac_p2_9a84", "v2", 544, 2.2),     # E-2 Auto A/C HVAC Lembar 2 (9A-84)
    ("v2_a8_bcm_p1_9a51", "v2", 511, 2.2),      # A-8 BCM Kontrol Bodi Lembar 1 (9A-51)
    ("v2_a8_bcm_p2_9a52", "v2", 512, 2.2),      # A-8 BCM Kontrol Bodi Lembar 2 (9A-52)
    ("v2_a7_icm_9a50", "v2", 510, 2.2),         # A-7 Immobilizer ICM G24 (9A-50)
    ("v2_b9_kscm_9a66", "v2", 526, 2.2),        # B-9 Smart Key / Keyless Start KSCM G44 (9A-66)

    # --- KATEGORI 4: PETA DASAR KELISTRIKAN (WARNA KABEL, SEKRING, GROUND, KONEKTOR) ---
    ("v2_base_colors_9a2", "v2", 462, 2.2),     # 9A-2 Singkatan & Simbol Warna Kabel
    ("v2_base_symbols_9a3", "v2", 463, 2.2),    # 9A-3 Simbol & Tanda Kelistrikan
    ("v2_base_ground_9a24", "v2", 484, 2.2),    # 9A-24 Titik Ground (Massa)
    ("v2_base_power_9a25", "v2", 485, 2.2),     # 9A-25 Diagram Power Supply
    ("v2_base_fuse1_9a28", "v2", 488, 2.2),     # 9A-28 Box Sikring No.1
    ("v2_base_fuse2_9a29", "v2", 489, 2.2),     # 9A-29 Box Sikring No.2 & Kotak Relay
    ("v2_base_fuse3_9a30", "v2", 490, 2.2),     # 9A-30 Box Sikring No.3 (Junction Block)
    ("v2_base_conn_eng_9a13", "v2", 473, 2.2),  # 9A-13 Layout Konektor Ruang Mesin
    ("v2_base_conn_c_9a91", "v2", 551, 2.2),    # 9A-91 Bentuk Fisik Konektor C
    ("v2_base_conn_e_9a93", "v2", 553, 2.2),    # 9A-93 Bentuk Fisik Konektor E
]


def trim_white_margins(img: Image.Image, pad: int = 22) -> Image.Image:
    rgb = img.convert("RGB")
    bg = Image.new("RGB", rgb.size, (255, 255, 255))
    diff = ImageChops.difference(rgb, bg)
    bbox = diff.getbbox()
    if not bbox:
        return rgb
    left = max(0, bbox[0] - pad)
    top = max(0, bbox[1] - pad)
    right = min(rgb.width, bbox[2] + pad)
    bottom = min(rgb.height, bbox[3] + pad)
    return rgb.crop((left, top, right, bottom))


def main() -> None:
    WEB_IMG_DIR.mkdir(parents=True, exist_ok=True)
    OFF_IMG_DIR.mkdir(parents=True, exist_ok=True)

    doc1 = pdfium.PdfDocument(str(VOL1_PDF))
    doc2 = pdfium.PdfDocument(str(VOL2_PDF))

    total_bytes = 0
    for slug, vol, pno, scale in PAGES_TO_RENDER:
        doc = doc1 if vol == "v1" else doc2
        page = doc[pno - 1]
        pil_img = page.render(scale=scale).to_pil()
        cropped = trim_white_margins(pil_img, pad=22)

        # Batasi lebar maksimum 1600px agar super tajam tapi sangat ringan di HP & APK
        if cropped.width > 1600:
            ratio = 1600 / cropped.width
            cropped = cropped.resize((1600, int(cropped.height * ratio)), Image.Resampling.LANCZOS)

        out_web = WEB_IMG_DIR / f"{slug}.webp"
        cropped.save(out_web, "WEBP", quality=82, method=4)
        shutil.copy2(out_web, OFF_IMG_DIR / f"{slug}.webp")
        sz = out_web.stat().st_size
        total_bytes += sz
        print(f"  [OK] {slug:28s} ({vol} p.{pno:3d}) -> {cropped.width}x{cropped.height} ({sz/1024:.1f} KB)")

    doc1.close()
    doc2.close()
    print(f"\n=== SELESAI: {len(PAGES_TO_RENDER)} foto wiring asli HD WebP ({total_bytes/1024/1024:.2f} MB total) ===")


if __name__ == "__main__":
    main()
