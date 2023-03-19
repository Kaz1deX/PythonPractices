def main(number):
    result = int(number, 16)
    m1 = result & 0b111111
    result >>= 6
    m2 = result & 0b1111
    result >>= 4
    m3 = result & 0b1111
    result >>= 4
    m4 = result & 0b111111111
    result >>= 9
    m5 = result & 0b11
    result >>= 2
    m6 = result & 0b1111
    return (str(m1), str(m2), str(m3), str(m4), str(m5), str(m6))
