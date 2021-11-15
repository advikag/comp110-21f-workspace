"""Practice with dictionaries."""

__author__ = "730519109"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """Function to invert the dictionary."""
    inv: dict[str, str]
    inv = dict()
    for key in x:
        i = x[key]
        j = key
        inv[i] = j
       
    return inv
       
    
def favorite_color(y: dict[str, str]) -> str:
    """Function to find the most popular color."""
    fav: str = ""
    p: dict[str, int]
    p = dict()
    max: int = 0
    fav: str = " "
    for key in y:
        c = y[key]
        count2: int = 0
        for key in y:
            if c == y[key]:
                count2 = count2 + 1
                o: int = count2
                p[key] = o
    for i in p:
        if max > p[i]:
            fav = i
    return fav


def count(u: list[str]) -> dict[str, int]:
    """Function to count the number of times a value is present."""
    b: dict[str, int]
    b = dict()
    
    for i in u:
        item = i
        b[i] = 0
        for j in u:
            if j == item:
                b[i] = b[i] + 1
    
    return b