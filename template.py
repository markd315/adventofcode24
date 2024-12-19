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
with open("input/X.txt") as f:
    in_a, in_b = f.read().split("\n\n")
in_list = []
map = defaultdict(list)
a = in_a.split(", ")
b = in_b.splitlines()
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
    ans += isInList(book)
print(ans)