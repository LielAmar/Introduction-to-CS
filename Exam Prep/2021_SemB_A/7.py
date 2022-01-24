# Solution:
#
#   f7(6674, 5):
#     res = 0
#     st = "6674"
#    
#     if n > 0: (True)
#       x = 0
#     else: (False)
#       x = 1
#     # x is 0 at this point
#
#     for i in range(x=0, len(st)+1=4+1=5):
#       y = st[:0] + str(5) + st[0:]  ->  y = "56674"
#       res = max(0, 56674) -> 56674
#     
#     return 66754
#
#  res: 66754