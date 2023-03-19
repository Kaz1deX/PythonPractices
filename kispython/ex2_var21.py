import math


def main(y):
    if y < 52:
        return 13*(y**2)
    elif 52 <= y and y < 108:
        return (55*y)**7
    else:
        return (abs(y))/71+80*(y**6)+56*(y**3)
