import collections
from collections import defaultdict


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
modifications = [SOUTH, WEST, NORTH, EAST]

with open("../input/18.txt") as f:
    lines = f.readlines()
# parse (two stage)
in_list = []


def range_violated(y, x):
    return x > e_x or y > e_y or x < 0 or y < 0

blocked = set()

for idy, line in enumerate(lines[0:]):
    ints = line.strip().split(",")
    blocked.add(T((int(ints[1]), int(ints[0]))))
    r_y, r_x = 0, 0
    e_y = 70
    e_x = 70

    scores = defaultdict(int)  # (y, x) -> int score
    paths = defaultdict(set)  # ()
    dir = {}

    scores[T((r_y, r_x))] = 0
    paths[T((r_y, r_x))] = set()
    dir[T((r_y, r_x))] = EAST
    queue = collections.deque()
    queue.append(T((r_y, r_x)))
    visited = set()
    escaped = False
    while len(queue) > 0:
        elem = queue.popleft()
        t_dir = dir[elem]
        old_score = scores[elem]
        for dirs in [t_dir, t_dir.rot(), t_dir.rot().rot().rot()]:
            new_loc = elem + dirs
            if new_loc in blocked or new_loc in visited or range_violated(new_loc[1], new_loc[0]):
                continue
            addl_score = 1
            y, x = new_loc[0], new_loc[1]
            if T((y, x)) not in paths[new_loc]:
                score = old_score + addl_score
                if scores[T((y, x))] == 0 or score < scores[T((y, x))]:
                    scores[T((y, x))] = score
                    visited.add(T((y, x)))
                    dir[new_loc] = dirs
                    queue.append(new_loc)
                if new_loc == T((e_y, e_x)):
                    escaped = True
                    break
        if escaped:
            break

    ans = scores[T((e_y, e_x))]
    if escaped:
        print("escaped " + str(idy))
    else:
        print("NOPE" + ints[0] + " " + ints[1])