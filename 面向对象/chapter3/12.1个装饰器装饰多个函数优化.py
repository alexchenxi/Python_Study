# 优化版
# 装饰器函数只接受一个入参
def my_deco(fn_name):  # fn_name被装饰的函数名对象
    def fn_inner(a, b):
        if fn_name.__name__ == "get_sum":
            print("计算加法中。。。")
        elif fn_name.__name__ == "get_minus":
            print("计算减法中。。。")
        return fn_name(a, b)

    return fn_inner


@my_deco
def get_sum(a, b):
    return a + b


@my_deco
def get_minus(a, b):
    return a - b


print(get_sum(1, 2))
print(get_minus(4, 2))
