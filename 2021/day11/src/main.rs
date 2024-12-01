fn flash(map: &mut Vec<Vec<u8>>, x: usize, y: usize) -> u32 {
    let neighbours: [(isize, isize); 8] = [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1,-1), (1, 0), (1, 1)];
    
    map[y][x] = 0;
    neighbours.iter()
        .map(|(xx, yy)| ((x as isize + xx) as usize, (y as isize + yy) as usize))
        .fold(1, |acc, (x, y)| {
            match map.get_mut(y).and_then(|l| l.get_mut(x)) {
                Some(cell) if *cell > 0 => {
                    *cell += 1;
                    acc + (*cell > 9).then(|| flash(map, x, y)).unwrap_or(0)
                }
                _ => acc
            }
        })
}
    
fn main() {
    let mut map = include_bytes!("../input.txt")
        .split(|&b| b == b'\n')
        .map(|a| a.iter().map(|b| b - b'0').collect::<Vec<_>>())
        .collect::<Vec<_>>();

    map.iter_mut().for_each(|l| l.iter_mut().for_each(|b| *b += 1 ));


    flash(&mut map, 0, 0);
    // (0..100).fold(|acc, _| {

        
    // })     

    println!("{:?}", map);
}
