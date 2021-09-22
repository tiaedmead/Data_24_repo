treeCounter = 0
right = 3
down = 1
x = 0
y = 0

with open('input.txt') as file:
    lines = file.read().splitlines()

    while y < len(lines):
        line = lines[y]

        for n in range(7):
            line = line + line

        if line[x] == "#":
            treeCounter += 1

        x = x + int(right)
        y = y + int(down)

    print(treeCounter)
