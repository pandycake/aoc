""" https://adventofcode.com/2021/day/1 """

from typing import List


def compare_measurements(records: List[int]) -> int:
    total = 0
    for i in range(1, len(records)):
        if records[i] > records[i - 1]:
            total += 1

    return total


def calculate_window(records: List[int]) -> int:
    windows = []

    for i in range(0, len(records) - 2):
        windows.append(sum(records[i: i + 3]))

    return windows


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        measurements = f.readlines()
        measurements = [int(m.strip()) for m in measurements]

        print('Star 1: ' + str(compare_measurements(measurements)))

        # Second star requires an altered list:
        windows = calculate_window(measurements)
        print('Star 2: ' + str(compare_measurements(windows)))
