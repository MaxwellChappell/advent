answer = 0


with open("06.txt") as f:
    lines = f.readline()

for i in range(0, len(lines)-14):
    if len(set(lines[i:i+14])) == 14:
        print(i+14)
        break
