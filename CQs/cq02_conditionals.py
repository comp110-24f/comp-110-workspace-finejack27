"""CQ02 Conditionals"""

__author__ = "730756949"


def guess_a_number() -> None:
    secret: int = 7

    userGuess: int = int(input("Guess a number: "))
    print("Your guess was " + str(userGuess))

    if userGuess == secret:
        print("You got it!")
    elif userGuess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
