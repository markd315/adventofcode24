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
    for c in map[b]:
        if c in map[a] and b in map[c] and c in map[b]:
            elems = [a, b, c]
            sets.add(tuple(sorted(elems)))
        if c in map[b] and a in map[c] and c in map[a]:
            elems = [a, b, c]
            sets.add(tuple(sorted(elems)))
    for c in map[a]:
        if c in map[a] and b in map[c] and c in map[b]:
            elems = [a, b, c]
            sets.add(tuple(sorted(elems)))
        if c in map[b] and a in map[c] and c in map[a]:
            elems = [a, b, c]
            sets.add(tuple(sorted(elems)))
    map[a].append(b)
    map[b].append(a)

print(ans)
for set in sets:
    a, b, c = set
    if "t" == a[0] or "t" == b[0] or "t" == c[0]:
        ans += 1
print(ans)