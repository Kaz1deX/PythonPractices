class MyClass:
    def __init__(self):
        self.state = 'A'

    def coast(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'E':
            self.state = 'B'
            return 7
        raise MealyError("coast")

    def stash(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'G':
            self.state = 'A'
            return 9
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'B':
            self.state = 'F'
            return 3
        raise MealyError("stash")


class MealyError(Exception):
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
    assert o.coast() == 0
    assert o.coast() == 2
    assert o.stash() == 4
    assert o.stash() == 5
    assert o.stash() == 6
    assert o.stash() == 8
    assert o.stash() == 9
    assert o.stash() == 1
    assert o.stash() == 5
    assert o.coast() == 7
    assert o.stash() == 3
    assert o.stash() == 8
    raises(lambda: o.coast(), MealyError)
    o.state = 'x'
    raises(lambda: o.stash(), MealyError)

# coverage run --branch -m pytest
