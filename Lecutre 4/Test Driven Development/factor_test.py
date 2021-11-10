from factor import factor

def test_factor_of_one() -> None:
    assert factor(1) == []

def test_factor_primes() -> None:
    assert factor(2) == [2]
    assert factor(3) == [3]
    assert factor(5) == [5]
    assert factor(7) == [7]

def test_factor_non_primes() -> None:
    assert factor(4) == [2, 2]
    assert factor(6) == [2, 3]
    assert factor(8) == [2, 2, 2]
    
    # assert factor(25) == [2, 3, 5]
