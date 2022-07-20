""" https://adventofcode.com/2021/day/2 """

from typing import List


def first_star(records: List[str]) -> int:
    horizontal = 0
    depth = 0

    for record in records:
        value = int(record.split(' ')[1].strip())
        if record.startswith('f'):
            horizontal += value
        elif record.startswith('up'):
            depth -= value
        else:
            depth += value

    return horizontal * depth


def second_star(records: List[str]) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    for record in records:
        value = int(record.split(' ')[1].strip())
        if record.startswith('f'):
            horizontal += value
            depth += aim * value
        elif record.startswith('up'):
            aim -= value
        else:
            aim += value

    return horizontal * depth


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        records = f.readlines()
        print('Star 1: ' + str(first_star(records)))
        print('Star 2: ' + str(second_star(records)))
