use std::{fs::File, io};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input_file_path = "inputs/1.txt";
    let file = File::open(input_file_path)?;
    let file_reader = io::BufReader::new(file);

    Ok(())
}
