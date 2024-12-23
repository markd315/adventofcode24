import functools
from collections import defaultdict
import sys
sys.setrecursionlimit(999999)

def mix(i, j):
   return i ^ j

# read
with open("input/22.txt") as f:
    in_a = f.read()
in_list = []
map = defaultdict(list)
a = in_a.splitlines()
# process
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

mod_divisor = 2048 * 64 * 128 #16777216


def secretNum(secret):
    secret = mix(secret, secret * 64) % 16777216
    secret = mix(secret, int(secret / 32)) % 16777216
    secret = mix(secret, secret * 2048) % 16777216
    return secret

print(mod_divisor)

for secret in a:
    secret = int(secret)
    for i in range(2000):
        secret = secretNum(secret)
    ans += secret
print(ans)
