import math


def main(n):
    if n == 0:
        return 0.19
    elif n == 1:
        return 0.35
    elif n >= 2:
        return 49*((math.atan(main(n-1)))**3)\
            + (math.tan(main(n-2)))+1
