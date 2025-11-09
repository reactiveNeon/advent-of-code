# Advent of Code Solutions

This repository contains my Advent of Code solutions organized by year and programming language

## Quick Start

This project uses [just](https://github.com/casey/just) as a command runner. Install it first if you haven't already.

### Unified Commands (from root directory)

All commands follow the pattern: `just <command> <year> <lang> <day> [part]`

```bash
just create 2024 go day-01
just create 2025 rust day-01   # Same commands, different year!
just create 2026 go day-01     # Works for any future year!
```

### Common Commands

**List available languages:**
```bash
just list-langs
```

**Create a new day from template:**
```bash
just create 2024 go day-03
just create 2024 rust day-01
```

**Run a solution:**
```bash
just run 2024 go day-01 1      # Run Go day 1, part 1
just run 2024 rust day-02 2    # Run Rust day 2, part 2
```

**Test a solution:**
```bash
just test 2024 go day-01 1     # Test Go day 1, part 1
just test-all 2024 rust day-01 # Test all parts for Rust day 1
```

**Fetch puzzle inputs:**
```bash
just get-inputs 2024 go day-01
```

**Show help:**
```bash
just help
```

## Repository Structure

```
├── justfile              # Root command runner (unified interface)
├── languages/            # Centralized language configurations
│   ├── go/
│   │   ├── justfile      # Go commands (works for any year)
│   │   ├── template/     # Go templates
│   │   └── README.md
│   └── rust/
│       ├── justfile      # Rust commands (works for any year)
│       ├── template/     # Rust templates
│       └── README.md
├── scripts/
│   └── get-inputs.sh     # Script to fetch puzzle inputs
├── 2024/
│   ├── go/
│   │   └── day-XX/       # Individual day solutions
│   └── rust/
│       └── day-XX/       # Individual day solutions
└── 2025/                 # Future years automatically supported!
    ├── go/
    └── rust/
```

## Workflow

1. **Create a new day:**
   ```bash
   just create 2024 go day-03
   ```
   This creates the directory structure, copies templates, and attempts to fetch inputs.

2. **Edit test inputs:**
   Add the example input to `2024/go/day-03/inputs/test1.txt` and expected result in the test.

3. **Implement the solution:**
   Write your solution in `2024/go/day-03/part1.go`

4. **Test your solution:**
   ```bash
   just test 2024 go day-03 1
   ```

5. **Run with actual input:**
   ```bash
   just run 2024 go day-03 1
   ```

6. **Repeat for part 2!**

## Adding a New Language

To add support for a new language (e.g., Python):

1. **Create the language directory:**
   ```bash
   mkdir -p languages/python/template
   ```

2. **Add your templates:**
   Create template files in `languages/python/template/`

3. **Create a justfile:**
   Create `languages/python/justfile` with these commands:
   - `create year day`
   - `run year day part`
   - `test year day part`
   - `test-all year day`
   - `get-inputs year day`

4. **That's it!** Use it immediately:
   ```bash
   just create 2024 python day-01
   just run 2024 python day-01 1
   ```

See `languages/README.md` for detailed instructions.

## Why This Structure?

This architecture provides maximum scalability:

- **Add 2025, 2026, etc.** → No configuration needed, just use them!
- **Add a new language** → Create one directory in `languages/`, works for all years
- **Update templates** → Change once in `languages/<lang>/template/`, affects all years
- **Consistent commands** → Same interface regardless of year or language

The separation of language configuration from year-specific solutions means the repository scales effortlessly.

