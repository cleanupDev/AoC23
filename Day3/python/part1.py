from pathlib import Path
import re
import string

symbols = string.punctuation.replace(".", "")

filename: Path = Path(__file__).resolve().parent.parent / "data" / "input.txt"


def read_data(filename: Path = filename) -> list[str]:
    """Read data from file"""
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File not found")
        raise SystemExit


def get_number_index(line: str) -> list[tuple[int, int]]:
    """Get index of numbers in line"""
    regex = re.compile(r"\d+")
    return [m.span() for m in regex.finditer(line)]


def validate_numbers(line: str, prev_line: str = "", next_line: str = ""):
    line = "." + line + "."
    if prev_line:
        prev_line = "." + prev_line + "."
    if next_line:
        next_line = "." + next_line + "."

    ind = get_number_index(line)

    result = 0
    for item in ind:
        is_valid = False

        if prev_line and next_line:
            for i in range(item[0] - 1, item[1] + 1):
                if (
                    (prev_line[i] in symbols)
                    or (line[i] in symbols)
                    or (next_line[i] in symbols)
                ):
                    is_valid = True
                    break

        elif prev_line:
            for i in range(item[0] - 1, item[1] + 1):
                if (prev_line[i] in symbols) or (line[i] in symbols):
                    is_valid = True
                    break

        elif next_line:
            for i in range(item[0] - 1, item[1] + 1):
                if (line[i] in symbols) or (next_line[i] in symbols):
                    is_valid = True
                    break

        if is_valid:
            result += int(line[item[0] : item[1]])

    return result


def part1():
    result = 0
    data = read_data()
    for i, line in enumerate(data):
        if i == 0:
            result += validate_numbers(line, next_line=data[i + 1])
        elif i == len(data) - 1:
            result += validate_numbers(line, prev_line=data[i - 1])
        else:
            result += validate_numbers(
                line, prev_line=data[i - 1], next_line=data[i + 1]
            )

    return result


if __name__ == "__main__":
    print(part1())
