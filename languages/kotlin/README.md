# Kotlin Language Support

This directory contains the centralized Kotlin language configuration for all years.

## Structure

- `justfile` - Kotlin-specific commands that work for any year
- `template/` - Template files used to generate new day solutions

## Template Files

- `Part1.kt` - Main solution file for part 1
- `Part2.kt` - Main solution file for part 2
- `Part1Test.kt` - Tests for part 1
- `Part2Test.kt` - Tests for part 2

## Requirements

- Kotlin compiler (`kotlinc`)
- Java Runtime Environment (JRE)

## Installing Kotlin on macOS

### Option 1: Homebrew (Recommended)
```bash
brew install kotlin
```

### Option 2: SDKMAN
```bash
# Install SDKMAN first if you don't have it
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# Install Kotlin
sdk install kotlin
```

### Option 3: Manual Installation
1. Download from https://github.com/JetBrains/kotlin/releases
2. Extract and add `bin` directory to your PATH

### Verify Installation
```bash
kotlinc -version
```

## How It Works

When you run `just create 2024 day-01 kotlin` from the root:
1. The root justfile calls this directory's justfile
2. This justfile creates `2024/day-01/kotlin/` directory
3. Templates are copied
4. Input files are created

## Commands

```bash
# Create a new day
just create 2024 day-01 kotlin

# Run a solution
just run 2024 day-01 kotlin 1

# Test a solution
just test 2024 day-01 kotlin 1

# Test all parts
just test-all 2024 day-01 kotlin
```

## Note

The Kotlin compiler compiles to JAR files which are then executed with Java. The first run may be slower due to compilation, but subsequent runs of the compiled JAR are fast.
