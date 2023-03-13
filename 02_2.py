
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
    if me == 'X':  # Me: Lose
        if op == "A":
            score += 3
        elif op == "B":
            score += 1
        else:
            score += 2
    elif me == "Y":  # Me: Draw
        score += 3
        if op == "A":
            score += 1
        elif op == "B":
            score += 2
        else:
            score += 3
    elif me == "Z":  # Me: Win
        score += 6
        if op == "A":
            score += 2
        elif op == "B":
            score += 3
        else:
            score += 1

print(score)
