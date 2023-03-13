answer = 0

with open("03.txt") as f:
    lines = f.readlines()

goods = ""
for rucksack in range(0, len(lines), 3):
    one = lines[rucksack]
    two = lines[rucksack + 1]
    three = lines[rucksack + 2]
    good = list(set.intersection(*map(set, [one, two, three])))
    good.sort()
    goods += good[1]

for letter in goods:
    if ord(letter) > 96:
        answer += ord(letter) - 96
    else:
        answer += ord(letter) - 38
print(answer)
