if __name__ == "__main__":
    with open("02.in") as file:
        lines = file.readlines()
        commands = [line.split(" ") for line in lines]
        commands = list(map(lambda x: [x[0], int(x[1])], commands))

        horizontal = 0
        depth = 0
        for direction, magnitude in commands:
            if direction == "forward":
                horizontal += magnitude
            elif direction == "down":
                depth += magnitude
            elif direction == "up":
                depth -= magnitude
        print(f"Part 1: {horizontal * depth}")

        horizontal = 0
        depth = 0
        aim = 0
        for direction, magnitude in commands:
            if direction == "forward":
                horizontal += magnitude
                depth += aim * magnitude
            elif direction == "down":
                aim += magnitude
            elif direction == "up":
                aim -= magnitude
        print(f"Part 2: {horizontal * depth}")
