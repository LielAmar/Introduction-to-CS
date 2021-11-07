import math

def quadratic_equation(a, b, c):
    """Calculates the solutions of a quadratic equation"""
    first_expression = (-1)*b
    second_expression = math.pow(b, 2) - 4*a*c
    third_expression = 1 / (2*a)

    if second_expression < 0:
        return None, None
    elif second_expression == 0:
        solution = (first_expression + math.sqrt(second_expression))
        solution = solution * third_expression

        return solution, None
    else:
        first_solution = (first_expression + math.sqrt(second_expression))
        first_solution = first_solution * third_expression

        second_solution = (first_expression - math.sqrt(second_expression))
        second_solution = second_solution * third_expression

        return first_solution, second_solution

def quadratic_equation_user_input():
    """Calculates the solutions of a quadratic equation given
    by use input"""
    a, b, c = input("Insert coefficients a, b, and c: ").split(" ")

    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        first_solution, second_solution = quadratic_equation(a, b, c)
        
        if first_solution != None and second_solution != None:
            print("The equation has 2 solutions:", first_solution,
                                "and", second_solution)
        elif first_solution == None and second_solution == None:
            print("The equation has no solutions")
        else:
            if first_solution == None:
                print("The equation has 1 solution:", second_solution)
            else:
                print("The equation has 1 solution:", first_solution)
            

if __name__ == "__main__":
    print(quadratic_equation(1, 1.5, -1))
    quadratic_equation_user_input()