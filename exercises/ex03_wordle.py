"""EX03 - Wordle - An interactive guessing game."""

__author__: str = "730756949"


def input_guess(secret_word_len: int) -> str:
    """The user will make a guess of the same length of the
    secret word. If the guess is a length different from that
    of the secret word, the guess is not wasted."""

    verbiage_1: str = f"Enter a {secret_word_len} character word: "
    verbiage_2: str = f"That wasn't {secret_word_len} chars! Try again: "
    # After remembering this function should be usable for any secret
    # word length, I had trouble formatting the verbiage, but decided
    # to create new vars, seen above. I do not know how this could
    # be more efficient and not cause an error inside the input block.
    # I did use a formatted string though!

    guess: str = str(input(verbiage_1))

    while len(guess) != secret_word_len:
        guess = str(input(verbiage_2))

    return guess


def contains_char(phrase: str, char: str) -> bool:
    """This function searches each index in a string for another
    string which is expected to be 1 character long"""

    assert len(char) == 1

    index: int = 0

    while index < len(phrase):
        if phrase[index] == char:
            return True
        index += 1

    return False
    # This function was easy to basically copy from EX_02 Chardle


def emojified(user_guess: str, secret_word: str) -> str:
    """This function will compare 2 strings of the same length.
    The first string will is the user’s guess and the 2nd is
    the secret word. A string of relevant emojis will be returned."""

    assert len(user_guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_string: str = ""

    index: int = 0
    while index < len(user_guess):
        if user_guess[index] == secret_word[index]:
            emoji_string += GREEN_BOX
            # This scenario is when we're at an index in both
            # the guess and the secret word, and the letter is
            # the same, meaning we should have a green box
            # indicating the letter guessed here is correct!
        elif contains_char(secret_word, user_guess[index]):
            emoji_string += YELLOW_BOX
            # I had to really think about what the arguments
            # would be in order to comply with contains_char.
            # Also, I had a redundant == True that I did not
            # need in the elif line because contains_char(...)
            # evaluates to a boolean and we don't need to compare
            # booleans.
        else:
            emoji_string += WHITE_BOX

        index += 1

    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turn_num: int = 1
    has_won: bool = False

    while turn_num <= 6 and (has_won == False):
        print(f"=== Turn {turn_num}/6 ===")

        guess: str = input_guess(len(secret))

        print(emojified(guess, secret))

        if guess == secret:
            has_won = True
        else:
            turn_num += 1

    if has_won:
        print(f"You won in {turn_num}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
