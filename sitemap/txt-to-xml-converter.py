from pathlib import Path
import re

txt_file = Path("./sitemap.txt")
xml_file = Path("./sitemap.xml")

with open(xml_file, 'w', encoding='utf-8') as xml:
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml.writelines(header)
    with open(txt_file) as file:
        url = file.readline().strip("\n")
        while url:
            short_url = re.sub(r'http(s?)://', '', url)
            url_parts = short_url.rstrip('/').split('/')
            priority = 0.7
            if len(url_parts) == 1:
                priority = 0.9
            elif len(url_parts) == 2:
                priority = 0.8
            ment = "    <url>\n" \
                   "        <loc>%s</loc>\n" \
                   "        <changefreq>weekly</changefreq>\n" \
                   "        <priority>%s</priority>\n" \
                   "    </url>\n" % (url, priority)
            xml.writelines(ment)
            url = file.readline().strip("\n")

    last = "</urlset>"
    xml.writelines(last)
