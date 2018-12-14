import sys

nums = []
for line in sys.stdin:
    if line[0] == "+":
        x = int(line[1:])
    else:
        x = -int(line[1:])
    nums.append(x)

seen = set()
freq = 0
while True:
    for num in nums:
        freq += num
        if freq in seen:
            print(freq)
            sys.exit()
        
        seen.add(freq)
