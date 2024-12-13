import collections
import re
from email.policy import default

# initialize
a = []
b = []
#read
with open("../input/3.txt") as f:
    lines = f.readlines()
#parse
bigstr = ""
for line in lines:
    bigstr += line
regex = r'mul\((\d+),(\d+)\)'
matches = re.finditer(regex, bigstr, re.MULTILINE)

sum = 0
# from regex101
enables = {}
dos_match = re.finditer(r'do\(\)', bigstr, re.MULTILINE)
for matchNum, match in enumerate(dos_match, start=1):
    enables[match.end()] = "Do"
donts_match = re.finditer(r"don't\(\)", bigstr, re.MULTILINE)
for matchNum, match in enumerate(donts_match, start=1):
    enables[match.end()] = "Dont"

enabled = True
for matchNum, match in enumerate(matches, start=1):
    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
    idx = match.end()
    while idx > 0:
        if idx in enables:
            instr = enables[idx]
            if instr == "Do":
                enabled = True
            if instr == "Dont":
                enabled = False
            break
        idx -= 1

    if enabled:
        sum += int(match.group(1)) * int(match.group(2))
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))
print(sum)