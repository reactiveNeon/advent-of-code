import math
from pathlib import Path


def solve(input_path: str) -> int | float:
    """Solve part 1 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    result = 0
    for line in lines:
        max_idx = 0
        for i in range(len(line) - 1):
            n = int(line[i])
            if n > int(line[max_idx]):
                max_idx = i
                
        second_max_idx = max_idx + 1
        for i in range(max_idx + 1, len(line)):
            n = int(line[i])
            if n > int(line[second_max_idx]):
                second_max_idx = i
            
        print("idx", second_max_idx)
        num = int(line[max_idx]) * 10 + int(line[second_max_idx])
        print(num)
        result += num
            
    return result


def main() -> None:
    result = solve("inputs/input1.txt")
    print(result)


if __name__ == "__main__":
    main()
