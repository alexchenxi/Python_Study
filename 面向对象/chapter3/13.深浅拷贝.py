import copy


def demo01():  # 不可变类型
    a = 10
    b = a
    print(f"id(a)--->{id(a)}")
    print(f"id(b)--->{id(b)}")
    print(f"id(10)--->{id(10)}")

    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [a, b]
    d = c
    print(f"id(a)--->{id(a)}")
    print(f"id(b)--->{id(b)}")
    print(f"id(c)--->{id(c)}")
    print(f"id(d)--->{id(d)}")  # 相同，D直接指向C的内存


def demo02():  # 浅拷贝可变类型
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]
    d = copy.copy(c)  # 浅拷贝可变类型，只会拷贝第一层
    print(f"id(c)--->{id(c)}")
    print(f"id(d)--->{id(d)}")  # 不同，

    print(id(c[2]))
    print(id(a))

    a[2] = 222
    print(f"c--->{c}")
    print(f"d--->{d}")


def demo03():  # 浅拷贝不可变类型
    a = (1, 2, 3)
    b = (11, 22, 33)
    c = (6, 7, a, b)
    d = copy.copy(
        c
    )  # 浅拷贝不可变类型 等同于普通赋值，直接指向 等同于=, copy.deepcopy()
    print(f"id(c)--->{id(c)}")
    print(f"id(d)--->{id(d)}")  # 相同，

    print(c)
    print(d)


def demo04():  # 深拷贝可变类型，会拷贝所有层
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]
    d = copy.deepcopy(c)
    print(f"id(c)--->{id(c)}")
    print(f"id(d)--->{id(d)}")  # 不同，

    print(id(d[2]))
    print(id(a))

    a[1] = 100
    b[1] = 800
    print(f"c--->{c}")
    print(f"d--->{d}")


def demo05():  # 深拷贝不可变类型
    a = (1, 2, 3)
    b = (11, 22, 33)
    c = (6, 7, a, b)
    d = copy.deepcopy(
        c
    )  # 深拷贝不可变类型 等同于普通赋值，直接指向 等同于=, copy.deepcopy()
    print(f"id(c)--->{id(c)}")
    print(f"id(d)--->{id(d)}")  # 相同，

    print(c)
    print(d)


# 只要存在可变类型，深拷贝就会开辟新内存空间


if __name__ == "__main__":
    demo05()
