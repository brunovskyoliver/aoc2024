import random
filename = "day5.in"
updates = []
orders = []
with open(filename) as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            orders.append(line.split("|"))
        elif "," in line:
            updates.append(line.split(","))

def checker(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def shufflehahaha(update, rules):
    while True:
        random.shuffle(update)
        if checker(update, rules):
            return update

sum = 0

for update in updates:
    if not checker(update, orders):
        shuffledone = shufflehahaha(update, orders)
        sum += int(shuffledone[len(shuffledone) // 2])

print(sum)
