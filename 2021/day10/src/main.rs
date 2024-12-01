fn main() {
    let out = include_str!("../input.txt")
        .lines().map(|l| 
            l.trim().chars().fold(vec![0,0,0,0], |acc, x| {
                if acc.contains(&-1) {
                    return acc
                }

                match x {
                    '(' => vec![acc[0]+1, acc[1], acc[2], acc[3]], 
                    ')' => vec![acc[0]-1, acc[1], acc[2], acc[3]], 
                    '[' => vec![acc[0], acc[1]+1, acc[2], acc[3]], 
                    ']' => vec![acc[0], acc[1]-1, acc[2], acc[3]], 
                    '{' => vec![acc[0], acc[1], acc[2]+1, acc[3]], 
                    '}' => vec![acc[0], acc[1], acc[2]-1, acc[3]], 
                    '<' => vec![acc[0], acc[1], acc[2], acc[3]+1], 
                    '>' => vec![acc[0], acc[1], acc[2], acc[3]-1], 
                    _ => unimplemented!()
                }
            })
            .iter().position(|x| *x == -1)
        );
        // .map(|c| [3,57,1197, 25137][c.unwrap() as usize])
        // ).sum::<u32>();

    println!("{:?}", out.collect::<Vec<_>>());

    // 51474 too low
}
