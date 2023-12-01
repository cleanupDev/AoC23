""" AoC Day1
"""
from pathlib import Path

filename: Path = Path(__file__).resolve().parent.parent / "data" / "input.txt"

digit_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def read_data(filename: Path = filename) -> list[str]:
    """Read data from file"""
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File not found")
        raise SystemExit


def find_digit(string: str) -> str:
    """Find the first digit in a string"""
    for char in string:
        if char.isdigit():
            return char
    return "0"


def sum_first_last_digit(line: str) -> int:
    """Sum the first and last digit in a string"""
    return int(find_digit(line) + find_digit(line[::-1]))


def calc_result(data: list[str]) -> int:
    """Sums the two digit numbers of all lines"""
    result = 0
    for line in data:
        result += sum_first_last_digit(line)
    return result


def apply_digit_mapping(line: str, mapping: dict) -> str:
    """Apply digit mapping to string"""
    for key, value in mapping.items():
        line = line.replace(key, key[0] + value + key[-1])  # (╯°□°)╯︵ ┻━┻
    return line


if __name__ == "__main__":
    print(f"Part1: {calc_result(read_data())}")
    print(
        f"Part2: {calc_result([apply_digit_mapping(line, digit_mapping) for line in read_data()])}"
    )
