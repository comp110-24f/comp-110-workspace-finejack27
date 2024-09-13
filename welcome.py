"""A welcoming test program to start COMP110"""

__author__ = "01234567"


def get_ticket_price_a() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price


def get_ticket_price_b() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age > 60:
        price: int = 5
    else:
        price: int = 10
    return price


def get_ticket_price_c() -> int:
    age: int = int(input("What is your age?"))
    if (age <= 12) or (age > 60):
        price: int = 5
    else:
        price: int = 10
    return price


def get_ticket_price_d() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age <= 60:
        price: int = 10
    return price


print(get_ticket_price_a())
print(get_ticket_price_b())
print(get_ticket_price_c())
print(get_ticket_price_d())
