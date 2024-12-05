import functools
from collections import defaultdict


def helper(inp, two):
    if inp in map.keys():
        if two in map[inp]:
            return -1
    if two in map.keys():
        if inp in map[two]:
            return 1
    return 0

# initialize
a = []
b = []
#read
with open("input/5.txt") as f:
    lines = f.readlines()
#parse
in_pages = False
pages = []
map = defaultdict(list)
for line in lines:
    if line.strip() == "":
        in_pages = True
        continue
    if not in_pages:
        x = line.split("|")
        a_x = int(x[0])
        b_x = int(x[1].strip())
        map[a_x].append(b_x)
    else:
        nums = []
        for n in line.strip().split(","):
            nums.append(int(n))
        pages.append(nums)
#process
#answer
ans = 0
for book in pages:
    valid = True
    for k in map.keys():
        if k in book:
            for v in map[k]:
                if v in book:
                    if book.index(v) < book.index(k):
                        valid = False
                        break
            if not valid:
                break
    if not valid:
        sorted_book = sorted(book, key=functools.cmp_to_key(helper), reverse=True)
        middle = sorted_book[int(len(book) / 2)]
        ans += middle
print(ans)