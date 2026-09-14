import re

email = "abcd@163.com"

result = re.match(r"^[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$", email)
if result:
    print(result.group(0))
    print(result.group(1))
else:
    print("邮箱不合法")
