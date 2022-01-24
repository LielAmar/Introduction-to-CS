from functools import *

def is_rotation(s1, s2):
    if s1 == s2:           return True
    if len(s1) != len(s2): return False

    return s1 in (s2 + s2)

assert is_rotation("", "") == True
assert is_rotation("a", "") == False
assert is_rotation("intro", "troin") == True
assert is_rotation("intro", "rotin") == False
assert is_rotation("hello", "llohe") == True
assert is_rotation("hello", "ollhe") == False
