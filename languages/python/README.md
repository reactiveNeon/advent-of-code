# Python Language Support

This directory contains the Python template and justfile for Advent of Code solutions.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager

## Usage

From the root directory:

```bash
# Create a new day
just create 2025 day-01 python

# Run a solution
just run 2025 day-01 python 1

# Test a solution
just test 2025 day-01 python 1

# Test all parts
just test-all 2025 day-01 python
```

## Project Structure

Each day creates:
```
{year}/{day}/python/
├── pyproject.toml    # uv project config
├── uv.lock           # dependency lock file
├── part1.py          # Part 1 solution
├── part2.py          # Part 2 solution
├── test_part1.py     # Part 1 tests
├── test_part2.py     # Part 2 tests
└── inputs/
    ├── input1.txt    # Part 1 puzzle input
    ├── input2.txt    # Part 2 puzzle input
    ├── test1.txt     # Part 1 test input
    └── test2.txt     # Part 2 test input
```
