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
bad = 0
for a, b, p in [parse(line) for line in lines]:
    p[0] += 10000000000000
    p[1] += 10000000000000

    def verify(i, j):
        if i < 0 or j < 0:
            return False
        return (a[0] * i + b[0] * j == p[0]) and \
               (a[1] * i + b[1] * j == p[1])

    i = (p[0] * b[1] - b[0] * p[1]) // (b[1] * a[0] - b[0] * a[1])
    j = (p[1] - a[1] * i) // b[1]

    if verify(i, j):
        prices.append(3 * int(i) + int(j))

print(sum(prices))
