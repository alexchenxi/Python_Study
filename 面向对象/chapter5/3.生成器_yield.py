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


def my_fun():
    yield from range(1, 11)


my_generator = my_fun()
for i in my_generator:
    print(i)
