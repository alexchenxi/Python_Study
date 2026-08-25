t1 = ("a", "b", "c")
print(t1[1])

# index()
print(t1.index("c"))

# count()
print(t1.count("a"))

# len()
print(len(t1))

# 元组里的第一层元素不可修改
t2 = ("a", "b", ["c", "d"])
t2[2][1] = "Jack"
print(t2)

# t2[0] = "df"
# print(t2)
