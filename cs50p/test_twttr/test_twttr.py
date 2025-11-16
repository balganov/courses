from twttr import shorten

def test_all_vowels():
    assert shorten("aeiouxxx") == "xxx"

def test_case():
    assert shorten("AaEexxx") == "xxx"

