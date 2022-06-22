""" https://adventofcode.com/2021/day/3 """

from typing import List
from collections import Counter


def generate_correct_answer():
    with open("/Users/andreavandenhooff/aoc/3/input.txt", "r") as f:
        records = f.readlines()
        records = [record.strip() for record in records]

        print(first_assignment(records))
        print(second_assignment(records))


def first_assignment(records: List[int]) -> int:
    gamma = ""

    for i in range(0, len(records[0])):
        dominant_bit = most_frequent(get_bits_in_nth_position(records, i))
        gamma += dominant_bit

    epsilon = ''.join('1' if bit == '0' else '0' for bit in gamma)
    return int(gamma, 2) * int(epsilon, 2)


def second_assignment(records: List[int]) -> int:
    oxygen = records
    scrubber = records

    i = 0
    while (len(oxygen) > 1):
        dominant_bit = most_frequent(get_bits_in_nth_position(oxygen, i))
        oxygen = [bitstring for bitstring in oxygen if bitstring[i] == dominant_bit]
        i += 1

    j = 0
    while (len(scrubber) > 1):
        sub_bit = least_frequent(get_bits_in_nth_position(scrubber, j))
        scrubber = [bitstring for bitstring in scrubber if bitstring[j] == sub_bit]
        j += 1

    return int(oxygen[0], 2) * int(scrubber[0], 2)


def get_bits_in_nth_position(records: List[str], index: int) -> List:
    return [bitstring[index] for bitstring in records]


def most_frequent(bits: List[str]) -> str:
    counter = Counter(bits)
    return '0' if counter['0'] > counter['1'] else '1'


def least_frequent(bits: List[str]) -> str:
    counter = Counter(bits)
    return '0' if counter['0'] <= counter['1'] else '1'


if __name__ == "__main__":
    generate_correct_answer()
