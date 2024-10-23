"""EX04 List Utils"""

__author__: str = "730756949"


def all(my_list: list[int], my_int: int) -> bool:
    """This function will check if an int-list's
    items are all equal to a given int"""
    if len(my_list) == 0:
        return False
    # I missed the above if statement the first time I submitted!

    index: int = 0

    while index < len(my_list):
        if my_list[index] == my_int:
            index += 1
            # I was tempted to use 'continue' here but I
            # was unsure if I could/should
        else:
            return False

    return True


def max(input: list[int]) -> int:
    """This will return the greatest value in a given list"""

    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    index: int = 0
    # I originally had index start at 1 but then thought about
    # the chance the list could be only 1 item long
    greatest: int = input[0]

    while index < len(input):
        if input[index] > greatest:
            greatest = input[index]
        index += 1

    return greatest


def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """This will return whether two lists have the
    same length and same values at each index"""
    # This was quite EZ

    if len(input_1) != len(input_2):
        return False

    index: int = 0

    while index < len(input_1):
        if input_1[index] == input_2[index]:
            index += 1
        else:
            return False

    return True


def extend(input_1: list[int], input_2: list[int]) -> None:
    """This will mutate the first list by appending the second list to it"""
    # This was quite easy to accomplish!

    index: int = 0

    while index < len(input_2):
        input_1.append(input_2[index])
        index += 1
