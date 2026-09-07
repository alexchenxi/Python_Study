"""
演示单任务，前面不执行完，后面不会执行
"""


def fun_a():
    for i in range(10):
        print("Hello")


def fun_b():
    for i in range(10):
        print("World")


fun_a()
fun_b()
