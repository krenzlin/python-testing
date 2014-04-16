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
