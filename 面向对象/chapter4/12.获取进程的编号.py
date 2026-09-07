import os
import multiprocessing


def code(person, num):
    for i in range(1, num + 1):
        print(f"{person} is coding for {i} times...")

    print(f"p1进程的Pid是{os.getpid()}，父进程ID为{os.getppid()}")


def music(person, count):
    for i in range(1, count + 1):
        print(f"{person} is coding for {i} times...")
    print(
        f"p2进程的Pid是{multiprocessing.current_process().pid}，父进程ID为{os.getppid()}"
    )


if __name__ == "__main__":
    # args 元组方式（顺序传参）
    # kwargs 字典方式（关键字传参）
    p1 = multiprocessing.Process(target=code, args=("小明", 100))
    p2 = multiprocessing.Process(target=music, kwargs={"person": "Jack", "count": 199})

    p1.start()
    p2.start()

    print(
        f"main进程的Pid是{multiprocessing.current_process().pid}，父进程ID为{os.getppid()}"
    )
