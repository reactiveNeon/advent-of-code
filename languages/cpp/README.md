# C++ Language Support

This directory contains the centralized C++ language configuration for all years.

## Structure

- `justfile` - C++-specific commands that work for any year
- `template/` - Template files used to generate new day solutions

## Template Files

- `part1.cpp` - Main solution file for part 1 (with tests)
- `part2.cpp` - Main solution file for part 2 (with tests)
- `Makefile` - Build configuration

## Requirements

- `g++` with C++17 support (or modify the Makefile for your compiler)
- `make`

## How It Works

When you run `just create 2024 day-01 cpp` from the root:
1. The root justfile calls this directory's justfile
2. This justfile creates `2024/day-01/cpp/` directory
3. Templates are copied
4. Input files are created

## Commands

```bash
# Create a new day
just create 2024 day-01 cpp

# Run a solution
just run 2024 day-01 cpp 1

# Test a solution
just test 2024 day-01 cpp 1

# Test all parts
just test-all 2024 day-01 cpp
```

## Note on Testing

Tests are embedded in the source files using preprocessor directives. When running tests, the code is compiled with `-DTEST_MODE` flag which enables the test main function instead of the regular one.
