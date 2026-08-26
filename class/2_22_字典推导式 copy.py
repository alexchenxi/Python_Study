list1 = ["name", "age", "gender", "id"]
list2 = ["Tom", 22, "Male"]
# 合并成一个字典
dict1 = {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}
print(dict1)

counts = {"IBM": 400, "Lenovo": 233, "asus": 123}
count1 = {k: v for k, v in counts.items() if v > 200}
print(count1)
