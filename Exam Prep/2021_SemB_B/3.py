# while = log2(n)
#   while = log2(n)
#     O(n)

# log2(n)^2*n = n*n = O(n^2)


def f3(n):
    ctr = 0

    a=0
    i, j = n, 1
    while i>0:
        ctr += 1

        i//=2
        while j<n:
            ctr += 1
            
            j*=2
            for k in range(n):
                ctr += 1

                k+=2
                a+=i+j+k
    return (a, ctr)


data_collector = dict()

for i in range(1000):
    res, ctr = f3(i)

    data_collector[i] = ctr
    print("i=", ctr)