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
origo_path = set()
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

facing = 0
while True:
    origo_path.add((x, y))
    next_x = x + directions[facing][1]
    next_y = y + directions[facing][0]

    if not (0 <= next_x < len(lines[0]) and 0 <= next_y < len(lines)):
        break
    if lines[next_y][next_x] == "#":
        facing = (facing + 1) % 4
    else:
        x, y = next_x, next_y

def loop(ox, oy):
    if lines[oy][ox] == "#":
        return False

    lines[oy][ox] = "#"
    gx, gy = lines[first].index("^"), first
    visited = set()
    facing = 0

    while True:
        if (gx, gy, facing) in visited:
            lines[oy][ox] = "."
            return True
        visited.add((gx, gy, facing))

        next_x = gx + directions[facing][1]
        next_y = gy + directions[facing][0]

        if not (0 <= next_x < len(lines[0]) and 0 <= next_y < len(lines)):
            lines[oy][ox] = "."
            return False

        if lines[next_y][next_x] == "#":
            facing = (facing + 1) % 4
        else:
            gx, gy = next_x, next_y

for x, y in origo_path:
    if (x, y) == (lines[first].index("^"), first):
        continue
    if loop(x, y):
        sum += 1

print(sum)
