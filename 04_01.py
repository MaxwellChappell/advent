answer = 0

with open("04.txt") as f:
    lines = f.readlines()

goods = ""
for assignments in lines:
    nums = list(map(int, assignments.replace(
        ",", "-").replace("\n", "").split("-")))
    if nums[0] <= nums[2] and nums[1] >= nums[3]:
        answer += 1
    elif nums[2] <= nums[0] and nums[3] >= nums[1]:
        answer += 1
print(answer)


0-1, 2-3
