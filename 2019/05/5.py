DONE = 99
ADD = 1  
MULTIPLY = 2
SAVE = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8

IMMEDIATE_MODE = "IMMEDIATE"
POSITION_MODE = "POSITION"


def get_values(nums, curr_pos, modes):
    res = []
    for i, mode in enumerate(modes):
        if mode == POSITION_MODE:
            res.append(get_value_positional(nums, curr_pos + 1 + i))
        else:
            res.append(get_value_immediate(nums, curr_pos + 1 + i))

    return res

def get_value_positional(nums, pos):
    idx = nums[pos]
    return nums[idx]

def get_value_immediate(nums, pos):
    return nums[pos]

def parse_opcode_and_modes(code):
    code = str(code)
    opcode = int(code[-2:])

    modes = [POSITION_MODE, POSITION_MODE, POSITION_MODE]
    if opcode == SAVE or opcode == OUTPUT:
        modes = [POSITION_MODE]
    elif opcode == JUMP_IF_FALSE or JUMP_IF_TRUE:
        modes = [POSITION_MODE, POSITION_MODE]
    
    for i in range(len(code) - 2):
        letter = code[(-3-i)]
        if letter == '0':
            modes[i] = POSITION_MODE
        elif letter == '1':
            modes[i] = IMMEDIATE_MODE
        else:
            print("rip")
        
    return opcode, modes

def run(nums):
    curr_pos = 0
    while True:
        opcode, modes = parse_opcode_and_modes(nums[curr_pos])

        if opcode == DONE:
            break
        elif opcode == ADD:
            x, y = get_values(nums, curr_pos, modes)
            dest = nums[curr_pos + 3]
            nums[dest] = x + y
            curr_pos += 4
        elif opcode == MULTIPLY:
            x, y = get_values(nums, curr_pos, modes)
            dest = nums[curr_pos + 3]
            nums[dest] = x * y
            curr_pos += 4
        elif opcode == SAVE:
            input_val = input("Enter an input value: ")
            dest = nums[curr_pos + 3]
            nums[dest] = int(input_val)
            curr_pos += 2
        elif opcode == OUTPUT:
            output_val = get_values(nums, curr_pos, modes)
            print(f"Output: {output_val}")
            curr_pos += 2
        elif opcode == JUMP_IF_TRUE:
            x, y = get_values(nums, curr_pos, modes)
            if x != 0:
                curr_pos = y
            else:
                curr_pos += 3
        elif opcode == JUMP_IF_FALSE:
            x, y, = get_values(nums, curr_pos, modes)
            if x == 0:
                curr_pos = y
            else:
                curr_pos += 3
        elif opcode == LESS_THAN:
            x, y = get_values(nums, curr_pos, modes)
            dest = nums[curr_pos + 3]
            if x < y:
                nums[dest] = 1
            else:
                nums[dest] = 0
            curr_pos += 4
        elif opcode == EQUALS:
            x, y = get_values(nums, curr_pos, modes)
            dest = nums[curr_pos + 3]
            if x == y:
                nums[dest] = 1
            else:
                nums[dest] = 0
            curr_pos += 4

    return nums[0]

if __name__ == '__main__':
    nums = []
    with open('5.in') as f:
        nums = [int(x) for x in f.readline().split(',')]

    run(nums)