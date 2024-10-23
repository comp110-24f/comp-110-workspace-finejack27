"""Testing different functions"""


def get_first(input: list[str]) -> str:
    """Returns first element in list"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Pop off the first element in a list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Takes a list of strings and returns (and
    later removes) the first element"""
    first: str = input[0]
    input.pop(0)
    return first
