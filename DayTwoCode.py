f = open("DayTwoTxt.txt")

reports = []

for line in f:
    levels = line.split(' ')
    reports.append([int(l) for l in levels])

def isSafe(level):
    increasing = level[0] < level[1]
    for x in range(1, len(level), 1):
        if increasing:
            diff = level[x] - level[x-1]
        else:
            diff = level[x-1] - level[x]
        if diff > 3 or diff < 1:
            return False
    return True

normalCount = 0
dampedCount = 0
for rep in reports:
    n = len(rep)
    if isSafe(rep):
        normalCount += 1
    for x in range(n):
        num = rep.pop(x)
        if isSafe(rep):
            dampedCount += 1
            break
        rep.insert(x, num)
print("Without dampener:",normalCount)
print("With dampener:",dampedCount)