class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state

    def stabilize(self):
        for i in range(1000):
            self.next()

    def next(self):
        pass


class LogisticMap(Chaos):

    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state


o = LogisticMap(2, 0.1)
print(o.next(), o.next(), o.next())

o = LogisticMap(3.2, 0.1)
print(o.next(), o.next(), o.next())

o = LogisticMap(3.5, 0.1)
print(o.next(), o.next(), o.next())

o = LogisticMap(3.55, 0.1)
print(o.next(), o.next(), o.next())