import pytest
from mymodule import mean


def test_mean():
    assert mean([10, 20]) == 15
    assert mean([100, 300]) == 200
    #assert mean([1, 2]) == 1.5
    
def test_mean_zero_divison():
    with pytest.raises(ZeroDivisionError):
        mean([])
