import functools
from collections import defaultdict

from parse import parse


def comparator(inp, two):
    if inp in map.keys():
        if two in map[inp]:
            return -1
    if two in map.keys():
        if inp in map[two]:
            return 1
    return 0

# initialize
a = []
b = []
#read
with open("input/17.txt") as f:
    lines = f.readlines()
#parse (two stage)
stage_two_parse = False
in_list = []
map = defaultdict(list)
registers = []
opcodes = []
for line in lines:
    if line.strip() == "":
        stage_two_parse = True
        continue
    if not stage_two_parse:
        nums = parse("Register {}: {:d}", line.strip())
        registers.append(nums[1])
    else:
        ops = parse("Program: {}", line.strip())
        ops = ops[0].split(",")
        for op in ops:
            opcodes.append(int(op))
#process
idx = 0

def comboOp(c):
    if c < 4:
        return c
    if c < 7:
        return registers[c-4]
    else:
        raise "ok"

output = [2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0]

a_lsbs = ""

b = 0
c = 0
for i in range(0,16):
    expected = output[i]
    for b in range(0,8):
        # b = A % 8 (LSBS)
        b = b ^ 3
        command = str(a) + "bits shifted by " + str(b)
        b = b ^ int(a / pow(2,b))
        # the division result will be A, bit shifted by 0-7 digits.
        # specifically, it will be
        # 001
        b = b ^ 5

        # B's bits will look like:
        # (we only care about the last 3)
        # [notb, notb, b]  XOR some next digits of A
        # we dont care about MSB of A either
        # xor is commutative
        #a = int(a / pow(2,3)) #03 opcode to shift bits
        #output  # 55 see below
        if b % 8 == expected:
            a_lsbs = str(a) + " " + a_lsbs
            print(command)

print(a_lsbs) # prints 6 5 2 2 4 5 6 2 7 2 1 5 7 4   answer in ternary binary chunks
#110 101 010 010 100 101 110 010 111 010 001 101 111 100
# = 266934515582600
# apparently this is wrong
# actually prints 7,3,1,6,5,4,1,5,7,3,1,6,4,4,2,1

# how about 3 0 6 6 1 7 0 3 6 2 6 4 0 2 7 1
# 011 000 110 110 001 111 000 011 100 010 110 100 000 010 111 011

# 2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0
# b = A % 8
# b = B xor 3
#75 c = A / 2^B
#15 b = b xor 5
#03 a = int(a / pow(2,3))
#42 b = b xor c
#55 output(b % 8)
#30 LOOP number of times that A can be divided by 8 before being floor to 0.


# we need 16 loops to even output 16 numbers so start a at 2^45
#LSBs from A are used at each loop for B
# b = 3 LSB from A xor 011
#75 C = A / 2^B
#15 B = B xor 5
#42 B = C xor C
#55 output(b % 8)
#03 a = int(a / 8) (next 3 bits basically to reset loop)
# LOOP x 16