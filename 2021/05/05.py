def to_tuples(line):
    coords = line.split(" -> ")
    first = [int(x) for x in coords[0].split(",")]
    second = [int(x) for x in coords[1].split(",")]
    return [first, second]

def mark_board(board, lines, only_horizontal_and_vertial=True):
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        if only_horizontal_and_vertial and not (x1 == x2 or y1 == y2):
            continue
    
        horizontal = False
        vertical = False
        if x1 == x2:
            vertical = True
        if y1 == y2:
            horizontal = True
        
        if horizontal:
            start = min(x1, x2)
            end = max(x1, x2)
            for i in range(start, end + 1):
                board[y1][i] += 1
        elif vertical:
            start = min(y1, y2)
            end = max(y1, y2)
            for j in range(start, end + 1):
                board[j][x1] += 1
        else:
            # 45 degree angle - two cases (going up to the right/going down to the right)
            startx, starty = x2, y2
            endx, endy = x1, y1
            if x1 < x2:
                startx, starty = x1, y1
                endx, endy = x2, y2

            if starty < endy:
                # Going down to the right
                i, j = startx, starty
                while i <= endx:
                    board[j][i] += 1
                    i += 1
                    j += 1
            else:
                # Going up to the right
                i, j = startx, starty
                while i <= endx:
                    board[j][i] += 1
                    i += 1
                    j -= 1

def count_twos(board):
    twos = 0
    for line in board:
        for num in line:
            if num >= 2:
                twos += 1
    return twos

if __name__ == "__main__":
    with open("05.in") as file:
        lines = [x.strip() for x in file.readlines()]
        lines = list(map(to_tuples, lines))

        max_x = 0
        max_y = 0
        for line in lines:
            x1, y1 = line[0]
            x2, y2 = line[1]
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)

        board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        mark_board(board, lines, only_horizontal_and_vertial=False)
        twos = count_twos(board)
        print(f"Twos: {twos}")
