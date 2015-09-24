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

@pytest.fixture()
def f2():
    data1 = Class1()
    return data1


def test_data(f):
    print f[0].get_data()
    print f[1].get_data()
    assert f[0].get_data() == f[1].get_data()

def test_data2(f2):
    print f2.get_data()
