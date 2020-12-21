require "set"

def generate_valids(nums, low, high)
    valids = Set[]
    for i in low...high
        for j in (i + 1)...high
            valids.add(nums[i] + nums[j])
        end
    end
    return valids
end

def find_invalid_num(nums, length)
    valids = generate_valids(nums, 0, length)
    for i in length...(nums.length() - 1)
        curr = nums[i]
        if !valids.include?(curr)
            return curr
        end
        valids = generate_valids(nums, i - length + 1, i + 1)
    end
end

def find_weakness(nums, target)
    for i in 0...nums.length()
        if nums[i] == target
            return 2 * nums[i]
        end

        curr = nums[i]
        for j in (i + 1)...nums.length()
            curr += nums[j]
            if curr == target
                return nums[i..j].min + nums[i..j].max
            end
        end
    end
end

lines = []
File.open("./09.in") do |f|
    f.each_line do |line|
        lines.append(Integer(line))
    end
end

length = 25

# Part 1
first_invalid = find_invalid_num(lines, length)
puts "First invalid number: #{first_invalid}"

# Part 2
weakness = find_weakness(lines, first_invalid)
puts "Encryption weakness: #{weakness}"
