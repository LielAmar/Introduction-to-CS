import math

def shape_area():
    """Calculates the area of the given shape through input"""
    shape_type = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))

    if shape_type == 1:
        return calculate_circle_area(float(input()))
    elif shape_type == 2:
        return calculate_rectengle_area(float(input()), float(input()))
    elif shape_type == 3:
        return calculate_equilateral_triangle_area(float(input()))

def calculate_circle_area(radius):
    return math.pi * math.pow(radius, 2)

def calculate_rectengle_area(first_side, second_side):
    return first_side * second_side

def calculate_equilateral_triangle_area(side):
    return (math.sqrt(3) / 4) * math.pow(side, 2)


if __name__ == "__main__":
    print(shape_area())