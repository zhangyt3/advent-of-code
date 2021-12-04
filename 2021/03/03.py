def to_decimal(bits):
    power = 0
    res = 0
    for bit in reversed(bits):
        if bit == 1:
            res += 2**power
        power += 1
    return res

def calc_gamma_and_epsilon(lines):
    bits_gamma = []
    bits_epsilon = []
    rows = len(lines)
    cols = len(lines[0])
    for j in range(0, cols):
        ones = 0
        zeros = 0
        for i in range(0, rows):
            if lines[i][j] == "1":
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            bits_gamma.append(1)
            bits_epsilon.append(0)
        else:
            bits_gamma.append(0)
            bits_epsilon.append(1)
    return to_decimal(bits_gamma), to_decimal(bits_epsilon)

def calc_rating(lines, oxygen=True):
    cols = len(lines[0])
    for j in range(0, cols):
        if len(lines) == 1:
            break
        ones = 0
        zeros = 0
        for i in range(0, len(lines)):
            if lines[i][j] == "1":
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            lines = list(filter(lambda line: line[j] == "1", lines)) if oxygen else list(filter(lambda line: line[j] == "0", lines))
        else:
            lines = list(filter(lambda line: line[j] == "0", lines)) if oxygen else list(filter(lambda line: line[j] == "1", lines))
    return to_decimal([int(x) for x in lines[0]])
     
if __name__ == "__main__":
    with open("03.in") as file:
        lines = [x.strip() for x in file.readlines()]

        # Part 1
        gamma, epsilon = calc_gamma_and_epsilon(lines)
        power = gamma * epsilon
        print(f"Power consumption: {power}")

        # Part 2
        oxygen = calc_rating(lines, oxygen=True)
        scrubbing = calc_rating(lines, oxygen=False)
        print(f"Life support rating: {oxygen * scrubbing}")
