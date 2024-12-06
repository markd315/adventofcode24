import collections
import re
from copy import copy
from email.policy import default

# initialize
#read
with open("input/6.txt") as f:
    lines = f.readlines()
#parse
puzzle = []
for idy, line in enumerate(lines):
    row = []
    for idx, char in enumerate(line.strip()):
        row.append(char)
        if char == "^":
            y_s = idy
            x_s = idx
    x_len = len(row)
    puzzle.append(row)
y_len = len(puzzle)
modifications = [(1,0),(0,-1),(-1,0),(0,1),]# dlur

def apply_mod(tuple, mod):
    return tuple[0] + mod[0], tuple[1] + mod[1]

def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0

positions = 0
dir_idx = 2
y, x = y_s, x_s

visited = set()
while True:
    mod = modifications[dir_idx]
    t_y, t_x = apply_mod((y, x), mod)
    if range_violated(t_y, t_x):
        break
    elif puzzle[t_y][t_x] == "#":
        dir_idx += 1
        dir_idx %= 4
        continue
    elif (y, x, dir_idx) not in visited:
        visited.add((y, x, dir_idx))
    else:
        break
    y, x = t_y, t_x

positions = 0
poses = set()
visited_first = copy(visited)
for nodes in visited_first: # only disturb the test pat
    y_obj = nodes[0]
    x_obj = nodes[1]
    y, x = y_s, x_s
    dir_idx = 2
    visited = set()
    while True:
        mod = modifications[dir_idx]
        t_y, t_x = apply_mod((y, x), mod)
        if range_violated(t_y, t_x):
            break
        elif puzzle[t_y][t_x] == "#":
            dir_idx += 1
            dir_idx %= 4
            continue
        elif t_y == y_obj and t_x == x_obj:
            dir_idx += 1
            dir_idx %= 4
            continue
        elif (y, x, dir_idx) not in visited:
            visited.add((y, x, dir_idx))
        else: # loop detect
            positions += 1
            poses.add((y_obj, x_obj))
            break
        y, x = t_y, t_x
print(len(poses))