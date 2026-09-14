import re

s = "qq:123456"

result = re.match(r"^qq:(\d{6,11})$", s)

if result:
    print(result.group())
    print(result.group(0))
    print("*" * 23)

    print(result.group(1))
else:
    print("不合法")
