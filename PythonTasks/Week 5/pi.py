from math import pi

def rug_calculator(radius):
    circumfrence = pi * (2 * radius)
    area = pi * radius * radius
    print(circumfrence, area)


rug_calculator(100000000)
