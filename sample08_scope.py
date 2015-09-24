
#function 	Run once per test
#class    	Run once per class of tests
#module 	Run once per module
#session 	Run once per session

import pytest

@pytest.fixture(scope="module")
def func(request):
    print ("\nsetup of a fixture function")
    def a_function():
        print ("\nteardown of a fixture function")
    request.addfinalizer(a_function)

def test_data1(func):
    return None

def test_data2():
    return None

@pytest.mark.usefixtures("func")
class TestClass1:
    def test_data3(self):
        return None

    def test_data4(self):
        return None



class TestClass2:
    def test_data5(self, func):
        return None

    def test_data6(self, func):
        return None 

    def test_data7(self):
        return None



