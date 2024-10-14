"""Summing the elements of a list using different loops"""

__author__ = "730756949"


def w_sum(vals: list[float]) -> float:
    """This function uses a while loop to sum floats in a list"""
    index: int = 0
    sum: float = 0.0
    # I originally had sum = 0, but noticed that would be an int

    while index < len(vals):
        sum = sum + vals[index]
        index += 1

    return sum


def f_sum(vals: list[float]) -> float:
    """This function uses a for-in loop to sum floats in a list"""
    sum: float = 0.0
    # No index var needed, as the following for loop has
    # direct access to the elements already.

    for val in vals:
        sum += val

    return sum


def f_range_sum(vals: list[float]) -> float:
    """This function uses a for-in-range loop to sum floats in a list"""
    sum: float = 0.0
    # I saved a millisecond by using += instead of the other way

    for idx in range(0, len(vals)):
        sum += vals[idx]

    return sum
