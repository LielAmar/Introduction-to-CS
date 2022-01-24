# (lambda a, b: a(10, b)())(k, 2)
# k(10, 2) => 10 - 2 = 8
# 8

k = lambda k, p: lambda: k - p
t = (lambda a, b: a(10, b)()) (k, 2)

print(t)