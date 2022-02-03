import pytest
from src.Square import Square

'''Simple test'''
def test_bad_type_value():
    with pytest.raises(ValueError):
        Square(0)

def test_ok_type_value():
        square = Square(2)
        assert isinstance (square, Square)

def test_perimeter():
    square = Square(2)
    assert square.perimeter == 8

def test_area():
    square = Square(2)
    assert square.area == 4

'''Tests with Fixrure'''

def test_perimeter_fixture(normal_square):
    assert normal_square.perimeter == 8

def test_area_fixture(normal_square):
    assert normal_square.area == 4

'''Test with parametrize'''

@pytest.mark.parametrize(
    ('side', 'expected'),
    (
            (2, 8),
            (5, 20),
    )
)
def test_perimeter_parametrize(side, expected):
    square = Square(side)
    assert square.perimeter == expected


