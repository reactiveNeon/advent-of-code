import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = list(map(list, Path(input_path).read_text().strip().split("\n")))
    
    lines[1][lines[0].index('S')] = '|'

    splits = 0
    
    for j, line in enumerate(lines[1:]):
        for i, ch in enumerate(line):
            if ch == '^':
                if lines[j][i] == '|':
                    line[i - 1] = '|'
                    line[i + 1] = '|'
                    splits += 1
            elif ch == '.':
                if lines[j][i] == '|':
                    lines[j + 1][i] = '|'
    
    return splits


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
