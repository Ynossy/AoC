use core::num::dec2flt::number;
use std::fs;

fn main() {
    let path = "input.txt";
    let contents = fs::read_to_string(path).expect("Something went wrong reading the file");
    let numbers = part1(&contents);
    part2(&contents, &numbers);
}

fn part1(contents: &String) -> Vec<[i32; 26]> {
    let mut numbers = vec![[0; 26]; contents.len()];
    let mut two = 0;
    let mut three = 0;

    for (i, line) in contents.trim().lines().enumerate() {
        for c in line.chars() {
            let abc = c as usize - 97;
            numbers[i][abc] += 1;
            // println!("{}", c as u32);
        }
        for c in 0..26 {
            if numbers[i][c] == 2 {
                two += 1;
                break;
            }
        }
        for c in 0..26 {
            if numbers[i][c] == 3 {
                three += 1;
                break;
            }
        }
    }
    println!(
        "Resulting Twos:{} Threes:{}, Result:{}",
        two,
        three,
        two * three
    );
    return numbers;
}

fn part2(contents: &String, numbers: Vec<[i32; 26]>) {}
