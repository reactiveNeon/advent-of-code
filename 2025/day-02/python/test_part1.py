from part1 import solve


def test_part1() -> None:
    expected = 1227775554
    result = solve("inputs/test.txt")
    assert result == expected, f"Expected {expected}, got {result}"
