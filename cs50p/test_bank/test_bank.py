from bank import value

def test_money():
    assert value("Hey") != 100
    assert value("Hello") == 0
    assert value("Whatsup") != 20
