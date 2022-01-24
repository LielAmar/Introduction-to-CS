# def subsets_with_sum(n,lst):
#     # if 7 in lst:
#     #     print("n", n)
#     #     print("lst", lst)
#     if not lst:
#         if n == 0:
#             print("found! remaining: ", lst)
#         return 1 if n == 0 else 0

#     return 1 if n == 0 else sum([subsets_with_sum(n-num, lst[:i] + lst[i+1:]) for i, num in enumerate(lst)])

def subsets_with_sum(n, lst):
    if not lst: return 1 if n == 0 else 0

    return subsets_with_sum(n-lst[0], lst[1:]) + subsets_with_sum(n, lst[1:])

lst = [1,2,3,5,7]

print(subsets_with_sum(8, lst))
print(subsets_with_sum(0, lst))
print(subsets_with_sum(-7, lst))