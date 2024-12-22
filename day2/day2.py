filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day2/day2.in"
lines = []

with open(filename) as file:
    while line := file.readline():
        lines.append(list(map(int, line.rstrip().split())))

sum = 0  

for i in range(len(lines)):
    tmp_line = lines[i]
    sorted_line = sorted(tmp_line)
    reverse_sorted_line = sorted(tmp_line, reverse=True)
    if tmp_line == sorted_line or tmp_line == reverse_sorted_line:
        if len(set(tmp_line)) == len(tmp_line):
            valid = True
            for j in range(1, len(tmp_line)):
                if abs(tmp_line[j] - tmp_line[j - 1]) > 3:
                    valid = False
                    break
            if valid:
                sum += 1
print(sum)