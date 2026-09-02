"""
完成学生管理系统 业务的操作，增删改查，保存
"""

import sys
import time
from pathlib import Path

from student import Student

base_dir = Path(__file__).parent


class StudentCMS:
    def __init__(self):
        self.students = []

    @staticmethod
    def show_menu():
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

    def query_student(self):
        query_name = input("请输入要查询的学生的姓名：")
        if len(self.students) > 0:
            for stu in self.students:
                if stu.name == query_name:
                    print(stu)
                    break
            else:
                print("没有找到这个学生的信息！")
            print()
        else:
            print("暂无信息!")

    def del_student(self):
        del_name = input("请输入要删除的学生的姓名：")
        print(del_name)
        for student in self.students:
            if student.name == del_name:
                self.students.remove(student)
                print(f"学生{del_name}已删除成功！")
                break
        else:
            print("没有找到该学生！")

    def modify_student(self):
        modify_name = input("请输入要修改信息的学生的姓名：")
        print(modify_name)
        for student in self.students:
            if student.name == modify_name:
                student.gender = input("请输入学生性别：男/女：")
                student.age = int(input("请输入学生年龄："))
                student.phone = input("请输入学生手机号码：")
                student.desc = input("请输入学生个人信息：")
                print(f"学生{modify_name}已更新成功！")
                break
        else:
            print("没有找到该学生！")

    def save_students(self):
        with open(base_dir / "stu_data.txt", "w", encoding="utf-8") as f:
            # 把[对象，对象]-》[字典，字典]
            stu_lists = [stu.__dict__ for stu in self.students]
            f.write(str(stu_lists))

    def load_students(self):
        try:
            with open(base_dir / "stu_data.txt", "r", encoding="utf-8") as f:
                stu_data = f.read()
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                    stu_list = []
                self.students = [Student(**stu_dict) for stu_dict in stu_list]
        except FileNotFoundError:
            with open(base_dir / "stu_data.txt", "w", encoding="utf-8") as f:
                f.write("[]")

    def start(self):
        # 加入延迟，等待用户操作

        print("欢迎使用学生管理系统！")
        self.load_students()
        while True:
            time.sleep(1)
            StudentCMS.show_menu()
            choice = input("请输入您的选择：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.del_student()
            elif choice == "3":
                self.modify_student()
            elif choice == "4":
                self.query_student()
            elif choice == "5":
                self.query_students()
            elif choice == "6":
                self.save_students()
                print("文件保存成功！")

            elif choice == "0":
                self.doube_check()
            else:
                print("输入错误，请重新输入")

    def doube_check(self):
        print("是否确认退出系统？")
        if input("请输入y/n：").lower() == "y":
            self.save_students()
            print("退出系统")
            sys.exit()
        else:
            print("继续操作")
            self.start()
