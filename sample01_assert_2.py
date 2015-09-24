def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

def test_answer2():
    assert func(3) == 5

def notest_answer3():
    assert func(3) == 5

def test_answer4():
    assert func(3) == 5, "This is not a correct answer!"

def test_answer5():
    assert func(3) == 4
    assert func(3) == 5, "The test will stop here"
    assert func(3) == 6
    


def test_answer6():
    expected = 5
    real_result = func(3)
    assert expected == real_result

