import functools
from collections import defaultdict
import sys
sys.setrecursionlimit(999999)

# read
with open("input/23.txt") as f:
    in_a =  f.read().splitlines()
map = defaultdict(list)
# process
# answer

ans = 0
sets = set()
for book in in_a:
    tmp = book.split("-")
    a = tmp[0].strip()
    b = tmp[1].strip()
    map[a].append(b)
    map[b].append(a)

#todo all connected to EACH OTHER

size = 0
arr = []
for elem in map.values():
    if len(elem) > size:
        arr = elem
        size = len(elem)
print(",".join(sorted(arr)))