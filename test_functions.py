from functions import division

def test_division_positive_numbers():
    assert division(20, 10) == 2
    assert division(6, 2) == 3
    assert division(11, 2) == 5.5
    assert division(17, 3) == 5.67


def test_division_negative_numbers():
    assert division(-6, -11) == 0.55
    assert division(-34, 8) == -4.25
    assert division(45, -10) == -4.5


def test_division_zero():
    assert division(0, 8) == 0
    assert division(10, 0) == "Division by zero is not suppotred! Please enter another denominator."


def test_division_float_numbers():
    assert division(11.5, 5.5) == 2.09
    assert division(34.8, 7) == 4.97
    assert division(92, 53.75) == 1.71