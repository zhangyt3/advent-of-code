require "set"

text = File.read("./04.in")
text = text.split(/\n{2,}/).map{|p| p.split.join(" ")}
passports = []
for i in 0...text.length()
    entries = text[i].split(" ")
    entries = entries.map{|entry| entry.split(":")}
    p = {}
    entries.each do |key, value|
        p[key] = value
    end
    passports.append(p)
end

def check_byr(byr)
    return byr.length() == 4 && 1920 <= Integer(byr) && Integer(byr) <= 2002
end

def check_iyr(iyr)
    return iyr.length() == 4 && 2010 <= Integer(iyr) && Integer(iyr) <= 2020
end

def check_eyr(eyr)
    return eyr.length() == 4 && 2020 <= Integer(eyr) && Integer(eyr) <= 2030
end

def check_hgt(hgt)
    puts hgt
    num = Integer(hgt[0...-2])
    unit = hgt[-2...]
    if unit == "cm"
        return 150 <= num && num <= 193
    elsif unit == "in"
        return 59 <= num && num <= 76
    end
    return false    
end

def check_hcl(hcl)
    return /(?<=#)(?<!^)\h{6}/.match(hcl)
end

def check_ecl(ecl)
    colors = Set["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return colors.include?(ecl)
end

def check_pid(pid)
    return /\A\d{9}\z/.match(pid)
end

checks = {
    "byr" => method(:check_byr),
    "iyr" => method(:check_iyr),
    "eyr" => method(:check_eyr),
    "hgt" => method(:check_hgt),
    "hcl" => method(:check_hcl),
    "ecl" => method(:check_ecl),
    "pid" => method(:check_pid)
}

valid = 0
passports.each do |p|
    good = true
    checks.each do |key, check|
        puts key, check
        if !p.include?(key) || !check.call(p[key])
            good = false
            break
        end
    end
    if good
        valid += 1
    end
end
puts "Valid passports: #{valid}"