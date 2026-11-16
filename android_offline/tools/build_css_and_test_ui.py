"""
Build Local Offline CSS (app.css) & Uji Responsivitas Mobile (360px, 393px, 412px)
==================================================================================
1. Mengompilasi seluruh kelas Tailwind CSS dari `www/index.html` dan `www/js/*.js`
   ditambah aturan mobile anti-amburadul dari `src/input.css` menjadi `www/css/app.css`.
2. Menguji tampilan `www/index.html` secara headless pada lebar layar HP:
   - 360px (HP Android kecil/umum)
   - 393px (Pixel / Redmi / Poco)
   - 412px (Samsung Galaxy A/S series)
   untuk memastikan tidak ada scroll horizontal (`scrollWidth <= clientWidth`)
   di seluruh 4 tab dan seluruh fitur berfungsi tanpa koneksi internet.
"""

from pathlib import Path
import json
import re
import subprocess
import urllib.request

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
OFFLINE_DIR = ROOT_DIR / "android_offline"
WWW_DIR = OFFLINE_DIR / "www"
NODE_BIN = Path.home() / "AppData" / "Roaming" / "Antigravity" / "bin" / "agy-node.cmd"
EDGE_BIN = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")


def build_offline_css() -> None:
    # Unduh script Tailwind Play CDN sekali untuk dieksekusi di Node/Edge lokal guna mengekstrak CSS murni
    tw_script_url = "https://cdn.tailwindcss.com/3.4.14"
    req = urllib.request.Request(tw_script_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        tw_js = resp.read().decode("utf-8")

    html_text = (WWW_DIR / "index.html").read_text(encoding="utf-8")
    js_texts = "\n".join(
        p.read_text(encoding="utf-8")
        for p in (WWW_DIR / "js").glob("*.js")
        if p.name != "embedded-data.js"
    )
    custom_css = (OFFLINE_DIR / "src" / "input.css").read_text(encoding="utf-8")
    custom_css = re.sub(r"@tailwind\s+\w+;\s*", "", custom_css)

    body_match = re.search(r"<body[^>]*>(.*)</body>", html_text, flags=re.S | re.I)
    body_inner = body_match.group(1) if body_match else html_text
    # Buang tag script dari body_inner saat ekstraksi CSS agar cepat
    body_no_scripts = re.sub(r"<script\b[^>]*>.*?</script>", "", body_inner, flags=re.S | re.I)

    tmp_html = OFFLINE_DIR / "tools" / "_tw_extract.html"
    tmp_html.write_text(
        f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>{tw_js}</script>
<script>
tailwind.config = {{
  darkMode: 'class',
  theme: {{
    extend: {{
      colors: {{
        brand: {{
          50: '#f0f7ff', 100: '#e0effe', 300: '#7dd3fc', 400: '#38bdf8',
          500: '#0284c7', 600: '#0369a1', 700: '#075985', 800: '#0c4a6e',
          900: '#0f172a', 950: '#082f49'
        }},
        accent: {{ 400: '#f59e0b', 500: '#d97706', 600: '#b45309' }}
      }}
    }}
  }}
}};
</script>
</head>
<body class="bg-slate-900 text-slate-100">
{body_no_scripts}
<div class="hidden">{js_texts}</div>
</body>
</html>""",
        encoding="utf-8",
    )

    try:
        file_url = tmp_html.resolve().as_uri()
        proc = subprocess.run(
            [
                str(EDGE_BIN),
                "--headless=new",
                "--disable-gpu",
                "--virtual-time-budget=3000",
                "--dump-dom",
                file_url,
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            check=True,
        )
        styles = re.findall(r"<style[^>]*>(.*?)</style>", proc.stdout, flags=re.S)
        tw_compiled = "\n".join(styles).strip()
        if len(tw_compiled) < 5000:
            raise RuntimeError("Hasil ekstraksi CSS terlalu pendek.")
        final_css = (
            "/* AGOS Smart Diagnostik — Offline Compiled Tailwind v3.4.14 + Mobile Card Rules */\n"
            + tw_compiled
            + "\n\n"
            + custom_css
        )
        out_path = WWW_DIR / "css" / "app.css"
        out_path.write_text(final_css, encoding="utf-8")
        print(f"[SUKSES] www/css/app.css berhasil dibangun ({len(final_css)/1024:.2f} KB)")
    finally:
        if tmp_html.exists():
            tmp_html.unlink()


def verify_mobile_viewports() -> None:
    print("\n=== UJI TAMPILAN MOBILE HP (360px, 393px, 412px) DI SEMUA 4 TAB ===")
    orig_html = (WWW_DIR / "index.html").read_text(encoding="utf-8")
    test_html = WWW_DIR / "_viewport_test.html"
    probe_script = """
<script>
window.addEventListener('load', async () => {
  await new Promise(r => setTimeout(r, 300));
  await loadSample('K001');
  await new Promise(r => setTimeout(r, 200));
  document.documentElement.classList.add('agos-mobile-sim');
  const report = {};
  for (const w of [360, 393, 412]) {
    document.documentElement.style.maxWidth = w + 'px';
    document.documentElement.style.width = w + 'px';
    document.body.style.maxWidth = w + 'px';
    document.body.style.width = w + 'px';
    report[w] = {};
    for (const t of ['diagnostic', 'database', 'manuals', 'tools']) {
      switchTab(t);
      await new Promise(r => setTimeout(r, 100));
      const rectW = Math.round(document.body.getBoundingClientRect().width);
      const sw = document.body.scrollWidth;
      report[w][t] = { clientWidth: rectW, scrollWidth: sw, overflowX: sw > w + 1 };
    }
  }
  const el = document.createElement('pre');
  el.id = 'agos-viewport-report';
  el.textContent = JSON.stringify(report);
  document.body.appendChild(el);
});
</script>
"""
    test_html.write_text(orig_html.replace("</body>", probe_script + "\n</body>"), encoding="utf-8")
    try:
        proc = subprocess.run(
            [
                str(EDGE_BIN),
                "--headless=new",
                "--disable-gpu",
                "--virtual-time-budget=4500",
                "--dump-dom",
                test_html.resolve().as_uri(),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            check=True,
        )
        m = re.search(r'<pre id="agos-viewport-report">(.*?)</pre>', proc.stdout, flags=re.S)
        if not m:
            raise RuntimeError("Gagal membaca laporan viewport")
        rep = json.loads(m.group(1))
        for width, tabs_data in rep.items():
            print(f"Lebar Layar HP {width}px:")
            for tab_name, info in tabs_data.items():
                status = "LULUS (Rapi, 0 Scroll Samping)" if not info["overflowX"] else "OVERFLOW!"
                print(
                    f"  - Tab {tab_name:<12}: width={info['clientWidth']}px, "
                    f"scrollWidth={info['scrollWidth']}px -> {status}"
                )
    finally:
        if test_html.exists():
            test_html.unlink()


if __name__ == "__main__":
    build_offline_css()
    verify_mobile_viewports()
