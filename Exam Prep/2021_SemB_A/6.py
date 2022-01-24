# Solution:
#
#   lst = [3]  
#   adi = func(y) -> {
#     lst.insert(0, y[0])
#     print(lst)
#     if y[1]:
#       lst.pop()  
#   }
#
#  adi((0,2)) -> lst = [0,3]
#  print([0,3])
#  lst = [0]
#  adi((1,0)) -> lst = [1,0]
#  print([1,0])
#  adi((None, None)) -> lst = [None,1,0]
#  print([None,1,0])