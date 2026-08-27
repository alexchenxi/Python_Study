# 累加
# 返回的内容必须包括自身函数，同样有一个结束条件
def sum_numbers(num):
    if num == 1:
        return 1
    else:
        return num + sum_numbers(num - 1)


print(sum_numbers(5))
