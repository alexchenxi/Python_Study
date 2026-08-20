import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

age = int(input("请输入年龄："))
if age>=18:
    print(f"您输入的年龄是{age},您是成年人")
elif age>=60:
    print(f"您输入的年龄是{age},您是老年人")
else:
    print(f"您输入的年龄是{age},您是未成年人")
print("End")  