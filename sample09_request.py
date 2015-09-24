import pytest


@pytest.fixture()
def use_request(request):
    print ("fixturename = %s" % request.fixturename)
    print ("scope = %s" % request.scope)
    print ("function = %s" % request.function.__name__)
    print ("cls = %s" % request.cls)
    print ("module = %s" % request.module.__name__)
    print ("fspath = %s" % request.fspath)

    if request.function.__name__ == "test_3":
        request.applymarker(pytest.mark.xfail)
        #https://pytest.org/latest/mark.html#mark

def test_1(use_request):
    print ("test_1():")

class TestClass():
    def test2(self, use_request):
        print ("test_2():")

def test_3(use_request):
    print ("test_3():")
    assert False













