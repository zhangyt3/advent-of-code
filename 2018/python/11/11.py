from pprint import pprint


# https://gist.github.com/SiestaMadokaist/74e573365a02f5d914d2
class SummedAreaTable(object):
    def __init__(self, size, data):
        """
        Just because I dislike a 2d array / list.
        data should be a List of Integer.
        """   
        width, height = size 
        assert width * height == len(data), "invalid data length and or data size"
        self.size = size 
        self.data = data    
        self.memo = [None for _ in range(width * height)]
        self.generate()  

    def get(self, x, y):
        """
        get the value of self, at point x, y.
        it's possible for the value at that point hadn't been generated.
        """
        width, height = self.size
        index = y * width + x    
        if(x < 0 or y < 0):
            # value at negative-indexed point is always 0
            return 0
        elif self.memo[index] is not None:
            # if the value at point x, y has already been generated
            return self.memo[index]
        else:
            # calculate the value at point x, y if it hasn't been generated
            cummulative = self.get(x - 1, y) + self.get(x, y - 1) - self.get(x - 1, y - 1) + self.data[index]
            self.memo[index] = cummulative
            return cummulative

    def total(self, x0, y0, x1, y1):
        """
        get the cummulative value of this instance from point (x0, y0) to (x1, y1)
        """
        a = self.get(x0 - 1, y0 - 1)
        b = self.get(x0 - 1, y1)
        c = self.get(x1, y0 - 1)
        d = self.get(x1, y1)
        return d - b - c + a

    def generate(self):    
        width, height = self.size      
        self.memo = [self.get(x, y) for y in range(height) for x in range(width)] 


def cell_power(x, y, serial_num):
    rack_id = x + 10
    power = rack_id * y 
    power += serial_num
    power *= rack_id
    if power < 100:
        power = 0
    else:
        power = (power // 100) % 10
    power -= 5
    return power


def initialize_grid(serial_num):
    grid = [[-1 for _ in range(300)] for _ in range(300)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] = cell_power(x + 1, y + 1, serial_num)
    return grid


if __name__ == '__main__':
    serial_num = 9445
    grid = initialize_grid(serial_num)
    
    summed = SummedAreaTable((300, 300), [x for row in grid for x in row])

    mx = 0
    my = 0
    max_power = 0
    size = 3
    for y in range(len(grid) - size):
            for x in range(len(grid[y]) - size):
                power = summed.total(x, y, x + size - 1, y + size - 1)
                if power > max_power:
                    max_power = power
                    mx = x
                    my = y
    print("Max power for size 3 is {} at x={}, y={}".format(max_power, mx + 1, my + 1))

    mx = 0
    my = 0
    max_power = 0
    best_size = 0
    for size in range(1, len(grid)):
        print("Size:", size)
        for y in range(len(grid) - size):
            for x in range(len(grid[y]) - size):
                power = summed.total(x, y, x + size - 1, y + size - 1)
                if power > max_power:
                    max_power = power
                    mx = x
                    my = y
                    best_size = size
    print("Max power for any size is {} at x={}, y={} with size={}".format(max_power, mx + 1, my + 1, best_size))
