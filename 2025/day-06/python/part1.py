import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")
 
    ops = lines[-1].split()
    results = [1 if op == '*' else 0 for op in ops]
    
    for line in lines[:-1]:
        nums = map(int, line.split())
        
        for i, num in enumerate(nums):
            op = ops[i]
            
            if op == '*':
                results[i] *= num
            else:
                results[i] += num
                
    total = sum(results)

    return total


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
