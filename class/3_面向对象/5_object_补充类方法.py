"""
静态方法：类似于类方法
1. @staticmethod
2. 静态方法是无需传参cls self
3. 只能访问类的属性/方法
4. 加载时机和类方法一样


总结：逻辑上高度归属该类，但不碰类、实例任何状态

"""


class Person:
    # private私有化属性 __xxx
    __age = 18

    def __init__(self, name):
        self.name = name

    def show_age(self):
        print(Person.age)

    @classmethod
    def test(cls):
        print("类方法test")

    @classmethod
    def minus_age(cls):
        print("年龄减一")
        cls.__age -= 1

    @classmethod
    def get_age(cls):
        print(cls.__age)

    @staticmethod  # 逻辑上高度归属该类，但不碰类、实例任何状态
    def hello():
        print(Person.__age)


# 想要修改age
# Person.test()
Person.get_age()
Person.minus_age()
Person.get_age()

# p1 = Person("Bob")
# p1.hello()

Person.hello()
