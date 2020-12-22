lines = []
File.open("./10.in") do |f|
    f.each_line do |line|
        lines.append(Integer(line))
    end
end

lines.sort!

# Part 1
one_jolt_diffs = 1
three_jolt_diffs = 1
for i in 0...(lines.length() - 1)
    diff = lines[i + 1] - lines[i]
    if diff == 1
        one_jolt_diffs += 1
    elsif diff == 3
        three_jolt_diffs += 1
    else
        puts "Not a 1 or 3 jolt difference"
    end
end
puts "1 jolt diffs (#{one_jolt_diffs}) x three jolt diffs (#{three_jolt_diffs}) = #{one_jolt_diffs * three_jolt_diffs}"

# Part 2
count = 1
i = 0
curr_count = 1
while i < lines.length()
    j = i + 1
    while j < lines.length()
        if lines[j] - lines[j - 1] == 1
            curr_count += 1
        else
            break
        end
        j += 1
    end

    if curr_count == 2
        count *= 2
    elsif curr_count == 3
        count *= 4
    elsif curr_count == 4
        count *= 7
    end

    curr_count = 0
    i = j
end
puts "# arrangements: #{count}"