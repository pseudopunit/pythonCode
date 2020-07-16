import math


class Circle:
    __radius = None

    def __init__(self, radius):
        self.setter(radius)

    def setter(self, radius):
        self.__radius = radius

    def getter(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, other):
        return Circle(self.__radius + other.__radius)

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __gt__(self, other):
        return self.__radius > other.__radius

    def __str__(self):
        return 'Circle area = ' + str(self.area())


c1 = Circle(10)
c2 = Circle(20)
c3 = c1 + c2
print(c3.getter())
print(c3.area())
print(c1 > c2)
print(c3 > c2)
print(str(c3))
print(dir(c1))

# Operator  Expression  FUNCTION
#  Math Operator Overloading
# Addition(+)  p1 + p2  p1.__add__(p2)
# Subtraction(-)  p1 - p2  p1.__sub__(p2)
# Multiplication(*)  p1 * p2  p1.__mul__(p2)
# Power(**)  p1 ** p2  p1.__pow__(p2)
# Division(/)  p1 / p2  p1.__truediv__(p2)
# Floor Division(//)  p1 // p2  p1.__floordiv__(p2)
# Remainder (modulo)(%)  p1 % p2  p1.__mod__(p2)
#  Bitwise Operator Overloading
# Bitwise left-shift(<<)  p1 << p2  p1.__lshift__(p2)
# Bitwise right-shift(>>)  p1 >> p2  p1.__rshift__(p2)
# Bitwise AND(&)  p1 & p2  p1.__and__(p2)
# Bitwise OR(|)  p1 | p2  p1.__or__(p2)
# Bitwise XOR(^)  p1 ^ p2  p1.__xor__(p2)(+)
# Bitwise NOT(~)  ~p1  p1.__invert__()
# Comparison operator __lt__{<}, __le__{<=}, __eq__{==}, __ne__{!=}, __gt__{>}, __ge__{>=}
