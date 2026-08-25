# for循环实现
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 推导式
list1 = [i for i in range(10)]
print(list1)

# 带if的推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
