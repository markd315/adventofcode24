from collections import defaultdict, deque
from itertools import combinations

#read
with open("../input/12.txt") as f:
    lines = f.readlines()
in_list = []
map = defaultdict(list)
for line in lines:
    nums = []
    y_len = len(lines)
    x_len = len(line.strip())
    for n in line.strip():
        nums.append(n)
    in_list.append(nums)
#process
class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))
    def __sub__(self, other):
        return T(x - y for x, y in zip(self, other))

    def rot(self):
        x, y = self
        return T((y, -x))

NORTH = T((-1, 0))
EAST = NORTH.rot()
SOUTH = EAST.rot()
WEST = SOUTH.rot()
modifications = [SOUTH,WEST,NORTH,EAST]
corners = [(SOUTH, WEST), (SOUTH, EAST), (NORTH, WEST), (NORTH, EAST)]

def apply_mod(tuple, mod):
    return tuple[0] + mod[0], tuple[1] + mod[1]

def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0
#answer
ans = 0
queue = deque()
visited = set()
areas = defaultdict(int)
region = []

def proc_queue():
    same_char = in_list[queue[0][0]][queue[0][1]]
    area = 0
    while len(queue) > 0:
        elem = queue.popleft()
        for mod in modifications:
            t_loc = elem + mod
            y, x = t_loc[0], t_loc[1]
            if not range_violated(y, x) and t_loc not in visited:
                char = in_list[y][x]
                if char == same_char:
                    queue.append(t_loc)
                    visited.add(t_loc)
                    area += 1
                    region.add(t_loc)
    return area

def corner(region):
    corner = 0
    calculated = set()
    for elem in region:
        for mods in corners:
            blanks = 0
            for mod in mods:
                t_loc = elem + mod
                y, x = t_loc[0], t_loc[1]
                if range_violated(y, x) or t_loc not in region:
                    blanks += 1
            if blanks == 2:# or blanks ==0: # both NORTH and WEST adj have to be blank for it to be a top-left corner for ex.
                corner += 1
            # OR if its not the corner in BETWEEN two NON blanks (inner corners)
            if blanks == 0:
                t_loc = elem + mods[1] + mods[0]
                y, x = t_loc[0], t_loc[1]
                if range_violated(y, x) or t_loc not in region:
                    corner += 1
    return corner #+ (corner - 4) # every out facing corner needs an in facing pair


for idy, row in enumerate(in_list):
    for idx, elem in enumerate(row):
        #print(in_list[idy][idx])
        region = set()
        if (idy, idx) not in visited:
            queue.append(T((idy, idx)))
            region.add(T((idy, idx)))
            area = proc_queue()
            peri = corner(region)
            if area == 0: # TODO this sucks
                area = 1
            print("%d * %d = %d" % (area, peri, area * peri))
            ans += area * peri
print(ans)