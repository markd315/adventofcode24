from collections import defaultdict
from parse import *

with open("../input/14.txt") as f:
    lines = f.readlines()
# parse (two stage)
in_list = []
map = defaultdict(list)
for line in lines:
    vals = []
    nums = parse("p={:d},{:d} v={:d},{:d}", line.strip())
    for num in nums:
        vals.append(num)
    in_list.append(vals)
# process
# answer
ans = 1
y_s = 103 #7
x_s = 101 #11
for i in range(1, 100000):
    poses = set()
    unique = True
    for idy, book in enumerate(in_list):
        book[0] += book[2]
        book[0] %= x_s
        book[1] += book[3]
        book[1] %= y_s
        if (book[0], book[1]) not in poses:
            poses.add((book[0], book[1]))
        else:
            unique = False
    if unique:
        print("unique after second" + str(i))