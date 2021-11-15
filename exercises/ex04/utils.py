"""utility functions."""

__author__ = "730519109"


def all(a: list[int], x: int) -> bool:
    """Function to check if all elements are the same."""
    if len(a) == 0:
        return False
    i: int = 0
    count: int = 0
    while i < len(a):
    
        if(a[i] == x):
            count += 1
            i += 1
        else:
            i += 1
    if(count == len(a)):
        return True
    else:
        return False


def is_equal(b: list[int], c: list[int]) -> bool:
    """Function to check if lists are equal."""
    if len(b) == 0 and len(c) == 0:
        return False
    if(len(c) != len(b)):
        return False
    j: int = 0
    c2: int = 0
    while j < len(b):
        if(b[j] == c[j]):
            c2 += 1
            j += 1
        else:
            j += 1
    if(c2 == len(b) and c2 == len(c)):
        return True
    else:
        return False


def max(d: list[int]) -> int:
    """Function to find the max."""
    if len(d) == 0:
        raise ValueError("max() arg is an empty list")

    m: int = d[0]
    k: int = 0
    while k < len(d):
        if(m < d[k]):
            m = d[k]
            k += 1
        else:
            k += 1
    return m