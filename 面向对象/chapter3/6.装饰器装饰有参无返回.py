def tip(fn):

    def fn_inner(a, b):
        print("请耐心等待...")
        fn(a, b)

    return fn_inner


@tip
def sum(a, b):
    sum = a + b
    print(f"Sum: {sum}")


sum(3, 6)
