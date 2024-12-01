// #![feature(drain_filter)]

const WIDTH: usize = 12;
const COUNT: usize = 1000;


fn part1() {


    let gamma = include_str!("../input.txt")
        .lines()
        .map(|l| usize::from_str_radix(l, 2).unwrap())
        .fold(vec![0; WIDTH], |count, bits| {
            count
                .iter()
                .enumerate()
                .map(|(i, n)| n + ((bits & 1 << i) >> i))
                .collect()
        })
        .into_iter()
        .enumerate()
        .map(|(i, b)| ((b >= COUNT / 2) as u32) << i)
        .sum::<u32>();

    println!("{}", gamma * (!gamma & ((1 << WIDTH) - 1)));
    // 3009600
}



fn part2() {
    let nums = include_str!("../input.txt")
        .lines()
        .map(|l| usize::from_str_radix(l, 2).unwrap())
        .collect::<Vec<_>>();

    let oxy = (0..WIDTH).rev().scan(nums.clone(), |o, i| {
        let one = o.iter().filter(|n| *n & 1 << i > 0).count() >= (o.len() + 1) / 2;
        let (drained, _): (Vec<usize>, Vec<usize>) = o.iter().partition(|n| (*n & 1 << i > 0) != one);
        drained.first().copied()
    }).last().unwrap();

    let co2 = (0..WIDTH).rev().scan(nums, |o, i| {
        let one = o.iter().filter(|n| *n & 1 << i > 0).count() >= (o.len() + 1) / 2;
        let (drained, _): (Vec<usize>, Vec<usize>) = o.iter().partition(|n| (*n & 1 << i > 0) == one);
        drained.first().copied()
    }).last().unwrap();

    println!("{:?}", oxy * co2);

    // 309518 too low
}

fn main() {
    part2();
}
