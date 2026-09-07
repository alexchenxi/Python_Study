"""
实现方式：
  1.导包
  2.创建进程对象，关联目标函数
  3.启动进程
"""

import multiprocessing
import time


def code():
    for i in range(1, 100):
        time.sleep(0.1)  # 模拟耗时操作
        print(f"Coding for {i} times...")


def music():
    for i in range(1, 100):
        time.sleep(0.1)
        print(f"Listen to music for {i} times...")


# 通过main进程（主进程）来参加紫禁城
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=code)
    p2 = multiprocessing.Process(target=music)

    p1.start()
    p2.start()
