""" https://adventofcode.com/2021/day/7 """

from typing import List


def first_assignment(numbers: List[int]) -> int:
    # Sounded like a median problem to me.
    mid = numbers[int(len(numbers) / 2)], numbers[int(len(numbers) / 2 + 1)]
    median = int((mid[0] + mid[1]) / 2)

    total = 0
    for nr in numbers:
        difference = median - nr if median > nr else nr - median
        total += difference

    return total

def second_assignment(numbers: List[int]) -> int:
    # Same to the first assignment, except for the mathematical: n(n + 1)/2, instead of n
    fuel_cost = {}
    for median in range(numbers[0], numbers[-1]):
        cost = 0
        for nr in numbers:
            difference = median - nr if median > nr else nr - median
            fuel = difference * (difference + 1) / 2
            cost += fuel
        
        fuel_cost[median] = int(cost)

    return min(fuel_cost, key=fuel_cost.get)


def generate_correct_answer():
    with open("input.txt", "r") as f:
        record = f.read()
        numbers = [int(nr) for nr in record.strip().split(",")]
        numbers.sort()

        print(first_assignment(numbers))
        print(second_assignment(numbers))
    

if __name__ == "__main__":
    generate_correct_answer()