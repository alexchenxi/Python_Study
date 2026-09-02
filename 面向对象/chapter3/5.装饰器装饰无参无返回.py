def tip(fn):

    def fn_inner():
        print("请耐心等待...")
        fn()

    return fn_inner


@tip
def sum():
    a = 20
    b = 20
    sum = a + b
    print(f"Sum: {sum}")


sum()
