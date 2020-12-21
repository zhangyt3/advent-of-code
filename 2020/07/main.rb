def parse_to_colors(str)
    str = str[...-1]

    colors = []
    str.split(",").each do |bag_num_color_pair_str|
        num = Integer(bag_num_color_pair_str[...2])
        color_bag = bag_num_color_pair_str[2...]
        color_bag.slice! " bags"
        color_bag.slice! " bag"
        colors.append([num, color_bag.strip])
    end

    return colors
end

def dfs(start_color, adjmap, memo)
    if memo.key?(start_color)
        return memo[start_color]
    end

    can_reach = false
    adjmap[start_color].each do |to_color|
        if to_color[1] == "shiny gold"
            can_reach = true
            break
        else
            can_reach = dfs(to_color[1], adjmap, memo)
            if can_reach
                break
            end
        end
    end

    memo[start_color] = can_reach
    return can_reach
end

def count_bags(start_color, adjmap, memo)
    if memo.key?(start_color)
        return memo[start_color]
    end

    count = 0
    adjmap[start_color].each do |num, col|
        count += num
        temp = count_bags(col, adjmap, memo)
        if temp != 0
            count += num * temp
        end
    end

    memo[start_color] = count
    return count
end

# color => list[color]
adjmap = {}
File.open("./07.in") do |f|
    f.each_line do |line|
        from_color, to_colors = line.split(" bags contain ")
        if to_colors.strip == "no other bags."
            adjmap[from_color] = []
        else
            adjmap[from_color] = parse_to_colors(to_colors.strip)
        end
    end
end

# Part 1
memo = {}  # color => boolean (can this color get to shiny gold or not?)
count = 0
adjmap.each do |start_color, _|
    if dfs(start_color, adjmap, memo)
        count += 1
    end
end
puts "#{count} bags can eventually have 1 shiny gold bag"

# Part 2
memo = {}  # color => number of bags it holds
count = count_bags("shiny gold", adjmap, memo)
puts "A shiny gold bag can contain #{count} bags"
