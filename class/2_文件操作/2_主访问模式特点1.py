from pathlib import Path

base_dir = Path(__file__).parent
# r：如果文件不存在，报错；不支持写入，只读

# f = open(base_dir / "test.txt", "r")
with open(base_dir / "test.txt", "r", encoding="utf-8") as f:
    print(f.read())

# w：只写，如果文件不存在，新建；写入会覆盖原内容
# f1 = open(base_dir / "abc.txt", "w")
with open(base_dir / "abc.txt", "w", encoding="utf-8") as f1:
    f1.write("abc")

# a：追加，如果不存在，新建
with open(base_dir / "abc.txt", "a", encoding="utf-8") as f2:
    f2.write(" haha")

# 访问模式可以省略，默认为r
# with open(base_dir / "null.txt") as f3:
