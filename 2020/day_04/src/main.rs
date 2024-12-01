use std::collections::HashMap;
use itertools::Itertools;

const REQ_FIELDS: [&'static str; 7] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
const EYE_COLORS: [&'static str; 7] = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];

fn valid_passport_part_2(pass: &HashMap<&str, &str>) -> bool {
    if !REQ_FIELDS.iter().all(|r| pass.contains_key(r)) {
        return false
    }

    if let Ok(x) = pass["byr"].parse::<i32>() {
        if x < 1920 || x > 2002 {
            return false
        }
    } else {
        return false
    }

    if let Ok(x) = pass["iyr"].parse::<i32>() {
        if x < 2010 || x > 2020 {
            return false
        }
    } else {
        return false
    }

    if let Ok(x) = pass["eyr"].parse::<i32>() {
        if x < 2020 || x > 2030 {
            return false
        }
    } else {
        return false
    }

    let len = pass["hgt"].len();
    if let Ok(x) = pass["hgt"][..len-2].parse::<i32>() {
        let unit = &pass["hgt"][len-2..];

        match unit {
            "cm" => {
                if x < 150 || x > 193 {
                    return false
                }
            },
            "in" => {
                if x < 59 || x > 76 {
                    return false
                }
            },
            _ => {
                return false
            },
        }

    } else {
        return false
    }


    if pass["hcl"].len() != 7 {
        return false
    }

    if let Some(x) = pass["hcl"].chars().nth(0) {
        if x != '#' {
            return false
        }
    }

    for c in pass["hcl"][1..].chars() {
        match c {
            '0' |'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'|'a'|'b'|'c'|'d'|'e'|'f' => {},
            _ => return false,
        }
    }

    if !["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].contains(&pass["ecl"]) {
        return false
    }


    if pass["pid"].len() != 9 {
        return false
    }
    if let Ok(x) = pass["pid"].parse::<i32>() {
        
    } else {
        return false
    }

    return true
}

fn validate_field(field: &str, value: &str) -> bool {
    match field {
        "byr" => (1920..=2002).contains(&value.parse::<i32>().unwrap()),
        "iyr" => (2010..=2020).contains(&value.parse::<i32>().unwrap()),
        "eyr" => (2020..=2030).contains(&value.parse::<i32>().unwrap()),
        "hgt" => {
            if value.ends_with("cm") && value.len() == 5 {
                (150..=193).contains(&value[0..3].parse::<i32>().unwrap())
            } else if value.ends_with("in") && value.len() == 4 {
                (59..=76).contains(&value[0..2].parse::<i32>().unwrap())
            } else {
                false
            }
        }
        "hcl" => value.len() == 7,
        "ecl" => EYE_COLORS.iter().any(|v| v == &value),
        "pid" => value.len() == 9,
        "cid" => true,
        _ => panic!("unknown field")
    }
}

fn main() {
    let passports: Vec<HashMap<&str, &str>> = include_str!("../input.txt")
        .split("\n\n")
        .map(|fields| fields
            .split_whitespace()
            .map(|f| f.splitn(2,':').collect_tuple().unwrap())
            .collect::<HashMap<&str, &str>>())
        .collect();

    println!(
        "part 1: {:?}", 
        passports
            .clone()
            .into_iter()
            .filter(|pass| REQ_FIELDS.iter().all(|r| pass.contains_key(r)))
            .count()
    ); // 204


    println!(
        "part 2: {:?}", 
        passports.clone().into_iter()
            .filter(|pass| REQ_FIELDS.iter().all(|r| pass.contains_key(r)))
            .filter(|pass| pass.iter().all(|(f, v)| validate_field(f, v)))
            .count()
    ); // 179

}
