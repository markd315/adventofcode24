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
with open("input/21.txt") as f:
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
@cache
def dgrid_orders(y, x, cy, cx, cursor_dest):
    if cursor_dest in "udlra":
        if cursor_dest in "ua" and cy == 1 and cx == 0:
            return "r" * x + "u" * (-y)
        if cursor_dest  == "l" and cy == 0 and cx > 0:
            return "d" * y + "l" * (-x)
    else: # NCURSOR
        if cursor_dest in "741" and y < 0 and x < 0 and cy == 3:  # avoid blank spaces
            return "u" * (-y) + "l" * (-x)
        if cursor_dest  in "0A" and y > 0 and x > 0 and cx == 0:
            return "r" * x + "d" * y
    if y < 0 and x < 0: return "l" * (-x) + "u" * (-y) #prefer "<^" over "^<"
    if y < 0 < x: return "u" * (-y) + "r" * x  #prefer "^>" over ">^"
    if y > 0 > x: return "l" * (-x) + "d" * y  # prefer "<v" over "v<"
    if y > 0 and x > 0: return "d" * y + "r" * x  # prefer "v>" over ">v"
    if x == 0:
        if y > 0:
            return "d" * y
        else:
            return "u" * (-y)
    else: # y == 0
        if x > 0:
            return "r" * x
        else:
            return "l" * (-x)

@cache
def find_in_grid(grid, target):
    for row_index, row in enumerate(grid):
        if target in row:
            col_index = row.index(target)
            return T((row_index, col_index))

@cache
def p_dir(cursor_target, cy, cx):
    target = find_in_grid(d_grid, cursor_target)
    diff = target - T((cy, cx))
    y, x = diff
    steps = list(dgrid_orders(y, x, cy, cx, cursor_target))
    steps.append('a')
    return steps, target

@cache
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
        for i in range(0,25):
            if steps_next is not None:
                steps = steps_next
            steps_next = []
            for dir1 in steps:
                steps, cursors[i] = p_dir(dir1, cursors[i][0], cursors[i][1])
                steps_next.extend(steps)
        count += len(steps_next)
    return count

for book in b:
    book = book.strip()
    c = int(book[0:3])
    count = press(book)
    complexity = c * count
    ans += complexity
print(ans)