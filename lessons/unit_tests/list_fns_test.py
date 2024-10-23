"""Testing functions in list_fns"""

from list_fns import get_first, remove_first


def test_get_first() -> None:
    # Other code can go here
    assert get_first(input=["Vik", "Sam", "Izz"]) == "Vik"


def test_remove_first() -> None:
    my_TAs: list[str] = ["Viktorya", "Samy", "Benjamin"]
    remove_first(my_TAs)
    assert my_TAs == ["Samy", "Benjamin"]


# HOW TO TEST IN TERMINAL:
# ------------------------
# 1. python
# 2. quit()
# 3. python -m pytest lessons/unit_tests/list_fns_test.py
