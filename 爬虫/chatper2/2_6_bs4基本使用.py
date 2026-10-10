import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/priceDetail.html"
res = requests.get(url)
base_dir = Path(__file__).parent
# 解析HTML
with open(base_dir / "菜价.csv", mode="w", encoding="utf-8-sig", newline="") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["商品名", "最低价"])
# 1.把页面原代码转换为bs4对象
    page = BeautifulSoup(res.text, "html.parser")
    # 2. 从bs4对象中提取需要的信息
    # find(标签，属性=属性值，属性=属性值)
    table = page.find("tbody", id="tableBody", class_="ul")
    trs = table.find_all("tr")
    for tr in trs:
        for td in tr.find_all("td"):
            name = td[0].text
            low = td[1].text
            print(name, low)
            csvwriter.writerow([name, low])
    res.close()
