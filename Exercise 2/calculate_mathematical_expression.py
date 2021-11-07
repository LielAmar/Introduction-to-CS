
def calculate_mathematical_expression(first_number, second_number,
                                      operation):
    """Calculates the mathematical expression of 'first_number' and
    'second_number' for the operator 'operation' and returns the
    result
    """
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return  first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == ":":
        if second_number == 0:
            return None
        return first_number / second_number

    return None

def calculate_from_string(expression):
    """Calculates the mathematical expression of 'expression' 
    using the 'calculate_from_expression' function and
    returns the result
    """
    first_number, operation, second_number = expression.split(" ")
    first_number = float(first_number)
    second_number = float(second_number)

    return calculate_mathematical_expression(first_number,
                                             second_number, operation)


if __name__ == "__main__":
    print(calculate_from_string('5.5 + 3.3'))
