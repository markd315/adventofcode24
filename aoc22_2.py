import collections
import functools
from collections import defaultdict
import sys
sys.setrecursionlimit(999999)
import numpy as np

def mix(i, j):
    #print("mix{0:b}".format(i ^ j))
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
    #print("   {0:b}".format(secret))
    secret = mix(secret, secret * 64) % 16777216
    #print("   {0:b}".format(secret))
    secret = mix(secret, int(secret / 32)) % 16777216
    #print("   {0:b}".format(secret))
    secret = mix(secret, secret * 2048) % 16777216
    #print("   {0:b}".format(secret))
    return secret

print(mod_divisor)



price_map = defaultdict(lambda: 0)
for secret in a:
    secret = int(secret)
    price_list = []
    prices_deque = collections.deque([secret % 10])
    discovered_chains = set()
    for i in range(2000):
        secret = secretNum(secret)
        price = secret % 10
        prices_deque.append(price)
        if i > 2:
            price_changes = []
            for j in range(len(prices_deque) - 1):
                price_changes.append(prices_deque[j+1] - prices_deque[j])
            prices_deque.popleft() # keep only latest 5
            t = tuple(price_changes)
            if t == (-2,1,-1,3):
                print("break")
            if t not in discovered_chains: # we found the first sequence
                price_map[t] += price
                discovered_chains.add(t)

max_sale = 0
for key, value in price_map.items():
    if value > max_sale:
        max_sale = value
print(max_sale)
# for example 1388589
# we have a repeated key of the LSBs 101101
# after mix 1, that sequence is doubled
# after mix 2, it is split up into the MSBs, and then LSB + "10"
# after mix 3, the MSB sequence is gone and the LSBs still have 10 at the end.
# feels like there are repeating 7 byte sequences in the output