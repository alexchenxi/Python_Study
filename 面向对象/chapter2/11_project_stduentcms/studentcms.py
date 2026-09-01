"""
完成学生管理系统 业务的操作，增删改查，保存
"""

import sys

from student import Student


class StudentCMS:
    def __init__(self):
        self.students = []

    def show_menu(self):
        print("*" * 34)
        print("学生管理系统")
        print("  1. 添加学生")
        print("  2. 删除学生")
        print("  3. 修改学生")
        print("  4. 查询学生")
        print("  5. 查看所有学生")
        print("  6. 保存学生")
        print("  0. 退出系统")
        print("*" * 34)

    def add_student(self):
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别：男/女：")
        age = int(input("请输入学生年龄："))
        phone = input("请输入学生手机号码：")
        desc = input("请输入学生个人信息：")
        s = Student(name, gender, age, phone, desc)
        self.students.append(s)
        print(f"添加学生{name}成功!")
        print(list(self.students))

    def query_students(self):
        if len(self.students) > 0:
            for stu in self.students:
                print(stu)
            print()
        else:
            print("暂无信息!")

    def start(self):
        while True:
            self.show_menu()
            choice = input("请输入您的选择：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                self.query_students()
            elif choice == "6":
                pass
            elif choice == "0":
                self.doube_check()
            else:
                print("输入错误，请重新输入")

    def doube_check(self):
        print("是否确认退出系统？")
        if input("请输入y/n：").lower() == "y":
            print("退出系统")
            sys.exit()
        else:
            print("继续操作")
            self.start()
