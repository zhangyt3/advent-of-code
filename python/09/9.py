def get_insert_spot(curr, length):
    # Insert between the marbles 1 and 2 steps clockwise (right) of curr
    # Should insert at the index +1 the returned index
    return (curr + 1) % length


def game(players, marbles):
    points = dict()

    circle = [0]
    curr = 0
    player = 1
    for i in range(1, marbles + 1):
        if i % 23 != 0:
            # If not a multiple of 23, just add
            j = get_insert_spot(curr, len(circle)) + 1
            circle.insert(j, i)
            curr = j
        else:
            # If a multiple of 23, keep marble
            points[player] = points.get(player, 0) + i

            # Also find marble 7 counter-clockwise and take it
            j = (curr - 7) % len(circle)
            curr = j
            m = circle.pop(j)
            points[player] = points.get(player, 0) + m
           
        # Move to next player
        player += 1
        if player > players:
            player = 1
    
    # Find max score
    max_score = 0
    for player, score in points.items():
        if score > max_score:
            max_score = score 
    print("Maximum score: {}".format(max_score))


if __name__ == '__main__':
    players = 473
    last_points = 70904
    game(players, last_points)
