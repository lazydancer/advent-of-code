fn main() {
    let course = include_str!("../input.txt").lines().map(|l| l.split_once(" ").unwrap());
    let course = course.map(|(d, v)| (d, v.parse::<i32>().unwrap()) );

    let (horz, depth) = course.clone().fold((0, 0),
        | (horz, depth), (dir, v) | {
            match (dir, v) {
                ("forward", v) => (horz + v, depth),
                ("down", v) => (horz, depth + v),
                ("up", v) => (horz, depth - v),
                _ => panic!(),
            }
        });

    println!("part 1: {:?}", horz * depth);



    let (horz, depth, _aim) = course.fold((0, 0, 0),
        | (horz, depth, aim), (dir, v) | {
            match (dir, v) {
                ("forward", v) => (horz + v, depth + aim * v, aim),
                ("down", v) => (horz, depth, aim + v),
                ("up", v) => (horz, depth, aim - v),
                _ => panic!(),
            }
        });

    println!("part 2: {:?}", horz * depth);

}
