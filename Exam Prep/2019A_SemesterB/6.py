# Solution:
#   O(n)


# def memoize(f):
#     cache = dict()
#     # k = input, v = output of f

#     def memoized_f(k):
#         if k in cache:
#             return cache[k]
        
#         output = f(k)
#         cache[k] = output
#         return output
    
#     return memoized_f