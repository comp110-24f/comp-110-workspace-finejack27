"""Unit Test of find_max"""

__author__ = "730756949"

from find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    """case tests"""
    my_list: list[int] = [1, 2, 3, 3, 2, 1]

    assert find_and_remove_max(my_list) == 3
    # Above is a use case test to ensure the function returns the correct maximum

    assert my_list == [1, 2, 2, 1]
    # Above is a use case test to ensure the function mutates the list correctly

    assert find_and_remove_max([-1, -69, -900, -1, -1]) == -1
    # Above is an edge case that ensures the function returns the correct value
    # in case of an unconventional input, this time being negative ints.
