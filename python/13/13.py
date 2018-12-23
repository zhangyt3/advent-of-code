import sys
from pprint import pprint

def simulate(map, players):
    """
    map: the map of the tracks 
    players: dictionary mapping (row, col) -> (direction, next_turn)
    """
    temp = dict()
    for i, row in enumerate(map):
        for j, _ in enumerate(row):
            if (i, j) in players:
                player = players.pop((i, j))
                ii, jj, player = move(map, player, i, j) 
                print("Player at {}, {} moving to {}, {}".format(i, j, ii, jj))
                
                if (ii, jj) in temp or (ii, jj) in players:
                    # Part 1 - find location of first crash
                    # print("First collision at row {} col {}".format(ii, jj))
                    # sys.exit(0)

                    # Part 2 - remove carts that crash
                    if (ii, jj) in temp:
                        temp.pop((ii, jj))
                    if (ii, jj) in players:
                        players.pop((ii, jj))
                else:
                    temp[(ii, jj)] = player
    return temp

def is_cart(char):
    return char == '>' or  char == '<' or char == '^' or char == 'v'

def direction(char):
    if char == '>':
        return "RIGHT"
    elif char == '<':
        return "LEFT"
    elif char == 'v':
        return "DOWN"
    else:
        return "UP"

def go_down(row, col):
    return row + 1, col, "DOWN"

def go_up(row, col):
    return row - 1, col, "UP"

def go_right(row, col):
    return row, col + 1, "RIGHT"

def go_left(row, col):
    return row, col - 1, "LEFT"

def move(map, player, row, col):
    new_row, new_col = -1, -1
    track = map[row][col]
    dir, turn_dir = player
    if track == "+":
        if turn_dir == "LEFT":
            turn_dir = "STRAIGHT"
            if dir == "LEFT":
                new_row , new_col, dir = go_down(row, col)
            elif dir == "RIGHT":
                new_row, new_col, dir = go_up(row, col)
            elif dir == "UP":
                new_row, new_col, dir = go_left(row, col)
            else:
                new_row, new_col, dir = go_right(row, col)
        elif turn_dir == "RIGHT":
            turn_dir = "LEFT"
            if dir == "LEFT":
                new_row, new_col, dir = go_up(row, col)
            elif dir == "RIGHT":
                new_row , new_col, dir = go_down(row, col)
            elif dir == "UP":
                new_row, new_col, dir = go_right(row, col)
            else:
                new_row, new_col, dir = go_left(row, col)
        else:
            # STRAIGHT
            turn_dir = "RIGHT"
            if dir == "LEFT":
                new_row, new_col, dir = go_left(row, col)
            elif dir == "RIGHT":
                new_row, new_col, dir = go_right(row, col)
            elif dir == "UP":
                new_row, new_col, dir = go_up(row, col)
            else:
                new_row , new_col, dir = go_down(row, col)
    else:
        if track == "-":
            new_row = row
            if dir == "LEFT":
                new_col = col - 1
            else:
                new_col = col + 1
        elif track == "|":
            new_col = col
            if dir == "UP":
                new_row = row - 1
            else:
                new_row = row + 1
        elif track == "\\":
            if dir == "UP":
                new_row, new_col, dir = go_left(row, col)
            elif dir == "RIGHT":
                new_row, new_col, dir = go_down(row, col)
            elif dir == "DOWN":
                new_row, new_col, dir = go_right(row, col)
            else:
                new_row, new_col, dir = go_up(row, col)
        elif track == "/":
            if dir == "UP":
                new_row, new_col, dir = go_right(row, col)
            elif dir == "RIGHT":
                new_row, new_col, dir = go_up(row, col)
            elif dir == "DOWN":
                new_row, new_col, dir = go_left(row, col)
            else:
                new_row, new_col, dir = go_down(row, col)
    
    return new_row, new_col, (dir, turn_dir)


if __name__ == '__main__':
    # Initialize map
    map = []
    players = dict()
    for row, line in enumerate(sys.stdin):
        line = line.rstrip()
        for col, char in enumerate(line):
            if is_cart(char):
                dir = direction(char)
                players[(row, col)] = (dir, "LEFT")
        line = line.replace(">", "-").replace("<", "-").replace("v", "|").replace("^", "|")
        map.append(line)
    pprint(map)
    pprint(players)

    while True:
        # Part 2: stop when 1 cart is left
        if len(players) == 1:
            for pos, info in players.items():
                print("Final position:", pos)
                sys.exit(0)

        players = simulate(map, players)
        pprint(players)


