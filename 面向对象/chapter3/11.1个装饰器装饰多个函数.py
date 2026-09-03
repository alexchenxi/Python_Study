# 装饰器函数只接受一个入参,如果需要增加参数，可以用一个新的函数包裹装饰器函数并返回
def flag(flag):
    def my_deco(fn_name):
        def fn_inner(a, b):
            if flag == "+":
                print("计算加法中。。。")
            elif flag == "-":
                print("计算减法中。。。")
            return fn_name(a, b)

        return fn_inner

    return my_deco


@flag("+")
def get_sum(a, b):
    return a + b


@flag("-")
def get_minus(a, b):
    return a - b


print(get_sum(1, 2))
print(get_minus(4, 2))
