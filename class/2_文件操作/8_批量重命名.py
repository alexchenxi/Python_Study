import os
from pathlib import Path

# 构造条件的数据
flag = 23

base_dir = Path(__file__).parent

# 1.找到所有文件
file_list = os.listdir(base_dir)
print(file_list)

# 2.构造名字

for i in file_list:
    if flag == 1:
        new_name = "Python_" + i
    else:
        new_name = i[len("Python_") :]
    os.rename(base_dir / i, base_dir / new_name)
# 3.重命名
