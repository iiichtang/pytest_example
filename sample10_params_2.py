import pytest

@pytest.fixture(scope="function", params=[1,2,3])
def func(request):
    print ("\nsetup of a fixture function")
    
    def a_function():
        print ("\nteardown of a fixture function")
    request.addfinalizer(a_function)

    data = request.param
    if data == 1:
        return "params is set to one"
    elif data == 2:
        return "params is set to two"
    else:
        return "params is set to three"

def test_data1(func):
    print ("test_1: %s" % func)
    return None


class TestClass():
    def test_data2(self, func):
        print ("test_2: %s" % func)
        return None

    def test_data3(self, func):
        print ("test_3: %s" % func)
        return None
