# 通过编写程序来获取互联网上的内容 模拟浏览器
# 需求：用程序模拟浏览器，输入网址，从中获取资源

from urllib.request import urlopen
from pathlib import Path

base_dir = Path(__file__).parent
url = "https://bang.tx3.163.com/bang/role/60_36692"
res = urlopen(url).read().decode("utf-8")
print(res)

with open(base_dir / "myhtml.html", mode="w", encoding="utf-8") as f:
    f.write(res)
