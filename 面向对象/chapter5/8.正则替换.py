import re

s = "开心你就大声笑,哈哈,呵呵,嘿嘿,嘻嘻,啦啦啦"
#
result = re.compile("哈|呵|嘿|嘻").sub("❤", s)
print(result)
print("*" * 23)

# 新版API
result = re.sub("哈|呵|嘿|嘻", "额", s)
print(result)
