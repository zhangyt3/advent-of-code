import sys

twos = 0
threes = 0
for line in sys.stdin:
    count = dict()
    for letter in line:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    seen_two = False
    seen_three = False
    for letter, times in count.items():
        if times == 2 and not seen_two:
            twos += 1
            seen_two = True
        elif times == 3 and not seen_three:
            threes += 1
            seen_three = True

print(twos * threes)

