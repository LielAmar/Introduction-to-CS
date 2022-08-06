def largest_and_smallest(first_number, second_number, third_number):
    """Returns the largest & smallest numbers"""
    max = min = first_number

    if max < second_number:
        max = second_number
    if max < third_number:
        max = third_number

    if min > second_number:
        min = second_number
    if min > third_number:
        min = third_number

    return max, min

def check_largest_and_smallest():
    """Checks the validity the largest_and_smallest function"""
    first_test_max, first_test_min = largest_and_smallest(17, 1, 6)
    second_test_max, second_test_min = largest_and_smallest(1, 17, 6)
    third_test_max, third_test_min = largest_and_smallest(1, 1, 2)
    fourth_test_max, fourth_test_min = largest_and_smallest(0, 0, 0)
    fifth_test_max, fifth_test_min = largest_and_smallest(-40, 0, 40)

    validate_first_test = first_test_max == 17 and first_test_min == 1
    validate_second_test = second_test_max == 17 and second_test_min == 1
    validate_third_test = third_test_max == 2 and third_test_min == 1
    validate_fourth_test = fourth_test_max == 0 and fourth_test_min == 0
    validate_fifth_test = fifth_test_max == 40 and fifth_test_min == -40

    return (validate_first_test and validate_second_test
            and validate_third_test and validate_fourth_test
            and validate_fifth_test)

if __name__ == "__main__":
    print(largest_and_smallest(5.3, 7.8, 2.2))
    print(check_largest_and_smallest())