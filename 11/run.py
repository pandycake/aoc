""" https://adventofcode.com/2021/day/11 """

from typing import List
import queue


class Grid:
    def __init__(self, rows: List[List[int]]) -> None:
        self.count = 0
        self.rows = rows
        self.octopuses = self._get_locations()  # dict of (x, y) = energy

    def _get_locations(self) -> dict:
        coordinates = {}
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                coordinates[(i, j)] = self.rows[i][j]

        return coordinates

    def check_all_flashing(self) -> bool:
        return all(x == 0 for x in self.octopuses.values())



def get_neighbours(location: tuple[int, int]) -> List[tuple[int, int]]:
    """ Returns all coordinates of the surrounding octopuses (8 in full grid). """
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if location[0] + i < 0 or location[0] + i > 9 or \
                    location[1] + j < 0 or location[1] + j > 9: # Hardcoded grid size out of laziness
                continue
            else:
                neighbours.append((location[0] + i, location[1] + j))

    neighbours.remove(location) # Current position should not be in the list
    return neighbours




def first_star(rows: List[List[int]]) -> int:
    g = Grid(rows)
    q = queue.Queue()

    for i in range(0, 100):
        g.octopuses = {key: value + 1 for key, value in g.octopuses.items()}
        flashing = {key: value for key, value in g.octopuses.items() if value == 10}
        g.count += len(flashing.keys())

        for octopus in flashing.keys():
            q.put(octopus) # FIFO queue to consider the domino effect of octopuses

        while (q.queue):
            o = q.get()
            neighbours = get_neighbours(o)
            for n in neighbours:
                g.octopuses[n] += 1 # Update all neighbours' energy
                if g.octopuses[n] == 10:
                    g.count += 1 # Current neighbour is flashing, so add it to the queue
                    q.put(n)

        # Reset the values of flashing octopuses 
        g.octopuses = {key: (value if value < 10 else 0) for key, value in g.octopuses.items()}

    return g.count


def second_star(rows: List[List[int]]) -> int:
    g = Grid(rows)
    q = queue.Queue()
    i = 0
    
    while not (g.check_all_flashing()):
        # Update all octopuses + the effect of flashing ones 
        g.octopuses = {key: value + 1 for key, value in g.octopuses.items()}
        flashing = {key: value for key, value in g.octopuses.items() if value == 10}

        for octopus in flashing.keys():
            q.put(octopus)

        while (q.queue):
            o = q.get()
            neighbours = get_neighbours(o)
            for n in neighbours:
                g.octopuses[n] += 1
                if g.octopuses[n] == 10:
                    q.put(n)

        # Reset all flashing octopuses' energy
        g.octopuses = {key: (value if value < 10 else 0) for key, value in g.octopuses.items()}
        i += 1

    return i


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [o.strip() for o in f.readlines()]
        octopuses = []
        for line in lines:
            octopuses.append([int(x) for x in line])
        print('Star 1: ' + str(first_star(octopuses)))
        print('Star 2: ' + str(second_star(octopuses)))
