name_list = ["Tom", "Rose", "Lily"]


# del 直接删除变量
# del name_list
# print(name_list)

del name_list[0]
print(name_list)

# pop(下标)，不提供参数则删最后，函数回调为删除的数据
name_list.pop()
print(name_list)

# remove 无回调
list2 = [1, 2, 3, 4, 5]
list2.remove(2)
print(list2)

# clear
list2.clear()
print(list2)
