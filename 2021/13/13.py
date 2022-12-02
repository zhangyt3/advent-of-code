from pprint import pprint

if __name__ == "__main__":
    lines = []
    folds = []
    with open("example.in") as f:
        lines_done = False
        for line in f.readlines():
            line = line.strip()
            if line == "":
                lines_done = True
                continue
            
            if not lines_done:
                lines.append(line)
            else:
                folds.append(line)

    # pprint(lines)
    # pprint(folds)
    # x == col
    # y == row
    lines = list(map(lambda line: [int(x) for x in line.split(",")], lines[:-3]))
    # pprint(lines)

    max_row = max([x[1] for x in lines])
    max_col = max([x[0] for x in lines])
    print(max_row, max_col)

    grid = [["." for _ in range(max_col + 1)] for _ in range(max_row + 1)]
    for col, row in lines:
        grid[row][col] = "#"
    pprint(grid)

    for fold in folds:
        tokens = fold.split(" ")
        axis, val = tokens[-1].split("=")
        
        if axis == "x":
            # Folding vertically
            print(f"Folding along x={val}")
            
            pass
        else:
            # Folding horizontally
            print(f"Folding along y={val}")
            pass

        break