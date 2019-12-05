start = 359282
end = 820401

def two_adjacent_digits(num):
    num = str(num)
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            return True
    return False

def just_two_adjacent_digits(num):
    num = str(num)
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            if i == 0 or (i - 1 >= 0 and num[i - 1] != num[i]):
                if i + 2 == len(num) or (i + 2 < len(num) and num[i + 2] != num[i]):
                    return True
    return False

def never_decreases(num):
    num = str(num)
    for i in range(len(num) - 1):
        if int(num[i + 1]) < int(num[i]):
            return False
    return True

if __name__ == "__main__":
    count = 0
    for num in range(start, end + 1):
        if two_adjacent_digits(num) and never_decreases(num):
            count += 1
    print(count)

    count = 0
    for num in range(start, end + 1):
        if just_two_adjacent_digits(num) and never_decreases(num):
            count += 1
    print(count)
