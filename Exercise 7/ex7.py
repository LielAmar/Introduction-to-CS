import ex7_helper as helper

def mult(x: float, y: int) -> float:
    """
    Multiplies x and y and returns the value
    """

    if y == 0:
        return 0

    return helper.add(x, mult(x, helper.subtract_1(y)))

def is_even(n: int) -> bool:
    """
    Returns whether the given non-negative integer is even or odd
    """

    if n == 0:
        return True
    return not is_even(helper.subtract_1(n))

def log_mult(x: float, y: int) -> float:
    """
    Mutliplies x and y and returns the value, using O(log(n)) time
    """

    if y == 0:
        return 0

    # y = 10 -> y = 5 -> y = 2 -> y = 1 -> y = 0
    #   y = 0:
    #     - returning 0
    #   y = 1:
    #     - mult_res = 0
    #     - we know 1 is odd, so we add x with 2*0 = x
    #   y = 2:
    #     - mult_res = x
    #     - we know 2 is even so we return 2*x = 2x
    #   y = 5:
    #     - mult_res = 2x
    #     - we know 5 is odd so we add x with 2*(2x) = 5x
    #   y = 10:
    #     - mult_res = 5x
    #     - we know 10 is even so we return 2*(5x) = 10x

    # Calculates the result of the multiplication with the y divided by 2.
    # if y is even in this run, we know we want to return the result times 2,
    # otherwise, we have a lost case for x, so we return the result times 2, 
    # but we also add another x to ensure we get the correct result.
    prev_res = log_mult(x, helper.divide_by_2(y))

    if helper.is_odd(y):
        return helper.add(x, helper.add(prev_res, prev_res))
    
    return helper.add(prev_res, prev_res)


def is_power(b: int, x: int) -> bool:
    """
    Returns whether b is a power of x
    """

    return is_power_helper(b, b, x)

def is_power_helper(b: int, current: int, x: int) -> bool:
    """
    A helper function to calculate whether b is a power of x
    """

    if current > x:
        return False
    
    if current == x:
        return True

    return is_power_helper(b, int(log_mult(current, b)), x)

def reverse(s: str) -> str:
    return reverse_helper(s, "", len(s) - 1)

def reverse_helper(s: str, current: str, index: int):
    if index == -1:
        return current
    
    return reverse_helper(s, helper.append_to_end(current, s[index]), index - 1)