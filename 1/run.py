""" https://adventofcode.com/2021/day/1 """

from typing import List


def generate_correct_answer():
    with open("input.txt", "r") as f:
        records = f.readlines()
        records = [record.strip() for record in records]

        print(compare_measurements(records))

        # Second assignment requires an altered list:
        values = calculate_window(values)
        print(compare_measurements(values))


def compare_measurements(records: List[int]) -> int:
    total = 0
    for i in range(1, len(records)):
        if records[i] > records[i - 1]:
            total += 1

    return total


def calculate_window(records: List[int]) -> int:
    records_window = []

    for i in range(0, len(records) - 2):
        records_window.append(sum(records[i: i + 3]))

    return records_window


if __name__ == "__main__":
    generate_correct_answer()
