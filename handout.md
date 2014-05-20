Testing in Python
=================

py.test
-------

* install `pip install pytest`
* uses `assert` statement
```python
def mean(xs):
    return sum(xs) / len(xs)

def test_mean():
    assert mean([10, 20]) == 15
    assert mean([10, 20]) != 10
    
    assert 10 in [10, 20]
    assert [10, 20] is not [20, 10]
```
* asserting an exception
```python
import py.test

def test_mean_zero_division():
    with pytest.raises(ZeroDivisionError):
        mean([])
```

* automatic test discovery
 * `test_*.py` or `*_test.py` files
 * `Test*` classes (without an `__init__` method)
 * `test_*` functions or methods are test items
