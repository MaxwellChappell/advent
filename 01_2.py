
max_calories_3 = [0, 0, 0]

with open("01.txt") as f:
    lines = f.readlines()


elf = 0
for line in lines:
    if line == "\n":
        print(max_calories_3)
        if elf > min(max_calories_3):
            max_calories_3.append(elf)
            max_calories_3.remove(min(max_calories_3))
        elf = 0
    else:
        elf += int(line)

print(sum(max_calories_3))
