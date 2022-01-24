# Solution:
# 
#     k == 5 != 0:
#       result = [k, (k-1)*rlm(k-1)]                   = 2 + 1 + 1 + 1 + 1 + 1
#         k == 4 != 0:
#           result = [k, (k-1)*rlm(k-1)]               = 2 + 1 + 1 + 1 + 1
#             k == 3 != 0:
#               result = [k, (k-1)*rlm(k-1)]           = 2 + 1 + 1 + 1
#                 k == 2 != 0:
#                   result = [k, (k-1)*rlm(k-1)]       = 2 + 1 + 1
#                     k == 1 != 0:
#                       result = [k, (k-1)*rlm(k-1)]   = 2 + 1
#                         k == 0: return [k, []]       = 2
#       return result

#  k = 0:
#    create 2
#  k = 1:
#    create 2
#  k = 2:
#    create 1
#  k = 3:
#    create 1
#  k = 4:
#    create 1
#  k = 5:
#    create 1

print(0*(1,2,3))