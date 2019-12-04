from pprint import pprint

input_file = '3.in'

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

def get_move(direction):
    if direction == 'U':
        return  UP
    elif direction == 'D':
        return DOWN
    elif direction == 'R':
        return RIGHT
    else:
        return LEFT

def draw(grid, num, magnitude, direction, start_row, start_col):
    move = get_move(direction)
    
    row = start_row
    col = start_col
    for _ in range(magnitude):
        drow, dcol = move
        row += drow
        col += dcol
        grid[row][col] += num
    
    return row, col

def mdist(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)

def init_grid(x, y):  
    mright = mleft = mup = mdown = 0
    cup = cright = 0
    for val in x:
        dir = val[0]
        magnitude = int(val[1:])

        if dir == 'U':
            cup += magnitude
            mup = max(mup, cup)
        elif dir == 'D':
            cup -= magnitude
            mdown =min(mdown, cup)
        elif dir == 'R':
            cright += magnitude
            mright = max(mright, cright)
        else:
            cright -= magnitude
            mleft = min(mleft, cright)
    
    mright2 = mleft2 = mup2 = mdown2 = 0
    cup = cright = 0
    for val in y:
        dir = val[0]
        magnitude = int(val[1:])

        if dir == 'U':
            cup += magnitude
            mup2 = max(mup2, cup)
        elif dir == 'D':
            cup -= magnitude
            mdown2 =min(mdown2, cup)
        elif dir == 'R':
            cright += magnitude
            mright2 = max(mright2, cright)
        else:
            cright -= magnitude
            mleft2 = min(mleft2, cright)

    mleft = min(mleft, mleft2)
    mright = max(mright, mright2)
    mup = max(mup, mup2)
    mdown = min(mdown, mdown2)
    print(mup, mdown, mright, mleft)

    # Central port location
    origin_row = mup
    origin_col = abs(mleft)
    print(f"Origin: {origin_row} {origin_col}")

    rows = abs(mdown) + mup + 2
    cols = abs(mleft) + mright + 2
    print(f"Dimensions: {rows}, {cols}")

    print("Initializing grid")
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid, origin_row, origin_col

def part1():
    x, y = [], []
    with open(input_file) as f:
    # with open('test.in') as f:
        x = f.readline().split(",")
        y = f.readline().split(",")

    grid, origin_row, origin_col = init_grid(x, y)
    rows = len(grid)
    cols = len(grid[0])

    print("Processing first wire")
    curr_row = origin_row
    curr_col = origin_col
    for val in x:
        direction = val[0]
        magnitude = int(val[1:])
        curr_row, curr_col = draw(grid, 1, magnitude, direction, curr_row, curr_col)

    print("Processing second wire")
    curr_row = origin_row
    curr_col = origin_col
    print(curr_row, curr_col)
    for val in y:
        direction = val[0]
        magnitude = int(val[1:])
        curr_row, curr_col = draw(grid, 2, magnitude, direction, curr_row, curr_col)

    # Intersections have a 3
    print("Processing intersections")
    intersections = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 3:
                intersections.append((i, j))
    print(f"Intersections: {intersections}")
    
    min_dist = 210932819312
    for r, c in intersections:
        distance = mdist(origin_row, origin_col, r, c)
        min_dist = min(min_dist, distance)
    
    print(min_dist)

    return intersections

def draw2(grid, num, magnitude, direction, start_row, start_col, irow, icol):
    move = get_move(direction)
    
    row = start_row
    col = start_col
    for i in range(magnitude):
        drow, dcol = move
        row += drow
        col += dcol
        grid[row][col] += num

        if row == irow and col == icol:
            return -1, -1, i + 1
    
    return row, col, magnitude

def part2(intersections):
    x, y = [], []
    with open(input_file) as f:
        x = f.readline().split(",")
        y = f.readline().split(",")
    
    grid, origin_row, origin_col = init_grid(x, y)

    # For each intersection, count the number of steps needed to reach it
    min_steps = 213293982823
    for i, intersection in enumerate(intersections):
        print(f"Processing intersection {i + 1} of {len(intersections)}")

        irow, icol = intersection

        # Draw wire 1
        grid1 = grid[:]
        steps1 = 0
        curr_row = origin_row
        curr_col = origin_col
        for val in x:
            direction = val[0]
            magnitude = int(val[1:])
            curr_row, curr_col, steps_taken = draw2(grid1, 1, magnitude, direction, curr_row, curr_col, irow, icol)
            steps1 += steps_taken

            # Reached intersection
            if curr_row == -1 and curr_col == -1:
                break

        # Draw wire 2
        grid2 = grid[:]
        steps2 = 0
        curr_row = origin_row
        curr_col = origin_col
        for val in y:
            direction = val[0]
            magnitude = int(val[1:])
            curr_row, curr_col, steps_taken = draw2(grid2, 2, magnitude, direction, curr_row, curr_col, irow, icol)
            steps2 += steps_taken

            # Reached intersection
            if curr_row == -1 and curr_col == -1:
                break
        
        steps = steps1 + steps2
        print(f"wire1:{steps1} wire2:{steps2}")
        min_steps = min(min_steps, steps)
    
    print(min_steps)


if __name__ == "__main__":
    intersections = part1()
    part2(intersections)
