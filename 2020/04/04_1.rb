require "set"

text = File.read("./04.in")
passports = text.split(/\n{2,}/).map{|p| p.split.join(" ")}
for i in 0...passports.length()
    entries = passports[i].split(" ")
    keys = entries.map{|entry| entry.split(":")[0]}
    passports[i] = keys.to_set
end

required = ["byr", "iyr", "eyr" , "hgt", "hcl" , "ecl", "pid"]
valid = 0
passports.each do |p|
    good = true
    required.each do |req|
        if !p.include?(req)
            good = false
            break
        end
    end
    if good
        valid += 1
    end
end
puts "Valid passports: #{valid}"