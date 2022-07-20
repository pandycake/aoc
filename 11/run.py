""" https://adventofcode.com/2021/day/11 """

from typing import List
import queue


class Grid:
    def __init__(self, rows: List[List[int]]) -> None:
        self.rows = rows
        self.octopuses = self._get_locations()  # = dict
        self.count = 0

    def _get_locations(self) -> dict:
        coordinates = {}
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                coordinates[(i, j)] = self.rows[i][j]

        return coordinates


def get_neighbours(location: tuple[int, int]) -> List[tuple[int, int]]:
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if location[0] + i < 0 or location[1] + j < 0 or location[0] + i > 9 or location[1] + j > 9:
                continue
            else:
                neighbours.append((location[0] + i, location[1] + j))

    neighbours.remove(location)
    return neighbours


def first_star(rows: List[List[int]]) -> int:
    g = Grid(rows)
    q = queue.Queue()

    for i in range(0, 100):
        g.octopuses = {key: value + 1 for key, value in g.octopuses.items()}
        flashing = {key: value for key, value in g.octopuses.items() if value == 10}
        g.count += len(flashing.keys())

        for octopus in flashing.keys():
            q.put(octopus)

        while (q.queue):
            o = q.get()
            neighbours = get_neighbours(o)
            for n in neighbours:
                g.octopuses[n] += 1
                if g.octopuses[n] == 10:
                    g.count += 1
                    q.put(n)

        # reset all flashing octopuses
        g.octopuses = {key: (value if value < 10 else 0)
                       for key, value in g.octopuses.items()}

    return g.count


def check_all_flashing(grid: Grid) -> bool:
    return all(x == 0 for x in grid.octopuses.values())


def second_star(rows: List[List[int]]) -> int:
    g = Grid(rows)
    q = queue.Queue()

    for i in range(0, 100000): # Generic placeholder, to fix
        g.octopuses = {key: value + 1 for key, value in g.octopuses.items()}
        flashing = {key: value for key, value in g.octopuses.items() if value == 10}
        g.count += len(flashing.keys())

        for octopus in flashing.keys():
            q.put(octopus)

        while (q.queue):
            o = q.get()
            neighbours = get_neighbours(o)
            for n in neighbours:
                g.octopuses[n] += 1
                if g.octopuses[n] == 10:
                    g.count += 1
                    q.put(n)

        # reset all flashing octopuses
        g.octopuses = {key: (value if value < 10 else 0) for key, value in g.octopuses.items()}
        if check_all_flashing(g):
            return i + 1

    return -1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [o.strip() for o in f.readlines()]
        octopuses = []
        for line in lines:
            octopuses.append([int(x) for x in line])
        print('Star 1: ' + str(first_star(octopuses)))
        print('Star 2 ' + str(second_star(octopuses)))
