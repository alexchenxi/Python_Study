"""
在内部函数修改外部函数的变量值
"""


def fn_outer():
    a = 100

    def fn_inner():
        nonlocal a
        a = a + 1
        print(a)

    return fn_inner


fn_inner = fn_outer()
fn_inner()
fn_inner()
fn_inner()
