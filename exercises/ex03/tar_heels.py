"""An exercise in remainders and boolean logic."""

__author__ = "730519109"

s: int = int(input("Enter a int: "))
if s % 2 == 0 and s % 7 == 0 :
    print("TAR HEELS")
else:
    if s % 2 == 0:
        print("TAR")
    else:
        if s % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")