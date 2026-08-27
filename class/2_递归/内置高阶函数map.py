list1 = [2, 3, 4, 5]


def func(x):
    return x**2


r = map(func, list1)
print(list(r))
