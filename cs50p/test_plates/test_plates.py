from plates import is_valid

def test_len():
    assert is_valid("1") == False
    assert is_valid("ASDASDASD") == False
    assert is_valid("CS50") == True
    assert is_valid("") == False

def test_alchar():
    assert is_valid("C550") == False
    assert is_valid("CS555") == True
    assert is_valid("**555") == False
    assert is_valid("PI3.14") == False

def test_digit():
    assert is_valid("AAA111") == True
    assert is_valid("AA11A") == False
    assert is_valid("AA000") == False

