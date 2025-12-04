# Java Language Support

This directory contains the centralized Java language configuration for all years.

## Structure

- `justfile` - Java-specific commands that work for any year
- `template/` - Template files used to generate new day solutions

## Template Files

- `Part1.java` - Main solution file for part 1
- `Part2.java` - Main solution file for part 2
- `Part1Test.java` - Tests for part 1
- `Part2Test.java` - Tests for part 2

## Requirements

- Java 11+ (uses single-file source-code programs feature)

## How It Works

When you run `just create 2024 day-01 java` from the root:
1. The root justfile calls this directory's justfile
2. This justfile creates `2024/day-01/java/` directory
3. Templates are copied
4. Input files are created

## Commands

```bash
# Create a new day
just create 2024 day-01 java

# Run a solution
just run 2024 day-01 java 1

# Test a solution
just test 2024 day-01 java 1

# Test all parts
just test-all 2024 day-01 java
```

## Note

This setup uses Java's single-file source-code programs feature (JEP 330, Java 11+), which allows running `.java` files directly without explicit compilation. Tests require assertions to be enabled - use `java -ea` if assertions aren't working.
