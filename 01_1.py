
max_calories = 0

with open("01.txt") as f:
    lines = f.readlines()


elf = 0
for line in lines:
    if line == "\n":
        if elf > max_calories:
            max_calories = elf
        elf = 0
    else:
        elf += int(line)

print(max_calories)
