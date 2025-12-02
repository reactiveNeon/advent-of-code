from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    MOD = 100
    curr = 50       # value which dial is pointing
    zero_count = 0
    
    for line in lines:
        direction = line[0]
        rotation = int(line[1:])

        if direction == 'R':
            curr += rotation
            zero_count += curr // MOD
        else:
            if curr == 0:
                zero_count -= 1
            curr -= rotation
            zero_count += curr // -MOD + 1

        curr %= MOD 
    
    return zero_count


def main() -> None:
    result = solve("inputs/input.txt")
    print(result)


if __name__ == "__main__":
    main()
