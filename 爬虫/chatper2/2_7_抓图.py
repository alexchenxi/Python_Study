import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/priceDetail.html"
res = requests.get(url)
res.encoding = "utf-8"
base_dir = Path(__file__).parent
print(res.text)
main_page = BeautifulSoup(res.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")
for a in alist:
    href = a.get("href")
    child_page_res = requests.get(href)
    child_page_res.encoding = "utf-8"
    text = child_page_res.text

    child_page = BeautifulSoup(text, "html.parser")
    p = child_page.find("p", align="center")
    img = p.find("img")
    image_src = img.get("src")

    image_res = requests.get(image_src)
    image_name = image_res.split("/")[-1]

    with open(base_dir / "images/" + image_name, mode="w", encoding="utf-8-sig") as f:
        f.write(image_res.content)

    print("over!!", image_name)
    time.sleep(1)
print("All saved!!")
