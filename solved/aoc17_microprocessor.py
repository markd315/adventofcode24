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
with open("../input/17.txt") as f:
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

output = []

while idx < len(opcodes):
    operand = opcodes[idx]
    combo = opcodes[idx+1] if idx + 1 < len(opcodes) else 0
    match operand:
        case 0:
            registers[0] =  int(registers[0] / pow(2,comboOp(combo)))
        case 1:
            registers[1] = registers[1] ^ combo
        case 2:
            registers[1] = comboOp(combo) % 8
        case 3:
            if registers[0] != 0:
                idx = combo
                continue
        case 4:
            registers[1] = registers[1] ^ registers[2]
        case 5:
            output.append(comboOp(combo) % 8)
        case 6:
            registers[1] = int(registers[0] / pow(2, comboOp(combo)))
        case 7:
            registers[2] = int(registers[0] / pow(2, comboOp(combo)))
    idx += 2
#answer
out = ""
for o in output:
    out += str(o) + ","
print(out[:-1])


