"""
Sinkronisasi Otomatis Web Dashboard (`backend/app/static/index.html`) ke APK Offline (`android_offline/www/index.html`)
========================================================================================================================
Menjaga 100% paritas fitur antara Web/PWA dan APK Android Offline:
- Mengganti Tailwind CDN & FontAwesome CDN dengan aset lokal (`css/fontawesome.min.css` & `css/app.css`)
- Memuat seluruh engine lokal offline (`embedded-data.js`, `data-store.js`, `engine.js`, `manual-search.js`,
  `offline-multi-model.js`, `offline-api.js`)
- Membelokkan seluruh panggilan `fetch('/api/v1/...')` & `fetch('/health')` ke `offlineFetch` secara otomatis
- Mempertahankan tombol orientasi layar Horizontal/Vertikal & handler tombol Back Android!
"""

from pathlib import Path
import re
import shutil
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
WEB_STATIC_DIR = ROOT_DIR / "backend" / "app" / "static"
WEB_HTML = WEB_STATIC_DIR / "index.html"
OFFLINE_WWW_DIR = ROOT_DIR / "android_offline" / "www"
OFFLINE_HTML = OFFLINE_WWW_DIR / "index.html"

OFFLINE_SCRIPTS = """  <!-- AGOS Offline Local Engine Bundle (100% Tanpa Server) -->
  <script src="js/embedded-data.js"></script>
  <script src="js/data-store.js"></script>
  <script src="js/engine.js"></script>
  <script src="js/manual-search.js"></script>
  <script src="js/offline-multi-model.js"></script>
  <script src="js/offline-api.js"></script>
  <script>
    (function () {
      const _origFetch = window.fetch ? window.fetch.bind(window) : null;
      window.fetch = function (input, init) {
        const url = typeof input === 'string' ? input : (input && input.url) || '';
        if (url.startsWith('/api/v1') || url.startsWith('/api/cases') || url === '/health' || url.endsWith('/health')) {
          return window.offlineFetch(url, init);
        }
        return _origFetch ? _origFetch(input, init) : Promise.reject(new Error('Offline mode'));
      };
    })();
  </script>
"""

ORIENTATION_AND_BACK_JS = """
    // ---------- TOMBOL ORIENTASI LAYAR ANDROID & HANDLER TOMBOL BACK ----------
    let isHorizontalOrientation = false;
    function syncOrientationButtonUI() {
      const isLand = window.innerWidth > window.innerHeight;
      const lbl = document.getElementById('label-orientation');
      const icon = document.getElementById('icon-orientation');
      if (isLand) {
        if (lbl) lbl.textContent = 'Vertikal';
        if (icon) icon.classList.remove('rotate-90');
      } else {
        if (lbl) lbl.textContent = 'Horizontal';
        if (icon) icon.classList.add('rotate-90');
      }
    }

    function toggleAppOrientation() {
      const targetHorizontal = !(window.innerWidth > window.innerHeight || isHorizontalOrientation);
      isHorizontalOrientation = targetHorizontal;
      const vp = document.querySelector('meta[name="viewport"]');
      const hasNative = Boolean(window.AgosNative && typeof window.AgosNative.setOrientation === 'function');
      if (targetHorizontal) {
        if (hasNative) {
          try { window.AgosNative.setOrientation('landscape'); } catch (e) {}
        } else if (screen.orientation && typeof screen.orientation.lock === 'function') {
          screen.orientation.lock('landscape').catch(() => {});
        }
      } else {
        if (hasNative) {
          try { window.AgosNative.setOrientation('portrait'); } catch (e) {}
        } else if (screen.orientation && typeof screen.orientation.lock === 'function') {
          screen.orientation.lock('portrait').catch(() => {});
        }
      }
      if (vp) vp.setAttribute('content', 'width=device-width, initial-scale=1.0, maximum-scale=3.0, user-scalable=yes, viewport-fit=cover');
      syncOrientationButtonUI();
      setTimeout(() => { renderManualComponentSimulator(); renderWiringSimulator(); }, 200);
    }

    window.addEventListener('resize', () => { syncOrientationButtonUI(); });
    window.addEventListener('orientationchange', () => { syncOrientationButtonUI(); });
    syncOrientationButtonUI();

    document.addEventListener('backbutton', (e) => {
      const modals = [
        ['modal-svg-zoom', () => closeAgosSvgZoomModal()],
        ['modal-jb420-photo-fullscreen', () => closeJb420PhotoFullscreen()],
        ['modal-engine-picker', () => closeEnginePickerModal()],
        ['modal-admin-security', () => closeAdminSecurityModal()],
        ['modal-manual-importer', () => toggleModalManualImporter(false)],
        ['modal-new-case', () => toggleModalNewCase(false)]
      ];
      for (const [id, closer] of modals) {
        const el = document.getElementById(id);
        if (el && !el.classList.contains('hidden')) {
          try { closer(); } catch (err) { el.classList.add('hidden'); }
          e.preventDefault();
          return;
        }
      }
    }, false);
"""


