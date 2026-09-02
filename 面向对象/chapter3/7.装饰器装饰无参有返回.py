def tip(fn):

    def fn_inner():
        print("请耐心等待...")
        return fn()  # 这里需要加return,因为原函数有返回

    return fn_inner


@tip
def sum():
    a = 1
    b = 2
    sum = a + b
    return sum


print(sum())
