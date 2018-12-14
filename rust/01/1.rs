use std::io::{self, BufRead};

fn main() {
    let mut freq = 0;

    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let x = line.unwrap().parse::<i32>().unwrap();
        freq += x;
    }

    println!("End frequency: {}", freq);
}