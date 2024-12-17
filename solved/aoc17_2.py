from collections import defaultdict
from copy import copy

from parse import parse

#read
with open("../input/17.txt") as f:
    lines = f.readlines()
#parse (two stage)
stage_two_parse = False
in_list = []
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

def simulate(a):
    out = []
    XOR1 = 3
    XOR2 = 5 # PROGRAM_CONSTANTS These will vary in different AOC inputs
    # XOR1 comes from 1,3 [2,3]
    # XOR2 comes from 1,5 [6,7]
    while a> 0:
        x = a % 8
        shift_bits = x ^ XOR1
        out.append( (x ^ (XOR2 ^ XOR1)) ^ (a >> shift_bits) %8)
        a //= 8
    return out

# Backtracking function to reconstruct A
def solve(i, curr=0):
    if not i:
        return curr
    for n in range(8):
        c = curr*8 + n
        if simulate(c) == output[i-1:]:
            if ret := solve(i-1, c):
                return ret

# Entry point to find A

# Run the reconstruction
result = solve(len(output))
if result:
    print(f"Reconstructed A: {result} ({hex(result)})")
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