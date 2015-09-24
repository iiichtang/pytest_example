import pytest


#autouse
@pytest.fixture(autouse=True)
def f():
    print ("\nfixture executed")
    return "fixture's return value"

def test_1():
    print ("test1")
    print f

def test_2():
    print ("test2")
    print f

class TestClass_1:
    def test_3(self):
        print ("test3")
        print f

    def test_4(self):
        print ("test4")
        print f

class TestClass_2:
    def test_5(self):
        print ("test5")
        print f

    def test_6(self):
        print ("test6")
        print f

