import pytest
from app.calculator import add, subtract, divide, multiply

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(x, y, expected):
    assert add(x, y) == expected