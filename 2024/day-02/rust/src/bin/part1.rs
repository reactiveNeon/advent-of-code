use std::{
    fs::File, 
    io::{
        self, 
        BufRead
    }
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    match solve("inputs/input1.txt") {
        Ok(res) => println!("{}", res),
        Err(e) => panic!("{}", e)
    }

    Ok(())
}

fn solve(input_file_path: &str) -> Result<i64, Box<dyn std::error::Error>> {
    let file = File::open(input_file_path)?;
    let file_reader = io::BufReader::new(file);

    let mut safe_count = 0;

    for line in file_reader.lines() {
        let line = line?;

        let nums: Vec<i32> = line
            .split_whitespace()
            .collect::<Vec<&str>>()
            .iter()
            .map(|s| s.parse().unwrap())
            .collect();

        let valid_sign = {
            let diff = nums.last().unwrap() - nums.first().unwrap();
            diff.signum()
        };

        let mut valid = true;

        for i in 1..nums.len() {
            let diff = nums[i] - nums[i - 1];

            if diff.abs() < 1 || diff.abs() > 3 || diff.signum() != valid_sign {
                valid = false;
                break;
            }
        }

        if valid {
            safe_count += 1;
        }
    }

    Ok(safe_count)
}

#[cfg(test)]
mod tests {
    use crate::solve;

    #[test]
    fn part1() {
        let expected_res: i64 = 2;

        match solve("inputs/test1.txt") {
            Ok(res) => assert_eq!(expected_res, res),
            Err(e) => panic!("{}", e)
        }
    }
}
