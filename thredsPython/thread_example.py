import _thread
import time


# using '_thread'
def print_epoch(nameofThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameofThread, '-------------', time.time())


try:
    _thread.start_new_thread(print_epoch, ('Thread 1', 2))
    _thread.start_new_thread(print_epoch, ('Thread 2', 4))
except Exception as e:
    print('Exception', e, 'occurred')

input()
