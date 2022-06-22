""" https://adventofcode.com/2021/day/2 """

from typing import List

def generate_correct_answer():
    with open("input.txt", "r") as f:
        records = f.readlines()
        print(first_assignment(records))
        print(second_assignment(records))


def first_assignment(records: List[str]) -> int:
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


def second_assignment(records: List[str]) -> int:
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
    generate_correct_answer()