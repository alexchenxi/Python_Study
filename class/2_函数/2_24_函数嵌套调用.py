def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)


def avg_num(a, b, c):
    sum_result = sum_num(a, b, c)
    return "%05.2f" % (sum_result / 3)


print(avg_num(1, 2, 4))
