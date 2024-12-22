filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day7/day7.in"
lines = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip().split(": "))

sum = 0

def calc(num,op):
    result = num[0]
    for i in range(len(op)):
        if op[i] == "+":
            result += num[i+1]
        elif op[i] == "*":
            result *= num[i+1]
    return result
            
for i in range(len(lines)):
    lines[i][0] = int(lines[i][0])
    lines[i][1] = list(map(int,lines[i][1].split(" ")))

for i in range(len(lines)):
    combs = [""]
    for j in range((len(lines[i][1])-1)):
        tmp_comb = []
        for comb in combs:
            tmp_comb.append(comb + "+")
            tmp_comb.append(comb + "*")
        combs = tmp_comb
    for j in range(len(combs)):
        if calc(lines[i][1],combs[j]) == lines[i][0]:
            sum += lines[i][0]
            break
print(sum)