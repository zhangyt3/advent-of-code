encoding = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

shape_scores = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}

outcome_scores = {
    "LOST": 0,
    "DRAW": 3,
    "WON": 6
}

def did_you_win(your_shape, opponent_shape):
    if your_shape == opponent_shape:
        return "DRAW"
    
    if (your_shape == "ROCK" and opponent_shape == "SCISSORS") or (your_shape == "SCISSORS" and opponent_shape == "PAPER") or (your_shape == "PAPER" and opponent_shape == "ROCK"):
        return "WON"
    
    return "LOST"

outcome_encoding = {
    "X": "LOST",
    "Y": "DRAW",
    "Z": "WON"
}

def calculate_needed_shape(outcome, opponent_shape):
    if outcome == "DRAW":
        return opponent_shape
    elif outcome == "WON":
        if opponent_shape == "ROCK":
            return "PAPER"
        elif opponent_shape == "PAPER":
            return "SCISSORS"
        else:
            return "ROCK"
    else:
        if opponent_shape == "ROCK":
            return "SCISSORS"
        elif opponent_shape == "PAPER":
            return "ROCK"
        else:
            return "PAPER"

if __name__ == "__main__":
    with open("02.in") as file:
        lines = file.readlines()
        
        score = 0
        for line in lines:
            opponent, you = line.strip().split(" ")

            your_shape = encoding[you]
            score += shape_scores[your_shape]

            opponent_shape = encoding[opponent]
            outcome = did_you_win(your_shape, opponent_shape)
            score += outcome_scores[outcome]
        
        print(f"Score: {score}")
        
        # Part 2
        score = 0
        for line in lines:
            opponent, outcome = line.strip().split(" ")

            outcome = outcome_encoding[outcome]
            score += outcome_scores[outcome]

            opponent_shape = encoding[opponent]
            your_shape = calculate_needed_shape(outcome, opponent_shape)
            score += shape_scores[your_shape]
        
        print(f"Score: {score}")
