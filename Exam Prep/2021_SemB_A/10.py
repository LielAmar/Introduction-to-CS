# Solution:
# 
#   gene(120, 1):
#     if num=120 < 10: (False)
#       yield num
#     else:
#       yield from gene(120//t=120, t+1=2) ->
#         ->
#         gene(120, 2):
#           if num=120 < 10: (False)
#             yield num
#           else:
#             yield from gene(120//t=60, 3) ->
#               ->
#               gene(60,3):
#                 if num=60 < 10: (False)
#                   yield num
#                 else:
#                   yield from gene(60//t=20, 4) ->
#                     ->
#                     gene(20, 4):
#                       if num=20 < 10: (False)
#                         yield num
#                       else:
#                         yield from gene(20//4=5, 5) ->
#                           ->
#                           gene(5,5):
#                             if num=5 < 10: (True)
#                               yield num
#
#                         yield 20//t = 5
#
#                   yield 60//t = 20
#     
#             yield 120//t = 60
#
#       yield 120//t = 120

# [5,5,20,60,120]