import csv
import math
import re
from pathlib import Path

import requests

base_dir = Path(__file__).parent
num = min(int(input("请输入你想获取的排名前几的电影：")), 250)
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}

obj = re.compile(
    r'<div class="info">[\s\S]*?<span class="title">(?P<name>.*?)</span>'
    r"[\s\S]*?<br>\s*(?P<year>\d{4})&nbsp;"
    r"[\s\S]*?<span>(?P<comments>\d+)人评价</span>",
    re.DOTALL,
)

# 豆瓣每页25条，按页数向上取整
page_count = math.ceil(num / 25)
collected = 0
with open(base_dir / "data.csv", mode="w", encoding="utf-8-sig", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["电影名", "上映时间", "评论人数"])
    for page_no in range(page_count):
        start = page_no * 25
        url = f"https://movie.douban.com/top250?start={start}"
        res = requests.get(url, headers=headers)
        for i in obj.finditer(res.text):
            if collected >= num:
                break
            csvwriter.writerow(i.groupdict().values())
            collected += 1
        res.close()
        if collected >= num:
            break

print(f"done! 共写入 {collected} 条数据")
