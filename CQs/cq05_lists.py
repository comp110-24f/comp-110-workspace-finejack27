"""Mutating functions."""

__author__ = "730756949"


def manual_append(my_list: list[int], my_int: int) -> None:
    """This function manually adds an int to an int-list"""
    my_list.append(my_int)


def double(my_list: list[int]) -> None:
    """This function loops through each index in a list
    and doubles the literal value"""
    index: int = 0

    while index < len(my_list):
        my_list[index] = my_list[index] * 2
        index = index + 1
        # I tried to run this but forgot to increment
        # my index every time so it looped infinitely


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
