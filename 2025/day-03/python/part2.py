from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    result = 0
    for line in lines:
        idxs = [-1]
        
        for k in range(11, -1, -1):
            max_idx = idxs[-1] + 1
            for i in range(max_idx, len(line) - k):
                n = int(line[i])
                if n > int(line[max_idx]):
                    max_idx = i
            idxs.append(max_idx)
            
        num = 0
        for i in range(1, len(idxs)):
            num = num * 10 + int(line[idxs[i]])
            
        result += num
            
    return result


def main() -> None:
    result = solve("inputs/input.txt")
    print(result)


if __name__ == "__main__":
    main()
