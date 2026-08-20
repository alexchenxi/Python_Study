# "%s" %(变量)

name = "alex"
age = 22
s = f"hello {name}, your age is {age} years old."
print(s)

greet = "How are you %s, your age is %s" % (name, age)

# %s内容转变为字符串，放入占位置
# %d内容转变为整数，放入占位置
# %f内容转变为浮点型，放入占位置

print(greet)

good = "orange"
year = 2026
price = 6.9
msg = "In year %d, %s unit price is $%f per kg" % (year, good, price)
print(msg)


# 浮点数精度控制
# "%m.nf" 宽度 小数点精度
width = 123
number = "%5d" % width
print(number)
acc = 11.345
print("%7.2f" % acc)
print("%.1f" % acc)

# 字符串格式化 快速写法 不做精度控制和类型
# f"{variable}"
movie = "alien"
print(f"My favourite movie is {movie}.")

# 表达式expression(有明确结果的代码语句)格式化
print("1 * 4 equals to %d" % (1 * 4))
print(f"1 * 4 equals to {1 * 4}")
print("String's type in Python is : %s" % (type("string")))
