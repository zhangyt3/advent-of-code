passwords = []
File.open("./02.in") do |f|
    f.each_line do |line|
        policy, password = line.split(":").map(&:strip)
        range, letter = policy.split(" ")
        low, high = range.split("-")
        passwords.append([password, letter, Integer(low), Integer(high)])
    end
end

# Part 1
valid = 0
passwords.each do |password, letter, low, high| 
    letterCount = password.count(letter)
    if low <= letterCount && letterCount <= high
        valid += 1
    end
end
puts "Valid passwords: #{valid}"

# Part 2
valid = 0
passwords.each do |password, letter, i, j|
    first = password[i - 1]
    second = password[j - 1]
    if ((letter == first || letter == second) && first != second) 
        valid += 1
    end
end
puts "Valid passwords: #{valid}"
