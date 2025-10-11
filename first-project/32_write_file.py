with open('./poem.txt', 'w', encoding='utf-8') as f:
    f.write("大江东去，浪淘尽，千古风流人物。\n")
    f.write("故垒西边，人道是，三国周郎赤壁。\n")
    f.write("乱石穿空，惊涛拍岸，卷起千堆雪。\n")
    f.write("江山如画，一时多少豪杰。\n")
with open('./poem.txt', 'a', encoding='utf-8') as f:
    f.write("遥想公瑾当年，小乔初嫁了，雄姿英发\n")
print("Poem finished")
