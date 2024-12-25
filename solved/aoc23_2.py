import functools
from collections import defaultdict
import sys
sys.setrecursionlimit(999999)

# read
with open("../input/23.txt") as f:
    in_a =  f.read().splitlines()
map = defaultdict(list)
# process
# answer

ans = 0
for book in in_a:
    tmp = book.split("-")
    a = tmp[0].strip()
    b = tmp[1].strip()
    map[a].append(b)
    map[b].append(a)

def backtrack(includeAll, includeSome, includeNone):
    if len(includeSome) == 0 and len(includeNone) == 0:
        return includeAll # base case bron kerbosch
    remaining = includeSome.copy()
    max_graph = {}
    for vertex in includeSome:
        neighbors = set(map[vertex])
        res = backtrack(includeAll.union({vertex}), remaining.intersection(neighbors), includeNone.intersection(neighbors))
        if len(res) > len(max_graph):
            max_graph = res
        remaining.remove(vertex)
        includeNone.add(vertex)
    return max_graph

in_connected = defaultdict(lambda: False)
max_graph = backtrack(set(), set(map.keys()), set())
max_graph = sorted(list(max_graph))
print(",".join(max_graph))