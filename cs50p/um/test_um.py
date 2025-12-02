from um import count

def test_um():
    assert count("yummy tom yum") == 0
    assert count("UM text") == 1
    assert count("text um, um...") == 2
    assert count("um um, um*") == 3
