from pathlib import Path
from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(5_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result + 1)
title = f"Results of rolling a D{die_1.num_sides} and a D{die_2.num_sides} 1000 times"
label = {"x": "Result", "y": "Frequency of Result"}
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(
    x=poss_results, y=frequencies, title=title, labels=label, color=frequencies
)
fig.update_xaxes(dtick=1)
# fig.show()
path = Path(__file__).parent / "dice_visual.html"
fig.write_html(path)
