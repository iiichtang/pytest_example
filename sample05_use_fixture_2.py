import pytest

#decorator
@pytest.fixture()
def f():
    print ("\nfixture executed")
    return "fixture's return value"

@pytest.mark.usefixtures("f")
def test_1(f):
    print ("test1")
    print f

@pytest.mark.usefixtures("f")
def test_2(f):
    print ("test2")
    print f

class TestClass_1:
    @pytest.mark.usefixtures("f")
    def test_3(f):
        print ("test3")
        print f

    @pytest.mark.usefixtures("f")
    def test_4(f):
        print ("test4")
        print f

@pytest.mark.usefixtures("f")
class TestClass_2:
    def test_5(f):
        print ("test5")
        print f

    def test_6(f):
        print ("test6")
        print f

