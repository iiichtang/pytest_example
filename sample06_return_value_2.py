import pytest

class Class1:
    def __init__(self):
        self.data = 1111
    def get_data(self):
        return self.data

class Class2:
    def __init__(self):
        self.data = "string"

    def get_data(self):
        return self.data

@pytest.fixture()
def f():
    class_list = list()
    data1 = Class1()
    class_list.append(data1)
    data2 = Class2()    
    class_list.append(data2)
    return class_list


def test_data(f):
    print
    print f[0].get_data()
    print f[1].get_data()

def test_data2(f):
    assert f[0].get_data() == 1111
    assert f[1].get_data() == "string"

def test_data3(f):
    assert f[0].get_data() == f[1].get_data()

