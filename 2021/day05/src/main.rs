use regex::Regex;
use itertools::Itertools;

fn main() {
    // let a = include_str!("../input.txt").lines()
    //     .map(|x| x.split(" -> ")
    //          .map(|c| c.split(",")
    //             .map(|v| v.parse::<u32>().unwrap())
    //             .collect::<Vec<_>>()).collect::<Vec<_>>()).collect::<Vec<_>>();
            


    // println!("{:?}", a);

    let (mut map, mut overlaps) = (vec![0u8; 1000 * 1000], 0);

    include_str!("../input.txt")
        .lines()
        .map(|x| {
            let (x, y, xx, yy) = Regex::new(r"[0-9]+")
                    .unwrap()
                    .find_iter(x)
                    .map(|x| x.as_str().parse::<u32>().unwrap())
                    .collect_tuple()
                    .unwrap();

            (x.min(xx), y.min(yy), x.max(xx), y.max(yy))
        })
        .for_each(|(x, y, xx, yy)| {
            if x == xx {
                (y..=yy).for_each(|yo| map[(x + yo * 1000) as usize] += 1);
            } else if y == yy {
                (x..=xx).for_each(|xo| map[(xo + y * 1000) as usize] += 1);
            }

        });


    println!("{:?}", map.iter().filter(|&x| *x>1).count());
}
