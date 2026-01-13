import matplotlib.pyplot as plt


def prac_15_1():
    input_values = range(1, 5001)
    cube = [x**3 for x in input_values]
    plt.style.use("seaborn-v0_8")

    _, ax = plt.subplots()
    ax.scatter(input_values, cube, linewidth=3)
    ax.axis([0, 5100, 0, 5100**3])
    ax.ticklabel_format(style="plain")
    # 添加标题和标签
    ax.set_title("Cube Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cube of Value", fontsize=14)

    plt.show()


def prac_15_2():
    try:
        input_values = range(1, 5001)
        cube = [x**3 for x in input_values]
        plt.style.use("seaborn-v0_8")

        fig, ax = plt.subplots()
        ax.scatter(input_values, cube, s=10, c=cube, cmap=plt.cm.YlOrBr)

        # 动态计算轴范围，而不是硬编码
        max_input = max(input_values)
        max_cube = max(cube)
        ax.axis([0, max_input * 1.02, 0, max_cube * 1.02])

        ax.ticklabel_format(style="plain")
        # 添加标题和标签
        ax.set_title("Cube Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Cube of Value", fontsize=14)

        plt.show()
    except Exception as e:
        print(f"绘图过程中发生错误: {e}")


prac_15_2()
