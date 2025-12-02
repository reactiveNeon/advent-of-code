from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")
    input = ''.join(lines)
    
    num_ranges = input.split(',')
    
    invalid_sum = 0
    
    for num_range in num_ranges:
        start, end = map(int, num_range.split('-'))
        for idx in range(start, end + 1):
            pass

    return invalid_sum


def main() -> None:
    result = solve("inputs/input.txt")
    print(result)


if __name__ == "__main__":
    main()
