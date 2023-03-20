class MyClass:
    def __init__(self):
        self.state = 'A'

    def snap(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'F'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 7
        raise MilliError("snap")

    def tail(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'F':
            self.state = 'C'
            return 8
        raise MilliError("tail")

    def draw(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'B'
            return 6
        raise MilliError("draw")


class MilliError(Exception):
    pass


def main():
    return MyClass()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.snap() == 0
    assert o.snap() == 3
    o = main()
    assert o.snap() == 0
    assert o.draw() == 2
    assert o.draw() == 4
    assert o.draw() == 6
    assert o.draw() == 2
    assert o.draw() == 4
    assert o.snap() == 5
    assert o.snap() == 7
    assert o.tail() == 8
    o = main()
    assert o.tail() == 1
    # raises(lambda: o.snap(), MilliError)
    # raises(lambda: o.draw(), MilliError)
    raises(lambda: o.tail(), MilliError)
    assert o.snap() == 5
    raises(lambda: o.draw(), MilliError)
    assert o.snap() == 7
    raises(lambda: o.snap(), MilliError)
# coverage run --branch -m pytest
