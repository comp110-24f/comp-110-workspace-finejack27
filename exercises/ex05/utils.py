"""EX05 More List Utility Functions"""

__author__ = "730756949"


def only_evens(my_list: list[int]) -> list[int]:
    """This function will take a list of ints and return a
    new list of only the even items from the input"""

    new_list: list[int] = []

    if len(my_list) == 0:
        return new_list
        # Added this if statement in the Unit Testing phase at the end
        # in order to account for an empty input list

    index: int = 0
    while index < len(my_list):
        if my_list[index] % 2 == 0:
            new_list.append(my_list[index])
        index += 1

    return new_list


def sub(my_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, this function will return a new
    list that begins at the 'start' index and ends at the 'end'
    index minus 1"""

    new_list: list[int] = []

    if len(my_list) == 0 or start >= len(my_list) or end < 1:
        return new_list
        # If the length of the list is 0, start is greater than or equal to the
        # length of the list, or end is at most 0, return the empty list.

    if start < 0:
        start = 0
        # If the start index is negative, start from the beginning of the list.

    if end > len(my_list):
        end = len(my_list)
        # If the end index is greater than the length of the list,
        # end with the end of the list.

    index: int = start
    while index < end:
        # I originally had 'end - 1' instead of 'end' in the above while statement.
        # This is redundant because we already exclude the end thanks to '<'.
        new_list.append(my_list[index])
        index += 1

    return new_list


def add_at_index(my_list: list[int], new_elem: int, index: int) -> None:
    """This will insert a new element into a list of ints at a given index"""

    if index < 0 or index > len(my_list):
        raise IndexError("Index is out of bounds for the input list")

    my_list.append(new_elem)

    for idx in range(len(my_list) - 1, index, -1):
        my_list[idx] = my_list[idx - 1]

    my_list[index] = new_elem
    # This was very tricky to come up with and I had to learn about steps,
    # aka incrementing backwards, in the range of for-loops. This was info
    # attainable via the pop-up in VSCode after typing range(...


list_a: list[int] = [0, 1, 9, 3, 5]
add_at_index(list_a, 9, 3)
print(list_a)
