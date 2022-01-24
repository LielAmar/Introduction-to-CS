from functools import reduce

def count_larger_than_n (n, lst):
    filter_result = filter(lambda x: x > n, lst)
    return reduce(lambda count, _: count+1, filter_result, 0)

print(count_larger_than_n(10, [1,2,12,51,20,5]))