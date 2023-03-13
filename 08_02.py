with open("08.txt") as f:
    forrest = f.readlines()


def main():
    max = 0

    for x in range(0, 99):
        for y in range(0, 99):
            value = look(x, y)
            if value > max:
                max = value

    print(max)
    print(look(97, 98))


def look(x, y):
    up, down, left, right = 0, 0, 0, 0
    height = int(forrest[x][y])
    # print(forrest[x][y])
    # up
    if x > 0:
        max_height = -1
        for dx in range(x-1, -1, -1):
            tree = int(forrest[dx][y])
            if tree >= height:
                up += 1
                break
            else:
                up += 1
    if x < 98:
        max_height = -1
        for dx in range(x+1, 99):
            tree = int(forrest[dx][y])
            if tree >= height:
                down += 1
                break
            else:
                down += 1
    if y > 0:
        max_height = -1
        for dy in range(y-1, -1, -1):
            tree = int(forrest[x][dy])
            if tree >= height:
                left += 1
                break
            else:
                left += 1
    if y < 98:
        max_height = -1
        for dy in range(y+1, 99):
            tree = int(forrest[x][dy])
            if tree >= height:
                right += 1
                break
            else:
                right += 1
    #print(x, y, up, down, left, right, up * down * left * right)
    return up * down * left * right


main()
