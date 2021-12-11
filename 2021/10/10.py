from pprint import pprint

starts = set(["(", "[", "{", "<"])
ends = set([")", "]", "}", ">"])
start_to_end = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
scores_two = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

if __name__ == "__main__":
    lines = []
    with open("10.in") as f:
        lines = [x.strip() for x in f.readlines()]

    completions = []
    score = 0
    for line in lines:
        stack = []
        corrupted = False
        for letter in line:
            if letter in starts:
                stack.append(letter)
            elif letter in ends:
                curr = stack.pop()
                if start_to_end.get(curr, "") != letter:
                    corrupted = True
                    score += scores[letter]
                    break
                
        if not corrupted:
            completions.append(list(map(lambda x: start_to_end[x], reversed(stack))))
    print(f"Score: {score}")

    scores = []
    for c in completions:
        score = 0
        for letter in c:
            score *= 5
            score += scores_two[letter]
        scores.append(score)
    scores = sorted(scores)
    print(f"Middle score: {scores[len(scores) // 2]}")
