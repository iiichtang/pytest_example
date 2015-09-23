#http://pydoing.blogspot.tw/2011/02/python-hasattr.html

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


class TestClass2:
    def test_three(self):
        x = "this"
        assert 'h' in x

    def test_four(self):
        x = "hello"
        assert hasattr(x, 'damn you')

    def test_five(self):
        x = "hello"
        assert hasattr(x,"You suck")
