# Solution:
#     g(x) = x+1
#     f(x) = 2x
#     
#     i = 0
#     list(map(lambda x: x(i), [g, f]))
#     value = [1, 0]
#   [1,0]
#     i = 1
#     list(map(lambda x: x(i), [g, f]))
#     value = [2, 2]
#   [2,2]
#     i = 2
#     list(map(lambda x: x(i), [g, f]))
#     value = [3, 4]
#   [3,4]


from typing import Iterable


h = lambda x: lambda y: lambda z: x+y+z
print(h(1)(2)(3))

def x(x):
    def y(y):
        def z(z):
            return x+y+z
        return z
    return y

print(x(1)(2)(3))


def map_2(fn, it: Iterable):
    for x in it:
        yield fn(x)


g = lambda x: x+1
f = lambda x: 2*x

for i in range(3):
    value = list(map_2(lambda x: x(i), [g, f]))
    print(value)
