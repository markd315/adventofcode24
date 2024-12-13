from collections import defaultdict


def range_violated(y, x):
    return x >= x_len or y >= y_len or x < 0 or y < 0


def calcAntinodes(list, inputantis):
    if len(list) < 2:
        return inputantis
    antis = set()
    origin = list[0]
    y_a = origin[0]
    x_a = origin[1]
    for elem in list[1:]:
        antis.add((origin[0], origin[1]))
        antis.add((elem[0], elem[1]))
        # identify and solve BOTTOM LEFT TOP RIGHT case
        higher_y = max(y_a, elem[0])
        higher_x = max(x_a, elem[1])
        lower_y = min(y_a, elem[0])
        lower_x = min(x_a, elem[1])
        if (y_a > elem[0] and x_a < elem[1]) or (y_a < elem[0] and x_a > elem[1]):
            # BOTTOM LEFT TOP RIGHT
            y_d = higher_y - lower_y
            x_d = higher_x - lower_x
            han = (lower_y - y_d, higher_x + x_d)
            lan = (higher_y + y_d, lower_x - x_d)
            while not range_violated(han[0], han[1]):
                antis.add(han)
                han = (han[0] - y_d, han[1] + x_d)
            while not range_violated(lan[0], lan[1]):
                antis.add(lan)
                lan = (lan[0] + y_d, lan[1] - x_d)
        else:
            y_d = higher_y - lower_y
            x_d = higher_x - lower_x
            han = (higher_y + y_d, higher_x + x_d)
            lan = (lower_y - y_d, lower_x - x_d)

            while not range_violated(han[0], han[1]):
                antis.add(han)
                han = (han[0] + y_d, han[1] + x_d)
            while not range_violated(lan[0], lan[1]):
                antis.add(lan)
                lan = (lan[0] - y_d, lan[1] - x_d)
    return antis.union(calcAntinodes(list[1:], inputantis))


# read
with open("../input/8.txt") as f:
    lines = f.readlines()
# parse (two stage)
chars = defaultdict(list)
for idy, line in enumerate(lines):
    y_len = len(lines)
    x_len = len(line)
    for idx, char in enumerate(line.strip()):
        if char != "." and char != "#":
            chars[char].append((idy, idx))

ans = 0
allSet = set()
for char in chars.keys():
    listPositions = chars[char]
    antinodes = calcAntinodes(listPositions, [])
    for node in antinodes:
        if node not in allSet:
            allSet.add(node)
            ans += 1
print(len(allSet))