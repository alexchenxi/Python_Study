"""
线程的使用步骤：
  1. 导包
  2. 创建线程对象
  3. 启动线程

线程 进程：
  1. 进程是CPU分配资源的基本单位，线程是CPU调度资源的最小单位
  2. 线程依附于进程，至少一个线程
  3. 进程相互隔离，同一个进程间线程数据可以共享
"""

import threading


def coding():
    for i in range(1, 10):
        print(f"正在敲第{i}编代码...")


def music():
    for i in range(1, 19):
        print(f"正在听第{i}遍音乐))))")


if __name__ == "__main__":
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)

    t1.start()
    t2.start()
