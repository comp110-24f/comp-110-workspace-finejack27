"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730756949"


def input_word() -> str:
    # This function will store a 5-character word input from the user as a variable and return it.
    chosen_word: str = str(input("Enter a 5-character word: "))
    # I originally wrote my creative variable names in camel case instead of snake case.
    if int(len(chosen_word)) == 5:
        return chosen_word
        # I forgot the syntax of the length feature. I was using chosen_word(len) instead of len(chosen_word)
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return chosen_word
        # I had trouble getting the correct order of these three lines above. I was confused on what to return.


def input_letter() -> str:
    # This function will store a single character input from the user as a variable and return it.
    chosen_char: str = str(input("Enter a single character: "))
    if int(len(chosen_char)) == 1:
        return chosen_char
    else:
        print("Error: Character must be a single character.")
        exit()
        return chosen_char


def contains_char(word: str, letter: str) -> None:
    # This function will utilize print every time a letter is found in a 5-character word.

    # I originally had the letter and word parameters immediately define as the return
    # variables of input_letter() and input_word() but realized that is too specific for
    # this broad-use function.
    print("Searching for " + letter + " in " + word)
    count: int = 0

    # I specifically did not use a loop because the directions implied we should not yet.
    if word[0] == letter:
        print(str(letter) + " found at index 0")
        count += 1
    if word[1] == letter:
        print(str(letter) + " found at index 1")
        count += 1
    if word[2] == letter:
        print(str(letter) + " found at index 2")
        count += 1
    if word[3] == letter:
        print(str(letter) + " found at index 3")
        count += 1
    if word[4] == letter:
        print(str(letter) + " found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
