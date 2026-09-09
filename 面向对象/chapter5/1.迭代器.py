"""
自定义迭代器

迭代器介绍：
  概述：
    迭代器是一个对象，提供了一个访问集合元素的方法，不暴露集合的底层实现
    自定义的类，只要重写了__iter__() 和 __next__() 方法，就可以成为 迭代器
  目的：
    1. 隐藏底层逻辑，让使用更方便
    2. 惰性加载，用的时候才获取
"""

for i in range(1, 6):
    print(i)
print("*" * 23)


class MyIterator:
    def __init__(self, start, end):
        self.current_value = start
        self.end = end

    # 通过__iter__魔法方法，返回当前值，并更新当前值
    def __iter__(self):
        return self

    # 重写next魔法方法，返回当前值，并更新当前值
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration  # 抛出异常，迭代结束

        # value = self.current_value
        # self.current_value += 1
        # return value
        self.current_value += 1
        return self.current_value - 1


for i in MyIterator(1, 6):
    print(i)
print("*" * 23)

my_itr = MyIterator(10, 13)
print(next(my_itr))
