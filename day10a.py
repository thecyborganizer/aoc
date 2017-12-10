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
       

nums = range(256)
#nums=range(5)

cur_pos = 0
skip_size = 0
lengths = [int(x) for x in ('106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118').split(',')]
#lengths = [int(x) for x in ('3, 4, 1, 5').split(',')]

for length in lengths:
    nums = reverse_range(nums, cur_pos, length)
    cur_pos = (cur_pos + length + skip_size) % len(nums)
    skip_size += 1

#print nums
#print len(nums)
print nums[0] * nums[1]
