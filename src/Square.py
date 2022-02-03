from src.Figure import Figure

class Square(Figure):

    name = "Square"

    def __init__(self, side):
        if type(side) not in [int, float] or side <= 0:
            raise ValueError("NaN or <= 0")
        self.side = side

    @property
    def area(self):
        return self.side * self.side

    @property
    def perimeter(self):
        return self.side * 4


# square = Square(0)
# print(square.side)
# print(square.name)
# print(square.area)
# print(square.perimeter)