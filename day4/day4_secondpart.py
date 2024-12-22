filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day4/day4.in"
lines = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip())

sum = 0
line = 0
col = 0

def bigones(l):
    d1 = []
    for i in range(len(l)):
        d1.append(l[i][i])
    d2 = []
    for i in range(len(l)):
        d2.append(l[i][len(l) - i - 1])
    s1 = "".join(col for col in d1)
    s2 = "".join(col for col in d2)
    if (s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM"):
        return 1
    else:
        return 0

while col+2 < len(lines):
    while line+2 < len(lines[col]):
        bigone_mas=[]
        for i in range(3):
            bigone_mas.append(lines[col+i][line:line+3])
        sum += bigones(bigone_mas)
        line += 1
    col += 1
    line = 0

print(sum)
