moves = [
    (-1, -1),
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1)
]

if __name__ == "__main__":
    octos = []
    with open("11.in") as f:
        octos = [x.strip() for x in f.readlines()]
    octos = list(map(lambda x: [int(num) for num in x], octos))

    flashes = 0
    steps = 500
    for step in range(steps):
        flashed = set()
        for i in range(len(octos)):
            for j in range(len(octos[i])):
                octos[i][j] += 1
        
        go = True
        while go:
            go = False
            for i in range(len(octos)):
                for j in range(len(octos[j])):
                    if octos[i][j] > 9:
                        flashes += 1
                        octos[i][j] = 0
                        flashed.add((i, j))
                        go = True

                        for di, dj in moves:
                            ni = i + di
                            nj = j + dj
                            if (ni, nj) in flashed:
                                continue
                            if 0 <= ni and ni < len(octos) and 0 <= nj and nj < len(octos[i]):
                                octos[ni][nj] += 1
        
        all_zero = True
        for row in octos:
            for val in row:
                if val != 0:
                    all_zero = False
                    break
        if all_zero:
            print(f"All octos flashing in step: {step + 1}")
    
    print(f"Flashes after {steps} steps: {flashes}")