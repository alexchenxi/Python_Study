import re

# obj = re.compile(r"\d+")
# res = obj.finditer("发掘和10086，发来的肌肤10010")
# for i in res:
#     print(i.group())

s = """
  <div class="allen"><span id="1">艾伦</span></div>
  <div class="bob"><span id="2">鲍勃</span></div>
  <div class="chris"><span id="3">克里斯</span></div>
  <div class="david"><span id="4">大卫</span></div>
"""

obj = re.compile(
    r"<div class=\".*?\"><span id=\"(?P<id>\d+?)\">(?P<name>.*?)</span></div>",
    re.DOTALL,
)  # 让.能匹配换行符
res = obj.finditer(s)
for i in res:
    print(f"{i.group('name')}的id是：{i.group('id')}")
