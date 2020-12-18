require "set"

passes = []
File.open("./05.in") do |f|
    f.each_line do |line|
        if !line.empty?
            passes.append(line)
        end 
    end
end

def bsearch(sequence)
    low = 0
    high = 2**sequence.length()
    i = 0
    while i < sequence.length()
        mid = (low + high) / 2
        if Set["L", "F"].include?(sequence[i])
            high = mid
        else
            low = mid
        end
        i += 1
    end
    return low
end

def calc_seat_id(row, col)
    return (8 * row) + col
end

# Part 1
highest = 0
passes.each do |pass|
    rowcode = pass[0...7].strip
    colcode = pass[7...].strip
    r = bsearch(rowcode)
    c = bsearch(colcode)
    highest = [highest, calc_seat_id(r, c)].max
end
puts "Highest seat id: #{highest}"

# Part 2
ids = []
passes.each do |pass|
    rowcode = pass[0...7].strip
    colcode = pass[7...].strip
    r = bsearch(rowcode)
    c = bsearch(colcode)
    id = calc_seat_id(r, c)
    ids.append(id)
end
ids = ids.sort

for i in 0...(ids.length() - 1)
    if ids[i + 1] != ids[i] + 1
        puts "Your seat id: #{ids[i] + 1}"
        break
    end
end