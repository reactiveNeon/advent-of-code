use std::{fs::File, io};

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

    Ok(todo!())
}

#[cfg(test)]
mod tests {
    use crate::solve;

    #[test]
    fn part1() {
        let expected_res: i64 = todo!();

        match solve("inputs/test1.txt") {
            Ok(res) => assert_eq!(expected_res, res),
            Err(e) => panic!("{}", e)
        }
    }
}
