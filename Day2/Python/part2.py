from part1 import read_data, remove_prefix, seperate_items, get_game_cubes


def find_max_cubes(items: list[list[str]]):
    """Returns the max number of cubes for a single game"""

    n_cubes = (get_game_cubes(item) for item in items)
    max_cubes = map(lambda x: max(x), zip(*n_cubes))

    return max_cubes


def calc_power_of_line(items: list[list[str]]) -> int:
    """Calculate the 'power' of a single line"""
    red, green, blue = find_max_cubes(items)
    return red * green * blue


def part2() -> int:
    data = read_data()
    result = 0

    for line in data:
        line = remove_prefix(line)
        items = seperate_items(line)
        power = calc_power_of_line(items)
        result += power

    return result
