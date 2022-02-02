from src.Figure import Figure

class Square(Figure):

    name = "Square"

    def __init__(self, side):
        if type(side) not in [int, float]:
            raise ValueError("NaN")
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


square = Square('a')
print(square.side)
print(square.name)
print(square.area())
print(square.perimeter())