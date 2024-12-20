import collections
import functools
import itertools
from collections import defaultdict

class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def __sub__(self, other):
        return T(x - y for x, y in zip(self, other))
    def rot(self):
        x, y = self
        return T((y, -x))



cheats = set()
NORTH = T((-1, 0))
EAST = NORTH.rot()
SOUTH = EAST.rot()
WEST = SOUTH.rot()
modifications = [SOUTH,WEST,NORTH,EAST]

with open("../input/20.txt") as f:
    lines = f.readlines()
# parse (two stage)
in_list = []
def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0

for idy, line in enumerate(lines):
    vals = []
    for idx, num in enumerate(line.strip()):
        x_len = len(line.strip())
        y_len = len(lines)
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

def run_maze(baseline=False):
    scores = defaultdict(int)  # (y, x) -> int score
    paths = defaultdict(set)  # ()
    dir = {}
    scores[T((r_y, r_x))] = 0
    paths[T((r_y, r_x))] = set()
    dir[T((r_y, r_x))] = EAST
    queue = collections.deque()
    queue.append(T((r_y, r_x)))
    visited = [T((r_y, r_x))]
    while len(queue) > 0:
        elem = queue.popleft()
        old_score = scores[elem]
        for dirs in modifications:
            addl_score = 1
            new_loc = elem + dirs
            y, x = new_loc[0], new_loc[1]
            if T((y, x)) in visited:
                continue
            if range_violated(y, x):
                continue
            if in_list[y][x] != "#":
                score = old_score + addl_score
                if scores[T((y, x))] == 0 or score < scores[T((y, x))]:
                    scores[T((y, x))] = score
                    dir[new_loc] = dirs
                    queue.append(new_loc)
                    visited.append(T((y, x)))
    if baseline:
        return scores, visited

dist_map = defaultdict(lambda:-1)

def run_cheat(cheat):
    in_loc = dist_map[cheat[0]]
    out_loc = dist_map[cheat[1]]
    if in_loc == -1 or out_loc == -1:
        return 0
    return out_loc - cheat[2] - in_loc

saved = {}
scores, visited = run_maze(True)

baseline = scores[T((e_y, e_x))]

#res = run_cheat((T((7, 8)), T((9, 8)), 2), visited)
#res = run_cheat((T((7, 7)), T((7, 5)), 2), visited)
#res = run_cheat((T((3, 1)), T((7, 3)), 6), visited)

def manhattan_set(elem, dist):
    ret = set()
    for y in range(-dist, dist+1):
        t = abs(y)
        t = dist - t
        for x in range(-t,t+1):
            ret.add(elem + T((y, x)))
    return ret

def manhattan_dist(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1])

cheats = set()
cheats_len = 20
for dist, elem in enumerate(visited):
    loc = elem
    dist_map[elem] = dist
    for opt in manhattan_set(elem, cheats_len):
        cheat = (elem, opt, manhattan_dist(elem, opt))
        valid = True
        for c in cheat[0:2]:
            y, x = c
            if range_violated(y, x):
                valid = False
        if valid and in_list[y][x] != "#":
            cheats.add(cheat)
            if cheat[2] > cheats_len:
                print("freeze")

print(len(cheats))
for cheat in cheats:
    saved = run_cheat(cheat)
    if saved >= 100:
        ans += 1
#print(saved)
print(ans)