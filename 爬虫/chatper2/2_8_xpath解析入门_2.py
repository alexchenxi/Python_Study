from pathlib import Path

from lxml import etree

base_dir = Path(__file__).parent

parser = etree.HTMLParser()
tree = etree.parse(base_dir / "xml_demo.html", parser)
# result = tree.xpath("/html/body/ol/li[1]/a/text()")
# result = tree.xpath("/html/body/ul/li/a[@href='banana']/text()")
# print(result)
ul_li_list = tree.xpath("/html/body/ul/li")
for li in ul_li_list:
    # 从每个li中提取文字信息
    result = li.xpath("./a/text()")  # 相对查找
    print(result)
    result2 = li.xpath("./a/@href")  # 获取属性值
    print(result2)

print(tree.xpath("/html/body/ol/li/a/@href"))
