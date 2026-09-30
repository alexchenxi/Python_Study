# 按照requests
# pip install requests
# https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

import requests
from pathlib import Path

base_dir = Path(__file__).parent
url = "https://movie.douban.com/j/chart/top_list"
param = {"type": "24", "interval_id": "100:90", "action": "", "start": 0, "limit": 20}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}
res = requests.get(url, params=param, headers=headers)
for i in res.json():
    print(i)
res.close()
