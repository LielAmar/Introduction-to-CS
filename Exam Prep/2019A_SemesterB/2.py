# Solution: 

#   begin

#   "x_0"


def h():
    print("begin")
    for i in range(2):
        yield i
        print('x_' + str(i))
    print("end")

z = h()
next(z)
next(z)
# next(z)