Testing (with Python)
=====================
* importance and usefulness are well known
* but still often unsued
* two major problems (beside many more)
 * inconvenient to write and need for boilerplate code
 * seen as useful but optional tool
* try to tackle both problems
 * py.test &rarr; easy to write and use tests for python
 * testing as a essential part of software development

why testing?
============
* verify (written) code
* also usefull in reverse to demonstrate errors, bugs and missing functionality
 * e.g. in bug fixing
 * write test that exploits the bug
 * fix the bug
 * test again to verify the fix
* confidence-building benefits
 * Did I break it?
 * Can I fix it?
 * Lets try it!
* obtain new view on your code
 * modularity and coupling
 * API and overal design
 * code smells
* tests as additional specs
 * reimplement software by using the tests
* **good** tests &rarr; maintainable and reusable code (&rarr; better code)


how to test?
============
`mymodule.py`

```python
def mean(list_of_numbers):
    """"Return mean of a list of numbers."""
    return sum(list_of_numbers) / len(list_of_numbers)
```

### 1. fire up the python shell

```python
>>> from mymodule import mean
>>> mean([10, 20])
15
>>> mean([100, 300])
200
```

### 2. make it a file

```python
if __name__ == '__main__':
    print mean([10, 20]), 'should be 15'
    print mean([100, 300]), 'should be 200'
```

### 3. the `assert` statement

```python
if __name__ == '__main__':
    assert mean([10, 20]) == 15
    assert mean([100, 300]) == 200
```

coverage
========

py.test und coverage


* install pytest-cov `pip install pytest-cov`
* py.test finds it

```
py.test --cov . test_all.py --cov-report=html --cov-report=term
```

* not sure about how . and test_all are interacting
* but with this it test every py module in place
* but it seems like its not running the authors.py

```
coverage run --branch `which py.test`
```

diff-coverage
* https://github.com/edx/diff-cover

mocking
=======

* http://www.voidspace.org.uk/python/mock/getting-started.html
* `pip install mock`

### where to patch
* http://www.voidspace.org.uk/python/mock/patch.html#where-to-patch
* scenario

```
a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> use SomeClass
```

do `@patch(‘b.SomeClass’)`

but if its

```
b.py
    -> import a impo
    -> use a.SomeClass
```

do `@patch(‘a.SomeClass’)`

talks
====
* https://www.youtube.com/watch?v=ukm64IUANwE
