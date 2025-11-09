# Advent of Code - Root Justfile
# Delegates commands to centralized language-specific justfiles in languages/

# Create a new day
create year lang day:
  @echo "Creating {{day}} for {{year}}/{{lang}}..."
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @mkdir -p {{year}}/{{lang}}
  cd languages/{{lang}} && just create {{year}} {{day}}

# Run a solution
run year lang day part:
  @echo "Running {{year}}/{{lang}}/{{day}} part {{part}}..."
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @if [ ! -d "{{year}}/{{lang}}/{{day}}" ]; then \
    echo "Error: {{year}}/{{lang}}/{{day}} does not exist"; \
    echo "Create it first with: just create {{year}} {{lang}} {{day}}"; \
    exit 1; \
  fi
  cd languages/{{lang}} && just run {{year}} {{day}} {{part}}

# Test a solution (specific part)
test year lang day part:
  @echo "Testing {{year}}/{{lang}}/{{day}} part {{part}}..."
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @if [ ! -d "{{year}}/{{lang}}/{{day}}" ]; then \
    echo "Error: {{year}}/{{lang}}/{{day}} does not exist"; \
    exit 1; \
  fi
  cd languages/{{lang}} && just test {{year}} {{day}} {{part}}

# Test all parts for a day
test-all year lang day:
  @echo "Testing all parts for {{year}}/{{lang}}/{{day}}..."
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  @if [ ! -d "{{year}}/{{lang}}/{{day}}" ]; then \
    echo "Error: {{year}}/{{lang}}/{{day}} does not exist"; \
    exit 1; \
  fi
  cd languages/{{lang}} && just test-all {{year}} {{day}}

# Get inputs for a day
get-inputs year lang day:
  @echo "Fetching inputs for {{year}}/{{lang}}/{{day}}..."
  @if [ ! -f "languages/{{lang}}/justfile" ]; then \
    echo "Error: Language '{{lang}}' not supported"; \
    echo "Available languages: $(ls -1 languages/ | tr '\n' ' ')"; \
    exit 1; \
  fi
  cd languages/{{lang}} && just get-inputs {{year}} {{day}}

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
  @find . -path './2*/*/day-*' -type d | sed 's|^\./||' | sort

# List available commands
help:
  @echo "Advent of Code Commands:"
  @echo ""
  @echo "  just list-langs                       - Show available languages"
  @echo "  just list-year <year>                 - Show solutions for a specific year"
  @echo "  just list                             - Show all solutions"
  @echo "  just create <year> <lang> <day>       - Create a new day from template"
  @echo "  just run <year> <lang> <day> <part>   - Run a solution"
  @echo "  just test <year> <lang> <day> <part>  - Test a specific part"
  @echo "  just test-all <year> <lang> <day>     - Test all parts for a day"
  @echo "  just get-inputs <year> <lang> <day>   - Fetch puzzle inputs"
  @echo ""
  @echo "Examples:"
  @echo "  just list-langs"
  @echo "  just create 2024 go day-03"
  @echo "  just create 2025 rust day-01    # Works for any year!"
  @echo "  just run 2024 rust day-01 1"
  @echo "  just test 2024 go day-02 2"
  @echo "  just test-all 2024 rust day-01"
