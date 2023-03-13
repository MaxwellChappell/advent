answer = 0


def mover(crates, start, end):
    print(crates, stacks[start-1], stacks[end-1])
    boxes = stacks[start-1][-crates:]
    [stacks[start-1].pop() for i in range(crates)]
    [stacks[end-1].append(crate) for crate in boxes]


with open("05.txt") as f:
    lines = f.readlines()

stacks = [
    ['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'],
    ['W', 'P', 'Q', 'G', 'S'],
    ['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'],
    ['F', 'Z', 'P', 'C', 'G', 'D', 'L'],
    ['T', 'P', 'S'],
    ['H', 'D', 'F', 'W', 'R', 'L'],
    ['Z', 'N', 'D', 'C'],
    ['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'],
    ['R', 'M', 'S', 'G', 'Z', 'W', 'V']
]
goods = ""
for move in lines[10:]:
    m = list(map(int, move.replace("move ", "").replace(
        "from ", "").replace("to ", "").replace("\n", "").split(" ")))
    mover(m[0], m[1], m[2])

for stack in stacks:
    print(stack)
