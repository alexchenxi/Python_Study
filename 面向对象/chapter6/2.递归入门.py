count = 0


def show():
    global count
    count += 1
    if count > 50:
        return
    print(f"我是show函数，被执行了{count}次。。。")
    show()


# 求阶乘
def factorial(n):
    # 内部递归计算，只返回数字
    def calc(k):
        # 出口
        if k == 1:
            return 1
        # 规律
        return k * calc(k - 1)

    return f"{n}的阶乘是{calc(n)}"


if __name__ == "__main__":
    # show()
    print(factorial(5))
