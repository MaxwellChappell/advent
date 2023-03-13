
score = 0

'''
A,X = Rock
b, Y = PAPER
c, Z = Scissors
'''

with open("02.txt") as f:
    lines = f.readlines()

for move in lines:
    op, me = move.split()
    if me == 'X':  # Me: Rock
        score += 1
        if op == "A":  # Op Rock
            score += 3
        elif op == "C":  # Op Scissors
            score += 6
    elif me == "Y":  # Me: Paper
        score += 2
        if op == "B":  # Op: Paper
            score += 3
        elif op == "A":  # Op: Rock
            score += 6
    elif me == "Z":  # Me: Scissors
        score += 3
        if op == "C":  # Op: Scissors
            score += 3
        elif op == "B":  # Op Rock
            score += 6

print(score)
