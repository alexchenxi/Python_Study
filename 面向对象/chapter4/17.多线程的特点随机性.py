import threading
import time


def print_info():
    time.sleep(0.2)
    current_thread = threading.current_thread()
    print(current_thread.name)


if __name__ == "__main__":
    for i in range(10):
        t = threading.Thread(target=print_info)
        t.start()
