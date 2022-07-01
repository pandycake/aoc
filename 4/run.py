""" https://adventofcode.com/2021/day/4 """

from typing import List


class Board:
    def __init__(self, rows: List[List[str]]) -> None:
        self.rows = rows
        self.columns = self._get_columns(rows)

    def _get_columns(self, rows: List[str]) -> List[str]:
        columns = [[] for _ in range(len(self.rows))]
        for i in range(0, len(rows[0])):
            for j in range(0, len(rows)):
                columns[j].append(rows[i][j])

        return columns

    def find_earliest_bingo(self, called_numbers: List[str]) -> int:
        index_of_bingos = []
        for row in (self.rows + self.columns):
            indices = []
            try:
                for number in row:  # Find the indices, in the set called_numbers, of the numbers in current row
                    indices.append(called_numbers.index(number))
                last_number = max(indices)  # Bingo achieved on last index
                index_of_bingos.append(last_number)
            except ValueError:
                continue
        return min(index_of_bingos)

    def print(self) -> None:
        for row in self.rows:
            print(row)

    def get_unmarked_numbers(self, called_numbers: List[str]) -> List[str]:
        all_numbers = []
        for row in self.rows:
            all_numbers += row

        return [int(number) for number in all_numbers if number not in called_numbers]


def calculate_score(board: Board, numbers: List[str]) -> int:
    return sum(board.get_unmarked_numbers(numbers)) * int(numbers[board.index_earliest_bingo])


def get_boards(records: List[str]) -> List[List[str]]:
    boards = []
    for i in range(0, len(records), 6):
        rows = []
        for j in range(0, 5):
            row = [number for number in records[i + j].strip().split(" ")
                   if number != ""]
            rows.append(row)
        board = Board(rows)
        boards.append(board)

    return boards


def first_assignment(numbers: List[str], boards: List[Board]) -> int:
    lowest_index = 100000000
    winning_board = None

    for board in boards:
        board.index_earliest_bingo = board.find_earliest_bingo(numbers)
        if board.index_earliest_bingo < lowest_index:
            lowest_index = board.index_earliest_bingo
            winning_board = board

    return calculate_score(winning_board, numbers[:winning_board.index_earliest_bingo + 1])


def second_assignment(numbers: List[str], boards: List[Board]) -> int:
    """ Copy of first assignment, except finding the board with the highest index
        in the called numbers of their first bingo."""
    lowest_index = 0
    winning_board = None

    for board in boards:
        index_earliest_bingo = board.find_earliest_bingo(numbers)
        if index_earliest_bingo > lowest_index:
            lowest_index = index_earliest_bingo
            winning_board = board

    return calculate_score(winning_board, numbers[:index_earliest_bingo + 1])


def generate_correct_answer():
    with open("input.txt", "r") as f:
        records = f.readlines()
        numbers = records[0].strip().split(",")
        boards = get_boards(records[2:])

    print(first_assignment(numbers, boards))
    print(second_assignment(numbers, boards))


if __name__ == "__main__":
    generate_correct_answer()
