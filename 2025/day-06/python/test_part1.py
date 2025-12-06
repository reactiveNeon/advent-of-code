from part1 import solve


def test_part1() -> None:
    expected = 4277556
    result = solve("inputs/test.txt")
    assert result == expected, f"Expected {expected}, got {result}"
