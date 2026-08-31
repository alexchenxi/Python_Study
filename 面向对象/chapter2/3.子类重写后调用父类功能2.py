# super().父类方法()，有则使用，没有则安卓MRO寻找
class Teacher:
    # def __init__(self):
    #     self.skill = "Python"

    # def code(self):
    #     print(f"I use {self.skill} to program!")
    pass


class School:
    def __init__(self):
        self.skill = "Javascript"

    def code(self):
        print(f"I use {self.skill} to program!")


class Student(Teacher, School):
    def __init__(self):
        self.skill = "Golang"

    def code(self):
        print(f"I use {self.skill} to program!")

    def teacher_code(self):
        super().__init__()
        super().code()


s1 = Student()
s1.code()
print(Student.__mro__)
s1.teacher_code()  # javascript
