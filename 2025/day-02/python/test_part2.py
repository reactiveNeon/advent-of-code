from part2 import solve


def test_part2() -> None:
    expected = 4174379265
    result = solve("inputs/test.txt")
    assert result == expected, f"Expected {expected}, got {result}"
