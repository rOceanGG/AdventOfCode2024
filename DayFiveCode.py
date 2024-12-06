f = open("DayFiveTxt.txt")
rules = {}
updates = []

#For Part One
def inOrder(arr):
    for i in range(len(arr) - 1):
        if arr[i+1] in rules and arr[i] in rules[arr[i+1]]:
            return False
    return True
#For Part Two
def bubble(arr):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            if arr[i+1] in rules and arr[i] in rules[arr[i+1]]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True

#Parsing input
for line in f:
    if line[2] == '|':
        first, second = int(line[:2]), int(line[3:])
        if first in rules:
            rules[first].append(second)
        else:
            rules[first] = [second]
    else:
        updates.append(list(map(int, line.split(','))))

count = 0
altCount = 0
for update in updates:
    if inOrder(update):
        count += update[len(update) // 2]
    else:
        bubble(update)
        altCount += update[len(update) // 2]
#Part One
print(count)
#Part Two
print(altCount)