filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day5/day5.in"
updates = []
orders = []
with open(filename) as file:
    while line := file.readline():
        if "|" in line.rstrip():
            orders.append(line.rstrip().split("|"))
        elif "," in line.rstrip():
            updates.append(line.rstrip().split(","))
sum = 0

for update in updates:
    correct = True
    for x,y in orders:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                correct = False
                break
    if correct:
        sum += int(update[len(update)//2])
print(sum)