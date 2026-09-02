def tip(fn):

    def fn_inner(a, b):
        print("请耐心等待...")
        return fn(a, b)  # 这里需要加return,因为原函数有返回

    return fn_inner


@tip
def sum(a, b):
    sum = a + b
    return sum


print(sum(3, 6))
