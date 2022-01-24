def dec(other):
    def dec2():
        return other(6, 10)
    print(dec2())
    return print

@dec
def func(a, b):
    return a - b

# func = dec(lambda a, b: a - b)(6, 10)
    
func(6, 10)

# -4
# 6 10