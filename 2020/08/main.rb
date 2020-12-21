require "set"

module Operations
    NOOP = "nop"
    ACCUMULATE = "acc"
    JUMP = "jmp"
end

def run(instructions)
    already_run = Set[]
    acc = 0
    i = 0
    while i < instructions.length()
        if already_run.include?(i)
            # puts "acc=#{acc} before running same instruction twice."
            return false
        end

        already_run.add(i)
        op, offset = instructions[i]

        case op
        when Operations::NOOP
            i += 1
        when Operations::ACCUMULATE
            acc += offset
            i += 1
        when Operations::JUMP
            i += offset
        end
    end

    return acc
end

def copy_instructions(instructions)
    copy = []
    instructions.each do |instruction|
        copy.append(instruction.dup)
    end
    return copy
end

instructions = []
File.open("./08.in") do |f|
    f.each_line do |line|
        op, offset = line.split(" ")
        instructions.append([op.strip, Integer(offset.strip)])
    end
end

for line in 0...instructions.length()
    op, val = instructions[line]
    if op == Operations::NOOP 
        copy = copy_instructions(instructions)
        copy[line][0] = Operations::JUMP
        res = run(copy)
        if res
            puts "Changing line #{line} from nop to jmp termiantes with acc=#{res}"
        end
    elsif op == Operations::JUMP
        copy = copy_instructions(instructions)
        copy[line][0] = Operations::NOOP
        res = run(copy)
        if res
            puts "Changing line #{line} from jmp to nop termiantes with acc=#{res}"
        end
    end
end
