
const WIDTH: usize = 100;
const HEIGHT: usize = 100;

fn lowest(heightmap: &[u8], i: usize) -> bool {
   !(   ((i+1) % WIDTH != 0)        && (heightmap[i as usize] >= heightmap[i + 1 ]) // Right
    ||  (i < (WIDTH * (HEIGHT-1)))  && (heightmap[i as usize] >= heightmap[i + WIDTH]) // Bottom
    ||  (i % WIDTH != 0)            && (heightmap[i as usize] >= heightmap[i - 1]) // Left
    ||  (i > WIDTH - 1)             && (heightmap[i as usize] >= heightmap[i - WIDTH]) // Top
    )
}

fn part1() {
    let heightmap: Vec<u8> = include_bytes!("../input.txt").into_iter()
        .filter(|&x| *x != b'\n')
        .map(|&x| x - b'0')
        .collect();

    let lowest_points = heightmap
        .iter().enumerate()
        .filter(|(i, n)| lowest(&heightmap, *i))
        .fold(0, |acc, x| 1 + acc + *x.1 as u32);

    println!("{:?}", lowest_points);
}

const NEXT: [(isize, isize); 4] = [(0, -1), (0, 1), (-1, 0), (1, 0)];

fn basin(map: &mut Vec<Vec<u8>>, x: usize, y: usize) -> usize {
    map[y][x] = b'9';
    NEXT.iter()
        .map(|(xx, yy)| ((x as isize + xx) as usize, (y as isize + yy) as usize))
        .fold(1, |acc, (x, y)| {
            match map.get(y).and_then(|l| l.get(x)).map(|&n| n < b'9') {
                Some(true) => acc + basin(map, x, y),
                _ => acc,
            }
        })
}

fn part2() {
    let mut map = include_bytes!("../input.txt")
        .split(|&b| b == b'\n')
        .map(|l| l.to_vec())
        .collect::<Vec<_>>();

    let mut basins = vec![];
    for y in 0..map.len() {
        for x in 0..map[0].len() {
            (map[y][x] < b'9').then(|| basins.push(basin(&mut map, x, y)));
        }
    }

    basins.sort();
    println!("{:?}", basins.iter().rev().take(3));


}

fn main() {
    part1();
    part2();
}
