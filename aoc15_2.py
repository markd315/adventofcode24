import functools
from collections import defaultdict

# initialize
a = []
b = []
#read
with open("input/15.txt") as f:
    lines = f.readlines()
#parse (two stage)
stage_two_parse = False
in_list = []
map = defaultdict(list)
for idy, line in enumerate(lines):
    if line.strip() == "":
        stage_two_parse = True
        continue
    if not stage_two_parse:
        tmp = []
        for idx, char in enumerate(line.strip()):
            if char == "@":
                r_x = idx * 2
                r_y = idy
                tmp.append(".")
                tmp.append(".")
            elif char == "O":
                tmp.append("[")
                tmp.append("]")
            else:
                tmp.append(char)
                tmp.append(char)
        a.append(tmp)
        x_len = len(tmp)
        y_len = len(a)
    else:
        for char in line.strip():
            b.append(char)
#process
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
mods = {
    "^": NORTH,
    "v": SOUTH,
    "<": WEST,
    ">": EAST
}

def apply_mod(tuple, mod):
    return tuple[0] + mod[0], tuple[1] + mod[1]
def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0
#answer

def rec_boxes(force, boxes, loc):
    yw, xw = loc
    if a[yw][xw] in "[]":
        boxes.add((yw, xw, a[yw][xw]))
    if a[yw][xw] == "[":
        boxes.add((yw, xw + 1, "]"))
    if a[yw][xw] == "]":
        boxes.add((yw, xw - 1, "["))
    newloc = force + loc
    yw, xw = loc
    if a[yw][xw] == "#":
        return True, boxes
    if a[yw][xw] == ".":
        return False, boxes
    if a[yw][xw] in "[]":
        boxes.add((yw, xw, a[yw][xw]))
    if a[yw][xw] == "[":
        boxes.add((yw, xw + 1, "]"))
        rwall, lboxes = False, set()
        lwall, rboxes = rec_boxes(force, boxes, newloc)
        if mod in [NORTH, SOUTH]:
            rwall, lboxes = rec_boxes(force, boxes, newloc + mods[">"])
        return lwall or rwall, rboxes.union(lboxes)
    if a[yw][xw] == "]":
        boxes.add((yw, xw - 1, "["))
        lwall, rboxes = False, set()
        if mod in [NORTH, SOUTH]:
            lwall, rboxes = rec_boxes(force, boxes, newloc + mods["<"])
        rwall, lboxes = rec_boxes(force, boxes, newloc)
        return lwall or rwall, rboxes.union(lboxes)

ans = 0
for instr in b:
    mod = mods[instr]
    y, x = mod + T((r_y, r_x))
    if range_violated(y, x):
        continue
    if a[y][x] == ".":
        r_y, r_x = y, x
    elif a[y][x] == "#":
        continue
    else: # box
        yw, xw = T((r_y, r_x)) + mod
        loc = T((yw, xw))
        wall, boxes = rec_boxes(mod, set(), loc)
        if wall:
            continue
        else: # pushed into a blank space. robot moves up one. blank space is O
            new_boxes = set()
            for box in boxes:
                yw, xw = T((box[0], box[1])) + mod
                a[yw][xw] = box[2] # char from tuple
                box = T((yw, xw))
                new_boxes.add(box)
            # blank out space below boxes
            if mod in [NORTH, SOUTH]:
                for box in new_boxes:
                    yw, xw = T((box[0], box[1])) + mod.rot().rot()  # subtract
                    found = False
                    for box in new_boxes:
                        if box[0] == yw and box[1] == xw:
                            found = True
                    if not found:
                        a[yw][xw] = "."
            else:
                r_y, r_x = y, x
                curr_char = a[r_y][r_x]
                a[r_y][r_x] = "."
            # when pushing vertical also clear other pair


for idy, line in enumerate(a):
    for idx, char in enumerate(line):
        if char == "[":
            ans += 100*idy + idx
print(ans)