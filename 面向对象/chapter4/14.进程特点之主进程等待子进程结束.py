"""
默认情况下，主进程会等子进程执行结束再结束
如果要设置主进程结束，子进程同步结束:
  1：设置子进程为 守护进程
  2：强制关闭子进程，可能会导致子进程变成僵尸进程，交由python解释器自动收回
"""

import multiprocessing
import time


def work():
    for i in range(10):
        print("Working...")
        time.sleep(0.2)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work, daemon=True)
    # p1.daemon = True  # 设置p1为守护进程
    # print(f"p1进程的名字：{p1.name}")

    p1.start()

    time.sleep(1)

    # 2.强制关闭子进程
    # p1.terminate()
    print("main结束了。。。")
