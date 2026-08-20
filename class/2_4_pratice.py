# 猜拳
import random

choices = {0: "剪刀", 1: "石头", 2: "布"}

user = int(input("请出拳：0-剪刀，1-石头，2-布，3-退出"))
while user != 3:
    computer = random.randint(0, 2)
    print(f"电脑出了{choices[computer]}，你出的是{choices[user]}")
    diff = (user - computer) % 3
    if diff == 0:
        print("打平，再来")
    elif diff == 1:
        print("恭喜你赢了！")
    else:
        print("你输了！")
    user = int(input("请出拳：0-剪刀，1-石头，2-布，3-退出"))
