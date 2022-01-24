def max_peaks(n):
    def rec_peaks(n, val):
        if n < 10:
            return True
        elif val:
            return n % 10 < ((n//10) % 10) and rec_peaks(n//10, not val)
        else:
            return n % 10 > ((n//10) % 10) and rec_peaks(n//10, not val)

    return rec_peaks(n, True) or rec_peaks(n, False)

assert max_peaks(1) == True
assert max_peaks(12) == True
assert max_peaks(11) == False
assert max_peaks(123) == False
assert max_peaks(21448) == False
assert max_peaks(2817263549) == True
assert max_peaks(21438790) == True