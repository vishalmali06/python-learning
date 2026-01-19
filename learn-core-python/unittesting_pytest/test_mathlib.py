import mathlib


def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == 9


def test_calc_multiply():
    total = mathlib.calc_multiply(10, 5)
    assert total == 50


def test_calc_add():
    total = mathlib.calc_add(10, 5)
    assert total == 15


def test_calc_subtract():
    total = mathlib.calc_subtract(10, 5)
    assert total == 5


def test_calc_divide():
    total = mathlib.calc_divide(10, 5)
    assert total == 2
