#!/usr/bin/env python3
"""生成 index.html — 台美報稅官網入口(logo 內嵌 base64,零外部資源)。"""
import base64
from pathlib import Path

LOGO = Path("/Users/dtsneg/Documents/Projects.nosync/agentcore-demo/taxagent/frontend/assets/logo.png")
API = "https://6ozxlfj5pi.execute-api.us-east-1.amazonaws.com/lead"
THREADS = "https://www.threads.net/@taiwan.us.tax"

logo_b64 = base64.b64encode(LOGO.read_bytes()).decode()

html = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>台美報稅 — Taiwan-US Tax</title>
<meta name="description" content="為在美台灣人與雙重身分者,把 IRS 與國稅局之間的灰色地帶,整理成一份可以放心遞出去的申報。誠實分享・服務籌備中。">
<link rel="icon" href="data:image/png;base64,{logo_b64}">
<style>
:root{{
  /* 甲 · 藍墨紅章 Blue Ink · Red Seal — 藍墨書寫,紅泥落印;黑白印信不動 */
  --paper:#F5F6F7; --paper-hi:#FBFCFD; --white:#FFF;
  --ink:#101214; --ink-soft:#33383D; --stone:#5F6A72; --stone-2:#8B959C;
  --line:#D4DADD; --line-2:#BAC3C8;
  --indigo:#1F4E79; --indigo-deep:#153A5B;
  --seal:#9E3B31; --seal-deep:#7C2D24;
  --kai:"Kaiti TC","STKaiti","BiauKai","Songti TC","Noto Serif TC",serif;
  --sans:"PingFang TC","Noto Sans TC",-apple-system,sans-serif;
  --cond:"Arial Narrow","Helvetica Neue Condensed","Roboto Condensed",sans-serif;
}}
*{{box-sizing:border-box;margin:0}}
body{{background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.72}}
.wrap{{max-width:720px;margin:0 auto;padding:clamp(1.5rem,5vw,3rem)}}
.label{{font-family:var(--cond);text-transform:uppercase;letter-spacing:.18em;font-size:.7rem;color:var(--stone)}}

/* Hero */
.hero{{text-align:center;padding:3.2rem 0 2.2rem}}
.hero img{{width:150px;height:150px;filter:drop-shadow(0 16px 30px rgba(16,18,20,.3))}}
.hero h1{{font-family:var(--kai);font-size:2.1rem;font-weight:700;margin-top:1.2rem;letter-spacing:.12em}}
.hero .en{{margin-top:.4rem}}
.hero p.essence{{margin:1.4rem auto 0;max-width:34em;color:var(--ink-soft);text-align:left}}
.badge{{display:inline-block;margin-top:1.2rem;border:1px solid var(--seal);color:var(--seal-deep);
  font-size:.78rem;padding:.25rem .9rem;letter-spacing:.14em}}

/* 誠準穩正 */
.values{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin:2.4rem 0}}
.values div{{background:var(--paper-hi);padding:1rem .6rem;text-align:center}}
.values b{{font-family:var(--kai);font-size:1.25rem;display:block;color:var(--indigo-deep)}}
.values span{{font-size:.72rem;color:var(--stone)}}

/* Cards */
.card{{background:var(--paper-hi);border:1px solid var(--line);padding:1.8rem;margin-top:1.6rem}}
.card h2{{font-family:var(--kai);font-size:1.3rem;margin:.4rem 0 1rem}}
input,textarea{{width:100%;background:var(--white);border:1px solid var(--line-2);border-radius:2px;
  padding:.7rem .9rem;font-family:var(--sans);font-size:.95rem;color:var(--ink);margin-top:.9rem}}
textarea{{min-height:110px;resize:vertical}}
input:focus,textarea:focus{{outline:none;border-color:var(--indigo)}}
button{{margin-top:1.1rem;width:100%;background:var(--indigo);color:var(--paper-hi);border:none;
  padding:.85rem;font-size:1rem;font-family:var(--kai);letter-spacing:.3em;cursor:pointer;border-radius:2px}}
button:hover{{background:var(--indigo-deep)}}
button:disabled{{background:var(--stone-2);cursor:wait}}
.hp{{position:absolute;left:-9999px;opacity:0;height:0;overflow:hidden}}
.ok{{display:none;border:1px solid var(--seal);color:var(--seal-deep);padding:1rem;margin-top:1rem;
  font-family:var(--kai);text-align:center;font-size:1.05rem}}
.err{{display:none;color:var(--seal-deep);font-size:.85rem;margin-top:.6rem}}

