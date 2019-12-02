DONE = 99
ADD = 1    
MULTIPLY = 2

def get_values(nums, curr_pos):
    idx1 = nums[curr_pos + 1]
    x = nums[idx1]

    idx2 = nums[curr_pos + 2]
    y = nums[idx2]

    return x, y

def part1(nums, a, b):
    nums[1] = a
    nums[2] = b

    curr_pos = 0
    while nums[curr_pos] != DONE:
        opcode = nums[curr_pos]

        if opcode != ADD and opcode != MULTIPLY:
            print("Opps")
            print(nums)
            break
        else:
            x, y = get_values(nums, curr_pos)
            dest = nums[curr_pos + 3]

            if opcode == ADD:
                res = x + y
            elif opcode == MULTIPLY:
                res = x * y

            nums[dest] = res
            curr_pos += 4

    return nums[0]

if __name__ == '__main__':
    nums = []
    with open('2.in') as f:
        nums = [int(x) for x in f.readline().split(',')]
    
    for noun in range(100):
        for verb in range(100):
            output = part1(nums[:], noun, verb)
            if output == 19690720:
                print(f"noun={noun}, verb={verb}")
                print(100 * noun + verb)
                break
   