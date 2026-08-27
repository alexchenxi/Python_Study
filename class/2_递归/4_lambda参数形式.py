fn = lambda a, b: a + b
print(fn(1, 3))

fn2 = lambda a, b, c=100: a + b + c
print(fn2(1, 2))

fn3 = lambda *args: args
print(fn3(3, 4, 5))

fn4 = lambda **kwargs: kwargs
print(fn4(name="alex", age=18))
