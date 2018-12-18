import sys
import matplotlib.pyplot as plt 


xs = []
ys = []
vels = []
for line in sys.stdin:
    line = line.strip()

    x = int(line[10:16])
    y = -int(line[17:24])
    xs.append(x)
    ys.append(y)

    dx = int(line[-7:-5])
    dy = -int(line[-3:-1])
    vels.append((dx, dy))

# Show initial arrangement
time = 0
plt.scatter(xs, ys)
plt.show()

# Fast forward to the intersting part
SPEED_UP = 250
for i in range(len(xs)):
    dx, dy = vels[i]
    xs[i] += dx * SPEED_UP * 43
    ys[i] += dy * SPEED_UP * 43
time += SPEED_UP * 43

# Walk through each frame...
SPEED_UP = 1
while True:
    # Update positions
    for i in range(len(xs)):
        dx, dy = vels[i]
        xs[i] += dx * SPEED_UP
        ys[i] += dy * SPEED_UP

    # Print time of each frame for part 2 (answer is 10813)
    time += SPEED_UP
    print(time)
    
    # Show
    plt.scatter(xs, ys)
    plt.show()


    
