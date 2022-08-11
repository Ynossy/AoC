use std::collections::HashSet;
use std::fs;
use std::str::FromStr;

fn main() {
    let path = "input.txt";
    let contents = fs::read_to_string(path).expect("Something went wrong reading the file");

    part1(&contents);
    part2(&contents);
}

fn part1(contents: &String) {
    let mut frequency: i32 = 0;
    for line in contents.trim().lines() {
        // println!("{}", line);
        frequency += i32::from_str(line).unwrap();
    }
    println!("Resulting Frequency: {}", frequency);
}

fn part2(contents: &String) {
    println!("Start Part 2");
    let mut used_frequencies = HashSet::new();
    let mut frequency = 0;
    'outer: loop {
        for line in contents.trim().lines() {
            // println!("{}", line);
            frequency += i32::from_str(line).unwrap();
            if !used_frequencies.insert(frequency) {
                println!("Repeated Frequency: {}", frequency);
                break 'outer;
            }
        }
    }
}
