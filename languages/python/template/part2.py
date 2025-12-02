from pathlib import Path


def solve(input_path: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = Path(input_path).read_text().strip().split("\n")

    # TODO: Implement solution
    for line in lines:
        pass

    return 0


def main() -> None:
    result = solve("inputs/input2.txt")
    print(result)


if __name__ == "__main__":
    main()
