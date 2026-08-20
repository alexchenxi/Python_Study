import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

name = "西梅"
unit_price = 19.99
good_id = 123321
growth_factor = 1.2
days = 7

print(f"产品：{name}，商品编号：{good_id}，当前均价：{unit_price}元/斤。")
print(
    "每日增长系数：%.2f，经过%d天的增长，均价达到了%.2f元/斤"
    % (growth_factor, days, (unit_price * growth_factor**days))
)
