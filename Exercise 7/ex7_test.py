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

def test_number_of_ones_valid_input():
    assert number_of_ones(13) == 6
    
    # 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21
    assert number_of_ones(21) == 13

    # above + 31, 41, 51
    assert number_of_ones(59) == 13 + 3

    # above + 61, 71, 81, 91, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112
    assert number_of_ones(112) == 16 + 22
    
    # above + 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130
    assert number_of_ones(130) == 16 + 22 + 26

def test_number_of_ones_invalid_input():
    assert number_of_ones(-1) == 0