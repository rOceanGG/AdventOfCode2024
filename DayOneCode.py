f = open("DayOneTxt.txt")
a = []
b = []
for x in f:
    sp = x.split(' ')
    a.append(int(sp[0]))
    b.append(int(sp[-1]))

bCounts = {}

for num in b:
    if num in bCounts:
        bCounts[num] += 1
    else:
        bCounts[num] = 1

sim = 0
for n in a:
    if n in bCounts:
        sim += n * bCounts[n]

print(sim)