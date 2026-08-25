dict1 = {"name": "Tom", "age": 12, "gender": "Male"}

dict2 = {}
dict2["name"] = "Rose"
print(dict2)

# 删除
del dict1["name"]
print(dict1)

dict2.clear()
print(dict2)

# 改
dict1["age"] = 22
print(dict1["age"])
