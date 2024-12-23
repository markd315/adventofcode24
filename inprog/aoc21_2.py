from functools import cache
from collections import defaultdict
import sys
sys.setrecursionlimit(999999)

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


# read
with open("../input/21.txt") as f:
    b = f.read().splitlines()
# process
# answer

ans = 0
f_grid = tuple([
    tuple(['7', '8', '9']),
    tuple(['4', '5', '6']),
    tuple(['1', '2', '3']),
    tuple(['e', '0', 'A']),
])
d_grid = tuple([
    tuple(['e', 'u', 'a']),
    tuple(['l', 'd', 'r'])
])

state_transitions = {
    "a": [],
    "ll": [],
    "rr": [],
    "dd": [],
    "uu": [],
    "aa": [],
    "al": ["ar", "rd", "dl"], #(a) dlla
    "ar": ["ar"],
    "au": ["au"],
    "ad": ["au", "ud"],
    "dr": ["dr"],
    "dl": ["dl"],
    "da": ["du", "ua"],
    "ra": ["ra"],
    "rd": ["rd"],
    "ru": ["rd", "du"],
    "la": ["ld", "dr", "ra"],
    "ld": ["ld"],
    "lu": ["ld", "du"],
    "ua": ["ua"],
    "ul": ["ud", "dl"],
    "ur": ["ud", "dr"],
    "du": ["du"],
    "ud": ["ud"],
    "lr": ["ld", "dr"],
    "rl": ["rd", "dl"],
}

trx_count = defaultdict(lambda:0)

dgrid_cache = defaultdict(lambda: None)
def dgrid_orders(y, x, cy, cx, cursor_dest):
    if dgrid_cache[(y, x, cy, cx, cursor_dest)]:
        return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    if cursor_dest in "udlra":
        if cursor_dest in "ua" and cy == 1 and cx == 0:
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "r" * x + "u" * (-y)
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]
        if cursor_dest  == "l" and cy == 0 and cx > 0:
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "d" * y + "l" * (-x)
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    else: # NCURSOR
        if cursor_dest in "741" and y < 0 and x < 0 and cy == 3:  # avoid blank spaces
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "u" * (-y) + "l" * (-x)
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]
        if cursor_dest  in "0A" and y > 0 and x > 0 and cx == 0:
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "r" * x + "d" * y
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    if y < 0 and x < 0:
        dgrid_cache[(y, x, cy, cx, cursor_dest)] = "l" * (-x) + "u" * (-y) #prefer "<^" over "^<"
        return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    if y < 0 < x:
        dgrid_cache[(y, x, cy, cx, cursor_dest)] = "u" * (-y) + "r" * x  #prefer "^>" over ">^"
        return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    if y > 0 > x:
        dgrid_cache[(y, x, cy, cx, cursor_dest)] ="l" * (-x) + "d" * y  # prefer "<v" over "v<"
        return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    if y > 0 and x > 0:
        dgrid_cache[(y, x, cy, cx, cursor_dest)] = "d" * y + "r" * x  # prefer "v>" over ">v"
        return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    if x == 0:
        if y > 0:
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "d" * y
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]
        else:
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "u" * (-y)
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]
    else: # y == 0
        if x > 0:
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "r" * x
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]
        else:
            dgrid_cache[(y, x, cy, cx, cursor_dest)] = "l" * (-x)
            return dgrid_cache[(y, x, cy, cx, cursor_dest)]

grid_cache = defaultdict(lambda: None)
def find_in_grid(grid, target):
    if grid_cache[(grid, target)] is not None:
        return grid_cache[grid, target]
    for row_index, row in enumerate(grid):
        if target in row:
            col_index = row.index(target)
            grid_cache[grid, target] = T((row_index, col_index))
            return grid_cache[grid, target]

pdir_cache = defaultdict(lambda: None)
def p_dir(cursor_target, cy, cx):
    target = find_in_grid(d_grid, cursor_target)
    diff = target - T((cy, cx))
    y, x = diff
    steps = list(dgrid_orders(y, x, cy, cx, cursor_target))
    steps.append('a')
    pdir_cache[(cursor_target, cy, cx)] = (steps, target)
    return pdir_cache[(cursor_target, cy, cx)]


def p_num(numerical, n_cursor):
    target = find_in_grid(f_grid, numerical)
    diff =  target - n_cursor
    y, x = diff
    steps = list(dgrid_orders(y, x, n_cursor[0], n_cursor[1], numerical))
    steps.append("a")
    return steps, target

def press(book):
    count = 0
    n_cursor = T((3, 2))
    for numerical in book:
        cursors = defaultdict(lambda: T((0, 2)))
        steps, n_cursor = p_num(numerical, n_cursor)
        steps_next = None
        for i in range(0,1):
            if steps_next is not None:
                steps = steps_next
            steps_next = []
            for dir1 in steps:
                steps, cursors[i] = p_dir(dir1, cursors[i][0], cursors[i][1])
                steps_next.extend(steps)
        all_steps = ['a']
        all_steps.extend(steps_next) # start at a
        trx_count = defaultdict(lambda: 0)
        for idx, elem in enumerate(all_steps[0:-1]):
            joined = elem + all_steps[idx+1]
            trx_count[joined] += 1
        for i in range(0,3): # Switch to memo solution
            next_trx_count = defaultdict(lambda: 0)
            for k, cnt in trx_count.items():
                trans = state_transitions[k]
                #trans.append("a")
                for elem in trans:
                    next_trx_count[elem] += cnt
            #a_presses = sum(next_trx_count.values())
            #next_trx_count['a'] = a_presses
            trx_count = next_trx_count
        trx_count['a'] = sum(trx_count.values())
        return trx_count['a']

for book in b:
    book = book.strip()
    c = int(book[0:3])
    count = press(book)
    complexity = c * count
    ans += complexity
print(ans)