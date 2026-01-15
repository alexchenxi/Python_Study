from pathlib import Path
import plotly.express as px
import json
import pandas as pd

path = Path(__file__).parent / "eq_data" / "eq_data_30_day_m1.geojson"
try:
    content = path.read_text()
except:
    content = path.read_text(encoding="utf-8")

# 将这个文件的字符串表示转换为 Python 对象
all_eq_data = json.loads(content)
all_eq_dicts = all_eq_data["features"]
title = all_eq_data["metadata"]["title"]


mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    if eq_dict["properties"]["mag"] > 0:
        mags.append(eq_dict["properties"]["mag"])
    titles.append(eq_dict["properties"]["title"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags, titles),
    columns=["经度", "纬度", "标题", "震级", "位置"],
)

fig = px.scatter(
    data,
    x="经度",
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title=title,
    size="震级",
    size_max=10,
    color="震级",
    hover_name="位置",
)

# fig.write_html(Path(__file__).parent / "global_earthquake.html")
fig.show()
