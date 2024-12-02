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
            if diff > 3 or diff < 1:
                return False
        else:
            diff = level[x-1] - level[x]
            if diff > 3 or diff < 1:
                return False
    
    return True

def isSafeWithDampener(level):
    increasing = level[0] < level[1]
    for x in range(1, len(level), 1):
        if increasing:
            diff = level[x] - level[x-1]
        else:
            diff = level[x-1] - level[x]
            
        if diff > 3 or diff < 1:
            first = level.pop(x)
            withoutFirst = isSafe(level)
            if withoutFirst: return True
            level.insert(x, first)
            level.pop(x-1)
            return isSafe(level)
    
    return True
#reports = [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
count = 0
for rep in reports:
    n = len(rep)
    for x in range(n):
        num = rep.pop(x)
        if isSafe(rep):
            count += 1
            #print("Done by removing", num, "at index", x)
            break
        rep.insert(x, num)
        #print("True")
    #else:
        #print("False")
print(count)