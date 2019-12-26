import math
from collections import deque
 
 
EMPTY = '.'
ASTEROID = '#'
 
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
# BFS-like
# If you can see an asteroid 2 rows over and 3 cols over, then you can't see
# an asteroid at any integer multiple of that displacement (e.g. 4 rows, 6 cols)
# Note: x = col, y = row
def find_seeable(grid, row, col):
    max_row, max_col = len(grid), len(grid[0])
    src_row, src_col = row, col
 
    seeable = []
    blocked = set()
    visited = set()
   
    q = deque()
    q.append((row, col))
    while q:
        # print(f'seeable-{seeable}, blocked-{blocked}, visited-{visited}')
        row, col = q.popleft()
     
        if (row, col) in visited:
            continue
     
        visited.add((row, col))
        if (row, col) not in blocked:
            if grid[row][col] == ASTEROID and (row, col) != (src_row, src_col):
                seeable.append((row, col))
                # Add all positions at integer multiples to blocked
                # reduce drow and dcol as much as possible first
                drow = row - src_row
                dcol = col - src_col
                gcd = math.gcd(drow, dcol)
                drow = drow // gcd
                dcol = dcol // gcd
                m = 2
                nrow = src_row + m * drow
                ncol = src_col + m * dcol
                while 0 <= nrow and nrow < max_row and 0 <= ncol and ncol < max_col:
                    # print(f'Blocking {nrow}, {ncol}')
                    blocked.add((nrow, ncol))
                    m += 1
                    nrow = src_row + m * drow
                    ncol = src_col + m * dcol
 
            for drow, dcol in MOVES:
                nrow = row + drow
                ncol = col + dcol
                if 0 <= nrow and nrow < max_row and 0 <= ncol and ncol < max_col:
                    # print(f'Adding to queue: {nrow}, {ncol}')
                    q.append((nrow, ncol))
 
    return seeable
 
def find_best_asteroid(grid):
    best_asteroid, best_count = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ASTEROID:
                seeable = find_seeable(grid, i, j)
                # print(f'i,j={i},{j}: {seeable}')
                if best_asteroid is None or len(seeable) > best_count:
                    best_asteroid = (i, j)
                    best_count = len(seeable)
 
    return best_asteroid, best_count

def simulate_laser(ogrid, src, n):
    """
    Find the nth asteroid to be vaporized.
    """
    rows = len(ogrid)
    cols = len(ogrid[0])
    orow, ocol = src

    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(ogrid[i][j])
    grid[orow][ocol] = EMPTY

    start_angle = math.atan2(-1, 0)

    # Find dist and angle of each asteroid to the monitoring station
    angles = dict()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ASTEROID:
                drow = i - orow
                dcol = j - ocol
                angle = math.atan2(dcol, drow) - 2 * start_angle
                if angle < 0:
                    angle += 2 * math.pi
                angles[(i, j)] = angle

    count = 0
    seeable = find_seeable(grid, orow, ocol)
    while seeable:   
        # Order all seeable asteroids by angle wrt monitoring station
        seeable = sorted(seeable, key=lambda x: -angles[x])

        # Vaporize
        for i, j in seeable:
            grid[i][j] = EMPTY
            count += 1
            print(f"The {count}th asteroid is at {i},{j}")
            if count == n:
                return i, j
        
        print(f"Count={count}")
        seeable = find_seeable(grid, orow, ocol)

    return -1, -1
 
if __name__ == '__main__':
    grid = []
    with open('10.in') as f:
        for line in f.readlines():
            grid.append(line.strip())
 
    rows = len(grid)
    cols = len(grid[0])
    print(f'Dimensions: {rows} rows by {cols} cols')
    print('\n'.join(grid))
   
    best, count = find_best_asteroid(grid[:])
    row, col = best
    print(f'Best asteroid for a monitoring station at x={col} y={row} can see {count} asteroids')

    # Part 2
    row, col = simulate_laser(grid[:], best, 200)
    print(f"The 200th asteroid vaporized is at row={row}, col={col}")
    print(f"col * 100 + row = {col * 100 + row}")
