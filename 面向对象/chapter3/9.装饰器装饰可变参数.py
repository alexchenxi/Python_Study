def tip(fn):

    def fn_inner(*args, **kwargs):
        print("请耐心等待...")
        return fn(*args, **kwargs)  # 这里需要加return,因为原函数有返回

    return fn_inner


@tip
def get_sum(*args, **kwargs):

    # sum = 0
    # for i in args:
    #     sum += i
    # for k in kwargs.values():
    #     sum += k
    # return sum

    # 简单写法
    return sum(args) + sum(kwargs.values())


print(get_sum(3, 6, 12, a=4, b=23))
