from struct import unpack_from, calcsize


class Types:
    uint16 = 'H'
    int16 = 'h'
    char = 's'
    float = 'f'
    int8 = 'b'
    int64 = 'q'
    uint64 = 'Q'
    uint32 = 'I'
    int32 = 'i'
    double = 'd'
    uint8 = 'B'


class BinaryReader:
    def __init__(self, data, offset, order='<'):
        self.data = data
        self.offset = offset
        self.order = order

    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_e(reader):
    e1 = reader.read(Types.uint16)
    e2 = [reader.read(Types.uint64) for _ in range(2)]
    e3 = reader.read(Types.int8)
    return dict(E1=e1, E2=e2, E3=e3)


def read_d(reader):
    d1 = reader.read(Types.uint16)
    d2 = reader.read(Types.uint8)
    d3 = reader.read(Types.int16)
    d4 = reader.read(Types.int64)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


def read_c(reader):
    c1_size = reader.read(Types.uint16)
    c1_offset = reader.read(Types.uint16)
    c1_reader = reader.jump_to(c1_offset)
    c1 = [read_d(reader.jump_to(c1_reader.read(Types.uint32)))
          for _ in range(c1_size)]

    c2 = reader.read(Types.int32)

    c3_size = reader.read(Types.uint32)
    c3_offset = reader.read(Types.uint32)
    c3_reader = reader.jump_to(c3_offset)
    c3 = [c3_reader.read(Types.float) for _ in range(c3_size)]
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader):
    b1 = reader.read(Types.int8)
    b2 = read_c(reader)
    b3 = reader.read(Types.int16)
    b4 = reader.read(Types.uint32)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4)


def read_a(reader):
    a1 = reader.read(Types.int32)

    b_offset = reader.read(Types.uint16)
    b_reader = reader.jump_to(b_offset)
    a2 = read_b(b_reader)

    a3 = b''.join([reader.read(Types.char) for _ in range(6)]).decode()
    a4 = reader.read(Types.uint8)
    a5 = reader.read(Types.int32)

    e_offset = reader.read(Types.uint32)
    e_reader = reader.jump_to(e_offset)
    a6 = read_e(e_reader)

    a7 = reader.read(Types.int16)
    a8 = [reader.read(Types.uint16) for _ in range(8)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(data):
    return read_a(BinaryReader(data, 5))


print(main((b'\xf8UHGX\x90)\xcd\x82x\x00ddbfho>\x12\xa4\xfbK\x8f\x00\x00\x00Z\xf4'
            b'\x17:\xcb\x8a\xe18\xc0\xb1\xceo\xba\x88H\x92nW\xa6+\x84:\xbfrrV\xde\xdcQ\xd2'
            b')R\x98\xe0\xf2\xf7\x11\xd0\xbb\x1f\x0fL\xb2\xe1.%\xc9\xe6\xca\xda"0V\x80'
            b'_\xdc?tQ\xbe\x98\xbfA\x93)q\xce\x96E\xc2,\x00\x00\x009\x00\x00\x00'
            b'F\x00\x00\x00S\x00\x00\x00\x17\x85}>\x07\x7f\x1c?\xcb\x04\x00`\x00\xff\x06~'
            b'\x7f\x02\x00\x00\x00p\x00\x00\x00\x12q\xa9\xe3\xe8*\xc3L\xb9\xd4\x9eOn$\xdc'
            b'\xadp\x1b\x1e\n\xe0"\xa6\xff%')))
