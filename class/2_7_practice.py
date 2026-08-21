# 九九乘法表

# i代表乘数 j代表被乘数
i = 1
while i < 10:
    # 靠右对齐
    print(" " * (9 - i) * 12, end="")
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j:2d}", end="  ")
        j += 1
    print()
    i += 1
