""" https://adventofcode.com/2021/day/5 """

from typing import List, Tuple
import collections
import numpy as np


class Coordinate:
    __slots__ = ['x', 'y']
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __init__(self, xy: List[int]) -> None:
        self.x = xy[0]
        self.y = xy[1]

    def __str__(self) -> str:
        return(f'({self.x}, {self.y})')

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Pipe:
    __slots__ = ['start', 'end']
    def __init__(self, start: Coordinate, end: Coordinate) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return (f'{self.start} -> {self.end}')

def check_horizontal_pipe(pipe: Pipe) -> bool:
    return pipe.start.y == pipe.end.y


def check_vertical_pipe(pipe: tuple) -> bool:
    return pipe.start.x == pipe.end.x


def get_coverage(pipe: Pipe) -> Tuple[List[Coordinate], List[Coordinate]]:
    straight_coverage = []
    diagonal_coverage = []

    if check_horizontal_pipe(pipe):
        if pipe.start.x < pipe.end.x:
            for i in range(pipe.start.x, pipe.end.x + 1):
                straight_coverage.append(Coordinate([i, pipe.start.y]))
        else:
            for i in range(pipe.end.x, pipe.start.x + 1):
                straight_coverage.append(Coordinate([i, pipe.start.y]))

    elif check_vertical_pipe(pipe):
        if pipe.start.y < pipe.end.y:
            for i in range(pipe.start.y, pipe.end.y + 1):
                straight_coverage.append(Coordinate([pipe.start.x, i]))
        else:
            for i in range(pipe.end.y, pipe.start.y + 1):
                straight_coverage.append(Coordinate([pipe.start.x, i]))
    else:
        diagonal_coverage += get_diagonal_coverage(pipe)
    
    return (straight_coverage, diagonal_coverage)


def get_diagonal_coverage(pipe: Pipe) -> List[Coordinate]:
    coverage = []
    if pipe.start.y < pipe.end.y:
        if pipe.start.x < pipe.end.x:
            j = pipe.start.x
            for i in range(pipe.start.y, pipe.end.y + 1):
                coverage.append(Coordinate([j, i]))
                j += 1
        else:
            j = pipe.start.x
            for i in range(pipe.start.y, pipe.end.y + 1):
                coverage.append(Coordinate([j, i]))
                j -= 1

    else:
        if pipe.start.x < pipe.end.x:
            j = pipe.end.x
            for i in range(pipe.end.y, pipe.start.y + 1):
                coverage.append(Coordinate([j, i]))
                j -= 1
        else:
            j = pipe.end.x
            for i in range(pipe.end.y, pipe.start.y + 1):
                coverage.append(Coordinate([j, i]))
                j += 1

    return coverage


def first_assignment(pipes: List[Pipe]) -> int:
    coverage = []
    for pipe in pipes:
        coverage += get_coverage(pipe)[0]
    duplicates = [item for item, count in collections.Counter(coverage).items() if count > 1]

    return len(duplicates)


def second_assignment(pipes: List[Pipe]) -> int:
    coverage = []
    for pipe in pipes:
        straight_coverage, diagonal_coverage = get_coverage(pipe)
        coverage += straight_coverage
        coverage += diagonal_coverage

    duplicates = [item for item, count in collections.Counter(
        coverage).items() if count > 1]

    return len(duplicates)



def generate_correct_answer():
    with open("input.txt", "r") as f:
        records = f.readlines()
        pipes = []
        for record in records:
            elements = record.strip().split(" ")
            start = Coordinate([int(coordinate) for coordinate in elements[0].split(",")])
            end = Coordinate([int(coordinate) for coordinate in elements[2].split(",")])
            pipes.append(Pipe(start, end))

    print(first_assignment(pipes))
    print(second_assignment(pipes))


if __name__ == "__main__":
    generate_correct_answer()
