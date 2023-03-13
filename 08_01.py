def main():
    with open("08.txt") as f:
        lines = f.readlines()

    visable = [['o'] * 99 for i in range(99)]
    # borders
    for i in range(99):
        visable[0][i] = "T"
        visable[98][i] = "T"
        visable[i][0] = "T"
        visable[i][98] = "T"

    # left to right
    print(type(int(lines[0][0])))

    for row in range(1, 99):
        max_height = int(lines[row][0])
        for col in range(1, 99):
            value = int(lines[row][col])
            if value > max_height:
                visable[row][col] = "T"
                max_height = value

    # right to left
    for row in range(1, 99):
        max_height = int(lines[row][98])
        for col in range(98, 0, -1):
            value = int(lines[row][col])
            if value > max_height:
                visable[row][col] = "T"
                max_height = value

    # up to down
    for col in range(1, 99):
        max_height = int(lines[0][col])
        for row in range(1, 99):
            value = int(lines[row][col])
            if value > max_height:
                visable[row][col] = "T"
                max_height = value

    # down to up
    for col in range(1, 99):
        max_height = int(lines[98][col])
        for row in range(98, 0, -1):
            value = int(lines[row][col])
            if value > max_height:
                visable[row][col] = "T"
                max_height = value

    for i in visable:
        print("".join(i))

    print(len(lines))
    print(len(visable))
    print(len(lines[0]))
    print(len(visable[0]))
    trees = 0
    for i in visable:
        trees += i.count("T")
    print(trees)


main()
