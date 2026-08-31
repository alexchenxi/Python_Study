# a继承b,b继承c
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


class Student(Teacher, School):
    def __init__(self):
        self.skill = "Golang"

    def code(self):
        print(f"I use {self.skill} to program!")

    def teacher_code(self):
        Teacher.__init__(self)  # 不可少
        Teacher.code(self)

    def school_code(self):
        School.__init__(self)
        School.code(self)


class MiniStudent(Student):
    pass


if __name__ == "__main__":
    ms1 = MiniStudent()
    ms1.code()
    ms1.teacher_code()
    ms1.school_code()
