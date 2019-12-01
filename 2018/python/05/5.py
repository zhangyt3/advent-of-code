def should_remove(x, y):
    return x != y and (x.lower() == y or x == y.lower())


line = input()

def react_polymer(polymer):
    changed = True
    while changed:
        #print(len(polymer))
        #print(polymer[:20])
        changed = False
        temp = ""
        i = 0
        while i < len(polymer) - 1:
            first = polymer[i]
            second = polymer[i + 1]
            #if should_remove(first, second):
            #    print(first, second, should_remove(first, second))
            if not should_remove(first, second):
                temp += first
                i += 1
            else:
                changed = True
                i += 2  
        if i == len(polymer) - 1:
            # Check last 2 letters
            first = polymer[-2]
            second = polymer[-1]
            if not should_remove(first, second):
                temp += polymer[-1]
        polymer = temp
    return polymer
    
alphabet = 'abcdefghijklmnopqrstuvwxyz'

min_len = 2193810293829210
for letter in alphabet:
    poly = ""
    for x in line:
        if x.lower() != letter:
            poly += x
    
    poly = react_polymer(poly)
    print(letter, len(poly))
    if len(poly) < min_len:
        min_len = len(poly)

print("Min length:", min_len)