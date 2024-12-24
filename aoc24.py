import functools
from collections import defaultdict
import sys

from parse import parse

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
with open("input/24.txt") as f:
    in_a, in_b = f.read().split("\n\n")
in_list = []
map = defaultdict(list)
a = in_a.splitlines()
b = in_b.splitlines()
# process
# answer


defined = {}
for a_e in a:
    nums = a_e.split(": ")
    defined[nums[0]] = int(nums[1])

for i in range(313):
    for b_x in b:
        nums = []
        vals = parse("{0} {1} {2} -> {3}", b_x.strip())
        for val in vals.fixed:
            nums.append(val)
        if nums[0] in defined and nums[2] in defined:
            if nums[1] == "XOR":
                defined[nums[3]] = defined[nums[0]] ^ defined[nums[2]]
            if nums[1] == "OR":
                defined[nums[3]] = defined[nums[0]] | defined[nums[2]]
            if nums[1] == "AND":
                defined[nums[3]] = defined[nums[0]] & defined[nums[2]]



ans = ""
for i in range(0,46)[::-1]:
    if i < 10:
        ans += str(defined["z0" + str(i)])
    else:
        ans += str(defined["z" + str(i)])
print(ans)