import sys

freq = 0
for line in sys.stdin:
    if line[0] == "+":
        x = int(line[1:])
    else:
        x = -int(line[1:])

    freq += x

print("Final:", freq)    

