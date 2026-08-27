# 高阶函数：fn是第三个参数，用来接收将来传入的函数
def sum_num(a, b, fn):
    return fn(a) + fn(b)


print(sum_num(3, -5, abs))
