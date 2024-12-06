import collections
import re
from email.policy import default

# initialize
a = []
b = []
#read
with open("input/4.txt") as f:
    lines = f.readlines()
#parse
bigstr = ""
xmas = "XMAS"
origin_tuples = []
puzzle = []
for idy, line in enumerate(lines):
    row = []
    for idx, char in enumerate(line):
        row.append(char)
        if char == "X":
            origin_tuples.append((idy, idx))
    x_len = len(row)
    puzzle.append(row)
y_len = len(puzzle)
sum = 0
modifications = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]

def apply_mod(tuple, mod):
    return tuple[0] + mod[0], tuple[1] + mod[1]

for start in origin_tuples:
    for mod in modifications:
        xmas_idx = 1
        y = start[0]
        x = start[1]
        while xmas_idx < 4: # oboe on max?
            y, x = apply_mod((y, x), mod)
            if x >= x_len or y >= y_len or x < 0 or y < 0:
                break
            if puzzle[y][x] != xmas[xmas_idx]:
                break
            else:
                xmas_idx += 1
        if xmas_idx > 3:
            sum += 1
print(sum)