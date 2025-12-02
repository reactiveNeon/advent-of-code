use std::{fs::File, io::{self, BufRead}};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input_file_path = "inputs/1.txt";
    let file = File::open(input_file_path)?;
    let file_reader = io::BufReader::new(file);

    let mut v1: Vec<i32> = Vec::new();
    let mut v2: Vec<i32> = Vec::new();

    for line in file_reader.lines() {
        let line = line?;

        let nums: Vec<&str> = line.split_whitespace().collect();

        let num1: i32 = nums[0].parse()?;
        let num2 = nums[1].parse::<i32>()?;

        v1.push(num1);
        v2.push(num2);
    }

    v1.sort();
    v2.sort();

    let mut total_sum = 0;

    for i in 0..v1.len() {
        total_sum += (v1[i] - v2[i]).abs(); 
    }

    println!("{}", total_sum);

    Ok(())
}
