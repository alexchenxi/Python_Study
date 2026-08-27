list1 = [2, 3, 4, 5]

import functools


def func(a, b):
    return a + b


r = functools.reduce(func, list1)
print(r)
