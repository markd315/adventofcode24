import functools
from collections import defaultdict


def helper(inp, two):
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
with open("input/4.txt") as f:
    lines = f.readlines()
#parse
in_pages = False
pages = []
map = defaultdict(list)
for line in lines:
    if line.strip() == "":
        in_pages = True
        continue
    if not in_pages:
        x = line.split("|")
        a_x = int(x[0])
        b_x = int(x[1].strip())
        map[a_x].append(b_x)
    else:
        nums = []
        for n in line.strip().split(","):
            nums.append(int(n))
        pages.append(nums)
#process
#answer
ans = 0


print(ans)