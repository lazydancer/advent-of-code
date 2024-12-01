
fn part1(input: &Vec<u8>) {
    let mut life: Vec<i8> = input.iter().map(|x| *x as i8).collect(); 

    for i in 0..80 {
        life.iter_mut().for_each(|x| *x -= 1);

        let count = life.iter().filter(|x| **x == -1).count();
        life.extend(vec![8; count]);


        life.iter_mut().filter(|x| **x == -1).for_each(|x| *x += 7 );
    }

    println!("{:?}", life.len());
}


fn part2(input: &Vec<u8>) {

    let mut life = [0; 9];
    input.iter().for_each(|x| life[*x as usize] += 1);

    (0..256).for_each(|_| {
        life.rotate_left(1);
        life[6] += life[8];
    });

    println!("{:?}, {}", life, life.iter().sum::<u64>());

}

fn main() {
    let input: Vec<u8> = include_str!("../input.txt")
        .trim()
        .split(',')
        .map(|x| x.parse::<u8>().unwrap())
        .collect();
    
    // part1(&input)
    part2(&input)

    // 380612
}
