from collections import  deque

with open("input/9.txt") as f:
    lines = f.readline()
unzipped = []
datum = 0
indices = []
totaldata = 0
for idx, char in enumerate(lines):
    if idx % 2 == 0:
        # datum, SIZE
        unzipped.append((str(datum), int(char)))
        totaldata += int(char)
        datum += 1
    else:
        unzipped.append((str(datum), int(char)))
        indices.append()
        totaldata += int(char)
print(unzipped)
print(indices)

#TODO wholesale rewrite of this.


checksum = 0
for idx, elem in enumerate(unzipped):
    if elem != ".":
        checksum += idx * int(elem)
print(checksum)