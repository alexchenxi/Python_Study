"""
把函数当作变量来用
实现方式：
  1. 装饰器
  2. 类属性
"""


class Student:
    def __init__(self):
        # 私有属性
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 0 and age <= 120:
            print("年龄已经修改！")
            self.__age = age
        else:
            print("不合法的年龄")


if __name__ == "__main__":
    s = Student()
    print(s.age)
    # s.set_age(22)

    # 已修饰，可以用属性赋值的方式来调用函数
    s.age = 20
    print(s.age)
