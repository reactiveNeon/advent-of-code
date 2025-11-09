# Go Language Support

This directory contains the centralized Go language configuration for all years.

## Structure

- `justfile` - Go-specific commands that work for any year
- `template/` - Template files used to generate new day solutions

## Template Files

- `part1.go.tmpl` - Main solution file for part 1
- `part2.go.tmpl` - Main solution file for part 2
- `part1_test.go.tmpl` - Tests for part 1
- `part2_test.go.tmpl` - Tests for part 2
- `go.mod.tmpl` - Go module file

## How It Works

When you run `just create 2024 go day-01` from the root:
1. The root justfile calls this directory's justfile
2. This justfile creates `2024/go/day-01/` directory
3. Templates are copied and processed
4. Input files are created

This approach allows the same templates and logic to be reused for any year!
