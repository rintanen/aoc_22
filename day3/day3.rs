
fn priority(b: &u8) -> u32 {
    if *b >= b'a' {
        (b - b'a') as u32 + 1
    } else {
        (b - b'A') as u32 + 27
    }
}

fn main() {
    let task_input = include_bytes!("input.txt");
    let pt1 = task_input
        .split(|b| *b == b'\n')
        .map(|l| l.split_at(l.len() / 2))
        .map(|(a, b)| 
            b.iter()
            .filter(|b| a.contains(b))
            .map(|b| priority(b))
            .next()
            .unwrap()
        )
        .sum::<u32>();
    
    let pt2 = task_input
        .split(|b| *b == b'\n')
        .collect::<Vec<_>>()
        .chunks(3)
        .map(|slice| slice[0].iter()
                .find(|b| slice[1].contains(b) && slice[2].contains(b))
                .unwrap()
        )
        .map(|b| priority(b))
        .sum::<u32>();

    println!("{}", pt1);
    println!("{}", pt2);
}       