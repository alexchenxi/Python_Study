# f-字符串
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
age = 18
name = "Tom"
weight = 75.5

print(f"我的名字是{name},我今年{age}岁，我的体重是{weight}")
