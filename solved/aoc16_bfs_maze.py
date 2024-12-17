import collections
from collections import defaultdict
from parse import *

class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot(self):
        x, y = self
        return T((y, -x))

NORTH = T((-1, 0))
EAST = NORTH.rot()
SOUTH = EAST.rot()
WEST = SOUTH.rot()
modifications = [SOUTH,WEST,NORTH,EAST]

with open("../input/16.txt") as f:
    lines = f.readlines()
# parse (two stage)
in_list = []
r_y, r_x = 0, 0
scores = defaultdict(int) # (y, x) -> int score
paths = defaultdict(set) # ()
dir = {}
for idy, line in enumerate(lines):
    vals = []
    for idx, num in enumerate(line.strip()):
        if num == "S":
            r_y = idy
            r_x = idx
        if num == "E":
            e_y = idy
            e_x = idx
        vals.append(num)
    in_list.append(vals)
# process
# answer

ans = 0

scores[T((r_y, r_x))] = 0
paths[T((r_y, r_x))] = set()
dir[T((r_y, r_x))] = EAST
queue = collections.deque()
queue.append(T((r_y, r_x)))
while len(queue) > 0:
    elem = queue.popleft()
    t_dir = dir[elem]
    old_score = scores[elem]
    for dirs in [t_dir, t_dir.rot(), t_dir.rot().rot().rot()]:
        addl_score = 1 if dirs == t_dir else 1001
        new_loc = elem + dirs
        y, x = new_loc[0], new_loc[1]
        if in_list[y][x] != "#" and T((y, x)) not in paths[new_loc]:
            score = old_score + addl_score
            if scores[T((y, x))] == 0 or score < scores[T((y, x))]:
                scores[T((y, x))] = score
                paths[new_loc] |= set(elem)
                dir[new_loc] = dirs
                queue.append(new_loc)

ans = scores[T((e_y, e_x))]
print(ans)