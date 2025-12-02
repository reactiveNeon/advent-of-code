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
            idx_str = str(idx)
            idx_str_half_len = len(idx_str) // 2
            
            for sub_str_size in range(1, idx_str_half_len + 1):
                if len(idx_str) % sub_str_size == 0:
                    full_sub_str = idx_str[:sub_str_size] * (len(idx_str) // sub_str_size)
                    if idx_str == full_sub_str:
                        invalid_sum += idx
                        break

    return invalid_sum


def main() -> None:
    result = solve("inputs/input.txt")
    print(result)


if __name__ == "__main__":
    main()
