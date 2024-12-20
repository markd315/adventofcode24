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

with open("input/20.txt") as f:
    lines = f.readlines()
# parse (two stage)
in_list = []
FIRST_N_LINES = 1024

for idy, line in enumerate(lines):
    vals = []
    for idx, num in enumerate(line.strip()):
        if num == "S":
            r_y = idy
            r_x = idx
        if num == "E":
            e_y = idy
            e_x = idx
        if num == "#":
            for d in [SOUTH, EAST]:
                loc = T((idy, idx))
                nl =  loc + d
                c1 = (nl, loc)
                c2 = (loc, nl)
                cheats.add(c1)
                cheats.add(c2)
        vals.append(num)
    x_len = len(line.strip())
    y_len = len(lines)
    in_list.append(vals)
# process
# answer

ans = 0

def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0

def run_maze(baseline=False):
    scores = defaultdict(int)  # (y, x) -> int score
    paths = defaultdict(set)  # ()
    dir = {}
    scores[T((r_y, r_x))] = 0
    paths[T((r_y, r_x))] = set()
    dir[T((r_y, r_x))] = EAST
    queue = collections.deque()
    queue.append(T((r_y, r_x)))
    visited = set()
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
                    visited.add(T((y, x)))
    if baseline:
        return scores
    return scores[T((e_y, e_x))]

def run_cheat(cheat, scores):
    ls = 99999999
    for entry_dir in modifications:
        entry_loc = cheat[0] + entry_dir
        y, x = entry_loc
        if range_violated(y, x) or in_list[y][x] == "#":
            continue
        for dir in modifications:
            if dir == entry_dir: # no turning around
                continue
            exit_loc = cheat[1] + dir
            y, x = exit_loc
            if not range_violated(y, x) and in_list[y][x] != "#":
                test_score = scores[entry_loc] + from_end[exit_loc] + 3
                if test_score < ls:
                    ls = test_score
    return baseline - ls if ls != 99999999 else 0

saved = {}
scores = run_maze(True)
#res = run_maze({T((8, 8)), T((9, 8))})
#res = run_maze({T((7, 8)), T((7, 6))})
baseline = scores[T((e_y, e_x))]

from_end = {}
for k in scores.keys():
    from_end[k] = baseline - scores[k]

for cheat in cheats:
    ans += 1 if run_cheat(cheat, scores) >= 8 else 0
#print(saved)
print(ans)