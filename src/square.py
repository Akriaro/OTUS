class Figure:
    pass

class Square(Figure):

    name = "Square"

    def __init__(self, side):
        if type(side) not in [int, float]:
            raise ValueError("Not int")
        self.side = side
        print(self)

    def area(self):
        return self.side * self.side

print(Square.name)

square = Square.area(side=10)
print(square)