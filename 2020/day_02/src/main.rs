use std::ops::RangeInclusive;

struct PasswordPolicy {
    byte: u8,
    range: RangeInclusive<usize>,
}

impl PasswordPolicy {
    fn is_valid(&self, password: &str) -> bool {
        self.range.contains(
            &password
                .as_bytes()
                .iter()
                .copied()
                .filter(|&b| b == self.byte)
                .count(),
        )
    }
}

struct PasswordPolicyPart2 {
    byte: u8,
    positions: [usize; 2],
}

impl PasswordPolicyPart2 {
    fn is_valid(&self, password: &str) -> bool {
        self.positions
            .iter()
            .copied()
            .filter(|&index| password.as_bytes()[index] == self.byte)
            .count()
            == 1
    }
}

fn parse_line(s: &str) -> (PasswordPolicy, &str) {
    let (policy, password) = {
        let mut tokens = s.split(':');
        (
            tokens.next().unwrap(),
            tokens.next().unwrap(),
        )
    };

    let (range, byte) = {
        let mut tokens = policy.split(' ');
        (
            tokens.next().unwrap(),
            tokens.next().unwrap(),
        )
    };

    let byte = if byte.as_bytes().len() == 1 {
        byte.as_bytes()[0]
    } else {
        panic!("password policy byte to be exactly 1 byte ");
    };

    let (min, max) = {
        let mut tokens = range.split('-');
        (
            tokens.next().unwrap(),
            tokens.next().unwrap(),
        )
    };

    let range = (min.parse().unwrap())..=(max.parse().unwrap());

    (PasswordPolicy { range, byte }, password)
}

fn parse_line_part_2(s: &str) -> (PasswordPolicyPart2, &str) {
    let (policy, password) = {
        let mut tokens = s.split(':');
        (
            tokens.next().unwrap(),
            tokens.next().unwrap(),
        )
    };

    let (range, byte) = {
        let mut tokens = policy.split(' ');
        (
            tokens.next().unwrap(),
            tokens.next().unwrap(),
        )
    };

    let byte = if byte.as_bytes().len() == 1 {
        byte.as_bytes()[0]
    } else {
        panic!("password policy byte to be exactly 1 byte ");
    };

    let (min, max) = {
        let mut tokens = range.split('-');
        (
            tokens.next().unwrap(),
            tokens.next().unwrap(),
        )
    };

    let positions = [min.parse().unwrap(), max.parse().unwrap()];

    (PasswordPolicyPart2 { positions, byte }, password)
}

fn main() {
    let count = include_str!("../input.txt")
        .lines()
        .map(parse_line_part_2)
        .filter(|(policy, password)| policy.is_valid(password))
        .count();
    println!("{} passwords are valid", count);
}
