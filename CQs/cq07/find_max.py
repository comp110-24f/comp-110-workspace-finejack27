"""CQ07 - Find Maximum and remove all instances"""

__author__ = "730756949"


def find_and_remove_max(input: list[int]) -> int:
    """This will find and return the largest
    number in the input list. This will also
    remove all instances of the largest number
    from the input list."""
    if len(input) == 0:
        return -1
    # The above if-statement handles empty lists

    index: int = 0
    greatest: int = input[0]

    while index < len(input):
        if input[index] > greatest:
            greatest = input[index]
        index += 1
    # The above loop identifies the maximum value
    # in the list. This could have been its own function.

    index = 0
    # I could have just made a new index var
    # for the second while loop (below)

    while index < len(input):
        if input[index] == greatest:
            input.pop(index)
            index -= 1
            # The above line is VERY IMPORTANT
            # to not skip an index. I remember
            # from previous classes that resetting
            # the index is important when popping.
        index += 1
    # The above iterates through the list again,
    # this time popping all instances of the maximum

    return greatest
