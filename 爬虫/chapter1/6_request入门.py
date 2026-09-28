# 按照requests
# pip install requests
# https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

import requests
from pathlib import Path

base_dir = Path(__file__).parent
query = input("Please input the content you want to query...")
url = f"https://www.sogou.com/web?query={query}"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res.text)
with open(base_dir / f"{query}.html", mode="w", encoding="utf-8") as f:
    f.write(res.text)
