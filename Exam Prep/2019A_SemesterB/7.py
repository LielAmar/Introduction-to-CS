# Solution:
#     f(x) = int(sqrt(x))
#     
#     rec(f, [1, 100, 4, 64])
#     [1] + ...
#       rec(f, [100, 4, 64])
#       [10] + ...
#         rec(f, [4, 64])
#         [2] + ...
#           rec(f, [64])
#           [8] + ...
#             []
#  [1,10,2,8]
#  

# if 0: print("0")
# else: print("not 0")
# if 1: print("1")
# else: print("not 1")
# if []: print("[]")
# else: print("not []")
# if [1]: print("[1]")
# else: print("not [1]")
# if '': print("''")
# else: print("not ''")
# if 'a': print("'a'")
# else: print("not 'a'")