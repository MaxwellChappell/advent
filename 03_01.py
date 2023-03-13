answer = 0

with open("03.txt") as f:
    lines = f.readlines()

goods = ""
for rucksack in lines:
    one = rucksack[:int(len(rucksack)/2)]
    two = rucksack[int(len(rucksack)/2):]
    goods += "".join(set(one).intersection(two))


for letter in goods:
    print(letter, ord(letter))
    if ord(letter) > 96:
        answer += ord(letter) - 96
    else:
        answer += ord(letter) - 38
print(answer)
