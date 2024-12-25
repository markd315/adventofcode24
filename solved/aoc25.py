import functools
from collections import defaultdict
import sys
sys.setrecursionlimit(999999)

def comparator(inp, two):
    if inp in map.keys():
        if two in map[inp]:
            return -1
    if two in map.keys():
        if inp in map[two]:
            return 1
    return 0


# read
with open("../input/25.txt") as f:
    blocks = f.read().split("\n\n")
in_list = []
map = defaultdict(list)

locks =[]
keys = []

def height(lk, type):
    heights = []
    for i in range(5):
        if type == "L":
            for j in range(7):
                if lk[j][i] == ".":
                    heights.append(j-1)
                    break
        else:
            for j in range(7):
                if lk[6-j][i] == ".":
                    heights.append(j-1)
                    break
    return heights


for block in blocks:
    lines = block.splitlines()
    if lines[0].strip() == "#####":
        locks.append(height(lines, "L"))
    else:
        keys.append(height(lines, "K"))

# process
# answer

def compat(lock, key):
    for i in range(5):
        if 5 < key[i] + lock[i]:
            return False
    return True

ans = 0
for lock in locks:
    for key in keys:
        if compat(lock, key):
            ans += 1
print(ans)