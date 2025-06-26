import pytest
import s0c0.main as hw

def test_add():
    assert hw.add(1, 2) == 3

def test_add_edge():
    assert hw.add(-999, 999) == 0

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        hw.divide(5, 0)
