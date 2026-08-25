s1 = {100, 10, 500}
s1.add(1000)
s1.add(10)
print(s1)

# update 数据是序列
s1.update([10, 20, 100])
print(s1)

# 删除
# remove(),不存在会报错
s1.remove(500)
# print(s1)
# s1.remove(11)

# discard(),不存在不会报错
s1.discard(123321)
print(s1)

# pop()，随机删除并返回删除的数据，set是无序的
del_num = s1.pop()
print(del_num)
print(s1)

# 查找
print(10 in s1)
print(999 not in s1)
