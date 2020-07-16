class ListIterator:

    def __init__(self, list):
        self.__list = list
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__list):
            raise StopIteration
        return self.__list[self.__index]


a = [2, 5, 4, 7, 3]
mylist = ListIterator(a)
it = iter(mylist)
# for i in it:
#     print(i)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))