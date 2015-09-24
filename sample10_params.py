import pytest


@pytest.fixture(params=[1,2,3])
def params_data(request):
    data = request.param
    if data == 1:
        return "params is set to one"
    elif data == 2:
        return "params is set to two"
    else:
        return "params is set to three"


def test_1(params_data):
    print ("test_1: %s" % params_data)
    assert params_data != "params is set to two"
