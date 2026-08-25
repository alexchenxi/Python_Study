dict1 = {"name": "Tom", "age": 18, "gender": "Male"}
for key in dict1:
    print(key)

for value in dict1.values():
    print(value)

# xx.items()：返回可迭代对象，内部是元组，元组有两个数据，key和value
for k, v in dict1.items():
    print(f"{k}的值是：{v}")
