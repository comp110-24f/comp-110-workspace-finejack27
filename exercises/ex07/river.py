"""File to define River class."""

__author__ = "730756949"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """A class that defines a river."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        # testing a comment to comply with style rules
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove any fish older than 3 and any bears older than 5."""
        # testing a comment to comply with style rules
        # Below, we make a temporary empty list and fill it with
        # every acceptable fish. Then, we make the true list of fish
        # equal to this temp list.
        temp_fish: list[Fish] = []
        for floppa in self.fish:
            if floppa.age < 4:
                temp_fish.append(floppa)
        self.fish = temp_fish

        # Same process as above for bears below...
        temp_bears: list[Bear] = []
        for growler in self.bears:
            if growler.age < 6:
                temp_bears.append(growler)
        self.bears = temp_bears

        return None

    def remove_fish(self, amount: int):
        """This will remove 'amount' many Fish from the River, starting at index 0."""
        # testing a comment to comply with style rules
        # This errored for me at the very end, so I had to add the if statement piece
        temp_fish: list[Fish] = []
        for idx in range(len(self.fish)):
            if idx >= amount:
                temp_fish.append(self.fish[idx])
        self.fish = temp_fish

    def bears_eating(self):
        """If at least 5 Fish in the river, each Bear will eat 3 Fish."""
        # testing a comment to comply with style rules
        # I had the for loop inside the if loop originally. I didn't understand
        # the wording of the instructions.
        for growler in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                growler.eat(3)
        return None

    def check_hunger(self):
        """For each Bear, if hunger_score < 0, remove the Bear from the river."""
        # testing a comment to comply with style rules
        # Temp list used below to not change a list as we iterate through it
        temp_bears: list[Bear] = []
        for growler in self.bears:
            if growler.hunger_score >= 0:
                temp_bears.append(growler)
        self.bears = temp_bears

        return None

    def repopulate_fish(self):
        """For n fish, there will be (n//2) * 4 new Fish added to fish."""
        # testing a comment to comply with style rules
        num_pairs: int = int(len(self.fish) / 2)
        num_offspring: int = num_pairs * 4
        for i in range(num_offspring):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """For n bears, there will be n//2 new Bears added to bears."""
        # testing a comment to comply with style rules
        num_pairs: int = int(len(self.bears) / 2)
        num_offspring: int = num_pairs
        for i in range(num_offspring):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Print out 3 lines to visualize the river on a current day."""
        # testing a comment to comply with style rules
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # testing a comment to comply with style rules
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Call one_river_day seven times."""
        # testing a comment to comply with style rules
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
