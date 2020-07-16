# checking exception class
a = input('Enter no 1 : ')
b = input('Enter no 2 : ')
try:
    a = float(a)
    b = float(b)
    result = a/b
except ValueError as e:
    print('ValueError :', type(e))
except TypeError as e:
    print('TypeError :', type(e))
except ZeroDivisionError as e:
    print('ZeroDivisionError', type(e))
else:
    print('Result :', result)
    print('__else__')
finally:
    print('__finally__')


# building custom-exception class
class customException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class testingException:
    def __init__(self, value):
        self.__value = value

    def testFunc(self):
        if self.__value is False:
            raise customException('value is ' + str(self.__value))
        elif self.__value is None:
            raise customException('value is ' + str(self.__value))
        else:
            print('value is', self.__value)


# c = testingException(False)
# c.testFunc()
# d = testingException(None)
# d.testFunc()
e = testingException(True)
e.testFunc()