.threads a{{color:var(--indigo-deep);font-weight:600;text-decoration:none;border-bottom:1px solid var(--indigo)}}
.threads a:hover{{color:var(--indigo)}}
.tool .tag{{float:right;border:1px solid var(--line-2);color:var(--stone);font-size:.7rem;
  font-family:var(--cond);text-transform:uppercase;letter-spacing:.16em;padding:.2rem .6rem}}
.tool p{{color:var(--ink-soft);font-size:.92rem}}
.tool .note{{margin-top:.8rem;font-size:.82rem;color:var(--stone)}}

footer{{margin:3rem 0 2rem;border-top:1px solid var(--line);padding-top:1.2rem;
  font-size:.75rem;color:var(--stone-2);text-align:center;line-height:1.9}}
</style>
</head>
<body>
<div class="wrap">

  <div class="hero">
    <img src="data:image/png;base64,{logo_b64}" alt="台美報稅印信標誌">
    <h1>台美報稅</h1>
    <div class="label en">Taiwan-US Tax · Cross-Border Filing</div>
    <p class="essence">為在美台灣人與雙重身分者而生:把 IRS 與國稅局之間那片沒人說得清的灰色地帶,整理成一份蓋了章、可以放心遞出去的申報。</p>
    <div class="badge">誠實分享 ・ 服務籌備中</div>
  </div>

  <div class="values">
    <div><b>誠</b><span>Honest</span></div>
    <div><b>準</b><span>Precise</span></div>
    <div><b>穩</b><span>Calm</span></div>
    <div><b>正</b><span>Official</span></div>
  </div>

  <div class="card">
    <div class="label">Get in Touch · 預約洽詢</div>
    <h2>留下 Email 與您的初步需求</h2>
    <p style="color:var(--ink-soft);font-size:.92rem">綠卡/公民海外申報、FBAR/FATCA、台灣公司 CFC/GILTI、跨境贈與——留下您的情況,籌備期間我們親自回信。</p>
    <form id="f">
      <input type="email" id="email" placeholder="您的 Email" required>
      <textarea id="need" placeholder="初步需求(例:我是綠卡持有人住台北,想了解台灣薪資與台股在美國怎麼申報…)"></textarea>
      <input class="hp" type="text" id="website" tabindex="-1" autocomplete="off">
      <button id="btn" type="submit">送 出</button>
      <div class="err" id="err"></div>
    </form>
    <div class="ok" id="ok">✓ 已收到,如同一枚落好的印。我們會盡快回信。</div>
  </div>

  <div class="card threads">
    <div class="label">Main Channel · 主要聯繫</div>
    <h2>Threads @taiwan.us.tax</h2>
    <p style="font-size:.92rem;color:var(--ink-soft)">日常的誠實分享與問答都在這裡:<a href="{THREADS}" target="_blank" rel="noopener">threads.net/@taiwan.us.tax →</a></p>
  </div>

  <div class="card tool">
    <span class="tag">Beta · 測試中</span>
    <div class="label">Coming Soon · 次要服務</div>
    <h2>專業台美雙邊分析工具</h2>
    <p>AI 檢索台灣 14 部稅法與美國 16 份 IRS 文件,逐條引用、逐步試算「分配 vs 保留」「FEIE vs FTC」等跨境情境,並附完整參考文獻。</p>
    <p class="note">目前為受邀測試(邀請碼制)。想搶先體驗,請在上方表單留下 Email 並註明「試用」。</p>
  </div>

  <footer>
    台美報稅 Taiwan-US Tax ・ 服務籌備中,尚未持照,正與持照會計師洽談合作。<br>
    本站內容與工具皆為法規資訊分享,非專業稅務建議。 Research aid, not professional tax advice.
  </footer>
</div>

<script>
document.getElementById('f').addEventListener('submit', async (e) => {{
  e.preventDefault();
  const btn = document.getElementById('btn'), err = document.getElementById('err');
  btn.disabled = true; err.style.display = 'none';
  try {{
    const r = await fetch('{API}', {{
      method: 'POST',
      headers: {{'content-type': 'application/json'}},
      body: JSON.stringify({{
        email: document.getElementById('email').value,
        need: document.getElementById('need').value,
        website: document.getElementById('website').value,
        source: 'landing',
      }}),
    }});
    const d = await r.json();
    if (d.ok) {{
      document.getElementById('f').style.display = 'none';
      document.getElementById('ok').style.display = 'block';
    }} else {{ throw new Error(d.error || 'failed'); }}
  }} catch (ex) {{
    err.textContent = '送出失敗:' + ex.message + ',請稍後再試或直接到 Threads 私訊。';
    err.style.display = 'block';
    btn.disabled = false;
  }}
}});
</script>
</body>
</html>
"""
out = Path(__file__).parent / "index.html"
out.write_text(html, encoding="utf-8")
print("wrote", out, len(html), "bytes")
