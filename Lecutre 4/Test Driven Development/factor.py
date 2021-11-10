def factor(num: int) -> list[int]:
    divisor = 2
    result = []

    while num >= divisor**2:
        if num % divisor == 0:
            result.append(divisor)
            num = num//divisor
        else:
            divisor += 1

    if num != 1:
        result.append(num)
    
    return result