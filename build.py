#!/usr/bin/env python3
"""生成 index.html — 台美報稅官網(logo 內嵌 base64,零外部資源)。

版面與文案在 template.html;本檔只負責把 logo、API 端點、Threads 連結填進去。
"""
import base64
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
# 導覽列與分頁圖示用的小印信(TW／US 加分隔線)。四字原版印信在 taxagent/frontend/assets/logo.png,留給大圖場合。
LOGO = HERE / "logo-mark-128.png"  # 內嵌用小圖;512px 原檔是 logo-mark.png
# 留資端點。Cloudflare 版走同源 /api/leads(worker.js 用 service binding 轉給 taxagent Worker,寫進 R2)。
# 根目錄的 index.html 是 GitHub Pages 時代的產物,切換完成前仍指向舊的 AWS 端點,行為不變。
API_CLOUDFLARE = "/api/leads"
API_LEGACY = "https://6ozxlfj5pi.execute-api.us-east-1.amazonaws.com/lead"
THREADS = "https://www.threads.net/@taiwan.us.tax"
THREADS_ICON = "M12.186 24h-.007c-3.581-.024-6.334-1.205-8.184-3.509C2.35 18.44 1.5 15.586 1.472 12.01v-.017c.03-3.579.879-6.43 2.525-8.482C5.845 1.205 8.6.024 12.18 0h.014c2.746.02 5.043.725 6.826 2.098 1.677 1.29 2.858 3.13 3.509 5.467l-2.04.569c-1.104-3.96-3.898-5.984-8.304-6.015-2.91.022-5.11.936-6.54 2.717C4.307 6.504 3.616 8.914 3.589 12c.027 3.086.718 5.496 2.057 7.164 1.43 1.783 3.631 2.698 6.54 2.717 2.623-.02 4.358-.631 5.8-2.045 1.647-1.613 1.618-3.593 1.09-4.798-.31-.71-.873-1.3-1.634-1.75-.192 1.352-.622 2.446-1.284 3.272-.886 1.102-2.14 1.704-3.73 1.79-1.202.065-2.361-.218-3.259-.801-1.063-.689-1.685-1.74-1.752-2.964-.065-1.19.408-2.285 1.33-3.082.88-.76 2.119-1.207 3.583-1.291a13.853 13.853 0 0 1 3.02.142c-.126-.742-.375-1.332-.75-1.757-.513-.586-1.308-.883-2.359-.89h-.029c-.844 0-1.992.232-2.721 1.32L7.734 7.847c.98-1.454 2.568-2.256 4.478-2.256h.044c3.194.02 5.097 1.975 5.287 5.388.108.046.216.094.321.142 1.49.7 2.58 1.761 3.154 3.07.797 1.82.871 4.79-1.548 7.158-1.85 1.81-4.094 2.628-7.277 2.65Zm1.003-11.69c-.242 0-.487.007-.739.021-1.836.103-2.98.946-2.916 2.143.067 1.256 1.452 1.839 2.784 1.767 1.224-.065 2.818-.543 3.086-3.71a10.5 10.5 0 0 0-2.215-.221z"

import shutil

template = (HERE / "template.html").read_text(encoding="utf-8")

# FAQ 結構化資料直接從頁面上的 <details> 產生,文案只維護一處。
faq = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", template)
assert faq, "template.html 找不到 FAQ"
JSONLD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebSite", "name": "台美報稅 Taiwan-US Tax", "url": "https://taiwanustax.com/", "inLanguage": "zh-Hant"},
    {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in faq]},
]}, ensure_ascii=False).replace("</", "<\\/")


def render(api: str) -> str:
    html = template
    for token, value in {
        "__LOGO__": base64.b64encode(LOGO.read_bytes()).decode(),
        "__API__": api,
        "__THREADS__": THREADS,
        "__THREADS_ICON__": THREADS_ICON,
        "__JSONLD__": JSONLD,
    }.items():
        assert token in html, f"template.html 少了 {token}"
        html = html.replace(token, value)
    assert "__" not in html.replace("__proto__", ""), "還有沒填的 placeholder"
    return html


# 1) Cloudflare:dist/ 是 Worker 靜態資產目錄,只放要公開的檔案。
DIST = HERE / "dist"
shutil.rmtree(DIST, ignore_errors=True)
DIST.mkdir()
(DIST / "index.html").write_text(render(API_CLOUDFLARE), encoding="utf-8")
for name in ["404.html", "robots.txt", "sitemap.xml", "_headers", "favicon-32.png", "icon-192.png",
             "apple-touch-icon.png", "og.png", "logo-mark-128.png", "logo-mark.png"]:
    shutil.copy2(HERE / name, DIST / name)
print("wrote", DIST, sorted(p.name for p in DIST.iterdir()))

# 2) GitHub Pages(舊):根目錄 index.html,切換完成後可刪。
out = HERE / "index.html"
out.write_text(render(API_LEGACY), encoding="utf-8")
print("wrote", out, out.stat().st_size, "bytes")
