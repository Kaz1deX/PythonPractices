import struct


def read_d_structure(data, address):
    d1, d2, d3, d4 = struct.unpack_from('>HIhq', data, address)
    return {
        'D1': d1,
        'D2': d2,
        'D3': d3,
        'D4': d4
    }


def read_c_structure(data, address):
    size_and_address, c2, data_size_and_address = struct.unpack_from(
        '>HixI', data, address)
    c1_size = size_and_address >> 2
    c1_address = size_and_address & ((1 << 16) - 1)
    c1 = []
    for i in range(c1_size):
        d_address = struct.unpack_from(
            '>I', data, address + c1_address + i * 4)[0]
        c1.append(read_d_structure(data, d_address))
    data_address = data_size_and_address & ((1 << 32) - 1)
    data_size = data_size_and_address >> 32
    c3 = struct.unpack_from('>' + 'd' * data_size, data, data_address)
    return {
        'C1': c1,
        'C2': c2,
        'C3': c3
    }


def read_e_structure(data, address):
    e1, e2_1, e2_2, e3 = struct.unpack_from('>HQQb', data, address)
    e2 = (e2_1 << 64) | e2_2
    return {
        'E1': e1,
        'E2': e2,
        'E3': e3
    }


def read_b_structure(data, address):
    b1, b2_address, b3, b4 = struct.unpack_from('>bHiI', data, address)
    b2 = read_c_structure(data, b2_address)
    return {
        'B1': b1,
        'B2': b2,
        'B3': b3,
        'B4': b4
    }


def read_a_structure(data, address):
    a1, a2_address, a3, a4, a5, a6_address, a7, a8_array = struct.unpack_from(
        '>iH6sBIi8H', data, address)
    a2 = read_b_structure(data, a2_address)
    a6 = read_e_structure(data, a6_address)
    a8 = list(struct.unpack_from('>8H', data, address + 28 + 14 + 16))
    return {
        'A1': a1,
        'A2': a2,
        'A3': a3,
        'A4': a4,
        'A5': a5,
        'A6': a6,
        'A7': a7,
        'A8': a8,
    }


def main(data):
    signature = bytes.fromhex('f855484758')
    signature_index = data.find(signature)
    if signature_index == -1:
        raise ValueError('Could not find signature in the data')
    a_address = signature_index + len(signature)
    a = read_a_structure(data, a_address)
    return a


print(main((b'\xf8UHGX\x90)\xcd\x82x\x00ddbfho>\x12\xa4\xfbK\x8f\x00\x00\x00Z\xf4'
            b'\x17:\xcb\x8a\xe18\xc0\xb1\xceo\xba\x88H\x92nW\xa6+\x84:\xbfrrV\xde\xdcQ\xd2'
            b')R\x98\xe0\xf2\xf7\x11\xd0\xbb\x1f\x0fL\xb2\xe1.%\xc9\xe6\xca\xda"0V\x80'
            b'_\xdc?tQ\xbe\x98\xbfA\x93)q\xce\x96E\xc2,\x00\x00\x009\x00\x00\x00'
            b'F\x00\x00\x00S\x00\x00\x00\x17\x85}>\x07\x7f\x1c?\xcb\x04\x00`\x00\xff\x06~'
            b'\x7f\x02\x00\x00\x00p\x00\x00\x00\x12q\xa9\xe3\xe8*\xc3L\xb9\xd4\x9eOn$\xdc'
            b'\xadp\x1b\x1e\n\xe0"\xa6\xff%')))
