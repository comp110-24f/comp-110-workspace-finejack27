"""CQ04 Importing & Scope on September 30 2024"""

__author__ = "730756949"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# I had to figure out to add CQs. in front of cq04.concatenation

x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
