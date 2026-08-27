def print_sys(str):
    print("\033[33;40m" + str + "\033[0m")


def print_warn(str):
    print("\033[31;40m" + str + "\033[0m")


def print_info(str):
    print("\033[36;40m" + str + "\033[0m")


def info_print():
    print_sys("欢迎使用人员管理系统！")
    print("请输入对应序号，执行操作")
    print(
        "1：添加人员 2：删除人员 3：修改人员信息 4：查询人员信息 5：显示所有人员信息 6：退出系统"
    )


# 初始数据
info = [
    {"name": "Alex", "age": 33, "phone": "18514002233"},
    {"name": "Rose", "age": 22, "phone": "13514002233"},
    {"name": "Bob", "age": 18, "phone": "16514002233"},
]


def add_info():
    global info

    user_name = input("请输入用户名字：")
    for i in info:
        if i["name"] == user_name:
            print_warn("已存在该名称的用户!")
            return
    user_age = int(input("请输入用户年龄："))
    user_phone = input("请输入用户手机号：")

    info_dict = {"name": user_name, "age": user_age, "phone": user_phone}
    info.append(info_dict)
    print_info(f"用户{user_name}添加完毕!")
    print(info)


def del_info():
    del_name = input("请输入需要输出的人员的名字：")
    for i in info:
        if i["name"] == del_name:
            info.remove(i)
            print_info(f"人员{del_name}删除成功！")
            break
    else:
        print_warn("找不到该人员！")
    print(info)


def modify_info():
    modify_name = input("请输入需要修改信息的人员的名字：")
    for i in info:
        if i["name"] == modify_name:
            new_age = input("请输入人员的年龄：")
            new_phone = input("请输入人员的手机号码：")
            i["age"] = new_age
            i["phone"] = new_phone
            print_info(f"人员{modify_name}信息修改成功")
            break
    else:
        print_warn("找不到该人员！")
    print(info)


def query_info():
    query_name = input("请输入需要修改信息的人员的名字：")
    for i in info:
        if i["name"] == query_name:
            print_info("查询到的人员信息如下--------------")
            print_info(f"人员姓名：{query_name}")
            print_info(f"人员年龄：{i['age']}")
            print_info(f"人员手机号码：{i['phone']}")
            break
    else:
        print_warn("找不到该人员！")


# 系统功能需要循环执行，知道输入6
while True:
    info_print()
    go = int(input("请输入序号："))
    match go:
        case 1:
            add_info()
        case 2:
            del_info()
        case 3:
            modify_info()
        case 4:
            query_info()
        case 5:
            print("添加人员")
        case 6:
            exit_flag = input("\033[31;40m请确认是否退出，1：确定 其他：取消\033[0m")
            if exit_flag == "1":
                print_sys("欢迎再次使用，谢谢！")
                break
        case _:
            print_warn("输入的功能序号有误！")
