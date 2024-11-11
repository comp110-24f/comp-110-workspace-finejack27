"""File to define Fish class."""


class Fish:
    """A class that defines a fish."""

    age: int

    def __init__(self):
        """Initialize a fish instance."""
        self.age = 0
        return None

    def one_day(self):
        """Increase a fish's age as a day passes."""
        self.age += 1
        return None
