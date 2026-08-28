from pathlib import Path

base_dir = Path(__file__).parent

# read(num) 读取num字节
# readlines()
with open(base_dir / "read_file.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    print(content)

# readline()
with open(base_dir / "read_file.txt", "r", encoding="utf-8") as f:
    content = f.readline()
    print(content)
    content = f.readline()
    print(content)
    content = f.readline()
    print(content)
    content = f.readline()
    print(content)
