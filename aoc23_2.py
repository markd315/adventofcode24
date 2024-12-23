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
for book in in_a:
    tmp = book.split("-")
    a = tmp[0].strip()
    b = tmp[1].strip()
    map[a].append(b)
    map[b].append(a)

def dfs(node, dest, map, ):


in_connected = defaultdict(lambda: False)
max_graph = list()
for key in map.keys():
    connect
print(ans)