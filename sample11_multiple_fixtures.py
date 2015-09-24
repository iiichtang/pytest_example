import pytest

@pytest.fixture()
def func_1():
    return 1

@pytest.fixture()
def func_2():
    return 2

@pytest.fixture()
def func_3():
    return 3

def test_sum(func_1, func_2, func_3):
    expected = 6
    real_result = func_1 + func_2 + func_3
    assert expected == real_result

