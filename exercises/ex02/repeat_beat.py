"""Repeating a beat in a loop."""

__author__ = "730519109"

a: str = input("What beat do you want to repeat? ")
b: str= input("How many times do you want to repeat it? ")
c: int = int(b)
d: str = ""
i: int = c

if c == 0:
    print("No beat...")
else:
    while i!= 0:
       if i==1:
         d=d+a
         i=i-1
       else:
         d=d+a+" "
         i=i-1
print(d)


# Begin your solution here...