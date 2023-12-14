from pathlib import Path
import re
import string

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


def parse_string(line: str) -> tuple:
    winning_card, card = line.split(" | ")
    winning_card = winning_card.split(" ")
    card = card.replace("  ", " ")
    card = card.removeprefix(" ")
    card = card.removesuffix(" ")
    card = card.split(" ")
    print(card)
    return winning_card, card


def calc_point(winning_card, card) -> tuple:
    result = 0
    for number in winning_card:
        if number in card:
            result += 1

    if result == 1:
        return 1, 1
    elif result == 0:
        return 0, 0
    else:
        points = 1
        for i in range(result - 1):
            points *= 2
        return points, result


def eval_card(data, line, index):
    if index >= len(data):
        return 0, 0
    else:
        yield calc_point(data[index], line)
        return eval_card(data, line, index + 1)


if __name__ == "__main__":
    data = read_data()

    num_scratch_cards = len(data)

    final = 0
    for i, line in enumerate(data):
        line = remove_prefix(line)
        winning_card, card = parse_string(line)
        result, add_cards = calc_point(winning_card, card)
        final += result
        num_scratch_cards += add_cards
        for j in range(add_cards):
            line = data[i + j + 1]
            line = remove_prefix(line)
            winning_card, card = parse_string(line)
            result, add_cards = calc_point(winning_card, card)
            final += result
            num_scratch_cards += add_cards

    print(final, num_scratch_cards)
