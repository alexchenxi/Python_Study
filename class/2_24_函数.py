# 1. 函数要先定义后调用
# 2. 不被调用则代码不会被执行
def add_num2(a, b):
    return a + b


print(add_num2(1, 2))

# 返回值

# 说明文档
help(min)
help(range)


def sum_num1(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    return a + b
