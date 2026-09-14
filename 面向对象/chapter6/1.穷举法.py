import time


def method_1():
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print(f"a:{a};b:{b};c:{c}")


def method_2():
    for a in range(1001):
        for b in range(1001):
            c = 1000 - a - b
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(f"a:{a};b:{b};c:{c}")


start = time.perf_counter()
method_2()
end = time.perf_counter()
print(f"总耗时: {end - start:.4f} s")
