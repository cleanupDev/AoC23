from part1 import read_data, get_number_index, symbols
import re
import string
import logging

logging.basicConfig(level=logging.INFO)


def get_star_positions(line: str) -> list:
    result = []
    regex = re.compile(r"\*")
    for m in regex.finditer(line):
        result.append(m.start() + 1)

    return result


def find_valid_stars(
    index: int,
    positions: list[int],
    line: str,
    prev_line: str = "",
    next_line: str = "",
) -> int:
    line = "." + line + "."
    if prev_line:
        prev_line = "." + prev_line + "."
    if next_line:
        next_line = "." + next_line + "."

    prev_line_ind = get_number_index(prev_line)
    line_ind = get_number_index(line)
    next_line_ind = get_number_index(next_line)

    result = 0

    for star in positions:
        print(star)
        valid_items = []
        for item in prev_line_ind:
            if star in range(item[0] - 1, item[1] + 1):
                valid_items.append(prev_line[item[0] : item[1]])
                break

        for item in line_ind:
            if star in range(item[0] - 1, item[1] + 1):
                valid_items.append(line[item[0] : item[1]])
                break

        for item in next_line_ind:
            if star in range(item[0] - 1, item[1] + 1):
                valid_items.append(next_line[item[0] : item[1]])
                break

        print(f"valid_items: {valid_items} for star at index {star} on line {index}")
        if len(valid_items) == 2:
            result += int(valid_items[0]) * int(valid_items[1])
            logging.debug(
                f"{valid_items[0]} * {valid_items[1]} = {result} for star at index {star} on line {index}"
            )

    return result


if __name__ == "__main__":
    data = read_data()

    result = 0

    for i, item in enumerate(data):
        positions = get_star_positions(item)
        print(positions)
        if positions == []:
            continue

        if i == 0:
            current_result = find_valid_stars(i, positions, item, next_line=data[i + 1])
        elif i == len(data) - 1:
            current_result = find_valid_stars(i, positions, item, prev_line=data[i - 1])
        else:
            current_result = find_valid_stars(
                i, positions, item, prev_line=data[i - 1], next_line=data[i + 1]
            )

        result += current_result

        # if i > 3:
        #     break

    print(result)
