def count_strings(n):
    return count_helper(n, False)

def count_helper(n, is_last_one):
    if n <= 0: return 1
    if n == 1: return 1 if is_last_one else 2

    # For 0
    sum = count_helper(n-1, False)

    # If we didn't hace one in the last iteration
    if not is_last_one:
        sum += count_helper(n-1, True)

    return sum

if __name__ == "__main__":
    assert count_strings(0) == 1
    assert count_strings(1) == 2
    assert count_strings(2) == 3
    assert count_strings(3) == 5
    assert count_strings(4) == 8
    assert count_strings(5) == 13
    assert count_strings(6) == 21

