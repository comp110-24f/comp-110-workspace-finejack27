"""CQ03 While Loops on September 18 2024"""

__author__ = "730756949"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
        # I almost forgot to add a "index += 1" line in my while loop!
        # I would have been stuck in an infinite loop if I had left that out.

    return count
