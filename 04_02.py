answer = 0

with open("04.txt") as f:
    lines = f.readlines()

goods = ""
for assignments in lines:
    nums = list(map(int, assignments.replace(
        ",", "-").replace("\n", "").split("-")))
    if set(range(nums[0], nums[1] + 1)) & set(range(nums[2], nums[3] + 1)):
        answer += 1
print(answer)


0-1, 2-3
