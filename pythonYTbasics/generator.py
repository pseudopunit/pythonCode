def gen():
    for i in range(5):
        print('----------------------', i)
        yield i


a = gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def list_iterator(list):
    for i in list:
        yield i


b = [2, 5, 4, 7, 3]
mylist = list_iterator(b)

print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))