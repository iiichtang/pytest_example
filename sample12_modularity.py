import pytest

@pytest.fixture(scope="module")
def func_1():
    return 1

@pytest.fixture()
def func_2(func_1):
    return 2 + func_1


def test_1(func_1):
    assert func_1 == 1

def test_2(func_2):
    assert func_2 == 2

