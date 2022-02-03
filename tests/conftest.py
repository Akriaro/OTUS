import pytest
from src.Square import Square

@pytest.fixture()
def normal_square():
    square = Square(2)
    yield square
