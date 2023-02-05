// use itertools::Itertools;

fn main() {
    let raw_input = include_str!("input.txt");

    let (boxes, moves) = raw_input.split_once("\n\n").unwrap();

    let num_stacks = boxes.lines()
        .rev()
        .take(1)
        .next()
        .unwrap()
        .chars()
        .filter(|c| c.is_numeric())
        .count();

    let mut stacks: Vec<Vec<char>>  = vec![vec![]; num_stacks];
    
    boxes.lines()
        .rev()
        .skip(1)
        .map(str::as_bytes)
        .for_each(|l| {
            for i in 0..stacks.len() {
                let val = l[1 + i * 4]; 
                if val.is_ascii_alphabetic() {
                    stacks[i].push(val as char);
                }
            }
        });
    
    moves.lines()
        .map(|l| l.split_ascii_whitespace())
        .filter_map(|s| s.parse::<usize>().ok())
        .for_each(|s| println!("{}", s));
        //     .filter_map(|s| s.parse::<usize>().ok())
        //     .collect_tuple()
        //     .unwrap()
        // )
        // .collect::<Vec<_>>();
    
    // let moves: Vec<(usize, usize, usize)> = moves.lines()
    //     .map(|l| l.split_whitespace()
    //         .filter_map(|s| s.parse::<usize>().ok())
    //         .collect_tuple()
    //         .unwrap()
    //     )
    //     // .map(|(_, how_many, _, from, _, to)| 
    //     //     (
    //     //         how_many.parse::<usize>().unwrap(),
    //     //         from.parse::<usize>().unwrap(),
    //     //         to.parse::<usize>().unwrap()
    //     //     )
    //     // )
    //     .collect();




}// println!("{}", stacks[stacks.len() - 1]);


