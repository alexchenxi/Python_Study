list1 = [2, 3, 4, 5]


def func(a):
    return a % 2 == 0


fn = lambda x: x % 2 == 0

# r = filter(func, list1)
r = filter(fn, list1)
print(list(r))
