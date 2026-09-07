import multiprocessing
import time

my_list = []


def write_data():
    for i in range(1, 6):
        my_list.append(i)
        print(f"添加数据:{i}")

    print(f"write_data函数：{my_list}")


def read_data():
    time.sleep(3)
    print(f"read_data函数：{my_list}")


# main外资源，在每个进程都会拷贝一份（三个）
print("我是main外资源")
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)

    p1.start()
    p2.start()
    print("我是main内资源")
