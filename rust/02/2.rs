use std::io::{self, BufRead};
use std::collections::HashMap;

fn main() {
    // Part 1
    let mut twos = 0;
    let mut threes = 0;
    let mut lines = Vec::new();

    let stdin = io::stdin();
    for l in stdin.lock().lines() {
        lines.push(l.unwrap());
        let line = lines.last().unwrap();

        // Count how many times each letter occurs
        let mut letter_counts = HashMap::new();
        for letter in line.chars() {
            if letter_counts.contains_key(&letter) {
                *letter_counts.get_mut(&letter).unwrap() += 1;
            }
            else {
                letter_counts.insert(letter, 1);
            }
        }

        // Does the line have any letter that occurs twice? three times?
        let mut twice = false;
        let mut thrice = false;
        for (_, count) in letter_counts.iter() {
            if *count == 2 {
                twice = true;
            }
            if *count == 3 {
                thrice = true;
            }
        }

        if twice {
            twos += 1;
        }
        if thrice {
            threes += 1;
        }
    }

    println!("Twos * Threes = {}", twos * threes);
    
    // Part 2 - find the lines differing in only 1 character
    for i in 0..lines.len() {
        for j in (i + 1)..lines.len() {
            let dist = differing_chars(&lines[i], &lines[j]);
            if dist == 1 {
                // Find which letters are the same
                let mut chars1 = lines[i].chars();
                let mut chars2 = lines[j].chars();
                let mut sames = Vec::new();
                for _ in 0..lines[i].len() {
                    let x1 = chars1.next();
                    let x2 = chars2.next();
                    if x1 == x2 {
                        sames.push(x1);
                    }
                }
                
                for letter in sames {
                    print!("{}", letter.unwrap());
                }
                println!();
            }
        }
    }
}

fn differing_chars(x: &String, y: &String) -> i32 {
    let mut diffs = 0;

    let mut x_chars = x.chars();
    let mut y_chars = y.chars();
    for _ in 0..x.len() {
        if x_chars.next() != y_chars.next() {
            diffs += 1
        }
    }

    diffs
}