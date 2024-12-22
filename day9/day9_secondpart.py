filename = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day9/day9.in"
inp = ""
with open(filename) as is_file:
    while line := is_file.readline():
        inp += line.rstrip()
bigone = []
sum = 0
size = [0] * len(inp)
loc = [0] * len(inp)
is_file = True
id = 0

for x in inp:
    x = int(x)
    if is_file:
        loc[id] = len(bigone)
        size[id] = x
        bigone += [id] * x
        id += 1
        is_file = False
    else:
        bigone += ["."] * x
        is_file = True

print(f"loc: {loc}")
print(f"size: {size}")

count = 0
while size[count] > 0:
    count += 1


for i in range(count-1, -1, -1):
    free_space = 0
    first_free = 0
    while first_free < loc[i] and free_space < size[i]:
        first_free += free_space
        free_space = 0
        while bigone[first_free] != ".":
            first_free += 1
        while first_free + free_space < len(bigone) and bigone[first_free + free_space] == ".":
            free_space += 1
    if first_free >= loc[i]:
        continue
    for j in range(first_free, first_free + size[i]):
        bigone[j] = i
    for j in range(loc[i], loc[i] + size[i]):
        bigone[j] = "."

for i in range(len(bigone)):
    if bigone[i] != ".":
        sum += i * int(bigone[i])

print(sum)