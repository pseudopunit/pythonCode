# demontrating various OOPS features
# encapsulation using class and privating variables and member functions using '__'
# inheritance in classes (single/multiple)
# getter and setter functions
# super() function returns a proxy object allowing us to refer to super class
# __mro__ is method resolution function used to resolve order of parent classes called in case of multiple inheritance
# example of commposition(part-of) and aggregation(has-a) is saved as SS
# Classes can be made abstract by inheriting from ABC(abstract-base-class) and decorating function by '@abstractmethod'
# ABC is imported from - "from abc import ABC, abstractmethod", eg SS is also saved for the same
from rectangle import Rectangle
from triangle import Triangle


rec = Rectangle()
rec.set_values(4, 5)
rec.set_colour('red')
print(rec.area())
print(rec.get_colour())
print(Rectangle.__mro__)

tri = Triangle()
tri.set_values(5, 6)
tri.set_colour('red')
print(tri.area())
print(tri.get_colour())
print(Triangle.__mro__)