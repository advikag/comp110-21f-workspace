"""Finding duplicate letters in a word."""

__author__ = "730519109"

s: str = input("Enter a word: ")
i: int = 0
j: int = 1
c: int = 0

while i < len(s):

    while j < len(s):
        if s[i] == s[j]:
            c = c + 1
        j = j + 1
    i = i + 1
    j = i + 1

if c > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")






