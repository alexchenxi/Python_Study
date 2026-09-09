import threading
import time


def work():
    for i in range(19):
        time.sleep(0.2)
        print("working...")


if __name__ == "__main__":
    # 守护线程，写法1，daemon属性
    # t = threading.Thread(target=work, daemon=True)
    t = threading.Thread(target=work)
    # 守护线程写法2 或者 t.setDaemon(True) 已废弃
    # t.setDaemon(True)
    t.daemon = True
    t.start()

    # 设置主线程休眠时间1秒
    time.sleep(1)
    print("main over!")
