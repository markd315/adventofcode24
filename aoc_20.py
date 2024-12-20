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
        if num == "#":
            for d in [SOUTH, EAST]:
                loc = T((idy, idx))
                nl =  loc + d
                c1 = (nl, loc)
                c2 = (loc, nl)
                cheats.add(c1)
                cheats.add(c2)
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
    visited = []
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


noop_mods = modifications
modifications.append(T((0,0)))
def run_cheat(cheat, visited):
    hs = 0
    if cheat[1] not in visited: # must escape on to open space
        return 0

    for entry_dir in modifications:
        entry_loc = cheat[0] + entry_dir
        try:
            in_loc = visited.index(entry_loc)
            out_loc = visited.index(cheat[1])
        except ValueError:
            continue
        if cheat[1] == T((e_y, e_x)):
            test_score = len(visited) - in_loc - 3
        else:
            test_score = out_loc - in_loc - 2
        if test_score > hs:
            hs = test_score
    return hs

saved = {}
scores, visited = run_maze(True)

baseline = scores[T((e_y, e_x))]

res = run_cheat((T((8, 8)), T((9, 8))), visited)
res = run_cheat((T((7, 6)), T((7, 5))), visited)


for cheat in cheats:
    saved = run_cheat(cheat, visited)
    if saved == 6:
        ans += 1
#print(saved)
print(ans)