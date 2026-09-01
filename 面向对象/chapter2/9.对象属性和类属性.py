"""
属性介绍：
  概述：描述事物的外在特征
  分类：对象属性
        类属性 该类下所有对象共享

"""


class Student:
    teacher_name = "Mr.Big"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名：{self.name}; 年龄：{self.age}。"


s1 = Student("Jack", 32)
s2 = Student("Rose", 25)

s1.name = "XXXX"
s1.age = "???"
print(s1)
# 用对象名.的方式来修改类属性
s1.teacher_name = "unknown"
# 修改类变量的值，只有用类.变量的方法修改
Student.teacher_name = "Win"

print(f"{s1.teacher_name}")
print(f"{s2.teacher_name}")
print(f"{Student.teacher_name}")
