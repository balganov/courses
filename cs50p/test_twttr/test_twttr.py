from twttr import shorten

def test_all_vowels():
    assert shorten("AEIOUxxx") == "xxx"

def test_case():
    assert shorten("AaEexxx") == "xxx"

