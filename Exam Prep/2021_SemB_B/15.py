def n_of_sums(n, k, fun):
    numbers = []
    
    result = k
    while result > 0:
        numbers.append(result)
        result = fun(result)
    
    solutions = []
    get_combinations(n, numbers, set(), solutions)
    
    return len(solutions)
    
def get_combinations(target, numbers, path, solutions):
    if target < 0:
        return
    
    if target == 0:
        if path not in solutions: solutions.append(path)
        return
    
    for i, number in enumerate(numbers):
        get_combinations(target-number, numbers[:i] + numbers[i+1:], \
                set(list(path) + [number]), solutions)
    
if __name__ == "__main__":
    assert n_of_sums(6, 4, lambda a: a - 1) == 2
    assert n_of_sums(12, 12, lambda b: b - 2) == 4
    assert n_of_sums(11, 8, lambda x: x // 2) == 1
    assert n_of_sums (7, 4, lambda y: y - 3) == 0

    