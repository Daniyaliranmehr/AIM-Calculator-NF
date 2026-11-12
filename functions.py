def add(num1: float, num2: float) -> float:
    """
Add two numbers.

Parameters
----------
num1 : float
    The first number.
num2 : float
    The second number.

Returns
-------
float
    The sum of the two numbers.
"""
    return num1 + num2


def sub(num1: float, num2: float) -> float:
    """
Subtract the second number from the first number.

Parameters
----------
num1 : float
    The first number.
num2 : float
    The second number.

Returns
-------
float
    The difference between the two numbers.
"""
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    """
Multiply two numbers.

Parameters
----------
num1 : float
    The first number.
num2 : float
    The second number.

Returns
-------
float
    The product of the two numbers.
"""
    return num1 * num2


def division(num1: float, num2: float) -> float:
    """
Divide the first number by the second number.

Parameters
----------
num1 : float
    The dividend.
num2 : float
    The divisor.

Returns
-------
float
    The result of the division.
"""
    return num1 / num2


def power(num1: float, num2: float) -> float:
    """
Raise the first number to the power of the second number.

Parameters
----------
num1 : float
    The base number.
num2 : float
    The exponent.

Returns
-------
float
    The result of the exponentiation.
"""
    return num1 ** num2


def mod(num1: float, num2: float) -> float:
    """
Calculate the remainder of the division of two numbers.

Parameters
----------
num1 : float
    The dividend.
num2 : float
    The divisor.

Returns
-------
float
    The remainder of the division.
"""
    return num1 % num2


def maximum(num1: float, num2: float) -> float:
   """
Find the larger of two numbers.

Parameters
----------
num1 : float
    The first number.
num2 : float
    The second number.

Returns
-------
float
    The larger number.
"""
   return max(num1, num2)


def minimum(num1: float, num2: float) -> float:
   """
Find the smaller of two numbers.

Parameters
----------
num1 : float
    The first number.
num2 : float
    The second number.

Returns
-------
float
    The smaller number.
"""
   return min(num1, num2)


def average(num1: float, num2: float) -> float:
    """
Calculate the average of two numbers.

Parameters
----------
num1 : float
    The first number.
num2 : float
    The second number.

Returns
-------
float
    The average of the two numbers.
"""
    return (num1 + num2) / 2

