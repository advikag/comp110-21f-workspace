"""Drawing forests in a loop."""

__author__ = "730519109"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
d: int = int(input("Depth: "))
i: int = 1
j: int = 1
s: str = " "
while(i <= d):
    
    while(j <= i):
        s = s + " " + TREE
        
        j = j + 1
    print(s)   
    i = i + 1