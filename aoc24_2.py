import functools
from collections import defaultdict
import sys

from parse import parse

sys.setrecursionlimit(999999)
# read
with open("input/24.txt") as f:
    in_a, in_b = f.read().split("\n\n")
in_list = []
map = defaultdict(list)
a = in_a.splitlines()
b = in_b.splitlines()
# process
# answer

# todo this isnt working but we can use it to test addition fixes we make

for j in range(0,44):
    print("ones bit " + str(j))
    defined = {}
    for i in range(0,44):
        if i == j:
            if i < 10:
                defined["x0" + str(i)] = 1
                defined["y0" + str(i)] = 1
            else:
                defined["x" + str(i)] = 1
                defined["y" + str(i)] = 1
        elif i < 10:
            defined["x0" + str(i)] = 0
            defined["y0" + str(i)] = 0
        else:
            defined["x" + str(i)] = 0
            defined["y" + str(i)] = 0


    for i in range(400):
        for b_x in b:
            nums = []
            vals = parse("{0} {1} {2} -> {3}", b_x.strip())
            for val in vals.fixed:
                nums.append(val)
            if nums[3] not in defined and nums[0] in defined and nums[2] in defined:
                if nums[1] == "XOR":
                    defined[nums[3]] = defined[nums[0]] ^ defined[nums[2]]
                if nums[1] == "OR":
                    defined[nums[3]] = defined[nums[0]] | defined[nums[2]]
                if nums[1] == "AND":
                    defined[nums[3]] = defined[nums[0]] & defined[nums[2]]



    ans = ""
    for i in range(0,46)[::-1]:
        try:
            if i < 10:
                ans += str(defined["z0" + str(i)])
            else:
                ans += str(defined["z" + str(i)])
        except BaseException:
            op = ans
    print(ans)

    ans = ""
    for i in range(0,44)[::-1]:
        if i < 10:
            ans += str(defined["x0" + str(i)])
        else:
            ans += str(defined["x" + str(i)])
    print(ans)

    ans = ""
    for i in range(0,44)[::-1]:
        if i < 10:
            ans += str(defined["y0" + str(i)])
        else:
            ans += str(defined["y" + str(i)])
    print(ans)

val = 58367545758258 - 7300390135833 - 15882766754361 - pow(2,11) - pow(2,45) - pow(2,5) + pow(2,6) - pow(2,24)
print("{0:b}".format(val))
# correct parts
# !01000111001 in y
# y11 wrong needs to be true
# 58367545758258 = 7300390135833 + 15882766754361

# z45 wrong needs to be false
# z5 wrong needs to be true
# z26 is wrong needs to be true

# resultant is
# !111111111111111111100000

# these bits flip in the output
# + pow(2,11) - pow(2,45) - pow(2,5) + pow(2,6) - pow(2,24)
# z06, z05, z11, z24, z45 all INDEPENDENT

# the theory for half and full adders is pretty simple.
# half adder
# z[0] = x[0] XOR y[0]

# full adder from two half adders (probably why we have ORs)
# z[0] = x[0] XOR y[0] XOR cin
# cout[0] = [(x[0] XOR y[0]) AND cin] OR (x[0] AND y[0])

#89 ANDs
#89 XORs
#44 ORs

# so this all feels very likely to be an exact solution, maybe with 1-2 wires that are constants or distractors
"""
x05 XOR y05 -> qfs
qfs XOR whh -> bpf
qfs AND whh -> z05

y05 AND x05 -> qjc
x04 XOR y04 -> vpn
vpn AND wjg -> rcr
vpn XOR wjg -> z04 # z04 is right, making both of these wrong?
x04 AND y04 -> fkc
rcr OR fkc -> whh
qfs XOR whh -> bpf
vgg AND fgw -> csf
bpf OR qjc -> fgw
fgw XOR vgg -> z06

TODO
skn OR spp -> z11
gmr XOR hqc -> z24
svd OR nfd -> z45

"""