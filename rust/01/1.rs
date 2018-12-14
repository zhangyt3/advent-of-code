use std::io::{self, BufRead};
use std::collections::HashSet;

fn main() {
    // Part 1
    let mut freq = 0;
    let stdin = io::stdin();
    let mut changes = Vec::new();

    for line in stdin.lock().lines() {
        let line = line.unwrap();
        let delta = line.parse::<i32>().unwrap();
        changes.push(delta);
        freq += delta;
    }
    println!("End frequency: {}", freq);

    // Part 2
    let mut seen: HashSet<i32> = HashSet::new();
    let mut first_repeat = 0;
    let mut found_repeat = false;
    
    freq = 0;
    seen.insert(0);
    while !found_repeat {
        for delta in &changes {
            freq += delta;
            
            if seen.contains(&freq) {
                first_repeat = freq;
                found_repeat = true;
                break;
            }
            else {
                seen.insert(freq);
            } 
        }
    }
    println!("First Repeat: {}", first_repeat);
}