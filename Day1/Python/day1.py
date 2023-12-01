""" AoC Day1
"""

from pathlib import Path

filename: Path = Path(__file__).resolve().parent.parent / "data" / "input.txt"


digit_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def read_data(filename: Path = filename) -> list[str]:
    """Read data from file"""
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File not found")
        raise SystemExit


def _find_digit(string: str) -> str:
    """Find the first digit in a string"""
    for char in string:
        if char.isdigit():
            return char
    return "0"


def sum_first_last_digit(string: str) -> int:
    """Sum the first and last digit in a string"""
    return int(_find_digit(string) + _find_digit(string[::-1]))


def calc_result(data: list[str]) -> int:
    """Calculate the result"""
    result = 0
    for line in data:
        result += sum_first_last_digit(line)
    return result

if __name__ == "__main__":
    print(f"Result part1: {calc_result(read_data())}")