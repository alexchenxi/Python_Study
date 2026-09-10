"""
把函数当作变量来用
实现方式：
  1. 装饰器
  2. 类属性

  类属性名=property(获取值的函数名，设置值的函数名)
"""


class Student:
    def __init__(self):
        # 私有属性
        self.__age = 18

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # 封装上述的公共方法为 类属性
    # 参1：获取值 参2：设置值
    age = property(get_age, set_age)


if __name__ == "__main__":
    s = Student()
    print(s.age)
    # s.set_age(22)

    # 已修饰，可以用属性赋值的方式来调用函数
    s.age = 20
    print(s.age)
