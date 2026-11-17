from functions import (add, 
                       sub, 
                       multiply, 
                       division, 
                       power, 
                       mod, 
                       maximum, 
                       minimum, 
                       average)


# add()

def test_add_positive_numbers():
    assert add(10, 5) == 15
    assert add(20, 30) == 50


def test_add_negative_numbers():
    assert add(-10, -5) == -15
    assert add(-20, -30) == -50


def test_add_zero():
    assert add(10, 0) == 10
    assert add(0, 0) == 0


def test_add_float_numbers():
    assert add(1.5, 2.5) == 4
    assert add(3.2, 1.8) == 5


# sub()

def test_sub_positive_numbers():
    assert sub(10, 5) == 5
    assert sub(20, 30) == -10


def test_sub_negative_numbers():
    assert sub(-10, -5) == -5
    assert sub(-20, -30) == 10


def test_sub_zero():
    assert sub(10, 0) == 10
    assert sub(0, 0) == 0


def test_sub_float_numbers():
    assert sub(5.5, 2.5) == 3
    assert round(sub(10.8, 3.3), 2) == 7.5


# multiply()

def test_multiply_positive_numbers():
    assert multiply(10, 5) == 50
    assert multiply(4, 3) == 12


def test_multiply_negative_numbers():
    assert multiply(-10, -5) == 50
    assert multiply(-10, 5) == -50


def test_multiply_zero():
    assert multiply(10, 0) == 0
    assert multiply(0, 0) == 0


def test_multiply_float_numbers():
    assert multiply(2.5, 2) == 5
    assert multiply(1.5, 3) == 4.5 


# division()

def test_division_positive_numbers():
    assert division(20, 10) == 2
    assert division(17, 3) == 5.67


def test_division_negative_numbers():
    assert division(-6, -11) == 0.55
    assert division(45, -10) == -4.5


def test_division_zero():
    assert division(0, 8) == 0
    assert division(10, 0) == "Division by zero is not suppotred! Please enter another denominator."


def test_division_float_numbers():
    assert division(11.5, 5.5) == 2.09
    assert division(92, 53.75) == 1.71 


# power()

def test_power_positive_numbers():
    assert power(2, 3) == 8
    assert power(5, 2) == 25


def test_power_negative_numbers():
    assert power(-2, 3) == -8
    assert power(-2, 2) == 4


def test_power_zero():
    assert power(5, 0) == 1
    assert power(10, 0) == 1


def test_power_float_numbers():
    assert power(2, -2) == 0.25
    assert power(4, -1) == 0.25


# mod()

def test_mod_positive_numbers():
    assert mod(10, 3) == 1
    assert mod(20, 6) == 2

def test_mod_negative_numbers():
    assert mod(-10, 3) == 2
    assert mod(10, -3) == -2

def test_mod_zero():
    assert mod(0, 3) == 0
    assert mod(0, 5) == 0

def test_mod_float_numbers():
    assert mod(10.5, 3) == 1.5
    assert mod(7.5, 2) == 1.5

# maximum()

def test_maximum_positive_numbers():
    assert maximum([10, 20, 5, 30]) == 30
    assert maximum([1, 2, 3, 4]) == 4


def test_maximum_negative_numbers():
    assert maximum([-10, -20, -5, -30]) == -5
    assert maximum([-1, -2, -3, -4]) == -1


def test_maximum_mixed_numbers():
    assert maximum([-10, 20, -5, 30]) == 30
    assert maximum([-50, 0, 10, -20]) == 10


def test_maximum_repeated_numbers():
    assert maximum([5, 5, 5, 5]) == 5
    assert maximum([10, 20, 20, 10]) == 20 


# minimum()

def test_minimum_positive_numbers():
    assert minimum([10, 20, 5, 30]) == 5
    assert minimum([1, 2, 3, 4]) == 1


def test_minimum_negative_numbers():
    assert minimum([-10, -20, -5, -30]) == -30
    assert minimum([-1, -2, -3, -4]) == -4


def test_minimum_mixed_numbers():
    assert minimum([-10, 20, -5, 30]) == -10
    assert minimum([-50, 0, 10, -20]) == -50


def test_minimum_repeated_numbers():
    assert minimum([5, 5, 5, 5]) == 5
    assert minimum([10, 20, 20, 10]) == 10


# average()

def test_average_positive_numbers():
    assert average([10, 20, 30, 40]) == 25
    assert average([2, 4, 6]) == 4


def test_average_negative_numbers():
    assert average([-10, -20, -30]) == -20
    assert average([-5, -15, -10]) == -10


def test_average_mixed_numbers():
    assert average([-10, 20, -5, 15]) == 5
    assert average([-5, 5]) == 0


def test_average_float_numbers():
    assert average([1.5, 2.5, 3.5]) == 2.5
    assert average([2.5, 3.5]) == 3 