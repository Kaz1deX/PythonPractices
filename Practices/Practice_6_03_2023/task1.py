
def pr1(dictionary):
    result = int(dictionary['Z6']) << 6
    result = (result + int(dictionary['Z5'])) << 2
    result = result << 6
    result = (result + int(dictionary['Z3'])) << 6
    result = (result + int(dictionary['Z2'])) << 3
    result += int(dictionary['Z1'])
    return str(hex(result))


# print(pr1({'Z1': '3', 'Z2': '2', 'Z3': '11', 'Z5': '32', 'Z6': '525'}))
# print(pr1({'Z1': '5', 'Z2': '55', 'Z3': '2', 'Z5': '53', 'Z6': '1016'}))
# print(pr1({'Z1': '3', 'Z2': '46', 'Z3': '43', 'Z5': '29', 'Z6': '387'}))
# print(pr1({'Z1': '3', 'Z2': '47', 'Z3': '51', 'Z5': '40', 'Z6': '550'}))


def pr2(tup):
    result = int(tup[5]) << 1
    result = (result + int(tup[4])) << 4
    result = (result + int(tup[3])) << 1
    result = (result + int(tup[2])) << 9
    result = (result + int(tup[1])) << 9
    result += int(tup[0])
    return str(result)


# print(pr2((376, 159, 1, 0, 1, 21)))
# print(pr2((130, 60, 1, 11, 1, 52)))
# print(pr2((396, 444, 0, 14, 0, 33)))
# print(pr2((110, 199, 1, 12, 0, 27)))


def pr3(number):
    result = int(number, 16)
    r1 = result & 0b1111
    result >>= 4
    r2 = result & 0b111111111
    result >>= 9
    r3 = result & 0b111
    result >>= 3
    r4 = result & 0b111
    result >>= 3
    r5 = result & 0b111111
    return [('R', str(r1)), ('R2', str(r2)), ('R3', str(r3)), ('R4', str(r4)), ('R5', str(r5))]


# print(pr3('0x6a9f6'))
# print(pr3('0x2464d1'))
# print(pr3('0x18ba48b'))
# print(pr3('0xb077e5'))


def pr4(number):
    result = int(number, 16)
    n1 = result & 0b111111
    result >>= 6
    n2 = result & 0b111111
    result >>= 6
    n3 = result & 0b1111111
    result >>= 7
    n4 = result & 0b11
    result >>= 2
    n5 = result & 0b111
    return {'N1': n1, 'N2': n2, 'N3': n3, 'N4': n4, 'N5': n5}


# print(pr4('0xb9a562'))
# print(pr4('0x85c1a5'))
# print(pr4('0xe3fb96'))
# print(pr4('0x2909e9'))
