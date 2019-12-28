from pprint import pprint

DONE = 99
ADD = 1
MULTIPLY = 2
SAVE = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJUST_REL_BASE = 9

ARG_DATA = {
    DONE: (),
    ADD: ('R', 'R', 'W'),
    MULTIPLY: ('R', 'R', 'W'),
    SAVE: ('W'),
    OUTPUT: ('R'),
    JUMP_IF_TRUE: ('R', 'R'),
    JUMP_IF_FALSE: ('R', 'R'),
    LESS_THAN: ('R', 'R', 'W'),
    EQUALS: ('R', 'R', 'W'),
    ADJUST_REL_BASE: ('R')
}

IMMEDIATE_MODE = "IMMEDIATE"
POSITION_MODE = "POSITION"
RELATIVE_MODE = "RELATIVE"

class Computer:
    def __init__(self, code):
        self.pos = 0
        self.base = 0

        self.mem = dict()
        for i, val in enumerate(code):
            self.mem[i] = val
        
        self.out = []
    
    def get_value(self, i):
        return self.mem.get(i, 0)
       
    def get_value_positional(self, i):
        i = self.get_value(i)
        return self.get_value(i)
    
    def get_value_relative(self, i):
        i = self.base + self.get_value(i)
        return self.get_value(i)
    
    def parse(self, op):
        op = str(op)
        opcode = int(op[-2:])

        arg_data = ARG_DATA[opcode]
        modes = [POSITION_MODE] * len(ARG_DATA[opcode])
        raw_modes = reversed(op[:-2])
        for i, val in enumerate(raw_modes):
            if val == '0':
                modes[i] = POSITION_MODE
            elif val == '1' and arg_data[i] == 'R':
                modes[i] = IMMEDIATE_MODE
            elif val == '2':
                modes[i] = RELATIVE_MODE
            else:
                raise Exception(f"Invalid parameter mode {val}: \narg_data: {arg_data} \nopcode: {opcode}")

        return opcode, modes
    
    def get_parameters(self, opcode, modes, pos):
        params = []

        arg_data = ARG_DATA[opcode]
        for i, mode in enumerate(modes):
            curr = pos + i + 1
            if mode == POSITION_MODE:
                if arg_data[i] == 'R':
                    params.append(self.get_value_positional(curr))
                else:
                    params.append(self.get_value(curr))
            elif mode == IMMEDIATE_MODE:
                params.append(self.get_value(curr))
            elif mode == RELATIVE_MODE:
                if arg_data[i] == 'R':
                    params.append(self.get_value_relative(curr))
                else:
                    params.append(self.get_value(curr) + self.base)
            else:
                raise Exception(f"Invalid parameter mode {mode}")      
        return params 

    def get_step_size(self, instruction):
        return len(ARG_DATA[instruction]) + 1
    
    def add(self, params):
        x, y, dest = params
        self.mem[dest] = x + y
        self.pos += self.get_step_size(ADD)
    
    def multiply(self, params):
        x, y, dest = params
        self.mem[dest] = x * y
        self.pos += self.get_step_size(MULTIPLY)
    
    def save(self, params, input_val):
        dest = params[0]
        self.mem[dest] = input_val
        self.pos += self.get_step_size(SAVE)
    
    def output(self, params):
        val = params[0]
        # print(f'Output value: {val}')
        self.pos += self.get_step_size(OUTPUT)

        self.out.append(val)
        if len(self.out) == 2:
            res = self.out
            self.out = []
            return res
        else:
            return None

    def jump_if_true(self, params):
        x, y = params
        if x != 0:
            self.pos = y
        else:
            self.pos += self.get_step_size(JUMP_IF_TRUE)
    
    def jump_if_false(self, params):
        x, y = params
        if x == 0:
            self.pos = y
        else:
            self.pos += self.get_step_size(JUMP_IF_FALSE)
    
    def less_than(self, params):
        x, y, dest = params
        if x < y:
            self.mem[dest] = 1
        else:
            self.mem[dest] = 0
        self.pos += self.get_step_size(LESS_THAN)
    
    def equals(self, params):
        x, y, dest = params
        if x == y:
            self.mem[dest] = 1
        else:
            self.mem[dest] = 0
        self.pos += self.get_step_size(EQUALS)
    
    def adjust_rel_base(self, params):
        dbase = params[0]
        self.base += dbase
        self.pos += self.get_step_size(ADJUST_REL_BASE)
    
    def run(self, input_val):
        while True:
            opcode, modes = self.parse(self.get_value(self.pos))
            params = self.get_parameters(opcode, modes, self.pos)
            
            if opcode == DONE:
                break
            elif opcode == ADD:
                self.add(params)
            elif opcode == MULTIPLY:
                self.multiply(params)
            elif opcode == SAVE:
                self.save(params, input_val)
            elif opcode == OUTPUT:
                res = self.output(params)
                if res:
                    return res
            elif opcode == JUMP_IF_TRUE:
                self.jump_if_true(params)
            elif opcode == JUMP_IF_FALSE:
                self.jump_if_false(params)
            elif opcode == LESS_THAN:
                self.less_than(params)
            elif opcode == EQUALS:
                self.equals(params)
            elif opcode == ADJUST_REL_BASE:
                self.adjust_rel_base(params)
            else:
                raise Exception(f"Invalid opcode {opcode}")
        
        return "DONE"

# Color input/output
BLACK = 0
WHITE = 1

# Direction output
LEFT = 0
RIGHT = 1

MOVES = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

class Robot:
    def __init__(self, code, grid, row, col, orientation):
        self.comp = Computer(code)
        self.grid = grid
        self.row = row
        self.col = col
        self.orientation = orientation
    
    def turn(self, turn_dir):
        dirs = ["UP", "RIGHT", "DOWN", "LEFT"]
        i = dirs.index(self.orientation)

        if turn_dir == LEFT:
            i = (i - 1) % 4
        elif turn_dir == RIGHT:
            i = (i + 1) % 4
        else:
            raise Exception(f"Invalid turn direction: {turn_dir}")

        self.orientation = dirs[i]
    
    def forward(self):
        drow, dcol = MOVES[self.orientation]
        nrow = self.row + drow
        ncol = self.col + dcol

        if nrow < 0 or ncol < 0 or nrow > len(self.grid) or ncol > len(self.grid[0]):
            raise Exception("Robot fell off grid")
        
        self.row = nrow
        self.col = ncol
        
    def paint(self):
        painted = set()
        i = 0
        while True:
            color = self.grid[self.row][self.col]
            res = self.comp.run(color)
            if res == "DONE":
                break
            
            output_color, turn_dir = res
            grid[self.row][self.col] = output_color
            painted.add((self.row, self.col))

            self.turn(turn_dir)
            self.forward()
            i += 1
        
        print(f"Painted {i + 1} times")
        print(f"Painted {len(painted)} unique cells")


if __name__ == "__main__":
    code = []
    with open('paint.intcode') as f:
        code = [int(x) for x in f.readline().split(',')]
    
    SIZE = 100
    grid = [[BLACK for _ in range(SIZE)] for _ in range(SIZE)]
    grid[SIZE // 2][SIZE // 2] = WHITE
    robot = Robot(code, grid, SIZE // 2, SIZE // 2, "UP")
    robot.paint()

    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == WHITE:
                print(' ', end='')
            else:
                print(u"\u25A0", end='')
        print()
