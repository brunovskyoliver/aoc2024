filname = "/Users/oliver/Documents/Programming/SEMINAR_INF/aoc2024/day11/day11.in"
with open(filname) as file:
    numbers = list(map(int, file.read().strip().split()))

nums = {}
for x in numbers:
    if x in nums:
        nums[x] += 1
    else:
        nums[x] = 1

def blink(nums: dict):
    new_nums = {}
    for x in nums:
        l = len(str(x))
        if x == 0:
            if 1 in new_nums:
                new_nums[1] += nums[0]
            else:
                new_nums[1] = nums[0]
        elif l % 2 == 0:
            left = int(str(x)[:l//2])
            right = int(str(x)[l//2:])
            if left in new_nums:
                new_nums[left] += nums[x]
            else:
                new_nums[left] = nums[x]
            if right in new_nums:
                new_nums[right] += nums[x]
            else:
                new_nums[right] = nums[x]
        else:
            new_key = x * 2024
            if new_key in new_nums:
                new_nums[new_key] += nums[x]
            else:
                new_nums[new_key] = nums[x]
    
    return new_nums

for i in range(75):
    nums = blink(nums)

ans = 0
for x in nums:
    ans += nums[x]
print(ans)
