#!/usr/bin/env python

def reverse_range(l, i, length):
    if length > len(l):
        return l
    if i + length < len(l):
        r = l[i:i+length]
        r.reverse()
        return l[0:i] + r + l[i+length:]
    else:
        overflow = i + length - len(l)
        r = l[i:] + l[0:overflow]
        r.reverse()
        to_return = r[len(r) - overflow:] + l[overflow:i] + r[0:len(r) - overflow]
        return to_return
       

def knot_hash(s):
    sparse = range(256)

    lengths = [ord(x) for x in list(s)] + [17, 31, 73, 47, 23]

    cur_pos = 0
    skip_size = 0


    for i in range(64):
        for length in lengths:
            sparse = reverse_range(sparse, cur_pos, length)
            cur_pos = (cur_pos + length + skip_size) % len(sparse)
            skip_size += 1

    dense = []
    for i in range(0, len(sparse), 16):
        b = 0
        for j in range(16):
            b = b ^ sparse[i + j]
        dense.append(b)

    return "".join([format(x, '02x') for x in dense])
def count_bits(k):
    i = int(k, 16)
    return (i & 0x1) + ((i & 0x2) >> 1) + ((i & 0x4) >> 2)  + ((i & 0x8) >> 3)
input_str = "ugkiagan"
#input_str = "flqrgnkx"
count = 0
for i in range(128):
    l = knot_hash(input_str + "-" + str(i))
    for j in list(l):
        count = count + count_bits(j)

print count
