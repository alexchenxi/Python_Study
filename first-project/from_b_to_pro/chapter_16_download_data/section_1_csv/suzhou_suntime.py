import csv
from datetime import datetime
from pathlib import Path

from matplotlib import pyplot as plt

path = Path(__file__).parent / "weather_data" / "suzhou_suntime.csv"
lines = path.read_text().splitlines()

reader = csv.reader(lines)
next(reader)
dates, sunrises, sunsets = [], [], []
for row in reader:
    dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
    sunrises.append(datetime.strptime(row[1], "%H:%M:%S"))
    sunsets.append(datetime.strptime(row[2], "%H:%M:%S"))

plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(dates, sunrises, c="blue")
ax.plot(dates, sunsets, c="red")
ax.fill_between(dates, sunrises, sunsets, facecolor="blue", alpha=0.1)

ax.set_title("Daily Sunrise and Sunset Times, Suzhou", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Time", fontsize=16)


# 添加图例
ax.legend(["Sunrise", "Sunset"], fontsize=16)

fig.autofmt_xdate()

plt.show()
