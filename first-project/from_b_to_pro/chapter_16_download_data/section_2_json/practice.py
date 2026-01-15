import csv
from pathlib import Path
import json
import plotly.express as px
import pandas as pd


def world_eq_map():
    path = Path(__file__).parent / "eq_data" / "all_month.geojson"

    try:
        content = path.read_text()
    except:
        content = path.read_text(encoding="utf-8")

    all_eq_data = json.loads(content)
    all_eq_dicts = all_eq_data["features"]
    title = all_eq_data["metadata"]["title"]

    mags, titles, lons, lats = [], [], [], []
    for eq_dict in all_eq_dicts:
        if eq_dict["properties"]["mag"] is not None:
            mag = eq_dict["properties"]["mag"]
            mags.append(max(mag, 0))
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

    fig.show()


def fire_map():
    path = Path(__file__).parent / "fire_data" / "world_fires_1_day.csv"
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    next(reader)

    lons, lats, bs = [], [], []

    for row in reader:
        lons.append(float(row[1]))
        lats.append(float(row[0]))
        bs.append(float(row[2]))

    ax = px.scatter_geo(
        lat=lats,
        lon=lons,
        size=bs,
        size_max=10,
        color=bs,
        color_continuous_scale="YlOrRd",
        labels={"color": "Brightness"},
        projection="natural earth",
        title="全球火灾地图",
    )
    ax.show()


fire_map()
