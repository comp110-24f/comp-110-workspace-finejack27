"""CQ04 Importing & Scope on September 30 2024"""

__author__ = "730756949"


def concat(input1: str, input2: str) -> str:
    """This function returns the squished together string of two string inputs"""
    return input1 + input2
    # No need for a new variable that holds input1 + input2. Just return that!


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"

    print(concat(word1, word2))
