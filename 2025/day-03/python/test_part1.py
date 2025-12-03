from part1 import solve


def test_part1() -> None:
    expected = 357
    result = solve("inputs/test1.txt")
    assert result == expected, f"Expected {expected}, got {result}"
