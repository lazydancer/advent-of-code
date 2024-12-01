/*
0 : 6
1 : 2 *
2 : 5
3 : 5
4 : 4 *
5 : 5
6 : 6
7 : 3 *
8 : 7 *
9 : 6


2: 1
3: 7
4: 4
5: 2,3,5 
6: 0,6,9
7: 8


1: 2,5
7: 0,2,5
4: 1,2,3,5
2: 0,1,3,4,6
3: 0,2,3,5,6
5: 0,1,3,5,6
0: 0,1,2,4,5,6
6: 0,1,3,4,5,6
9: 0,1,2,3,5,6
8: 0,1,2,3,4,5,6 
*/


fn main() {
    let result: usize = include_str!("../input.txt")
        .lines().map(|l| {
            l.split_once("|").unwrap().1
                .split_whitespace()
                .filter(|x| vec!{2,4,3,7}.contains(&x.len())).count()
        }).sum();

    println!("{:?}", result);

    //1121 too high
    //321 !
}
