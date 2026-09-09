import threading
import time

my_list = []


def save():
    for i in range(1, 6):
        time.sleep(0.2)
        my_list.append(i)
        print(f"写入数据：{i}")
    print(f"save函数：{my_list}")


def load():
    time.sleep(0.5)
    print(f"load函数：{my_list}")


if __name__ == "__main__":
    t1 = threading.Thread(target=save)
    t2 = threading.Thread(target=load)
    t1.start()
    t2.start()
