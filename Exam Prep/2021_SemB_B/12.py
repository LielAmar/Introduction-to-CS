def map_collatz(k, fun):
    counter = 0
    
    for i in collatz(k):
        fun(i)
        counter += 1
    
    return counter

def collatz(k):
    if k <= 1:
        yield k
        return
    
    yield k
    
    if k % 2 == 0:
        yield from collatz(k/2)
        return
    
    yield from collatz(3*k + 1)

if __name__ == "__main__":
    def f1(k):
        print((k+1)/0.25)
    
    ans = map_collatz(6, f1)
    assert ans == 9

    ans = map_collatz(5, print)
    assert ans == 6
    
    liz = []
    l_len = map_collatz(13, liz.append)
    print(liz, l_len)
    
    zed = set()
    z_len = map_collatz(10, zed.add)
    print(zed, z_len)
