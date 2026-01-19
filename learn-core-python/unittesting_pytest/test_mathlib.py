"""
==================== PYTEST TERMINAL COMMANDS ====================

1️⃣ Run all tests in this file
------------------------------------------------
pytest test_mathlib.py


2️⃣ Run a single test by name
------------------------------------------------
pytest test_mathlib.py -k test_calc_add

(run tests whose name contains 'test_calc_add')


3️⃣ Run multiple tests by partial name
------------------------------------------------
pytest -k "add or subtract"

(runs tests containing 'add' OR 'subtract')


4️⃣ Skip a particular test (from command line)
------------------------------------------------
pytest -k "not test_calc_divide"

(runs all tests EXCEPT test_calc_divide)


5️⃣ Run only Windows-specific tests (custom marker)
------------------------------------------------
pytest -m windows


6️⃣ Run only Mac-specific tests (custom marker)
------------------------------------------------
pytest -m mac


7️⃣ Run everything EXCEPT Windows tests
------------------------------------------------
pytest -m "not windows"


8️⃣ Run Windows AND Mac tests together
------------------------------------------------
pytest -m "windows or mac"


9️⃣ Run tests with verbose output
------------------------------------------------
pytest -v


🔟 Show print() output in terminal
------------------------------------------------
pytest -s


1️⃣1️⃣ Stop execution on first failure
------------------------------------------------
pytest -x


1️⃣2️⃣ Run tests in parallel (requires pytest-xdist)
------------------------------------------------
pip install pytest-xdist
pytest -n auto


1️⃣3️⃣ List all available markers
------------------------------------------------
pytest --markers


1️⃣4️⃣ Run tests and show slowest 5 tests
------------------------------------------------
pytest --durations=5


1️⃣5️⃣ Dry run (collect tests only, do not run)
------------------------------------------------
pytest --collect-only

==================================================
"""

import mathlib
import pytest


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


@pytest.mark.windows
def test_windows_1():
    assert True


@pytest.mark.windows
def test_windows_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True


@pytest.mark.mac
def test_mac_2():
    assert True
