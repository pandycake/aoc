""" https://adventofcode.com/2021/day/3 """

from typing import List


def generate_correct_answer():
    with open("/Users/andreavandenhooff/aoc/3/input.txt", "r") as f:
        records = f.readlines()
        records = [record.strip() for record in records]
        print(first_assignment(records))
        print(second_assignment(records))


def first_assignment(records: List[str]) -> int:
    bit_count = [[0, 0] for bit in records[0]]

    # Create a list with tuples counting the number of zeros and ones per index of the bit.
    for record in records:
        for i in range(0, len(record)):
            if record[i] == '0':
                bit_count[i][0] += 1
            else:
                bit_count[i][1] += 1

    # Of each tuple, the index of the highest element of the tuple represents the more occurring bit value.
    gamma = ""
    for i in range(0, len(bit_count)):
        gamma += str(bit_count[i].index(max(bit_count[i])))

    epsilon = ''.join('1' if bit == '0' else '0' for bit in gamma)

    return int(gamma, 2) * int(epsilon, 2)


def second_assignment(records: List[str]) -> int:
    # TODO
    return len(records)


if __name__ == "__main__":
    generate_correct_answer()
