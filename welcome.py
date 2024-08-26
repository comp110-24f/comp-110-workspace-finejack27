"""A welcoming test program to start COMP110"""

__author__ = "01234567"

"""print("Welcome to COMP110!")
print("You are in for a fun adventure into programming!")
print("<3 the COMP110 Team!")
print("spooky"[len("spooky")])"""


def sum(num1: int, num2: int) -> int:
    """Add two numbers together"""
    return num1 + num2


print(sum(2, 3))
print(sum(num1=2, num2=3))
print(sum(2 + 1, 6 * 2))
