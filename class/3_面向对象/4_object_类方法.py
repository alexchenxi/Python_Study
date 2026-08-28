class Dog:
    # name = "Puppy"
    # 类方法只能使用类属性，也不能调用普通方法
    # 作用：做一些对象创建之前的操作

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"{self.name} is {self.age} years old.")

    @classmethod  # 装饰器 定义类方法
    def test(cls):
        print("类方法test被调用")
        print(cls)
        # print(cls.name)


d1 = Dog("Beibei", 1)

d1.get_info()
# d1.test()

Dog.test()
