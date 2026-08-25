str1 = "aa"
str2 = "bb"

list1 = [1, 2]
list2 = [10, 20]

t1 = (1, 2)
t2 = (10, 20)

dict1 = {"name": "Jack"}
dict2 = {"age": 22}


# +：合并 子列元
print(str1 + str2)
print(list1 + list2)
print(t1 + t2)
# print(dict1 + dict2)


# *：复制 子列元
print(str1 * 5)
print(list1 * 5)
print(t1 * 5)

# in/not in: 是否存在 全部

# len() 全部
print(len(dict1))

# del() 全部
del list2[0]
print(list2)

# min max() 全部
print(max(dict2))

# range(start,end,step) 全部
for i in range(1, 10, 2):
    print(i)

# enumerate 返回元组，第一个元素是下标，第二个元素是对象属数据 全部
for e in enumerate(t1, start=1):
    print(e)

# 类型转换
