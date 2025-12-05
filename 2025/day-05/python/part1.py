import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    ranges = []
    nums = []
    
    nums_from = -1
    for i, line in enumerate(lines):
        if line == '':
            nums_from = i + 1
            break
            
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
        
    for line in lines[nums_from:]:
        nums.append(int(line))
        
    fresh = 0
    for num in nums:
        for range in ranges:
            start, end = range
            if num >= start and num <= end:
                fresh += 1
                break

    return fresh


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
