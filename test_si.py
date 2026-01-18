from si import calculate_simple_interest

def test_simple_interest_basic():
    assert calculate_simple_interest(1000, 5, 2) == 100

def test_simple_interest_zero():
    assert calculate_simple_interest(0, 5, 2) == 0

def test_simple_interest_decimal():
    assert calculate_simple_interest(1500, 4.5, 3) == 202.5
