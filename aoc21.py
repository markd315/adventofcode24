import functools
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
f_grid = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['e', '0', 'A'],
]
d_grid = [
    ['e', 'u', 'a'],
    ['l', 'd', 'r']
]
dgrid_orders = {
    None: "rdlu",
    T((0, 1)): "udlr",
    T((0,2)): "urdl",
    T((1,0)): "ldur",
    T((1,1)): "dlru",
    T((1,2)): "rdul",
}

def find_in_grid(grid, target):
    for row_index, row in enumerate(grid):
        if target in row:
            col_index = row.index(target)
            return T((row_index, col_index))

def p_dir(dir1, in_cursor, next_cursor):
    target = find_in_grid(d_grid, dir1)
    diff = target - in_cursor
    y, x = diff
    orders = [dgrid_orders[next_cursor]]
    if y > 0 and x > 0:
        orders = ["dr", "rd"]
    if x < 0 and y < 0:
        orders = ["lu", "ul"]
    if y > 0 and x < 0:
        orders = ["dl", "ld"]
    if y < 0 and x > 0:
        orders = ["ur", "ru"]
    if dir1 in "ua" and in_cursor == T((1,0)):
        orders = "ru"
    if dir1 == "l" and in_cursor in [T((0,1)),T((0,2))]:
        orders = "dl"
    steps = resolve_ops(orders, y, x)
    for seq in steps:
        seq.append('a')
    return steps, target

def resolve_ops(orders, y, x):
    seqs = []
    for ordering in orders:
        steps = []
        for elem in ordering:
            while y > 0 and elem == "d":
                steps.append("d")
                y -= 1
            while y < 0 and elem == "u":
                steps.append("u")
                y += 1
            while x > 0 and elem == "r":
                steps.append("r")
                x -= 1
            while x < 0 and elem == "l":
                steps.append("l")
                x += 1
        seqs.append(steps)
    return seqs

def p_num(numerical, n_cursor, next_cursor):
    target = find_in_grid(f_grid, numerical)
    diff =  target - n_cursor
    y, x = diff
    orders = [dgrid_orders[next_cursor]]
    if y > 0 and x > 0:
        orders = ["dr", "rd"]
    if x < 0 and y < 0:
        orders = ["lu", "ul"]
    if y > 0 and x < 0:
        orders = ["dl", "ld"]
    if y < 0 and x > 0:
        orders = ["ur", "ru"]
    if numerical in "741" and y < 0 and x < 0: # avoid blank spaces
        orders = ["lu"]
    if numerical in "0A" and y > 0 and x > 0:
        orders = ["dr"]
    steps = resolve_ops(orders, y, x)
    for seq in steps:
        seq.append('a')
    return steps, target

def press(book, n_cursor, d1_cursor, d2_cursor):
    count = 0
    for numerical in book:
        steps, n_cursor = p_num(numerical, n_cursor, d1_cursor)
        for dir1 in steps:
            steps2, d1_cursor = p_dir(dir1, d1_cursor, d2_cursor)
            for dir2 in steps2:
                steps3, d2_cursor = p_dir(dir2, d2_cursor, None)
                #for dir3 in steps3:
                    #steps4, d3_cursor = p_dir(dir3, d3_cursor, None)
                count += len(steps3)
    return count, n_cursor, d1_cursor, d2_cursor

n_cursor = T((3, 2))
d1_cursor = T((0, 2))
d2_cursor = T((0, 2))
d3_cursor = T((0, 2))
for book in b:
    book = book.strip()
    c = int(book[0:3])
    if book == "379A":
        print("brk")
    count, n_cursor, d1_cursor, d2_cursor = press(book, n_cursor, d1_cursor, d2_cursor)
    complexity = c * count
    ans += complexity
print(ans)