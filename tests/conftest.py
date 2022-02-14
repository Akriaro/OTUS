import pytest
from src.Square import Square
from src.Rectangle import Rectangle

@pytest.fixture()
def normal_square():
    square = Square(2)
    yield square

@pytest.fixture()
def normal_rectangle():
    reqtangle = Rectangle(2,4)
    yield reqtangle
