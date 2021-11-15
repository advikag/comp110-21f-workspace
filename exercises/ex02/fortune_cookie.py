"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730519109"


a: str = "You will have a good week"
b: str = "You will win the lottery"
c: str = "You will meet a very special person tomorrow"
d: str = "You will get what you've been wishing for soon"
e: str = "You are going to recieve very good news"

print("Your fortune cookie says....")
from random import randint

x: int = randint(1,5)


if x == 1:
    print(a)
else:
    if x == 2:
        print(b)
    else:
        if x== 3:
            print(c)
        else:
            if x == 4:
                print(d)
            else:
                print(e)
print("Now, go spread positive vibes!")

              

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...