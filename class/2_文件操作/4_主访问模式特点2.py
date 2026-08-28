from pathlib import Path

base_dir = Path(__file__).parent

# r+：r没有文件则报错；文件指针在开头
with open(base_dir / "read_file.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    print(content)

# w+：没有文件则创建；w特点：文件指针在开头，用新内容覆盖
with open(base_dir / "write_file.txt", "w+", encoding="utf-8") as f1:
    content = f1.read()
    print(content)

# a+：没有文件则创建；文件指针在结尾，无法读取数据
