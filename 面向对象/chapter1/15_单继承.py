class Teacher:
    def __init__(self):
        self.skill = "Python"

    def code(self):
        print(f"I use {self.skill} to program!")


class Student(Teacher):
    def __init__(self):
        self.skill = "Python"

    def code(self):
        print(f"I use {self.skill} to program!")


s1 = Student()
s1.code()
