# 可变和不可变
a = 1
b = a
print(id(a) == id(b))

a = 20
print(id(b) == id(a))

# 可变类型 列表
aa = [10, 20]
bb = aa
print(id(aa) == id(bb))

aa.append(30)
print(id(aa) == id(bb))
