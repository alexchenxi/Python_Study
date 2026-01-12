import matplotlib.pyplot as plt
import os

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.YlOrBr)

# 设置图表标题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

# 这段代码设置了matplotlib图表的坐标轴范围，将x轴设为0-1100，y轴设为0-1100000
ax.axis([0, 1100, 0, 1_100_000])
# 将x轴和y轴的刻度标签格式设为普通格式，而不是科学计数法
ax.ticklabel_format(style="plain")

# 获取当前脚本所在的目录
current_dir = os.path.dirname(__file__)

# 构建完整的文件路径，将图片保存到脚本所在的目录
file_path = os.path.join(current_dir, "squares_plot.png")

# plt.show()
plt.savefig(file_path, bbox_inches="tight")
