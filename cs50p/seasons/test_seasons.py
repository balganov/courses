import pytest
from seasons import minutes

def test_date():
    with pytest.raises(SystemExit) as e:
        minutes("Sep 19, 1992")
    assert e.value.code == "Invalid date"

def test_result():
    assert minutes("1992-09-19") == "Seventeen million, four hundred sixty thousand minutes"
