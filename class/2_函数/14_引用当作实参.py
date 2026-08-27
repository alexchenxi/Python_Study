def test(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))


# 不可变类型：字符串 整形 浮点型 元组
b = "string"
test(b)

# 可变类型：字典 集合 列表
c = [11, 22]
test(c)
