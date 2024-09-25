"""A program that calculates a total cost to have a tea party!"""

__author__ = "730756949"


def main_planner(guests: int) -> None:
    # This function will take a number of guests and then calculate the gross cost of a tea party!
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    # I STRUGGLED here. I was able to fix it on my own, but I was freaking out because I was getting
    # error after error after error. Luckily I caught the fact I was missing a colon in the signature!
    # I also nearly forgot to contain a $ in the fourth print statement. Lastly, I almost forgot to
    # stringify my returned values from the various function calls inside the print statements! Doh!


def tea_bags(people: int) -> int:
    # This function will return the number of tea bags required based on the number of guests
    return people + people
    # This function was easy; I could have made it return people*2 but I chose to go with addition


def treats(people: int) -> int:
    # This will return the number of treats needed based on the total count of teas guests are expected to drink
    return int(tea_bags(people=people) * 1.5)
    # I had to keep the people variables straight in my head during this part


def cost(tea_count: int, treat_count: int) -> float:
    # This will calculate the cost of the tea bags and the treats combined
    return float((tea_count * 0.5) + (treat_count * 0.75))
    # This function was pretty intuitive. Gotta remember to ensure I am returning a float though!


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # This was an easy copypasta
