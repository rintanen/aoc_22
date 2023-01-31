use std::fs;

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input");

    let rounds: Vec<&str> = input.split("\n").collect();

    let combos_p1 = ["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"];
    let combos_p2 = ["B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"];

    let points_pt1: usize = rounds
        .iter()
        .map(|round| combos_p1.iter().position(|&r| r == *round).unwrap() + 1)
        .sum();
    
    let points_pt2: usize = rounds
        .iter()
        .map(|round| combos_p2.iter().position(|&r| r == *round).unwrap() + 1)
        .sum();

    println!("{}", points_pt1);
    println!("{}", points_pt2);
}