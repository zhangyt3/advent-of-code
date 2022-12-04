priorities = dict()
for i in range(26):
    code = i + 65
    priorities[chr(code)] = code - 38
for i in range(26):
    code = i + 97
    priorities[chr(code)] = code - 96
    
if __name__ == "__main__":
    with open("03.in") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

        duplicated = []
        for line in lines:
            mid = len(line) // 2
            first = line[:mid]
            second = set(line[mid:])

            for letter in first:
                if letter in second:
                    duplicated.append(letter)
                    break
            
        answer = 0
        for letter in duplicated:
            answer += priorities[letter]
        print(answer)

        # Part 2
        badges = []
        for i in range(0, len(lines) - 2, 3):
            first = lines[i]
            second = lines[i + 1]
            third = lines[i + 2]

            found = None
            for x in first:
                for y in second:
                    for z in third:
                        if x == y and y == z:
                            found = x
            badges.append(found)
        
        answer = 0
        for letter in badges:
            answer += priorities[letter]
        print(answer)
        
  
