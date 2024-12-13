import functools
from collections import defaultdict
from copy import copy


def evaluate(equals, in_list):
    if len(in_list) == 2:
        return in_list[0] * in_list[1] == equals or in_list[0] + in_list[1] == equals
    mult = copy(in_list)
    mult[1] *= mult[0]
    in_list[1] += in_list[0]
    return evaluate(equals, mult[1:]) or evaluate(equals, in_list[1:])

# initialize
in_list = []
# read
with open("../input/7.txt") as f:
    lines = f.readlines()
for line in lines:
    nums = []
    for n in line.strip().split(" "):
        nums.append(int(n.replace(":", "")))
    in_list.append(nums)
# process
# answer
ans = 0
for book in in_list:
    equals = book[0]
    ans = ans + equals if evaluate(equals, book[1:]) else ans
print(ans)