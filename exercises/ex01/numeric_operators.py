"""two numbers with operations performed on them"""
__author__= "730519109"


x = input("Left-hand side: ")
y = input("Right-hand side: ")
a = int(x)
b = int(y)

exp = a ** b
exp = str(exp)
print(x+" ** "+y+" is "+exp)
div = a / b
div = str(div)
print(x+" / "+y+" is "+div)
div2 = a // b
div2 = str(div2)
print(x+" // "+y+" is "+div2)
mod = a % b
mod = str(mod)
print(x+" % "+y+" is "+mod)

