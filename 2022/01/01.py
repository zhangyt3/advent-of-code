if __name__ == "__main__":
    with open("01.in") as file:
        lines = file.readlines()
        calories = []
        curr = 0
        for line in lines:
            if line.strip() == '':
                calories.append(curr)
                curr = 0
            else:
                curr += int(line.strip())
        
        print(f"Max calories: {max(calories)}")

        calories = sorted(calories)
        top_three = calories[-3:]
        print(f"Sum of top three: {sum(top_three)}")
