import os
from datetime import datetime

BASE_URL = "https://solaemanachmad.github.io/panduan_pmpsti"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
OUTPUT_FILE = os.path.join(DOCS_DIR, "sitemap.xml")

urls = []

for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith(".html"):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, DOCS_DIR)
            url = f"{BASE_URL}/{rel_path.replace(os.sep, '/')}"
            
            if "404.html" in url:
                continue

            urls.append(url)

urls = sorted(urls)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n')

    for url in urls:
        f.write("  <url>\n")
        f.write(f"    <loc>{url}</loc>\n")
        f.write(f"    <lastmod>{datetime.today().date()}</lastmod>\n")
        f.write("    <changefreq>monthly</changefreq>\n")
        f.write("    <priority>0.8</priority>\n")
        f.write("  </url>\n\n")

    f.write("</urlset>\n")

print(f"✅ Sitemap generated: {OUTPUT_FILE}")