grid = []
File.open("./03.in") do |f|
    f.each_line do |line|
        if !line.empty?
            grid.append(line)
        end 
    end
end

def count_hits(drow, dcol, grid)
    i = 0
    j = 0
    hits = 0
    while i < grid.length()
        if grid[i][j] == "#"
            hits += 1
        end
        i = i + drow
        j = (j + dcol) % (grid[0].length() - 1)
    end
    return hits
end

# Part 1
puts "Trees encountered: #{count_hits(1, 3, grid)}"

# Part 2
combos = [
    [1, 1], [1, 3], [1, 5], [1, 7], [2, 1]
]
hits = []
combos.each do |drow, dcol|
    hits.append(count_hits(drow, dcol, grid))
    puts "Trees encountered with drow=#{drow}, dcol=#{dcol}: #{hits[-1]}"
end
puts "Answer: #{hits.inject(:*)}"
