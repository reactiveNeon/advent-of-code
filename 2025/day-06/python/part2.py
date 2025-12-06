from itertools import product
import math
import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    M = len(lines)
    N = 0
    for line in lines:
        N = max(N, len(line))
        
    total = 0
    
    nums = []
    for j in range(N - 1, -1, -1):
        any_digits = False
        num = 0
        for i in range(0, M - 1):
            try:
                if lines[i][j] == ' ':
                    continue
                
                num = num * 10 + int(lines[i][j])
                any_digits = True
            except IndexError:
                pass
        
        if any_digits:
            nums.append(num)
        
        try:
            op = lines[-1][j]
            # print(nums, op)
            if op != ' ':
                if op == '*':
                    total += math.prod(nums)
                else:
                    total += sum(nums)
                nums.clear()
        except IndexError:
            pass
        
    return total
    
    # for line in lines[:-1]:
    #     nums_str = line.split()
        
    #     for i, num_str in enumerate(nums_str):
    #         # if idx is odd then from left, if even then from right
    #         if not (i & 1):
    #             num_str = num_str[::-1]
                
    #         for j, digit in enumerate(num_str):
    #             if len(store[i]) - 1 < j:
    #                 padding_needed = j - len(store[i]) + 1
    #                 padding = [0] * padding_needed
    #                 store[i].extend(padding)
                
    #             store[i][j] = int(store[i][j]) * 10 + int(digit)
                
    # print(store)
    
    # ops = lines[-1].split()
    # for i, op in enumerate(ops):     
    #     if op == '*':
    #         total += math.prod(store[i])
    #     else:
    #         total += sum(store[i])                


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
