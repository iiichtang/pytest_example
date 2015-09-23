def func(x):
    return x + 1

def test_assert():
    assert 0

def test_assert2():
    assert 1


def test_answer():
    assert func(3) == 4

def test_answer2():
    assert func(3) == 5

def test_answer3():
    expected = 5
    real_result = func(3)
    assert expected == real_result
	

def test_answer4():
    a = 3
    assert a % 2 == 0, "value was odd, should be even"
