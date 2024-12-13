import collections
import re
from email.policy import default

# initialize
a = []
b = []
#read
with open("../input/6.txt") as f:
    lines = f.readlines()
#parse
puzzle = []
for idy, line in enumerate(lines):
    row = []
    for idx, char in enumerate(line):
        row.append(char)
        if char == "^":
            y_s = idy
            x_s = idx
    x_len = len(row)
    puzzle.append(row)
y_len = len(puzzle)
class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot(self):
        x, y = self
        return T((y, -x))
NORTH = T((-1, 0))
EAST = NORTH.rot()
SOUTH = EAST.rot()
WEST = SOUTH.rot()
modifications = [SOUTH,WEST,NORTH,EAST]

def apply_mod(tuple, mod):
    return tuple[0] + mod[0], tuple[1] + mod[1]

def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0

moves = 0
dir_idx = 2
y, x = y_s, x_s
visited = set()
while True:
    mod = modifications[dir_idx]
    t_y, t_x = apply_mod((y, x), mod)
    if range_violated(y, x):
        print(moves)
        break
    elif puzzle[t_y][t_x] == "#":
        dir_idx += 1
        dir_idx %= 4
        continue
    elif (y, x) not in visited:
        visited.add((y, x))
        moves += 1
    y, x = t_y, t_x