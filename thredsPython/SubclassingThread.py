import threading
import time


# using 'threading' module/class
def print_epoch(nameofThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameofThread, '-------------', time.time())


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self) -> None:
        print('Start Thread :', self.name)
        print_epoch(self.name, self.delay)
        print('End Thread :', self.name)


if __name__ == "__main__":
    t1 = MyThread('T-1', 1)
    t2 = MyThread('T-2', 2)

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())
    print('Active Count :', threading.activeCount())
    print('Current Thread', threading.currentThread())
    print('Enumerate', threading.enumerate())

    t1.join()
    t2.join()
