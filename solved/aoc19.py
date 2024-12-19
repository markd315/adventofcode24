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


# initialize
a = []
b = []
# read
with open("../input/19.txt") as f:
    lines = f.readlines()
# parse (two stage)
stage_two_parse = False
in_list = []
map = defaultdict(list)
for line in lines:
    if line.strip() == "":
        stage_two_parse = True
        continue
    if not stage_two_parse:
        x = line.strip().split(",")
        for ax in x:
            a.append(ax.strip())
    else:
        b.append(line.strip())
# process
# answer

@functools.cache
def isInList(remainder):
    if remainder == "":
        return 1
    else:
        count = 0
        for towel in a:
            if remainder.startswith(towel):
                count += isInList(remainder[len(towel):])
        return count

ans = 0
for book in b:
    if isInList(book):
        ans += 1
print(ans)