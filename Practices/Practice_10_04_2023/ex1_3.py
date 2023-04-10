class A:
    pass


class B(A):
    pass


class C(B):
    pass


def get_inheritance(T):
    return ' -> '.join([c.__name__ for c in T.mro()])


print(get_inheritance(C))
