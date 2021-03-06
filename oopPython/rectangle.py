from polygon import Polygon
from shape import Shape


class Rectangle(Polygon, Shape):

    def area(self):
        return self.get_width() * self.get_height()

    def set_values(self, width, height):
        self.set_width(width)
        self.set_height(height)

