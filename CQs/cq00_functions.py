"""CQ00"""

__author__ = "730756949"


def mimic(message: str) -> str:
    """A function that mimics what it is given."""
    return message


def main() -> None:
    """A function that implements the high-level logic of this program."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
