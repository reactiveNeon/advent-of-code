import sys
import time
from pathlib import Path

from utils.disjoint_set import DisjointSet
from utils.general import distance


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    num_points = len(lines)
    dists = {}
    
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            x1, y1, z1 = map(int, lines[i].split(','))
            x2, y2, z2 = map(int, lines[j].split(','))
            
            dist = distance((x1, y1, z1), (x2, y2, z2))
            dists[(i, j)] = dist
            
    dps = []  # dist with points
    for (i, j), dist in dists.items():
        dps.append((dist, (i, j)))
        
    dps.sort()
    
    ds = DisjointSet(num_points)
    for _, (i, j) in dps:
        ds.union(i, j)
        if ds.components == 1:
            x1, _, _ = map(int, lines[i].split(','))
            x2, _, _ = map(int, lines[j].split(','))
            return x1 * x2
    
    return -1

def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
