Testing in Python
=================

py.test
-------

* installation: `pip install pytest`
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
* usefull commands
 * `py.test -v` verbose output
 * `py.test -s` print stdout/stderr (hidden by default)
 * `py.test -k <pattern>` only execute tests containing <pattern>
* fixtures 
* can also run nosetest, unittest and doctest 


problems with writing testable code
-----------------------------------
* implicit dependencies &rarr; dependency injection
```python
def process_everything():
    db = Database()
    data = db.select('*')
    return process(data)
```
&darr&;
```python
def process_everything(db):
    data = db.select('*')
    return process(data)
```

