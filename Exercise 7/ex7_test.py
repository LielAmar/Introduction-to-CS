from ex7 import *

def test_mult_function_valid_input():
    assert mult(2, 3) == 6
    assert mult(5, 1) == 5
    assert mult(5, 0) == 0
    assert mult(1.111, 3) == 3.333
    assert mult(2.25, 4) == 9

def test_is_even_valid_input():
    assert is_even(0) == True
    assert is_even(8) == True
    assert is_even(479) == False
    assert is_even(9) == False

def test_log_mult_function_valid_input():
    assert log_mult(2, 3) == 6
    assert log_mult(5, 1) == 5
    assert log_mult(5, 0) == 0
    assert log_mult(1.111, 3) == 3.333
    assert log_mult(2.25, 4) == 9
    assert log_mult(1, 100) == 100

def test_is_power_function_valid_input():
    assert is_power(2, 16) == True
    assert is_power(3, 16) == False
    assert is_power(3, 17) == False
    assert is_power(3, 27) == True
    assert is_power(4, 8) == False
    assert is_power(4, 16) == True
    assert is_power(5, 125) == True

def test_reverse_function_valid_input():
    assert reverse("Intro") == "ortnI"
    assert reverse("intro") == "ortni"
    assert reverse("Hello") == "olleH"
    assert reverse("Amazing") == "gnizamA"
    assert reverse("eDgE cAsE") == "EsAc EgDe"
    assert reverse("ANOtheR OnE?") == "?EnO RehtONA"