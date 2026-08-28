"""
面向对象：
好处：
 对象的结合 ---> 共同特征

 多个对象 ----> 提取对象的共同特征和动作--->封装到一个类里
"""

# 类要求首字母大写+驼峰
"""
class TestClass[(父类)]：
    属性：
    方法：
"""


class Phone:
    type = "SmartPhone"
    Brand = "IPhone"

    # 类方法的第一个参数必须为self,为对象本身
    def call(self, duration):
        print(f"I({self.name}) can make phone call for {duration} seconds")


print(Phone)
IPhone = Phone()
IPhone.name = "Big Phone"
print(IPhone.type)
IPhone.call(100)
