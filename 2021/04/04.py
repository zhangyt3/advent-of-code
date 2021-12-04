def parse_input(lines):
    numbers = [int(x) for x in lines[0].split(",")]

    board_size = 5
    boards = []
    board = []
    i = 1
    while i < len(lines):   
        line = [int(x) for x in lines[i].split()]
        board.append(line)
        i += 1

        if len(board) == board_size:
            boards.append(board)
            board = []

    return numbers, boards

def play(numbers, boards):
    for i, num in enumerate(numbers):
        for j, board in enumerate(boards):
            done = check_board(board, num)
            if done:
                return board, num, i, j
            
    return None, None, None, None

def check_board(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == num:
                board[i][j][1] = True
    
    for i in range(len(board)):
        bingo = True
        for j in range(len(board[i])):
            if not board[i][j][1]:
                bingo = False
                break
        if bingo:
            return True 
    
    for j in range(len(board[0])):
        bingo = True
        for i in range(len(board)):
            if not board[i][j][1]:
                bingo = False
                break
        if bingo:
            return True
    
    return False
    
def sum_unmarked(board):
    res = 0
    for line in board:
        for num, marked in line:
            if not marked:
                res += num
    return res

if __name__ == "__main__":
    with open("04.in") as file:
        lines = list(filter(lambda line: line != "", [x.strip() for x in file.readlines()]))
        numbers, boards = parse_input(lines)
        boards = list(map(lambda board: list(map(lambda line: [[num, False] for num in line], board)), boards))

        # Part 1
        winning_board, last_num, _, _ = play(numbers, boards)
        print(f"{sum_unmarked(winning_board) * last_num}")

        # Part 2
        while len(boards) > 1:
            winning_board, last_num, idx_num, idx_board = play(numbers, boards)
            boards = boards[:idx_board] + boards[idx_board + 1:]
            for board in boards:
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        board[i][j][1] = False
        winning_board, last_num, _, _ = play(numbers, boards)
        print(f"{sum_unmarked(winning_board * last_num)}")
        