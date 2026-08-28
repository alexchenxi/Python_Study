class Student:
    # 魔术方法之一：__名字__  不会手动直接调用，**在特定语法、内置函数触发时自动执行**。 __new__(cls)创建对象，分配内存；cls是类 __del__(self) 对象被垃圾回收的时候触发
    def __init__(self):
        print("-" * 10 + "init" + "-" * 10)
        self.grade = 8
        self.teacher = "Mr.Zen"

    # 类属性
    # name = "xxx"
    # age = 22

    def getGrade(self):
        print(f"His/Her grade is {self.grade}")


Bob = Student()
# 对象属性
Bob.name = "Bob"
Bob.age = 18
# 先找自己的对象属性，找不到再去类属性找
print(Bob.age)
# Bob.course = "English" 没有course会报错
Bob.getGrade()
