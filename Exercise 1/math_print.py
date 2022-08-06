import math

def sin_30():
 print(math.sin(30))

def tan_50():
 print(math.tan(50))

def cos_86():
 print(math.cos(86))


def golden_ratio():
    # Calculates and prints the golden ratio by the formula:
    # (1 + sqrt(5) ) / 2
    print((1 + math.sqrt(5)) / 2)

def six_squared():
    # Prints the value of 6 squared (6^2)
    print(math.pow(6, 2))

def hypotenuse():
    # Prints the value of the hypotenuse of a right triangle
    # with 12 and 5 as its sides
    print(math.sqrt(math.pow(12, 2) + math.pow(5, 2)))

def pi():
    # Prints the value of pi
    print(math.pi)

def e():
    # Prints the value of e
    print(math.e)

def squares_area():
    # Prints the areas of all squares with a side length of 1 to 10
    print(1*1, 2*2, 3*3, 4*4, 5*5, 6*6, 7*7, 8*8, 9*9, 10*10)


if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()