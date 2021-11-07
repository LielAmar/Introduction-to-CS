def is_vormir_safe(min_temp, first_day, second_day, third_day):
    """Checks if the temperature on vormir is safe"""
    first_check = check_two_days_for_temp(min_temp, first_day, second_day)
    second_check = check_two_days_for_temp(min_temp, first_day, third_day)
    third_check = check_two_days_for_temp(min_temp, second_day, third_day)

    return first_check or second_check or third_check

def check_two_days_for_temp(min_temp, first_day, second_day):
    """Checks if both provided days had higher temperature than
    the minimum temperature given"""
    return first_day > min_temp and second_day > min_temp

if __name__ == "__main__":
    print(is_vormir_safe(7, 5, -2, 11))