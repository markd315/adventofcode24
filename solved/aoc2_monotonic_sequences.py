def isSafe(in_list):
    inc = False
    if in_list[1] > in_list[0]:
        inc = True
    for idx, num in enumerate(in_list):
        if idx == 0: # skip first lap
            continue
        if inc:
            if num <= in_list[idx - 1]: # decreased or same
                return False
            if num - in_list[idx - 1] > 3:
                return False
        else:
            if num >= in_list[idx - 1]:  # inreased or same
                return False
            if num - in_list[idx - 1] < -3:
                return False
    return True

# initialize
reports = []
#read
with open("../input/2.txt") as f:
    lines = f.readlines()
#parse
for line in lines:
    nums = []
    for num in line.split(" "):
        nums.append(int(num))
    reports.append(nums)
#process
#answer
safe = 0
for idx, elem in enumerate(reports):
    safe = safe + 1 if isSafe(elem) else safe
print(safe)