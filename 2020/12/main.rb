module Actions
    MOVE_NORTH = 'N'.freeze
    MOVE_EAST = 'E'.freeze
    MOVE_SOUTH = 'S'.freeze
    MOVE_WEST = 'W'.freeze
    MOVE_FORWARD = 'F'.freeze
    ROTATE_RIGHT = 'R'.freeze
    ROTATE_LEFT = 'L'.freeze
end

def move(action, amount, row, col)
    if action == Actions::MOVE_EAST
        col += amount
    elsif action == Actions::MOVE_SOUTH
        row += amount
    elsif action == Actions::MOVE_WEST
        col -= amount
    elsif action == Actions::MOVE_NORTH
        row -= amount
    end
    return row, col
end

def execute_actions(actions)
    row = 0
    col = 0

    orientation = 0 # 0 => E, 1 => S, 2 => W, 3 => N
    directions = {
        0 => Actions::MOVE_EAST,
        1 => Actions::MOVE_SOUTH,
        2 => Actions::MOVE_WEST,
        3 => Actions::MOVE_NORTH
    }

    for i in 0...actions.length()
        action = actions[i][0]
        amount = Integer(actions[i][1...])
        if action == Actions::ROTATE_RIGHT
            delta = amount / 90
            orientation = (orientation + delta) % 4
        elsif action == Actions::ROTATE_LEFT
            delta = amount / 90
            orientation = (orientation - delta) % 4
        elsif action == Actions::MOVE_FORWARD
            direction = directions[orientation]
            row, col = move(direction, amount, row, col)
        else
            row, col = move(action, amount, row, col)
        end
    end

    puts "Final coordinations: row=#{row} col=#{col}"
    puts "Manhatten distance: #{row.abs + col.abs}"
end

def execute_actions_two(actions)
    row = 0
    col = 0
    waypoint_row = -1
    waypoint_col = 10

    for i in 0...actions.length()
        action = actions[i][0]
        amount = Integer(actions[i][1...])
        if action == Actions::MOVE_FORWARD
            row += amount * waypoint_row
            col += amount * waypoint_col
        elsif action == Actions::ROTATE_RIGHT
            times = amount / 90
            for _ in 0...times
                waypoint_row, waypoint_col = waypoint_col, -waypoint_row
            end
            
        elsif action == Actions::ROTATE_LEFT
            times = amount / 90
            for _ in 0...times
                waypoint_row, waypoint_col = -waypoint_col, waypoint_row 
            end
        else
            waypoint_row, waypoint_col = move(action, amount, waypoint_row, waypoint_col)
        end   
    end

    puts "Final coordinations: row=#{row} col=#{col}"
    puts "Manhatten distance: #{row.abs + col.abs}"
end

actions = []
File.open('./12.in') do |f|
    f.each_line do |line|
        actions.append(line)
    end
end

execute_actions(actions)
execute_actions_two(actions)
