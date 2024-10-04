"""CQ04 Importing & Scope on September 30 2024"""

__author__ = "730756949"


def get_coords(xs: str, ys: str) -> None:
    """This function will print the formatted pairs of each character in the two input strings"""

    indexx: int = 0
    # Originally had my indexy var up here, too. See below...

    while indexx < len(xs):
        indexy: int = 0  # THIS WAS SUCH A TRICKSTER! Must not forget about scope!
        # You don't want this y-index var to reach the maximum outside of this while loop.
        # This was halting my progress after the first time the y index reached the length of ys.

        while indexy < len(ys):
            print("(" + xs[indexx] + "," + ys[indexy] + ")")
            # Getting this syntax correct is hard. I mustn't forget the addition symbols!
            indexy += 1

        indexx += 1


# FUNC TEST: get_coords("12", "34")
