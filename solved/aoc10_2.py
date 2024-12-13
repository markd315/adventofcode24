import collections
import re
from email.policy import default

# initialize
a = []
b = []
#read
with open("../input/10.txt") as f:
    lines = f.readlines()
#parse
puzzle = []
origins = []
for idy, line in enumerate(lines):
    row = []
    for idx, char in enumerate(line):
        row.append(char)
        if char == "0":
            y_s = idy
            x_s = idx
            origins.append((y_s, x_s))
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

def dfs(origin, modifications, count, path):
    trails = 0
    for idx, mod in enumerate(modifications):
        y, x = (origin[0] + mod[0], origin[1] + mod[1])
        if not range_violated(y, x):
            char = puzzle[y][x]
            if char != "." and int(char) == count:
                if count == 9:# and (y,x) not in paths:
                    #paths.add(path)
                    trails += 1
                else:
                    path.append(mod)
                    trails += dfs((y,x), modifications, count + 1, path)
    return trails

moves = 0
dir_idx = 2
y, x = y_s, x_s
visited = set()
ans = 0
for origin in origins:
    paths = set()
    score = dfs(origin, modifications, 1, [])
    #print(score)
    ans += score
print(ans)