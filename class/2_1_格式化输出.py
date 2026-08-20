# 格式化符号

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
age = 18
name = "Tom"
weight = 75.5
stu_id = 1

print("今年我%d岁" % age)
print("我的学号是%06d" % stu_id)
