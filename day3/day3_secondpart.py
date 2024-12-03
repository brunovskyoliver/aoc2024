filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day3/day3.in"
lines = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip())

sum = 0
bigone = ""
for i in range(len(lines)):
    bigone += lines[i]
status = True
first = True

while len(bigone) > 0:
    do_index = bigone.find("do()")
    dont_index = bigone.find("don't()")
    index = bigone.find("mul(")
    if (do_index != -1 and (index == -1 or do_index < index)) or \
       (dont_index != -1 and (index == -1 or dont_index < index)):
        if do_index != -1 and (dont_index == -1 or do_index < dont_index):
            status = True
            bigone = bigone[do_index + len("do()"):]
        elif dont_index != -1:
            status = False
            first = False
            bigone = bigone[dont_index + len("don't()"):]
    elif index != -1:
        bigone = bigone[index:]
        opening = bigone.find("(")
        closing = bigone.find(")")
        inside = bigone[opening + 1:closing]
        if not " {}[]&^%$@#" in inside and closing - opening <= 8 and (status or first):
            print(f"im inside of {bigone[do_index:closing+1]} with inside of {inside}")
            comma = inside.find(",")
            if 0 < comma < closing:
                just_inside_without_comma = inside.replace(",", "")
                if just_inside_without_comma.isnumeric():
                    sum += int(inside[0:comma]) * int(inside[comma + 1:])
        bigone = bigone[closing + 1:]
    else:
        break

print(sum)
