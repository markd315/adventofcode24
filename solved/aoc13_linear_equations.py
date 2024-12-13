import functools
import math
from collections import defaultdict

import numpy

with open("../input/13.txt") as f:
    lines = f.readlines()
#parse (two stage)
stage_two_parse = False
in_list = []
prize = []
for line in lines:
    if line.strip() == "":
        in_list.append(prize)
        prize = []
    else:
        parts = line.strip().split(" ")
        x = int(parts[2][2:-1])
        y = int(parts[3][2:])
        prize.append(x)
        prize.append(y)
#process
#answer
ans = 0
for book in in_list:
    print(book)
    # [94, 34, 22, 67, 8400, 5400] x y x y = x y
    # book[0]x + book[2]y = book[4]
    # book[1]x + book[3]y = book[5]
    # book[0]x = [4] - [2]y
    # x = ([4] - [2]y)/[0]
    # book[1](([4] - [2]y)/[0]) + book[3]y = book[5]
    # [4][1]/[0] - [2][1]y/[0] + [3] = [5]
    # [2][1]y/[0] = [4][1]/[0] - [2][1]y/[0] + [3] - [5]
    # 2y = [4]/[2] + [0]([3] - [5])/([2][1])
    A = numpy.array([[book[0], book[2]], [book[1], book[3]]])
    b = numpy.array([book[4], book[5]])
    x = numpy.linalg.solve(A, b)
    y = round(x[1], 3)
    x = round(x[0], 3)
    if int(y) == y and y >= 0:
        if int(x) == x and x >= 0:
            ans += 3* x + y
            print(str(x) + ", " +  str(y))
print(ans)