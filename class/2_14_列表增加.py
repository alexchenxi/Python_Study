name_list = ["Tom", "Rose", "Lily"]
# name = input("请输入用户名：")
# if name in name_list:
#     print(f"您输入的名字是{name}，系统已存在")
# else:
#     print(f"可以注册")

# 列表可改变的

# append()
name_list.append("David")

# extend([序列])
name_list.extend(["Jack"])
print(name_list)

# insert(位置下标，数据)
name_list.insert(1, "Harris")
print(name_list)
