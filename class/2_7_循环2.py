# 子循环条件不满足，退出子循环，继续夫循环
i = 1

while i <= 3:
    j = 1
    while j <= 3:
        print("Current step is %d-%d." % (i, j))
        j += 1
    i += 1
    print()
