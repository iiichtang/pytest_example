import pytest


#Input as a parameter
@pytest.fixture()
def f():
    print ("\nfixture executed")
    return "fixture's return value"

def test_1(f):
    print ("test1")
    print f

def test_2():
    print ("test2")
    print f
