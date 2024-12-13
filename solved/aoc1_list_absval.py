# initialize
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
b.sort()
#answer
dist = 0
for idx, elem in enumerate(a):
    dist += abs(elem - b[idx])
print(dist)