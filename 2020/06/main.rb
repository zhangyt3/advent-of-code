require "set"

text = File.read("./06.in")
answers = text.split(/\n{2,}/).map{|p| p.split.join(" ")}

# Part 1
yes_count = 0
answers.each do |answer|
    seen = Set[]
    answer.split(" ").each do |answers_per_person|
        answers_per_person.chars.each do |letter|
            seen.add(letter)
        end
    end
    yes_count += seen.length()
end
puts "Yes count: #{yes_count}"

# Part 2
yes_count = 0
answers.each do |answer|
    sets = []
    answer.split(" ").each do |answers_per_person|
        seen = Set[]
        answers_per_person.chars.each do |letter|
            seen.add(letter)
        end
        sets.append(seen)
    end
    intersection = sets.inject(:&)
    yes_count += intersection.length()
end
puts "Yes count (intersection): #{yes_count}"
