# Solution:
#   lsty1 = [1,3]
#   lsty2 = [[4],[5]]
#   
#   zoom(lsty1, lsty2):
#     t = lsty2[0][0]        = 4
#     c = lsty1              = [1,3]
#     c[0] (a[0]) = b[1]     = [5]   (c(a) = [[5], 3])
#     b = [c[:][1], c[:][1]] = [3,3] (b    = [3,3])
#     b[-1] = a[0][:]        = [5]   (b    = [3, [5]])
#     a[0][0] = t            = 4     (c(a) = [[4], 3])
#     print(a) -> [[4], 3]
#     print(b) -> [3, [5]]
#     print(c) -> [[4], 3]

def zoom(a, b):
    t = b[0][0]
    c = a
    c[0] = b[1]
    b = [c[:][1], c[:][1]]
    b[-1] = a[0][:]
    a[0][0] = t
    print(a)
    print(b)
    print(c)
    
lsty1 = [1,3]
lsty2 = [[4],[5]]
zoom(lsty1, lsty2)
