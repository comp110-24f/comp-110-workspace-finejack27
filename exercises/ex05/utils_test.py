"""EX05 Unit Testing"""

__author__ = "730756949"

from utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_use1() -> None:
    """Testing that only_evens properly returns a list of even
    ints when input contains positive ints and 0"""
    assert only_evens([9, 11, 42, 97, 10, 84]) == [42, 10, 84]


def test_only_evens_use2() -> None:
    """Testing that only_evens properly does not mutate its input
    but rather returns a distinct new list"""
    list_a: list[int] = [-4, -69, -420, 2, 100000001, 0]
    list_b: list[int] = only_evens(list_a)
    assert list_a == [-4, -69, -420, 2, 100000001, 0] and list_b == [-4, -420, 2, 0]


def test_only_evens_edge() -> None:
    """Testing that only_evens returns an empty list when
    given an empty list"""
    assert only_evens([]) == []


# -------------------------------------------------------------------


def test_sub_use1() -> None:
    """Testing that sub properly returns a new list that begins at
    the 'start' index and ends at the 'end' index (not inclusive)"""
    list_a: list[int] = [3, 6, 9, 12, 18]
    assert sub(list_a, 2, 4) == [9, 12]


def test_sub_use2() -> None:
    """Testing that sub properly returns a new list and does not
    mutate the given list"""
    list_a: list[int] = [3, 6, 9, 12, 18]
    list_b: list[int] = sub(list_a, 2, 4)  # [9, 12]
    assert list_a == [3, 6, 9, 12, 18] and list_b == [9, 12]


def test_sub_edge() -> None:
    """Testing the edge case that can handle illogical starts and end index inputs"""
    list_a: list[int] = [1, 23, 45, 6, 78]
    list_b: list[int] = sub(list_a, -9, 10)
    assert list_b == [1, 23, 45, 6, 78]


# -------------------------------------------------------------------


def test_add_at_index_use1() -> None:
    """Testing that add_at_index correctly inserts a new element at a given index."""
    list_a: list[int] = [0, 1, 3, 4, 5, 6]
    add_at_index(list_a, 2, 2)
    assert list_a == [0, 1, 2, 3, 4, 5, 6]


def test_add_at_index_use2() -> None:
    """Testing that add_at_index correctly mutates the original input."""
    list_a: list[int] = [99, 98, 95, 94]
    add_at_index(list_a, 97, 2)
    assert list_a == [99, 98, 97, 95, 94]


def test_add_at_index_edge() -> None:
    """Testing that add_at_index can handle negative numbers."""
    list_a: list[int] = [-99, -98, -95, -94]
    add_at_index(list_a, -97, 2)
    assert list_a == [-99, -98, -97, -95, -94]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    list_a: list[int] = [0, 1, 3, 4, 5, 6]

    with pytest.raises(IndexError):
        add_at_index(list_a, 2, 10)
        # an IndexError is raised for the case when the add_at_index is given an
        # <index_to_insert_num> that is greater than the length of our <list_object>
