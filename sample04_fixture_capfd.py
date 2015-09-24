
def f(name):
    print "hello {}".format(name)


def test_f(capfd):
    f("Tom")

    out, err = capfd.readouterr()
    assert out == "hello Tom\n"

def test_f_2(capfd):
    f("Jack")
    
    out, err = capfd.readouterr()
    assert out == "hello Tom\n"
