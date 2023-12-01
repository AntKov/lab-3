import calculator

def test_add_positive_numbers():
    result = calculator.add(3, 4)
    assert result == 7

def test_add_negative_numbers():
    result = calculator.add(-2, -5)
    assert result == -7