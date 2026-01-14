from datetime import datetime
from pathlib import Path
import csv

from matplotlib import pyplot as plt

# 使用Path对象的joinpath方法构建正确的路径
path = Path(__file__).parent / "weather_data" / "sitka_weather_2021_simple.csv"
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    high = int(row[4])
    low = int(row[5])
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    highs.append(high)
    dates.append(current_date)
    lows.append(low)

# 根据最高和最低温度绘制图表
plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)


plt.show()
