import pytest

#decorator
@pytest.fixture()
def f():
    print ("\nfixture executed")
    return "fixture's return value"

@pytest.mark.usefixtures("f")
def test_1():
    print ("test1")
    print f

@pytest.mark.usefixtures("f")
def test_2():
    print ("test2")
    print f

class TestClass_1:
    @pytest.mark.usefixtures("f")
    def test_3(self):
        print ("test3")
        print str(f)

    @pytest.mark.usefixtures("f")
    def test_4(self):
        print ("test4")
        print f

@pytest.mark.usefixtures("f")
class TestClass_2:
    def test_5(self):
        print ("test5")
        print f

    def test_6(self):
        print ("test6")
        print f

