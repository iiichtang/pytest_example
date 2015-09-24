import pytest


@pytest.fixture()
def func(request):
    print ("\nsetup of a fixture function")
    data = {"item_1":1, "item_2":2, "item_3":3}
    def a_function():
        print ("\nteardown of a fixture function")
    request.addfinalizer(a_function)
    return data

def test_data(func):
    assert func["item_2"] == 2

def test_data2(func):
    assert func["item_3"] == 1

