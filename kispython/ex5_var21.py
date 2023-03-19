import math


def main(z, x, y):
    result = 0
    n = len(z)
    for i in range(0, n):
        result += (((y[(n-1)+1-(math.floor(i/2)+1)])/5)
                   + ((z[math.floor((i/4))])**3)
                   + ((x[(math.floor(i/4))])**2))**5
    return result
