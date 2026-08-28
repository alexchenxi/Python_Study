import os
from pathlib import Path

base_dir = Path(__file__).parent
# os.rename(base_dir / "abc.txt", base_dir / "abcde.txt")

# os.remove(base_dir / "abcde.txt")


# mkdir() 创建
# os.mkdir(base_dir / "aa")

# rmdir() 删除
# os.rmdir(base_dir / "aa")

# getcwd() 获取当前目录

print(os.getcwd())

# chdir() 改变目录路径
# os.chdir(base_dir / "aa")
# os.mkdir("bb")

os.chdir(base_dir / "aa")
print(base_dir)
