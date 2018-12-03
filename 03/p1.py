import sys

# Each cell contains the # of times it is included in an entry
grid = [
    [0 for _ in range(10000)] for _ in range(10000)
]

claims = dict()
for line in sys.stdin:
    # Process the line to extract the values we need
    tokens = line.split(" ")
    id = tokens[0]

    yx = tokens[2].replace(":", "").split(",")
    y = int(yx[0])
    x = int(yx[1])

    wl = tokens[3].split("x")
    cols = int(wl[0])
    rows = int(wl[1])

    claims[id] = (x, y, rows, cols)

    # Update counter
    for i in range(x, x + rows):
        for j in range(y, y + cols):
            grid[i][j] += 1

# How many cells have counts > 1?
count = 0
for row in grid:
    for item in row:
        if item > 1:
            count += 1
print(count)

# Part 2: find the claim that doesn't overlap with any others
for id, props in claims.items():
    # Check that all cells of this claim have a 1
    found = True
    for i in range(props[0], props[0] + props[2]):
        for j in range(props[1], props[1] + props[3]):
            if grid[i][j] > 1:
                found = False
    
    if found:
        print("Id: {}".format(id))
        break

