import pytest
from app.calculator import add, subtract, divide, multiply, kuno

@pytest.mark.parametrize("x, y, expected", [
    (2, 2, 4),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
    (-1, -1, 0),
])
def test_subtract(x, y, expected):
    assert subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-6, 2, -3),
    (5, 2, 2.5),
])
def test_divide(x, y, expected):
    assert divide(x, y) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
    (10, 10, 100),
])
def test_multiply(x, y, expected):
    assert multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (5, 0, 1),
    (10, 1, 10),
])
def test_kuno(x, y, expected):
    assert kuno(x, y) == expected