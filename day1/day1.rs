use std::fs;


fn main() {
    let mut calories: Vec<u32> = fs::read_to_string("input.txt")
        .expect("Failed to read input")
        .split("\n\n")
        .map(|s| {
            s.lines()
            .map(|i| i.parse::<u32>().unwrap())
            .sum()
        })
        .collect();

    calories.sort();
    calories.reverse();

    println!("{}", calories[0]);
    println!("{}", calories[0] + calories[1] + calories[2]);
}