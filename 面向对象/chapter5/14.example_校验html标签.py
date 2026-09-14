import re

html_s = "<html><h1>我是html页面</h1></html>"

# \1表示引用第N组分组规则
# result = re.match(r"^<([a-zA-Z]{1,4})>.*</\1>$", html_s)

# 引入分组概念
result = re.match(r"^<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>$", html_s)
# 命名(?P<name>xxxxxxx)
# 引用(?P=name)
result = re.match(
    r"^<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>.*</(?P=B)></(?P=A)>$", html_s
)

if result:
    print(result.group())
else:
    print("不合法")
