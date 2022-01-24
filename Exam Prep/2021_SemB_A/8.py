# Solution:
# 
#   first = [0,1,2,3,4]
#   second = [0,1,2,3,4]
#   first = [4,3,2,1,0]

#   goo(second[4]=4)

#   i = 4
#   if i > 0:
#     i = 3
#     goo(3):
#       i = 3
#       if i > 0:
#           i = 2
#           goo(2):
#             i = 2
#             if i > 0:
#               goo(1):
#                 goo(0)
#                 print(1, end=" ")
#                 goo(0)
#               print(2, end=" ")
#               goo(1)
#                 goo(0)
#                 print(1, end=" ")
#                 goo(0)
#            

# goo(0) = ""
# goo(1) = goo(0) + "0 "                      -> "0 "
# goo(2) = goo(1) + "1 " + goo(0)             -> "0 1 "
# goo(3) = goo(2) + "2 " + goo(1)             -> "0 1 2 0 "
# goo(4) = goo(3) + "3 " + goo(2)             -> "0 1 2 0 3 0 1 "

# 0 1 2 0 3 0 1 