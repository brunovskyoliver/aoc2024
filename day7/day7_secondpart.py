filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day7/day7.in"
lines = []
with open(filename) as file:
    while line := file.readline():
        lines.append(line.rstrip().split(": "))

sum = 0

def merge(a, b):
    return int(str(a) + str(b))

def calc(num, op):
    if len(op) < len(num) - 1:
        op += ['+'] * (len(num) - 1 - len(op))
    result = num[0]
    for i in range(len(op)):
        if op[i] == '+':
            result += num[i+1]
        elif op[i] == '*':
            result *= num[i+1]
        elif op[i] == '||':
            result = merge(result, num[i+1])
    return result

def all_combs(l):
    ops = ['+', '*', '||']
    combs = [[]]
    for i in range(l):
        tmp_comb = []
        for op in ops:
            for comb in combs:
                tmp_comb.append(comb + [op])
        combs = tmp_comb
    return combs


for i in range(len(lines)):
    nums = list(map(int, lines[i][1].split(" ")))
    for ops in all_combs(len(nums) - 1):
        try:
            if calc(nums, ops) == int(lines[i][0]):
                sum += int(lines[i][0])
                break
        except:
            continue

print(sum)
