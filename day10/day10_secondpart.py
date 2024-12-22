filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day10/day10.in"
lines = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip())
sum = 0
n = len(lines)
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def check(i, j):
    return (0 <= i < n) and (0 <= j < n)

def score(i, j):
    if lines[i][j] != "0":
        return 0
    sum = 0
    pos = [(i, j)]
    checked = set()
    while len(pos) > 0:
        cy, cx = pos.pop()
        cur = int(lines[cy][cx])
        if cur == 9:
            sum += 1
            continue
        for dy, dx in dirs:
            ii, jj = cy + dy, cx + dx
            if not check(ii, jj):
                continue
            if int(lines[ii][jj]) != cur + 1:
                continue
            pos.append((ii, jj))
    return sum


for i in range(n):
    for j in range(n):
        sum += score(i, j)

print(sum)