"""Counting letters in a string."""

__author__ = "730519109"

s: str = input("What letter do you want to search for?: ")
st: str = input("Enter a word: ")

i: int = 0
count: int = 0

while i < len(st):
    if st[i] == s:
        count = count + 1
        i=i+1
    else:
        i=i+1
b: str=str(count)
print("Count: " + b )
#i Begin your solution here...