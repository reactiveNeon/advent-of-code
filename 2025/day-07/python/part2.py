from functools import cache
import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = list(map(list, Path(input_path).read_text().strip().split("\n")))
    
    init_source_idx = lines[0].index('S')
    
    @cache
    def bt(j, i) -> int:
        if j == len(lines) - 1:
            return 1
        
        if lines[j][i] == '^':
            return bt(j + 1, i - 1) + bt(j + 1, i + 1)
            
        return bt(j + 1, i)
            
    return bt(0, init_source_idx)

def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
