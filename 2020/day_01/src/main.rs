use std::{
    path::Path, 
    io::{BufReader, prelude::*}, 
    fs::File
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<i32> {
    let file = File::open(filename).expect("no such file");
    BufReader::new(file).lines()
        .map(|l| l.expect("could not parse line").parse().expect("could not convert line"))
        .collect()
}

fn part1(lines: &Vec<i32>) {
    for a in lines {
        for b in lines {
            if a + b == 2020 {
                println!("{} + {} == 2020. The product is {}", a, b, a*b)
            }
        }
    }
}

fn part2(lines: &Vec<i32>) {
    for a in lines {
        for b in lines {
            for c in lines {
                if a + b + c == 2020 {
                    println!("{} + {} + {} == 2020. The product is {}", a, b, c, a*b*c)
                }
            }
        }
    }

}

fn main() {
    let lines = lines_from_file("input.txt");

    part1(&lines);
    part2(&lines);
}
