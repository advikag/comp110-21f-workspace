"""List utility functions part 2."""

__author__ = "730519109"
# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    """Function to return the even numbers."""
    i: int = 0
    b: list[int] = list()
    j: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            b.append(a[i])
            j += 1
            i += 1
        else:
            i += 1
    if len(b) == 0:
        return []
    else:
        return b


def sub(c: list[int], d: int, e: int) -> list[int]:
    """Function to return the values between subscripts."""
    f: list[int] = list()
    if d < 0 :
        d = 0
    if e > len(c):
        e = len(c) - 1
    i: int = d
    while(i < e):
        f.append(c[i])
        i += 1
           
    if len(f) == 0:
        return []
    else:
        return f
        

def concat(g: list[int], h: list[int]) -> list[int]:
    """Function to concatinate the lists."""
    z: list[int] = list()
    i: int = 0
    while i < len(g):
        z.append(g[i])
        i += 1
    j: int = 0
    while j < len(h):
        z.append(h[j])
        j += 1
    return z