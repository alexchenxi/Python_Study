# 拿到页面原代码
# 提取和解析数据

import csv
import time
from pathlib import Path

import requests
from lxml import etree

base_dir = Path(__file__).parent

# 搜索接口：可以把 sass 换成任意关键词
keyword = "sass"
url = f"https://www.zbj.com/fw/?k={keyword}"

# 模拟浏览器请求头（完整浏览器头能绕过大部分基础反爬）
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}

resp = requests.get(url, headers=headers, timeout=15)
resp.encoding = resp.apparent_encoding

# 先保存 HTML 到本地，方便用浏览器打开调试结构
save_path = base_dir / "zbj_sass.html"
with open(save_path, "w", encoding="utf-8") as f:
    f.write(resp.text)
print(f"HTML 已保存到: {save_path}")
print(f"响应状态: {resp.status_code}, 长度: {len(resp.text)}")

# 反爬判断：如果页面包含 verify/zjs 字样，说明被拦截
if "verify.zbj.com" in resp.text or "sec.zbj.com" in resp.text:
    print("⚠️  被反爬拦截！请在浏览器中手动访问一次，完成 IP 验证后，")
    print("   复制浏览器 DevTools Network 面板中该请求的 Cookie 加入 headers 再试。")
    resp.close()
    raise SystemExit(1)

# 解析 HTML
html = etree.HTML(resp.text)

# 猪八戒价格在不同结构中出现，用通用 XPath 覆盖几种常见模式：
# 1) <span class="price">¥299</span>   
# 2) <em class="price-num">199.00</em>
# 3) 任何包含 class 带 price 的节点 + 直接文本
price_xpaths = [
    '//*[contains(@class, "price") and contains(text(), "¥")]/text()',
    '//*[contains(@class, "price")]//text()[contains(., "¥")]',
    '//*[contains(@class, "price")]/text()',
    '//em[contains(@class, "price")]/text()',
    '//span[contains(@class, "price")]/text()',
]

all_prices = []
for xp in price_xpaths:
    hits = html.xpath(xp)
    if hits:
        print(f"XPath [{xp}] 匹配到 {len(hits)} 条")
        all_prices.extend(hits)

# 去空、去重、清理多余空白
clean_prices = []
seen = set()
for p in all_prices:
    p = p.strip()
    if p and p not in seen:
        seen.add(p)
        clean_prices.append(p)

print(f"\n共收集到 {len(clean_prices)} 条价格:")
for price in clean_prices:
    print(f"  {price}")

# 写入 CSV（带时间戳，避免覆盖）
if clean_prices:
    ts = time.strftime("%Y%m%d_%H%M%S")
    csv_path = base_dir / f"zbj_{keyword}_prices_{ts}.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["价格"])
        for p in clean_prices:
            writer.writerow([p])
    print(f"\n✅ 已写入 CSV: {csv_path}")

resp.close()


