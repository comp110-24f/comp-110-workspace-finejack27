"""EX06 Dict Utils"""

__author__: str = "730756949"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This will return a new dict of strings with the keys and values inverted"""
    inverted_dict: dict[str, str] = {}

    for key in input_dict:
        # We have to declare the value below to use it later
        value = input_dict[key]
        # Check if the value already exists in inverted_dict
        if value in inverted_dict:
            # I wish if ___ in ___ statements would have been taught earlier
            # in this exercise or in class >:(
            raise KeyError("Duplicate value found: " + value)
        inverted_dict[value] = key

    return inverted_dict


# Personal test use cases for INVERT:
# print(invert({"a": "z", "b": "y", "c": "x"}))
# print(invert({"apple": "cat"}))
# print(invert({"kris": "jordan", "michael": "jordan"}))


def favorite_color(color_dict: dict[str, str]) -> str:
    """This takes a dictionary of names and colors and then
    returns which color is the most popular"""
    color_count: dict[str, int] = {}

    # Count occurrences of each color below
    for color in color_dict:
        value = color_dict[color]
        if value not in color_count:
            color_count[value] = 1
        else:
            color_count[value] += 1

    # Find the most frequent color below
    most_frequent_color: str = ""
    max_count: int = 0

    for color in color_dict:
        value = color_dict[color]
        current_count: int = color_count[value]
        if current_count > max_count:
            most_frequent_color = value
            max_count = current_count

    return most_frequent_color


# Personal test use cases for FAVORITE_COLOR:
# print(favorite_color({"Marc": "yellow",
# "Zak": "blue", "Ezri": "blue", "Kris": "yellow"}))


def count(input_list: list[str]) -> dict[str, int]:
    """With an input of a list[str], this function will return a dict[str, int]
    where each key is a distinct string in the given list and every corresponding
    value is the number of times that string was in the input list."""

    new_dict: dict[str, int] = {}
    for item in input_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


# Personal test use cases for COUNT:
# print(count(["pru", "du", "lo", "pru", "lo", "pru"]))


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """After receiving a list[str], this function will return a dict[str, list[str]]
    where each key is a unique letter in the alphabet and each value is a
    list of the words that begin with that letter."""
    new_dict: dict[str, list[str]] = {}

    for word in words:
        # Convert the first letter of the word to lowercase below
        first_letter: str = word[0].lower()

        # Initialize the list for this letter if it's not already present
        if first_letter not in new_dict:
            new_dict[first_letter] = []

        # Append the word to the appropriate list
        new_dict[first_letter].append(word)

    return new_dict


# Personal test use cases for ALPHABETIZER:
# print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Given an attendance dict of strings and lists of strings, we'll mutate that
    attendance dict with a given day and student, and return nothing"""

    if day not in attendance:
        attendance[day] = []

    attendance[day].append(student)


# Personal test use cases for UPDATE_ATTENDANCE:
# attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
# update_attendance(attendance_log, "Tuesday", "Vrinda")
# update_attendance(attendance_log, "Wednesday", "Kaleb")
# print(attendance_log)
