from numb3rs import validate

def test_range():
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False
    assert validate("0.0.0.0.256") == False
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_char():
    assert validate("cat") == False
    assert validate("a.a.a.a") == False
    assert validate("0.0.0.l") == False

def test_nonip():
    assert validate("This is my ip 0.0.0.0") == False
