import calc

def test_add_positive_numbers():
    result = calc.add(3, 4)
    assert result == 7

def test_add_negative_numbers():
    result = calc.add(-2, -5)
    assert result == -7