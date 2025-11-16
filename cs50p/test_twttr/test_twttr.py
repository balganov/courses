from twttr import shorten

def test_all_vowels():
    assert shorten("AEIOUxxx") == "xxx"

def test_case():
    assert shorten("AaEexxx") == "xxx"

def test_num_sym():
    assert shorten("AaEe1*,.xxx") == "1*,.xxx"

