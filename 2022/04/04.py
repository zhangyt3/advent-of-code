if __name__ == "__main__":
    with open("04.in") as file:
        lines = file.readlines()

        count = 0
        for line in lines:
            line = line.strip()
            first, second = line.split(",")
            low1, high1 = [int(x) for x in first.split("-")]
            low2, high2 = [int(x) for x in second.split("-")]

            if (low1 <= low2 and high2 <= high1) or (low2 <= low1 and high1 <= high2):
                count += 1
        print(count) 

        count = 0
        for line in lines:
            line = line.strip()
            first, second = line.split(",")
            low1, high1 = [int(x) for x in first.split("-")]
            low2, high2 = [int(x) for x in second.split("-")]
            if (low1 <= low2 and high1 >= low2) or (low2 <= low1 and high2 >= low1):
                count += 1
        print(count)
        

