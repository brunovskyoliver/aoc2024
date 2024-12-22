filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day13/day13.in"
lines = []
with open(filename) as file:
    lines = file.read().strip().split("\n\n")

def parse(x):
    lines = x.split("\n")
    a_line = lines[0].split("Button A: X+")[1].split(", Y+")
    a = [int(a_line[0]), int(a_line[1])]
    b_line = lines[1].split("Button B: X+")[1].split(", Y+")
    b = [int(b_line[0]), int(b_line[1])]
    p_line = lines[2].split("Prize: X=")[1].split(", Y=")
    p = [int(p_line[0]), int(p_line[1])]

    return a, b, p

prices = []
for a, b, p in [parse(line) for line in lines]:
    def test(i, j):
        x = a[0] * i + b[0] * j
        y = a[1] * i + b[1] * j
        return (x, y) == tuple(p)

    va = 1 << 30
    for i in range(100):
        for j in range(100):
            if test(i, j):
                va = min(va, 3 * i + j)

    if va < 1 << 30:
        prices.append(va)

print(sum(prices))
