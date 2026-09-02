from project_stduentcms.student import Student

"""
__dict__属性介绍：
    python内置属性，可以把对象转为字典形式
"""

s1 = Student("Alex", "男", 38, 18514444433, "凌乱了")
print(s1)
sone = s1.__dict__
print(sone)

s2 = Student("Rose", "女", 28, 18514442123, "JumP")
s3 = Student("Dywane", "男", 44, 18514324433, "This is my house")
students = [s1, s2, s3]

# 列表推导式
list_students = [stu.__dict__ for stu in students]
print(list_students)

my_dict = {
    "name": "jack",
    "gender": "男",
    "age": 12,
    "phone": 183212312,
    "desc": "titanic",
}

# name, gender, age, phone, desc = my_dict.values()
# s5 = Student(name, gender, age, phone, desc)
# print(s5)

# 解包运算符，*：list tuple str set range **:dict
s5 = Student(**my_dict)
print(s5)
