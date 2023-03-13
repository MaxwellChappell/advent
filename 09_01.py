X = 0
Y = 1
head = [0, 0]
tail = [0, 0]


def move_right(amount):
    spaces = []
    start_same = 0
    print(head[X], tail[X])
    if head[Y] == tail[Y]:
        if head[X] == tail[X]:
            start_same = 1
        spaces = [[X + i, tail[Y]] for i in range(amount - start_same)]
        head[X] += amount
        tail[X] += amount - start_same
    print(head[X], tail[X])
    return spaces


with open("09.txt") as f:
    moves = f.readlines()
visited = set(tail)
print(move_right(5))
