def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


fib_cache: list = []

def fib_efficient(n):
    if len(fib_cache) < n:
        return fib_cache[n]

    fib_cache.append(fib_efficient(n-1) + fib_efficient(n-2))
    return fib_cache[n]