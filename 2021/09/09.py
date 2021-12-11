moves = [
    (-1, 0), 
    (1, 0),
    (0, -1),
    (0, 1)
]

if __name__ == "__main__":
    lines = []
    with open("09.in") as f:
        lines = f.readlines()
    lines = list(map(lambda line: [int(x) for x in line.strip()], lines))

    total_risk = 0
    low_points = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            is_low = True
            for di, dj in moves:
                ni = i + di
                nj = j + dj
                if 0 <= ni and ni < len(lines) and 0 <= nj and nj < len(lines[i]):
                    if lines[i][j] >= lines[ni][nj]:
                        is_low = False
                        break
            if is_low:
                low_points.append((i, j))
                risk = 1 + lines[i][j]
                total_risk += risk
    print(f"Total risk: {total_risk}")

    basin_sizes = []
    for starti, startj in low_points:
        basin_size = 0
        stack = []
        visited = set()
        stack.append((starti, startj))
        while stack:
            i, j = stack.pop()

            if (i, j) in visited:
                continue
            visited.add((i, j))

            if lines[i][j] == 9:
                continue
                
            basin_size += 1
            for di, dj in moves:
                ni = i + di
                nj = j + dj
                if 0 <= ni and ni < len(lines) and 0 <= nj and nj < len(lines[i]):
                    if lines[i][j] < lines[ni][nj]:
                        stack.append((ni, nj))
        
        basin_sizes.append(basin_size)
    
    basin_sizes = sorted(basin_sizes)
    print(f"Part 2: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}")
