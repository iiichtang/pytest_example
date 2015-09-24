#http://pydoing.blogspot.tw/2011/01/python-raise.html
#https://docs.python.org/2/tutorial/errors.html

import pytest


def f():
    raise SystemExit(1)


def test_raise():
    with pytest.raises(SystemExit):
        f()

def test_raise2():
    with pytest.raises(IOError):
        f()


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
