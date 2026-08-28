from pathlib import Path

base_dir = Path(__file__).parent
# seek(偏移量，起始位置) 0开头1当前2结尾


with open(base_dir / "read_file.txt", "r+", encoding="utf-8") as f:
    # 中文一个汉字占3个字节
    f.seek(6, 0)
    content = f.read()
    print(content)

print("#" * 50)
with open(base_dir / "read_file.txt", "a+", encoding="utf-8") as f1:
    # 中文一个汉字占3个字节
    # f1.seek(0, 1)
    f1.seek(0)
    content = f1.read()
    print(content)
