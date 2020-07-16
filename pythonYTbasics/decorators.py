def decoratorFunc(func):
    def wrapper_Func():
        print('*' * 20)
        func()
        print('-' * 20)

    return wrapper_Func

#can be used multiple times and diff ones too
@decoratorFunc
@decoratorFunc
def say_hlo():
    print('hello world!')


# hello = decoratorFunc(say_hlo)
# hello()
say_hlo()

from time import time


def timing(func):
    def wrapperFn(*args, **kwargs):
        start = time()
        #print(start)
        result = func(*args, **kwargs)
        end = time()
        #print(end)
        print('Elapsed time : {}'.format(end - start))
        return result

    return wrapperFn


@timing
def count(num):
    sum = 0
    for i in range(num + 1):
        sum += i

    return sum


print(count(17111144))