import re

result = re.match(r"\d+.*", "abc123xyz")
result = re.search(r"\d+.*", "abc123xyz")  # 123x

result = re.search(r"^\d+.*", "abc123xyz")  # 未匹配


# 需求2：检验字符串必须以数字开头，以任意的3个字母结尾
result = re.search(r"^\d+.*[a-zA-Z]{3}", "1__abc")
result = re.search(r"^\d+.*[a-zA-Z]{3}", "123你好abc123123")  # 123你好abc
result = re.search(r"^\d+.*[a-zA-Z]{3}$", "123你好abc123123")  # 未匹配

# 手机号，11位，纯数字，第一位必须是1，第二位3到9
result = re.search(r"^1[3-9]\d{9}$", "1551404034a")

print(result.group() if result else "未匹配")
