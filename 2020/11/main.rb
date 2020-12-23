grid = []
File.open('./11.in') do |f|
  f.each_line do |line|
    grid.append(line)
  end
end

def count_adjacent(grid, row, col)
  moves = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
  neighbours = 0
  moves.each do |drow, dcol|
    next unless row + drow >= 0 && row + drow < grid.length && col + dcol >= 0 && col + dcol < grid[0].length

    neighbours += 1 if grid[row + drow][col + dcol] == '#'
  end
  neighbours
end

def count_seen(grid, row, col)
  directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
  seen = 0

  # For each direction, keep going until you see a seat or reach the edge
  directions.each do |drow, dcol|
    curr_row = row + drow
    curr_col = col + dcol
    while curr_row >= 0 && curr_row < grid.length && curr_col >= 0 && curr_col < grid[0].length
      curr = grid[curr_row][curr_col]
      if curr == '#'
        seen += 1
        break
      elsif curr == 'L'
        break
      end
      curr_row += drow
      curr_col += dcol
    end
  end

  seen
end

def simulate(grid)
  old_grid = Marshal.load(Marshal.dump(grid))
  changed = true

  while changed
    new_grid = Marshal.load(Marshal.dump(old_grid))
    changed = false
    (0...old_grid.length).each do |row|
      (0...old_grid[row].length).each do |col|
        neighbours = count_adjacent(old_grid, row, col)
        if old_grid[row][col] == 'L' && neighbours == 0
          new_grid[row][col] = '#'
          changed = true
        elsif old_grid[row][col] == '#' && neighbours >= 4
          new_grid[row][col] = 'L'
          changed = true
        end
      end
    end
    old_grid = new_grid
  end

  new_grid
end

def simulate_seen(grid)
  old_grid = Marshal.load(Marshal.dump(grid))
  changed = true

  while changed
    new_grid = Marshal.load(Marshal.dump(old_grid))
    changed = false
    (0...old_grid.length).each do |row|
      (0...old_grid[row].length).each do |col|
        seen = count_seen(old_grid, row, col)
        if old_grid[row][col] == 'L' && seen == 0
          new_grid[row][col] = '#'
          changed = true
        elsif old_grid[row][col] == '#' && seen >= 5
          new_grid[row][col] = 'L'
          changed = true
        end
      end
    end
    old_grid = new_grid
  end

  new_grid
end

def count_filled_seats(grid)
  count = 0
  (0...grid.length).each do |i|
    (0...grid[i].length).each do |j|
      count += 1 if grid[i][j] == '#'
    end
  end
  count
end

# Part 1
final_grid = simulate(grid)
count = count_filled_seats(final_grid)
puts "Filled seats: #{count}"

# Part 2
final_grid = simulate_seen(grid)
count = count_filled_seats(final_grid)
puts "Part 2 filled seats: #{count}"
