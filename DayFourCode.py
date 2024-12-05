#Part One
def wordSearch(grid):
    WORD = "XMAS"
    WORD_LEN = len(WORD)

    def frontHoriz(y, x):
        if x + WORD_LEN > len(grid[y]):
            return False
        return ''.join([grid[y][a] for a in range(x, x + WORD_LEN)]) == WORD

    def backHoriz(y, x):
        if x - WORD_LEN + 1 < 0:
            return False
        return ''.join([grid[y][a] for a in range(x, x - WORD_LEN, -1)]) == WORD

    def downVert(y, x):
        if y + WORD_LEN > len(grid):
            return False
        return ''.join([grid[a][x] for a in range(y, y + WORD_LEN)]) == WORD

    def upVert(y, x):
        if y - WORD_LEN + 1 < 0:
            return False
        return ''.join([grid[a][x] for a in range(y, y - WORD_LEN, -1)]) == WORD

    def downRight(y, x):
        if y + WORD_LEN > len(grid) or x + WORD_LEN > len(grid[y]):
            return False
        return ''.join([grid[y + c][x + c] for c in range(WORD_LEN)]) == WORD

    def downLeft(y, x):
        if y + WORD_LEN > len(grid) or x - WORD_LEN + 1 < 0:
            return False
        return ''.join([grid[y + c][x - c] for c in range(WORD_LEN)]) == WORD

    def upRight(y, x):
        if y - WORD_LEN + 1 < 0 or x + WORD_LEN > len(grid[y]):
            return False
        return ''.join([grid[y - c][x + c] for c in range(WORD_LEN)]) == WORD

    def upLeft(y, x):
        if y - WORD_LEN + 1 < 0 or x - WORD_LEN + 1 < 0:
            return False
        return ''.join([grid[y - c][x - c] for c in range(WORD_LEN)]) == WORD

    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if downVert(y, x): count += 1
            if downLeft(y, x): count += 1
            if downRight(y, x): count += 1
            if upLeft(y, x): count += 1
            if upRight(y, x): count += 1
            if upVert(y, x): count += 1
            if frontHoriz(y, x): count += 1
            if backHoriz(y, x): count += 1

    return count

# Read file and grid
with open("DayFourTxt.txt") as f:
    grid = [[letter for letter in line.strip()] for line in f]

# Run the search
print(wordSearch(grid))

#Part Two
def findXMas(grid):
    WORD = "MAS"
    WORD_LEN = len(WORD)

    def downRight(y, x):
        if y + WORD_LEN > len(grid) or x + WORD_LEN > len(grid[y]):
            return False
        return ''.join([grid[y + c][x + c] for c in range(WORD_LEN)]) == WORD

    def downLeft(y, x):
        if y + WORD_LEN > len(grid) or x - WORD_LEN + 1 < 0:
            return False
        return ''.join([grid[y + c][x - c] for c in range(WORD_LEN)]) == WORD

    def upRight(y, x):
        if y - WORD_LEN + 1 < 0 or x + WORD_LEN > len(grid[y]):
            return False
        return ''.join([grid[y - c][x + c] for c in range(WORD_LEN)]) == WORD

    def upLeft(y, x):
        if y - WORD_LEN + 1 < 0 or x - WORD_LEN + 1 < 0:
            return False
        return ''.join([grid[y - c][x - c] for c in range(WORD_LEN)]) == WORD
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x-1 >= 0 and x+1 < len(grid[y]) and y-1 >= 0 and y+1 < len(grid):
                if downRight(y-1, x-1) and (upRight(y+1, x-1) or downLeft(y-1, x+1)):
                    count += 1
                if upLeft(y+1, x+1) and (downLeft(y-1, x+1) or upRight(y+1, x-1)):
                    count += 1
    return count

print(findXMas(grid))
