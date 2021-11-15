"""Relational operators"""
__author__  =  "730519109"

x = input("Left hand side: ")
y = input("right hand side: ")
x_int = int(x)
y_int = int(y)
a = x_int < y_int
a = str(a)
print(x + " < "+ y +" is " + a)
b = x_int >= y_int
b = str(b)
print(x + " >= " + y + " is " + b)
c =  x_int == y_int
c = str(c)
print(x+" == "+y+" is "+c)
d = x_int != y_int
d = str(d)
print(x+" != "+y+" is "+d)
