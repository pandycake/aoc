""" https://adventofcode.com/2021/day/9 """


from typing import List, Tuple


class Measurements:
    def __init__(self, points: List[List[int]]) -> None:
        self.points = points
        self.low_points = self._find_low_points()  # Tuples of coordinates

    def _find_low_points(self) -> List[Tuple]:
        lows = []
        for i in range(0, len(self.points)):
            for j in range(0, len(self.points[i])):
                if i == 0 or self._compare_points(self.points[i][j], self.points[i - 1][j]):
                    if i == len(self.points) - 1 or self._compare_points(self.points[i][j], self.points[i + 1][j]):
                        if j == 0 or self._compare_points(self.points[i][j], self.points[i][j - 1]):
                            if j == len(self.points[i]) - 1 or self._compare_points(self.points[i][j], self.points[i][j + 1]):
                                lows.append((i, j))

        return lows

    @staticmethod
    def _compare_points(measurement: int, neighbour: int) -> bool:
        return measurement < neighbour

    def second_star(self) -> int:
        sizes = []

        for low in self.low_points:
            basin_points = set(self._find_basin_points(low))
            sizes.append(len(basin_points))

            # Find all higher locations
        s = sorted(sizes)
        return s[-3] * s[-2] * s[-1]

    def _find_basin_points(self, c: tuple) -> List[tuple]:
        points = [c]
        current_value = self.points[c[0]][c[1]]
        if current_value == 9:
            return []

        # print(f'coordinate: {c}, value: {current_value}')

        if c[0] - 1 >= 0:
            # Check N
            if self._compare_points(current_value, self.points[c[0] - 1][c[1]]):
                points += self._find_basin_points((c[0] - 1, c[1]))

        if c[0] + 1 < len(self.points):
            # Check S
            if self._compare_points(current_value, self.points[c[0] + 1][c[1]]):
                points += self._find_basin_points((c[0] + 1, c[1]))

        if c[1] - 1 >= 0:
            # Check W
            if self._compare_points(current_value, self.points[c[0]][c[1] - 1]):
                points += self._find_basin_points((c[0], c[1] - 1))

        if c[1] + 1 < len(self.points[0]):
            # Check E
            if self._compare_points(current_value, self.points[c[0]][c[1] + 1]):
                points += self._find_basin_points((c[0], c[1] + 1))

        return points


def first_star(m: Measurements) -> int:
    values = [m.points[x[0]][x[1]] for x in m.low_points]
    return sum([x + 1 for x in values])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        measurements = f.readlines()
        points = []
        for row in measurements:
            points.append([int(x) for x in row.strip()])
        m = Measurements(points)
        print('Star 1: ' + str(first_star(m)))
        print('Star 2: ' + str(m.second_star()))
