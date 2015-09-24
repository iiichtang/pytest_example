import pytest


#Input as a parameter
@pytest.fixture()
def f():
    print ("\nfixture executed")


def test_1(f):
    print ("test1")

def test_2():
    print ("test2")
