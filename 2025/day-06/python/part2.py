import math
import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().split("\n")

    M = len(lines)
    N = max(len(line) for line in lines)

    total = 0
    
    nums = []
    skip_col = False
    for j in range(N - 1, -1, -1):
        if skip_col:
            skip_col = False
            continue

        num = 0
        for i in range(0, M - 1):
            try:
                digit = lines[i][j]
            except IndexError:
                digit = ' '

            if digit == ' ':
                continue
            
            num = num * 10 + int(digit)

        nums.append(num)
                
        try:
            poss_op = lines[-1][j]
        except IndexError:
            poss_op = ' '

        if poss_op != ' ':
            if poss_op == '*':
                total += math.prod(nums)
            else:
                total += sum(nums)
                
            nums.clear()
            skip_col = True 
            
    return total


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
