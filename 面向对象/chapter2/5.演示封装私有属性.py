# 封装 隐藏对象的属性和方法，仅对外提供公共的访问方法
# 函数，类 都是封装
# 好处：1.提高安全性 私有化
# 2. 提高复用性 函数
# 代码量增加了


class Teacher:
    def __init__(self):
        self.skill = "Python"
        self.__money = 200000  # 私有
        self.money = 1999

    def code(self):
        print(f'I have skill "{self.skill}".')

    # 针对私有属性，提供公共的访问方式
    def show_money(self):
        return self.__money

    def show_public_money(self):
        return self.money


class Student(Teacher):
    pass


s1 = Student()
# s1.code()  # ok
# print(s1.__money)  # 报错
print(s1.show_money())
s1.__money = -100
print(s1.__money)  # 此时s1创建一个同名变量__money
print(s1.show_money())  # 数值不变
print("*" * 34)
print(s1.show_public_money())
s1.money = -1000  # 对象修改了属性，生效
print(s1.show_public_money())
