class Teacher:
    def __init__(self):
        self.skill = "Python"

    def code(self):
        print(f"I use {self.skill} to program!")


class School:
    def __init__(self):
        self.skill = "Javascript"

    def code(self):
        print(f"I use {self.skill} to program!")


class Student(School, Teacher):
    pass
    # 当一个类有多个父类时，默认使用第一个父类的同名属性和方法，可以用类名.__mro__属性或者类名.mro()方法查看调用顺序 method resolution order


s1 = Student()
s1.code()
print(Student.__mro__)
