import csv
import re
from pathlib import Path

import requests

base_dir = Path(__file__).parent
url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
page = res.text
print(page)

obj = re.compile(
    r'<div class="info">[\s\S]*?<span class="title">(?P<name>.*?)</span>'
    r"[\s\S]*?<br>\s*(?P<year>\d{4})&nbsp;"
    r"[\s\S]*?<span>(?P<comments>\d+)人评价</span>",
    re.DOTALL,
)
result = obj.finditer(page)
with open(base_dir / "data.csv", mode="w", encoding="utf-8-sig", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["电影名", "上映时间", "评论人数"])
    for i in result:
        dic = i.groupdict()
        csvwriter.writerow(dic.values())
# with open(base_dir / "douban250.html", mode="w", encoding="utf-8") as f:
#     f.write(res.text)


res.close()
