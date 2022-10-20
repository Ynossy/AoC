use std::fs;

fn main() {
    let path = "input.txt";
    let contents = fs::read_to_string(path).expect("Something went wrong reading the file");
    part1(&contents);
    part2(&contents);
}

fn part1(contents: &String) {
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
}

fn part2(contents: &String) {
    let lines: Vec<&str> = contents.trim().lines().collect();
    'task: for line1 in &lines {
        for line2 in &lines {
            let vec_line1: Vec<char> = line1.chars().collect();
            let vec_line2: Vec<char> = line2.chars().collect();
            let mut same = 0;
            for c in 0..vec_line1.len() {
                if vec_line1[c] == vec_line2[c] {
                    same += 1;
                }
            }
            if same == vec_line1.len()-1 {
                println!("Found Strings: ");
                println!("{}", line1);
                println!("{}", line2);
                break 'task;
            }
        }
    }
}
