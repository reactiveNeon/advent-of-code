use std::{fs::File, io, time::Instant};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let start = Instant::now();
    match solve("inputs/input.txt") {
        Ok(res) => {
            let elapsed = start.elapsed();
            println!("{}", res);
            eprintln!("Runtime: {}ms", elapsed.as_millis());
        }
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

        match solve("inputs/test.txt") {
            Ok(res) => assert_eq!(expected_res, res),
            Err(e) => panic!("{}", e)
        }
    }
}
