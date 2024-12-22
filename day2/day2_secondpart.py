filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day2/day2.in"
lines = []

with open(filename) as file:
    while line := file.readline():
        lines.append(list(map(int, line.rstrip().split())))

sum = 0  

for i in range(len(lines)):
    tmp_line = lines[i]
    sorted_line = sorted(tmp_line)
    r_sorted_line = sorted(tmp_line, reverse=True)
    found = False
    secound_found = False
    if not found and tmp_line == sorted_line or tmp_line == r_sorted_line:
        if len(set(tmp_line)) == len(tmp_line):
            valid = True
            for j in range(1, len(tmp_line)):
                if abs(tmp_line[j] - tmp_line[j - 1]) > 3:
                    valid = False
                    break
            if valid:
                sum += 1
                found = True
    if not found:
        for j in range(len(tmp_line)):
            secondpart_list = tmp_line[:]
            if not secound_found:
                del secondpart_list[j]
                sorted_line = sorted(secondpart_list)
                r_sorted_line = sorted(secondpart_list, reverse=True)
                if len(set(secondpart_list)) == len(secondpart_list) and (secondpart_list == sorted_line or secondpart_list == r_sorted_line) :
                    valid = True
                    for k in range(1, len(secondpart_list)):
                        if abs(secondpart_list[k] - secondpart_list[k - 1]) > 3:
                            valid = False
                            break
                    if valid:
                        sum += 1
                        secound_found = True
print(sum)
