use std::{collections::HashMap, fs::File, io::{self, BufRead}};
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input_file_path = "inputs/1.txt";
    let file = File::open(input_file_path)?;
    let file_reader = io::BufReader::new(file);

    let mut v1: Vec<i32> = Vec::new();
    let mut v2: Vec<i32> = Vec::new();

    let mut num_fq = HashMap::new();

    for line in file_reader.lines() {
        let line = line?;

        let nums: Vec<&str> = line.split_whitespace().collect();

        let num1: i32 = nums[0].parse()?;
        let num2 = nums[1].parse::<i32>()?;

        v1.push(num1);
        v2.push(num2);

        num_fq
            .entry(num2)
            .and_modify(|v| *v = *v + 1)
            .or_insert(1);
    }

    let mut sim = 0;

    for num in &v1 {
        if let Some(val) = num_fq.get(&num) {
            sim += val * num;
        }
    }

    println!("{}", sim);

    Ok(())
}
