filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day9/day9.in"
inp = ""
with open(filename) as file:
    while line := file.readline():
        inp += line.rstrip()
bigone = []
sum = 0
id = 0
is_file = True
for x in inp:
    x = int(x)
    if is_file:
        bigone += [id] * x
        id += 1
        is_file = False
    else:
        bigone += ["."] * x
        is_file = True
first_free = 0
while bigone[first_free] != ".":
    first_free += 1

i = len(bigone) - 1
while bigone[i] == ".":
    i -= 1

while i > first_free:
    bigone[first_free] = bigone[i]
    bigone[i] = "."
    while bigone[i] == ".":
        i -= 1
    while bigone[first_free] != ".":
        first_free += 1

for i in range(len(bigone)):
    if bigone[i] != ".":
        sum += i * int(bigone[i])

print(sum)