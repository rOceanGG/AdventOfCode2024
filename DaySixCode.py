#f = open("Test.txt")
f = open("DaySixTxt.txt")

grid = []

for line in f:
    grid.append([line[x] for x in range(len(line)) if line[x] != '\n'])

found = False
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] in "^>v<":
            curY = y
            curX = x
            direction = "^>v<".index(grid[y][x])  # Map symbol to direction
            found = True
            break
    if found:
        break
#Part One
visited = {(curY, curX)}
distincts = 1
def frontBlock(grid, direction, curY, curX):
    if direction == 0:
        if curY == 0:
            return False
        return grid[curY-1][curX] == '#'
    elif direction == 1:
        if curX == len(grid[curY]) -1 : return False
        return grid[curY][curX+1] == '#'
    elif direction == 2:
        if curY == len(grid) - 1: return False
        return grid[curY+1][curX] == '#'
    else:
        if curX == 0: return False
        return grid[curY][curX-1] == '#'
#0 -> North, 1 -> East, 2 -> South, 3 -> West
while curY >= 0 and curX >= 0 and curY < len(grid) and curX < len(grid):
    if frontBlock(grid, direction, curY, curX):
        direction = (direction + 1) % 4
    else:
        if direction == 0:
            curY -= 1
        elif direction == 1:
            curX += 1
        elif direction == 2:
            curY += 1
        else:
            curX -= 1
        visited.add((curY, curX))

print(len(visited)-1)