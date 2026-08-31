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
    def __init__(self):
        self.skill = "Golang"

    def code(self):
        print(f"I use {self.skill} to program!")

    def teacher_code(self):
        Teacher.__init__(self)  # 不可少
        Teacher.code(self)

    def school_code(self):
        School.code(self)


s1 = Student()
s1.code()
# print(Student.__mro__)
s1.teacher_code()
s1.code()
