import math

height = float(input("Enter height: "))
rad = float(input("Enter radius: "))

def Volume(h, r):
    return (math.pi * r * r * h)

print(Volume(height, rad))