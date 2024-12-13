import collections

# initialize
from email.policy import default

a = []
b = []
#read
with open("../input/1.txt") as f:
    lines = f.readlines()
#parse
for line in lines:
    x = line.split("   ")
    a.append(int(x[0]))
    b.append(int(x[1]))
#process
a.sort()
b_map = collections.defaultdict(int)
#b.sort()
for elem in b:
    b_map[elem] += 1
#answer
s_score = 0
for idx, elem in enumerate(a):
    s_score += b_map[elem] * elem
print(s_score)