def sync_static_js_assets() -> None:
    """Pastikan skrip lokal penting (Atlas JB420, Cockpit UI, SheetJS) selalu identik di APK Offline."""
    js_files = [
        "jb420-wiring-atlas.js",
        "jb420-cockpit-ui.js",
        "xlsx.full.min.js",
    ]
    out_js_dir = OFFLINE_WWW_DIR / "js"
    out_js_dir.mkdir(parents=True, exist_ok=True)
    for fname in js_files:
        src = WEB_STATIC_DIR / "js" / fname
        if src.exists():
            shutil.copy2(src, out_js_dir / fname)
            print(f"[SUKSES] Sinkron JS lokal: android_offline/www/js/{fname} ({src.stat().st_size/1024:.1f} KB)")


def sync() -> None:
    sync_static_js_assets()
    html = WEB_HTML.read_text(encoding="utf-8")

    # 1. Ganti title, viewport pinch-zoom, & icon/asset paths agar relatif (file:// / Capacitor WebView)
    html = re.sub(
        r'<meta\s+name="viewport"\s+content="[^"]*"\s*/?>',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=4.0, user-scalable=yes, viewport-fit=cover">',
        html,
        count=1,
    )
    html = html.replace('href="/static/icon-192.png"', 'href="icon-192.png"')
    html = html.replace('src="/static/icon-192.png"', 'src="icon-192.png"')
    html = html.replace('src="/static/js/xlsx.full.min.js"', 'src="js/xlsx.full.min.js"')
    html = html.replace('src="/static/js/jb420-wiring-atlas.js"', 'src="js/jb420-wiring-atlas.js"')
    html = html.replace('src="/static/js/jb420-cockpit-ui.js"', 'src="js/jb420-cockpit-ui.js"')
    html = html.replace('href="/wiring-viewer"', 'href="ewd_viewer.html"')
    html = html.replace('>App v2.0<', '>v2.3.0 · JB420<')
    html = html.replace('>v2.2.0<', '>v2.3.0 · JB420<')
    html = html.replace('>v2.2.0 · JB420<', '>v2.3.0 · JB420<')
    html = html.replace('href="/manifest.json"', '')
    html = html.replace(
        "<title>AGOS SMART DIAGNOSTIK by Agos Corporation — Aplikasi Bengkel AI</title>",
        "<title>AGOS SMART DIAGNOSTIK — Aplikasi Android Offline Bengkel AI</title>",
    )
    html = html.replace(
        "<title>AGOS SMART DIAGNOSTIK — Aplikasi Android & Web Bengkel AI</title>",
        "<title>AGOS SMART DIAGNOSTIK — Aplikasi Android Offline Bengkel AI</title>",
    )

    # 2. Hapus CDN Tailwind, config script Tailwind, FontAwesome CDN, dan Google Fonts @import SECARA TERPISAH
    #    (FIX BUG KRITIS LAYAR PUTIH OFFLINE: sebelumnya regex gabungan gagal cocok karena ada <script> lain di antaranya!)
    html, tw_count = re.subn(
        r'<script\s+src="https://cdn\.tailwindcss\.com[^"]*"[^>]*></script>',
        '<!-- Local Offline Compiled Tailwind CSS (100% Tanpa Internet) -->\n  <link rel="stylesheet" href="css/app.css">',
        html,
        count=1,
    )
    if tw_count == 0 and 'href="css/app.css"' not in html:
        html = html.replace(
            "</head>",
            '  <link rel="stylesheet" href="css/app.css">\n</head>',
            1,
        )

    html = re.sub(
        r'\s*<script>\s*tailwind\.config\s*=[\s\S]*?</script>',
        '',
        html,
        count=1,
    )
    html = re.sub(
        r'<link\s+rel="stylesheet"\s+href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]+"[^>]*>',
        '<!-- Local Offline Font Awesome -->\n  <link rel="stylesheet" href="css/fontawesome.min.css">',
        html,
        count=1,
    )
    # Hapus Google Fonts @import agar WebView Android tidak pernah menunggu koneksi internet
    html = re.sub(
        r"@import\s+url\(['\"]https://fonts\.googleapis\.com/[^'\"]+['\"]\)\s*;?",
        "/* Offline Native System Font (Zero Internet Request) */",
        html,
    )

    # 3. Sisipkan tombol Orientasi Horizontal/Vertikal untuk APK Offline (tanpa tombol Admin / Bagikan APK)
    orient_btn = (
        '<button type="button" id="btn-toggle-orientation" onclick="toggleAppOrientation()" '
        'class="flex items-center gap-1.5 text-[11px] sm:text-xs font-semibold text-cyan-300 bg-cyan-950/80 '
        'hover:bg-cyan-900 border border-cyan-700/80 px-2.5 py-1.5 rounded-full shrink-0 active:scale-95 transition whitespace-nowrap" '
        'title="Putar Layar Horizontal / Vertikal">'
        '<i class="fa-solid fa-mobile-screen-button rotate-90 text-cyan-400" id="icon-orientation"></i>'
        '<span id="label-orientation">Horizontal</span></button>'
    )
    if "<!-- OFFLINE_ORIENTATION_SLOT -->" in html:
        html = html.replace("<!-- OFFLINE_ORIENTATION_SLOT -->", orient_btn, 1)
    else:
        html = re.sub(
            r'<button type="button" onclick="toggleModalAppInstall\(true\)" id="btn-header-install-app"[\s\S]*?</button>',
            orient_btn,
            html,
            count=1,
        )

    # 4. Hapus gambar QR CDN eksternal agar tidak panggil internet di mode offline (berhenti juga pada backtick & spasi!)
    html = re.sub(r'https://api\.qrserver\.com/[^"\'`\s]+', 'icon-192.png', html)

    # 5. Sisipkan bundle JS Offline sebelum <!-- JAVASCRIPT LOGIC CLIENT -->
    html = html.replace(
        "  <!-- JAVASCRIPT LOGIC CLIENT -->",
        OFFLINE_SCRIPTS + "\n  <!-- JAVASCRIPT LOGIC CLIENT -->",
        1,
    )

    # 6. Tambahkan orientation & Android back button handler sebelum </script> penutup terakhir
    last_script_end = html.rfind("</script>")
    if last_script_end != -1:
        html = html[:last_script_end] + ORIENTATION_AND_BACK_JS + "\n  " + html[last_script_end:]

    # 7. Lewati registrasi Service Worker pada Capacitor offline
    html = html.replace("if ('serviceWorker' in navigator)", "if (false && 'serviceWorker' in navigator)")

    # 8. HARD AUDIT 100% TRUE OFFLINE (GAGAL CEPAT BILA MASIH ADA CDN EKSTERNAL ATAU CSS LOKAL HILANG!)
    errors = []
    if 'href="css/app.css"' not in html:
        errors.append("MISSING <link rel=\"stylesheet\" href=\"css/app.css\"> di android_offline/www/index.html!")
    if 'href="css/fontawesome.min.css"' not in html:
        errors.append("MISSING <link rel=\"stylesheet\" href=\"css/fontawesome.min.css\"> di android_offline/www/index.html!")
    for forbidden in ("cdn.tailwindcss.com", "cdnjs.cloudflare.com", "fonts.googleapis.com", "api.qrserver.com"):
        if forbidden in html:
            errors.append(f"FORBIDDEN EXTERNAL CDN TERDETEKSI di index.html offline: {forbidden}")
    if errors:
        for err in errors:
            print(f"[FATAL OFFLINE AUDIT] {err}", file=sys.stderr)
        sys.exit(1)

    OFFLINE_HTML.write_text(html, encoding="utf-8")
    print(f"[SUKSES] android_offline/www/index.html disinkronkan ({len(html)/1024:.1f} KB) — 100% ZERO-CDN TERVERIFIKASI!")

    # 9. Sinkronkan juga ewd_viewer.html untuk mode 100% offline APK
    web_ewd = WEB_STATIC_DIR / "ewd_viewer.html"
    off_ewd = OFFLINE_WWW_DIR / "ewd_viewer.html"
    if web_ewd.exists():
        ewd_html = web_ewd.read_text(encoding="utf-8")
        ewd_html = re.sub(
            r'<meta\s+name="viewport"\s+content="[^"]*"\s*/?>',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=4.0, user-scalable=yes, viewport-fit=cover" />',
            ewd_html,
            count=1,
        )
        ewd_html = ewd_html.replace('href="/"', 'href="index.html"')
        off_ewd.write_text(ewd_html, encoding="utf-8")
        print(f"[SUKSES] android_offline/www/ewd_viewer.html disinkronkan ({len(ewd_html)/1024:.1f} KB)")


if __name__ == "__main__":
    sync()
