# 定义一个学生类
# 要求：
# 1. 属性包括学生姓名、学号，以及语数外成绩
# 2. 能够设置学生某科目的成绩
# 3. 能够打印该学生的所有科目成绩
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.scores = {"Chinese": 0, "Math": 0, "English": 0}

    def set_score(self, course, score):
        self.scores[course] = score

    def print_score(self):
        print(f"Stuent {self.name} (id: {self.id})'s scores are: ")
        for i in self.scores:
            print(f"{i}: {self.scores[i]}")


stu1 = Student("Alex", "001")
stu2 = Student("Bob", "002")
stu1.set_score("Chinese", 82)
stu1.set_score("Math", 78)
stu1.set_score("English", 99)
stu1.print_score()
