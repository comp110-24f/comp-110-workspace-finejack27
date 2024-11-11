"""File to define Bear class."""


class Bear:
    """A class that defines a bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a bear instance."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase a bear's age as a day passes."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """This will update the Bear’s hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish
