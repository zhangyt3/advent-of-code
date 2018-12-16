use std::io::{self, BufRead};
use std::collections::HashSet;
use std::collections::HashMap;


fn main() {
    let mut coords = Vec::new();
    let mut min_row = 9999;
    let mut min_col = 9999;
    let mut max_row = 0;
    let mut max_col = 0;

    // Read in all the coordinates; store in (row, col) form.
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let line = line.unwrap();
        let split: Vec<&str> = line.split(", ").collect();
        let col = split[0].parse::<i32>().unwrap();
        let row = split[1].parse::<i32>().unwrap();

        // Keep track of smallest and largets row and col, to find infinite
        // areas later.
        if row < min_row {
            min_row = row;
        }
        if row > max_row {
            max_row = row;
        }

        if col < min_col {
            min_col = col;
        }
        if col > max_col {
            max_col = col;
        }

        coords.push((row, col));
    }

    // For each cell, find the marker it is closest too
    // Hack: map row 0 to row 2500, col 0 to col 2500
    // Then the areas which are infinite will probably be over 10000
    let eps: usize = 5000;
    let mut safes = 0;
    let mut grid = vec![vec![-1; (max_col as usize) + eps]; (max_row as usize) + eps];
    for row in 0..(max_row + 5000) {
        for col in 0..(max_col + 5000) {
            let mut min_dist = 9999999;
            let mut closest_marker: i32 = 0;
            let mut sum_dist = 0;
            for (index, coord) in coords.iter().enumerate() {
                let (i, j) = *coord;
                let dist = manhatten_dist(row, col, i + 2500, j + 2500);
                sum_dist += dist;
                if dist < min_dist {
                    min_dist = dist;
                    closest_marker = index as i32;
                }
                else if dist == min_dist {
                    // Tie for closest, so we don't want to set the cell at all
                    closest_marker = -(1 as i32);
                }
            }

            if sum_dist < 10000 {
                safes += 1;
            }
            grid[row as usize][col as usize] = closest_marker;
        }
    }

    // Find the markers with infinite areas
    let mut infinites = HashSet::new();
    for (index, coord) in coords.iter().enumerate() {
        let (i, j) = *coord;
        if i == min_row || i == max_row || j == min_col || j == max_col {
            infinites.insert(index);
        }
    }
    println!("Infinites: {:?}", infinites);

    // Calculate area of each marker
    let mut areas = HashMap::new();
    for marker in grid.iter().flatten() {
        if areas.contains_key(marker) {
            *areas.get_mut(&marker).unwrap() += 1;
        }
        else {
            areas.insert(marker, 1);
        }
    }

    // Find largest area that isn't infinite
    let mut largest = 0;
    let mut best_marker = 0;
    for (marker, area) in areas.iter() {
        if **marker == -1 {
            continue;
        }
        if !infinites.contains(&(**marker as usize)) && *area > largest && *area < 10000 {
            largest = *area;
            best_marker = **marker;
        }
    }

    println!("Best marker: {}", best_marker);
    println!("Largest non-infinite area: {}", largest);
    println!("Safes: {}", safes);
}


fn manhatten_dist(x1: i32, y1: i32, x2: i32, y2: i32) -> i32 {
    let dx: i32 = (x1 - x2).abs();
    let dy: i32 = (y1 - y2).abs();
    dx + dy
}