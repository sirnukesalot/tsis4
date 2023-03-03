#Write a Python program to calculate the area of regular polygon.
from math import tan, pi
n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
s = n * (a**2)/(4*tan(pi/n))
print("The area of the polygon is: ",s)