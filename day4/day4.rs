use std::fs;


fn main() {
    let task_input = fs::read_to_string("input.txt").expect("fars");

    let pt1 = task_input
        .lines()
        .map(|l| {
            let (first, second) = l.split_once(',').unwrap();
            let ((a, b), (c, d)) = (first.split_once('-').unwrap(), second.split_once('-').unwrap());
            (
                a.parse::<u32>().unwrap(),
                b.parse::<u32>().unwrap(),
                c.parse::<u32>().unwrap(),
                d.parse::<u32>().unwrap()
            )})
        .filter(|(a, b, c, d)| {
            (a >= c && b <= d) || (c >= a && d <= b)
        })
        .count();
    
    let pt2 = task_input
    .lines()
    .map(|l| {
        let (first, second) = l.split_once(',').unwrap();
        let ((a, b), (c, d)) = (first.split_once('-').unwrap(), second.split_once('-').unwrap());
        (
            a.parse::<u32>().unwrap(),
            b.parse::<u32>().unwrap(),
            c.parse::<u32>().unwrap(),
            d.parse::<u32>().unwrap()
        )})
    .filter_map(|(a, b, c, d)| {
        let first = a..b + 1;
        let second = c..d + 1;

        for i in first {
            if second.contains(&i) {
                return Some(true);
            } 
        }
        None
    })
    .count();

    println!("{}", pt1);
    println!("{}", pt2);
        
}