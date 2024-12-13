import functools
from collections import defaultdict

def blink(param):
    out = []
    for elem in param:
        strelem = str(elem)
        if elem == 0:
            out.append(1)
        elif len(strelem) % 2 == 0:
            half = int(len(strelem)/2)
            out.append(int(strelem[0:half]))
            out.append(int(strelem[half:]))
        else:
            out.append(elem * 2024)
    return out

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
#out = blink(in_list)
#print(out)
prev = len(in_list)
for i in range(0,6):
    in_list = blink(in_list)
    print("blink " + str(i) + "   " + str(len(in_list)) + " div" + str(len(in_list) / prev))
    prev = len(in_list)
    print(in_list)
print(len(in_list))