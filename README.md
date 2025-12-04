# Advent of Code Solutions

This repository contains my Advent of Code solutions organized by year and programming language

## Quick Start

This project uses [just](https://github.com/casey/just) as a command runner. Install it first if you haven't already.

### Unified Commands (from root directory)

All commands follow the pattern: `just <command> <year> <day> <lang> [part]`

```bash
just create 2024 day-01 go
just create 2025 day-01 rust   # Same commands, different year!
just create 2025 day-02 python # Python with uv support!
```

### Common Commands

**List available languages:**
```bash
just list-langs
```

**Create a new day from template:**
```bash
just create 2024 day-03 go
just create 2024 day-01 rust
just create 2025 day-01 python
```

**Run a solution:**
```bash
just run 2024 day-01 go 1      # Run Go day 1, part 1
just run 2024 day-02 rust 2    # Run Rust day 2, part 2
just run 2025 day-01 python 1  # Run Python day 1, part 1
```

**Test a solution:**
```bash
just test 2024 day-01 go 1     # Test Go day 1, part 1
just test-all 2024 day-01 rust # Test all parts for Rust day 1
```

**Fetch puzzle inputs:**
```bash
just get-inputs 2024 day-01 go
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
│   ├── rust/
│   │   ├── justfile      # Rust commands (works for any year)
│   │   ├── template/     # Rust templates
│   │   └── README.md
│   ├── python/
│   │   ├── justfile      # Python commands (uses uv)
│   │   ├── template/     # Python templates
│   │   └── README.md
│   ├── cpp/
│   │   ├── justfile      # C++ commands (uses make)
│   │   ├── template/     # C++ templates
│   │   └── README.md
│   └── java/
│       ├── justfile      # Java commands
│       ├── template/     # Java templates
│       └── README.md
├── scripts/
│   └── get-inputs.sh     # Script to fetch puzzle inputs
├── 2024/
│   └── day-XX/
│       ├── go/           # Go solution for this day
│       ├── rust/         # Rust solution for this day
│       ├── python/       # Python solution for this day
│       ├── cpp/          # C++ solution for this day
│       └── java/         # Java solution for this day
└── 2025/
## Workflow

1. **Create a new day:**
   ```bash
   just create 2024 day-03 go
   ```
   This creates the directory structure, copies templates, and attempts to fetch inputs.

2. **Edit test inputs:**
   Add the example input to `2024/day-03/go/inputs/test1.txt` and expected result in the test.

3. **Implement the solution:**
   Write your solution in `2024/day-03/go/part1.go`

4. **Test your solution:**
   ```bash
   just test 2024 day-03 go 1
   ```

5. **Run with actual input:**
   ```bash
   just run 2024 day-03 go 1
   ```

6. **Repeat for part 2!**

## Adding a New Language

To add support for a new language (e.g., Java):

1. **Create the language directory:**
   ```bash
   mkdir -p languages/java/template
   ```

2. **Add your templates:**
   Create template files in `languages/java/template/`

3. **Create a justfile:**
   Create `languages/java/justfile` with these commands:
   - `create year day`
   - `run year day part`
   - `test year day part`
   - `test-all year day`
   - `get-inputs year day`

4. **That's it!** Use it immediately:
   ```bash
   just create 2024 day-01 java
   just run 2024 day-01 java 1
   ```

See `languages/README.md` for detailed instructions.

## Why This Structure?

This architecture provides maximum scalability:

- **Add 2025, 2026, etc.** → No configuration needed, just use them!
- **Add a new language** → Create one directory in `languages/`, works for all years
- **Update templates** → Change once in `languages/<lang>/template/`, affects all years
- **Consistent commands** → Same interface regardless of year or language
- **Multi-language per day** → Solve the same day in multiple languages side by side

The separation of language configuration from year-specific solutions means the repository scales effortlessly.
- **Add 2025, 2026, etc.** → No configuration needed, just use them!
- **Add a new language** → Create one directory in `languages/`, works for all years
- **Update templates** → Change once in `languages/<lang>/template/`, affects all years
- **Consistent commands** → Same interface regardless of year or language

The separation of language configuration from year-specific solutions means the repository scales effortlessly.

