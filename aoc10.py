import collections
import re
from email.policy import default

# initialize
a = []
b = []
#read
with open("input/10.txt") as f:
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
modifications = [(1,0),(0,-1),(-1,0),(0,1),]# dlur

def apply_mod(tuple, mod):
    return tuple[0] + mod[0], tuple[1] + mod[1]

def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0

def dfs(origin, modifications, count):
    trails = 0
    for mod in modifications:
        y, x = (origin[0] + mod[0], origin[1] + mod[1])
        if not range_violated(y, x):
            char = puzzle[y][x]
            if char != "." and int(char) == count:
                if count == 9 and (y,x) not in found:
                    found.add((y,x))
                    trails += 1
                else:
                    trails += dfs((y,x), modifications, count + 1)
    return trails

moves = 0
dir_idx = 2
y, x = y_s, x_s
visited = set()
ans = 0
for origin in origins:
    found = set()
    score = dfs(origin, modifications, 1)
    #print(score)
    ans += score
print(ans)