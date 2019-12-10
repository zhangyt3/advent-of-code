ROWS = 6
COLS = 25

BLACK = 0
WHITE = 1
TRANSPARENT = 2


def fill_layer(layer, nums, layer_num, cells_per_layer):
    start = layer_num * cells_per_layer
    for i in range(cells_per_layer):
        layer[i] = nums[start + i]

def count_zeros(layer):
    count = 0
    for num in layer:
        if num == 0:
            count += 1
    return count

def find_final_image(layers):
    final = [None for _ in range(len(layers[0]))]
    for i in range(len(layers[0])):
        final[i] = find_pixel_val(layers, i)
    return final

def find_pixel_val(layers, i):
    for layer in layers:
        if layer[i] != TRANSPARENT:
            return layer[i]

if __name__ == "__main__":
    nums = []
    with open('8.in') as f:
        nums = [int(x) for x in f.readline().strip()]

    cells_per_layer = ROWS * COLS
    num_layers = len(nums) // cells_per_layer

    print(f'Numbers: {len(nums)}')
    print(f'Cells per layer: {cells_per_layer}')
    print(f'Layers: {num_layers}')

    layers = [
        [None for _ in range(cells_per_layer)] for _ in range(num_layers)
    ]

    for i, layer in enumerate(layers):
        fill_layer(layer, nums, i, cells_per_layer)

    min_zeros = count_zeros(layers[0])
    best_layer = layers[0]
    for l in layers[1:]:
        zeros = count_zeros(l)
        if zeros < min_zeros:
            min_zeros = zeros
            best_layer = l

    ones = 0
    twos = 0
    for num in best_layer:
        if num == 1:
            ones += 1
        elif num == 2:
            twos += 1

    print(f'{ones * twos}')

    # PART 2
    image = find_final_image(layers)
    
    print("Raw:")
    for i in range(ROWS):
        for j in range(COLS):
            print(image[i * COLS + j], end='')
        print()

    print("Image:")
    for i in range(ROWS):
        for j in range(COLS):
            cell = image[i * COLS + j]
            if cell == BLACK:
                print(u'\u2588', end='')
            elif cell == WHITE:
                print(' ', end='')
        print()

