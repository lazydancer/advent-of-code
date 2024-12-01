fn main() {
    let horizontal_positions: Vec<u32> = include_str!("../input.txt")
        .trim()
        .split(",")
        .map(|x| x.parse::<u32>().unwrap())
        .collect();

    let average = (horizontal_positions.iter().sum::<u32>() as f32 / horizontal_positions.len() as f32).round() as u32;
    
    for avg in 0..average {
        let result: u32 = horizontal_positions.iter().fold(0, |acc, val| acc + val.max(&avg) - val.min(&avg));
        println!("{}, {:?}", avg, result);
    }


    // println!("{}", vec!{16,1,2,0,4,2,7,1,2,14}.iter().sum::<i32>() / 10);
    // 365553 too high
}
