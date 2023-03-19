import math


def main(a, b, z):
    result = 0
    for j in range(1, b+1):
        for i in range(1, a+1):
            result += 46*(math.log(97*(j**3))) - \
                ((math.cos(i-1-(i**3)))**6)-(z**7)
    return result
