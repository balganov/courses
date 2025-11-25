from working import convert
import pytest

def test_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 9 PM")

def test_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9 PM")

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_result():
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"
