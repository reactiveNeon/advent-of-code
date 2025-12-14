from collections import defaultdict
import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")
    
    adjs_list = defaultdict(list)

    for line in lines:
        line_parts = line.split(':')
        source = line_parts[0]
        dests = line_parts[1:][0].split()
        
        for dest in dests:
            adjs_list[source].append(dest)
    
    
    def bt(source: str) -> int:
        if source == "out":
            return 1
            
        total = 0
        for adj in adjs_list[source]:
            total += bt(adj)
        
        return total
    
    paths = bt("you")

    return paths


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
