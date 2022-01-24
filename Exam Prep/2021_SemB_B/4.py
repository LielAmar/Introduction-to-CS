# Solution:
#     f4(2):
#       g(x, d):
#         if x<= 0: return 1
#         return d(x)
#       h(x):
#         return x*g(x-1, h)
#     return g(x, h)
#
#    g(2,h) -> h(2) = 2*g(1, h)
#    g(1,h) -> h(1) = 1*g(0, h)
#    g(0,h) -> 1
#  = 2*1*1 = 2