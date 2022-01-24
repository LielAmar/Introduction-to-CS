# Solution:
#
#   i = 1
#   while i < n:      -> O(n)
#     j = i
#     while j < n:    -> O(1)
#       while j < n:  -> O(n-i)
#         j += 1
#       j += 1
#     i += 1
#
#  O(n^2)