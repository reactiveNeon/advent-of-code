# Advent of Code - Root Justfile
# Delegates commands to centralized language-specific justfiles in languages/

# Create a new day
create year day lang:
  @echo "Creating {{year}}/{{day}}/{{lang}}..."
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @mkdir -p {{year}}/{{day}}
  @cd languages/{{lang}} && just create {{year}} {{day}}

# Run a solution
run year day lang part:
  @echo "Running {{year}}/{{day}}/{{lang}} part {{part}}..." >&2
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @if [ ! -d "{{year}}/{{day}}/{{lang}}" ]; then \
    echo "Error: {{year}}/{{day}}/{{lang}} does not exist"; \
    echo "Create it first with: just create {{year}} {{day}} {{lang}}"; \
    exit 1; \
  fi
  @cd languages/{{lang}} && just run {{year}} {{day}} {{part}}

# Test a solution (specific part)
test year day lang part:
  @echo "Testing {{year}}/{{day}}/{{lang}} part {{part}}..." >&2
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @if [ ! -d "{{year}}/{{day}}/{{lang}}" ]; then \
    echo "Error: {{year}}/{{day}}/{{lang}} does not exist"; \
    exit 1; \
  fi
  @cd languages/{{lang}} && just test {{year}} {{day}} {{part}}

# Test all parts for a day
test-all year day lang:
  @echo "Testing all parts for {{year}}/{{day}}/{{lang}}..." >&2
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @if [ ! -d "{{year}}/{{day}}/{{lang}}" ]; then \
    echo "Error: {{year}}/{{day}}/{{lang}} does not exist"; \
    exit 1; \
  fi
  @cd languages/{{lang}} && just test-all {{year}} {{day}}

# Get inputs for a day
get-inputs year day lang:
  @echo "Fetching inputs for {{year}}/{{day}}/{{lang}}..."
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @cd languages/{{lang}} && just get-inputs {{year}} {{day}}

# List available languages
list-langs:
  @echo "Available languages:"
  @find languages -mindepth 1 -maxdepth 1 -type d -exec basename {} \;

# List solutions for a year
list-year year:
  @echo "Solutions for {{year}}:"
  @if [ -d "{{year}}" ]; then \
    find {{year}} -mindepth 2 -maxdepth 2 -type d | sed 's|{{year}}/||' | sort; \
  else \
    echo "No solutions found for {{year}}"; \
  fi

# List all solutions
list:
  @echo "All solutions:"
  @find . -path './2*/day-*/*' -type d -mindepth 3 -maxdepth 3 | sed 's|^\./||' | sort

# List available commands
help:
  @echo "Advent of Code Commands:"
  @echo ""
  @echo "  just list-langs                       - Show available languages"
  @echo "  just list-year <year>                 - Show solutions for a specific year"
  @echo "  just list                             - Show all solutions"
  @echo "  just create <year> <day> <lang>       - Create a new day from template"
  @echo "  just run <year> <day> <lang> <part>   - Run a solution"
  @echo "  just test <year> <day> <lang> <part>  - Test a specific part"
  @echo "  just test-all <year> <day> <lang>     - Test all parts for a day"
  @echo "  just get-inputs <year> <day> <lang>   - Fetch puzzle inputs"
  @echo ""
  @echo "Examples:"
  @echo "  just list-langs"
  @echo "  just create 2024 day-03 go"
  @echo "  just create 2025 day-01 rust         # Works for any year!"
  @echo "  just run 2024 day-01 rust 1"
  @echo "  just test 2024 day-02 go 2"
  @echo "  just test-all 2024 day-01 rust"
