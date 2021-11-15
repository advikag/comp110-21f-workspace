"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

__author__ = "730519109"
from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """test for the even function."""
    a: list[int] = [3, 4, 5, 6]
    assert only_evens(a) == [4, 6]


def test_sub() -> None:
    """test for the subscript function."""
    c: list[int] = [10, 20, 30, 40]  
    d: int = 1
    e: int = 3
    assert sub(c, d, e) == [20, 30]

def test_concat() -> None:
    """Test for concatination function."""
    g: list[int] = [1, 2, 3, 4]
    h: list[int] = [5, 6, 7, 8]
    assert concat(g, h) == [1, 2, 3, 4, 5, 6, 7, 8]