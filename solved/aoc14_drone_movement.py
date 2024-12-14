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
for i in range(0, 100):
    for idy, book in enumerate(in_list):
        book[0] += book[2]
        book[0] %= x_s
        book[1] += book[3]
        book[1] %= y_s
quads = defaultdict(int)
for idy, book in enumerate(in_list):
    quad = ""
    if book[1] >= (int(y_s/2) + 1):
        quad += "s"
    elif book[1] < (int(y_s/2)):
        quad += "n"
    if book[0] >= (int(x_s/2) + 1):
        quad += "e"
    elif book[0] < (int(x_s / 2)):
        quad += "w"
    if len(quad) == 2:
        quads[quad] += 1
for k in quads.keys():
    ans *= quads[k]
print(ans)