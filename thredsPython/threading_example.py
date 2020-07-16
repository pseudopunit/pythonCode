import threading
import time


# using 'threading' module/class
def print_epoch(nameofThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameofThread, '-------------', time.time())


def square(num):
    print('Square = {}'.format(num ** 2))


def cube(num):
    print('Cube = {}'.format(num ** 3))


if __name__ == "__main__":
    # t1 = threading.Thread(target=print_epoch, args=('Thread 1', 2))
    # t2 = threading.Thread(target=print_epoch, args=('Thread 2', 4))
    t1 = threading.Thread(target=square, args=(2,))
    t2 = threading.Thread(target=cube, args=(2,))


    # start the threads
    t1.start()
    t2.start()

    # wait for the thread to get exicuted
    t1.join()
    print('-------------T1 got executed-------------')
    t2.join()
    print('-------------T2 got executed-------------')
