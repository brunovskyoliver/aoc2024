filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day14/day14.in"
lines = []
with open(filename) as file:
    lines = file.read().strip().split("\n")

wide = 103
tall = 101

p = []
v = []
for line in lines:
    a, b = line.split(" ")
    p.append(list(map(int, a.split("=")[1].split(","))))
    v.append(tuple(map(int, b.split("=")[1].split(","))))
    p[-1] = [p[-1][1], p[-1][0]]
    v[-1] = [v[-1][1], v[-1][0]]

length = len(p)
def update():
    global p, v
    for i in range(length):
        p[i][0] = (p[i][0] + v[i][0] + wide) % wide
        p[i][1] = (p[i][1] + v[i][1] + tall) % tall

def count_robots(i0, i1, j0, j1):
    sum = 0
    for i in range(i0, i1):
        for j in range(j0, j1):
            for ii, jj in p:
                if i == ii and j == jj:
                    sum += 1
    return sum

for i in range(100):    
    update()

q0 = count_robots(0, wide//2, 0, tall//2)
q1 = count_robots(wide//2+1, wide, 0, tall//2)
q2 = count_robots(0, wide//2, tall//2+1, tall)
q3 = count_robots(wide//2+1, wide, tall//2+1, tall)

print(q0, q1, q2, q3)
print(q0 * q1 * q2 * q3)