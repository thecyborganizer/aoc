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
       

sparse = range(256)
input_str = '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118'

lengths = [ord(x) for x in list(input_str)] + [17, 31, 73, 47, 23]

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

print "".join([format(x, '02x') for x in dense])
