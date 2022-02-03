from src.Figure import Figure

class Triangle(Figure):

    name = 'Triangle'

    def __init__(self, side_a, side_b, side_c):
        if type(side_a and side_b and side_c) not in [int, float]:
            raise ValueError('NaN')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
