from functools import cache, lru_cache
import sys

sys.setrecursionlimit(10**6)

@cache
def stone(elem, steps):
    strelem = str(elem)
    if steps == 0:
        return 1
    elif elem == 0:
        ret=stone(1, steps - 1)
    elif len(strelem) % 2 == 0:
        half = int(len(strelem) / 2)
        left = int(strelem[0:half])
        right = int(strelem[half:])
        ret=stone(left, steps - 1) + stone(right, steps -1)
    else:
        ret = stone(elem * 2024, steps -1)
    return ret


# initialize
in_list = []
b = []
#read
with open("../input/11.txt") as f:
    lines = f.readline()
for n in lines.strip().split(" "):
    in_list.append(int(n))
#process
#answer
ans = 0
prev = len(in_list)
sum = 0
for st in in_list:
    sum += stone(st, 75)
    print(sum)
    print(str(st) + "STONE")
print(sum)

