import re

f = open("DayThreeTxt.txt", 'r')
p1allcoms = []
p2allcoms = []
total = 0
#Part One
for line in f:
    p1allcoms += re.findall(r"mul\(\d+,\d+\)", line)


for c in p1allcoms:
    arg = c.split(',')
    total += int(arg[0][4:]) * int(arg[1][:len(arg[1]) -1])

print(total)

#Part Two
f = open("DayThreeTxt.txt", 'r')
for line in f:
    p2allcoms += re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
total = 0
curIndex = 0
while curIndex < len(p2allcoms):
    if p2allcoms[curIndex] == "don't()":
        while curIndex < len(p2allcoms) and p2allcoms[curIndex] != "do()":
            curIndex += 1
    elif p2allcoms[curIndex] == "do()":
        curIndex += 1
    else:
        c = p2allcoms[curIndex]
        arg = c.split(',')
        total += int(arg[0][4:]) * int(arg[1][:len(arg[1]) -1])
        curIndex += 1

print(total)
