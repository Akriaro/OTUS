import pytest
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle

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


@pytest.mark.parametrize(
    ('side', 'expected'),
    (
            (0, ValueError),
            (-1, ValueError),
            ('a', ValueError),
            (None, ValueError),
    )
)
def test_bad_values_parametrize(side, expected):
    with pytest.raises(expected):
        Square(side)


'''Add Figures'''

@pytest.mark.parametrize(
    ('value', 'expected'),
    (
        (Circle(10), 414.1592653589793),
        (Rectangle(10, 15), 250),
        (Square(10), 200),
        (Triangle(2, 2, 2), 101.73205080756888),
    )
)
def test_check_add_area(value, expected):
    figure = Square(10)
    assert figure.add_area(value) == expected


def test_check_add_area_error():
    circle = Square(10, )
    with pytest.raises(ValueError):
        circle.add_area([1, 2, 3])

def test_circle_add_area():
    circle = Circle(5)
    square = Square(10)
    assert circle.add_area(square) == 178.53981633974485
