import pytest


#autouse
@pytest.fixture(autouse=True)
def f():
    print ("\nfixture executed")
    return "fixture's return value"

def test_1():
    print ("test1")
    print f

def test_2(f):
    print ("test2")
    print f

class TestClass:
    def test_3(self):
        print ("test3")
        print f

    def test_4(self,f):
        print ("test4")
        print f

