
fn is_bingo(board: &[u32], numbers: &[u32]) -> bool {
    // Horizontal
    board.chunks(5).any(|r| {
        r.iter().all(|e| numbers.contains(e))        
    })

    || 
    
    // Vertical
    (0..5).any(|c| {
        (0..5).all(|e| numbers.contains(&board[e*5+c]))
    }) 
}


fn main() {
    let (numbers, boards)  = include_str!("../input.txt").split_once("\n\n").unwrap();

    let numbers: Vec<u32> = numbers
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect();

    let boards: Vec<Vec<u32>> = boards
        .split("\n\n")
        .map(|b| {
            b.split_whitespace()
             .map(|i| i.parse().unwrap())
             .collect()
    }).collect();


    let mut marks = vec!{};
    let (r_board, r_marks) = numbers.iter().find_map(|num| {
        
        marks.push(*num);

        boards.iter().find_map(|b|     
            match is_bingo(b, &marks) {
                true => Some((b.clone(), marks.clone())),
                false => None,
            } 
        )
    }).unwrap();

    let unmarked: u32 = r_board.into_iter().filter(|s| !marks.contains(s)).sum();

    println!("{:?}",  r_marks.last().unwrap() * unmarked);        // 8136
}
