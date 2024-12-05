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
        if char == "A":
            origin_tuples.append((idy, idx))
    x_len = len(row)
    puzzle.append(row)
y_len = len(puzzle)
sum = 0
modifications = [(-1,-1),(1,1),(1,-1),(-1,1)]
# non-diags (1,0),(-1,0),(0,1),(0,-1),
def apply_mod(tuple, mod):
    return tuple[0] + mod[0], tuple[1] + mod[1]

def gen_star_mods(tuple, mod):
    opposite = (mod[0] * -1, mod[1] * -1)
    adj_y = (-1 * mod[1], mod[0])
    adj_x = (mod[1], -1 * mod[0])
    return [apply_mod(tuple, opposite), apply_mod(tuple, adj_x), apply_mod(tuple, adj_y)]

def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0

for start in origin_tuples:
    for mod in modifications:
        y_s = start[0]
        x_s = start[1]

        y, x = apply_mod((y_s, x_s), mod)
        if range_violated(y,x):
            continue
        if puzzle[y][x] != "M":
            continue
        stars = gen_star_mods((y_s, x_s), mod)
        string = ""
        for coord in stars:
            if range_violated(coord[0], coord[1]):
                break
            string += puzzle[coord[0]][coord[1]]
        if string == "SMS" or string == "SSM":
            sum += 1
print(sum/2)