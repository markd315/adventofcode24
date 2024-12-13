# I messed this file up implementing aoc9_2 and I dont even care anymore this one was bnasically an entirely different problem

from collections import  deque

with open("../input/9.txt") as f:
    lines = f.readline()
unzipped = []
datum = 0
indices = []
for idx, char in enumerate(lines):
    if idx % 2 == 0:
        # datum, SIZE
        unzipped.append((str(datum), int(char)))
    else:
        for i in range(0,int(char)):
            # INDEX<
            indices.append((len(unzipped) + i, int(char)))
        unzipped.append((".", int(char)))
print(unzipped)
print(indices)

idx = len(unzipped) - 1
while len(indices) > 0 and idx > indices[0]:
    if unzipped[idx][0] != ".":
        block_size = unzipped[idx][1]
        for idy, insert_size in indices:
            if block_size < insert_size:
                unzipped[indices[idy][0]][0] = "ok"
    idx -= 1
unzipped = unzipped[0:idx+1]
print(unzipped)
checksum = 0
for idx, elem in enumerate(unzipped):
    if elem != ".":
        checksum += idx * int(elem)
print(checksum)