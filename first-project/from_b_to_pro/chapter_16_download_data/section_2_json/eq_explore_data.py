from pathlib import Path
import json

path = Path(__file__).parent / "eq_data" / "eq_data_1_day_m1.geojson"
content = path.read_text()
# 将这个文件的字符串表示转换为 Python 对象
all_eq_data = json.loads(content)
all_eq_dicts = all_eq_data["features"]


mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    title = eq_dict["properties"]["title"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(titles[:10])
print(lons[:10])
print(lats[:10])
