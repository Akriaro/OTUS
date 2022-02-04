from src.Figure import Figure
from math import pi

class Circle(Figure):

    name = 'Circle'

    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise ValueError('NaN')
        self.radius = radius

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.radius
