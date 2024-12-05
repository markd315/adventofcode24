from collections import defaultdict


def helper(inp):
    print(inp)
    return inp

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
    if valid:
        middle = book[int(len(book) / 2)]
        ans += middle
print(ans)