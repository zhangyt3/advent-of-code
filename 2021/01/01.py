if __name__ == "__main__":
    with open("01.in") as file:
        lines = file.readlines()
        depths = [int(line.rstrip()) for line in lines]

        # Part 1
        increases = 0
        for i in range(1, len(depths)):
            if depths[i] > depths[i - 1]:
                increases += 1
        print(f"Increases: {increases}")

        # Part 2
        window_size = 3
        increases = 0
        for i in range(0, len(depths) - window_size):
            prev = sum(depths[i:i + window_size])
            next = sum(depths[i + 1:i + window_size +1])
            if next > prev:
                increases += 1
        print(f"Increases: {increases}")
