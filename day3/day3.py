filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day3/day3.in"
lines = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip())
sum = 0
bigone = ""
for i in range(len(lines)):
    bigone += lines[i]
while len(bigone) > 0:
    index = bigone.find("mul(")
    bigone = bigone[index:]
    index = bigone.find("mul(")
    opening = bigone.find("(")
    closing = bigone.find(")")
    inside = bigone[opening+1:closing]
    if not " {}[]&^%$@#" in inside and closing - opening <= 8:
        print(f"im inside of {bigone[index:closing+1]} with inside of {inside}")
        comma = inside.find(",")
        if 0 < comma < closing:
            just_inside_without_comma = inside.replace(",","")
            if just_inside_without_comma.isnumeric():
                sum += int(inside[0:comma])*int(inside[comma+1:])
    bigone = bigone[opening+3:]

print(sum)