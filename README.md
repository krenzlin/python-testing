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
