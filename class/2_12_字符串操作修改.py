mystr = "Get fucking off you bastard peeking my screen!"

# replace
newstr = mystr.replace("y", "Y", 10)
print(newstr)
# 调用replace函数，源字符串的数据并没有被修改，修改的是函数返回值
# 说明 字符串是不可改变数据类型

# split('',分割次数)
sections = mystr.split(" ", 3)
print(sections)


# join 合并列表中的字符串
list1 = ["Hello", "World"]
str3 = "___".join(list1)
print(str3)
