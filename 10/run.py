""" https://adventofcode.com/2021/day/10 """


from typing import List
from collections import deque

CHUNKS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

POINTS_INCORRECT = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

POINTS_INCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def find_wrong_chars(lines: List[List[str]]) -> List[str]:
    wrong_chars = []

    for line in lines:
        stack = deque()

        for char in line:
            if char in CHUNKS.keys():  # Opening chars can go on the stack
                stack.append(char)
            else:
                last_char = stack.pop()  # Closing chars should close the last in opening
                if CHUNKS[last_char] != char:
                    wrong_chars.append(char)
                    break  # Find only the first incorrect char

    return wrong_chars


def autocomplete_chunks(lines: List[List[str]]) -> List[str]:
    completion_strings = []
    stack = deque()

    for line in lines:
        correct_line = True
        stack.clear()
        for char in line:
            if char in CHUNKS.keys():  # Opening chars can go on the stack
                stack.append(char)
            else:
                last_char = stack.pop()  # Closing chars should close the last in opening
                if CHUNKS[last_char] != char:
                    correct_line = False
                    break  # Incorrect lines can be skipped

        if correct_line:
            closing_chunks = ""
            while stack:
                last_char = stack.pop()
                closing_chunks += CHUNKS[last_char]
            completion_strings.append(closing_chunks)

    return completion_strings


def calculate_scores(completion_strings: List[str]) -> List[int]:
    scores = []
    for string in completion_strings:
        total = 0
        for char in string:
            total *= 5
            total += POINTS_INCOMPLETE[char]

        scores.append(total)
    return scores


def first_star(navigations: List[List[str]]) -> int:
    wrong_chars = find_wrong_chars(navigations)
    return sum([POINTS_INCORRECT[c]for c in wrong_chars])


def second_star(navigations: List[List[str]]) -> int:
    finishing_chars = autocomplete_chunks(navigations)
    scores = sorted(calculate_scores(finishing_chars))
    return scores[int(len(scores) / 2)]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        navigations = [x.strip() for x in f.readlines()]
        print('Star 1: ' + str(first_star(navigations)))
        print('Star 2: ' + str(second_star(navigations)))
