use std::io::{self, BufRead};

fn main() {
    // Part 1
    let mut rectangles = Vec::new();
    let mut max_row: usize = 0;
    let mut max_col: usize = 0;

    // Read input and store (i, j, height, width) - id will be index + 1.
    // Also keep track of max i and j.
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let line = line.unwrap();

        let tokens: Vec<&str> = line.split(" ").collect(); // #id, @, (j, i), (width x height)
        
        let coords: Vec<&str> = tokens[2].split(",").collect();
        let j = coords[0].parse::<usize>().unwrap();
        let last_index = coords[1].len() - 1;
        let i = coords[1][..last_index].parse::<usize>().unwrap();

        let dims: Vec<&str> = tokens[3].split("x").collect();
        let width = dims[0].parse::<usize>().unwrap();
        let height = dims[1].parse::<usize>().unwrap();

        if i + height > max_row {
            max_row = i + height;
        }
        if j + width > max_col {
            max_col = j + width;
        }

        rectangles.push((i, j, height, width));
    }

    println!("Max row: {}, max col: {}", max_row, max_col);

    // Create grid with size (max i, max j)
    let mut grid = vec![vec![0; max_row + 1]; max_col + 1];

    // Process each rectangle (+1 to each cell the rectangle is on)
    for rect in rectangles.iter() {
        let (i, j, height, width) = *rect;
        for y in i..(i + height) {
            for x in j..(j + width) {
                grid[y][x] += 1;
            } 
        }
    }

    // Count # of cells that are >= 2
    let mut overlaps = 0;
    for count in grid.iter().flatten() {
        if *count >= 2 {
            overlaps += 1;
        }
    }
    println!("{} cells are in 2 or more claims.", overlaps);

    // Part 2: Find the rectangle with only 1's
    for (index, rect) in rectangles.iter().enumerate() {
        let (i, j, height, width) = *rect;
        let mut found = true;
        for y in i..(i + height) {
            for x in j..(j + width) {
                if grid[y][x] != 1 {
                    found = false;
                }
            } 
        }

        if found {
            println!("ID of claim that doesn't overlap: {}", index + 1);
            break;
        }
    }
}