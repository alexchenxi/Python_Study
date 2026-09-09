"""
生成器：
  概述：
    基于数据规则，用一部分生成一部分，而不是一下子生成完成
  目的：
    节省大量内存
  实现：
    1. 推导式
    2. yield
"""

import sys

# 1.生成1~10之间的整数
my_generator = (i for i in range(1, 11))
print(my_generator)
print(type(my_generator))

# 2.生成1~10之间的偶数
my_generator2 = (i for i in range(1, 11) if i % 2 == 0)
print(my_generator2)

# 3. 如何从生成器中获取数据
# 1. next()
print(next(my_generator2))
for i in my_generator2:
    print(i)

# 验证 生成器的目的 可以减少内存占用
my_list = [i for i in range(10000000)]
my_gt3 = (i for i in range(1000000))

print(f"my_list占用：{sys.getsizeof(my_list)}")
print(f"my_gt3占用：{sys.getsizeof(my_gt3)}")
