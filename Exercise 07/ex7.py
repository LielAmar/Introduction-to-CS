from typing import Any, List

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

    if x == 1:
        return True

    return _is_power_helper(b, b, x)

def _is_power_helper(b: int, current: int, x: int) -> bool:
    """
    A helper function to calculate whether b is a power of x
    """

    if current > x:
        return False
    
    if current == x:
        return True

    return _is_power_helper(b, int(log_mult(current, b)), x)


def reverse(s: str) -> str:
    """
    Reverses a string
    """
    
    return _reverse_helper(s, "", len(s) - 1)

def _reverse_helper(s: str, current: str, index: int) -> str:
    """
    A helper function to reverse append the last character of a string to
    the beginning of ${current} using recursion
    """

    if index == -1:
        return current
    
    return _reverse_helper(s, helper.append_to_end(current, s[index]), index - 1)


def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """
    Solves the Hanoi Game problem
    
    Unfortunately it's too freaking hard to explain why this works in a single
    comment, so please trust me - IT WORKS!

    For more information, please visit my tablet :)
    """

    if n <= 0:
        return

    play_hanoi(Hanoi, n - 1, src, temp, dst)
    Hanoi.move(src, dst)
    play_hanoi(Hanoi, n - 1, temp, dst, src)


def number_of_ones(n: int) -> int:
    """
    Calculates the amount of times the digit '1' appears in all numbers from
    1 to n
    """
    
    # base case
    if n <= 0:
        return 0

    # returns the number of occurrences of 1 in ${n} and recursively calls
    # number_of_ones on ${n - 1}
    return _number_of_ones_helper(n) + number_of_ones(n - 1)

def _number_of_ones_helper(n: int) -> int:
    """
    A helper recursive-function to check how many times the digit '1'
    appears in the given number ${n}
    """

    # base case
    if n <= 0:
        return 0

    occurrences = 0

    # if the remainder of the current number divided by 10 is 1, obviously we
    # have the digit 1 appearing in the last index of the number
    if n % 10 == 1:
        occurrences += 1

    # if the result of division by 10 (no remainder) is not 1, we want to keep
    # on checking the number divided by 10.
    # For example:
    #   15 // 1 = 1
    #   we'll run the same function on '1' and we'll get a result of one
    #   in the next iteration
    if n // 10 != 1:
        occurrences += _number_of_ones_helper(n // 10)
    
    # if the division of n by 10 (no remainder) is 1, we obviously landed on 1
    # so we add +1 to the occurrences
    else:
        occurrences += 1

    # returning the amount of occurrences we got
    return occurrences


def compare_2d_lists(l1: List[List[int]], 
        l2: List[List[int]]) -> bool:
    """
    Compares 2 2D lists
    """

    return _compare_2d_lists_helper(l1, l2, row_idx=0, column_idx=0)

def _compare_2d_lists_helper(l1: List[List[int]],
        l2: List[List[int]], row_idx: int, column_idx: int) -> bool:
    """
    A helper function to check if the 2 given 2D arrays are equal
    """

    # If the amount of l1's columns/current row is not equal to
    # l2's columns/current row    
    if len(l1) != len(l2) or len(l1[0]) != len(l2[0]):
        return False

    # If we're checking a row that's beyond the lists' limit, we've finished
    # our comparison
    if row_idx >= len(l1):
        return True

    # If the current column is beyond the list's limit, we've finished the
    # current iteration, so we move on to the next row
    if column_idx >= len(l1[row_idx]):
        return _compare_2d_lists_helper(l1, l2, row_idx + 1, 0)

    # we return whether the current element of l1 is equal to the l2's element,
    # and keep on comparing the next element in the row
    return (l1[row_idx][column_idx] == l2[row_idx][column_idx]
            and _compare_2d_lists_helper(l1, l2, row_idx, column_idx + 1))


def magic_list(n: int) -> List[Any]:
    """
    Returns a magic list of size n
    """

    if n == 0:
        return []
    
    return _magic_list_helper(n, 0)

def _magic_list_helper(n: int, idx: int) -> List[Any]:
    """
    A helper function to calculate the magic list of ${n} and ${indx}
    in such way:
    
    it calculates the magic list for ${n - 1} and ${idx} and then repeats
    that to get a new instance of the previous list, then appends it to the previous
    list
    """

    if idx == n:
        return []

    res = _magic_list_helper(n - 1, 0)
    res.append(_magic_list_helper(n - 1, 0))
    return res