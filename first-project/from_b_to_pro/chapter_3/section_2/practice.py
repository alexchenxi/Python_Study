# 1
guests = ["Jack", "Allen", "David"]
for guest in guests:
    print(f"{guest} please come to my party")
print("####################")
# 2
print(f"{guests[2]} can not come")
guests[2] = "Chris"
for guest in guests:
    print(f"{guest} please come to my party")
print("####################")
# 3
guests.insert(0, "Sofie")
guests.insert(2, "John")
guests.append("Wayne")
for guest in guests:
    print(f"{guest} please come to my party")
print("####################")
# 4
print("I'm sorry to inform that only two guests can be invited")
print(len(guests))
while len(guests) > 2:
    print(f"{guests.pop()} you're kicked out!")
print("Okay we finined")
for guest in guests:
    print(f"{guest} you're the lucky guy to stay")
while len(guests) > 0:
    del guests[0]
print(f"Now {len(guests)} guest in my list")
print("####################")
print(dir(__builtins__))  # 内置函数
print("####################")
print(dir(list))  # 列表的内置方法

