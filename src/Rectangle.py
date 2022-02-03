from src.Figure import Figure

class Rectangle(Figure):

    name = 'Rectangle'

    def __init__(self, side_a, side_b):
        if type(side_a and side_b) not in [int, float]:
            raise ValueError('NaN')
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2
