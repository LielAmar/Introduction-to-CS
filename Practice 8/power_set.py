def power_set(A):
    if len(A) == 0:
        return [[]]
    
    a = A[0]
    rest = power_set(A[1:])
    return rest + [[a] + s for s in rest]