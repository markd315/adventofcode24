import functools
from collections import defaultdict
import sys
sys.setrecursionlimit(999999)

# read
with open("../input/19.txt") as f:
    in_a, in_b = f.read().split("\n\n")
in_list = []
map = defaultdict(list)
a = in_a.split(", ")
b = in_b.splitlines()
# answer

@functools.cache
def isInList(remainder):
    if remainder == "":
        return 1
    else:
        count = 0
        for towel in a:
            if remainder.startswith(towel):
                count += isInList(remainder[len(towel):])
        return count

ans = 0
for book in b:
    if isInList(book):
        ans += 1
print(ans)