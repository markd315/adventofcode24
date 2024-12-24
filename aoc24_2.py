import functools
from collections import defaultdict
import sys

from parse import parse
# read
with open("input/24.txt") as f:
    in_a, in_b = f.read().split("\n\n")
in_list = []
map = defaultdict(list)
a = in_a.splitlines()
b = in_b.splitlines()
# process
# answer

# x44 y44 max 44 bit number
for x in range(0 : 17592186044415):
    for y in range(0: 17592186044415):
        for i in range(313):
            for b_x in b:
                nums = []
                vals = parse("{0} {1} {2} -> {3}", b_x.strip())
                for val in vals.fixed:
                    nums.append(val)
                if nums[3].startswith("z"):

                if nums[3] not in defined and nums[0] in defined and nums[2] in defined:
                    if nums[1] == "XOR":
                        result =
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