# xpath是XML文档中搜索内容的一门语言
# html是XML的一个子集

# lxml模块
# pip install lxml -i xxx
# xpath解析
from lxml import etree

xml = """
<books>
    <book id="1">
        <title>XML入门教程</title>
        <author>张三</author>
        <author>李四</author>
        <author>王五</author>
        <div>
          <author>王五2</author>
                  <div>
          <author>王五3</author>
        </div>
        </div>
        <price>39.9</price>
    </book>
    <book id="2">
        <title>前端开发手册</title>
        <author>李四</author>
        <price>59.0</price>
    </book>
</books>
"""

tree = etree.XML(xml)

result = tree.xpath(
    "/books/book/title/text()"
)  # /表示层级关系，第一个/是根节点 text()取文本

result = tree.xpath("/books/book//author/text()")  # // 表示取后代

print(result)
