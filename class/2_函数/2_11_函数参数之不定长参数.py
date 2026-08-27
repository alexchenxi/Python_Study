def user_info(name, age, gender):
    print(f"您的姓名是{name}，年龄{age}岁，性别是{gender}。")


user_info("Alex", 33, "男")
# 关键字参数，键=值
user_info("Rose", gender="女", age=22)


# 缺省参数
def user_info2(name, age, gender="男"):
    print(f"您的姓名是{name}，年龄{age}岁，性别是{gender}。")


user_info2("Jack", 32)
