import collections
from collections import defaultdict
from copy import copy


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

with open("input/16.txt") as f:
    lines = f.readlines()
# parse (two stage)
in_list = []
r_y, r_x = 0, 0
scores = defaultdict(lambda: float('inf')) # (y, x) -> int score
paths = defaultdict(list) # dict: T(y, x) -> [{},{}]
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

scores[T((r_y, r_x, EAST))] = 0
paths[T((r_y, r_x))] = [{T((r_y, r_x))}] #todo array of set for p2
frz = frozenset({T((r_y, r_x))})
facing = {frz: EAST} # dict: path -> dir
queue = collections.deque()
queue.append(T((r_y, r_x)))
best_paths = []
visited = set()
while len(queue) > 0:
    elem = queue.popleft()
    for path in paths[elem]:
        t_dir = facing[frozenset(path)]
        for dirs in [t_dir, t_dir.rot(), t_dir.rot().rot().rot()]:
            old_score = scores[(elem[0], elem[1], t_dir)]
            new_loc = elem + dirs
            y, x = new_loc[0], new_loc[1]
            #if (y, x, dirs) not in visited:
            #    visited.add((y, x, dirs))
            #else:
            #    continue
            if in_list[y][x] == "#":
                continue
            score = old_score
            score += 1 if dirs == t_dir else 1001
            if score >= scores[(y, x, dirs)]:
                continue
            if frz in paths[new_loc]:  # short circuit cycles
                continue
            curr_path = copy(path)
            curr_path.add(new_loc)
            frz = frozenset(curr_path)
            if score <= scores[(y, x, t_dir)]:
                if y == 7 and x == 15: # todo
                    # junction is wrong because to GET to 7,15 is cheaper from the left but to PROGRESS from there is same
                    print("break")
                    # [score for score in scores if score[1] == 15 and score[0] == 7]
                    # scores[[score for score in scores if score[1] == 15 and score[0] == 7][0]]
                if score < scores[(y,x, dirs)]:
                    paths[new_loc] = [curr_path]
                    scores[(y, x, dirs)] = score
                else:
                    paths[new_loc].append(curr_path)
                queue.append(new_loc)
                facing[frz] = dirs

ans = scores[T((e_y, e_x))]
total_set = set()
for path in paths[T((e_y, e_x))]:
    for elem in path:
        total_set.add(elem)
print(len(total_set))
for y, line in enumerate(in_list):
    out = ""
    for x, char in enumerate(line):
        if T((y, x)) in total_set:
            out += "0"
        else:
            out += char
    print(out)
#print(ans)