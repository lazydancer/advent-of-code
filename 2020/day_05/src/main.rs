
/*

Binary space partitioning

7 charaters will be F or B which represents 1 of 128 rows on the plane.

F means lower, B means Back

front 0-63, back 64-127

B = 1, F = 0

010110 = 44

R = 1, L = 0

101

*/


fn get_row(seat: &str) -> i32 {
    let row = &seat[..7]
        .replace("B", "1")
        .replace("F", "0");

    let row = i32::from_str_radix(row, 2).unwrap();

    row
}

fn get_column(seat: &str) -> i32 {
    let column = &seat[7..]
        .replace("R", "1")
        .replace("L", "0");

    let column = i32::from_str_radix(column, 2).unwrap();

    column
}

fn get_id(seat: &str) -> i32 {

    let row = get_row(seat);
    let column = get_column(seat);

    row * 8 + column

}

fn main() {

    let seat_addresses: Vec<&str> = include_str!("../input.txt").split("\n").collect();

    let ids: Vec<i32> = seat_addresses.into_iter().map(get_id).collect();

    println!("{:?}", ids.iter().max().unwrap()); // 861

    let mut locs: Vec<(i32, i32)> = seat_addresses.into_iter().map(|x| (get_row(x), get_column(x))).collect(); 
    locs.sort_by_key(|k| k.1);
    locs.sort_by_key(|k| k.0);

    for l in locs {
        println!("{:?}", l);
    } // (79,1)

}

