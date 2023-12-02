from pathlib import Path
import re

filename: Path = Path(__file__).resolve().parent.parent / "data" / "input.txt"


def read_data(filename: Path = filename) -> list[str]:
    """Read data from file"""
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File not found")
        raise SystemExit


def remove_prefix(line: str) -> str:
    """Remove prefix from line"""
    index = line.find(":")
    line = line[index + 1 :]
    return line


def seperate_items(line: str) -> list[list[str]]:
    """Seperate items in line"""
    item = line.replace(" ", "").split(";")
    item = [i.split(",") for i in item]
    return item


def get_game_cubes(items: list[str]) -> tuple[int, int, int]:
    """Calculate cubes for a single game / line

    Args:
        items (list[str]): list of items

    Returns:
        tuple[int, int, int]: red, green, blue
    """
    red = 0
    green = 0
    blue = 0

    for item in items:
        number = int(re.findall(r"\d+", item)[0])
        if "red" in item:
            red += number
        elif "green" in item:
            green += number
        elif "blue" in item:
            blue += number

    return red, green, blue


def validate_line(items: list[list[str]]) -> bool:
    """Returns if a game would have been possible

    Args:
        items (list[list[str]]): A single game consisting of sets

    Returns:
        bool: Valid or not
    """
    red_limit, green_limit, blue_limit = 12, 13, 14

    eval_cube_set = (
        lambda x: x[0] <= red_limit and x[1] <= green_limit and x[2] <= blue_limit
    )

    mapping = map(lambda x: eval_cube_set(get_game_cubes(x)), items)

    return all(mapping)


def part1() -> int:
    data = read_data()
    result = 0

    for i, line in enumerate(data):
        line = remove_prefix(line)
        items = seperate_items(line)
        if validate_line(items):
            result += i + 1

    return result
