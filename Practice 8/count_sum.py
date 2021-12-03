def count_sums(a, s):
    # return count_sums_helper(a, s, 0)
    if s < 0:
        return 0

    if len(a) == 0:
        if s == 0:
            return 1
        return 0
        
    return count_sums(a[1:], s) + count_sums(a[1:], s-a[0])

# def count_sums_helper(a, target, value):
    if value >= target:
        return []

    results = []

    for number in a:
        number_results = count_sums_helper(a, target, value + number)
        
        for res in number_results:
            results.append([number] + res)

    return results


print(count_sums([1, 2, 3, 4, 5], 5))