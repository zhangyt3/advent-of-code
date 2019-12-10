from itertools import permutations

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

class Computer:
    def __init__(self, program, phase):
        self.program = program
        self.phase = phase
        self.input_count = 0
        self.curr_pos = 0

    def get_values(self, modes):
        res = []
        for i, mode in enumerate(modes):
            if mode == POSITION_MODE:
                res.append(self.get_value_positional(self.curr_pos + 1 + i))
            else:
                res.append(self.get_value_immediate(self.curr_pos + 1 + i))

        return res

    def get_value_positional(self, pos):
        idx = self.program[pos]
        return self.program[idx]

    def get_value_immediate(self, pos):
        return self.program[pos]

    def parse_opcode_and_modes(self, code):
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

    def run(self, input_val):
        while True:
            opcode, modes = self.parse_opcode_and_modes(self.program[self.curr_pos])

            if opcode == DONE:
                break
            elif opcode == ADD:
                x, y = self.get_values(modes)
                dest = self.program[self.curr_pos + 3]
                self.program[dest] = x + y
                self.curr_pos += 4
            elif opcode == MULTIPLY:
                x, y = self.get_values(modes)
                dest = self.program[self.curr_pos + 3]
                self.program[dest] = x * y
                self.curr_pos += 4
            elif opcode == SAVE:
                dest = self.program[self.curr_pos + 1]
                if self.input_count == 0:
                    self.program[dest] = self.phase
                    self.input_count += 1
                else:
                    self.program[dest] = input_val
                    self.input_count += 1
                self.curr_pos += 2
            elif opcode == OUTPUT:
                output_val = self.get_values(modes)
                self.curr_pos += 2
                return output_val[0]
            elif opcode == JUMP_IF_TRUE:
                x, y = self.get_values(modes)
                if x != 0:
                    self.curr_pos = y
                else:
                    self.curr_pos += 3
            elif opcode == JUMP_IF_FALSE:
                x, y, = self.get_values(modes)
                if x == 0:
                    self.curr_pos = y
                else:
                    self.curr_pos += 3
            elif opcode == LESS_THAN:
                x, y = self.get_values(modes)
                dest = self.program[self.curr_pos + 3]
                if x < y:
                    self.program[dest] = 1
                else:
                    self.program[dest] = 0
                self.curr_pos += 4
            elif opcode == EQUALS:
                x, y = self.get_values(modes)
                dest = self.program[self.curr_pos + 3]
                if x == y:
                    self.program[dest] = 1
                else:
                    self.program[dest] = 0
                self.curr_pos += 4

        return "DONE"

def process_permutation(phases, nums):
    max_output = 0

    comps = []
    for phase in phases:
        comps.append(Computer(nums[:], phase))

    signal = 0
    from_e = 0
    i = 0
    while True:
        c = comps[i]

        temp = c.run(signal)
        # print(f'Output from computer {i}: {temp}')
        if temp == "DONE":
            break
        else:
            signal = temp

        if i == len(comps) - 1:
            from_e = signal
            max_output = max(max_output, from_e)
        i = (i + 1) % len(comps)

    return max_output


if __name__ == '__main__':
    nums = []
    with open('7.in') as f:
        nums = [int(x) for x in f.readline().split(',')]
    print(nums)

    perms = permutations([5, 6, 7, 8, 9])

    max_output = 0
    for i, perm in enumerate(perms):
        signal = process_permutation(perm, nums)
        print(f'Signal from permutation {i}: {signal}')

        max_output = max(max_output, signal)

    print(f'{max_output}')

