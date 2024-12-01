#[derive(Debug, Copy, Clone)]
struct Vec2 {
    x: i32,
    y: i32,
}

impl Vec2 {
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }
}

#[derive(Debug)]
struct Map {
    size: Vec2,
    tiles: Vec<Tile>,
}

impl Map {
    fn get(&self, pos: Vec2) -> Tile {
        let (x, y) = (pos.x, pos.y);
        let x = x - 1;
        let y = y - 1;

        let x = x % self.size.x;

        println!("x: {:?}, y: {:?}, result: {:?}", x, y, y * self.size.x + x);



        self.tiles[ ( y * self.size.x + x ) as usize]
    } 
    fn parse(s: &[u8]) -> Map {
        let mut map = Map { size: Vec2 { x: 31, y: 323}, tiles: vec![] };
        for &c in s.iter() {
            let tile = match c {
                b'.' => Some(Tile::Open),
                b'#' => Some(Tile::Tree),
                b'\n' => None,
                c => panic!("Expected '.' or '#', but got: {:?}", c),
            };

            if let Some(x) = tile {
                map.tiles.push(x);
            }

        }

        map
    }
}



#[derive(Debug, Copy, Clone, PartialEq)]
enum Tile {
    Tree,
    Open,
}

fn main() {
    let map = Map::parse(include_bytes!("../input.txt"));
    let itinerary = (0..map.size.y).into_iter().map(|y| Vec2::new(y*3+1, y+1));
    let num_trees = itinerary.filter(|&pos| map.get(pos) == Tile::Tree).count();
    
    println!("part a {} trees", num_trees);
    
    let mut num_trees = num_trees;
    
    let itinerary = (0..map.size.y).into_iter().map(|y| Vec2::new(y+1, y+1));
    num_trees *= itinerary.filter(|&pos| map.get(pos) == Tile::Tree).count();

    let itinerary = (0..map.size.y).into_iter().map(|y| Vec2::new(y*5+1, y+1));
    num_trees *= itinerary.filter(|&pos| map.get(pos) == Tile::Tree).count();


    let itinerary = (0..map.size.y).into_iter().map(|y| Vec2::new(y*7+1, y+1));
    num_trees *= itinerary.filter(|&pos| map.get(pos) == Tile::Tree).count();

    let itinerary = (0..((map.size.y-1)/2)).into_iter().map(|y| Vec2::new(y+1, y*2+1));
    num_trees *= itinerary.filter(|&pos| map.get(pos) == Tile::Tree).count();


    println!("part b {} trees", num_trees);
}
