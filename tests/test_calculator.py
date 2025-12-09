import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import add, subtract, multiply, divide


def test_add_integers():
    assert add(1, 2) == 3


def test_add_floats():
    # Используем approx для сравнения float
    assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
