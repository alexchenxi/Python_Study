"""
累加次数不够
原因：
    线程1还没有来得及执行完一个完整的动作，被线程2抢走了资源
解决：
    互斥锁
        是什么：对共享数据进行锁定，保证同一时刻只有一个线程去操作
        步骤：创建threading.Lock() 上锁mutex.acquire() 解锁mutex.release()
        死锁：一直等待对方释放锁的情景
                未在合适的时机解锁
                造成程序阻塞
"""

import threading

global_num = 0

# 创建线程锁
mutex = threading.Lock()


def fun1():
    # 枷锁
    mutex.acquire()
    for _ in range(1000000):
        global global_num
        global_num += 1
    print(f"函数fun1执行结果：{global_num}")
    # 解锁
    mutex.release()


def fun2():
    for _ in range(1000000):
        global global_num
        global_num += 1
    print(f"函数fun2执行结果：{global_num}")


if __name__ == "__main__":
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)

    t1.start()
    t2.start()

    # fun1()
    # fun2()
