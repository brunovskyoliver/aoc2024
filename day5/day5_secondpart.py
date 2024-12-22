import random
filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day5/day5.in"
updates = []
orders = []
with open(filename) as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            orders.append(line.split("|"))
        elif "," in line:
            updates.append(line.split(","))

sum = 0

def checker(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def correcter3000(update, rules):
    current = update[:]
    for i in range(1000):
        current = random.shuffle(current)
        if checker(current, rules):
            return current
    for x, y in rules:
        if x in current and y in current:
            if current.index(x) > current.index(y):
                x_index = current.index(x)
                y_index = current.index(y)
                current[x_index], current[y_index] = current[y_index], current[x_index]
    return current

for update in updates:
    if not checker(update, orders):
        wrongones = correcter3000(update, orders)
        sum += int(wrongones[len(wrongones)//2])

print(sum)