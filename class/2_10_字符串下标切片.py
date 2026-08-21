str = "abcdefg"

print(str[1])
print(str[1:5:1])
# string[起点：终点：步长] 左闭右开
print(str[:5:1])
# 步长为负数，倒叙
print(str[::-2])
# 序列-1表示最后一个数据
print(str[-4:-1])  # def
# 注意 选不出来，前两个表明是顺序，最后又要倒叙，矛盾
print(str[-4:-1:-1])  # 空格
