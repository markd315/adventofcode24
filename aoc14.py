import functools
from collections import defaultdict

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
#read
with open("input/14.txt") as f:
    lines = f.readlines()
#parse (two stage)
stage_two_parse = False
in_list = []
map = defaultdict(list)
for line in lines:
    if line.strip() == "":
        stage_two_parse = True
        continue
    if not stage_two_parse:
        x = line.split("|")
        a_x = int(x[0])
        b_x = int(x[1].strip())
        map[a_x].append(b_x)
    else:
        nums = []
        for n in line.strip().split(","):
            nums.append(int(n))
        in_list.append(nums)
#process
#answer
ans = 0
sorted(in_list, key=functools.cmp_to_key(comparator), reverse=True)
for book in in_list:
    