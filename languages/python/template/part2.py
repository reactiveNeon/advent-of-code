import sys
import time
from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    # TODO: Implement solution
    for line in lines:
        pass

    return 0


def main() -> None:
    start = time.perf_counter()
    result = solve("inputs/input.txt")
    elapsed = (time.perf_counter() - start) * 1000
    print(result)
    print(f"Runtime: {elapsed:.2f}ms", file=sys.stderr)


if __name__ == "__main__":
    main()
