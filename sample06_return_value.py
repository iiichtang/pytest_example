import pytest


@pytest.fixture()
def some_data():
    data = {"item_1":1, "item_2":2, "item_3":3}
    return data

def test_data(some_data):
    assert some_data["item_2"] == 2

def test_data2(some_data):
    assert some_data["item_3"] == 1

