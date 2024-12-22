filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day6/day6.in"
lines = []
first = 0
count = 0
sum = 0

with open(filename) as file:
    while line := file.readline():
        if "^" in line.rstrip():
            first = count
        lines.append(list(line.rstrip()))
        count += 1

x, y = lines[first].index("^"), first

def up(lines, x, y):
    if y == 0:
        lines[y][x] = "X"
        return lines, x, -1
    elif lines[y-1][x] != "#":
        lines[y][x] = "X"
        lines[y-1][x] = "^"
        return lines, x, y-1
    else:
        return False

def down(lines, x, y):
    if y == len(lines) - 1:
        lines[y][x] = "X"
        return lines, x, len(lines)
    elif lines[y+1][x] != "#":
        lines[y][x] = "X"
        lines[y+1][x] = "v"
        return lines, x, y+1
    else:
        return False

def right(lines, x, y):
    if x == len(lines[y]) - 1:
        lines[y][x] = "X"
        return lines, len(lines[y]), y
    elif lines[y][x+1] != "#":
        lines[y][x] = "X"
        lines[y][x+1] = ">"
        return lines, x+1, y
    else:
        return False

def left(lines, x, y):
    if x == 0:
        lines[y][x] = "X"
        return lines, -1, y
    elif lines[y][x-1] != "#":
        lines[y][x] = "X"
        lines[y][x-1] = "<"
        return lines, x-1, y
    else:
        return False

while (0 <= x < len(lines[0])) and (0 <= y < len(lines)):
    guard = lines[y][x]
    if guard == "^":
        if result := up(lines, x, y):
            lines, x, y = result
        else:
            lines[y][x] = ">"
    elif guard == ">":
        if result := right(lines, x, y):
            lines, x, y = result
        else:
            lines[y][x] = "v"
    elif guard == "v":
        if result := down(lines, x, y):
            lines, x, y = result
        else:
            lines[y][x] = "<"
    elif guard == "<":
        if result := left(lines, x, y):
            lines, x, y = result
        else:
            lines[y][x] = "^"
    if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
        break

for line in lines:
    sum += line.count("X")

print(sum)
