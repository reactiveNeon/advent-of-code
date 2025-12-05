import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    ranges = []
    for line in lines:
        if line == '':
            break
        
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    ranges.sort()
    
    prev_start, prev_end = ranges[0]
    
    unique = 0
    for range in ranges[1:]:
        start, end = range
        if start > prev_end:
            unique += prev_end - prev_start + 1
            prev_start, prev_end = start, end
            continue
        
        prev_end = max(prev_end, end)
        
    unique += prev_end - prev_start + 1
        
    return unique


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
