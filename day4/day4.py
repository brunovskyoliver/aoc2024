filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day4/day4.in"
lines = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip())

sum = 0

 

def smallones(l):
    diagonals = []
    for col in range(len(l[0])):
        diagonal = []
        x, y = 0, col
        while x < len(l) and y >= 0:
            diagonal.append(l[x][y])
            x += 1
            y -= 1
        diagonals.append("".join(diagonal))
    for row in range(1, len(l)):
        diagonal = []
        x, y = row, len(l[0]) - 1
        while x < len(l) and y >= 0:
            diagonal.append(l[x][y])
            x += 1
            y -= 1
        diagonals.append("".join(diagonal))
    return diagonals

diagonals = bigones(lines) + smallones(lines)

vertical = []
for i in range(len(lines[0])):
    vertical.append([])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        vertical[j].append(lines[i][j])
vertical = ["".join(col) for col in vertical]

for i in range(len(lines)):
    sum += lines[i].count("XMAS")
    sum += lines[i].count("SAMX")

for i in range(len(diagonals)):
    sum += diagonals[i].count("XMAS")
    sum += diagonals[i].count("SAMX")

for i in range(len(vertical)):
    sum += vertical[i].count("XMAS")
    sum += vertical[i].count("SAMX")

print(sum)