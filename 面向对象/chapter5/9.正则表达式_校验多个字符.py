import re

# *前边的内容，出现0~无数次
result = re.match(".*hm.*", "abchm123")
result = re.match(".*hm.*", "hm123")

# + 至少一次
result = re.match(".+hm.*", "ahm12312321")
result = re.match(".+hm.*", "hm12312321")

# ? 0或者1次
# {n} {n,} {n,m}
print(result.group() if result else "未找到匹配")
