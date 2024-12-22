filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day1/day1.in"
lines = []
l1 = []
l2 = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip().split(" "))
for i in range(len(lines)):
    l1.append(lines[i][0])
    l2.append(lines[i][-1])

sum = 0

l1.sort()
l2.sort()
for i in range(len(l1)):
    sum += abs(int(l1[i])-int(l2[i]))
print(sum)